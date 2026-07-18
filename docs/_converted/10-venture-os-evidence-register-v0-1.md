# Venture Operations System

## Evidence Register

**Documento:** Evidence Register
**Código:** VOS-EVR-EXP-001
**Projeto:** VOS-EXP-001
**Versão:** 0.1
**Estado:** Pronto para piloto
**Agente responsável:** Explorer
**Research Plan de referência:** VOS-RES-EXP-001 v0.1
**Interview Guide de referência:** VOS-INT-EXP-001 v0.1
**Protocolo aplicável:** VOS-PRO-EXP-001 v0.1

# 1. Finalidade

O Evidence Register é o repositório estruturado de evidências recolhidas durante a exploração do projeto VOS-EXP-001.

A sua função é garantir que as conclusões do Explorer podem ser:

1. verificadas;

1. rastreadas até à origem;

1. comparadas;

1. contestadas;

1. atualizadas;

1. utilizadas no Opportunity Brief;

1. utilizadas na Confidence Matrix;

1. apresentadas no CEO Gate.

O Evidence Register não é um arquivo de notas soltas.

É um sistema de controlo da qualidade do conhecimento produzido durante a exploração.

# 2. Princípio central

**Nenhuma conclusão deve parecer mais sólida do que a evidência que a suporta.**

O Evidence Register deve tornar visível:

1. o que foi observado;

1. quem ou o que originou a evidência;

1. em que contexto surgiu;

1. que interpretação foi feita;

1. que hipótese é afetada;

1. qual é a força da evidência;

1. que limitações existem;

1. se há evidência contraditória.

# 3. Unidade básica de registo

A unidade básica do Evidence Register é o **Evidence Record**.

Cada Evidence Record deve conter apenas uma observação principal.

Quando uma entrevista produz várias evidências distintas, devem ser criados vários registos.

## Exemplo

Uma pessoa afirma que:

1. depende de recomendações;

1. investiu 500 euros em anúncios sem retorno;

1. não sabe qual canal funciona melhor.

Estas observações devem originar três Evidence Records separados.

Não devem ser agregadas num único registo genérico.

# 4. Estrutura do código

Cada Evidence Record recebe um código único.

## Formato

**VOS-EV-[PROJETO]-[NÚMERO]**

## Exemplo

**VOS-EV-EXP-001-0001**

### Componentes

1. **VOS:** Venture Operations System;

1. **EV:** Evidence Record;

1. **EXP-001:** projeto;

1. **0001:** número sequencial.

Os códigos nunca devem ser reutilizados, mesmo quando um registo é invalidado.

# 5. Tipos de evidência

Cada registo deve ser classificado segundo o tipo principal de evidência.

## 5.1 Evidência observacional

Algo diretamente observado pelo investigador.

Exemplos:

1. processo manual;

1. utilização de várias ferramentas;

1. dificuldade em explicar uma oferta;

1. comportamento durante uma tarefa;

1. sequência real de pesquisa.

## 5.2 Evidência declarada

Informação relatada diretamente por um participante.

Exemplos:

1. descrição de uma dificuldade;

1. relato de uma experiência;

1. motivo declarado para uma decisão;

1. satisfação ou insatisfação;

1. consequência percebida.

## 5.3 Evidência comportamental

Uma ação real que demonstra relevância.

Exemplos:

1. contratação de um serviço;

1. repetição de uma pesquisa;

1. utilização recorrente de canais;

1. criação de processos improvisados;

1. abandono de uma alternativa;

1. pedido ativo de ajuda.

## 5.4 Evidência económica

Um comportamento com consequência financeira.

Exemplos:

1. pagamento;

1. perda de receita;

1. investimento;

1. custo de aquisição;

1. orçamento atribuído;

1. contratação;

1. compromisso financeiro;

1. desperdício mensurável.

## 5.5 Evidência documental

Informação proveniente de documentos ou registos.

Exemplos:

1. relatórios;

1. métricas;

1. faturas;

1. propostas;

1. históricos de campanha;

1. pesquisas;

1. dados de mercado;

1. documentação de processos.

## 5.6 Evidência digital pública

Informação proveniente de contextos públicos digitais.

Exemplos:

1. fóruns;

