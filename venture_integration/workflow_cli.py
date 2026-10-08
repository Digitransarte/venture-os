"""Generate reviewable Venture Record + Project Agent handoff drafts.

Read-only CLI. Always outputs JSON to stdout. Never connects to Core, sends
agent tasks, stores data, opens a website or authorizes external operations.

Example:
 python -m venture_integration.workflow_cli --input opportunities.json \
   --opportunity-ref VOS-OPP-WEB-001 --project-slug designeo
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from . import VentureRecordError
from .workflow import prepare_discovery_workflow


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare a Venture record and handoff")
    parser.add_argument("--input", required=True)
    parser.add_argument("--opportunity-ref", required=True)
    parser.add_argument("--project-slug", required=True)
    args = parser.parse_args(argv)
    try:
        content = json.loads(Path(args.input).read_text(encoding="utf-8"))
        candidates = content["opportunities"]
        if not isinstance(candidates, list):
            raise VentureRecordError("opportunities must be a list")
        matched = [x for x in candidates
                   if isinstance(x, dict) and x.get("opportunity_ref") == args.opportunity_ref]
        if len(matched) != 1:
            raise VentureRecordError("Opportunity reference must match exactly one entry")
        result = prepare_discovery_workflow(matched[0], project_slug=args.project_slug)
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, VentureRecordError) as exc:
        parser.error(f"Cannot prepare Venture workflow: {exc}")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
