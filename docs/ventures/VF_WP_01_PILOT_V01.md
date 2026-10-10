# VF-WP-01 · Viabilidade de kit WordPress — estudo interno v0.1

**Oportunidade de origem:** `VOS-OPP-WEB-001`  
**Estado:** planeado / levantamento interno; **não validado**, sem produto vendido ou entregue  
**Proprietário:** Designeo · Venture OS  
**Objetivo:** avaliar se faz sentido criar um ativo web original, reutilizável, vendável como kit e/ou acompanhado de implementação personalizada, com baixo esforço humano adicional por cliente.

## 1. Decisão de escopo

**Hipótese de nicho:** profissionais e microempresas independentes de bem-estar (estúdios, aulas, terapias). É uma hipótese de design para limitar o ensaio, **não** uma inferência de procura confirmada. Nenhum conteúdo, identidade ou material de clientes existentes (incluindo Casa Bhumi) pode ser usado sem consentimento/licença específicos.

**Base tecnológica preferida para estudo:** WordPress com Gutenberg (block theme, patterns e `theme.json`), com elementos desenhados de raiz e recursos verificadamente licenciados. Elementor só é alternativa a comparar num estudo de custos, e não a base de componentes para revenda.

**A. Produto digital (hipótese):** kit original de identidade visual e estrutura web, exportável/documentado: estilos globais, header/footer, página inicial e blocos reutilizáveis, com instruções de instalação. A venda, distribuição e condições de suporte serão definidas apenas após validação de licenças e custos.

**B. Serviço (hipótese):** adaptação do kit a um site WordPress de cliente, configurando conteúdos, identidade e componentes. Hosting, domínio, imagens, texto profissional, integrações, manutenção, revisão e custos de terceiros devem ser explicitamente incluídos/excluídos numa proposta futura.

Ambas as ofertas permanecem hipóteses. Não fixar preços ao público antes de medir custos e diferenciação.

## 2. Experiência mínima — sem produzir o kit completo

Entregáveis exclusivamente internos:
1. **Arquitetura de uma página:** comprador, problema, proposta de valor, componentes comuns, dependências, riscos e exclusões.
2. **Mapa de reutilização:** 4 tipos de página como hipótese de kit completo (Início, Serviços, Sobre, Contactos); para este estudo, detalhar apenas a página inicial e os padrões Hero, Serviços e CTA. Nenhum website operacional é exigido.
3. **Especificação de uma secção original:** hierarquia, tokens tipográficos/cromáticos e estrutura de pattern — pode ser texto/wireframe, sem desenvolvimento de plugin, tema ou imagens nesta fase.
4. **Estimativa de esforço por tarefa + registo de tempo efetivo** para Project Agent, Design Agent, implementação Gutenberg e revisão humana. Distinguir estimativa de medição real.
5. **Matriz de custo e decisão:** separadamente para kit digital e kit + implementação, indicando os campos desconhecidos. Comparar custos totais, riscos de licenças e etapas com intervenção humana.

**Não fazer:** criar loja, comprar software, gerar site completo, instalar ou publicar WordPress, contactar clientes, anunciar, produzir assets gráficos finalizados, usar fotografias/marcas de terceiros sem licença, inventar testes de vendas ou margens.

## 3. Medição (preencher ao executar cada atividade)

Registar, para cada evento, `activity`, `actor`, `estimated_minutes`, `measured_minutes`, `cost_eur`, `cost_status`, `source_ref`, `output_ref`, `rework_minutes`, `notes`.

- **Humanos:** discovery, direção criativa, correções, revisão e QA; custo-hora indicado manualmente e separado das horas medidas.
- **Agentes:** número de chamadas, modelos, tokens (quando conhecidos), EUR reais cobrados ou `null` quando indisponíveis; não converter `null` em zero.
- **Desenvolvimento:** tempo inicial de criação do kit, custos de testes/dependências, horas adicionais de instalação por cliente, correções e suporte.
- **Despesas:** licenças de fontes, media, serviços, plataforma/marketplace, pagamentos, aquisição e infraestrutura; sempre distinguir custo fixo, por unidade e hipótese.
- **Venda:** preço hipotético de kit e preço hipotético de implementação em duas linhas independentes; IVA, IRC/IRS, amortização, overhead e taxas não devem desaparecer dos relatórios.

**Métricas para decisão:** `setup_human_hours`, `setup_agent_cost_eur`, `per_sale_human_hours`, `per_sale_agent_cost_eur`, `third_party_variable_cost_eur`, `price_hypothesis_eur`, `net_contribution_scenario_eur`, `payback_orders_scenario`. Sem dados, os resultados são `null`, não zero.

## 4. Gates de decisão

**G0 — Preparar (autorizado apenas como estudo interno):** arquitetar e preencher estimativas com proveniência. Não comprometer despesas externas nem executar especialistas sem handoff supervisionado.

**G1 — Construção mínima (pendente):** decidir se se investe numa pequena prova de conceito de Gutenberg com **um** pattern funcional; exige tempo humano disponível, custos estimados e verificação de direitos.

**G2 — Validação de mercado (pendente):** só após aprovação humana escolher um canal, preço de ensaio e métrica de compra/consulta verificável; aprovar qualquer contacto ou publicação separadamente. Sem evidência de procura, não declarar negócio viável.

**Parar/reformular** se faltar licença comercial, se a mesma secção exigir trabalho quase integral por cliente, se a contribuição estimada for insuficiente para cobrir o esforço humano, ou se o nicho/cliente alvo não puder ser descrito sem inventar procura. Estes são critérios qualitativos, não resultados observados.

## 5. Fontes técnicas/licenças a rever

- Patterns reutilizáveis em templates: https://developer.wordpress.org/themes/patterns/usage-in-templates/
- Definição de estilos globais em `theme.json`: https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/
- Distribuição de código derivado WordPress sob GPL: https://wordpress.org/about/license/
- Elementor Template Library: https://elementor.com/terms/template-library/ — modelos da biblioteca podem servir sites de clientes mas não ser revendidos como produto autónomo; não usá-los no kit comercial.
- Licenças de quaisquer fontes, fotografias e recursos externos a confirmar individualmente.

## 6. Resultado atual e próxima ação

**Conhecido:** capacidades do estúdio em WordPress/Elementor, design e web; WordPress oferece padrões de blocos reutilizáveis; existe uma base técnica para o estudo.  
**Não conhecido:** segmento comprador real, procura, disposição a pagar, tempo de implementação em Gutenberg, custo real dos agentes, licenças de todos os recursos, custo do suporte, CAC e margem.

**Próxima ação interna:** Project Agent preparar o handoff ao Design Agent v3 para entregar **apenas** a arquitetura/blueprint, mapa de padrões e estimativa de esforço com incertezas. Não gerar design final nem executar ferramentas externas nesta fase. Depois registar os minutos efetivamente consumidos e comparar a venda do kit com o serviço de implementação.

**Nenhuma decisão de investimento, produto comercial ou lançamento está aprovada por este documento.**