1. comunidades;

1. avaliações;

1. publicações;

1. comentários;

1. pedidos de recomendação;

1. tendências de pesquisa;

1. páginas de concorrentes.

## 5.7 Evidência experimental

Resultado obtido através de uma experiência estruturada.

Exemplos:

1. teste de procura;

1. landing page;

1. pré-compromisso;

1. teste de mensagem;

1. experiência de recrutamento;

1. protótipo;

1. comparação de alternativas.

Este tipo poderá ser mais relevante em fases posteriores.

## 5.8 Evidência contraditória

Informação que enfraquece, limita ou invalida uma hipótese.

A evidência contraditória pode pertencer simultaneamente a outro tipo.

Exemplo:

Uma entrevista pode ser classificada como evidência declarada e contraditória.

# 6. Níveis de evidência

O Evidence Register utiliza a hierarquia definida no Explorer Validation Protocol.

| Nível | Designação | Descrição |
| --- | --- | --- |
| 0 | Intuição | Opinião, pressuposto ou observação isolada |
| 1 | Indireta | Informação secundária ou contextual |
| 2 | Declarada | Relato direto de uma pessoa |
| 3 | Comportamental | Ação real e observável |
| 4 | Económica | Compromisso financeiro ou impacto económico |

O nível não determina sozinho a qualidade da evidência.

Uma evidência económica mal documentada pode ser menos útil do que uma evidência declarada detalhada e contextualizada.

# 7. Estado do Evidence Record

Cada registo deve possuir um estado.

| Estado | Significado |
| --- | --- |
| Capturado | Registo inicial ainda não revisto |
| Revisto | Conteúdo verificado e classificado |
| Consolidado | Integrado numa análise ou conclusão |
| Contestável | Existem dúvidas materiais |
| Contraditado | Outra evidência enfraquece diretamente o registo |
| Invalidado | Erro, duplicação ou origem não fiável |
| Arquivado | Mantido para histórico, sem uso ativo |

Um registo invalidado não deve ser apagado.

Deve permanecer acessível com a respetiva justificação.

# 8. Campos obrigatórios

Cada Evidence Record deve conter os seguintes campos.

## 8.1 Identificação

**Código da evidência:**
[VOS-EV-EXP-001-XXXX]

**Projeto:**
VOS-EXP-001

**Data de recolha:**
[AAAA-MM-DD]

**Data de registo:**
[AAAA-MM-DD]

**Responsável pelo registo:**
[Nome, função ou agente]

**Estado:**
[Capturado/Revisto/Consolidado/Contestável/Contraditado/Invalidado/Arquivado]

## 8.2 Origem

**Tipo de fonte:**
[Entrevista/Observação/Documento/Dado público/Experiência/Outro]

**Código da fonte:**
[Ex.: VOS-PAR-EXP-001-A03]

**Grupo:**
[A — Pequeno negócio / B — Potencial cliente / C — Intermediário / D — Fonte documental]

**Segmento:**
[Descrição específica]

**Origem concreta:**
[Entrevista, documento, página, relatório ou observação]

**Acesso à fonte:**
[Localização, referência ou ligação interna]

**Consentimento ou restrições:**
[Quando aplicável]

## 8.3 Observação factual

**Observação:**

[Descrever o que foi dito, feito, medido ou observado.]

A observação deve evitar:

1. inferências;

1. diagnósticos;

1. adjetivos vagos;

1. conclusões estratégicas;

1. linguagem de solução.

### Exemplo adequado

O participante publicou semanalmente em duas redes sociais durante quatro meses e não conseguiu identificar quantos clientes tiveram origem nessas publicações.

### Exemplo inadequado

O participante tem uma estratégia de marketing ineficaz.

A segunda frase é uma interpretação, não uma observação.

## 8.4 Contexto

**Situação em que ocorreu:**
[Descrição]

**Momento:**
[Quando ocorreu]

**Frequência:**
[Única/Ocasional/Recorrente/Contínua/Desconhecida]

**Duração:**
[Quando conhecida]

**Consequência observada ou relatada:**
[Descrição]

**Alternativa utilizada:**
[Descrição]

**Resultado obtido:**
[Descrição]

## 8.5 Quantificação

