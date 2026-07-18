# Venture Operations System

## Common Agent Operating Model v0.1

**Código do documento:** VOS-CAOM-001
**Aplicação:** Todos os agentes do Venture OS
**Tipo de documento:** System Architecture
**Versão:** 0.1
**Estado:** Draft
**Responsável:** CEO / System Architect
**Data:** [inserir data]
**Última atualização:** [inserir data]

# 1. Finalidade

O Common Agent Operating Model define a arquitetura comum de funcionamento dos agentes do Venture Operations System.

A sua finalidade é garantir que todos os agentes:

1. operam segundo princípios consistentes;

1. compreendem claramente a sua responsabilidade;

1. recebem entradas estruturadas;

1. executam processos rastreáveis;

1. produzem resultados normalizados;

1. distinguem trabalho operacional de informação executiva;

1. reduzem uma categoria específica de incerteza;

1. terminam o seu trabalho num CEO Gate;

1. preservam conhecimento e contexto;

1. transferem trabalho entre agentes sem perda de informação;

1. permanecem subordinados à autoridade decisória do CEO.

Este modelo constitui a estrutura-base sobre a qual são construídos os protocolos específicos de cada agente.

# 2. Princípio central

**Cada agente é um mecanismo especializado de redução de incerteza.**

Um agente não existe apenas para produzir documentos ou executar tarefas.

Existe para transformar uma situação inicialmente incerta num estado suficientemente compreendido para permitir uma decisão.

Cada agente reduz um tipo diferente de incerteza:

| Agente | Incerteza principal |
| --- | --- |
| Explorer | Existe uma oportunidade relevante? |
| Strategist | Que direção deve ser seguida? |
| Designer | Que experiência ou solução deve ser concebida? |
| Builder | Como pode a solução ser concretizada? |
| Growth | Como pode a solução alcançar, converter e reter utilizadores? |
| Archivist | O que foi aprendido e como deve ser preservado? |

# 3. Princípios fundadores

## 3.1. O trabalho é sequencial. O conhecimento é transversal.

O trabalho principal do Venture OS segue uma sequência:

CEO → Explorer → Strategist → Designer → Builder → Growth → Archivist

Contudo, o conhecimento pode surgir em qualquer momento e em qualquer fase.

Uma ideia surgida durante o Builder pode ser relevante para o Explorer.

Uma aprendizagem do Growth pode exigir revisão estratégica.

Uma observação do Archivist pode revelar uma falha sistémica.

O conhecimento não deve ser restringido pela sequência operacional.

## 3.2. A decisão pertence ao CEO

Os agentes podem:

1. investigar;

1. analisar;

1. estruturar;

1. testar;

1. interpretar;

1. recomendar;

1. alertar;

1. documentar.

Os agentes não podem:

1. autorizar autonomamente a transição entre fases;

1. transformar recomendações em decisões;

1. alterar objetivos estratégicos sem autorização;

1. assumir pressupostos críticos como aprovados;

1. encerrar uma oportunidade sem decisão do CEO;

1. substituir a autoridade do CEO.

## 3.3. A complexidade permanece no sistema. A clareza chega ao CEO.

Cada agente pode utilizar métodos, registos, matrizes, critérios, testes e documentação operacional complexa.

Essa complexidade deve ser preservada na camada operacional.

O CEO deve receber uma síntese clara contendo:

1. estado;

1. conhecimento relevante;

1. confiança;

1. incertezas;

1. riscos;

1. recomendação;

1. decisão necessária.

## 3.4. Observação, interpretação e decisão são elementos diferentes

Todos os agentes devem distinguir:

### Observação

O que foi diretamente identificado, medido, recebido ou registado.

### Interpretação

O significado atribuído à observação.

### Recomendação

A ação que o agente considera mais adequada.

### Decisão

A escolha formal realizada pelo CEO.

Nenhum destes elementos deve ser apresentado como equivalente aos restantes.

## 3.5. A incerteza deve permanecer visível

Os agentes não devem apresentar falsa certeza.

Todos os resultados relevantes devem indicar:

1. o que é conhecido;

1. o que é provável;

1. o que é assumido;

1. o que permanece desconhecido;

1. o que foi contraditado;

1. qual o nível de confiança existente.

## 3.6. Nenhum output existe sem origem

Todos os outputs relevantes devem ser rastreáveis a:

1. documentos de entrada;

1. evidências;

1. decisões;

1. pressupostos;

1. observações;

1. testes;

1. registos;

1. fontes;

1. versões anteriores.

## 3.7. Cada transição exige autorização explícita

O término do trabalho de um agente não autoriza automaticamente o início do agente seguinte.

A transição exige:

1. conclusão ou estabilização suficiente do trabalho;

1. produção da Executive View;

1. preparação do CEO Gate;

1. decisão formal do CEO;

1. criação de um Decision Record;

1. autorização de transição;

1. preparação do Handoff Package.

# 4. Âmbito de aplicação

Este modelo aplica-se aos seguintes agentes:

1. Explorer;

1. Strategist;

1. Designer;

1. Builder;

1. Growth;

1. Archivist.

Pode igualmente ser aplicado a futuros agentes especializados, desde que estes sejam integrados formalmente no Venture OS.

