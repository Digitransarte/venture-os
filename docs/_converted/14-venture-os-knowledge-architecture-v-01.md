# Venture Operations System

## Knowledge Architecture

**Documento:** Knowledge Architecture
**Código:** VOS-KNO-CORE-001
**Versão:** 0.1
**Estado:** Arquitetura fundadora — piloto
**Âmbito:** Venture Operations System
**Autoridade:** CEO
**Responsável pela integridade:** Archivist
**Documentos de referência:**

1. VOS-ARC-CORE-001 — Global Architecture v0.1

1. VOS-GOV-CORE-001 — Governance Charter v0.1

# 1. Finalidade

A Knowledge Architecture define como o Venture Operations System cria, recebe, classifica, relaciona, valida, atualiza, utiliza e preserva conhecimento.

A sua função é garantir que:

1. informação não é confundida com conhecimento;

1. ideias não são confundidas com decisões;

1. hipóteses não são tratadas como factos;

1. evidência mantém ligação à origem;

1. documentos oficiais representam o estado atual do projeto;

1. conhecimento contraditório permanece visível;

1. agentes conseguem reutilizar aprendizagens anteriores;

1. o CEO recebe conclusões claras sem perder rastreabilidade;

1. o sistema aprende sem apagar o histórico;

1. cada decisão pode ser reconstruída.

Este documento governa o ciclo de vida do conhecimento no Venture OS.

# 2. Princípio fundador

**O trabalho é sequencial. O conhecimento é transversal.**

Os agentes executam funções distintas ao longo do pipeline.

O conhecimento, porém, pode:

1. surgir em qualquer etapa;

1. ser relevante para vários agentes;

1. alterar interpretações anteriores;

1. permanecer útil depois do projeto terminar;

1. revelar oportunidades fora do âmbito atual;

1. melhorar o próprio Venture OS.

A arquitetura deve permitir circulação sem provocar desorganização.

# 3. Princípio de separação

**Informação, evidência, interpretação, hipótese, decisão e conhecimento são objetos diferentes.**

O Venture OS não deve fundi-los numa única narrativa.

Cada objeto possui:

1. função;

1. autoridade;

1. estado;

1. responsável;

1. proveniência;

1. ciclo de vida próprio.

Esta separação reduz:

1. falsa certeza;

1. perda de contexto;

1. duplicação;

1. enviesamento;

1. alteração silenciosa da realidade;

1. decisões baseadas em memória imprecisa.

# 4. Objetivos da arquitetura

A Knowledge Architecture deve permitir ao sistema responder:

1. O que sabemos?

1. Como sabemos?

1. Quem registou?

1. Quando foi observado?

1. Em que contexto?

1. Que interpretação foi feita?

1. Que hipótese está relacionada?

1. Que decisão depende desta informação?

1. Que documento representa o estado atual?

1. Que conhecimento foi contraditado?

1. Que versão substituiu a anterior?

1. Que aprendizagem pode ser reutilizada?

1. Que informação ainda é provisória?

# 5. Camadas do conhecimento

O Venture OS organiza o conhecimento em seis camadas.

## Camada 1 — Captura

Contém material ainda não estruturado.

Exemplos:

1. notas;

1. transcrições;

1. observações;

1. documentos;

1. mensagens;

1. dados;

1. ideias;

1. resultados de ferramentas.

## Camada 2 — Registos estruturados

Transforma material bruto em objetos rastreáveis.

Exemplos:

1. Evidence Records;

1. Knowledge Seeds;

1. Assumptions;

1. Risks;

1. Decision Records;

1. Learning Notes;

1. Incident Records.

## Camada 3 — Síntese

Agrupa objetos individuais em padrões interpretáveis.

Exemplos:

1. Evidence Clusters;

1. temas;

1. segmentos;

1. padrões;

1. contradições;

1. mapas;

1. matrizes;

1. conclusões provisórias.

## Camada 4 — Documentos oficiais

Representa o estado consolidado do projeto.

Exemplos:

1. Opportunity Brief;

1. Strategic Brief;

1. Experience Brief;

1. Build Plan;

1. Growth Strategy.

## Camada 5 — Decisão

Regista a escolha do CEO perante alternativas, evidência e risco.

Exemplos:

1. Decision Records;

1. CEO Gates aprovados;

1. autorizações;

1. redefinições;

1. suspensões.

## Camada 6 — Aprendizagem institucional

Preserva conhecimento para utilização futura.

Exemplos:

1. Project Learning Notes;

1. System Learning Notes;

1. padrões reutilizáveis;

1. princípios;

1. alterações de protocolo;

1. memória de decisões.

# 6. Unidade fundamental de conhecimento

A unidade fundamental do Venture OS é o **Knowledge Object**.

Um Knowledge Object é qualquer elemento formal que possui identidade, função e ciclo de vida no sistema.

## Exemplos

1. uma evidência;

1. uma hipótese;

1. uma decisão;

1. um risco;

1. uma Knowledge Seed;

1. um documento;

1. uma aprendizagem;

1. um participante;

1. uma fonte;

1. uma métrica;

1. uma contradição.

# 7. Propriedades mínimas de um Knowledge Object

Cada objeto relevante deve possuir, sempre que aplicável:

1. código;

1. título;

1. tipo;

1. descrição;

1. projeto;

1. agente responsável;

1. autor ou origem;

1. data de criação;

1. data de atualização;

1. estado;

1. versão;

1. nível de confiança;

1. sensibilidade;

1. relações;

1. proveniência;

1. limitações;

1. histórico.

