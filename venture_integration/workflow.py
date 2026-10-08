"""Discovery → Core Venture Record → Project Agent handoff preparation.

No implicit network, Core writes, tool calls, sales or specialist execution.
The Core's append_atomic operation is the only authorized write mechanism.
"""
from __future__ import annotations

import re
from collections.abc import Mapping
from copy import deepcopy

from . import VentureRecordError, prepare_handoff, validate
from .discovery import opportunity_brief


SPECIALIST_ROUTES = {
    "design-web": {
        "target": "designos", "agent": "design-agent-v3",
        "result": "Creative/technical requirements for a licensable WordPress kit; editable assets, exclusions and QA checklist; no design output yet",
    },
    "print-apparel": {
        "target": "illustration-agent", "agent": "illustration-agent",
        "result": "Inventory of two existing original artworks: provenance, rights, master files, print technique constraints and unresolved questions; no transformation or production",
    },
    "metal-fabrication": {
        "target": "engineering", "agent": "software-agent",
        "result": "Catalogue/configuration and costing requirements for representative metalwork products; manual measurement, engineering QA and fabrication gates; no fabrication",
    },
}
REF_RE = re.compile(r"^VOS-[A-Z0-9-]{4,80}$")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,78}[a-z0-9]$")
EVIDENCE_TRANSLATIONS = {
    "hypothesis": "hypothesis",
    "owner_observation": "reported_observation",
    "indirect_market": "reported_indirect_market",
    "customer_statement": "reported_customer_statement",
    "customer_behaviour": "reported_customer_behaviour",
    "paid_transaction": "reported_paid_transaction",
    "contradictory": "reported_contradictory",
    "unknown": "unknown",
}


def prepare_promotion(item: Mapping, *, project_slug: str) -> dict:
    """Create a complete *proposal* from a quick Discovery opportunity.

    Returning this structure never persists it; observed evidence stays marked
    as reported/unverified, and any economic values stay scenario-only.
    """
    if not isinstance(project_slug, str) or not SLUG_RE.fullmatch(project_slug):
        raise VentureRecordError("A valid Core project slug is required")
    brief = opportunity_brief(item)
    ref = brief["opportunity_ref"]
    if not REF_RE.fullmatch(ref):
        raise VentureRecordError("Opportunity reference incompatible with Core Venture Record")
    observations = []
    for index, evidence in enumerate(brief["evidence"], start=1):
        kind = evidence["type"]
        observations.append({
            "id": f"EV-{index:03d}",
            "classification": EVIDENCE_TRANSLATIONS[kind],
            "claim": evidence["claim"],
            "source_type": evidence.get("source_ref") if kind not in {"hypothesis", "unknown"} else None,
            "source_ref": evidence.get("source_ref"),
            "independent_market_validation": False,
            "verification_state": "unverified_report",
        })
    record = {
        "schema_version": "venture_record.v0.1-candidate",
        "venture_ref": ref,
        "name": brief["title"],
        "core_project_slug": project_slug,
        "stage": "exploring",
        "depth": "quick",
        "classification": "internal_opportunity_candidate",
        "vertical": brief["vertical"],
        "buyer_hypothesis": brief["buyer_hypothesis"],
        "problem_hypothesis": brief["problem_hypothesis"],
        "offer_hypothesis": brief["offer_hypothesis"],
        "revenue_model_hypothesis": brief["revenue_model_hypothesis"],
        "channel_hypothesis": brief["channel_hypothesis"],
        "existing_capabilities": deepcopy(brief["existing_capabilities"]),
        "assumptions": deepcopy(brief["assumptions"]),
        "unknowns": deepcopy(brief["unknowns"]),
        "evidence": observations,
        "experiment": {
            "id": f"{ref}-EX-001",
            "status": "not_authorized",
            "question": brief["problem_hypothesis"],
            "minimum_test_proposal": brief["minimum_test_proposal"],
            "success_criteria": None,
            "failure_criteria": None,
            "external_outreach_approved": False,
            "launch_approved": False,
        },
        "economics": {
            "currency": "EUR",
            "revenue": None,
            "contribution_margin": None,
            "assumption_scenario": deepcopy(brief["unit_economics"]),
            "profitability_confirmed": False,
        },
        "gate": {
            "status": "pending",
            "name": "Discovery Quick / review required",
            "ceo_decision": None,
            "approved_action_ref": None,
        },
        "next_action": brief["suggested_next_action"],
        "discovery_origin": {
            "opportunity_ref": ref,
            "source_classification": "draft_input",
            "customer_demand_validated": False,
            "automated_ranking_produced": False,
        },
    }
    return validate(record)