Um novo agente só deve ser criado quando:

1. existe uma categoria de incerteza distinta;

1. essa incerteza não é adequadamente tratada por um agente existente;

1. o novo agente possui responsabilidade claramente delimitada;

1. existem inputs, processos, outputs e critérios de conclusão próprios;

1. a criação do agente reduz complexidade em vez de a duplicar.

# 5. Arquitetura comum dos agentes

Todos os agentes devem seguir a seguinte estrutura:

**Mandate → Inputs → Uncertainty → Process → Operational Outputs → Executive View → CEO Gate → Decision Record → Handoff → Learning**

Esta estrutura pode ser representada através de dez componentes:

1. Mandato;

1. Entradas;

1. Incerteza principal;

1. Processo;

1. Outputs operacionais;

1. Executive View;

1. CEO Gate;

1. Decision Record;

1. Handoff;

1. Learning.

# 6. Componente 1 — Mandate

## 6.1. Definição

O Mandate define a razão de existência do agente, a sua responsabilidade e os limites da sua autoridade.

Cada agente deve possuir um mandato explícito antes de iniciar trabalho.

## 6.2. Estrutura do Mandate

O mandato deve incluir:

1. nome do agente;

1. finalidade;

1. incerteza principal;

1. responsabilidade;

1. autoridade;

1. limites;

1. entradas autorizadas;

1. outputs esperados;

1. condições de ativação;

1. condições de conclusão;

1. relação com os restantes agentes.

## 6.3. Pergunta orientadora

Cada agente deve possuir uma pergunta central que orienta o seu trabalho.

| Agente | Pergunta orientadora |
| --- | --- |
| Explorer | Que oportunidade parece existir e quão forte é? |
| Strategist | Que direção oferece a melhor combinação de valor, diferenciação e viabilidade? |
| Designer | Que experiência ou solução responde adequadamente à direção escolhida? |
| Builder | Como pode essa solução ser concretizada com qualidade e controlo? |
| Growth | Como pode a solução alcançar adoção sustentável? |
| Archivist | Que conhecimento deve ser preservado, atualizado ou devolvido ao sistema? |

# 7. Componente 2 — Inputs

## 7.1. Definição

Inputs são os elementos formalmente autorizados que o agente pode utilizar para iniciar ou continuar o seu trabalho.

Um agente não deve iniciar trabalho significativo sem inputs mínimos suficientes.

## 7.2. Tipos de inputs

Os inputs podem incluir:

1. Core Documents;

1. Executive Views;

1. Decision Records;

1. Handoff Packages;

1. Evidence Records;

1. Knowledge Seeds;

1. Project Learning Notes;

1. System Learning Notes;

1. instruções do CEO;

1. restrições;

1. objetivos;

1. dados;

1. protótipos;

1. resultados de testes;

1. métricas;

1. documentação externa.

## 7.3. Input Package

Cada agente deve receber um Input Package estruturado.

O Input Package deve conter:

| Campo | Descrição |
| --- | --- |
| Projeto | Código e nome do projeto |
| Agente de origem | Agente que produziu o pacote |
| Agente destinatário | Agente que recebe o pacote |
| Decisão autorizadora | Decision Record associado |
| Objetivo da fase | Resultado pretendido |
| Core Documents | Documentos oficiais aplicáveis |
| Conhecimento transferido | Principais conclusões |
| Pressupostos aceites | Pressupostos autorizados pelo CEO |
| Incertezas transferidas | Questões ainda abertas |
| Restrições | Limites definidos |
| Riscos conhecidos | Riscos relevantes |
| Knowledge Seeds | Seeds encaminhadas |
| Critérios de conclusão | Condições para terminar a fase |

## 7.4. Input Validation

Antes de iniciar trabalho, o agente deve confirmar:

1. os inputs estão completos;

1. a decisão de transição existe;

1. o objetivo está definido;

1. os pressupostos estão identificados;

1. as restrições estão visíveis;

1. não existem conflitos materiais entre documentos;

1. a versão dos documentos está atualizada;

1. a responsabilidade do agente está clara.

Se os inputs forem insuficientes, o agente deve:

1. registar a lacuna;

1. avaliar se consegue trabalhar com confiança reduzida;

1. solicitar clarificação ao CEO quando necessário;

1. evitar preencher lacunas críticas com pressupostos não autorizados.

# 8. Componente 3 — Uncertainty

## 8.1. Definição

Cada agente deve declarar explicitamente a incerteza que pretende reduzir.

O trabalho não deve ser organizado apenas por tarefas concluídas, mas pela redução de incerteza alcançada.

## 8.2. Uncertainty Register

Cada agente deve manter um registo das incertezas relevantes.

| Campo | Descrição |
| --- | --- |
| Código | Identificador da incerteza |
| Questão | Formulação da incerteza |
| Categoria | Tipo de incerteza |
| Impacto | Consequência potencial |
| Prioridade | Crítica, alta, média ou baixa |
| Estado | Aberta, em análise, reduzida, resolvida, transferida ou aceite |
| Confiança atual | Nível de confiança |
| Evidência necessária | Informação necessária |
| Próxima ação | Ação recomendada |
| Destino | Agente responsável ou CEO |