Preencher apenas quando existirem dados.

**Tempo investido:**
[Valor, intervalo ou desconhecido]

**Dinheiro investido:**
[Valor, intervalo ou desconhecido]

**Receita afetada:**
[Valor, intervalo ou desconhecido]

**Número de ocorrências:**
[Valor ou desconhecido]

**Número de alternativas testadas:**
[Valor ou desconhecido]

**Outro indicador:**
[Descrição]

Quando um valor for estimado pelo participante, deve ser identificado como estimativa.

## 8.6 Citação literal

**Citação autorizada:**

“[Frase literal do participante.]”

**Nível de fidelidade:**

1. Transcrição literal;

1. Registo aproximado;

1. Tradução;

1. Não aplicável.

As citações não devem ser retiradas do contexto de forma a alterar o seu significado.

## 8.7 Interpretação

**Interpretação do Explorer:**

[Explicar o que a observação poderá significar.]

### Regra

A interpretação deve utilizar linguagem de possibilidade.

Preferir:

1. pode indicar;

1. sugere;

1. é compatível com;

1. poderá reforçar;

1. levanta a hipótese de.

Evitar:

1. prova que;

1. demonstra definitivamente;

1. confirma sem dúvida.

## 8.8 Hipóteses relacionadas

**Hipóteses afetadas:**

1. H1 — Existência da oportunidade;

1. H2 — O problema não é apenas visibilidade;

1. H3 — Alguns segmentos sofrem mais;

1. H4 — As soluções atuais são fragmentadas;

1. H5 — Existe custo relevante de não resolução;

1. H6 — Existe procura por orientação;

1. H7 — O problema também existe do lado da procura;

1. H8 — O momento atual aumenta a relevância;

1. Nova hipótese.

**Efeito sobre a hipótese:**

1. Reforça;

1. Enfraquece;

1. Contradiz;

1. Contextualiza;

1. Não conclusivo;

1. Gera nova hipótese.

## 8.9 Classificação da evidência

**Tipo principal:**
[Observacional/Declarada/Comportamental/Económica/Documental/Digital pública/Experimental]

**É contraditória?**
[Sim/Não]

**Nível de evidência:**
[0–4]

**Relevância para a oportunidade:**
[Baixa/Média/Alta]

**Confiança no registo:**
[Muito baixa/Baixa/Média/Alta/Muito alta]

**Justificação da confiança:**
[Descrição]

## 8.10 Limitações

**Limitações conhecidas:**

1. memória imperfeita;

1. ausência de documentação;

1. participante próximo do projeto;

1. conflito de interesse;

1. exemplo isolado;

1. falta de quantificação;

1. resposta abstrata;

1. possível enviesamento de cortesia;

1. interpretação não confirmada;

1. fonte secundária;

1. amostra não representativa;

1. outra.

**Descrição das limitações:**
[Detalhe]

## 8.11 Relações

**Evidências relacionadas:**
[Códigos]

**Evidências que contradizem este registo:**
[Códigos]

**Knowledge Seeds relacionadas:**
[Códigos]

**Decision Records relacionados:**
[Códigos, quando existirem]

**Versão do Opportunity Brief afetada:**
[Versão]

## 8.12 Ação seguinte

**Ação recomendada:**

1. Nenhuma;

1. Procurar repetição;

1. Confirmar com documentação;

1. Realizar pergunta de seguimento;

1. Testar noutro segmento;

1. Procurar evidência contraditória;

1. Atualizar hipótese;

1. Atualizar Opportunity Brief;

1. Criar Knowledge Seed;

1. Invalidar registo;

1. Outra.

**Responsável:**
[Nome ou agente]

**Prazo ou condição:**
[Data ou condição]

# 9. Modelo completo de Evidence Record

## Evidence Record

**Código:** VOS-EV-EXP-001-[XXXX]
**Estado:** [Estado]
**Data de recolha:** [Data]
**Responsável:** [Responsável]

### Origem

**Tipo de fonte:** [Tipo]
**Código da fonte:** [Código]
**Grupo:** [Grupo]
**Segmento:** [Segmento]
**Origem concreta:** [Descrição]
**Restrições:** [Descrição]

### Observação factual

[Observação sem interpretação.]

