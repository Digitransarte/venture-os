# Biblioteca documental do Venture OS v0.1

Esta pasta organiza a documentação da versão 0.1 sem alterar as fontes históricas. A classificação é documental e operacional; não define nem altera a arquitetura de software da aplicação.

## Como ler a biblioteca

- `canonical/` contém os documentos ativos para operar ou controlar a versão 0.1. Os documentos em `canonical/projects/` são canónicos apenas no contexto do projeto indicado.
- `reference/` contém arquitetura e reflexão úteis para interpretar o sistema, mas que não são requisitos operacionais diretos da v0.1.
- `_source_word/` preserva os documentos Word originais e não deve ser editada durante a manutenção desta biblioteca.
- `_converted/` preserva as conversões integrais da primeira passagem. São fontes imutáveis para reconstruir as cópias classificadas.
- `archive/superseded/` conserva versões substituídas; `archive/duplicates/` conserva cópias integralmente repetidas.
- `decisions/` destina-se a futuros registos formais de decisões documentais.
- `canonical-manifest.yaml` é o índice legível por máquina de todos os 25 documentos classificados.

No manifesto, `classification` indica a localização documental (`canonical`, `project-specific`, `reference`, `duplicate` ou `superseded`) e `status` indica maturidade editorial. Os documentos ativos ainda não testados usam `Draft` ou `Candidate`; nenhum está marcado como `Approved`.

## Núcleo operacional da v0.1

O núcleo de controlo e operação é constituído por:

- [Scope and Completion Map](canonical/system/v0-1-scope-and-completion-map.md)
- [Governance Charter](canonical/system/governance-charter.md)
- [Common Agent Operating Model](canonical/operations/common-agent-operating-model.md)
- [Agent Function Handbook](canonical/operations/agent-function-handbook.md)
- [Decision Protocol](canonical/operations/decision-protocol.md)
- [Venture OS Orchestrator](canonical/operations/venture-os-orchestrator.md)
- [Venture Project Record](canonical/templates/venture-project-record.md)
- [Core Output Templates](canonical/templates/core-output-templates.md)
- documentação operacional em [canonical/explorer](canonical/explorer/)

O [Core Manual](canonical/system/venture-os-core-manual.md) preserva a fundação e os princípios. A Global Architecture, Knowledge Architecture e Reasoning Framework ficam em `reference/` como enquadramento, sem serem obrigatórios para executar a primeira versão.

## Projeto piloto

Os documentos preenchidos para `VOS-EXP-001` estão em [canonical/projects/VOS-EXP-001](canonical/projects/VOS-EXP-001/). O seu estatuto `project-specific` evita confundi-los com templates genéricos.

## Como adicionar ou atualizar um documento

1. Preservar o Word original em `_source_word/` e gerar uma conversão integral em `_converted/`.
2. Atualizar `document-inventory.md` e `conversion-report.md` quando a fonte ou a conversão mudar.
3. Escolher explicitamente um estado: `canonical`, `reference`, `project-specific`, `superseded`, `duplicate` ou `uncertain`.
4. Criar uma cópia classificada com o bloco YAML normalizado, sem editar a conversão integral.
5. Atualizar `canonical-manifest.yaml`, incluindo relações e proveniência.
6. Se a nova versão substituir outra, preencher `supersedes`/`superseded_by` e conservar a versão anterior em `archive/superseded/`.
7. Executar os testes documentais antes de aceitar a atualização.

As cópias classificadas são reproduzíveis através de `scripts/build_canonical_docs.py`. Alterações de classificação devem ser feitas conscientemente no mapa desse script e refletidas no relatório.

## Política de carregamento

A futura aplicação deve usar [document-loading.yaml](../config/document-loading.yaml), evitando carregar toda a biblioteca em todos os contextos:

- o Orchestrator recebe apenas Scope Map, Agent Function Handbook, Orchestrator e Venture Project Record por defeito;
- o Explorer Protocol define o funcionamento geral do Explorer;
- o Explorer Validation Protocol é carregado apenas para tarefas de validação e, por defeito, nos modos Standard e Deep;
- Interview Guide e Evidence Register permanecem documentos específicos do Explorer na v0.1;
- documentos de projeto só entram quando o projeto correspondente está ativo;
- referência, duplicados e documentos substituídos nunca entram no carregamento automático global.