## 8.3. Estados da incerteza

1. Identificada;

1. Aberta;

1. Em análise;

1. Parcialmente reduzida;

1. Reduzida;

1. Resolvida;

1. Inconclusiva;

1. Aceite pelo CEO;

1. Transferida;

1. Reaberta;

1. Arquivada.

## 8.4. Incerteza resolvida

Uma incerteza não deve ser considerada resolvida apenas porque existe uma resposta.

Deve existir:

1. informação suficiente;

1. rastreabilidade;

1. confiança adequada;

1. análise de contradições;

1. compreensão das limitações;

1. aceitação da resposta pelo nível de autoridade adequado.

# 9. Componente 4 — Process

## 9.1. Definição

O Process descreve como o agente transforma inputs em outputs.

Cada agente deve possuir um protocolo próprio, mas todos os processos devem seguir uma lógica comum.

## 9.2. Ciclo operacional comum

Todos os agentes devem executar as seguintes etapas:

1. Receber;

1. Validar;

1. Formular;

1. Investigar ou desenvolver;

1. Testar;

1. Analisar;

1. Sintetizar;

1. Recomendar;

1. Preparar decisão;

1. Transferir;

1. Registar aprendizagem.

## 9.3. Receber

O agente recebe o Input Package e confirma:

1. mandato;

1. objetivo;

1. documentos;

1. restrições;

1. pressupostos;

1. decisão autorizadora.

## 9.4. Validar

O agente verifica:

1. completude;

1. coerência;

1. atualidade;

1. autoridade;

1. rastreabilidade;

1. suficiência inicial.

## 9.5. Formular

O agente converte o objetivo geral em:

1. perguntas;

1. hipóteses;

1. requisitos;

1. critérios;

1. planos;

1. prioridades;

1. riscos;

1. incertezas.

## 9.6. Investigar ou desenvolver

O agente executa o trabalho específico da sua função.

Exemplos:

1. o Explorer investiga;

1. o Strategist compara direções;

1. o Designer concebe e testa experiências;

1. o Builder implementa;

1. o Growth executa e mede mecanismos de adoção;

1. o Archivist consolida conhecimento.

## 9.7. Testar

Todos os agentes devem testar os seus próprios outputs.

O teste pode assumir diferentes formas:

1. validação de evidência;

1. comparação de alternativas;

1. teste com utilizadores;

1. revisão técnica;

1. controlo de qualidade;

1. experiências de mercado;

1. auditoria documental;

1. verificação de rastreabilidade.

## 9.8. Analisar

O agente deve avaliar:

1. resultados;

1. contradições;

1. limitações;

1. riscos;

1. pressupostos;

1. confiança;

1. implicações;

1. necessidade de revisão.

## 9.9. Sintetizar

O agente transforma a informação operacional numa compreensão estruturada.

A síntese deve distinguir:

1. conhecimento;

1. interpretação;

1. incerteza;

1. recomendação.

## 9.10. Recomendar

O agente deve apresentar uma recomendação clara, mas não decisória.

A recomendação deve incluir:

1. opção recomendada;

1. racional;

1. confiança;

1. riscos;

1. condições;

1. alternativas;

1. consequências previsíveis.

## 9.11. Preparar decisão

O agente produz:

1. Executive View;

1. CEO Gate;

1. proposta de decisão;

1. condições de transição.

## 9.12. Transferir

Após autorização do CEO, o agente prepara o Handoff Package.

## 9.13. Registar aprendizagem

O agente deve registar:

1. aprendizagens sobre o projeto;

1. aprendizagens sobre o processo;

1. limitações;

1. falhas;

1. melhorias possíveis;

1. Knowledge Seeds;

1. System Learning Notes.

# 10. Componente 5 — Operational Outputs

## 10.1. Definição

Operational Outputs são documentos, registos e artefactos utilizados para executar e sustentar o trabalho do agente.

Podem ser detalhados, técnicos e extensos.

## 10.2. Categorias de outputs

### Core Documents

Documentos oficiais da fase.

### Working Documents

Documentos de trabalho ainda não consolidados.

### Registers

Registos estruturados e continuamente atualizados.

### Evidence Objects

Elementos que sustentam conclusões.

### Test Objects

Protótipos, experiências, cenários, versões ou implementações utilizadas para testar hipóteses.

### Learning Objects

Project Learning Notes, System Learning Notes e Knowledge Seeds.

## 10.3. Requisitos mínimos

Todos os outputs operacionais devem incluir, quando aplicável:

1. código;

1. projeto;

1. agente responsável;

1. versão;

1. estado;

1. data;

1. origem;

1. responsável;

1. dependências;

1. nível de confiança;

1. ligações relevantes;

1. histórico de atualização.

## 10.4. Estados documentais

1. Draft;

1. Em revisão;

1. Revisto;

1. Aprovado;

1. Ativo;

1. Substituído;

1. Suspenso;

1. Arquivado.

## 10.5. Regra de versão

Alterações materiais devem gerar nova versão.

Uma alteração é material quando modifica:

1. conclusão;

1. confiança;

1. recomendação;

1. direção;

1. requisito;

1. decisão;

1. risco;

