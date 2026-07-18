# Relatório de classificação documental — Venture OS v0.1

## Resultado

Os 25 documentos convertidos foram classificados e copiados sem alterar ou eliminar os ficheiros de `_source_word` e `_converted`.

| Estado final | Quantidade |
| --- | ---: |
| `canonical` | 17 |
| `project-specific` | 3 |
| `reference` | 3 |
| `superseded` | 1 |
| `duplicate` | 1 |
| `uncertain` | 0 |

`uncertain` não foi atribuído como estado final porque todos os documentos receberam uma localização reversível. Isto não elimina os pontos de revisão humana indicados abaixo.

### Maturidade editorial

| Estado editorial | Quantidade |
| --- | ---: |
| `Draft` | 12 |
| `Candidate` | 8 |
| `Reference` | 3 |
| `Superseded` | 1 |
| `Duplicate` | 1 |
| `Approved` | 0 |

Classificação e maturidade são campos distintos no manifesto. Nenhum documento canónico ainda não testado foi promovido a `Approved`.

## Classificação final dos 25 documentos

| Nº | Título | Estado final | Função documental | Caminho definitivo |
| ---: | --- | --- | --- | --- |
| 1 | Venture OS Core — Manual Operacional | canonical | Fundação e princípios | `docs/canonical/system/venture-os-core-manual.md` |
| 2 | Explorer Protocol | canonical | Funcionamento geral do Explorer | `docs/canonical/explorer/explorer-protocol.md` |
| 3 | Knowledge Architecture — proposta inicial | superseded | Arquitetura inicial preservada | `docs/archive/superseded/knowledge-architecture-v0-1-initial.md` |
| 4 | Knowledge Seed — KS-0006 | project-specific | Registo de conhecimento do projeto | `docs/canonical/projects/VOS-EXP-001/knowledge-seed-ks-0006.md` |
| 5 | Opportunity Brief | project-specific | Output preenchido do projeto | `docs/canonical/projects/VOS-EXP-001/opportunity-brief.md` |
| 6 | Explorer Validation Protocol | canonical | Subprotocolo de validação do Explorer | `docs/canonical/explorer/explorer-validation-protocol.md` |
| 7 | CEO Gate — Explorer | canonical | Template reutilizável de decisão | `docs/canonical/templates/ceo-gate-explorer.md` |
| 8 | Research Plan | project-specific | Plano preenchido do projeto | `docs/canonical/projects/VOS-EXP-001/research-plan.md` |
| 9 | Interview Guide | canonical | Guia operacional específico do Explorer | `docs/canonical/explorer/interview-guide.md` |
| 10 | Evidence Register | canonical | Registo de evidência específico do Explorer | `docs/canonical/explorer/evidence-register.md` |
| 11 | Research Participant System (`v.0`) | duplicate | Cópia integral repetida | `docs/archive/duplicates/research-participant-system-v0-duplicate.md` |
| 12 | Global Architecture | reference | Arquitetura organizacional de referência | `docs/reference/global-architecture.md` |
| 13 | Governance Charter | canonical | Autoridade e governação | `docs/canonical/system/governance-charter.md` |
| 14 | Knowledge Architecture (`VOS-KNO-CORE-001`) | reference | Arquitetura de conhecimento atual | `docs/reference/knowledge-architecture.md` |
| 15 | Decision Protocol | canonical | Protocolo operacional de decisão | `docs/canonical/operations/decision-protocol.md` |
| 16 | Reasoning Framework | reference | Princípios transversais de raciocínio | `docs/reference/reasoning-framework.md` |
| 17 | Explorer Reasoning Engine | canonical | Raciocínio operacional especializado | `docs/canonical/explorer/explorer-reasoning-engine.md` |
| 18 | Research Participant System (`v.01`) | canonical | Sistema operacional de participantes | `docs/canonical/explorer/research-participant-system.md` |
| 19 | Explorer Dashboard | canonical | Vista executiva do Explorer | `docs/canonical/explorer/explorer-dashboard.md` |
| 20 | Common Agent Operating Model | canonical | Funcionamento operacional comum dos agentes | `docs/canonical/operations/common-agent-operating-model.md` |
| 21 | v0.1 Scope and Completion Map | canonical | Âmbito e critérios de conclusão | `docs/canonical/system/v0-1-scope-and-completion-map.md` |
| 22 | Agent Function Handbook | canonical | Funções, inputs, outputs e limites | `docs/canonical/operations/agent-function-handbook.md` |
| 23 | Venture Project Record | canonical | Template de registo vivo de projeto | `docs/canonical/templates/venture-project-record.md` |
| 24 | Venture OS Orchestrator | canonical | Coordenação e routing | `docs/canonical/operations/venture-os-orchestrator.md` |
| 25 | Core Output Templates | canonical | Catálogo de templates operacionais | `docs/canonical/templates/core-output-templates.md` |

## Decisões tomadas

### Duplicação 11/18

