# Venture Discovery Quick · v0.1

**Estado:** candidate, implementação pura e sem efeitos laterais  
**Data:** 2026-10-08  
**Função:** transformar ideias comerciais num radar comparável de oportunidades, sem inferir procura, vendas ou rentabilidade a partir da experiência técnica.

## Execução

No repositório Venture OS:

```bash
python -m venture_integration.discovery_cli --input docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json
python -m venture_integration.discovery_cli --input docs/integration/fixtures/OPPORTUNITY_RADAR_3_DOMAINS_V01.json --format json
```

O GitHub Actions executa os 54 testes e gera o Markdown/JSON na coleção temporária **venture-discovery-quick-candidate**. Os relatórios não são publicados no website nem persistidos automaticamente no Core.

## Inputs / outputs

Entrada: oportunidades JSON com oportunidade, vertical, proposta de valor, hipóteses sobre comprador, problema, modelo de receita e canal, evidências com `type`, `claim`, `source_ref`, pressupostos, eventual cenário de economia unitária e teste mínimo.

Saída: *Opportunity Brief* com estágio `discovery_not_validated`, classificação de evidências sem assumir verificação externa, lista de incógnitas, custo completo apenas se todos os campos monetários tiverem sido fornecidos, e gate de decisão sempre pendente de revisão humana.

**Não há score/ranking de rentabilidade automático.** Uma oportunidade potencialmente atraente sem dados de compradores continua desconhecida. Uma simulação unitária completa continua `complete_assumption_scenario`, com `profitability_confirmed=false`; os custos fixos, impostos e outras omissões são enumerados. A ação seguinte proposta não autoriza contactos, publicação, compras ou produção.

## Três candidatas iniciais

1. **Design & Web:** template WordPress original, incluindo serviço de implementação e eventual manutenção.
2. **Print & Apparel:** Noetic Ink, arte autoral e T-shirts serigrafadas/DTF.
3. **Manufacturing:** catálogo e orçamentação assistida para portões/vedações, articulado com fabrico.

Estes três casos são **exemplos para exercitar o método e a infraestrutura**, não uma shortlist fechada nem uma decisão de investimento. O utilizador pretende continuar a explorar diferentes modelos dentro dos domínios em que já possui experiência.

## Critérios para escolher experiência real

Avaliar, com factos diferenciados de hipóteses: comprador concreto, problema, existência de alternativa, procura demonstrada, canal, preço possível, custos reais, intervenção humana, fiabilidade e autorização. O modelo Quick aponta lacunas; decisões Quick→Standard→Deep exigem revisão humana.

Para o primeiro caso real, escolher uma hipótese e definir um teste mínimo com *stop condition* mensurável, sem investir em desenvolvimento completo antes de procurar sinais de compra.

## Relação com Core

- `venture_integration.discovery`: pesquisa/estrutura de oportunidades sem rede.
- `venture_integration.core_http`: leitura/gravação de uma Venture Record no Core apenas através de endpoints versionados e scoped (candidato da PR Core #30).
- `venture_integration.migration`: proposta auditável de mudança de projeto.
- Core Project, Memory/Tasks/Decisions, ExternalRefs e Project Agent continuam a ser a infraestrutura. O Discovery Quick não cria projetos nem duplica memória.

**Bloqueadores:** PRs #1 e #30 continuam Draft, com integração em produção, autenticação multicliente e lançamento comercial não aprovados.