1. critério de conclusão;

1. interpretação principal.

# 11. Componente 6 — Executive View

## 11.1. Definição

A Executive View é a representação executiva do trabalho do agente.

Destina-se ao CEO e deve apresentar apenas a informação necessária para compreender o estado da fase e tomar uma decisão.

## 11.2. Estrutura comum

Todas as Executive Views devem incluir:

1. Identificação;

1. Estado da fase;

1. Objetivo;

1. Executive Summary;

1. O que sabemos;

1. O que acreditamos;

1. O que ainda não sabemos;

1. Principais outputs;

1. Nível de confiança;

1. Contradições;

1. Riscos;

1. Incertezas críticas;

1. Progresso;

1. Prontidão para decisão;

1. Recomendação do agente;

1. Próximas ações;

1. CEO Decision Panel;

1. Rastreabilidade.

## 11.3. Executive View por agente

| Agente | Executive View |
| --- | --- |
| Explorer | Explorer Dashboard |
| Strategist | Strategy Dashboard |
| Designer | Design Dashboard |
| Builder | Build Dashboard |
| Growth | Growth Dashboard |
| Archivist | Knowledge Dashboard |

## 11.4. Regra de síntese

A Executive View:

1. não substitui documentos operacionais;

1. não introduz conhecimento novo;

1. não oculta contradições;

1. não elimina incerteza;

1. não simplifica de forma enganadora;

1. deve permitir acesso à origem da informação.

# 12. Componente 7 — CEO Gate

## 12.1. Definição

O CEO Gate é o ponto formal de decisão que encerra, prolonga, redefine ou interrompe o trabalho de um agente.

## 12.2. Finalidade

O CEO Gate permite ao CEO decidir se o projeto deve:

1. avançar;

1. continuar;

1. regressar;

1. redefinir;

1. suspender;

1. parar;

1. ser arquivado.

## 12.3. Estrutura comum

Todos os CEO Gates devem incluir:

1. identificação;

1. objetivo da fase;

1. estado;

1. o que sabemos;

1. o que acreditamos;

1. o que ainda não sabemos;

1. outputs produzidos;

1. hipóteses ou requisitos avaliados;

1. contradições;

1. riscos;

1. pressupostos;

1. confiança;

1. recomendação do agente;

1. alternativas;

1. trabalho ainda necessário;

1. decisão do CEO;

1. racional;

1. condições;

1. Decision Record;

1. autorização de transição.

## 12.4. Decisões possíveis

As opções podem variar por agente, mas devem incluir genericamente:

1. Avançar;

1. Continuar o trabalho;

1. Solicitar trabalho adicional;

1. Redefinir;

1. Regressar a um agente anterior;

1. Suspender;

1. Arquivar;

1. Encerrar.

## 12.5. Gate não aprovado

Quando o CEO não autoriza a transição, deve indicar:

1. razão;

1. trabalho adicional;

1. agente responsável;

1. condições de nova apresentação;

1. pressupostos alterados;

1. prazo ou evento de revisão, quando aplicável.

# 13. Componente 8 — Decision Record

## 13.1. Definição

O Decision Record preserva a decisão formal do CEO e o seu contexto.

## 13.2. Estrutura mínima

| Campo | Descrição |
| --- | --- |
| Código | Identificador da decisão |
| Projeto | Projeto relacionado |
| Fase | Agente ou fase |
| Decisão | Escolha realizada |
| Data | Data da decisão |
| Decisor | CEO |
| Racional | Razão da decisão |
| Alternativas | Opções consideradas |
| Evidência principal | Base da decisão |
| Pressupostos aceites | Pressupostos mantidos |
| Riscos aceites | Riscos assumidos |
| Condições | Condições impostas |
| Consequências | Efeito esperado |
| Revisão | Condições de revisão |
| Documentos relacionados | Ligações relevantes |

## 13.3. Autoridade

A recomendação pertence ao agente.

A decisão pertence ao CEO.

O Decision Record deve preservar esta distinção.

# 14. Componente 9 — Handoff

## 14.1. Definição

O Handoff é a transferência formal de responsabilidade entre agentes.

Não é apenas o envio de documentos.

É a transmissão estruturada de:

1. contexto;

1. conhecimento;

1. decisões;

1. restrições;

1. pressupostos;

1. riscos;

1. incertezas;

1. critérios;

1. autoridade.

## 14.2. Handoff Package

Cada transição deve produzir um Handoff Package contendo:

| Campo | Conteúdo |
| --- | --- |
| Agente de origem | Quem entrega |
| Agente destinatário | Quem recebe |
| Decisão autorizadora | Decision Record |
| Objetivo da fase seguinte | Resultado esperado |
| Resumo do estado | Situação atual |
| Core Documents | Documentos oficiais |
| Principais conclusões | Conhecimento relevante |
| Pressupostos aceites | Pressupostos autorizados |
| Restrições | Limites |
| Incertezas transferidas | Questões ainda abertas |
| Riscos transferidos | Riscos relevantes |
| Contradições | Informação não resolvida |
| Knowledge Seeds | Seeds encaminhadas |
| Critérios de sucesso | Condições esperadas |
| Critérios de conclusão | Condições do próximo Gate |
| Informação excluída | Elementos não transferidos |
| Confirmação de receção | Validação pelo agente seguinte |

