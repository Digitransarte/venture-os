# Learning OS → Venture Factory · medição de IA (proposta técnica v0.1)

**Estado:** contrato proposto, sem instrumentação instalada no Learning OS e sem consumos históricos faturados importados.  
**Âmbito:** preparar medição de custos em produto real sem copiar matérias, respostas, gravações nem identificadores de menores.

## Observação do código existente (2026-10-17)

Fonte inspecionada apenas em leitura: `/opt/anki-os/apps/anki-os/backend/main.py`.

| Operação | Ponto observado | Fornecedor | Situação |
| --- | --- | --- | --- |
| `card_generation` | fluxo de geração de cartões por fonte (~linha 845) e `/api/decks/{did}/ai/propose` (~1870) | OpenRouter Chat Completions | Resposta é interpretada; não há registo agregado persistente de `usage` identificado nesse fluxo |
| `tutor_feedback` | `POST /api/study/tutor/feedback` (~1749–1828) | OpenRouter Chat Completions | Limite local de 8 pedidos/h por utilizador; processo em memória |
| `audio_transcription` | `POST /api/study/transcribe` (~1833) | OpenRouter Audio Transcriptions | Sem tarifação agregada observada no endpoint; validação de tipo e máximo de 6 MB |

O fluxo de geração de cartões por fonte também limita a **5 gerações/h** por utilizador, num contador em memória. Esses limites são uma proteção local, não um controlo de quota partilhado por múltiplas instâncias, nem representam custos reais medidos.

## O que medir na aplicação sem dados pessoais

Após cada operação externa concluída, produzir **um evento agregado, ou incrementar um contador persistente**, com apenas:

- `month` em YYYY-MM e `app = learning-os`;
- `operation` entre `card_generation`, `tutor_feedback` e `audio_transcription`;
- `provider` e `model` apenas como identificadores técnicos;
- `requests` agregado; `input_tokens` e `output_tokens` se devolvidos pelo fornecedor;
- `cost_eur` apenas quando existir valor reportado, convertido e identificado como custo estimado ou faturado;
- `source_kind`: `provider_dashboard`, `provider_invoice` ou `manual_estimate`.

**Proibido nesta camada:** prompts, matéria escolar, textos de resposta, notas, áudio, transcrições, nomes, contas, alunos, `user_id`, `deck_id`, IPs, emails, `request_id` individual e identificadores de sessão. Não usar `None` como custo zero. A auditoria financeira não pode inferir rentabilidade de amostras incompletas.

## Integração proposta (não implementada)

1. Confirmar o formato das respostas e das métricas de faturação do fornecedor para cada operação; não assumir que transcrição e texto fornecem os mesmos campos.
2. Instrumentar uma única função server-side com allowlist de campos, chamada em casos de sucesso e de erro. Erros registam contagens, sem conteúdo. Não guardar as chamadas individuais.
3. Agregar por mês, operação, fornecedor e modelo dentro da base do **Learning OS**, com limites de retenção e sem chave de aluno.
4. Reconciliar custos em EUR com painel/fatura do fornecedor, preservando `fonte: declarada` versus `verificada` como estados diferentes; restringir permissões de leitura às métricas internas.
5. Expor ao Venture OS só agregados já validados, nunca acesso indiscriminado à base pedagógica. Implementar autenticação de serviço por escopo, histórico de alterações e proteção contra duplicações.
6. Confrontar custos com utilização, satisfação, qualidade dos exercícios, retenção e eventual disposição para pagar antes de decidir uma fase comercial.

## Workspaces

O Venture Workspace **já tem a página `Consumo IA` em branch**, com formulário e importação CSV de agregados estritamente limitados; estes dados residem apenas na sessão da interface e podem ser exportados como JSON de resumos. **Não é um conector de faturação nem mede automaticamente o Learning OS**.

O `Venture Workspace` ainda não está publicado. A integração Core, isolamento de utilizadores, autenticação, backup/restauro e aprovação de operação permanecem gates separados. Não tocar no Learning OS em produção ao validar a interface.

## Validação

- Cálculo de cenários da Viabilidade SaaS em `venture_workspace/economics.py`.
- Contrato de agregados em `venture_workspace/usage_metering.py`.
- Testes automáticos em `tests/test_venture_usage_metering.py`, rejeitando colunas adicionais com dados pessoais e custos desconhecidos apresentados como zero.
- Fonte principal da hipótese de produto: `VF-LEARNING-01`, registada no Designeo OS Core.

**Decisão recomendada:** manter o Learning OS como piloto familiar até instrumentar custos reais, garantir privacidade e testar a continuidade pedagógica. Nunca interpretar sucesso técnico interno como viabilidade comercial.
