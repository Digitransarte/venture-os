# Relatório de conversão Word para Markdown

## Resultado

- 25 ficheiros `.docx` encontrados e convertidos.
- 25 ficheiros Markdown criados em `docs/_converted`.
- 0 erros de abertura ou conversão.
- 0 imagens, caixas de texto, equações, alterações controladas, comentários ativos ou referências de notas de rodapé/finais detetados no corpo dos documentos.
- Os documentos Word originais não foram alterados; os hashes SHA-256 anteriores à conversão estão guardados em `docs/_conversion-metadata.json` e são validados pelos testes.

## Ficheiros convertidos

| Word original | Markdown convertido | Tabelas | Revisão humana prioritária |
| --- | --- | ---: | --- |
| `1-Venture OS Core-Manual Operacional para Criação de Negócios Assistida por IA_v 0.1.docx` | `1-venture-os-core-manual-operacional-para-criacao-de-negocios-assistida-por-ia-v-0-1.md` | 0 | Sim — documento fundador e sobreposições |
| `2-Venture OS — Explorer Protocol_v 0.2.docx` | `2-venture-os-explorer-protocol-v-0-2.md` | 0 | Sim — fronteira com protocolo 6 |
| `3-Venture OS — Knowledge Architecture_v 0.1.docx` | `3-venture-os-knowledge-architecture-v-0-1.md` | 0 | Sim — provável versão anterior de 14 |
| `4-Knowledge Seed — KS-0006.docx` | `4-knowledge-seed-ks-0006.md` | 0 | Sim — conteúdo específico de projeto |
| `5-Venture OS Opportunity Brief_v01.docx` | `5-venture-os-opportunity-brief-v01.md` | 0 | Sim — conteúdo específico de projeto |
| `6-Venture OS-Explorer Validation Protocol_v0.1.docx` | `6-venture-os-explorer-validation-protocol-v0-1.md` | 1 | Sim — tabela e sobreposição com 2 |
| `7-Venture OS-CEO Gate — Explorer_V0.1.docx` | `7-venture-os-ceo-gate-explorer-v0-1.md` | 8 | Sim — template com tabelas/campos |
| `8-Venture OS - Research Plan_v0.1.docx` | `8-venture-os-research-plan-v0-1.md` | 2 | Sim — tabelas e conteúdo de projeto |
| `9-Venture OS - Interview Guide_v0.1.docx` | `9-venture-os-interview-guide-v0-1.md` | 0 | Não prioritária |
| `10-Venture OS - Evidence Register_v0.1.docx` | `10-venture-os-evidence-register-v0-1.md` | 7 | Sim — tabelas de registo |
| `11-Venture OS - Research Participant System_v.0.docx` | `11-venture-os-research-participant-system-v-0.md` | 4 | Sim — duplicado integral de 18 |
| `12-Venture OS - Global Architecture_v-01.docx` | `12-venture-os-global-architecture-v-01.md` | 2 | Não prioritária |
| `13-Venture OS Governance Charter_v.01.docx` | `13-venture-os-governance-charter-v-01.md` | 2 | Não prioritária |
| `14-Venture OS - Knowledge Architecture_v.01.docx` | `14-venture-os-knowledge-architecture-v-01.md` | 0 | Sim — conflito de versão com 3 |
| `15-Venture OS - Decision Protocol_v.01.docx` | `15-venture-os-decision-protocol-v-01.md` | 6 | Sim — tabelas de decisão |
| `16-Venture OS - Reasoning Framework_v.01.docx` | `16-venture-os-reasoning-framework-v-01.md` | 3 | Não prioritária |
| `17-Venture OS - Explorer Reasoning Engine_v.01.docx` | `17-venture-os-explorer-reasoning-engine-v-01.md` | 4 | Não prioritária |
| `18-Venture OS - Research Participant System_v.01.docx` | `18-venture-os-research-participant-system-v-01.md` | 4 | Sim — duplicado integral de 11 |
| `19-Venture OS - Explorer Dashboard v0.1_v.01.docx` | `19-venture-os-explorer-dashboard-v0-1-v-01.md` | 26 | Sim — maior risco de perda visual |
| `20-Venture OS - Common Agent Operating Model_v0.1.docx` | `20-venture-os-common-agent-operating-model-v0-1.md` | 15 | Sim — muitas tabelas e estado Draft |
| `21.Venture OS - v0.1 Scope and Completion Map_v.01.docx` | `21-venture-os-v0-1-scope-and-completion-map-v-01.md` | 0 | Sim — estado Draft e validade temporal |
| `22-Venture OS - Agent Function Handbook_v0.1.docx` | `22-venture-os-agent-function-handbook-v0-1.md` | 1 | Sim — estado Draft e sobreposições |
| `23-Venture OS - Venture Project Record_v0.1.docx` | `23-venture-os-venture-project-record-v0-1.md` | 9 | Sim — template com tabelas/campos |
| `24-Venture OS -Venture OS Orchestrator_v0.1.docx` | `24-venture-os-venture-os-orchestrator-v0-1.md` | 0 | Sim — estado Draft e relações arquiteturais |
| `25-Venture OS - Core Output Templates_v0.1.docx` | `25-venture-os-core-output-templates-v0-1.md` | 17 | Sim — templates e muitas tabelas |

## Perdas e limitações de formatação

- Títulos e subtítulos foram convertidos a partir dos estilos Word `Title`, `Subtitle` e `Heading 1–6`.
- Listas foram preservadas como listas Markdown. A numeração automática usa `1.` em cada item, que é a forma Markdown canónica; o renderizador recalcula a sequência.
- As 111 tabelas foram convertidas para tabelas Markdown. Larguras de coluna, cores, bordas, alinhamento, alturas, células mescladas e paginação do Word não são representáveis de forma equivalente e precisam de revisão visual, sobretudo nos documentos 19, 20 e 25.
- Negrito, itálico, rasurado, citações e blocos identificados por estilo de código foram preservados quando presentes nos runs/estilos Word.
- Hiperligações são preservadas com texto e URL quando expostas pelo modelo `python-docx`.
- Quebras de página, margens, cabeçalhos visuais, rodapés visuais, numeração de páginas e índice automático não têm equivalente direto no Markdown. Não foi encontrado texto significativo em cabeçalhos ou rodapés.
- Não foram detetadas imagens. Se forem acrescentadas futuramente, o conversor extrai-as para `docs/_converted/assets`, mas posiciona-as no final para revisão humana.

## Documentos que precisam de revisão humana

Todos os Markdown devem receber uma leitura final antes de classificação definitiva. As prioridades são:

1. 11 e 18, para resolver a duplicação sem perda.
2. 3 e 14, para estabelecer a sucessão da Knowledge Architecture.
3. 19, 20, 23 e 25, devido à densidade de tabelas/templates.
4. 1, 12, 20, 22 e 24, para reconciliar sobreposições documentais sem alterar a arquitetura de software.
5. 4, 5 e 8, para separar documentação do sistema de registos do projeto `VOS-EXP-001`.

Não foram fundidos, eliminados, renomeados ou movidos conteúdos nesta passagem.
