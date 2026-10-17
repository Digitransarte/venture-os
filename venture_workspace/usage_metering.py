"""Privacy-minimal AI usage measurement for Venture OS.

Summaries contain *only* month, app, operation, model/provider, aggregate
request/token counts, optional EUR cost, and provenance. No prompts,
transcripts, student IDs, deck IDs, or request-level logs are accepted.
Reports are user-declared until independently reconciled with provider bills.
"""
from __future__ import annotations

import csv
import io
import math
import re
from dataclasses import asdict, dataclass
from decimal import Decimal, InvalidOperation

PERIOD_RE = re.compile(r"^20\d{2}-(0[1-9]|1[0-2])$")
TAG_RE = re.compile(r"^[a-z0-9][a-z0-9/_\-\.]{0,79}$")
OPERATIONS = frozenset({"card_generation", "tutor_feedback", "audio_transcription", "other"})
SOURCES = frozenset({"provider_dashboard", "provider_invoice", "manual_estimate"})
COLUMNS = ("month", "app", "operation", "provider", "model",
           "requests", "input_tokens", "output_tokens", "cost_eur", "source_kind")
MAX_CSV_BYTES = 128_000
MAX_ROWS = 500
DECIMAL_MAX = Decimal("1000000000")


class UsageError(ValueError):
    pass


@dataclass(frozen=True)
class Usage:
    month: str
    app: str
    operation: str
    provider: str
    model: str
    requests: int
    input_tokens: int
    output_tokens: int
    cost_eur: Decimal | None
    source_kind: str

    def as_json(self) -> dict:
        row = asdict(self)
        row["cost_eur"] = str(self.cost_eur) if self.cost_eur is not None else None
        row["reconciled"] = False
        return row


def parse_usage(row: dict) -> Usage:
    """Strictly allowlisted aggregate fields. Do not accept accidental PII fields."""
    if not isinstance(row, dict) or set(row) != set(COLUMNS):
        raise UsageError("Only aggregate usage fields are accepted; personal data is forbidden")
    month = row["month"]
    if not isinstance(month, str) or not PERIOD_RE.fullmatch(month):
        raise UsageError("Invalid YYYY-MM month")
    tokens = (row["app"], row["provider"], row["model"])
    if any(not isinstance(x, str) or not TAG_RE.fullmatch(x) for x in tokens):
        raise UsageError("Invalid application/provider/model tag")
    if row["operation"] not in OPERATIONS or row["source_kind"] not in SOURCES:
        raise UsageError("Invalid operation or provenance")
    nums = []
    for key in ("requests", "input_tokens", "output_tokens"):
        raw = row[key]
        if isinstance(raw, bool) or not isinstance(raw, (int, str)):
            raise UsageError(f"{key} must be an integer")
        if isinstance(raw, str) and not re.fullmatch(r"\d{1,12}", raw):
            raise UsageError(f"{key} must be an integer")
        v = int(raw)
        if v < 0 or v > 10**12:
            raise UsageError(f"{key} out of range")
        nums.append(v)
    cost_raw = row["cost_eur"]
    if cost_raw is None or cost_raw == "":
        cost = None
    else:
        try:
            cost = Decimal(str(cost_raw))
        except (InvalidOperation, ValueError):
            raise UsageError("Invalid cost") from None
        if not cost.is_finite() or not 0 <= cost <= DECIMAL_MAX:
            raise UsageError("Invalid cost")
    if row["source_kind"] == "provider_invoice" and cost is None:
        raise UsageError("Invoice rows must include billed cost")
    return Usage(month, *tokens[:1], row["operation"], *tokens[1:],
                 *nums, cost, row["source_kind"])


def read_aggregates_csv(data: bytes) -> list[Usage]:
    """In-memory import; exact header, bounded size/rows and no raw logs."""
    if not isinstance(data, bytes) or len(data) > MAX_CSV_BYTES:
        raise UsageError("CSV too large (128KB maximum)")
    try:
        content = data.decode("utf-8-sig")
    except UnicodeDecodeError:
        raise UsageError("CSV must be UTF-8") from None
    reader = csv.DictReader(io.StringIO(content))
    if reader.fieldnames is None or set(reader.fieldnames) != set(COLUMNS) or len(reader.fieldnames) != len(COLUMNS):
        raise UsageError("CSV must contain exactly the approved aggregate headers")
    result = []
    for row in reader:
        if len(result) >= MAX_ROWS:
            raise UsageError("Too many usage rows (500 maximum)")
        result.append(parse_usage(row))
    return result


def totals(rows: list[Usage]) -> dict:
    """No zero-filling missing billed costs, and no claim of invoice validation."""
    grouped: dict[tuple[str, str], dict] = {}
    all_requests = 0
    covered_requests = 0
    total_cost = Decimal("0")
    for entry in rows:
        key = (entry.month, entry.operation)
        point = grouped.setdefault(key, {
            "month": entry.month, "operation": entry.operation,
            "requests": 0, "input_tokens": 0, "output_tokens": 0,
            "requests_with_cost": 0, "declared_cost_eur": Decimal("0"),
            "cost_complete": True, "source_kinds": set(),
        })
        point["requests"] += entry.requests
        point["input_tokens"] += entry.input_tokens
        point["output_tokens"] += entry.output_tokens
        point["source_kinds"].add(entry.source_kind)
        all_requests += entry.requests
        if entry.cost_eur is None:
            point["cost_complete"] = False
        else:
            point["requests_with_cost"] += entry.requests
            point["declared_cost_eur"] += entry.cost_eur
            total_cost += entry.cost_eur
            covered_requests += entry.requests
    return {
        "requests": all_requests,
        "requests_with_cost": covered_requests,
        "coverage_percent": 100 * covered_requests / all_requests if all_requests else None,
        "declared_cost_eur": str(total_cost),
        "any_missing_cost": covered_requests != all_requests,
        "reconciled_with_provider": False,
        "by_month_operation": [
            {**{k: v for k, v in obj.items() if k != "source_kinds"},
             "declared_cost_eur": str(obj["declared_cost_eur"]),
             "source_kinds": sorted(obj["source_kinds"])}
            for _, obj in sorted(grouped.items())
        ],
    }