Os dois Markdown foram novamente comparados e são integralmente idênticos, incluindo tabelas. O documento 18 foi escolhido como cópia canónica porque o nome `_v.01` é coerente com a versão 0.1 declarada no conteúdo. O documento 11, cujo nome termina em `_v.0`, foi copiado para `archive/duplicates` com ligação explícita a `VOS-RPS-EXP-001`.

### Substituição 3/14

O documento 14 é mais desenvolvido: aproximadamente 40 mil caracteres e 201 cabeçalhos, contra cerca de 20 mil caracteres e 83 cabeçalhos no documento 3. Também possui código formal, relações com a Global Architecture e Governance Charter e um modelo mais abrangente.

O documento 14 foi tratado como sucessor e colocado em `reference/knowledge-architecture.md`; o documento 3 foi preservado em `archive/superseded`. Não houve fusão. O documento 3 contém material que merece revisão antes de qualquer consolidação futura, incluindo:

- routing de Knowledge Seeds;
- aplicação explícita ao projeto `VOS-EXP-001`;
- anti-padrões documentais;
- versão mínima operacional;
- próximas evoluções previstas.

### Documentos específicos do projeto

Os documentos 4, 5 e 8 são instâncias preenchidas para `VOS-EXP-001`, não templates genéricos. Foram colocados em `canonical/projects/VOS-EXP-001` com estado `project-specific`.

### Relação entre os protocolos do Explorer

O Explorer Protocol define o funcionamento geral do Explorer. O Explorer Validation Protocol é um subprotocolo ativado quando a tarefa exige validação, sobretudo nos modos Standard e Deep. A política de carregamento reflete esta separação: o primeiro pertence ao contexto do agente; o segundo é ativado por tarefa ou modo.

Interview Guide e Evidence Register permanecem documentos específicos do Explorer na v0.1. Não foram generalizados nem convertidos em documentação global.

### Separação das funções sobrepostas

- Core Manual: fundação, missão e princípios do Venture OS.
- Global Architecture: arquitetura organizacional de referência, não arquitetura de software.
- Common Agent Operating Model: funcionamento operacional comum dos agentes.
- Agent Function Handbook: responsabilidades, inputs, outputs, limites e handoffs por agente.
- Orchestrator: coordenação, interpretação da intenção e routing do trabalho.

Nenhum destes textos foi fundido. A separação é funcional e ainda deve ser testada na operação real.

## Sobreposições ainda não resolvidas

1. O Core Manual continua a repetir conceitos presentes na Global Architecture, no modelo comum de agentes e no handbook.
2. Interview Guide e Evidence Register continuam a conter referências concretas a `VOS-EXP-001`, embora pertençam ao conjunto documental do Explorer.
3. O Explorer Dashboard, Common Agent Operating Model, Scope Map, Agent Function Handbook, Project Record, Orchestrator e Core Output Templates permanecem `Draft`.
4. O Core Output Templates poderá, no futuro, ser dividido em templates individuais; não foi desagregado nesta passagem.

## Decisões finais antes do primeiro commit documental

- A Knowledge Architecture mais recente permanece `reference` e não normativa.
- A Knowledge Architecture inicial permanece `superseded`; os tópicos exclusivos não foram consolidados.
- A fronteira entre Explorer Protocol e Explorer Validation Protocol está definida pela regra de ativação acima.
- Interview Guide e Evidence Register permanecem específicos do Explorer na v0.1.
- Documentos ativos não testados mantêm estado `Draft` ou `Candidate`; nenhum é `Approved`.

## Revisão humana futura

- Avaliar os tópicos exclusivos da Knowledge Architecture inicial apenas numa futura tarefa de consolidação.
- Validar em operação real os documentos `Draft` e `Candidate` antes de qualquer promoção a `Approved`.
- Decidir futuramente se as referências concretas a `VOS-EXP-001` justificam variantes genéricas do Interview Guide e Evidence Register.
- Confirmar se o Governance Charter e Decision Protocol amadurecem de `Candidate` para `Approved` após teste.

## Revisão das tabelas Markdown

Foram auditadas 67 tabelas: 26 no Explorer Dashboard, 15 no Common Agent Operating Model, 9 no Venture Project Record e 17 no Core Output Templates. Todas possuem separador Markdown válido e número consistente de colunas. Não foram encontradas tabelas inválidas e, por isso, nenhum conteúdo ou estrutura foi alterado.

## Recomendações de consolidação futura

1. Criar uma matriz de responsabilidades que compare Core Manual, CAOM, Agent Function Handbook e Orchestrator antes de redigir qualquer consolidação.
2. Produzir versões genéricas dos artefactos de investigação, mantendo separadamente as instâncias de `VOS-EXP-001`.
3. Extrair templates individuais do Core Output Templates apenas quando houver necessidade operacional comprovada.
4. Registar decisões de promoção, substituição ou consolidação em `docs/decisions/`.
5. Só depois de validação em projeto real considerar a fusão ou redução dos documentos sobrepostos.
