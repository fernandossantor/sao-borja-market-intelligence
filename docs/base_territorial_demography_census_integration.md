# Integração dos produtos censitários reconstruídos

## Objetivo

Registrar a integração não destrutiva dos produtos censitários reconstruídos ao
modelo canônico da Base Territorial e comparar uma nova execução real com a
execução anterior.

## Evidências observadas

A reconstrução `demography-census-rebuild-20260729-001426` preserva dois
produtos em destino próprio:

- `household_composition.parquet`, SHA-256
  `f7a879aa4dec986f9bb2c2e8162794d45624de4265b29c80198fee4444605e43`;
- `territory.parquet`, SHA-256
  `87e15bc4db6637d25377ae1a09aa5b7567fa649a2505408a990244dff3ec83e1`.

O consumidor `canonical_territorial_model` usa diretamente esses dois arquivos.
O manifesto e a reconciliação da execução canônica registram os caminhos e
hashes de cada entrada separadamente.

A execução de verificação
`canonical-territorial-20260729-153151` foi criada em novo destino, sem
substituir `canonical-territorial-20260729-025938` ou qualquer produto
histórico.

## Resultados calculados

O modelo canônico contém cinco fatos censitários de São Borja, código IBGE
`4318002`, com referência em 2022:

| Indicador | Categoria | Valor | Unidade |
|---|---|---:|---|
| participação na composição domiciliar | domicílios com cônjuges sem filhos | 23,18 | percentual |
| participação na composição domiciliar | domicílios com 1 morador | 21,31 | percentual |
| participação na composição domiciliar | domicílios com cônjuges do mesmo sexo | 0,31 | percentual |
| área territorial | — | 3.616,69 | km² |
| densidade demográfica | — | 16,5 | habitantes por km² |

A execução nova produziu:

- 70 fatos territoriais;
- 36 indicadores distintos;
- um território;
- zero chaves de fato duplicadas;
- zero células nulas nos campos obrigatórios;
- zero arquivos históricos modificados.

Os seis produtos da execução nova e da execução anterior possuem SHA-256
idênticos:

- `canonical_manifest.csv`;
- `dim_indicator.parquet`;
- `dim_territory.parquet`;
- `fact_territorial_indicator.parquet`;
- `source_reconciliation.csv`;
- `validation_summary.csv`.

Os três Parquets também possuem esquemas e conteúdos idênticos quando lidos
como tabelas. A comparação é classificada como `IDENTICAL`.

## Estimativas

Não há estimativa adotada como resultado desta integração.

## Interpretações

A reconstrução corrigiu a escala decimal antes da transformação canônica. O
modelo consome os produtos reconstruídos em `curated`, mantém os históricos
como evidência e preserva a proveniência imediata por caminho e SHA-256.

A igualdade entre execuções demonstra reprodutibilidade para as entradas e o
código examinados. Ela não demonstra, isoladamente, autoridade da fonte,
validade conceitual ou comparabilidade com outros períodos e territórios.

## O que pode ser concluído

- os dois produtos censitários reconstruídos estão integrados ao consumidor
  canônico da Base Territorial;
- os cinco valores corrigidos são promovidos sem duplicidade ou nulos
  obrigatórios;
- a execução de verificação reproduziu integralmente a execução anterior;
- nenhum histórico foi substituído, movido ou excluído;
- não há diferença `UNEXPLAINED` entre as execuções comparadas.

## O que não pode ser concluído

- a integração não valida todos os demais produtos censitários;
- correspondência de conteúdo não prova autoridade ou linhagem completa;
- a execução não prova comparabilidade temporal ou territorial;
- não foi realizada publicação em sistema externo.

## Validações e operações

Pipeline real executado:

```bash
make build-canonical-territorial-model
```

Execuções comparadas:

```text
anterior: canonical-territorial-20260729-025938
atual:    canonical-territorial-20260729-153151
classe:   IDENTICAL
decisão:  preservar ambas; considerar a integração concluída
```

Não houve acesso ao Google Drive, Supabase ou outra fonte externa. Os
diretórios históricos e os artefatos anteriores em `.data` permaneceram
inalterados.

## Recomendação

Retirar a integração censitária da lista de pendências. A próxima prioridade
de curadoria permanece a definição da política para ocorrências repetidas nos
dados fiscais antes de sua promoção.
