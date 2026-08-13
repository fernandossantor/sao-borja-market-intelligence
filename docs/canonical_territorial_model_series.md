# Extensão canônica das séries territoriais

## Objetivo

Acrescentar ao modelo canônico estendido sete famílias já curadas e validadas,
sem modificar os builders históricos ou substituir produtos existentes.

## Entradas e decisões

- demografia histórica SIDRA: promover somente valores numéricos;
- demografia censitária SIDRA: preservar categorias multidimensionais e excluir
  ausências/supressões;
- PIB e VAB: manter séries metodológicas, tipos de valor e variáveis separados;
- empresas e emprego: preservar unidades e não equiparar vínculos a pessoas;
- educação: preservar categorias e periodicidades de origem;
- finanças públicas locais: manter estágio não comprovado e limitações;
- DCA/SICONFI: manter conta, dimensão e medida, sem somar hierarquias.

O canônico estendido anterior é preservado integralmente como entrada imediata.
Cada família recebe um `source_dataset` próprio; finanças públicas locais e DCA
oficial não são reconciliadas como equivalentes.

## Segurança e validação

A execução escreve primeiro em diretório parcial, promove atomicamente e recusa
sobrescrita. Geografia, contratos, valores numéricos, chaves e campos obrigatórios
são validados. O manifesto registra tamanhos e hashes calculados das entradas e
saídas; ele não comprova equivalência com manifestos upstream. Valores ausentes ou
suprimidos são registrados na reconciliação e não são convertidos em zero.

## Execução

```bash
make build-canonical-territorial-model-series \
  CANONICAL_SERIES_BASE_ROOT=.data/curated/base_territorial/canonical_extended/<execucao> \
  CANONICAL_DEMOGRAPHY_HISTORICAL_PATH=.data/curated/base_territorial/demography_historical_values/<execucao>/sidra_historical_values.csv \
  CANONICAL_DEMOGRAPHY_CENSUS_PATH=.data/curated/base_territorial/demography_census_series/<execucao>/demography_census_series.csv \
  CANONICAL_ECONOMY_GDP_PATH=.data/curated/base_territorial/economy_gdp_series/<execucao>/economy_gdp_series.csv \
  CANONICAL_BUSINESS_EMPLOYMENT_PATH=.data/curated/base_territorial/business_employment_series/<execucao>/business_employment_series.csv \
  CANONICAL_EDUCATION_PATH=.data/curated/base_territorial/education_series/<execucao>/education_series.csv \
  CANONICAL_PUBLIC_FINANCE_PATH=.data/curated/base_territorial/public_finance_series/<execucao>/public_finance_series.csv \
  CANONICAL_SICONFI_DCA_PATH=.data/curated/base_territorial/siconfi_dca_series/<execucao>/siconfi_dca_series.csv
```

O destino é `.data/curated/base_territorial/canonical_series`, sempre sob novo
identificador de execução. Todas as entradas são obrigatórias e explícitas; o
pipeline não seleciona automaticamente a execução mais recente nem mantém IDs
de checkpoint embutidos no código.
