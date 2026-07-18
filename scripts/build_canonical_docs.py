"""Build the classified Venture OS v0.1 documentation library.

The source Markdown files under docs/_converted are read-only inputs. Every
classified copy is recreated deterministically with a small YAML front matter.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONVERTED = DOCS / "_converted"


DOCUMENTS = [
    dict(id="VOS-DOC-001", title="Venture OS Core — Manual Operacional para Criação de Negócios Assistida por IA", code=None, version="0.1", status="canonical", role="fundação e princípios", source="1-venture-os-core-manual-operacional-para-criacao-de-negocios-assistida-por-ia-v-0-1.md", word="1-Venture OS Core-Manual Operacional para Criação de Negócios Assistida por IA_v 0.1.docx", path="canonical/system/venture-os-core-manual.md", supersedes=None, superseded_by=None, project=None, related=["VOS-ARC-CORE-001", "VOS-CAOM-001", "VOS-AFH-001", "VOS-ORC-001"], notes="Documento fundador ativo; sobreposições mantidas para consolidação futura."),
    dict(id="VOS-PRO-EXP", title="Venture OS — Explorer Protocol", code="VOS-PRO-EXP", version="0.2", status="canonical", role="funcionamento geral do Explorer", source="2-venture-os-explorer-protocol-v-0-2.md", word="2-Venture OS — Explorer Protocol_v 0.2.docx", path="canonical/explorer/explorer-protocol.md", supersedes=None, superseded_by=None, project=None, related=["VOS-PRO-EXP-001", "VOS-REA-EXP-001"], notes="Define o funcionamento geral do Explorer e permanece carregado no contexto do agente."),
    dict(id="VOS-DOC-003", title="Venture OS — Knowledge Architecture (proposta inicial)", code=None, version="0.1", status="superseded", role="arquitetura de conhecimento inicial", source="3-venture-os-knowledge-architecture-v-0-1.md", word="3-Venture OS — Knowledge Architecture_v 0.1.docx", path="archive/superseded/knowledge-architecture-v0-1-initial.md", supersedes=None, superseded_by="VOS-KNO-CORE-001", project=None, related=["VOS-KNO-CORE-001"], notes="Substituído pela arquitetura mais desenvolvida; contém tópicos exclusivos a rever antes de qualquer consolidação."),
    dict(id="KS-0006", title="Knowledge Seed — KS-0006", code="KS-0006", version=None, status="project-specific", role="knowledge seed de projeto", source="4-knowledge-seed-ks-0006.md", word="4-Knowledge Seed — KS-0006.docx", path="canonical/projects/VOS-EXP-001/knowledge-seed-ks-0006.md", supersedes=None, superseded_by=None, project="VOS-EXP-001", related=["VOS-EXP-001", "VOS-RES-EXP-001"], notes="Registo específico do projeto; não é template genérico."),
    dict(id="VOS-DOC-005", title="Venture OS — Opportunity Brief", code=None, version="0.1", status="project-specific", role="opportunity brief de projeto", source="5-venture-os-opportunity-brief-v01.md", word="5-Venture OS Opportunity Brief_v01.docx", path="canonical/projects/VOS-EXP-001/opportunity-brief.md", supersedes=None, superseded_by=None, project="VOS-EXP-001", related=["VOS-RES-EXP-001", "VOS-GATE-EXP-001"], notes="Instância preenchida do projeto VOS-EXP-001."),
    dict(id="VOS-PRO-EXP-001", title="Explorer Validation Protocol", code="VOS-PRO-EXP-001", version="0.1", status="canonical", role="subprotocolo de validação do Explorer", source="6-venture-os-explorer-validation-protocol-v0-1.md", word="6-Venture OS-Explorer Validation Protocol_v0.1.docx", path="canonical/explorer/explorer-validation-protocol.md", supersedes=None, superseded_by=None, project=None, related=["VOS-PRO-EXP", "VOS-RES-EXP-001"], notes="Ativado quando é necessária validação, sobretudo nos modos Standard e Deep; não é carregado por defeito com o agente."),
    dict(id="VOS-GATE-EXP-001", title="CEO Gate — Explorer", code="VOS-GATE-EXP-001", version="0.1", status="canonical", role="template de decisão do CEO", source="7-venture-os-ceo-gate-explorer-v0-1.md", word="7-Venture OS-CEO Gate — Explorer_V0.1.docx", path="canonical/templates/ceo-gate-explorer.md", supersedes=None, superseded_by=None, project=None, related=["VOS-DEC-CORE-001", "VOS-EXP-001"], notes="Template reutilizável; os campos de projeto permanecem por preencher."),
    dict(id="VOS-RES-EXP-001", title="Research Plan", code="VOS-RES-EXP-001", version="0.1", status="project-specific", role="plano de investigação de projeto", source="8-venture-os-research-plan-v0-1.md", word="8-Venture OS - Research Plan_v0.1.docx", path="canonical/projects/VOS-EXP-001/research-plan.md", supersedes=None, superseded_by=None, project="VOS-EXP-001", related=["VOS-PRO-EXP-001", "VOS-INT-EXP-001", "VOS-EVR-EXP-001"], notes="Plano preenchido para VOS-EXP-001, não template genérico."),
    dict(id="VOS-INT-EXP-001", title="Interview Guide", code="VOS-INT-EXP-001", version="0.1", status="canonical", role="guia operacional de entrevistas do Explorer", source="9-venture-os-interview-guide-v0-1.md", word="9-Venture OS - Interview Guide_v0.1.docx", path="canonical/explorer/interview-guide.md", supersedes=None, superseded_by=None, project=None, related=["VOS-RES-EXP-001", "VOS-PRO-EXP-001", "VOS-RPS-EXP-001"], notes="Mantido como documento específico do Explorer na v0.1; pode conter referências ao projeto piloto."),
    dict(id="VOS-EVR-EXP-001", title="Evidence Register", code="VOS-EVR-EXP-001", version="0.1", status="canonical", role="registo e controlo de evidência do Explorer", source="10-venture-os-evidence-register-v0-1.md", word="10-Venture OS - Evidence Register_v0.1.docx", path="canonical/explorer/evidence-register.md", supersedes=None, superseded_by=None, project=None, related=["VOS-RES-EXP-001", "VOS-INT-EXP-001", "VOS-GATE-EXP-001"], notes="Mantido como documento específico do Explorer na v0.1; pode conter referências ao projeto piloto."),
    dict(id="VOS-RPS-EXP-001-DUP", title="Research Participant System (duplicado)", code="VOS-RPS-EXP-001", version="0.1", status="duplicate", role="cópia integral duplicada", source="11-venture-os-research-participant-system-v-0.md", word="11-Venture OS - Research Participant System_v.0.docx", path="archive/duplicates/research-participant-system-v0-duplicate.md", supersedes=None, superseded_by=None, project=None, related=["VOS-RPS-EXP-001"], notes="Conteúdo integralmente idêntico à cópia canónica proveniente do documento 18."),
    dict(id="VOS-ARC-CORE-001", title="Global Architecture", code="VOS-ARC-CORE-001", version="0.1", status="reference", role="arquitetura de referência", source="12-venture-os-global-architecture-v-01.md", word="12-Venture OS - Global Architecture_v-01.docx", path="reference/global-architecture.md", supersedes=None, superseded_by=None, project=None, related=["VOS-GOV-CORE-001", "VOS-KNO-CORE-001", "VOS-CAOM-001"], notes="Arquitetura organizacional útil, mas não requisito operacional direto da v0.1."),
    dict(id="VOS-GOV-CORE-001", title="Governance Charter", code="VOS-GOV-CORE-001", version="0.1", status="canonical", role="governação e autoridade", source="13-venture-os-governance-charter-v-01.md", word="13-Venture OS Governance Charter_v.01.docx", path="canonical/system/governance-charter.md", supersedes=None, superseded_by=None, project=None, related=["VOS-ARC-CORE-001", "VOS-DEC-CORE-001"], notes="Regras ativas de autoridade e controlo da versão 0.1."),
    dict(id="VOS-KNO-CORE-001", title="Knowledge Architecture", code="VOS-KNO-CORE-001", version="0.1", status="reference", role="arquitetura de conhecimento de referência", source="14-venture-os-knowledge-architecture-v-01.md", word="14-Venture OS - Knowledge Architecture_v.01.docx", path="reference/knowledge-architecture.md", supersedes="VOS-DOC-003", superseded_by=None, project=None, related=["VOS-ARC-CORE-001", "VOS-GOV-CORE-001"], notes="Substitui a proposta inicial 3; classificada como referência por ser mais abstrata do que o núcleo executável."),
    dict(id="VOS-DEC-CORE-001", title="Decision Protocol", code="VOS-DEC-CORE-001", version="0.1", status="canonical", role="protocolo operacional de decisão", source="15-venture-os-decision-protocol-v-01.md", word="15-Venture OS - Decision Protocol_v.01.docx", path="canonical/operations/decision-protocol.md", supersedes=None, superseded_by=None, project=None, related=["VOS-GOV-CORE-001", "VOS-GATE-EXP-001"], notes="Norma operacional para decisões e gates."),
    dict(id="VOS-REA-CORE-001", title="Reasoning Framework", code="VOS-REA-CORE-001", version="0.1", status="reference", role="framework de raciocínio de referência", source="16-venture-os-reasoning-framework-v-01.md", word="16-Venture OS - Reasoning Framework_v.01.docx", path="reference/reasoning-framework.md", supersedes=None, superseded_by=None, project=None, related=["VOS-DEC-CORE-001", "VOS-REA-EXP-001"], notes="Princípios transversais úteis; a execução do Explorer está no motor especializado."),
    dict(id="VOS-REA-EXP-001", title="Explorer Reasoning Engine", code="VOS-REA-EXP-001", version="0.1", status="canonical", role="motor operacional de raciocínio do Explorer", source="17-venture-os-explorer-reasoning-engine-v-01.md", word="17-Venture OS - Explorer Reasoning Engine_v.01.docx", path="canonical/explorer/explorer-reasoning-engine.md", supersedes=None, superseded_by=None, project=None, related=["VOS-REA-CORE-001", "VOS-PRO-EXP-001"], notes="Especialização operacional do raciocínio para o Explorer."),
    dict(id="VOS-RPS-EXP-001", title="Research Participant System", code="VOS-RPS-EXP-001", version="0.1", status="canonical", role="sistema operacional de participantes", source="18-venture-os-research-participant-system-v-01.md", word="18-Venture OS - Research Participant System_v.01.docx", path="canonical/explorer/research-participant-system.md", supersedes=None, superseded_by=None, project=None, related=["VOS-RPS-EXP-001-DUP", "VOS-INT-EXP-001", "VOS-EVR-EXP-001"], notes="Cópia canónica escolhida por ter nome de versão coerente; conteúdo idêntico ao documento 11."),
    dict(id="VOS-ED-EXP-001", title="Explorer Dashboard v0.1", code="VOS-ED-EXP-001", version="0.1", status="canonical", role="vista executiva do Explorer", source="19-venture-os-explorer-dashboard-v0-1-v-01.md", word="19-Venture OS - Explorer Dashboard v0.1_v.01.docx", path="canonical/explorer/explorer-dashboard.md", supersedes=None, superseded_by=None, project=None, related=["VOS-EVR-EXP-001", "VOS-GATE-EXP-001"], notes="Ativo para v0.1 apesar do estado interno Draft; exige revisão das tabelas e campos de data."),
    dict(id="VOS-CAOM-001", title="Common Agent Operating Model v0.1", code="VOS-CAOM-001", version="0.1", status="canonical", role="funcionamento operacional comum dos agentes", source="20-venture-os-common-agent-operating-model-v0-1.md", word="20-Venture OS - Common Agent Operating Model_v0.1.docx", path="canonical/operations/common-agent-operating-model.md", supersedes=None, superseded_by=None, project=None, related=["VOS-AFH-001", "VOS-ORC-001", "VOS-ARC-CORE-001"], notes="Define o modelo comum; não foi fundido com o handbook ou a arquitetura."),
    dict(id="VOS-SCOPE-001", title="v0.1 Scope and Completion Map", code="VOS-SCOPE-001", version="0.1", status="canonical", role="âmbito e critérios de conclusão da v0.1", source="21-venture-os-v0-1-scope-and-completion-map-v-01.md", word="21.Venture OS - v0.1 Scope and Completion Map_v.01.docx", path="canonical/system/v0-1-scope-and-completion-map.md", supersedes=None, superseded_by=None, project=None, related=["VOS-AFH-001", "VOS-COT-001", "VOS-ORC-001"], notes="Documento essencial de controlo do âmbito da versão 0.1."),
    dict(id="VOS-AFH-001", title="Agent Function Handbook v0.1", code="VOS-AFH-001", version="0.1", status="canonical", role="manual operacional das funções dos agentes", source="22-venture-os-agent-function-handbook-v0-1.md", word="22-Venture OS - Agent Function Handbook_v0.1.docx", path="canonical/operations/agent-function-handbook.md", supersedes=None, superseded_by=None, project=None, related=["VOS-CAOM-001", "VOS-ORC-001"], notes="Documento essencial; descreve funções, inputs, outputs e limites."),
    dict(id="VOS-VPR-001", title="Venture Project Record v0.1", code="VOS-VPR-001", version="0.1", status="canonical", role="template de registo vivo de projeto", source="23-venture-os-venture-project-record-v0-1.md", word="23-Venture OS - Venture Project Record_v0.1.docx", path="canonical/templates/venture-project-record.md", supersedes=None, superseded_by=None, project=None, related=["VOS-ORC-001", "VOS-COT-001"], notes="Template essencial para o estado documental de cada projeto."),
    dict(id="VOS-ORC-001", title="Venture OS Orchestrator v0.1", code="VOS-ORC-001", version="0.1", status="canonical", role="coordenação e routing", source="24-venture-os-venture-os-orchestrator-v0-1.md", word="24-Venture OS -Venture OS Orchestrator_v0.1.docx", path="canonical/operations/venture-os-orchestrator.md", supersedes=None, superseded_by=None, project=None, related=["VOS-CAOM-001", "VOS-AFH-001", "VOS-VPR-001"], notes="Define coordenação documental e routing; não constitui implementação de software."),
    dict(id="VOS-COT-001", title="Core Output Templates v0.1", code="VOS-COT-001", version="0.1", status="canonical", role="catálogo de templates operacionais", source="25-venture-os-core-output-templates-v0-1.md", word="25-Venture OS - Core Output Templates_v0.1.docx", path="canonical/templates/core-output-templates.md", supersedes=None, superseded_by=None, project=None, related=["VOS-VPR-001", "VOS-AFH-001"], notes="Documento essencial; mantém os templates agrupados nesta etapa."),
]


LIFECYCLE = {
    "VOS-DOC-001": "Draft",
    "VOS-PRO-EXP": "Candidate",
    "VOS-DOC-003": "Superseded",
    "KS-0006": "Draft",
    "VOS-DOC-005": "Draft",
    "VOS-PRO-EXP-001": "Draft",
    "VOS-GATE-EXP-001": "Candidate",
    "VOS-RES-EXP-001": "Draft",
    "VOS-INT-EXP-001": "Candidate",
    "VOS-EVR-EXP-001": "Candidate",
    "VOS-RPS-EXP-001-DUP": "Duplicate",
    "VOS-ARC-CORE-001": "Reference",
    "VOS-GOV-CORE-001": "Candidate",
    "VOS-KNO-CORE-001": "Reference",
    "VOS-DEC-CORE-001": "Candidate",
    "VOS-REA-CORE-001": "Reference",
    "VOS-REA-EXP-001": "Candidate",
    "VOS-RPS-EXP-001": "Candidate",
    "VOS-ED-EXP-001": "Draft",
    "VOS-CAOM-001": "Draft",
    "VOS-SCOPE-001": "Draft",
    "VOS-AFH-001": "Draft",
    "VOS-VPR-001": "Draft",
    "VOS-ORC-001": "Draft",
    "VOS-COT-001": "Draft",
}


def scalar(value):
    if value is None:
        return "null"
    if isinstance(value, list):
        return json.dumps(value, ensure_ascii=False)
    return json.dumps(str(value), ensure_ascii=False)


def front_matter(document):
    fields = {
        "title": document["title"],
        "code": document["code"],
        "version": document["version"],
        "status": LIFECYCLE[document["id"]],
        "document_role": document["role"],
        "source_file": document["word"],
        "supersedes": document["supersedes"],
        "superseded_by": document["superseded_by"],
        "project": document["project"],
    }
    return "---\n" + "\n".join(f"{key}: {scalar(value)}" for key, value in fields.items()) + "\n---\n\n"


def write_manifest():
    lines = ["documents:"]
    for document in DOCUMENTS:
        lines.append(f"  - id: {scalar(document['id'])}")
        lines.append(f"    title: {scalar(document['title'])}")
        lines.append(f"    role: {scalar(document['role'])}")
        lines.append(f"    status: {scalar(LIFECYCLE[document['id']])}")
        lines.append(f"    classification: {scalar(document['status'])}")
        for key, source_key in (
            ("canonical_path", "path"), ("source_markdown", "source"),
            ("source_word", "word"), ("supersedes", "supersedes"),
            ("related_documents", "related"), ("project", "project"),
            ("notes", "notes"),
        ):
            value = document[source_key]
            if key in {"canonical_path", "source_markdown"}:
                value = f"docs/{value}" if key == "canonical_path" else f"docs/_converted/{value}"
            lines.append(f"    {key}: {scalar(value)}")
    (DOCS / "canonical-manifest.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    for directory in (
        "canonical/system", "canonical/operations", "canonical/explorer",
        "canonical/templates", "canonical/projects/VOS-EXP-001", "reference",
        "archive/duplicates", "archive/superseded", "decisions",
    ):
        (DOCS / directory).mkdir(parents=True, exist_ok=True)
    for document in DOCUMENTS:
        source = CONVERTED / document["source"]
        destination = DOCS / document["path"]
        if not source.is_file():
            raise FileNotFoundError(source)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(front_matter(document) + source.read_text(encoding="utf-8"), encoding="utf-8")
    write_manifest()


if __name__ == "__main__":
    main()