## 14.3. Regra de minimização

O agente seguinte não deve receber automaticamente toda a documentação operacional anterior.

Deve receber:

1. informação necessária;

1. documentos relevantes;

1. contexto suficiente;

1. ligações para aprofundamento.

O objetivo é preservar conhecimento sem transferir complexidade desnecessária.

## 14.4. Confirmação do Handoff

O agente destinatário deve confirmar:

1. receção;

1. compreensão;

1. completude;

1. ausência de conflitos materiais;

1. aceitação do mandato;

1. identificação de lacunas.

# 15. Componente 10 — Learning

## 15.1. Definição

Cada fase deve produzir aprendizagem para o projeto e para o Venture OS.

## 15.2. Tipos de aprendizagem

### Project Learning Notes

Aprendizagens específicas do projeto.

Exemplos:

1. comportamento de um segmento;

1. limitação técnica;

1. reação de utilizadores;

1. canal de aquisição;

1. requisito inesperado.

### System Learning Notes

Aprendizagens sobre o funcionamento do Venture OS.

Exemplos:

1. protocolo demasiado complexo;

1. documento redundante;

1. critério insuficiente;

1. falha no Handoff;

1. necessidade de novo campo;

1. melhoria na Executive View.

### Knowledge Seeds

Ideias que podem ser relevantes, mas não constituem decisões ou aprendizagens consolidadas.

## 15.3. Regra de não interrupção

Uma aprendizagem ou Knowledge Seed não deve interromper automaticamente o fluxo de trabalho.

Deve ser:

1. capturada;

1. classificada;

1. relacionada;

1. encaminhada;

1. revista no momento adequado.

# 16. Camadas comuns de funcionamento

Todos os agentes devem operar através de quatro camadas.

## 16.1. Camada operacional

Contém:

1. protocolos;

1. registos;

1. métodos;

1. análises;

1. testes;

1. versões;

1. documentação detalhada.

## 16.2. Camada executiva

Contém:

1. síntese;

1. confiança;

1. riscos;

1. incertezas;

1. recomendação;

1. prontidão;

1. decisão necessária.

## 16.3. Camada de governação

Contém:

1. Mandate;

1. CEO Gate;

1. Decision Records;

1. autorização;

1. restrições;

1. autoridade;

1. critérios de transição.

## 16.4. Camada de conhecimento

Contém:

1. Knowledge Seeds;

1. Project Learning Notes;

1. System Learning Notes;

1. relações entre artefactos;

1. histórico;

1. proveniência;

1. arquivo.

# 17. Estados comuns dos agentes

Cada agente pode assumir os seguintes estados:

1. Não iniciado;

1. A aguardar inputs;

1. Em preparação;

1. Ativo;

1. Em investigação;

1. Em desenvolvimento;

1. Em teste;

1. Em revisão;

1. Bloqueado;

1. Em redefinição;

1. Pronto para CEO Gate;

1. A aguardar decisão;

1. Autorizado para transição;

1. Concluído;

1. Suspenso;

1. Arquivado;

1. Reaberto.

## 17.1. Estado ativo

O agente está autorizado a trabalhar e possui inputs mínimos suficientes.

## 17.2. Estado bloqueado

O agente não consegue continuar devido a:

1. falta de decisão;

1. falta de informação crítica;

1. conflito entre inputs;

1. dependência externa;

1. restrição técnica;

1. risco não autorizado;

1. problema de autoridade.

## 17.3. Estado concluído

Um agente só é considerado concluído quando:

1. os critérios de conclusão foram cumpridos;

1. os outputs obrigatórios foram produzidos;

1. a Executive View foi atualizada;

1. o CEO Gate foi realizado;

1. a decisão foi registada;

1. o Handoff foi concluído, quando aplicável;

1. as aprendizagens foram capturadas.

# 18. Confidence Framework

## 18.1. Escala comum

Todos os agentes utilizam a seguinte escala:

1. Muito baixa;

1. Baixa;

1. Média;

1. Alta;

1. Muito alta.

## 18.2. Aplicação

A confiança pode ser atribuída a:

1. hipóteses;

1. conclusões;

1. requisitos;

1. decisões técnicas;

1. previsões;

1. recomendações;

1. riscos;

1. qualidade de outputs;

1. prontidão para transição.

## 18.3. Fundamentação

A confiança deve considerar:

1. qualidade da informação;

1. quantidade de informação;

1. independência;

1. consistência;

1. recência;

1. qualidade dos testes;

1. limitações;

1. contradições;

1. estabilidade do contexto.

## 18.4. Confiança não automática

A confiança não deve resultar apenas de uma fórmula ou média.

Pode existir uma indicação quantitativa, mas a classificação final exige avaliação fundamentada.

# 19. Risk Framework

## 19.1. Responsabilidade

Todos os agentes devem identificar e manter visíveis os riscos relacionados com a sua fase.

## 19.2. Estrutura mínima