Nem todos os campos precisam de estar visíveis ao CEO.

Devem, porém, estar disponíveis para o sistema.

# 8. Sistema de identificação

Cada Knowledge Object deve possuir um identificador único.

## Formato base

**VOS-[TIPO]-[PROJETO]-[NÚMERO]**

## Exemplos

1. VOS-EV-EXP-001-0001 — Evidence Record;

1. VOS-KS-EXP-001-001 — Knowledge Seed;

1. VOS-DEC-EXP-001-001 — Decision Record;

1. VOS-RSK-EXP-001-001 — Risk;

1. VOS-ASM-EXP-001-001 — Assumption;

1. VOS-PLN-EXP-001-001 — Project Learning Note;

1. VOS-SLN-SYS-001-001 — System Learning Note;

1. VOS-EVC-EXP-001-001 — Evidence Cluster.

Os identificadores não devem ser reutilizados.

# 9. Taxonomia principal

O Venture OS organiza os Knowledge Objects nas seguintes famílias:

1. Evidence;

1. Hypotheses;

1. Assumptions;

1. Decisions;

1. Knowledge Seeds;

1. Risks;

1. Core Documents;

1. Operational Artefacts;

1. Learning;

1. Governance;

1. Sources;

1. Participants;

1. Metrics;

1. Incidents;

1. System Changes.

# 10. Evidence

Evidence representa observações que podem apoiar, enfraquecer, contextualizar ou contradizer uma hipótese.

## Tipos principais

1. observacional;

1. declarada;

1. comportamental;

1. económica;

1. documental;

1. digital pública;

1. experimental;

1. técnica;

1. operacional;

1. contraditória.

## Regra

Uma evidência não deve conter várias observações principais misturadas.

# 11. Estrutura conceptual da evidência

Cada Evidence Record deve distinguir:

## Observação

O que foi visto, ouvido, medido ou encontrado.

## Contexto

Em que circunstância ocorreu.

## Origem

Quem ou o que produziu a informação.

## Interpretação

O que o agente entende que a observação pode significar.

## Relação

Que hipótese, risco ou decisão pode ser afetado.

## Limitação

O que reduz a sua força ou aplicabilidade.

# 12. Hierarquia de evidência

A escala base do Venture OS utiliza cinco níveis.

## Nível 0 — Opinião ou suposição

Sem observação verificável.

## Nível 1 — Indício fraco

Observação isolada, indireta ou pouco específica.

## Nível 2 — Evidência relevante

Experiência concreta ou fonte aplicável, ainda limitada.

## Nível 3 — Evidência forte

Comportamento, dados ou múltiplas fontes independentes.

## Nível 4 — Evidência muito forte

Padrão consistente, replicável, quantificado ou experimental.

O nível não substitui a análise de contexto.

# 13. Hipóteses

Uma hipótese é uma afirmação testável que ainda não possui autoridade de facto consolidado.

## Estrutura mínima

1. formulação;

1. origem;

1. tipo;

1. importância;

1. evidência favorável;

1. evidência contrária;

1. método de teste;

1. estado;

1. confiança;

1. consequência se invalidada.

# 14. Tipos de hipótese

O Venture OS pode utilizar:

1. hipótese de problema;

1. hipótese de segmento;

1. hipótese de comportamento;

1. hipótese de valor;

1. hipótese de canal;

1. hipótese de modelo;

1. hipótese técnica;

1. hipótese operacional;

1. hipótese de crescimento;

1. hipótese de sistema.

# 15. Estados de hipótese

1. Não testada;

1. Em exploração;

1. Parcialmente sustentada;

1. Sustentada;

1. Enfraquecida;

1. Contraditada;

1. Invalidada;

1. Reformulada;

1. Arquivada.

Uma hipótese sustentada continua sujeita a revisão.

# 16. Pressupostos

Um pressuposto é uma condição tomada como verdadeira para permitir planeamento ou execução, apesar de ainda não estar suficientemente demonstrada.

## Diferença entre hipótese e pressuposto

A hipótese é formulada para ser investigada.

O pressuposto é utilizado provisoriamente para permitir que o trabalho prossiga.

## Exemplo

**Hipótese:**
Pequenos negócios têm dificuldade em escolher canais de aquisição.

**Pressuposto:**
O segmento terá disponibilidade para participar em entrevistas remotas.

# 17. Estados de pressuposto

1. Não testado;

1. Em teste;

1. Parcialmente sustentado;

1. Sustentado;

1. Enfraquecido;

1. Invalidado;

1. Substituído;

1. Arquivado.

Pressupostos críticos devem aparecer na Executive View.

# 18. Knowledge Seeds

Uma Knowledge Seed é uma ideia capturada sem autoridade para alterar o projeto.

Pode representar:

1. solução;

1. funcionalidade;

1. oportunidade;

1. melhoria;

1. parceria;

1. modelo;

1. experiência;

1. nova pergunta;

1. alteração do sistema.

## Regra principal

**Capturar não significa aprovar.**

# 19. Estrutura de uma Knowledge Seed

1. código;

1. título;

1. descrição;

1. origem;

1. contexto;

1. projeto;

1. agente destinatário;

1. potencial aplicação;

1. relação com objetos existentes;

1. risco de distração;

1. estado;

1. decisão associada, quando existir.

# 20. Estados de uma Knowledge Seed

1. Capturada;

1. Classificada;

1. Relacionada;

1. Em espera;

1. Em avaliação;

1. Promovida;

1. Integrada;

1. Rejeitada;

1. Arquivada.

# 21. Promoção de Knowledge Seeds

