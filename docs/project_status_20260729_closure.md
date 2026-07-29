# São Borja — Inteligência Mercadológica

## Fechamento do ciclo de estabilização em 29 de julho de 2026

Este documento registra o estado do projeto após a incorporação dos PRs #18 a
#21. Ele complementa, sem substituir, os pontos de situação anteriores e os
documentos metodológicos de cada módulo.

Referência local e remota confirmada:

```text
branch: main
commit: a5eaaf87673fd9eeb54bdb3a3d708d7c635afc52
último PR incorporado: #21
```

## Evidências observadas

### Repositório

- PR #18 incorporou o ponto de situação anterior;
- PR #19 registrou o encerramento da integração censitária;
- PR #20 definiu a política para repetições fiscais estaduais;
- PR #21 registrou o mapa de prioridade RAIS;
- o CI dos quatro PRs foi concluído com sucesso antes dos merges;
- a `main` local está sincronizada com `origin/main` e sem alterações pendentes.

### Demografia censitária

Os produtos `household_composition.parquet` e `territory.parquet` da execução
`demography-census-rebuild-20260729-001426` são consumidos pelo modelo canônico.
A execução `canonical-territorial-20260729-153151` reproduziu integralmente
`canonical-territorial-20260729-025938` nos seis produtos comparados.

A comparação foi classificada como `IDENTICAL`. Os cinco fatos censitários
corrigidos permanecem rastreados por caminho e SHA-256, sem substituição dos
produtos históricos.

### Política fiscal

A auditoria `fiscal-semantic-20260729-171147` registrou 10 grupos estaduais,
com 29 ocorrências estritamente repetidas de IPVA e 19 ocorrências excedentes.
A decisão por grupo é `PRESERVE_OCCURRENCES_BLOCK_AGGREGATION`.

Todas as ocorrências e linhas de origem foram preservadas. A agregação e a
promoção permanecem bloqueadas. Os produtos federais e históricos não afetados
pela mudança metodológica permaneceram `IDENTICAL` à execução anterior.

### RAIS

A auditoria `rais-lineage-20260729-174813` reproduziu os cinco produtos
analíticos da execução anterior com classificação `IDENTICAL`.

O mapa de prioridade definiu:

- `RAIS SB 2024`: `CONTENT_EQUIVALENT_NO_REBUILD`;
- nove candidatos analíticos: `HOLD_NOMINAL_LINEAGE_ONLY`;
- sete abas de notas: `NON_ANALYTICAL_EVIDENCE`;
- pares divergentes e unidades sem proveniência suficiente: `BLOCK_REBUILD`;
- dois arquivos XLS: `NOT_ASSESSED`.

Nenhum produto RAIS foi reconstruído ou promovido.

## Resultados calculados

- as cinco ações do ponto de situação anterior foram tratadas;
- as comparações finais de censo e RAIS são `IDENTICAL`;
- a mudança fiscal é `METHODOLOGY_CHANGE`, sem diferença `UNEXPLAINED`;
- os bloqueios de promoção permanecem ativos onde a evidência é insuficiente;
- não existe pendência urgente decorrente dos PRs #18 a #21.

## Estimativas

Não há estimativa numérica adotada como resultado neste fechamento.

## Interpretações

O projeto encerrou uma onda de estabilização, reconstrução pontual e auditoria.
A existência de arquivos brutos ou gaps em um mapa de cobertura não constitui,
isoladamente, justificativa para iniciar outra auditoria.

O mapa de cobertura `coverage-map-20260729` antecede parte dos encerramentos
deste documento. Ele continua útil como inventário diagnóstico, mas não deve ser
tratado como fila automática nem como prova do estado substantivo atual.

## O que pode ser concluído

- a integração censitária está concluída e reproduzível para as entradas
  examinadas;
- a política fiscal preserva evidências e impede agregação não sustentada;
- a reconstrução RAIS está encerrada como ação atual;
- diferenças relevantes estão classificadas e bloqueadas;
- arquivos históricos, brutos, processados, exports e snapshots não foram
  substituídos ou removidos nessas etapas.

## O que não pode ser concluído

- que todos os blocos temáticos estejam substantivamente completos;
- que os contratos fiscais ou RAIS bloqueados estejam aptos para curadoria;
- que o mapa de cobertura reflita integralmente o estado posterior ao PR #21;
- que presença, nome ou equivalência de conteúdo comprovem autoridade;
- que nova coleta externa seja necessária sem uma demanda concreta.

## Validações executadas

Nas etapas encerradas:

- `make build-canonical-territorial-model`;
- `make audit-base-territorial-fiscal-semantics`;
- `make audit-base-territorial-rais-lineage`;
- testes focais associados;
- `make verify`, com 199 testes e Ruff no estado incorporado pelos PRs #20 e
  #21;
- inspeção de manifestos, resumos, decisões, hashes e diferenças;
- CI aprovado nos PRs #18, #19, #20 e #21.

## Operações externas

As únicas escritas externas deste ciclo foram commits, pushes e operações nos
PRs autorizados. Não houve escrita, movimentação, sincronização ou exclusão no
Google Drive, nem publicação no Supabase.

## Estado de arquivos e artefatos

Este fechamento cria somente documentação versionada. Execuções locais novas
foram publicadas em destinos próprios dentro de `.data`, com recusa de
sobrescrita. Artefatos reconstruíveis de `.data` permanecem fora do Git.

## Próxima ação recomendada

Não iniciar nova auditoria genérica. O próximo trabalho deve partir de pelo
menos uma destas condições:

1. pergunta de negócio explicitamente priorizada;
2. consumidor ou produto com contrato definido;
3. evidência nova capaz de remover um bloqueio existente;
4. atualização de fonte que exija comparação classificada;
5. necessidade concreta de publicação.

Antes de coleta externa, reconstrução, promoção ou mudança arquitetural,
reapresentar objetivo, escopo, volume, destinos, riscos e validações para
autorização.
