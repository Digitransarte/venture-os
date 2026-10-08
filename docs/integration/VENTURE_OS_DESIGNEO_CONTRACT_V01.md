# Venture OS → Designeo OS: contrato de integração v0.1

**Estado:** Candidate / não implementado  
**Data:** 2026-10-08  
**Autoridade:** CEO  
**Escopo:** Venture OS como módulo de inteligência e desenvolvimento empresarial, ligado ao Designeo OS Core  
**Fonte:** Biblioteca Venture OS v0.1, especialmente Scope Map, Common Agent Operating Model, Explorer Protocol v0.2, Decision Protocol, Venture Project Record e Governance Charter.  
**Implementação:** proposta documental em branch isolada; sem deploy ou alterações à base de dados.

## 1. Missão

Converter uma ideia, um problema ou uma capacidade existente num percurso empresarial fundamentado: **descobrir → modelar → validar → criar → lançar → operar → aprender**.

Aplicar primeiro aos domínios com experiência e infraestrutura: (a) design, identidade, web e produtos digitais; (b) serigrafia, DTF e vestuário; (c) serralharia, CAD e fabrico físico. O Investment Agent/trading é uma linha de risco separada, não receita operacional de Venture OS. O sistema servirá inicialmente projetos próprios e poderá apoiar serviços ponta-a-ponta de desenvolvimento de marcas/negócios para terceiros.

**Princípio:** melhorar a economia da atividade real, não aumentar o número de agentes. O resultado de cada ciclo inclui: (1) decisão/experiência executável, (2) aprendizagem reutilizável com evidência.

## 2. O que se recupera do Venture OS original

| Legado | Manter como | Situação na nova arquitetura |
|---|---|---|
| Explorer Protocol / Validation | metodologia de descoberta, contraditório, Opportunity Brief | Venture OS, acionado pelo Project Agent |
| Strategist | proposta de valor, escolha de mercado, receita e testes económicos | função Venture OS, não agente canónico duplicado |
| Designer (legado) | definição da solução/MVP e necessidades do utilizador | Venture OS para produto; Design Agent v3 para criação visual |
| Builder (legado) | plano do que construir, custos, critérios de aceitação | Venture OS define hipótese/aceitação; Software Agent implementa; Builder controla deploy |
| Growth | aquisição, canais, conversão, retenção | função Venture OS, com execução assistida e autorizada |
| Archivist | decisão, experiência, knowledge seeds e learning | memória/decisões/evidência do Core; sem segundo arquivo |
| Venture Project Record | visão agregada do projeto e estado | Core Project + Decisions + Tasks + Memory + ExternalRefs + system state; **não duplicar base de dados** |
| Venture Orchestrator | recuperar intenção, contexto, prontidão, rota e próxima ação | Project Agent já definido; sem segundo orquestrador |
| Common Agent Operating Model | mandato → inputs → incerteza → processo → outputs → síntese → gate → handoff → aprendizagem | contrato transversal |
| CEO Gates | autorização em decisões materiais e mudança de fase | Decision Protocol + Core Decisions/controlled actions |

Os originais em docs/_source_word, docs/_converted e docs/canonical permanecem imutáveis. Os documentos canónicos históricos estão maioritariamente em Draft/Candidate; não os promover implicitamente a aprovado.

## 3. Responsabilidades e fronteiras

**Venture OS (domínio de negócio)** possui: captura da oportunidade, síntese de mercado, comparação de alternativas, definição de segmento/comprador, hipótese de proposta de valor, modelo de receita, unit economics, desenho de experimentos, leitura de evidência, recomendação de gates e aprendizagem sobre negócios.

**Project Agent / Designeo OS Core (infraestrutura)** possui: identificação do projeto, recuperação de contexto, memória, decisões formais, tarefas, permissões, handoffs, referências e continuidade. Não substitui análise especializada.

**DesignOS / Design Agent / Illustration Agent** possuem: briefing criativo, conceito visual, marca, ilustração, preparação técnica de ativos editáveis e QA próprio. Recebem requisitos e critérios, não instruções vagas para inventar a viabilidade de mercado.

**Software Agent** implementa e testa alterações em branch isolada, documenta erros e evidência de testes. **Builder** trata do deploy controlado, sujeito a aprovação.

**Screenprint OS** possui orçamentos, preparação técnica, consumíveis, planos de impressão, produção e stock. **CompanyOS/Engineering** possui custos, engenharia, fabrico, operações e segurança física.

**Investment Agent** possui análise de trading e risco financeiro. Eventuais bots de cripto operam em paper trading até uma aprovação separada para capital real.

O Venture OS não escreve diretamente nos dados operacionais dos especialistas fora dos contratos existentes e não declara que um handoff executou quando apenas o preparou.

## 4. Fases e gates (não linear)

| Fase | Resultado mínimo | Gate |
|---|---|---|
| Capture | ideia original, origem, domínio e intenção | triagem |
| Explore | Opportunity Brief, comprador, problema, alternativas, evidências e incógnitas | investigar / reformular / arquivar |
| Strategy | opções, proposta de valor, posicionamento, canal, preço hipotético e custos | escolher hipótese para testar |
| Validate | experiência mínima, critérios positivos/negativos, resultados observados e confiança | continuar / pivotar / parar |
| Design & Build | solução/MVP, handoff ao especialista e critérios de aceitação | autorização de recursos e publicação |
| Launch & Operate | oferta, aquisição, entrega, qualidade, receitas, custos e esforço humano | manter / escalar / alterar / suspender |
| Learn | aprendizagem do projeto e aprendizagem de sistema com proveniência | aceitar, testar ou rejeitar alterações |

