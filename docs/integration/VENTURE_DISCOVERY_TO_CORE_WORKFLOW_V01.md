# Venture OS · Discovery → Core → Especialista v0.1

**Estado:** proposta executável em branch, não deployada  
**Data:** 2026-10-08  
**Sem ações comerciais ou financeiras automáticas**

## O primeiro circuito realista

```text
Discovery Quick (ideia, comprador, hipóteses, evidência, custos)
  ↓ prepara revisão
Venture Record v0.1-candidate (Core Project + provenance)
  ↓ autorização explícita para persistir apenas DRAFT interno
Core scoped API (POST /venture-records/{ref}/revisions, CAS)
  ↓ confirma revision + hash; pode rejeitar 409
Project Agent handoff draft (objetivo, critérios, lacunas)
  ↓ aprovação específica e execução posterior por ferramenta apropriada
Design Agent / Illustration Agent / CompanyOS-facing Consulting Agent
  ↓ evidência técnica/comercial real, se e quando executado
Venture OS reavalia gates e próxima experiência
```

Os passos anteriores até à preparação são **lógica de código executada em memória**. A PR testa a gravação apenas num **Core efémero**. No Core operacional não foram criadas estas novas Ventures nem executados os handoffs produzidos por esta etapa.

## Utilização local do Discovery Quick

```bash
python -m venture_integration.discovery_cli --input docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json --format markdown
```

Preparar pacote de trabalho para WordPress:

```bash
python -m venture_integration.workflow_cli --input docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json --opportunity-ref VOS-OPP-WEB-001 --project-slug designeo
```

Para T-shirts e serigrafia, substituir referência por `VOS-OPP-APPAREL-001`; para serralharia, por `VOS-OPP-METAL-001`. O JSON resultante contém `venture_record` e `handoff` com estados `prepared_not_persisted` e `prepared_not_executed`.

**Não existe opção `--commit` na CLI.** Por desenho, os ficheiros gerados não causam gravação, contacto, aprovação, fabricação ou publicação.

## Associação ao Core

O integrador Python `venture_integration.workflow` suporta o método
`persist_candidate_after_review(prepared, adapter=CoreMemoryHttpAdapter(...), expected_revision=..., expected_digest=..., authorized_internal_write=True)`.
Exige configuração de credencial scoped Venture no Core e autorização de escrita explícita. Aceita somente estado `exploring` e gate `pending`. O servidor Core da PR #30 verifica novamente o pedido com controlo transacional/identidade. Antes do merge da PR Core #30, a API live não suporta isto.

O *Project Agent handoff* é um pacote de parâmetros compatível com o método `prepare_agent_handoff` existente na integração. Preparar esse JSON **não invoca a ferramenta**. Para executar uma análise especializada será necessária ação subsequente autorizada, com contexto e ficheiros verdadeiros. O Project Agent coordena, não assume que o especialista executou.

## Rotas por vertical

| Vertical | Destino proposto | Que incerteza reduzir | Limite |
|---|---|---|---|
| Design & Web | Design Agent v3 / DesignOS | Produto WordPress original, direitos, qualidade, esforço | Sem criar ou vender kit sem revisão |
| Print & Apparel | Illustration Agent → Screenprint OS após dados reais | Direitos e aptidão técnica de duas artes | Sem impressão nem stock |
| Metal Fabrication | Consulting Agent / CompanyOS / Engineering | Custos, catálogo, medições e orçamentação | Sem promessa técnica, cotação real ou fabrico |

Os destinos são **propostas de roteamento**; não prova de que os agentes têm runtime pronto ou dados suficientes.

## Evidência e economia

As observações do dono recebem classificação `reported_observation` e `independent_market_validation = false`. Mesmo para uma receita ou preço hipotético, `economics.revenue` e `economics.contribution_margin` no Record ficam `null` até existir medição suportada; cálculos de cenário assumido são separados e identificados como tal.

## Testes e condições

A biblioteca Venture OS valida com unittest o circuito completo em memória: 3 verticais, proveniência, receio de aprovações fictícias, rejeição de operações não autorizadas, conflito de projeto e separação de números comerciais reais de cenários. A PR Core #30 executa **E2E HTTP real com SQLite e PostgreSQL efémeros**: gravação com credenciais de teste scoped, readback, revisão/hashes, recusa de escrita sem autorização e geração de handoff sem execução.

Critérios ainda abertos antes de uso operacional:
- Revisão das PRs e merge coordenado.
- Deployment interno aprovado com segredos scoped e rollback.
- Projetos Core próprios das Ventures quando houver vida operacional.
- Informação real para o primeiro teste comercial e autorização dos contactos/publicação.
- RBAC completo antes de vender o sistema como serviço multicliente.
