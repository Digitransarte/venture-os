# Venture Workspace V0.1 — release gates e evidências

**Estado: HOLD / não publicar.** Esta nota regista a revisão do código e dos dados realizada em 2026-10-17, sem autorização para merge, release, deploy, integração com dados de menores ou comercialização.

## O que já foi demonstrado

- Existe uma aplicação Streamlit na branch `feature/venture-workspace-v01-20261016` com Board, ficha Workspace, Experiências, Consumo IA, Viabilidade SaaS e SaaS Core.
- O GitHub Actions executa `compileall` da interface e os testes Python. Ver estado atual da PR #2 e do último workflow antes de qualquer revisão.
- A camada Core está restrita a `GET /v1/system/state?scope=venture-factory`. Não pode atualizar, apagar, aprovar ou executar operações; há um limite de resposta de 1 MB e rejeição de dados malformados/IDs duplicados.
- `VENTURE_WORKSPACE_DEMO=1` utiliza apenas um candidato sintético. A consulta real exige explicitamente `VENTURE_WORKSPACE_ENABLE_LIVE_READ=1` além de URL e token do Core no servidor.
- O conector Designeo OS devolveu **dois candidatos reais** com chaves/schema/campos essenciais compatíveis: `VF-LEARNING-01` e `VF-HORTA-01`. Isto **não** constitui teste HTTP direto do Streamlit.
- A aplicação não guarda conteúdo escolar. O formulário Consumo IA só admite resumos mensais agregados em sessão; preços e resultados são hipóteses inseridas pelo operador até reconciliação com fornecedor.
- O Learning OS não foi modificado. Os fluxos OpenRouter identificados em leitura foram documentados em `LEARNING_OS_AI_METERING_V01.md`.

## Bloqueios antes de qualquer publicação privada

| Gate | Estado | Evidência necessária |
| --- | --- | --- |
| Autenticação por identidade e escopo | BLOQUEADO | Credenciais de serviço com privilégio mínimo; proteção independente de rede / proxy e testes negativos de acesso |
| Core PR #30 / revisões atómicas | BLOQUEADO | Revisão autorizada da integração das alterações locais, CI na árvore reconciliada, sem contorno de bloqueios anteriores |
| Cópias de segurança e rollback | BLOQUEADO | Backup cifrado fora do host + ensaio de restauro + rollback de aplicação documentado |
| Dados reais no Streamlit | NÃO TESTADO | GET autenticado seguro em ambiente privado; apresentar ambos os candidatos sem publicar segredos |
| QA visual/browser e autenticação | PARCIAL | Teste desktop/mobile; nova vista Consumo IA por testar após bloqueio de execução remoto |
| Inventário de custos reais | NÃO MEDIDO | Consumos de fornecedor efetivamente agregados por operação, câmbio/faturas e origem verificável |
| Privacidade de menores | FORA DE ESCOPO DO WORKSPACE | Aprovação autónoma antes de convidar famílias externas; não copiar dados do Learning OS |
| Aprovação da publicação | NÃO DADA | Revisão humana do plano, âmbito, domínio e janela de alteração |

**Sem dependências adicionais em produção:** a PR permanece draft no repositório `Digitransarte/venture-os` e não se regista deployment ativo.

## Processo de validação recomendado

1. Rever código e dependências em ambiente isolado, sem acesso à base de dados real.
2. Verificar credenciais **dedicadas de leitura e com escopo**; não utilizar o token administrativo global em interfaces expostas.
3. Verificar segurança do acesso do browser (TLS, private access boundary, sessões, CSRF e limites de tentativas) antes de qualquer ligação ao Core.
4. Validar leitura contra os dois registos existentes, sem os duplicar nem atualizar.
5. Concluir restauro e rollback com prova e confirmar que nenhum serviço ativo muda durante a QA.
6. Fazer revisão final e aprovação humana separada para merge/deploy privado. O lançamento público é outro gate.

## Comportamento em caso de falha

- Core indisponível ou credenciais inválidas: mostrar erro genérico e **não** cair para dados fictícios sem identificá-los como demonstração.
- Erro de validação de registos: falhar fechado, sem reescrever dados.
- Dados de consumo incompletos: mostrar custos como desconhecidos; não preencher como custo zero.
- Falha de autenticação, restauro ou isolamento: **NO-GO** para qualquer exposição externa.

Não adicionar chaves API, faturas identificáveis, tokens ou dados pedagógicos ao repositório GitHub. O repositório Venture OS é público.