Uma Knowledge Seed pode ser promovida a:

1. hipótese;

1. tarefa;

1. experiência;

1. requisito;

1. projeto;

1. risco;

1. melhoria;

1. alteração de sistema;

1. documento oficial.

A promoção deve possuir responsável e justificação.

# 22. Decision Records

Um Decision Record representa uma escolha com autoridade institucional.

## Elementos obrigatórios

1. decisão;

1. decisor;

1. contexto;

1. data;

1. alternativas;

1. racional;

1. evidência;

1. pressupostos;

1. riscos;

1. consequências;

1. reversibilidade;

1. condição de revisão;

1. objetos afetados.

# 23. Estados de decisão

1. Proposta;

1. Pendente;

1. Aprovada;

1. Condicional;

1. Em execução;

1. Implementada;

1. Em revisão;

1. Substituída;

1. Revertida;

1. Arquivada.

Decisões substituídas não devem ser eliminadas.

# 24. Riscos

Um risco representa um acontecimento incerto que pode afetar objetivos, pessoas, recursos, qualidade, reputação ou continuidade.

## Estrutura mínima

1. descrição;

1. causa;

1. consequência;

1. probabilidade;

1. impacto;

1. nível;

1. sinais;

1. mitigação;

1. responsável;

1. estado;

1. condição de escalada.

# 25. Estados de risco

1. Identificado;

1. Em avaliação;

1. Ativo;

1. Mitigado;

1. Aceite;

1. Escalado;

1. Materializado;

1. Encerrado;

1. Arquivado.

# 26. Core Documents

Core Documents representam o estado oficial de uma área do projeto.

## Exemplos por agente

### Explorer

1. Opportunity Brief.

### Strategist

1. Strategic Brief.

### Designer

1. Experience Brief.

### Builder

1. Build Plan.

### Growth

1. Growth Strategy.

## Regra

Cada projeto deve saber qual é a versão ativa de cada Core Document.

# 27. Estados documentais

1. Rascunho;

1. Em revisão;

1. Provisório;

1. Pronto para decisão;

1. Aprovado;

1. Aprovado condicionalmente;

1. Ativo;

1. Substituído;

1. Suspenso;

1. Arquivado.

# 28. Templates e instâncias

O Venture OS distingue:

## Template

Define uma estrutura reutilizável do sistema.

## Instância

Aplica essa estrutura a um projeto específico.

## Exemplo

**Opportunity Brief Template**
Define como um Opportunity Brief deve ser construído.

**Opportunity Brief VOS-EXP-001**
Contém a oportunidade concreta do projeto piloto.

Templates e instâncias devem possuir códigos distintos.

# 29. Operational Artefacts

São documentos utilizados para executar trabalho, sem representarem necessariamente o estado oficial do projeto.

## Exemplos

1. Research Plan;

1. Interview Guide;

1. Participant Log;

1. backlog;

1. checklist;

1. roteiro;

1. matriz;

1. plano de teste;

1. relatório técnico;

1. calendário;

1. log operacional.

Podem ser essenciais sem serem Core Documents.

# 30. Project Learning Notes

Uma Project Learning Note regista conhecimento aprendido sobre um projeto específico.

## Pode conter

1. padrão observado;

1. pressuposto invalidado;

1. decisão eficaz;

1. erro;

1. reação de utilizadores;

1. limitação do modelo;

1. comportamento de canal;

1. aprendizagem técnica;

1. melhoria operacional.

# 31. System Learning Notes

Uma System Learning Note regista uma aprendizagem sobre o próprio Venture OS.

## Exemplos

1. excesso de campos num template;

1. ausência de um estado documental;

1. CEO Gate demasiado longo;

1. conflito entre agentes;

1. classificação ambígua;

1. protocolo que não reduz incerteza;

1. dashboard que oculta risco.

# 32. Fontes

Uma Source representa a origem documental, digital, humana ou técnica de informação.

## Tipos

1. documento;

1. website;

1. base de dados;

1. entrevista;

1. sistema;

1. observação;

1. relatório;

1. artigo;

1. ferramenta;

1. experiência;

1. especialista;

1. dado interno.

# 33. Source Record

Cada fonte relevante deve possuir:

1. código;

1. título;

1. autor ou entidade;

1. data;

1. localização;

1. tipo;

1. qualidade;

1. independência;

1. relevância;

1. limitações;

1. objetos derivados;

1. estado de acesso.

# 34. Participantes

Os participantes são fontes humanas de investigação, mas possuem governação própria.

Cada participante deve estar ligado a:

1. Participant Record;

1. consentimentos;

1. entrevistas;

1. Evidence Records;

1. segmento;

1. independência;

1. relevância.

A identidade deve permanecer separada da análise sempre que possível.

# 35. Evidence Clusters

Um Evidence Cluster agrupa várias evidências que parecem representar o mesmo padrão.

## Deve incluir

1. formulação do padrão;

1. evidências associadas;

1. fontes independentes;

1. segmentos;

1. exceções;

1. contradições;

1. confiança;

1. limitações;

1. hipóteses afetadas.

O cluster não substitui os Evidence Records individuais.

# 36. Contradições

O Venture OS deve tratar contradições como objetos de conhecimento relevantes.

Uma contradição pode ocorrer entre:

1. duas evidências;

1. evidência e hipótese;

1. dois documentos;

1. decisão e resultado;

1. agentes;

1. versões;

1. conhecimento atual e conhecimento anterior.

# 37. Contradiction Record

Quando a contradição for material, deve ser registada.

## Estrutura

