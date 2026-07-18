# Inventário documental do Venture OS

Primeira passagem sobre os 25 ficheiros Word de `docs/_source_word`. As categorias, estados e caminhos abaixo são propostas para revisão; nenhum documento foi classificado ou movido para uma pasta definitiva.

Estados usados: **atual** (coerente com o conjunto e utilizável no estado declarado), **referência** (material fundador/template que deve ser preservado), **ultrapassado** (há uma versão posterior ou duplicado mais bem identificado) e **incerto** (rascunho, conteúdo específico de projeto ou conflito que exige decisão humana).

| Ficheiro original | Título identificado | Finalidade / resumo curto | Área do Venture OS | Versão | Categoria proposta | Estado proposto | Caminho Markdown recomendado | Observações ou conflitos |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1-Venture OS Core-Manual Operacional para Criação de Negócios Assistida por IA_v 0.1.docx` | Venture OS Core — Manual Operacional para Criação de Negócios Assistida por IA | Define missão, princípios, agentes, etapas e operação geral do sistema. | Core / operação global | 0.1; em desenvolvimento | Manual fundador | referência | `docs/system/venture-os-core-manual.md` | Antecede e sobrepõe-se parcialmente aos documentos 12–17 e 20–25; requer reconciliação, não substituição automática. |
| `2-Venture OS — Explorer Protocol_v 0.2.docx` | Venture OS — Explorer Protocol | Define missão, limites, processo e output do agente Explorer. | Explorer | 0.2; piloto | Protocolo de agente | atual | `docs/explorer/explorer-protocol.md` | Relaciona-se com 5–11 e 17–19; possível sobreposição de processo com o Explorer Validation Protocol (6). |
| `3-Venture OS — Knowledge Architecture_v 0.1.docx` | Venture OS — Knowledge Architecture | Proposta inicial para criação, circulação e reutilização de conhecimento. | Core / conhecimento | 0.1; proposta operacional | Arquitetura de conhecimento | ultrapassado | `docs/system/knowledge-architecture-legacy-v0-1.md` | Mesmo título/versão que 14, mas muito menos extenso e sem código VOS-KNO-CORE-001; provável antecessor. |
| `4-Knowledge Seed — KS-0006.docx` | Knowledge Seed — KS-0006 | Regista uma ideia de ferramenta para empreendedores no website da Designeo. | Projeto VOS-EXP-001 / conhecimento | não indicada; capturada, não avaliada | Registo de projeto | incerto | `docs/explorer/projects/vos-exp-001/knowledge-seed-ks-0006.md` | Conteúdo específico de projeto, relacionado com 5 e 8; não é documentação normativa do sistema. |
| `5-Venture OS Opportunity Brief_v01.docx` | Venture OS — Opportunity Brief | Formula e delimita a oportunidade do projeto VOS-EXP-001. | Explorer / projeto | 0.1; em exploração | Output de projeto | incerto | `docs/explorer/projects/vos-exp-001/opportunity-brief.md` | Instância preenchida, não apenas template; alimenta 8 e o CEO Gate (7). |
| `6-Venture OS-Explorer Validation Protocol_v0.1.docx` | Explorer Validation Protocol | Define como investigar e avaliar oportunidades antes da estratégia. | Explorer / validação | 0.1; em desenvolvimento | Protocolo operacional | atual | `docs/explorer/explorer-validation-protocol.md` | Complementa 2, mas há sobreposição de missão/processo; é referência explícita de 8–10. |
| `7-Venture OS-CEO Gate — Explorer_V0.1.docx` | CEO Gate — Explorer | Template de decisão do CEO no fim da exploração. | Explorer / governação | 0.1; pendente de decisão | Template de decisão | referência | `docs/templates/ceo-gate-explorer.md` | Campos por preencher; depende de Opportunity Brief, evidência e matriz de confiança. |
| `8-Venture OS - Research Plan_v0.1.docx` | Research Plan | Plano de investigação do projeto VOS-EXP-001, com hipóteses e critérios. | Explorer / investigação | 0.1; planeado | Plano de projeto | atual | `docs/explorer/projects/vos-exp-001/research-plan.md` | Refere 5 e 6; origina 9–11/18 e 10. |
| `9-Venture OS - Interview Guide_v0.1.docx` | Interview Guide | Guia as entrevistas exploratórias e o consentimento dos participantes. | Explorer / investigação | 0.1; pronto para piloto | Guia de investigação | atual | `docs/explorer/interview-guide.md` | Refere 8 e 6; usado por 10 e 11/18. Pode conter partes genéricas e partes específicas do projeto. |
| `10-Venture OS - Evidence Register_v0.1.docx` | Evidence Register | Define o registo rastreável de evidências do projeto. | Explorer / evidência | 0.1; pronto para piloto | Registo/template de evidência | atual | `docs/explorer/evidence-register.md` | Refere 8, 9 e 6; alimenta Opportunity Brief, Confidence Matrix e CEO Gate. |
| `11-Venture OS - Research Participant System_v.0.docx` | Research Participant System | Define identificação, recrutamento, proteção e acompanhamento de participantes. | Explorer / investigação | Conteúdo indica 0.1; pronto para piloto | Sistema de participantes | ultrapassado | `docs/explorer/research-participant-system-duplicate-v0-1.md` | Conteúdo e tabelas idênticos ao documento 18; o nome `_v.0` é ambíguo. Preservar até decisão humana. |
| `12-Venture OS - Global Architecture_v-01.docx` | Global Architecture | Define a estrutura organizacional, operacional e informacional global. | Core / arquitetura | 0.1; arquitetura fundadora | Arquitetura global | referência | `docs/system/global-architecture.md` | Documento-base de 13–17; sobrepõe partes do manual 1 e não deve ser tratado como arquitetura de software. |
| `13-Venture OS Governance Charter_v.01.docx` | Governance Charter | Define autoridade, responsabilidade, supervisão e controlo do sistema. | Core / governação | 0.1; fundadora — piloto | Carta de governação | atual | `docs/system/governance-charter.md` | Refere 12; base normativa de 14–17. |
| `14-Venture OS - Knowledge Architecture_v.01.docx` | Knowledge Architecture | Define o ciclo completo de criação, classificação, validação e preservação do conhecimento. | Core / conhecimento | 0.1; fundadora — piloto | Arquitetura de conhecimento | atual | `docs/system/knowledge-architecture.md` | Refere 12 e 13; provável sucessor/expansão do documento 3, apesar da mesma versão declarada. |
| `15-Venture OS - Decision Protocol_v.01.docx` | Decision Protocol | Estabelece decisões explícitas, proporcionais, contestáveis e rastreáveis. | Core / decisão | 0.1; fundador — piloto | Protocolo de decisão | atual | `docs/system/decision-protocol.md` | Depende de 12–14; enquadra CEO Gates e decisões materiais. |
| `16-Venture OS - Reasoning Framework_v.01.docx` | Reasoning Framework | Define princípios comuns de análise, hipótese, evidência e incerteza. | Core / raciocínio | 0.1; fundador — piloto | Framework de raciocínio | atual | `docs/system/reasoning-framework.md` | Refere 12–15; base comum do motor especializado 17. |
| `17-Venture OS - Explorer Reasoning Engine_v.01.docx` | Explorer Reasoning Engine | Especializa o raciocínio do Explorer para descobrir e validar oportunidades. | Explorer / raciocínio | 0.1; piloto | Motor de raciocínio de agente | atual | `docs/explorer/explorer-reasoning-engine.md` | Depende de 12–16 e referencia 6, 8, 9, 10 e 11/18. |
| `18-Venture OS - Research Participant System_v.01.docx` | Research Participant System | Define identificação, recrutamento, proteção e acompanhamento de participantes. | Explorer / investigação | 0.1; pronto para piloto | Sistema de participantes | atual | `docs/explorer/research-participant-system.md` | Conteúdo e tabelas idênticos ao 11; nome de versão mais coerente, proposto como cópia corrente. |
| `19-Venture OS - Explorer Dashboard v0.1_v.01.docx` | Explorer Dashboard v0.1 | Especifica a vista executiva do estado, evidência, incerteza e recomendação do Explorer. | Explorer / executivo | 0.1; draft | Dashboard / executive view | incerto | `docs/explorer/explorer-dashboard.md` | 26 tabelas; datas por preencher. Sintetiza outputs do Explorer sem os substituir. |
| `20-Venture OS - Common Agent Operating Model_v0.1.docx` | Common Agent Operating Model v0.1 | Define uma arquitetura operacional comum para todos os agentes. | Core / agentes | 0.1; draft | Modelo operacional | incerto | `docs/system/common-agent-operating-model.md` | Deve ser reconciliado com 1, 12, 13, 16, 22 e 24; ainda em rascunho. |
| `21.Venture OS - v0.1 Scope and Completion Map_v.01.docx` | v0.1 Scope and Completion Map | Delimita o âmbito funcional e os critérios de conclusão da versão 0.1. | Core / planeamento | 0.1; draft | Mapa de âmbito | incerto | `docs/system/v0-1-scope-and-completion-map.md` | Documento de controlo de versão; pode ficar desatualizado à medida que o sistema evolui. |
| `22-Venture OS - Agent Function Handbook_v0.1.docx` | Agent Function Handbook v0.1 | Descreve inputs, funções, outputs, decisões e limites de cada agente. | Core / agentes | 0.1; draft | Manual de agentes | incerto | `docs/system/agent-function-handbook.md` | Complementa 20 e sobrepõe parcialmente o manual 1 e a arquitetura 12. |
| `23-Venture OS - Venture Project Record_v0.1.docx` | Venture Project Record v0.1 | Define o registo vivo e central de cada projeto Venture OS. | Core / registos de projeto | 0.1; draft | Template de registo | incerto | `docs/templates/venture-project-record.md` | Relaciona agentes e documentos; operado pelo CEO/Orchestrator. Contém 9 tabelas. |
| `24-Venture OS -Venture OS Orchestrator_v0.1.docx` | Venture OS Orchestrator v0.1 | Define a camada de entrada, interpretação de intenção e coordenação do trabalho. | Core / orquestração | 0.1; draft | Modelo de orquestração | incerto | `docs/system/venture-os-orchestrator.md` | Depende do modelo de agentes e do Project Record; é descrição documental, não implementação de software. |
| `25-Venture OS - Core Output Templates_v0.1.docx` | Core Output Templates v0.1 | Reúne templates dos principais outputs operacionais da versão 0.1. | Core / templates | 0.1; draft | Catálogo de templates | incerto | `docs/templates/core-output-templates.md` | 17 tabelas; não inclui o Opportunity Brief por já existir separadamente. Potencial duplicação futura com templates individuais. |

## Conflitos prioritários para revisão

1. Documentos 11 e 18: duplicação integral confirmada; decidir qual é canónico sem eliminar o outro nesta fase.
2. Documentos 3 e 14: mesmo tema e versão declarada, mas o 14 é substancialmente mais completo e integrado na arquitetura fundadora.
3. Documentos 1, 12, 20, 22 e 24: sobreposição parcial na descrição do sistema, agentes e operação.
4. Documentos 2 e 6: esclarecer a fronteira entre o protocolo geral do Explorer e o protocolo de validação.
5. Documentos específicos de `VOS-EXP-001` (4, 5 e 8, e parcialmente 9–11/18): decidir se permanecem como exemplos/projeto ou se serão generalizados.

## Classificação final — segunda passagem

Esta tabela complementa o inventário original. Os ficheiros de `_converted` permanecem inalterados; os caminhos abaixo são cópias classificadas.

| Nº | Estado final | Caminho definitivo | Documento canónico relacionado | Duplicação ou substituição |
| ---: | --- | --- | --- | --- |
| 1 | canonical | `docs/canonical/system/venture-os-core-manual.md` | VOS Core Manual | Sobreposição não resolvida com 12, 20, 22 e 24 |
| 2 | canonical | `docs/canonical/explorer/explorer-protocol.md` | `VOS-PRO-EXP` | Complementa 6; não substitui |
| 3 | superseded | `docs/archive/superseded/knowledge-architecture-v0-1-initial.md` | `VOS-KNO-CORE-001` (14) | Substituído por 14; conteúdo exclusivo registado no relatório |
| 4 | project-specific | `docs/canonical/projects/VOS-EXP-001/knowledge-seed-ks-0006.md` | `KS-0006` | Não aplicável |
| 5 | project-specific | `docs/canonical/projects/VOS-EXP-001/opportunity-brief.md` | Opportunity Brief de `VOS-EXP-001` | Não aplicável |
| 6 | canonical | `docs/canonical/explorer/explorer-validation-protocol.md` | `VOS-PRO-EXP-001` | Complementa 2; não substitui |
| 7 | canonical | `docs/canonical/templates/ceo-gate-explorer.md` | `VOS-GATE-EXP-001` | Não aplicável |
| 8 | project-specific | `docs/canonical/projects/VOS-EXP-001/research-plan.md` | `VOS-RES-EXP-001` | Não aplicável |
| 9 | canonical | `docs/canonical/explorer/interview-guide.md` | `VOS-INT-EXP-001` | Possível futura variante genérica/projeto |
| 10 | canonical | `docs/canonical/explorer/evidence-register.md` | `VOS-EVR-EXP-001` | Possível futura variante genérica/projeto |
| 11 | duplicate | `docs/archive/duplicates/research-participant-system-v0-duplicate.md` | `VOS-RPS-EXP-001` (18) | Conteúdo integralmente idêntico a 18 |
| 12 | reference | `docs/reference/global-architecture.md` | `VOS-ARC-CORE-001` | Sobreposição de referência com 1 e 20 |
| 13 | canonical | `docs/canonical/system/governance-charter.md` | `VOS-GOV-CORE-001` | Não aplicável |
| 14 | reference | `docs/reference/knowledge-architecture.md` | `VOS-KNO-CORE-001` | Substitui 3 |
| 15 | canonical | `docs/canonical/operations/decision-protocol.md` | `VOS-DEC-CORE-001` | Não aplicável |
| 16 | reference | `docs/reference/reasoning-framework.md` | `VOS-REA-CORE-001` | Base conceptual de 17 |
| 17 | canonical | `docs/canonical/explorer/explorer-reasoning-engine.md` | `VOS-REA-EXP-001` | Especializa 16; não o substitui |
| 18 | canonical | `docs/canonical/explorer/research-participant-system.md` | `VOS-RPS-EXP-001` | Cópia canónica; equivalente integral a 11 |
| 19 | canonical | `docs/canonical/explorer/explorer-dashboard.md` | `VOS-ED-EXP-001` | Não aplicável |
| 20 | canonical | `docs/canonical/operations/common-agent-operating-model.md` | `VOS-CAOM-001` | Função distinta de 1, 12, 22 e 24 |
| 21 | canonical | `docs/canonical/system/v0-1-scope-and-completion-map.md` | `VOS-SCOPE-001` | Não aplicável |
| 22 | canonical | `docs/canonical/operations/agent-function-handbook.md` | `VOS-AFH-001` | Função distinta de 20 e 24 |
| 23 | canonical | `docs/canonical/templates/venture-project-record.md` | `VOS-VPR-001` | Não aplicável |
| 24 | canonical | `docs/canonical/operations/venture-os-orchestrator.md` | `VOS-ORC-001` | Coordenação/routing; não implementação de software |
| 25 | canonical | `docs/canonical/templates/core-output-templates.md` | `VOS-COT-001` | Pode originar templates individuais no futuro |

## Decisões finais pré-commit

- A Knowledge Architecture 14 mantém classificação `reference`; a Knowledge Architecture 3 mantém `superseded`, sem consolidação dos seus tópicos exclusivos.
- O Explorer Protocol é o protocolo geral do agente. O Explorer Validation Protocol é um subprotocolo ativado por validação, sobretudo nos modos Standard e Deep.
- Interview Guide e Evidence Register permanecem específicos do Explorer na v0.1.
- A maturidade editorial passou a ser distinta da classificação: existem 12 documentos `Draft`, 8 `Candidate`, 3 `Reference`, 1 `Superseded` e 1 `Duplicate`. Não existe nenhum `Approved`.
- A política de carregamento encontra-se em `config/document-loading.yaml` e usa apenas caminhos classificados existentes.
