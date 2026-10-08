# Venture OS · Identidade, governação e isolamento de projetos v0.1

**Estado:** Draft, para revisão técnica · 2026-10-08  
**Abrangência:** Designeo OS Core, Venture OS e especialistas  
**Implementação de negócio:** não ativada · **Acesso multi-cliente:** NÃO suportado nesta versão.

## 1. Princípios

Um empreendimento (venture) tem identidade e histórico próprios sem exigir uma base de dados paralela. O **Core Project** é a unidade de continuidade (memórias, tarefas, decisões e refs); o **Venture Record** é uma sequência versionada e verificável dentro desse projeto. Domínios especializados continuam donos dos seus dados operacionais.

Identidades distintas:
- `venture_ref`: código imutável e único da tese/empreendimento (por exemplo `VOS-PILOT-2026-001`).
- `core_project_slug`: identificador de projeto no Core. Um projeto distinto por Venture **operacional ou candidata com vida própria**, quando os seus dados e decisões deixam de ser apenas uma investigação transversal.
- `origin_project_slug`: projeto/empresa que originou a oportunidade; anotação de proveniência, não permissão e não parent com cascatas.
- `domain_external_refs`: referências a DesignOS, Screenprint OS, CompanyOS ou outros sistemas via Core ExternalRefs; não copiar orçamento, artes, inventário, contratos ou dados pessoais.
- `stage` e `gate`: avanço do empreendimento e estado de decisão; estado histórico de aprendizagem não prova automaticamente autorização.

## 2. Modelo de projetos

| Caso | Core Project | Venture Record | Dono de dados de domínio |
|---|---|---|---|
| Exploração geral de oportunidades | projeto Venture OS / Designeo | ideias ainda não operacionalizadas | Core |
| Marca própria em desenvolvimento (Noetic Ink) | projeto próprio `noetic-ink` *proposto* | `VOS-PILOT-2026-001` | DesignOS / Screenprint OS / plataforma de vendas |
| Serviço específico a cliente | projeto de cliente próprio com regras de acesso | opcional, se incluir descoberta de negócio | DesignOS/CompanyOS conforme trabalho |
| Produto digital comercializado | projeto/empreendimento de produto | tese e métricas de venda | catálogo, web ou loja própria |
| Trading/investimento | domínio Investment Agent em circuito separado | **não** tratar como faturação comercial | sistema financeiro com credenciais e riscos próprios |

**Importante:** o projeto `noetic-ink` ainda não foi criado no Core. O primeiro registo de experiência foi guardado historicamente no projeto `designeo`; não apagar nem alterar esse registo silenciosamente.

## 3. Migração de memória candidata (futura)

Após autorização e criação do projeto próprio:
1. Ler a entrada histórica pelo seu ID e comprovar a fonte, evitando importar versões divergentes.
2. Criar um novo registo de revisão **rev1** no novo projeto, com `core_project_slug = noetic-ink` e `migrated_from_core_memory_id` no campo de proveniência.
3. Registar decisão de migração e external ref para a origem; não reescrever nem eliminar histórico em `designeo`.
4. Calcular novo hash porque o projeto faz parte do conteúdo. Isto é uma migração auditável, **não** uma rev2 da mesma cadeia no projeto antigo.
5. Consultas normais passam a ler a revisão autorizada do novo projeto; manter a origem apenas como referência histórica.

Migração **não executada** neste incremento.

## 4. Descoberta e handoffs

Venture OS define intenção comercial, hipótese, critérios de aceitação e evidência. Project Agent coordena contexto, identidade e decisões; os agentes e aplicações especialistas mantêm dados próprios. Handoff `prepared` apenas prepara instruções; não confirma inspeção de artes, produto imprimível ou custo real. Um resultado só entra no Venture Record com referência verificável e avaliação.

No caso Noetic Ink:
- Project Agent → Design Agent v3: inventário de duas artes e direitos (já preparado, sem assets anexados).
- Design Agent v3 → Illustration Agent: pré-impressão e integridade visual (pode ser preparado quando houver duas artes identificadas).
- Illustration Agent → Project Agent: sintetizar ficha técnica e critérios de orçamentação; Project Agent consulta Screenprint OS **somente em modo preview**.
- Project Agent/Venture OS: compara alternativas técnicas, custos completos, margem e procura e prepara CEO Gate.
- Produção, publicação e venda só após aprovação específica.

## 5. Modelo de confiança — lacuna crítica

No Core atual (`app/auth.py`), **um único Bearer token global** autentica todos os pedidos. Logo, `core_project_slug` é um filtro lógico e **não** uma fronteira de autorização para clientes independentes. Um serviço ou agente com esse token pode aceder a outros projetos Core; isto não é aceitável para contas de clientes ou execução não supervisionada.

Política para v0.1:
- Integrar apenas agentes internos de confiança; manter código sem deploy e PRs em Draft até revisão.
- Não divulgar o token global a clientes, plugins externos, browser ou agentes sem confiança.
- Não expor um painel multi-cliente sobre este contrato; não usar os filtros `slug` como substituto de RBAC.
- Antes de serviço comercial a terceiros, conceber autenticação por identidade (pessoa/serviço), autorização por projeto, scopes por ação, segregação dos segredos, auditoria e verificação negativa de acesso cruzado.
- Uma aprovação CEO só é válida se ligada a um ator autenticado/autorizado e a uma decisão auditada; `gate.status=approved` no JSON **não** equivale a aprovação.

## 6. Integridade das revisões

A PR Core #30 apresenta endpoint transacional para candidatos:
- compara `expected_revision` e `expected_digest` (CAS), bloqueando atualizações desatualizadas;
- no PostgreSQL, serializa escritores através do bloqueio de linha do Core Project; em SQLite experimental usa `BEGIN IMMEDIATE`;
- preserva snapshots append-only na tabela `MemoryEntry`; não cria nova tabela;
- recusa estágios externos e aprovações de contacto/lançamento nesta versão;
- reserva o tipo de memória `venture_record_snapshot_v01` no endpoint HTTP genérico, sem permitir contornar o controlo de revisões por essa via;
- executa testes E2E com SQLite e PostgreSQL temporários.

Isto **não** constitui, por si só, isolamento de dados, autorização multi-utilizador ou garantia contra processos privilegiados com acesso direto à base de dados.

## 7. Gates de evolução

- **Gate técnico A:** PRs revistas e CI local/SQLite/PostgreSQL verde (testado em branch; ainda não aprovado para deploy).
- **Gate técnico B:** autenticação/segredos, concorrência, auditoria, regras de projeto e acesso cruzado revistos, inclusive todos os caminhos de escrita.
- **Gate operacional C:** projeto Noetic Ink individual, migração auditada e ligação de refs por especialista; sem execução pública.
- **Gate económico D:** fichas reais de produção, direitos das imagens, compradores e teste mínimo autorizado.
- **Gate comercial E:** operações externas, pedidos ou vendas só com aprovação explícita e controlos de qualidade.

**Esta é uma proposta de política, não uma afirmação de que estes gates já foram todos cumpridos.**
