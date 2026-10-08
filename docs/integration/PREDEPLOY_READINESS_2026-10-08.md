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