1. objetos em conflito;

1. natureza da divergência;

1. contexto;

1. importância;

1. explicações possíveis;

1. investigação necessária;

1. responsável;

1. estado;

1. impacto potencial.

# 38. Estados de contradição

1. Identificada;

1. Em análise;

1. Explicada por contexto;

1. Parcialmente resolvida;

1. Resolvida;

1. Mantida;

1. Escalada;

1. Arquivada.

Nem todas as contradições precisam de ser eliminadas.

Algumas revelam segmentação ou complexidade real.

# 39. Factos, interpretações e conclusões

O Venture OS utiliza três níveis distintos.

## Facto observado

Afirmação limitada ao que foi diretamente registado.

## Interpretação

Significado atribuído por um agente.

## Conclusão

Síntese sustentada por múltiplos objetos e apresentada com determinado nível de confiança.

## Exemplo

**Facto observado:**
O participante afirmou ter utilizado três agências no último ano.

**Interpretação:**
O participante parece insatisfeito com as soluções utilizadas.

**Conclusão provisória:**
Existe rotatividade de fornecedores neste segmento, possivelmente relacionada com insatisfação.

# 40. Níveis de confiança

A confiança pode ser classificada como:

1. Muito baixa;

1. Baixa;

1. Média;

1. Alta;

1. Muito alta.

## A confiança deve considerar

1. quantidade de evidência;

1. qualidade;

1. independência;

1. consistência;

1. atualidade;

1. representatividade;

1. força de contradições;

1. aplicabilidade ao contexto.

# 41. Regra da confiança

**A confiança pertence à afirmação, não ao documento inteiro.**

Um documento pode conter:

1. conclusões com confiança alta;

1. hipóteses com confiança média;

1. pressupostos com confiança baixa;

1. questões totalmente desconhecidas.

Deve evitar-se uma única classificação simplista quando isso oculta diferenças importantes.

# 42. Autoridade epistemológica

Nem todos os objetos possuem a mesma autoridade.

## Autoridade muito baixa

1. opinião não fundamentada;

1. memória informal;

1. ideia;

1. Knowledge Seed.

## Autoridade baixa

1. hipótese;

1. indício;

1. observação isolada;

1. pressuposto.

## Autoridade média

1. padrão parcial;

1. múltiplas observações;

1. interpretação revista;

1. documento provisório.

## Autoridade alta

1. conclusão sustentada;

1. Core Document aprovado;

1. decisão formal;

1. aprendizagem validada.

## Autoridade institucional

1. Governance Charter;

1. Global Architecture;

1. decisão do CEO;

1. protocolo aprovado;

1. versão ativa oficial.

Autoridade institucional não transforma uma afirmação falsa em verdadeira.

# 43. Proveniência

Proveniência é a capacidade de reconstruir a origem e transformação de um Knowledge Object.

## Deve indicar

1. origem primária;

1. autor ou sistema;

1. método;

1. data;

1. contexto;

1. transformações;

1. relações;

1. documentos derivados;

1. decisões que o utilizaram.

# 44. Cadeia de proveniência

Exemplo:

Entrevista
↓
Evidence Record
↓
Evidence Cluster
↓
Hipótese atualizada
↓
Opportunity Brief
↓
CEO Gate
↓
Decision Record

O sistema deve permitir percorrer esta cadeia em ambos os sentidos.

# 45. Regra de proveniência

**Quanto mais importante a decisão, maior deve ser a rastreabilidade do conhecimento que a suporta.**

Decisões reversíveis e operacionais podem utilizar documentação leve.

Decisões estratégicas, financeiras, legais ou irreversíveis exigem cadeia mais robusta.

# 46. Relações entre objetos

Os objetos podem possuir relações como:

1. reforça;

1. enfraquece;

1. contradiz;

1. deriva de;

1. depende de;

1. substitui;

1. aprova;

1. rejeita;

1. testa;

1. origina;

1. limita;

1. mitiga;

1. materializa;

1. atualiza;

1. pertence a;

1. aplica-se a;

1. reutiliza;

1. resolve.

# 47. Knowledge Graph

O conjunto destas relações forma o Knowledge Graph do Venture OS.

O Knowledge Graph não precisa de ser inicialmente uma tecnologia complexa.

Pode começar como:

1. campos relacionais;

1. referências cruzadas;

1. tabelas;

1. bases de dados;

1. códigos;

1. links entre documentos.

O princípio é mais importante do que a ferramenta.

# 48. Perguntas do Knowledge Graph

O sistema deverá conseguir responder progressivamente:

1. Que evidências sustentam esta conclusão?

1. Que decisões dependem deste pressuposto?

1. Que riscos afetam este plano?

1. Que Knowledge Seeds surgiram neste projeto?

1. Que aprendizagem alterou este template?

1. Que documentos ainda referem uma versão antiga?

1. Que segmentos contradizem esta hipótese?

1. Que agentes utilizaram esta fonte?

1. Que decisão precisa de revisão?

# 49. Ciclo de vida do conhecimento

O ciclo geral contém:

1. Captura;

1. Estruturação;

1. Classificação;

1. Relação;

1. Revisão;

1. Síntese;

1. Aprovação;

1. Utilização;

1. Monitorização;

1. Atualização;

1. Substituição;

1. Arquivo;

1. Reutilização.

Nem todos os objetos percorrem todas as etapas.

# 50. Captura

A captura deve ser simples para evitar perda de informação.

Pode ocorrer através de:

1. formulário;

1. conversa;

1. nota;

1. importação;

1. ferramenta;

