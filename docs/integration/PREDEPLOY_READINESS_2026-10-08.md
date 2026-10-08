# Designeo Core ↔ Venture OS · Auditoria de pré-instalação

**Data:** 2026-10-08  
**Estado:** HOLD / revisão manual obrigatória  
**Natureza:** observações de leitura e GitHub; nenhuma execução de deploy, backup, migração, aquisição, envio ou mudança de credenciais.

## 1. Observações verificadas

| Área | Verificação | Resultado |
|---|---|---|
| Venture OS source | PR #1 no GitHub | **Merged**, squash commit `2bc04b71c7f108bd2ec62d0f1fa34c2ed607c5d0` |
| Core source | PR #30 | **Open**, head `9dc564e8386766abb8ae00cc9c29d411ca2ec22d`, sem merge |
| CI Core | run #37776626041 | **Success**: testes Core, Docker build, integração HTTP SQLite/PostgreSQL com Venture OS principal |
| Deployment live | Core health API | HTTP 200, Core `0.7.2` |
| Host | Remote Desktop Commander /opt/designeo-os | main, working tree limpa e HEAD local `424b03903828cfa9a1f9843a27ed40e99b4f56ce` na observação |
| Containers live | Docker status observado | Core API, MCP e PostgreSQL saudáveis; túnel ativo; sem alteração executada |
| Backup | varrimento superficial de pastas até 3 níveis sob `/opt` | **NÃO verificada** uma cópia de segurança/restauro do PostgreSQL do Designeo Core; snapshots externos podem existir |
| Core PR review | comentários/reviews inicialmente consultados | Sem revisões antes desta auditoria; comentário técnico com os bloqueadores submetido à PR |
| PR merge | tentativa via conector | BLOQUEADA por verificação de segurança; não contornar |
| Venture runtime | app registada | **inativa**, sem URL e sem deployment |
| Pilot | Noetic Ink Core Project | não criado na instância live; registo histórico de teste permanece no projeto Designeo |

## 2. Divergência Git a resolver

Comparação `main...feature/venture-record-atomic-core-v01` indicou `ahead_by=29`, `behind_by=3`, com merge base `217f81cdbd865b706e8bf95f8b0a6d8d8ca61183`. Os três commits novos da `main` afetam `app/illustration_control.py`, `docs/ADR-001_CONTROL_SURFACE_RUNTIME.md` e `docs/ILLUSTRATION_AGENT_CONTROL_SURFACE.md`. Não foi identificada sobreposição de nomes de ficheiro na comparação, mas é necessário reconciliar e executar CI contra a `main` atual antes de integrar.

O commit instalado observado no host (`424b...`) não foi resolvido pelo comparador GitHub (HTTP 404). Isto **não prova corrupção nem perda de dados**; pode indicar commit não publicado, branch/repositório diferente, permissões ou histórico ainda não sincronizado. Antes de correr `git pull`, confirmar a origem do commit e os deltas de código/infraestrutura a aplicar. Uma cópia local com working tree limpa **não significa** que a versão coincida com o GitHub.

## 3. Observação do Builder que altera o plano de rollback

O worker de deployment existente (fonte `ops/builder_worker.py`) executa, quando existe uma ação de deployment aprovada:
- `git fetch --prune origin <branch>`;
- `git checkout <branch>`;
- `git pull --ff-only origin <branch>`;
- `docker compose ... up -d --build`, seguido de health check.

A API Builder aceita somente `ref` igual à branch registada. **Não oferece hoje um rollback por SHA antigo**. Antes da ativação:
- identificar o exato commit de produção, a imagem em funcionamento e plano para restaurar código/imagem;
- obter/restaurar backup numa base efémera e comprovar que o teste não toca nas bases reais;
- documentar como se repõe um commit/imagem anterior com pessoa autorizada se um deploy de `main` falhar;
- confirmar que scripts de arranque não fazem migração destrutiva, que volumes persistem e que instalações existentes não são afetadas.

Não dar como garantido que reexecutar o Builder reconstrói a versão antiga: por defeito, volta a instalar a `main` mais recente.

## 4. Gates obrigatórios antes de ativar Venture OS