### Contexto

**Situação:** [Descrição]
**Momento:** [Descrição]
**Frequência:** [Descrição]
**Alternativa utilizada:** [Descrição]
**Resultado:** [Descrição]

### Quantificação

**Tempo:** [Valor]
**Dinheiro:** [Valor]
**Receita afetada:** [Valor]
**Ocorrências:** [Valor]
**Outros dados:** [Descrição]

### Citação

“[Citação autorizada.]”

### Interpretação do Explorer

[Interpretação.]

### Relação com hipóteses

**Hipótese:** [Código]
**Efeito:** [Reforça/Enfraquece/Contradiz/Contextualiza/Não conclusivo]

### Classificação

**Tipo de evidência:** [Tipo]
**Nível:** [0–4]
**Relevância:** [Baixa/Média/Alta]
**Confiança:** [Nível]
**Justificação:** [Descrição]

### Limitações

[Descrição]

### Relações

**Evidências relacionadas:** [Códigos]
**Evidências contraditórias:** [Códigos]
**Knowledge Seeds:** [Códigos]

### Próxima ação

[Descrição]

# 10. Evidence Register principal

O registo central deve apresentar uma linha por Evidence Record.

| Código | Data | Fonte | Grupo | Segmento | Observação resumida | Hipótese | Efeito | Tipo | Nível | Relevância | Confiança | Estado |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VOS-EV-EXP-001-0001 | [Data] | [Fonte] | [Grupo] | [Segmento] | [Resumo factual] | [H#] | [Efeito] | [Tipo] | [0–4] | [Nível] | [Nível] | [Estado] |

Esta tabela funciona como índice.

O conteúdo completo de cada evidência deve permanecer no respetivo Evidence Record.

# 11. Research Participant Log

Para proteger a identidade e permitir rastreabilidade, os participantes devem possuir códigos próprios.

## Formato

**VOS-PAR-[PROJETO]-[GRUPO][NÚMERO]**

## Exemplos

1. VOS-PAR-EXP-001-A01 — pequeno negócio;

1. VOS-PAR-EXP-001-B01 — potencial cliente;

1. VOS-PAR-EXP-001-C01 — intermediário.

## Estrutura

| Código | Grupo | Segmento | Perfil | Data da entrevista | Consentimento | Relevância | Seguimento |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VOS-PAR-EXP-001-A01 | A | [Segmento] | [Descrição] | [Data] | [Estado] | [Alta/Média/Baixa] | [Sim/Não] |

Os nomes e contactos devem ficar separados do Evidence Register quando existirem requisitos de privacidade.

# 12. Source Register

As fontes documentais e públicas devem possuir um registo próprio.

## Formato do código

**VOS-SRC-[PROJETO]-[NÚMERO]**

## Exemplo

**VOS-SRC-EXP-001-001**

## Campos

1. código;

1. título;

1. autor ou organização;

1. data;

1. tipo de fonte;

1. localização;

1. data de acesso;

1. credibilidade;

1. relevância;

1. limitações;

1. Evidence Records associados.

# 13. Registo de evidência contraditória

Embora a evidência contraditória esteja integrada no Evidence Register, deve existir uma vista específica para facilitar a análise.

| Código | Hipótese afetada | Evidência contraditória | Segmento | Gravidade | Confiança | Consequência possível |
| --- | --- | --- | --- | --- | --- | --- |
| [Código] | [H#] | [Resumo] | [Segmento] | [Baixa/Média/Alta] | [Nível] | [Implicação] |

## Regra

Uma hipótese não deve ser classificada com confiança alta enquanto existir evidência contraditória relevante sem explicação.

# 14. Evidence Clusters

À medida que a investigação progride, evidências semelhantes podem ser agrupadas em **Evidence Clusters**.

Um cluster não substitui os registos individuais.

Serve para identificar padrões.

## Formato do código

**VOS-EVC-[PROJETO]-[NÚMERO]**

## Exemplo

**VOS-EVC-EXP-001-001 — Dependência de recomendações**

## Campos do cluster

**Código:**
[Identificador]

**Nome do padrão:**
[Descrição]

**Hipótese relacionada:**
[H#]

**Segmentos onde aparece:**
[Lista]

**Evidence Records incluídos:**
[Códigos]

**Número de fontes independentes:**
[Quantidade]

**Tipos de evidência presentes:**
[Lista]

**Evidência contraditória:**
[Códigos]

**Interpretação provisória:**
[Descrição]

**Confiança no padrão:**
[Nível]

**Limitações:**
[Descrição]

# 15. Regras de independência

Várias evidências não são necessariamente várias fontes independentes.

## Exemplo

Uma entrevista produz:

1. uma declaração;

1. uma captura de ecrã;

1. uma estimativa financeira.

Podem existir três Evidence Records, mas apenas uma fonte principal.

Para avaliar a força de um padrão, deve distinguir-se:

1. número de registos;

1. número de participantes;

1. número de fontes independentes;

1. diversidade de segmentos;

1. diversidade de métodos.

# 16. Regras para duplicação

Não criar novos registos quando:

1. a mesma observação foi copiada para outra síntese;

1. uma frase aparece em notas e transcrição;

1. um dado documental é repetido por várias páginas da mesma fonte;

1. uma interpretação é reformulada sem nova evidência.

Criar novo registo quando:

1. surge nova fonte independente;

1. existe novo comportamento;

1. aparece uma consequência diferente;

1. uma nova medição altera a força da evidência;

1. o mesmo padrão surge noutro segmento.

# 17. Avaliação da qualidade da fonte

Cada fonte deve ser avaliada segundo cinco dimensões.

## 17.1 Proximidade

A fonte viveu ou observou diretamente o acontecimento?

## 17.2 Atualidade

A informação é recente e ainda relevante?

## 17.3 Especificidade

A informação descreve um caso concreto?

## 17.4 Verificabilidade

Existem documentos, comportamentos ou dados que a sustentem?

## 17.5 Independência

A fonte é independente do fundador, da solução e das outras fontes?

### Escala opcional

| Pontuação | Significado |
| --- | --- |
| 1 | Muito fraca |
| 2 | Fraca |
| 3 | Moderada |
| 4 | Forte |
| 5 | Muito forte |

Esta pontuação não deve ser convertida automaticamente em nível de evidência.

# 18. Confidence Score auxiliar

O Venture OS pode utilizar uma pontuação auxiliar para ordenar registos, sem substituir julgamento humano.

## Dimensões

1. qualidade da fonte;

1. especificidade;

1. verificabilidade;

1. relevância;

1. independência;

1. atualidade.

Cada dimensão pode ser avaliada entre 1 e 5.

## Fórmula auxiliar

**Pontuação total máxima:** 30

| Resultado | Leitura indicativa |
| --- | --- |
| 6–11 | Evidência fraca |
| 12–17 | Evidência limitada |
| 18–23 | Evidência moderada |
| 24–27 | Evidência forte |
| 28–30 | Evidência muito forte |

## Regra de governação

A pontuação:

1. ajuda a ordenar;

1. ajuda a detetar registos frágeis;

1. não decide a confiança final;

1. não transforma relatos em factos;

1. não substitui evidência contraditória;

1. não deve ser apresentada ao CEO sem contexto.

# 19. Relação entre evidência e confiança

A confiança numa hipótese deve considerar:

1. força individual das evidências;

1. número de fontes independentes;

1. repetição do padrão;

1. diversidade dos segmentos;

1. presença de comportamento real;

1. presença de compromisso económico;

1. qualidade das fontes;

1. evidência contraditória;

1. explicações alternativas;

1. lacunas ainda existentes.

## Exemplo

Dez participantes afirmarem que “gostariam de ter mais clientes” não criam, por si só, confiança alta.

Três participantes que:

1. investiram dinheiro;

1. testaram várias alternativas;

1. mantêm um processo manual;

1. conseguem quantificar perdas;

podem produzir evidência mais forte.

# 20. Regras de interpretação

## 20.1 Não confundir frequência com intensidade

Um problema frequente pode ter baixo impacto.

Um problema raro pode ser crítico.

## 20.2 Não confundir insatisfação com mudança

Uma pessoa pode estar insatisfeita e continuar sem procurar alternativa.

## 20.3 Não confundir utilização com sucesso

Uma ferramenta usada regularmente pode ser apenas a opção disponível.

## 20.4 Não confundir pagamento com satisfação

O pagamento demonstra relevância económica, não demonstra que a alternativa funciona bem.

## 20.5 Não confundir opinião de especialista com comportamento do utilizador

A experiência de intermediários é relevante, mas não substitui evidência direta.

## 20.6 Não confundir ausência de concorrência com oportunidade

Pode significar:

1. falta de procura;

1. dificuldade técnica;

1. baixa capacidade de pagamento;

1. mudança comportamental excessiva;

1. mercado pouco atrativo.

# 21. Gestão de novas hipóteses

Quando uma evidência não se enquadrar nas hipóteses existentes, pode gerar uma nova hipótese.

## Processo

1. Registar a evidência;

1. marcar “Gera nova hipótese”;

1. descrever a hipótese provisória;

1. procurar evidência adicional;

1. avaliar se deve entrar formalmente no Research Plan;

1. obter decisão do Explorer ou CEO, conforme o impacto.

## Regra

Uma nova hipótese não deve alterar silenciosamente o foco da investigação.

# 22. Gestão de Knowledge Seeds

Quando uma evidência sugere uma solução, funcionalidade ou aplicação futura:

1. registar a evidência original;

1. criar uma Knowledge Seed separada;

1. ligar os dois objetos;

1. manter a solução fora da interpretação factual;

1. não alterar o Research Plan sem autorização.

## Exemplo

**Evidência:**
Vários participantes têm dificuldade em decidir que ação de marketing iniciar.

**Knowledge Seed:**
Ferramenta de diagnóstico que recomenda o próximo passo.

A seed não é uma conclusão da investigação.

# 23. Revisão após cada entrevista

Depois de cada entrevista, o Explorer deve:

1. criar ou atualizar o Participant Log;

1. produzir a ficha de síntese;

1. extrair Evidence Records;

1. separar observações de interpretações;

1. identificar citações;

1. ligar evidências às hipóteses;

1. registar contradições;

1. criar Knowledge Seeds quando necessário;

1. indicar perguntas de seguimento;

1. rever a qualidade da entrevista.

O registo deve ser concluído enquanto a memória da conversa está fresca.

# 24. Revisão periódica do Register

## Revisão após cinco entrevistas

Avaliar:

1. qualidade dos registos;

1. consistência de classificação;

1. perguntas que geram evidência;

1. duplicações;

1. hipóteses sem cobertura;

1. segmentos em falta.

## Revisão após dez entrevistas

Avaliar:

1. padrões emergentes;

1. Evidence Clusters;

1. contradições;

1. alterações ao Interview Guide;

1. necessidade de atualizar o Research Plan;

1. confiança provisória.

## Revisão final da exploração

Antes do CEO Gate:

1. todos os registos relevantes devem estar revistos;

1. registos frágeis devem estar identificados;

1. duplicações devem estar resolvidas;

1. clusters devem estar consolidados;

1. contradições devem estar visíveis;

1. as conclusões devem apontar para códigos concretos;

1. a Confidence Matrix deve ser justificável.

# 25. Quality Control Checklist

Antes de marcar um registo como “Revisto”, confirmar:

1. Contém apenas uma observação principal;

1. A observação está separada da interpretação;

1. A fonte está identificada;

1. O contexto está descrito;

1. A hipótese relacionada está indicada;

1. O efeito sobre a hipótese está classificado;

1. O nível de evidência está justificado;

1. A confiança não está sobrestimada;

1. As limitações estão registadas;

1. A existência de contradições foi verificada;

1. A citação está autorizada;

1. Dados pessoais desnecessários foram removidos;

1. A próxima ação está definida, quando necessária.

# 26. Exemplo de Evidence Record

## Evidence Record

**Código:** VOS-EV-EXP-001-0001
**Estado:** Revisto
**Data de recolha:** [Data]
**Responsável:** Explorer

### Origem

**Tipo de fonte:** Entrevista
**Código da fonte:** VOS-PAR-EXP-001-A01
**Grupo:** A — Pequeno negócio
**Segmento:** Profissional independente, serviços especializados
**Origem concreta:** Entrevista exploratória
**Restrições:** Citação anónima autorizada

### Observação factual

O participante afirmou que os últimos quatro clientes chegaram por recomendação. Não conseguiu identificar um canal alternativo que gerasse clientes de forma previsível.

### Contexto

**Situação:** Aquisição de clientes nos últimos seis meses
**Frequência:** Recorrente
**Alternativa utilizada:** Recomendações pessoais
**Resultado:** Aquisição irregular e dependente da rede existente

### Quantificação

**Tempo:** Não quantificado
**Dinheiro:** Não aplicável
**Receita afetada:** Não quantificada
**Ocorrências:** Quatro clientes referidos

### Citação

“Quando alguém me recomenda, normalmente corre bem. O problema é que não sei quando vai acontecer outra vez.”

### Interpretação do Explorer

A observação pode indicar dependência de um canal eficaz, mas pouco controlável e pouco previsível.

### Relação com hipóteses

**Hipóteses:** H1, H4 e H5
**Efeito:** Reforça provisoriamente

### Classificação

**Tipo de evidência:** Declarada
**Nível:** 2
**Relevância:** Alta
**Confiança:** Média
**Justificação:** Experiência concreta e recente, mas sem documentação ou quantificação económica.

### Limitações

1. fonte única;

1. ausência de dados financeiros;

1. não permite concluir que o padrão seja comum ao segmento.

### Relações

**Evidências relacionadas:** Nenhuma
**Evidências contraditórias:** Nenhuma
**Knowledge Seeds:** Nenhuma

### Próxima ação

Procurar repetição do padrão em outros profissionais independentes e investigar o impacto económico da irregularidade.

# 27. Exemplo de evidência contraditória

## Evidence Record

**Código:** VOS-EV-EXP-001-0002
**Estado:** Revisto
**Data de recolha:** [Data]
**Responsável:** Explorer

### Origem

**Tipo de fonte:** Entrevista
**Código da fonte:** VOS-PAR-EXP-001-A02
**Grupo:** A — Pequeno negócio
**Segmento:** Serviço local recorrente

### Observação factual

O participante afirmou que recebe clientes suficientes através de pesquisa local e recomendações, não investe em publicidade e não considera a aquisição de clientes um problema atual.

### Contexto

**Situação:** Operação dos últimos doze meses
**Frequência:** Contínua
**Alternativa utilizada:** Pesquisa local e recomendações
**Resultado:** Procura considerada suficiente

### Interpretação do Explorer

A oportunidade pode ter baixa relevância para negócios locais com procura recorrente, reputação estabelecida e boa presença em pesquisa local.

### Relação com hipóteses

**Hipóteses:** H1 e H3
**Efeito:** Enfraquece H1 como formulação ampla e reforça H3

### Classificação

**Tipo de evidência:** Declarada e contraditória
**Nível:** 2
**Relevância:** Alta
**Confiança:** Média
**Justificação:** Relato direto e contextualizado, ainda sem verificação documental.

### Limitações

1. caso individual;

1. negócio já estabelecido;

1. pode não representar negócios em fase inicial.

### Próxima ação

Investigar se maturidade, reputação e recorrência reduzem sistematicamente a intensidade do problema.

# 28. Outputs produzidos pelo Evidence Register

O Evidence Register deve permitir gerar:

1. contagem de evidências por hipótese;

1. contagem por segmento;

1. distribuição por nível;

1. lista de evidências económicas;

1. lista de evidências comportamentais;

1. lista de contradições;

1. padrões recorrentes;

1. clusters;

1. lacunas de investigação;

1. matriz de confiança;

1. referências para o Opportunity Brief;

1. referências para o CEO Gate.

# 29. Critério de prontidão para síntese

O Evidence Register está pronto para alimentar uma síntese quando:

1. os registos principais foram revistos;

1. as fontes estão identificadas;

1. observação e interpretação estão separadas;

1. existe cobertura das hipóteses prioritárias;

1. há evidência favorável e contraditória;

1. os segmentos podem ser comparados;

1. os padrões estão agrupados;

1. as limitações estão visíveis;

1. as conclusões podem apontar para evidências específicas.

# 30. Princípio final

**A memória pode inspirar uma hipótese. Apenas um registo rastreável pode sustentar uma decisão.**