1. entrevista;

1. observação;

1. agente;

1. documento;

1. integração.

## Regra

A captura inicial não deve exigir classificação perfeita.

A organização pode ocorrer depois.

# 51. Inbox de conhecimento

O Venture OS deve possuir uma Knowledge Inbox para objetos ainda não classificados.

Pode receber:

1. notas;

1. ideias;

1. links;

1. documentos;

1. questões;

1. observações;

1. alertas;

1. resultados;

1. contradições.

O Archivist ou agente responsável deve processar periodicamente esta caixa.

# 52. Processamento da Knowledge Inbox

Cada entrada deve ser:

1. descartada;

1. transformada em Knowledge Seed;

1. transformada em Evidence Record;

1. ligada a um objeto existente;

1. atribuída a um agente;

1. promovida a tarefa;

1. marcada para revisão;

1. arquivada.

A Inbox não deve tornar-se arquivo permanente.

# 53. Classificação

A classificação deve utilizar apenas categorias úteis para:

1. encontrar;

1. relacionar;

1. decidir;

1. proteger;

1. reutilizar;

1. auditar.

Evitar taxonomias excessivamente detalhadas sem uso operacional.

# 54. Metadados obrigatórios

Os campos mínimos dependem do tipo de objeto.

Contudo, objetos materiais devem possuir:

1. tipo;

1. projeto;

1. responsável;

1. estado;

1. data;

1. origem;

1. relações principais.

Documentos oficiais devem ainda possuir:

1. versão;

1. aprovação;

1. documento substituído;

1. autoridade.

# 55. Revisão

A revisão procura verificar:

1. clareza;

1. exatidão;

1. coerência;

1. proveniência;

1. relevância;

1. duplicação;

1. sensibilidade;

1. relações;

1. autoridade;

1. limitações.

Uma revisão pode ser:

1. automática;

1. pelo agente;

1. por outro agente;

1. pelo Archivist;

1. pelo CEO;

1. externa.

# 56. Validação

Validar não significa provar definitivamente.

Significa confirmar que o objeto cumpre critérios suficientes para o uso pretendido.

## Exemplos

Uma Evidence Record pode ser válida como relato individual, mas insuficiente para sustentar uma conclusão geral.

Uma hipótese pode ser suficientemente sustentada para um teste, mas não para um investimento elevado.

# 57. Síntese

A síntese transforma vários objetos numa representação mais útil.

Pode produzir:

1. padrão;

1. conclusão;

1. briefing;

1. dashboard;

1. mapa;

1. recomendação;

1. previsão;

1. decisão proposta.

A síntese deve preservar acesso às fontes de origem.

# 58. Aprovação

A aprovação altera a autoridade de um objeto.

## Pode significar

1. aceitação de um Core Document;

1. decisão de utilizar uma direção;

1. validação de um protocolo;

1. adoção de uma aprendizagem;

1. promoção de uma seed;

1. autorização de passagem.

A aprovação deve identificar quem possui autoridade.

# 59. Atualização

Quando conhecimento novo afeta um objeto existente, o sistema deve decidir entre:

1. acrescentar;

1. corrigir;

1. reformular;

1. criar nova versão;

1. contraditar;

1. substituir;

1. arquivar.

Alterações de significado exigem nova versão ou novo objeto.

# 60. Substituição

Um objeto substituído:

1. deixa de ser a versão ativa;

1. mantém identidade;

1. preserva relações;

1. indica sucessor;

1. continua acessível no histórico.

## Regra

**Substituir não é apagar.**

# 61. Arquivo

Arquivar significa retirar um objeto do fluxo ativo sem eliminar o seu valor histórico.

Um objeto pode ser arquivado porque:

1. perdeu relevância;

1. foi substituído;

1. o projeto terminou;

1. a hipótese foi invalidada;

1. a seed não será explorada;

1. a decisão foi revertida;

1. o material deixou de ser operacional.

# 62. Reutilização

Antes de iniciar novo trabalho, os agentes devem procurar:

1. projetos semelhantes;

1. evidências relacionadas;

1. decisões anteriores;

1. padrões;

1. riscos recorrentes;

1. templates;

1. aprendizagens;

1. especialistas;

1. fontes;

1. falhas anteriores.

## Princípio

**O sistema deve lembrar antes de voltar a descobrir.**

# 63. Contexto de utilização

Conhecimento válido num contexto pode não ser aplicável noutro.

Cada conclusão relevante deve indicar:

1. segmento;

1. geografia;

1. momento;

1. canal;

1. dimensão;

1. tecnologia;

1. restrições;

1. população;

1. condições.

Isto evita generalizações inadequadas.

# 64. Atualidade

O conhecimento deve possuir indicação de atualidade quando o tempo puder alterar a sua validade.

## Classificações possíveis

1. Atual;

1. Provavelmente atual;

1. Necessita revisão;

1. Desatualizado;

1. Histórico.

A atualidade não é igual à qualidade.

Uma fonte antiga pode ser historicamente valiosa, mas inadequada para uma decisão atual.

# 65. Duplicação

Dois objetos semelhantes podem representar:

1. duplicação real;

1. confirmação independente;

1. versão posterior;

1. aplicação noutro contexto;

1. perspetiva contraditória.

O sistema não deve fundir automaticamente informação apenas por semelhança.

# 66. Regra de independência

Múltiplos objetos derivados da mesma fonte não equivalem a múltiplas fontes independentes.

## Exemplo

Dez artigos que repetem o mesmo comunicado representam uma origem principal, não dez evidências independentes.