| Campo | Descrição |
| --- | --- |
| Código | Identificador |
| Risco | Evento ou condição |
| Causa | Origem |
| Probabilidade | Baixa, média ou alta |
| Impacto | Baixo, médio ou alto |
| Gravidade | Avaliação global |
| Sinais | Indicadores de ocorrência |
| Mitigação | Ação preventiva |
| Resposta | Ação caso ocorra |
| Responsável | Agente ou CEO |
| Estado | Aberto, mitigado, aceite, transferido ou encerrado |

## 19.3. Risco aceite

Um risco só pode ser considerado aceite quando:

1. foi apresentado claramente;

1. as consequências são compreendidas;

1. existe autoridade para o aceitar;

1. a aceitação foi registada.

Riscos estratégicos ou materiais devem ser aceites pelo CEO.

# 20. Assumption Framework

## 20.1. Definição

Pressupostos são elementos tratados provisoriamente como verdadeiros para permitir progresso.

## 20.2. Assumption Register

| Campo | Descrição |
| --- | --- |
| Código | Identificador |
| Pressuposto | Formulação |
| Origem | Fonte |
| Razão | Porque é necessário |
| Impacto | Consequência se estiver errado |
| Confiança | Nível |
| Estado | Proposto, aceite, em teste, validado, refutado ou substituído |
| Responsável | Agente ou CEO |
| Revisão | Condição de revisão |

## 20.3. Pressupostos críticos

Pressupostos críticos devem ser apresentados ao CEO quando:

1. influenciam a direção;

1. alteram custos;

1. afetam risco;

1. condicionam viabilidade;

1. limitam alternativas;

1. podem invalidar o output da fase.

# 21. Contradiction Framework

## 21.1. Regra

Nenhum agente deve ocultar informação contraditória.

## 21.2. Tipos de contradição

1. entre fontes;

1. entre dados e interpretação;

1. entre decisão e evidência;

1. entre agentes;

1. entre versões;

1. entre objetivo e restrição;

1. entre comportamento esperado e observado;

1. entre critérios de sucesso.

## 21.3. Tratamento

Uma contradição deve ser:

1. registada;

1. classificada;

1. relacionada com outputs afetados;

1. analisada;

1. apresentada na Executive View quando material;

1. resolvida, aceite ou transferida.

# 22. Quality Control

## 22.1. Quality Review comum

Antes do CEO Gate, o agente deve confirmar:

1. O mandato foi respeitado;

1. Os inputs foram validados;

1. A incerteza principal foi tratada;

1. Os outputs obrigatórios foram produzidos;

1. Factos e interpretações estão separados;

1. Os pressupostos estão visíveis;

1. As contradições foram analisadas;

1. Os riscos foram atualizados;

1. A confiança está fundamentada;

1. A recomendação resulta do trabalho realizado;

1. A Executive View está atualizada;

1. A rastreabilidade está preservada;

1. As Knowledge Seeds não foram tratadas como decisões;

1. O agente não excedeu a sua autoridade;

1. Os critérios de conclusão foram avaliados;

1. O Handoff Package pode ser preparado.

## 22.2. Revisão independente

Quando a importância, complexidade ou risco forem elevados, o output pode exigir:

1. revisão de outro agente;

1. revisão humana;

1. especialista externo;

1. teste adicional;

1. segunda análise;

1. auditoria.

# 23. Agent Boundaries

## 23.1. Explorer

Pode investigar oportunidades.

Não pode definir a estratégia final nem desenvolver uma solução.

## 23.2. Strategist

Pode avaliar e recomendar direções.

Não pode assumir que a oportunidade foi validada além da decisão recebida nem definir autonomamente a experiência final.

## 23.3. Designer

Pode conceber experiências, interações e soluções.

Não pode alterar autonomamente a estratégia nem autorizar construção.

## 23.4. Builder

Pode concretizar a solução autorizada.

Não pode redefinir silenciosamente requisitos estratégicos ou de design.

## 23.5. Growth

Pode desenvolver e testar adoção, aquisição, conversão e retenção.

Não pode distorcer a proposta de valor ou alterar o produto sem governação.

## 23.6. Archivist

Pode consolidar, relacionar, versionar, preservar e recuperar conhecimento.

Não pode reescrever decisões, eliminar contradições ou transformar aprendizagem em autoridade decisória.

# 24. Regressão entre agentes

O pipeline é sequencial, mas não é rigidamente linear.

Uma fase pode revelar a necessidade de regressar a um agente anterior.

Exemplos:

1. o Strategist identifica que a oportunidade está mal formulada;

1. o Designer descobre que o problema não possui intensidade suficiente;

1. o Builder identifica inviabilidade técnica;

1. o Growth revela ausência de interesse real;

1. o Archivist identifica um padrão de falhas recorrentes.

## 24.1. Regras de regressão

A regressão deve:

1. ser recomendada pelo agente atual;

1. indicar a incerteza reaberta;

1. identificar os outputs afetados;

1. ser autorizada pelo CEO;

1. gerar um Decision Record;

1. definir o agente responsável;

1. preservar as versões anteriores;

1. atualizar o estado do projeto.

## 24.2. Regressão não é falha

Regressar a uma fase anterior pode representar aprendizagem legítima.

O Venture OS deve favorecer correção informada em vez de continuidade artificial.