O CEO pode parar, recuar, reabrir ou comparar oportunidades sem percorrer toda a sequência. Quick = triagem curta; Standard = hipótese e teste; Deep = múltiplas fontes, contraditório, economia e riscos.

## 5. Contrato mínimo de Venture Record (sobre Core)

Não criar uma segunda tabela Project na fase 0.1. Para cada oportunidade associar uma **referência de Venture** a um Core Project existente ou criar um novo Core Project pela API autorizada quando existir integração adequada.

Campos mínimos:

- venture_ref: identificador estável e único (não confundir com project slug);
- core_project_slug; vertical; type (internal-venture / client-venture / improvement);
- owner, current_stage, exploration_depth, current_hypothesis, buyer, user, beneficiary;
- evidence[]: claim, source_ref, date, evidence_level, supporting_or_contradictory, provenance;
- assumptions[], uncertainties[], critical_risks[], confidence, confidence_rationale;
- alternatives[], experiment: question, minimum_test, success_condition, failure_condition, budget_cap, status, results;
- commercial: offer, pricing_hypothesis, sales_channel, acquisition_cost, conversion, units, gross_revenue, direct_costs, platform_fees, refunds, material_costs;
- autonomy: agent_costs, review_hours, exceptions, approvals_required, reliability;
- outputs[] (refs da aplicação especialista), next_action, decision_ref, stage_gate;
- learnings[]: observation, interpretation, proposed_change, owner, review_state, version.

Nas versões iniciais, representar estes dados como documento estruturado versionado + Memory/Tasks/Decisions/ExternalRefs do Core. Quando houver 2+ pilotos e queries transversais reais, avaliar esquema tipado/API dedicado — sem promover necessidades hipotéticas a funcionalidades.

Os valores financeiros nunca devem misturar margem de contribuição com lucro líquido. Estimar separadamente horas de arranque, supervisão e aquisição de clientes. Vendas, taxas e margens estimadas devem ser rotuladas como hipóteses.

## 6. Evidência, decisão e risco

Distinguir explicitamente **observação**, **interpretação**, **hipótese**, **recomendação** e **decisão**. Conservar evidência contrária e origem; não inferir procura a partir de um marketplace ou de anúncios de preço. Usar os níveis originais de validação: intuição, dados indiretos, declarações, comportamento e evidência económica.

**Gates humanos obrigatórios:** compromissos financeiros, contacto externo a clientes, envio de propostas, publicação pública, encomendas, produção irreversível, direitos de propriedade intelectual, acesso a contas, deploy e capital real. Investigação e elaboração de drafts podem operar com menor fricção dentro de permissões e orçamentos explícitos.

Aprendizagens nunca alteram automaticamente agentes canónicos, condições contratuais ou software de produção. Propor modificação versionada → testar → rever → aprovar → publicar. Privacidade e direitos dos clientes permanecem separados dos ativos comerciais reutilizáveis.

## 7. Critérios de conclusão da integração v0.1

1. Uma ideia pode entrar em Quick mode e sair com oportunidade, desconhecidos, recomendação e next action.
2. Existe pelo menos um Opportunity Brief real com hipótese, evidência disponível, evidência em falta e teste mínimo.
3. O mesmo projeto é recuperado pelo Core sem duplicação; decisões e tarefas permanecem rastreáveis.
4. Um handoff para DesignOS ou Screenprint OS é preparado com critérios de aceitação específicos e propriedade de dados definida.
5. É possível colocar um projeto em pause/reformulate/abandon sem perder aprendizagem.
6. O circuito explicita custo de produção, custos de canais, intervenção humana e estado de validação.
7. Testes documentais da biblioteca e testes de integração devem passar antes de aprovar implementação.
8. Nenhuma oferta ou produção é publicada/lançada sem autorização e verificação da execução.

## 8. Próximos incrementos

**I0 (este documento):** recuperação documental e contrato proposto; original imutável.  
**I1:** piloto Noetic Ink com dados de oportunidade/experimento e handoff apenas preparado.  
**I2:** adaptador tipado sobre Core + contrato Project Agent; testar read/write com fixtures.  
**I3:** ciclo supervisionado DesignOS → Illustration → Screenprint → loja/canal e métricas reais, apenas após gates.  
**I4:** segundo caso da nova empresa de serralharia (produto/serviço físico), com riscos e custos próprios; terceiros após validação interna.

Referências canónicas: [Core Manual](../canonical/system/venture-os-core-manual.md), [Scope Map](../canonical/system/v0-1-scope-and-completion-map.md), [Common Agent Operating Model](../canonical/operations/common-agent-operating-model.md), [Explorer Protocol](../canonical/explorer/explorer-protocol.md), [Validation Protocol](../canonical/explorer/explorer-validation-protocol.md), [Decision Protocol](../canonical/operations/decision-protocol.md), [Venture Project Record](../canonical/templates/venture-project-record.md).