1. **Manual GitHub:** manter PR Core #30 aberta até resolver revisão de código e eventual divergência `main`; não contornar bloqueio da ferramenta; fundir apenas por ação humana autorizada.
2. **Git & runtime:** reconciliar HEAD local vs GitHub; confirmar que o Core principal continua saudável e o Builder não possui ações aprovadas inesperadas.
3. **Backup & recuperação:** obter evidência de backup/restauro da BD; definir rollback de aplicação testável e independente do `pull` atual.
4. **Deploy fase 1 / default deny:** Core sem tokens Venture provisionados; verificar 401/403 de acesso e endpoints legacy anteriores.
5. **Segredos:** autenticação scoped para serviços internos, nunca tokens globais de administração em clientes ou interfaces.
6. **Projetos próprios:** criar `venture-os` e `noetic-ink` no Core após deploy aprovado, de forma idempotente e verificando conflitos.
7. **Dados:** migrar registo Noetic com proveniência verificada e sem eliminar o histórico original; explorar 3 domínios, não lançar produtos ainda.
8. **Handoffs:** Project Agent/Design/Illustration/CompanyOS só podem executar com fontes reais, critérios técnicos e gate independente; nada de publicar, vender ou fabricar automaticamente.

## 5. Ação seguinte executável por humano autorizado

