# VF-WP-01 · Revisão de arquitetura e esforço v0.2 (G0)

**Data:** 2026-10-10  
**Tipo de trabalho:** análise técnica preliminar elaborada em ChatGPT, não execução do Design Agent v3.  
**Estado:** proposta interna, sem desenvolvimento WordPress, desenho final, licença comercial verificada ou contacto a clientes.  
**Origem:** `VOS-OPP-WEB-001`; [brief](VF_WP_01_PILOT_V01.md), [blueprint](VF_WP_01_BLUEPRINT_V01.md), [medições](VF_WP_01_MEASUREMENTS_V01.json).

## 1. Hipótese revista: serviço primeiro, produto depois

A oferta que se deve testar primeiro é o **serviço de implementação Designeo com uma biblioteca própria de componentes**, mantendo a venda do kit como hipótese secundária. Justificação: blocos WordPress básicos e padrões gratuitos já existem, logo a diferenciação de um produto avulso terá de resultar de sistema visual, qualidade, reutilização, documentação e poupança real de horas. Não existe ainda informação de vendas, CAC, valores praticados por este nicho ou procura confirmada. Não inferir que a oferta foi validada.

- **Oferta A, fase posterior:** kit original que pode ser distribuído separadamente, sujeito a revisão de qualidade, licenças e suporte.
- **Oferta B, piloto preferido:** implementar um website de apresentação para um microprestador de serviços, usando patterns próprios e adaptáveis, sem reutilizar qualquer propriedade de clientes anteriores.

O nicho de bem-estar continua apenas um *perfil-arquétipo* para limitar a análise, não uma decisão de mercado. Usar nomes, textos e identidades fictícios durante prototipagem.

## 2. Arquitetura recomendada de estudo

**Estrato de design:** tokens de paleta, tipografia, escalas, largura, espaçamento, componentes CTA e guidelines responsivas. O Design Agent deve definir as regras, não produzir imagens por tentativa/erro.

**Estrato Gutenberg:** tema de blocos de referência em sandbox, `theme.json` para tokens `settings` e `styles`; padrões originais registados por ficheiros próprios em `/patterns`; partes de template para header/footer; blocos core WordPress sempre que possível. Distinguir patterns **não sincronizados** da atualização global de estilos — ao inserir um pattern no conteúdo, as alterações futuras ao padrão não se propagam automaticamente a cada cópia já inserida.

**Estrato editorial:** para um Hero funcional, exigir promessa clara, subtítulo, CTA primário e apoio visual opcional (sem media de terceiros); três cartões de serviço reutilizáveis e CTA contacto apenas no blueprint. Cada pattern deve ser testável com duas identidades fictícias muito diferentes.

**Estrato de entrega:** manual de troca de textos, alterações de cor/tipografia, limites de personalização, checklist de QA mobile/acessibilidade e matriz de dependências.

**Não construir agora** um tema completo, quatro páginas, plug-in, loja, meios de pagamento, checkout ou geração de assets; isto é uma especificação.

## 3. Estimativas de esforço — APENAS intervalos de planeamento

Estimativas de gabinete sem medição empírica deste fluxo. Não são horas efetivamente gastas nem promessas de produtividade de agentes. Intervalos dependem da experiência em Gutenberg e da qualidade do material de entrada.

| Atividade | Esforço hipotético (min) | Evidência atual |
|---|---:|---|
| Project Agent: rever oferta, definir componentes e scope | 45–90 | Handoff preparado; execução não confirmada |
| Design Agent v3: especificação visual e revisão (sem arte final) | 60–120 | Não executado |
| Revisão humana de consistência/direitos | 30–75 | Não medida |
| **G1, se aprovado:** um Hero Gutenberg funcional original, teste com 2 identidades e QA | **300–600** | Bloqueado por aprovação G1 |
| **Kit futuro (fase diferente):** design + 3 patterns + template parts + documentação + QA | **1 500–3 000** | Cenário indicativo, não orçamentado |
| **Implementação por cliente (fase diferente):** quatro páginas com textos/assets prontos | **360–840** | Cenário indicativo, fortemente dependente do cliente |

As estimativas do kit completo e da implementação **não se somam automaticamente**: parte do trabalho inicial pode ser reutilizada. Esforço de correções, suporte, plugins, conformidade, acessibilidade e licenças pode prolongar os intervalos. Antes de precificar, medir trabalho real numa experiência aprovada.

## 4. Modelo económico a preencher, não preços inventados

Para cada opção `i` (kit ou implementação):

`contribuição_por_encomenda_i = preço_sem_IVA_i - comissões_i - custos_de_entrega_i - licenças_variáveis_i - aquisição_i - custo_agentes_i - minutos_humanos_i/60 × custo_hora_humano`.

O **custo inicial de criação** fica numa linha separada, e `encomendas_para_recuperar_investimento_i = custo_inicial / contribuição_por_encomenda_i` só é calculável se houver contribuição positiva e custos suportados por estimativas explícitas ou medições. Custos fixos, fiscalidade e cenários de devolução/revisão devem ser considerados na decisão posterior. Por agora manter preços, margens, recuperação de investimento e custos reais como **desconhecidos**.

**Métrica prioritária:** horas humanas consumidas numa adaptação com duas identidades fictícias comparadas com uma implementação manual, usando condições equivalentes. Não atribuir poupança percentual antes desta comparação.

## 5. Critério de aprovação para G1 (decisão humana posterior)

Autorizar **apenas um pattern Hero** num WordPress sandbox, sem publicar, se:
- arquitetura e licenças do componente forem avaliadas;
- comprador e variante de conteúdo de exemplo estiverem suficientemente definidos;
- existir um limite de horas humano aceite;
- forem definidos os critérios de sucesso: inserir, personalizar textos e tokens, verificar mobile/teclado e verificar duas identidades, registando retrabalho;
- puder ser revogado/descartado sem afetar sites ou dados de clientes.

**Gate G2 permanece fechado:** não testar procura, publicar, contactar potenciais clientes ou cobrar valores nesta etapa.

## 6. Limitações e fontes

O endpoint atual do Designeo OS permite **preparar** um pacote Project Agent → Design Agent v3, mas não comprova a **execução** do especialista. O contrato do Design Agent v3 consultado indica `implemented-designos-branch`. Não descrever esta análise como produzida ou medida pelo agente.

- WordPress: [introduction to theme.json](https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/).
- WordPress: [registering patterns](https://developer.wordpress.org/themes/patterns/registering-patterns/).
- WordPress: [synced and non-synced patterns](https://developer.wordpress.org/themes/patterns/introduction-to-patterns/).
- Elementor: [Template Library terms](https://elementor.com/terms/template-library/) — uso em websites de clientes não autoriza revenda isolada de modelos dessa biblioteca.

**Conclusão G0:** o serviço com biblioteca própria merece um ensaio técnico de poupança de tempo, mas ainda não existe base para concluir que compensa financeiramente. Próximo gate: decidir se se justifica construir e medir um único Hero funcional.
