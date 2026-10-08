"""Plan a Venture Record project migration without altering either Core project.

A migration creates revision 1 in the destination project via its own scoped
Core identity; source memories are retained and only referred to by provenance.
This module performs NO network calls and never approves gates or launches.
"""
from __future__ import annotations

from copy import deepcopy

from . import VentureRecordError, fingerprint, validate


def prepare_project_migration(
    source_record: dict,
    *,
    destination_project_slug: str,
    source_core_memory_id: str,
    source_revision: int | None = None,
) -> dict:
    """Return a new verified candidate record bound to the destination Core project."""
    source = validate(source_record)
    if not isinstance(destination_project_slug, str) or not destination_project_slug:
        raise VentureRecordError("Destination Core project is required")
    if destination_project_slug == source["core_project_slug"]:
        raise VentureRecordError("Cannot migrate to the same Core project")
    if not isinstance(source_core_memory_id, str) or not source_core_memory_id.strip():
        raise VentureRecordError("Source Core memory reference required")
    if source_revision is not None and (type(source_revision) is not int or source_revision < 1):
        raise VentureRecordError("Invalid source revision")
    if source["stage"] in {"launching", "operating"}:
        raise VentureRecordError("Only exploratory/non-operating Ventures can be migrated here")
    gate = source["gate"]
    if gate.get("status") in {"approved", "authorized"} or gate.get("ceo_decision"):
        raise VentureRecordError("Migration cannot copy approval claims")
    experiment = source["experiment"]
    if experiment.get("launch_approved") or experiment.get("external_outreach_approved"):
        raise VentureRecordError("Migration cannot copy authorized external actions")
    result = deepcopy(source)
    result["core_project_slug"] = destination_project_slug
    if "migration_provenance" in result:
        raise VentureRecordError("A record with existing migration provenance needs manual review")
    result["migration_provenance"] = {
        "source_project_slug": source["core_project_slug"],
        "source_core_memory_id": source_core_memory_id,
        "source_revision": source_revision,
        "source_digest": fingerprint(source),
        "migration_method": "new_destination_revision_1",
        "historical_source_preserved": True,
        "ceo_authorization_inferred": False,
    }
    return validate(result)
