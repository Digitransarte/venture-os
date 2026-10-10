# VF-WP-01 · Blueprint interno v0.1 — Kit WordPress para serviços de bem-estar

**Autor do rascunho:** estudo preparatório do Venture OS, **não** output de execução do Design Agent v3.  
**Estado:** G0, hipótese de produto; sem validação comercial ou protótipo funcional.  
**Referência:** `VOS-OPP-WEB-001`; [brief e gates](VF_WP_01_PILOT_V01.md); [medição](VF_WP_01_MEASUREMENTS_V01.json).

## 1. Proposta de valor testável

Para profissionais independentes de bem-estar que querem uma presença digital clara e credível sem iniciar um website totalmente de raiz:

> Um conjunto de componentes WordPress originais, rápidos de adaptar à identidade, conteúdos e serviços de cada profissional, com uma opção de instalação supervisionada pela Designeo.

**Hipóteses**, não promessas comprovadas: menor esforço de implementação, menos revisões visuais, maior consistência, integração simplificada com WordPress, aquisição potencialmente repetível.

### Oferta A · Kit digital

- `theme.json` com tokens globais, tipografia, cor, espaçamento e largura;
- estrutura de homepage e três padrões (hero, cartões de serviços, CTA);
- header e footer como peças reutilizáveis;
- manual mínimo de instalação, personalização e dependências.
- **Não inclui:** hosting, domínio, imagens licenciadas, textos completos, branding de cliente, suporte ilimitado, Elementor Pro ou componentes proprietários.

### Oferta B · Kit + implementação

Inclui A como base de trabalho e serviço separado de instalação/adaptação. Hipótese para futuro escopo: páginas Início, Serviços, Sobre, Contactos; identidade e conteúdos fornecidos pelo cliente; testes básicos em desktop/mobile. **Não inclui automaticamente** copywriting especializado, SEO contínuo, cookies/conformidade jurídica, funcionalidades e-commerce, manutenção, licença de terceiros ou revisões ilimitadas.

## 2. Mapa textual do sistema, sem criar site

```text
WordPress / Gutenberg
  ├── theme.json (cores, tipografia, espaçamento, largura, botões)
  ├── Site structure
  │   ├── Header: símbolo/nome, menu, ação primária
  │   └── Footer: contacto, ligações, créditos
  └── Homepage blueprint
      ├── Pattern A: hero (promessa + prova editável + CTA)
      ├── Pattern B: services (3 cartões de serviço editáveis)
      ├── Pattern C: CTA/contact (contacto primário claro)
      └── pequenas secções editoriais opcionais
```

**Conteúdo de exemplo:** placeholders genéricos, nunca dados de clientes. Não incluir imagens nesta fase; escolher recursos apenas depois de provar direitos/licença.

**Sistema visual de referência:** hierarquia H1/H2/H3; 2 escalas de texto (corpo e títulos); 1 cor primária e paleta neutra; margens responsivas; contraste e foco de navegação a validar na implementação.

**Diferença comercial que temos de medir:** quantos elementos comuns sobrevivem a uma personalização real sem retrabalho excessivo? Sem esta medição, o kit pode ser apenas um website por medida disfarçado.

## 3. Desdobramento das tarefas e pontos de medição

| Etapa | Resultado mínimo | Responsável proposto | Tempo real |
|---|---|---|---|
| Delimitar comprador e promessa | 1 parágrafo de posicionamento e exclusões | Project Agent + humano | Por medir |
| Estrutura e design system | Árvore de componentes e hierarquia visual | Design Agent v3 (handoff preparado) | Por medir |
| Engenharia Gutenberg | Verificar padrão HTML/blocos e `theme.json`, sem build nesta fase | Software Agent / humano | Por medir |
| Direitos e licenças | Lista de dependências autorizadas, proibidas e por verificar | Humano | Por medir |
| Revisão de viabilidade | Mapa de custos, horas e recomendação G1 | Venture OS + humano | Por medir |

A chamada de `prepare_agent_handoff` não equivale a execução do Design Agent. Os custos de cada etapa serão lançados no ficheiro de medição quando houver chamadas e horas concretas; não inferir tarifa humana nem custo por token.

## 4. Riscos e decisões

- **Revenda e propriedade:** WordPress software GPL; código derivado e componentes de terceiros exigem análise de licenças. Não copiar nem revender modelos da Elementor Template Library.
- **Tecnologia:** padrões Gutenberg permitem reutilização, mas facilidade real de personalização, compatibilidade com outros temas, atualizações, importação/exportação e QA continuam sem testes.
- **Distribuição:** site Designeo vs marketplace vs venda de implementação. Taxas, condições de publicação, licença e CAC ainda desconhecidos.
- **Empreendimento:** não há prova de procura, clientes dispostos a pagar nem comparação de margens; selecionar preço/posicionamento só depois do custo medido.

## 5. Gate seguinte, sem compromisso automático

Aprovar uma **única prova funcional de pattern Hero** apenas se o blueprint estiver coerente, os direitos dos recursos forem verificáveis e o custo/tempo incremental aceitável. A prova funcional deverá ser testada em WordPress isolado e **não publicada**. Decisão posterior: continuar, ajustar nicho/escopo ou abandonar a ideia.

## 6. Fontes técnicas

- WordPress Patterns em templates: https://developer.wordpress.org/themes/patterns/usage-in-templates/
- `theme.json` oficial: https://developer.wordpress.org/themes/global-settings-and-styles/introduction-to-theme-json/
- Licença WordPress: https://wordpress.org/about/license/
- Elementor Template Library: https://elementor.com/terms/template-library/

**Fecho G0 (parcial):** arquitetura textual e ofertas propostas; Design Agent ainda não executado, horas e custos ainda não medidos; gates G1 e G2 pendentes.
