# Modelo canônico territorial

## Objetivo

Consolidar produtos já validados em `curated` num contrato longo e rastreável,
sem modificar entradas. O grão é território, período, indicador, categoria e
dataset de origem.

## Escopo inicial

- cinco valores do Censo 2022 reconstruído;
- dezessete pontuações ODS do IDSC-BR 2025;
- quarenta e oito pontuações IPS publicadas de 2024 a 2026.

Esses 70 fatos correspondem a 36 indicadores distintos: três censitários,
dezessete do IDSC e dezesseis do IPS repetidos nas três edições.

Dados fiscais ainda em `staging` não são consumidos. O resumo IPS 2026 é
`CONTENT_DUPLICATE` da série completa e excluído. Factsheet e comparação IDSC
são complementares e não geram fatos.

A duplicidade do resumo IPS 2026 é verificada por igualdade de esquema e
conteúdo com o recorte de 2026 da série completa. Os produtos excluídos são
registrados no manifesto e na reconciliação com caminho e SHA-256.

## Produtos e segurança

Cada execução cria `fact_territorial_indicator.parquet`, `dim_indicator.parquet`,
`dim_territory.parquet`, `source_reconciliation.csv`, `validation_summary.csv`
e `canonical_manifest.csv`. A escrita usa diretório parcial, promoção atômica
e recusa destinos existentes.

Os valores são observados nas entradas curadas; a mudança de formato é
calculada deterministicamente. Classes IDSC são heurísticas mantidas como
atributos. O IPS preserva `NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS`; não são
calculadas variações temporais. O modelo não prova comparabilidade ou causalidade.

## Execução

```bash
make build-canonical-territorial-model
```