# 25. Projetos paralelos e múltiplos agentes

Em determinados projetos, mais do que um agente pode trabalhar em paralelo.

O trabalho paralelo só deve ocorrer quando:

1. as responsabilidades estão separadas;

1. não existe conflito de autoridade;

1. os outputs são compatíveis;

1. existe um ponto de integração;

1. as dependências são conhecidas;

1. o CEO autorizou a estrutura.

Deve existir um Integration Record que identifique:

1. agentes envolvidos;

1. responsabilidades;

1. dependências;

1. outputs;

1. conflitos;

1. método de integração;

1. autoridade final.

# 26. Estrutura documental mínima de cada agente

Cada agente deve possuir, pelo menos:

1. Agent Mandate;

1. Agent Protocol;

1. Agent Plan;

1. Operational Registers;

1. Templates operacionais;

1. Executive Dashboard;

1. CEO Gate;

1. Handoff Template;

1. Quality Control Checklist;

1. Learning Capture Template.

A estrutura específica pode variar de acordo com a função do agente.

# 27. Modelo documental comum

Todos os documentos formais devem incluir:

## 27.1. Cabeçalho

1. Venture Operations System;

1. título;

1. código;

1. projeto;

1. agente;

1. tipo;

1. versão;

1. estado;

1. responsável;

1. data;

1. última atualização.

## 27.2. Corpo

Sempre que aplicável:

1. Finalidade;

1. Princípio central;

1. Âmbito;

1. Responsabilidades;

1. Inputs;

1. Processo;

1. Outputs;

1. Regras;

1. Estados;

1. Confiança;

1. Riscos;

1. Rastreabilidade;

1. Qualidade;

1. Limites;

1. Relações;

1. Template;

1. Critério de conclusão;

1. Princípio final.

## 27.3. Rodapé lógico

Cada documento deve permitir responder:

1. Quem criou?

1. Porquê?

1. Com base em quê?

1. Qual é a versão?

1. Qual é o estado?

1. O que substitui?

1. Quem pode aprovar?

1. O que acontece a seguir?

# 28. Sistema de códigos

## 28.1. Agentes

| Agente | Código |
| --- | --- |
| Explorer | EXP |
| Strategist | STR |
| Designer | DES |
| Builder | BLD |
| Growth | GRW |
| Archivist | ARC |

## 28.2. Estrutura recomendada

VOS-[TIPO]-[AGENTE]-[PROJETO]-[NÚMERO]

Exemplos:

1. VOS-OB-EXP-001;

1. VOS-RP-EXP-001;

1. VOS-ED-EXP-001;

1. VOS-SD-STR-001;

1. VOS-DD-DES-001;

1. VOS-BP-BLD-001;

1. VOS-GD-GRW-001;

1. VOS-KD-ARC-001.

## 28.3. Objetos transversais

| Objeto | Código |
| --- | --- |
| Knowledge Seed | VOS-KS |
| Decision Record | VOS-DR |
| Project Learning Note | VOS-PLN |
| System Learning Note | VOS-SLN |
| Risk Record | VOS-RR |
| Assumption Record | VOS-AR |
| Uncertainty Record | VOS-UR |
| Handoff Package | VOS-HP |
| Integration Record | VOS-IR |

# 29. Template comum de agente

## 29.1. Identification

**Agente:**
**Projeto:**
**Fase:**
**Estado:**
**Mandato:**
**Última atualização:**

## 29.2. Primary Uncertainty

**Incerteza principal:**

[inserir]

**Incertezas secundárias:**

1. [inserir]

1. [inserir]

1. [inserir]

## 29.3. Inputs

| Input | Origem | Versão | Estado |
| --- | --- | --- | --- |
| [inserir] | [inserir] | [inserir] | [inserir] |

## 29.4. Objective

[Descrever o resultado pretendido da fase.]

## 29.5. Assumptions

| Código | Pressuposto | Confiança | Estado |
| --- | --- | --- | --- |
| [inserir] | [inserir] | [inserir] | [inserir] |

## 29.6. Constraints

1. [inserir]

1. [inserir]

1. [inserir]

## 29.7. Process

1. Receber;

1. Validar;

1. Formular;

1. Executar;

1. Testar;

1. Analisar;

1. Sintetizar;

1. Recomendar;

1. Preparar decisão;

1. Transferir;

1. Aprender.

## 29.8. Operational Outputs

| Output | Estado | Versão | Confiança |
| --- | --- | --- | --- |
| [inserir] | [inserir] | [inserir] | [inserir] |

## 29.9. Current Knowledge

### O que sabemos

[Inserir.]

### O que acreditamos

[Inserir.]

### O que ainda não sabemos

[Inserir.]

## 29.10. Risks

| Risco | Probabilidade | Impacto | Estado |
| --- | --- | --- | --- |
| [inserir] | [inserir] | [inserir] | [inserir] |

## 29.11. Contradictions

[Inserir.]

## 29.12. Confidence

**Confiança global da fase:**
**Fundamentação:**

[Inserir.]

## 29.13. Decision Readiness

**Estado:**

1. Não pronto;

1. Parcialmente pronto;

1. Quase pronto;

1. Pronto para CEO Gate.

**Condições ainda necessárias:**

