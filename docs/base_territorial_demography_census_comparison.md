# Comparação de conteúdo dos arquivos do Censo 2022

## Objetivo

Comparar cada planilha `xlsx` capturada em `raw/social` com o produto `parquet` correspondente em `processed/social`.

A comparação testa a preservação estrutural e de valores entre a fonte armazenada e o produto derivado. Ela não valida a autoridade da fonte, a definição dos indicadores, o período, a unidade ou a comparabilidade.

## Entradas

```text
.data/audit/base_territorial/demography_lineage/<execução>/demography_lineage_register.csv
.data/snapshots/sources/demography_census/<captura>/
.data/snapshots/derived_products/<captura>/
```

Somente pares com o estado abaixo são comparados:

```text
MATCHED_ONE_TO_ONE_BY_NAME
```

## Canonicalização

A comparação aplica transformações controladas apenas para evitar diferenças de representação:

- cabeçalhos são convertidos para minúsculas, sem acentos e com separadores padronizados;
- espaços externos e sequências de espaços em textos são normalizados;
- números armazenados como texto com vírgula decimal são comparados numericamente;
- inteiros e decimais equivalentes, como `10` e `10.0`, são tratados como o mesmo valor;
- ausências são representadas de maneira uniforme.

Não são aplicadas:

- correções ortográficas;
- aproximações numéricas;
- arredondamentos adicionais;
- equivalências por sinônimos;
- mudanças de categoria;
- reordenação silenciosa das linhas.

## Estados de comparação

```text
EXACT_AFTER_CANONICALIZATION
ROW_ORDER_DIFFERS_ONLY
SCHEMA_MISMATCH
ROW_COUNT_MISMATCH
CELL_VALUE_MISMATCH
READ_ERROR
```

### `EXACT_AFTER_CANONICALIZATION`

Cabeçalhos, quantidade e ordem das linhas, valores e ausências coincidem após as normalizações documentadas.

### `ROW_ORDER_DIFFERS_ONLY`

O conjunto de linhas é igual, mas a ordem foi modificada. Esse estado não é considerado equivalência exata porque a transformação não está documentada.

### Demais estados

Indicam diferenças estruturais, de volume, de valores ou falha de leitura. As diferenças observadas são registradas até o limite configurado por dataset.

## Saídas

```text
.data/audit/base_territorial/demography_census_comparison/
└── demography-census-comparison-AAAAMMDD/
    ├── demography_census_dataset_comparison.csv
    ├── demography_census_column_comparison.csv
    ├── demography_census_cell_differences.csv
    └── demography_census_comparison_summary.csv
```

### Comparação por dataset

Registra:

- caminhos da fonte e do produto;
- aba observada;
- linhas e colunas;
- igualdade do conjunto e da ordem dos cabeçalhos;
- igualdade das ausências;
- hash SHA-256 da representação canônica;
- estado de equivalência;
- erros de leitura;
- pendência de autoridade e validação conceitual.

### Comparação por coluna

Registra presença, quantidade de valores não ausentes, tipos semânticos e igualdade dos valores por coluna.

### Diferenças de células

Registra linha, coluna, tipo e valor observado nos dois arquivos. O limite padrão é de 100 diferenças por dataset.

## Execução

```bash
make compare-base-territorial-demography-census
```

Para substituir a execução do mesmo dia:

```bash
python -m sbmi.demography_census_comparison_cli --replace
```

## Interpretação

A equivalência de conteúdo autoriza apenas a conclusão de que o produto `parquet` reproduz a planilha capturada segundo os critérios aplicados.

Ela não autoriza concluir que:

- a planilha é uma extração oficial intacta do IBGE;
- o conceito estatístico foi interpretado corretamente;
- a unidade é apropriada;
- os dados são comparáveis com outras edições;
- o indicador pode ser publicado sem notas metodológicas;
- a tabela pertence necessariamente ao bloco demográfico principal.

## Etapa posterior

Depois da comparação de conteúdo, cada dataset deverá receber revisão de metadados e conceito, incluindo:

- fonte institucional e URL de origem, quando disponível;
- tabela, variável ou publicação oficial correspondente;
- período de referência;
- unidade;
- população ou universo estatístico;
- abrangência geográfica;
- notas, categorias residuais e critérios de sigilo;
- comparabilidade temporal;
- decisão de inclusão na camada curada.

Nenhum indicador é calculado nesta etapa. Nenhuma fonte nova é coletada e nenhum arquivo do Drive é modificado.
