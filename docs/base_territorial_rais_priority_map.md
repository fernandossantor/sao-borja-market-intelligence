# Mapa de prioridade dos pares RAIS

## Objetivo

Registrar decisões explícitas para os pares e unidades RAIS examinados, sem
transformar correspondência nominal em prova de linhagem e sem iniciar
reconstrução sem contrato conceitual suficiente.

## Evidências observadas

A auditoria `rais-lineage-20260729-174813` examinou 21 arquivos brutos, 112
arquivos processados e 86 pares candidatos. Os cinco produtos analíticos são
binariamente idênticos aos da execução `rais-lineage-20260729-045503`.

O único par declarado explicitamente no código é:

```text
RAIS SB 2024.csv → RAIS SB 2024.parquet
```

Esse par possui conteúdo equivalente nas 18.923 linhas e 58 colunas
examinadas. Seu papel semântico permanece `MICRODATA_CANDIDATE`, sustentado
somente pelo nome do arquivo.

Os outros pares XLSX/Parquet foram formados por nome de arquivo e aba. Essa
regra produz candidatos, não vínculos comprovados de linhagem.

## Resultados calculados

- 17 pares `CONTENT_EQUIVALENT`;
- 69 pares `VALUE_DIFFERENCE`;
- 41 unidades brutas `NO_NOMINAL_CANDIDATE`;
- 26 arquivos processados sem candidato;
- 27.550 células com perda de separador decimal;
- 1.074 células com perda de valor bruto;
- 49 outras diferenças;
- 2 arquivos XLS não avaliados;
- `promotion_allowed=0`.

Entre os 17 pares equivalentes, sete correspondem a abas de notas e dez possuem
conteúdo analítico aparente. Desses dez, somente `RAIS SB 2024` possui par
declarado explicitamente; os outros nove permanecem hipóteses nominais.

## Decisões

| Grupo | Quantidade | Decisão | Justificativa |
|---|---:|---|---|
| `RAIS SB 2024` | 1 | `CONTENT_EQUIVALENT_NO_REBUILD` | reconstrução não é necessária; autoridade e adequação permanecem não comprovadas |
| candidatos analíticos equivalentes | 9 | `HOLD_NOMINAL_LINEAGE_ONLY` | conteúdo equivalente não comprova vínculo de linhagem |
| abas de notas equivalentes | 7 | `NON_ANALYTICAL_EVIDENCE` | preservam contexto, mas não constituem produto analítico próprio |
| pares com diferenças | 69 | `BLOCK_REBUILD` | diferenças materiais e vínculo apenas candidato |
| unidades sem candidato nominal | 41 | `BLOCK_REBUILD` | ausência de entrada imediata mapeada |
| arquivos processados sem candidato | 26 | `BLOCK_REBUILD` | proveniência imediata não demonstrada |
| arquivos XLS não avaliados | 2 | `NOT_ASSESSED` | leitor específico indisponível |

Nenhuma decisão autoriza promoção, exclusão ou substituição de arquivo.

## Estimativas

Não há estimativa numérica adotada como resultado. A separação entre abas
analíticas e abas de notas usa o papel observado no nome da unidade apenas para
priorização, não como prova de conteúdo ou autoridade.

## Interpretações

A reconstrução não é a próxima ação adequada. O único par explicitamente
mapeado já é equivalente; os demais exigiriam inferir linhagem a partir de
nomes. Reconstruí-los agora criaria produtos aparentemente autorizados sem
evidência proporcional.

## O que pode ser concluído

- não existe produto RAIS que reúna necessidade de reconstrução, proveniência
  suficiente e contrato conceitual validado;
- os produtos divergentes devem permanecer bloqueados;
- `RAIS SB 2024` pode ser preservado como evidência equivalente, sem promoção;
- as duas execuções comparadas são `IDENTICAL` nos cinco produtos analíticos.

## O que não pode ser concluído

- que os pares nominais comprovem linhagem;
- que os exports RAIS derivem de `RAIS SB 2024`;
- que as diferenças compartilhem uma única causa ou regra de correção;
- que a fonte seja autoritativa ou comparável em toda a série;
- que qualquer produto esteja apto para `curated`.

## Validações e operações

Pipeline real executado:

```bash
make audit-base-territorial-rais-lineage
```

Execuções comparadas:

```text
anterior: rais-lineage-20260729-045503
atual:    rais-lineage-20260729-174813
classe:   IDENTICAL
```

Não houve operação externa, escrita no Drive, reconstrução ou promoção. Todos
os arquivos brutos, processados, exports e snapshots históricos foram
preservados.

## Recomendação

Encerrar a reconstrução RAIS como ação atual. Reabrir somente quando houver
contrato conceitual explícito e evidência de proveniência para um produto
específico, ou quando um consumidor concreto exigir uma tabela hoje bloqueada.