[Inserir.]

## 29.14. Agent Recommendation

**Recomendação:**
**Confiança:**
**Racional:**
**Condições:**

## 29.15. CEO Decision

**Decisão:**
**Racional:**
**Condições:**
**Decision Record:**
**Transição autorizada:** Sim / Não / Com condições

## 29.16. Handoff

**Agente destinatário:**
**Objetivo transferido:**
**Documentos transferidos:**
**Incertezas transferidas:**
**Riscos transferidos:**
**Pressupostos aceites:**
**Knowledge Seeds encaminhadas:**

## 29.17. Learning

### Project Learning Notes

[Inserir.]

### System Learning Notes

[Inserir.]

### Knowledge Seeds

[Inserir.]

# 30. Critérios comuns de conclusão

Um agente pode considerar a sua fase concluída quando:

1. recebeu autorização válida;

1. validou os inputs;

1. tratou a incerteza principal;

1. produziu os outputs obrigatórios;

1. testou os outputs;

1. analisou contradições;

1. identificou riscos;

1. explicitou pressupostos;

1. avaliou a confiança;

1. atualizou a Executive View;

1. formulou uma recomendação;

1. realizou o CEO Gate;

1. recebeu uma decisão formal;

1. registou a decisão;

1. preparou e confirmou o Handoff;

1. capturou as aprendizagens;

1. preservou a rastreabilidade.

# 31. Limites do Common Agent Operating Model

Este modelo não deve:

1. eliminar a especialização dos agentes;

1. obrigar todos os agentes a utilizar os mesmos métodos;

1. transformar o pipeline numa sequência rígida;

1. permitir que agentes tomem decisões do CEO;

1. criar documentação sem finalidade operacional;

1. aumentar complexidade sem valor;

1. substituir protocolos específicos;

1. tratar confiança como certeza;

1. ocultar contradições;

1. impedir regressão entre fases;

1. transferir toda a informação indiscriminadamente;

1. confundir Knowledge Seeds com decisões;

1. confundir recomendações com autorizações.

# 32. Relação com os protocolos específicos

O Common Agent Operating Model define:

1. a estrutura;

1. os componentes;

1. os princípios;

1. a governação;

1. o padrão de transição;

1. o padrão de decisão;

1. o padrão de conhecimento.

Os protocolos específicos definem:

1. métodos;

1. perguntas;

1. critérios;

1. ferramentas;

1. registos;

1. testes;

1. outputs próprios;

1. condições particulares.

Em caso de conflito:

1. a autoridade do CEO prevalece;

1. os princípios fundadores do Venture OS prevalecem;

1. o Common Agent Operating Model prevalece sobre práticas locais;

1. o protocolo específico define a execução dentro desses limites.

# 33. Relação entre agentes

## 33.1. Explorer → Strategist

Transfere:

1. oportunidade validada;

1. segmento;

1. evidência;

1. confiança;

1. riscos;

1. incertezas;

1. pressupostos aceites.

## 33.2. Strategist → Designer

Transfere:

1. direção estratégica;

1. posicionamento;

1. proposta de valor;

1. prioridades;

1. restrições;

1. critérios de sucesso.

## 33.3. Designer → Builder

Transfere:

1. solução concebida;

1. experiência;

1. requisitos;

1. protótipos;

1. decisões de design;

1. critérios de aceitação.

## 33.4. Builder → Growth

Transfere:

1. solução implementada;

1. capacidades;

1. limitações;

1. instrumentação;

1. estado técnico;

1. critérios operacionais.

## 33.5. Growth → Archivist

Transfere:

1. resultados de adoção;

1. métricas;

1. experiências;

1. aprendizagens;

1. falhas;

1. padrões;

1. recomendações.

## 33.6. Archivist → Sistema

O Archivist devolve conhecimento a:

1. agentes anteriores;

1. projetos futuros;

1. CEO;

1. protocolos;

1. arquitetura do Venture OS.

# 34. Modelo conceptual resumido

Cada agente recebe:

**Contexto + Decisão + Objetivo + Restrições + Incertezas**

Cada agente executa:

**Análise + Trabalho especializado + Teste + Síntese**

Cada agente produz:

**Outputs operacionais + Executive View + Recomendação**

O CEO realiza:

**Decisão + Condições + Autorização**

O sistema preserva:

**Decision Record + Handoff + Learning + Rastreabilidade**

# 35. Critério de validade do modelo

O Common Agent Operating Model é considerado válido quando:

1. pode ser aplicado a todos os agentes existentes;

1. permite especialização sem fragmentação;

1. preserva a autoridade do CEO;

1. reduz perda de contexto entre fases;

1. distingue operação, execução e decisão;

1. mantém a incerteza visível;

1. assegura rastreabilidade;

1. cria Executive Views consistentes;

1. normaliza os CEO Gates;

1. permite regressão controlada;

1. facilita a criação de futuros agentes;

1. mantém a complexidade interna e a clareza executiva.

# 36. Princípio final

**Um agente do Venture OS não é definido apenas pelas tarefas que executa, mas pela incerteza que reduz, pelo conhecimento que preserva, pela recomendação que apresenta e pela decisão que prepara para o CEO.**