Esta regra é especialmente importante para:

1. tendências;

1. notícias;

1. dados de mercado;

1. relatos;

1. investigação secundária.

# 67. Qualidade da fonte

A qualidade deve considerar:

1. proximidade ao acontecimento;

1. competência;

1. interesse direto;

1. método;

1. verificabilidade;

1. consistência;

1. transparência;

1. atualidade;

1. independência;

1. reputação contextual.

A reputação geral não substitui adequação à pergunta.

# 68. Conhecimento negativo

O Venture OS deve preservar também o que não funcionou.

## Exemplos

1. canal sem resultados;

1. hipótese invalidada;

1. entrevista inconclusiva;

1. segmento inadequado;

1. tecnologia inviável;

1. campanha falhada;

1. premissa errada;

1. processo excessivamente pesado.

Conhecimento negativo reduz repetição de erros.

# 69. Ausência de evidência

A ausência de evidência não deve ser automaticamente interpretada como evidência de ausência.

O sistema deve distinguir:

1. ainda não investigado;

1. investigado sem resultados;

1. difícil de observar;

1. ausência provável;

1. ausência fortemente sustentada.

# 70. Desconhecimento explícito

Questões importantes ainda sem resposta devem ser formalizadas.

## Unknown Record

Pode conter:

1. pergunta;

1. importância;

1. agente responsável;

1. impacto;

1. método possível;

1. urgência;

1. estado.

## Estados

1. Identificado;

1. Em investigação;

1. Parcialmente respondido;

1. Respondido;

1. Deixou de ser relevante;

1. Arquivado.

# 71. Sensibilidade da informação

Cada objeto pode ser classificado como:

1. Público;

1. Interno;

1. Confidencial;

1. Restrito.

A classificação influencia:

1. acesso;

1. partilha;

1. armazenamento;

1. exportação;

1. retenção;

1. utilização por agentes.

# 72. Princípio da minimização

O sistema deve guardar informação suficiente para cumprir a finalidade, mas não informação pessoal, sensível ou irrelevante apenas porque está disponível.

## Evitar

1. credenciais;

1. dados pessoais desnecessários;

1. segredos comerciais sem finalidade;

1. detalhes médicos irrelevantes;

1. informação familiar;

1. cópias integrais quando um resumo rastreável basta.

# 73. Acesso

O acesso ao conhecimento deve seguir:

1. necessidade;

1. função;

1. sensibilidade;

1. projeto;

1. duração;

1. risco.

O Archivist mantém a estrutura de acesso.

O CEO mantém autoridade sobre exceções materiais.

# 74. Retenção

A retenção deve variar conforme o objeto.

## Preservação longa

1. documentos oficiais;

1. decisões;

1. versões;

1. aprendizagens;

1. arquitetura;

1. protocolos;

1. riscos materializados;

1. histórico de alterações.

## Retenção limitada

1. gravações;

1. dados pessoais;

1. ficheiros temporários;

1. exports;

1. cópias de trabalho;

1. informação sensível sem utilidade futura.

# 75. Eliminação

A eliminação deve ser excecional para objetos institucionais.

Pode aplicar-se a:

1. duplicados confirmados;

1. dados pessoais sem necessidade;

1. ficheiros corrompidos;

1. material sem valor;

1. informação recolhida indevidamente;

1. credenciais expostas.

Quando relevante, deve existir registo de eliminação.

# 76. Papel do CEO

O CEO é responsável por:

1. aprovar documentos fundadores;

1. decidir sobre direções;

1. aceitar risco epistemológico;

1. determinar quando a confiança é suficiente;

1. autorizar promoções materiais;

1. rever decisões;

1. proteger o sistema contra falsa certeza.

O CEO não precisa de gerir todos os objetos.

# 77. Papel dos agentes

Os agentes são responsáveis por:

1. criar objetos adequados;

1. separar facto e interpretação;

1. indicar limitações;

1. relacionar conhecimento;

1. atualizar estados;

1. consultar memória existente;

1. sinalizar contradições;

1. preparar sínteses;

1. evitar duplicação.

# 78. Papel do Archivist

O Archivist é responsável pela integridade do sistema de conhecimento.

Compete-lhe:

1. manter taxonomia;

1. controlar identificadores;

1. preservar versões;

1. verificar relações;

1. gerir estados;

1. detetar duplicação;

1. sinalizar objetos órfãos;

1. proteger proveniência;

1. processar conhecimento transversal;

1. gerir arquivo;

1. produzir relatórios de saúde.

# 79. Objetos órfãos

Um objeto é órfão quando não possui relação suficiente com:

1. projeto;

1. responsável;

1. hipótese;

1. documento;

1. decisão;

1. origem;

1. finalidade.

O Archivist deve:

1. relacionar;

1. atribuir;

1. clarificar;

1. arquivar;

1. eliminar, quando apropriado.

# 80. Knowledge Health

A saúde do conhecimento pode ser avaliada através de:

1. objetos sem origem;

1. documentos sem versão;

1. decisões sem racional;

1. hipóteses sem evidência;

1. evidência não relacionada;

1. pressupostos desatualizados;

1. riscos sem responsável;

1. Knowledge Seeds abandonadas;

1. contradições não revistas;

1. documentos ativos incompatíveis;

1. excesso de informação não processada.

# 81. Knowledge Health Report

O Archivist deve produzir periodicamente uma vista contendo:

## Integridade

1. documentos oficiais completos;

1. versões ativas;

1. objetos sem proveniência;

1. ligações quebradas.

## Atualidade

1. conhecimento a rever;

