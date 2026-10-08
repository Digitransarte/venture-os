"""Venture OS candidate integration primitives. No network calls or side effects.

The Designeo OS Core remains the system of record; a Venture Record is a
versioned payload stored in Core Memory, not a second database.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable, Mapping
from copy import deepcopy
from typing import Any

VALID_STAGES = frozenset({
    "idea", "exploring", "strategy", "validating", "designing",
    "building", "launching", "operating", "learning", "paused", "archived",
})
EXTERNAL_STAGES = frozenset({"launching", "operating"})
REF_PATTERN = re.compile(r"^VOS-[A-Z0-9-]+$")
KIND = "venture_record_snapshot_v01"


class VentureRecordError(ValueError):
    """A contract check or concurrency assumption failed."""


def validate(record: Mapping[str, Any]) -> dict[str, Any]:
    """Validate the minimum contract without upgrading hypotheses to evidence."""
    if not isinstance(record, Mapping):
        raise VentureRecordError("Venture Record must be an object")
    obj = deepcopy(dict(record))
    if obj.get("schema_version") != "venture_record.v0.1-candidate":
        raise VentureRecordError("Unsupported schema version")
    ref = obj.get("venture_ref")
    if not isinstance(ref, str) or not REF_PATTERN.fullmatch(ref):
        raise VentureRecordError("Missing or invalid venture_ref")
    if not isinstance(obj.get("core_project_slug"), str) or not obj["core_project_slug"].strip():
        raise VentureRecordError("core_project_slug is required")
    stage = obj.get("stage")
    if stage not in VALID_STAGES:
        raise VentureRecordError(f"Invalid stage: {stage!r}")
    evidence = obj.get("evidence")
    if not isinstance(evidence, list):
        raise VentureRecordError("evidence must be a list")
    for ev in evidence:
        if not isinstance(ev, dict) or not ev.get("classification") or not ev.get("claim"):
            raise VentureRecordError("Every evidence item needs classification and claim")
        if ev.get("independent_market_validation") is True and not ev.get("source_type"):
            raise VentureRecordError("Market validation requires a source")
    gate = obj.get("gate")
    if not isinstance(gate, dict) or "status" not in gate:
        raise VentureRecordError("Gate status must be explicit")
    experiment = obj.get("experiment")
    if not isinstance(experiment, dict) or "status" not in experiment:
        raise VentureRecordError("Experiment status must be explicit")
    economics = obj.get("economics")
    if not isinstance(economics, dict):
        raise VentureRecordError("Economics must be a separate object")
    for field in ("revenue", "contribution_margin"):
        value = economics.get(field)
        if value is not None and (type(value) not in (float, int) or value < 0 and field == "revenue"):
            raise VentureRecordError(f"{field} must be numeric or null")
    if stage in EXTERNAL_STAGES and not experiment.get("launch_approved"):
        raise VentureRecordError("External/operational stage requires launch_approved")
    if stage in EXTERNAL_STAGES and gate.get("status") != "approved":
        raise VentureRecordError("External/operational stage requires an approved gate")
    return obj


def fingerprint(record: Mapping[str, Any]) -> str:
    payload = json.dumps(validate(record), ensure_ascii=False, sort_keys=True,
                         separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def prepare_handoff(
    record: Mapping[str, Any], target: str, expected_output: str
) -> dict[str, Any]:
    obj = validate(record)
    targets = {"designos", "illustration-agent", "screenprint-os",
               "companyos", "engineering", "software-agent"}
    if target not in targets or not expected_output.strip():
        raise VentureRecordError("Unknown target or missing expected_output")
    return {
        "venture_ref": obj["venture_ref"],
        "source_project": obj["core_project_slug"],
        "target": target,
        "purpose": obj.get("problem_hypothesis"),
        "current_stage": obj["stage"],
        "expected_output": expected_output,
        "constraints": ["Respect specialist data ownership",
                        "Do not publish, quote, procure or produce without authorization"],
        "source_record_hash": fingerprint(obj),
        "status": "prepared_not_executed",
        "external_action_authorized": False,
    }


def extract_snapshots(entries: list[Mapping[str, Any]], venture_ref: str) -> list[dict[str, Any]]:
    """Read-only recovery. Ignores unrelated/malformed Core Memory entries."""
    snapshots = []
    for entry in entries:
        if entry.get("kind") != KIND:
            continue
        try:
            content = json.loads(entry["content"])
            record = validate(content["record"])
            if record["venture_ref"] != venture_ref:
                continue
            if content["digest"] != fingerprint(record):
                raise VentureRecordError("Snapshot digest mismatch")
            revision = content["revision"]
            if type(revision) is not int or revision < 1:
                raise VentureRecordError("Invalid revision")
        except (KeyError, TypeError, json.JSONDecodeError, VentureRecordError):
            continue
        snapshots.append({
            "revision": revision,
            "digest": content["digest"],
            "record": record,
            "memory_id": entry.get("id"),
        })
    snapshots.sort(key=lambda s: (s["revision"], str(s.get("memory_id"))))
    for a, b in zip(snapshots, snapshots[1:]):
        if a["revision"] == b["revision"] and a["digest"] != b["digest"]:
            raise VentureRecordError("Conflicting snapshots at identical revision")
    return snapshots


class VentureCoreJournal:
    """Inject Core callables. This is a non-atomic append-only adapter.

    list_memory(kind, ref) -> Core Memory entries; add_memory(dict) -> entry.
    A process-wide Core-side uniqueness guarantee is required before concurrent
    writers can be enabled.
    """

    def __init__(
        self,
        list_memory: Callable[[str, str], list[Mapping[str, Any]]],
        add_memory: Callable[[dict[str, Any]], Mapping[str, Any]],
    ):
        self._list_memory = list_memory
        self._add_memory = add_memory

    def append(self, record: Mapping[str, Any]) -> dict[str, Any]:
        obj = validate(record)
        ref = obj["venture_ref"]
        history = extract_snapshots(self._list_memory(KIND, ref), ref)
        digest = fingerprint(obj)
        if history and history[-1]["digest"] == digest:
            return {"status": "unchanged", "revision": history[-1]["revision"],
                    "memory_id": history[-1]["memory_id"]}
        revision = history[-1]["revision"] + 1 if history else 1
        snapshot = {"revision": revision, "digest": digest, "record": obj}
        entry = {
            "title": f"{ref} rev{revision:03d}",
            "kind": KIND,
            "content": json.dumps(snapshot, ensure_ascii=False, sort_keys=True),
            "tags": ["venture-os", ref.lower(), f"rev-{revision}"],
        }
        saved = self._add_memory(entry)
        if not saved.get("id"):
            raise VentureRecordError("Core Memory did not confirm record ID")
        return {"status": "created", "revision": revision, "memory_id": saved["id"]}