def prepare_project_agent_packet(record: Mapping) -> dict:
    """Construct a message shape compatible with Core prepare_agent_handoff.

    Caller must review and separately invoke Project Agent via authorized Core
    tool. 'prepared_not_executed' is not an agent invocation.
    """
    obj = validate(record)
    route = SPECIALIST_ROUTES.get(obj.get("vertical"))
    if route is None:
        raise VentureRecordError("No safe specialist route for vertical; human triage required")
    core_packet = prepare_handoff(obj, route["target"], route["result"])
    return {
        "project_slug": obj["core_project_slug"],
        "from_agent": "project-agent",
        "to_agent": route["agent"],
        "objective": f"Review {obj['venture_ref']} as a candidate, reduce uncertainty without creating or publishing assets",
        "requested_output": route["result"],
        "context_summary": (
            f"Venture {obj['venture_ref']} is in Discovery; no customer demand or margins "
            "have been validated. All external decisions pending CEO approval."
        ),
        "inputs": [
            {"type": "venture_record_ref", "venture_ref": obj["venture_ref"],
             "project_slug": obj["core_project_slug"], "stage": obj["stage"],
             "source_record_hash": core_packet["source_record_hash"]},
            {"type": "open_questions", "items": deepcopy(obj["unknowns"])},
        ],
        "decisions": [{"status": "pending", "authorizing_external_actions": False}],
        "constraints": [
            "No external outreach, publishing, spending, quoting, purchase or production",
            "No invented customer evidence, margins, source files or IP rights",
            "A prepared handoff does not authorize execution",
        ],
        "acceptance_criteria": [
            "Unknowns and provenance explicitly identified",
            "Specialist requirements prepared, not represented as completed",
            "No external effects or modifications to live creative/production data",
        ],
        "status": "prepared_not_executed",
    }


def prepare_discovery_workflow(item: Mapping, *, project_slug: str) -> dict:
    """Return an independently reviewable handoff + record, zero side effects."""
    record = prepare_promotion(item, project_slug=project_slug)
    packet = prepare_project_agent_packet(record)
    return {
        "workflow_version": "discovery_to_core.v0.1-candidate",
        "status": "prepared_not_persisted",
        "venture_record": record,
        "handoff": packet,
        "write_authorized": False,
        "external_action_authorized": False,
        "next_step": "Review and explicitly invoke an authorized scoped Core write",
    }


def persist_candidate_after_review(
    prepared: Mapping, *, adapter, expected_revision: int,
    expected_digest: str | None, authorized_internal_write: bool = False,
) -> dict:
    """Persist ONLY a candidate snapshot with explicit internal write consent.

    No specialist handoff invocation. Core CAS prevents stale writes.
    """
    if not authorized_internal_write:
        raise VentureRecordError("Explicit authorization to persist candidate is required")
    if not isinstance(prepared, Mapping) or prepared.get("status") != "prepared_not_persisted":
        raise VentureRecordError("Only prepared workflows can be persisted")
    if prepared.get("write_authorized") or prepared.get("external_action_authorized"):
        raise VentureRecordError("Prepared workflow must not authorize external actions")
    record = validate(prepared["venture_record"])
    if record["stage"] != "exploring" or record["gate"]["status"] != "pending":
        raise VentureRecordError("Candidate is not in the safe Explorer state")
    if record["experiment"].get("external_outreach_approved") or record["experiment"].get("launch_approved"):
        raise VentureRecordError("External approvals forbidden in Discovery persistence")
    if adapter.project_slug != record["core_project_slug"]:
        raise VentureRecordError("Adapter/record Core project mismatch")
    return adapter.append_atomic(record, expected_revision=expected_revision,
                                 expected_digest=expected_digest)