1. fontes desatualizadas;

1. pressupostos antigos;

1. decisões com condição de revisão atingida.

## Coerência

1. contradições;

1. duplicações;

1. documentos incompatíveis;

1. estados ambíguos.

## Utilização

1. conhecimento reutilizado;

1. objetos nunca consultados;

1. Knowledge Seeds promovidas;

1. aprendizagens aplicadas.

# 82. Executive Knowledge View

O CEO deve receber apenas uma síntese.

## Estado do conhecimento

**Confiança geral:**
[Classificação]

**Principais conclusões:**
[Máximo de cinco]

**Principais incertezas:**
[Máximo de cinco]

**Pressupostos críticos:**
[Resumo]

**Contradições relevantes:**
[Resumo]

**Decisões dependentes:**
[Resumo]

**Conhecimento desatualizado:**
[Resumo]

**Ação necessária do CEO:**
[Decisão ou nenhuma]

# 83. Interface dos agentes

Cada agente deve conseguir consultar:

1. entradas aprovadas;

1. conhecimento confirmado;

1. pressupostos ativos;

1. riscos;

1. questões em aberto;

1. Knowledge Seeds relevantes;

1. decisões;

1. versões;

1. fontes;

1. aprendizagens.

Não deve receber todo o arquivo sem filtragem.

# 84. Pacote de contexto

Ao iniciar uma etapa, o agente deve receber um Context Package.

## Conteúdo mínimo

1. mandato;

1. Core Document ativo;

1. Decision Record;

1. Executive Summary;

1. conclusões confirmadas;

1. pressupostos;

1. riscos;

1. questões em aberto;

1. Knowledge Seeds autorizadas;

1. restrições;

1. critérios de sucesso.

# 85. Context Package vs arquivo

O Context Package contém o que o agente precisa agora.

O arquivo contém tudo o que o sistema preserva.

Esta distinção evita:

1. sobrecarga;

1. perda de foco;

1. utilização de versões antigas;

1. influência de ideias não aprovadas;

1. confusão entre histórico e estado atual.

# 86. Handoff de conhecimento

Cada Agent Handoff deve transferir:

1. conhecimento confirmado;

1. conhecimento provisório;

1. pressupostos ativos;

1. riscos;

1. contradições;

1. questões;

1. decisões;

1. Knowledge Seeds relevantes;

1. fontes essenciais;

1. limitações.

# 87. Regra de não herança silenciosa

Um agente não deve herdar automaticamente todas as interpretações do agente anterior.

Deve receber:

1. factos;

1. evidências;

1. conclusões;

1. confiança;

1. limitações.

Pode contestar interpretações dentro do seu mandato.

# 88. Memória do projeto

Cada projeto deve possuir uma estrutura lógica mínima.

## Project Knowledge Space

1. Charter;

1. Core Documents;

1. Decisions;

1. Evidence;

1. Hypotheses;

1. Assumptions;

1. Risks;

1. Knowledge Seeds;

1. Operational Artefacts;

1. Learning;

1. Handoffs;

1. Archive.

# 89. Memória do sistema

O Venture OS deve possuir uma área transversal.

## System Knowledge Space

1. Global Architecture;

1. Governance Charter;

1. Knowledge Architecture;

1. protocolos;

1. templates;

1. Agent Definitions;

1. System Learning Notes;

1. Change Log;

1. padrões reutilizáveis;

1. métricas;

1. incidentes;

1. versões;

1. biblioteca de métodos.

# 90. Conhecimento transversal

Um objeto pode ser promovido de conhecimento de projeto para conhecimento do sistema quando:

1. se repete em vários projetos;

1. melhora um protocolo;

1. revela uma falha estrutural;

1. representa um padrão reutilizável;

1. altera a definição de um agente;

1. justifica uma nova regra;

1. pode reduzir trabalho futuro.

A promoção deve ser avaliada pelo Archivist e aprovada quando material.

# 91. Conhecimento reutilizável

Pode assumir a forma de:

1. pattern;

1. playbook;

1. checklist;

1. método;

1. warning;

1. benchmark;

1. decisão típica;

1. risco recorrente;

1. template;

1. princípio;

1. exemplo.

Cada objeto reutilizável deve indicar limites de aplicabilidade.

# 92. Knowledge Pattern

Um Knowledge Pattern representa uma aprendizagem recorrente observada em vários contextos.

## Estrutura

1. nome;

1. descrição;

1. contextos;

1. evidências;

1. exceções;

1. condições;

1. aplicação;

1. riscos;

1. confiança;

1. projetos de origem.

# 93. Princípio da não generalização prematura

Um padrão observado num projeto não deve ser promovido automaticamente a regra geral.

A promoção exige:

1. repetição;

1. diversidade contextual;

1. revisão;

1. exceções conhecidas;

1. utilidade;

1. confiança adequada.

# 94. Aprendizagem por decisão

O sistema deve comparar:

1. decisão;

1. racional;

1. expectativa;

1. resultado;

1. desvio;

1. aprendizagem.

Isto permite avaliar a qualidade da decisão separadamente do resultado.

Uma boa decisão pode gerar um resultado negativo por fatores imprevisíveis.

Uma má decisão pode gerar um resultado positivo por sorte.

# 95. Decision Outcome Review

Após período relevante, decisões materiais devem poder receber uma revisão.

## Estrutura

1. decisão original;

1. resultado esperado;

1. resultado observado;

1. pressupostos confirmados;

1. pressupostos invalidados;

1. fatores externos;

1. qualidade do processo;

1. aprendizagem;