Abrir [Core PR #30](https://github.com/Digitransarte/designeo-os/pull/30), ler o comentário de revisão, reconciliar com a `main` atual e confirmar CI; só então realizar o merge pela UI, se aprovado. A seguir, seguir o [Runbook de release v0.4](RELEASE_RUNBOOK_V04.md), **com os ajustes de rollback acima**.

A biblioteca [Venture OS](https://github.com/Digitransarte/venture-os) está integrada em `main` mas não disponibilizada como serviço. A capacidade de Discovery permanece utilizável via código/CLI em ambiente de desenvolvimento, sem clientes externos.

## 6. Atualização após restabelecer Remote Desktop (2026-10-08)

**Backup e ensaio de restauro local: PASS.** Foi produzido um `pg_dump` em formato custom, guardado com permissões restritas no servidor; a leitura do arquivo e o restauro integral numa instância PostgreSQL 17 temporária, sem ligação à rede, concluíram sem erros. Verificaram-se 10 tabelas na origem e 10 no destino. O contentor temporário foi eliminado, sem alterar a base original. **Ainda não existe aqui prova de backup fora do servidor.** Não incluir ficheiros da BD ou credenciais em GitHub/CI.

**Situação real do checkout:** o servidor mudou entretanto para `main` local em `820aa040...`, com working tree limpa. A `main` publicada no GitHub era `be4f677b...` na verificação. O checkout do servidor tem **37 commits locais adicionais**, incluindo trabalho de Control Board e Illustration Agent. A comparação por nomes mostra **4 ficheiros sobrepostos** com a PR Core #30: `app/config.py`, `app/main.py`, `app/mcp_server.py` e `tests/test_mcp_discovery.py`.

Por isso, a hipótese anterior de uma integração sem conflitos relevantes deixou de ser válida. É necessário:
1. Preservar e rever todos os commits locais do servidor sem eliminar trabalho em curso.
2. Reconciliar o trabalho do Core, Control Board e Illustration Agent numa branch de integração sujeita a review.
3. Voltar a executar testes do Core, CI Docker, isolamento por projeto e E2E SQLite/PostgreSQL no estado reconciliado.
4. Só depois rever o merge da PR #30 na UI autorizada, respeitando o bloqueio prévio do conector.
5. Confirmar backup externo e rollback de aplicação independente de `git pull main` antes do deploy.

**Estado do Gate:** código Venture OS integrado, Core candidate CI historicamente verde, restore local confirmado, mas **merge e deploy suspensos** por divergência significativa do repositório do servidor. Não ativar Venture OS nem alterar projetos clientes.

## 7. Reconciliação dos dois conflitos (preview não persistido em Git)

Em 2026-10-08, numa cópia isolada do código do servidor (commit de referência `73ac21674482718af9bd0cf263af773f5c49490f`), foi executado um ensaio de `git merge-tree --write-tree` com a PR Core #30 (`9dc564e8386766abb8ae00cc9c29d411ca2ec22d`). Este comando não fundiu branches nem alterou o Git operacional.

**Resultado:** dois conflitos de conteúdo, em `app/main.py` e `tests/test_mcp_discovery.py`.

- `app/main.py`: o import da lista de routers deverá incluir **ambos** `agents` (Project Agent presente no servidor) e `venture_records` (PR Core); os `app.include_router` correspondentes já estavam presentes no resultado automático.
- `tests/test_mcp_discovery.py`: o teste deverá incluir `create_project` da PR sem perder ferramentas do servidor (`list_agents`, `get_agent`, `route_agent`, `prepare_agent_handoff`, `get_agent_handoff`, `get_project_agent_context`, `get_illustration_agent_manifest`).
- `app/config.py` e `app/mcp_server.py`: tiveram junção automática pelo Git, mas ainda exigem revisão funcional.

Foi construída uma **pré-visualização não versionada** em `/tmp/venture-core-merge-preview-20261008`, sem `.git`, resolvendo apenas esses conflitos textuais. Passou `python3 -m compileall -q` para a aplicação e os testes; não foram detetados marcadores de conflito remanescentes.

**Limitação da validação:** uma tentativa de executar o teste de arranque do Core contra SQLite num contentor temporário foi **bloqueada pelas verificações de segurança da ferramenta**, e não foi repetida por via alternativa. Logo, **não temos execução de testes funcionais da versão combinada**. O teste anterior de GitHub Actions corresponde à PR não reconciliada, não a esta cópia.

**Próximo passo:** revisão do merge por humano autorizado, preservação dos commits locais de Control Board/Illustration Agent, preparação da integração num ambiente Git legítimo e nova CI integral. Não há autorização para `git push --force`, `git reset --hard`, deploy ou migração de dados.

## 8. Revisão de reconciliação estática — checkpoint isolado atualizado

Uma nova análise foi executada contra o commit *local* `997df41728bc365c4d081a01c43c849a2b2ab879` e a PR #30 em `9dc564e8386766abb8ae00cc9c29d411ca2ec22d`. O servidor continua a receber commits independentes, pelo que **este checkpoint não é a versão definitiva de produção**.

- `git merge-tree --write-tree` voltou a encontrar **dois** conflitos textuais: `app/main.py` e `tests/test_mcp_discovery.py`.
- Num diretório isolado não versionado `/tmp/venture-core-merge-preview-latest-20261008`, foi preservado tanto `agents` como `venture_records` e feita a união dos métodos MCP existentes com `create_project`.
- `python3 -m compileall` terminou sem erros em `app/` e `tests/`; a análise AST confirmou registo único das duas rotas, presença de oito métodos MCP críticos e ausência de marcadores de conflito. O snapshot continha 60 ficheiros Python.
- Sete verificações estáticas adicionais passaram: definição única da política de acesso Venture, implementação única do `create_project`, preservação do handoff de agentes, implementação única do endpoint de revisão, proteção da escrita de memória genérica, autenticação por projeto e dependências de leitura/escrita em endpoints Venture.
- Foi produzido **exclusivamente no servidor** o patch de resolução dos dois conflitos, `/tmp/venture-core-pr30-conflicts-only-20261008.patch` (1 571 bytes; SHA-256 `7a7cd2dd91cceb98f5b9a689896a3fb37950f4c7ae80348b0a0db2064a1ac1d8`) e um manifesto de verificação `/tmp/venture-core-pr30-review-manifest-20261008.txt`. Não contém cópia integral dos 41+ commits inéditos nem foi publicado em GitHub. Os ficheiros `/tmp` podem ser eliminados pelo sistema; não são backups duradouros.

**Limite essencial:** não foram executados testes funcionais ou integração contínua desta combinação; a execução local correspondente foi bloqueada por verificação de segurança e não foi contornada. Não houve novo merge, push, alteração da `main` operacional ou deploy. Antes de produção, uma pessoa autorizada terá de preservar/rever os commits locais, reconciliar numa branch apropriada e executar a CI completa, incluindo HTTP E2E em SQLite e PostgreSQL.


