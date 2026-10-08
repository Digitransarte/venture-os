"""Venture Discovery v0.1: evidence-first business opportunity briefs.

Pure stdlib implementation: no network, no persistence, no autonomous action.
Outputs are decision aids, never proof of demand or authorization to launch.
"""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from collections.abc import Mapping

from . import VentureRecordError

VERTICALS = frozenset({"design-web", "print-apparel", "metal-fabrication", "other"})
EVIDENCE_TYPES = frozenset({
    "hypothesis", "owner_observation", "indirect_market",
    "customer_statement", "customer_behaviour", "paid_transaction",
    "contradictory", "unknown",
})
MONETARY_FIELDS = ("sale_price", "materials_and_fulfilment", "platform_fees",
                   "acquisition_cost", "agent_cost", "human_labour_cost")


def _required_str(data: dict, key: str) -> str:
    val = data.get(key)
    if not isinstance(val, str) or not val.strip():
        raise VentureRecordError(f"{key} requires nonempty text")
    return val.strip()


def _money(raw: object, field: str) -> Decimal | None:
    if raw is None:
        return None
    if isinstance(raw, (bool, list, dict)):
        raise VentureRecordError(f"Invalid monetary value for {field}")
    try:
        val = Decimal(str(raw))
    except (InvalidOperation, ValueError):
        raise VentureRecordError(f"Invalid monetary value for {field}") from None
    if not val.is_finite() or val < 0:
        raise VentureRecordError(f"Invalid monetary value for {field}")
    if val.as_tuple().exponent < -2:
        raise VentureRecordError(f"{field} must use at most two decimal places")
    return val


def unit_economics_preview(inputs: Mapping[str, object]) -> dict:
    """Return a transparent cost scenario, or gaps; never invent missing costs.

    Human labour is opportunity cost, separately visible. All cost values refer
    to one paid order (not acquisition per lead). Excludes taxes and fixed costs.
    """
    if not isinstance(inputs, Mapping):
        raise VentureRecordError("economics must be an object")
    vals = {k: _money(inputs.get(k), k) for k in MONETARY_FIELDS}
    known = {k: str(v.quantize(Decimal(".01"))) if v is not None else None
             for k, v in vals.items()}
    missing = [k for k, v in vals.items() if v is None]
    margin = None
    if not missing:
        price = vals["sale_price"]
        costs = sum((vals[k] for k in MONETARY_FIELDS if k != "sale_price"),
                    Decimal("0"))
        margin = (price - costs).quantize(Decimal(".01"), rounding=ROUND_HALF_UP)
    return {
        "currency": "EUR",
        "input_status": "complete_assumption_scenario" if not missing else "incomplete",
        "known_inputs": known,
        "missing_fields": missing,
        "contribution_after_variable_and_human_costs": str(margin) if margin is not None else None,
        "profitability_confirmed": False,
        "exclusions": ["VAT and income/corporate tax", "fixed overhead and capital expenditure",
                       "returns and contingencies unless included in inputs"],
        "note": "A completed hypothetical scenario does not establish demand, cash profit or actual margins.",
    }


def opportunity_brief(item: Mapping[str, object]) -> dict:
    """Create a comparable Discovery Brief without treating conjectures as data."""
    if not isinstance(item, Mapping):
        raise VentureRecordError("Opportunity must be a mapping")
    obj = deepcopy(dict(item))
    ref = _required_str(obj, "opportunity_ref")
    title = _required_str(obj, "title")
    vertical = _required_str(obj, "vertical")
    if vertical not in VERTICALS:
        raise VentureRecordError(f"Unknown vertical: {vertical}")
    _required_str(obj, "problem_hypothesis")
    _required_str(obj, "offer_hypothesis")
    _required_str(obj, "revenue_model_hypothesis")
    hypotheses = obj.get("assumptions")
    if not isinstance(hypotheses, list) or not all(isinstance(x, str) and x.strip() for x in hypotheses):
        raise VentureRecordError("assumptions must be text list")
    evidence = obj.get("evidence")
    if not isinstance(evidence, list):
        raise VentureRecordError("evidence must be a list")
    counts = {kind: 0 for kind in EVIDENCE_TYPES}
    for record in evidence:
        if not isinstance(record, dict) or record.get("type") not in EVIDENCE_TYPES:
            raise VentureRecordError("Evidence must specify a known type")
        if not isinstance(record.get("claim"), str) or not record["claim"].strip():
            raise VentureRecordError("Evidence requires a claim")
        if record["type"] not in {"hypothesis", "unknown"}:
            if not isinstance(record.get("source_ref"), str) or not record["source_ref"].strip():
                raise VentureRecordError("Evidence requires provenance")
        counts[record["type"]] += 1
    economics = unit_economics_preview(obj.get("economics", {}))
    buyer = obj.get("buyer_hypothesis")
    buyer_known = isinstance(buyer, str) and bool(buyer.strip())
    channel = obj.get("channel_hypothesis")
    channel_known = isinstance(channel, str) and bool(channel.strip())
    proof_count = counts["customer_behaviour"] + counts["paid_transaction"]
    contrary = counts["contradictory"]
    gaps = []
    if not buyer_known:
        gaps.append("Define a specific potential buyer")
    if not channel_known:
        gaps.append("Identify a plausible acquisition channel")
    if proof_count == 0:
        gaps.append("No customer behaviour or paid transactions evidenced")
    if contrary:
        gaps.append("Review contradictory evidence before selecting a test")
    if economics["missing_fields"]:
        gaps.append("Complete a credible cost and human-effort scenario")
    test = obj.get("minimum_test_proposal")
    if not isinstance(test, str) or not test.strip():
        gaps.append("Design a small and measurable test with a stop condition")
    return {
        "opportunity_ref": ref,
        "title": title,
        "vertical": vertical,
        "stage": "discovery_not_validated",
        "buyer_hypothesis": buyer if buyer_known else None,
        "problem_hypothesis": obj["problem_hypothesis"],
        "offer_hypothesis": obj["offer_hypothesis"],
        "revenue_model_hypothesis": obj["revenue_model_hypothesis"],
        "channel_hypothesis": channel if channel_known else None,
        "existing_capabilities": obj.get("existing_capabilities") or [],
        "assumptions": hypotheses,
        "evidence": evidence,
        "evidence_counts": counts,
        "reported_buyer_behaviour_or_sales": proof_count,
        "unit_economics": economics,
        "unknowns": gaps,
        "minimum_test_proposal": test if isinstance(test, str) and test.strip() else None,
        "suggested_next_action": gaps[0] if gaps else "Review evidence and define CEO-authorized experiment",
        "decision_gate": {
            "status": "pending_human_review", "authorized_to_contact_or_publish": False,
            "authorized_to_spend_or_operate": False,
            "launch_recommended": False,
        },
        "quality_flags": [
            "Owner observations confirm capabilities, not customer demand",
            "Evidence types are reported classifications; sources still require independent checking",
            "No relative business ranking is inferred from incomplete or hypothetical evidence",
        ],
    }


def compare_briefs(items: list[Mapping[str, object]]) -> list[dict]:
    """Keep input order: evidence coverage comparison is NOT a profitability rank."""
    if not isinstance(items, list) or not items:
        raise VentureRecordError("Expected a nonempty list of opportunities")
    briefs = [opportunity_brief(item) for item in items]
    refs = [b["opportunity_ref"] for b in briefs]
    if len(set(refs)) != len(refs):
        raise VentureRecordError("Opportunity references must be unique")
    return briefs