1. revisão necessária.

# 96. Aprendizagem por falha

Quando ocorre falha, o sistema deve perguntar:

1. O conhecimento estava incorreto?

1. A decisão ignorou conhecimento disponível?

1. O handoff foi incompleto?

1. O agente interpretou mal?

1. O protocolo era insuficiente?

1. A execução falhou?

1. O contexto mudou?

1. O risco era conhecido?

1. A monitorização foi tardia?

# 97. Aprendizagem por sucesso

O sucesso também deve ser analisado.

Perguntas:

1. O que funcionou?

1. Porquê?

1. Era esperado?

1. É replicável?

1. Dependeu de contexto especial?

1. Que riscos não se materializaram?

1. Que conhecimento deve ser preservado?

1. O resultado pode ter sido causado por fatores externos?

# 98. Atualização de agentes

Aprendizagens podem alterar:

1. instruções;

1. limites;

1. templates;

1. ferramentas;

1. métodos;

1. checklists;

1. critérios de escalada;

1. dashboards;

1. níveis de autonomia.

Alterações relevantes exigem System Change Record.

# 99. System Change Record

Deve incluir:

1. problema observado;

1. objetos afetados;

1. alteração proposta;

1. racional;

1. aprendizagem de origem;

1. impacto;

1. riscos;

1. aprovação;

1. versão resultante;

1. data de revisão futura.

# 100. Maturidade da Knowledge Architecture

## Nível 0 — Conversacional

Conhecimento reside principalmente em conversas.

## Nível 1 — Documentado

Existem documentos, mas poucas relações.

## Nível 2 — Estruturado

Existem objetos, códigos, estados e versões.

## Nível 3 — Relacional

Conhecimento está ligado através de proveniência e dependências.

## Nível 4 — Operacional

Agentes consultam, atualizam e reutilizam conhecimento sistematicamente.

## Nível 5 — Adaptativo

O sistema identifica lacunas, contradições e oportunidades de aprendizagem de forma contínua.

# 101. Estado atual do Venture OS

O Venture OS encontra-se entre:

**Nível 1 — Documentado**
e
**Nível 2 — Estruturado**

Já existem:

1. documentos fundadores;

1. taxonomia inicial;

1. códigos;

1. estados;

1. Evidence Records;

1. Decision Records;

1. Knowledge Seeds;

1. Learning Notes;

1. versionamento conceptual.

Ainda faltam:

1. implementação tecnológica;

1. ligações automáticas;

1. pesquisa unificada;

1. dashboards;

1. controlo de acessos;

1. alertas;

1. auditoria;

1. métricas de utilização.

# 102. Implementação mínima

A primeira implementação não necessita de um Knowledge Graph tecnológico completo.

Deve garantir apenas:

1. identificadores únicos;

1. tipos de objeto claros;

1. estados;

1. versões;

1. relações principais;

1. proveniência;

1. pesquisa;

1. distinção entre ativo e arquivo;

1. Executive Views;

1. responsabilidade do Archivist.

# 103. Regra de simplicidade

**A estrutura deve servir a utilização. Não deve existir apenas porque pode ser construída.**

Antes de criar um novo tipo de objeto, perguntar:

1. É diferente dos existentes?

1. Tem ciclo de vida próprio?

1. Precisa de autoridade distinta?

1. Será utilizado em decisões?

1. Melhora pesquisa ou rastreabilidade?

1. Compensa a complexidade adicional?

# 104. Critérios para criar um novo objeto

Criar um novo tipo apenas quando:

1. informação relevante está a ser perdida;

1. dois conceitos distintos estão misturados;

1. existe necessidade recorrente;

1. o estado precisa de ser acompanhado;

1. uma decisão depende dele;

1. o seu ciclo de vida é diferente;

1. a relação com outros objetos é importante.

# 105. Critérios de revisão da arquitetura

Este documento deve ser revisto quando:

1. agentes não encontram conhecimento;

1. versões antigas são utilizadas;

1. decisões não podem ser reconstruídas;

1. existe duplicação recorrente;

1. a Inbox cresce sem controlo;

1. o CEO recebe detalhe excessivo;

1. conhecimento importante não é reutilizado;

1. a taxonomia se torna pesada;

1. novos agentes exigem outros objetos;

1. surgem problemas de acesso ou privacidade.

# 106. Questões em aberto

A versão 0.1 ainda não define completamente:

1. tecnologia de armazenamento;

1. ferramenta de Knowledge Graph;

1. mecanismo de pesquisa semântica;

1. permissões por campo;

1. automatização do Archivist;

1. retenção quantitativa;

1. backups;

1. integração com ferramentas externas;

1. exportação entre sistemas;

1. formatos técnicos de metadados;

1. migração de conhecimento;

1. autenticação de proveniência;

1. critérios de confiança automatizados.

Estas decisões devem surgir após uso real.

# 107. Resumo estrutural

## Entrada

Informação, observações, dados, ideias e documentos.

## Estrutura

Knowledge Objects com identidade, estado e proveniência.

## Relação

Knowledge Graph com dependências e ligações.

## Síntese

Clusters, briefs, dashboards e conclusões.

## Autoridade

Core Documents, CEO Gates e Decision Records.

## Aprendizagem

Project Learning Notes e System Learning Notes.

## Memória

Archivist, versionamento, arquivo e reutilização.

# 108. Princípio final

**O Venture OS não deve apenas guardar informação. Deve conseguir demonstrar o que sabe, como sabe, onde ainda pode estar errado e que decisões foram tomadas a partir desse conhecimento.**
