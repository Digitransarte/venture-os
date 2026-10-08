"""Venture Discovery Quick CLI. No network and no writes to Core.

Usage:
  python -m venture_integration.discovery_cli --input path/to/opportunities.json
  python -m venture_integration.discovery_cli --input path/to/opportunities.json --format json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import VentureRecordError
from .discovery import compare_briefs


def render_markdown(briefs: list[dict]) -> str:
    rows = ["# Venture Discovery · Quick Radar (candidate)",
            "",
            "Estes registos descrevem hipóteses, não negócios validados ou rentáveis.",
            ""]
    for b in briefs:
        rows.extend([
            f"## {b['title']}",
            f"- Referência: `{b['opportunity_ref']}` · Domínio: `{b['vertical']}`",
            f"- Comprador (hipótese): {b['buyer_hypothesis'] or '**por definir**'}",
            f"- Oferta: {b['offer_hypothesis']}",
            f"- Receita (hipótese): {b['revenue_model_hypothesis']}",
            f"- Evidências de comportamento/pagamento reportadas: {b['reported_buyer_behaviour_or_sales']}",
            f"- Unit economics: **{b['unit_economics']['input_status']}** (não validadas)",
            "- Lacunas:",
        ])
        rows.extend(f"  - {gap}" for gap in b["unknowns"])
        rows.extend([
            f"- Teste mínimo proposto: {b['minimum_test_proposal'] or 'Por definir'}",
            "- Decisão: **pendente de revisão humana**; contactos, gastos e publicações não autorizados.",
            "",
        ])
    rows.append("A ordem apresentada não corresponde a um ranking económico.")
    return "\n".join(rows) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate candidate Venture Discovery briefs")
    parser.add_argument("--input", required=True, help="JSON file with opportunities array")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args(argv)
    try:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        briefs = compare_briefs(data["opportunities"])
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, VentureRecordError) as exc:
        parser.error(f"invalid opportunity dataset: {exc}")
    if args.format == "json":
        print(json.dumps({"schema_version": "discovery_briefs.v0.1",
                          "status": "draft_not_authorized",
                          "opportunities": briefs}, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(briefs), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
