# Revisão de qualidade dos produtos censitários

## Objetivo

Classificar os resultados da comparação entre as 17 planilhas `xlsx` capturadas e os 17 produtos históricos em `parquet`, distinguindo:

- reprodução de conteúdo confirmada;
- anomalia sistemática;
- produto que deve permanecer em quarentena;
- pendências de autoridade da fonte e validação conceitual.

A revisão não altera os produtos históricos e não corrige silenciosamente valores.

## Resultado observado em 24 de julho de 2026

A comparação real encontrou:

- 17 pares testados;
- 15 equivalentes após canonicalização controlada;
- 2 com divergências de valor;
- nenhuma divergência de esquema, quantidade de linhas ou valores ausentes;
- 5 células divergentes.

Os dois produtos divergentes são:

```text
Censo 2022 - Composição domiciliar - São Borja (RS)_Sheet1.parquet
Censo 2022 - Território - São Borja (RS)_Sheet1.parquet
```

Em todas as cinco células, o valor processado corresponde ao valor bruto multiplicado por 100:

```text
23.18   → 2318
21.31   → 2131
0.31    → 31
3616.69 → 361669
16.5    → 1650
```

O padrão é classificado como:

```text
SYSTEMATIC_DECIMAL_SCALE_ERROR
```

A classificação descreve a relação observada. Ela não prova qual etapa histórica causou o erro, porque o código original de transformação ainda não foi identificado.

## Estados de reutilização

### Produtos equivalentes

```text
CONTENT_EQUIVALENT_SOURCE_NOT_VALIDATED
```

Significa que o `parquet` reproduz a planilha capturada após normalização controlada de cabeçalhos e representações numéricas. Isso não comprova que a planilha seja uma fonte oficial ou metodologicamente suficiente.

### Produtos divergentes

```text
QUARANTINE_PROCESSED_PRODUCT
```

Os produtos em quarentena não devem sustentar cálculos, gráficos ou interpretações. A ação indicada é reconstruir a partir da planilha capturada, preservando os decimais, e validar novamente a equivalência.

## Classificação automática

A revisão considera erro sistemático de escala decimal quando:

1. todas as diferenças são numéricas;
2. nenhuma diferença utiliza valor bruto igual a zero;
3. a razão `processado ÷ bruto` é constante em todas as células divergentes;
4. o fator constante é `100` ou `0,01`.

Outros fatores constantes são classificados como diferença sistemática de escala numérica. Diferenças heterogêneas permanecem em revisão manual.

## Execução

```bash
make review-base-territorial-demography-census-quality
```

Para substituir a execução do mesmo dia:

```bash
python -m sbmi.demography_census_quality_review_cli --replace
```

## Saídas

```text
.data/audit/base_territorial/demography_census_quality/
└── demography-census-quality-AAAAMMDD/
    ├── demography_census_quality_register.csv
    ├── demography_census_quarantine_register.csv
    └── demography_census_quality_summary.csv
```

## Limitações

- a revisão identifica o padrão da divergência, mas não reconstrói a etapa histórica que o produziu;
- equivalência de conteúdo não valida a autoridade institucional da fonte;
- nenhuma tabela é considerada conceitualmente validada;
- os 15 produtos equivalentes continuam dependendo de revisão de origem, conceito, período, unidade e abrangência;
- os dois produtos divergentes não devem ser corrigidos por divisão direta sem reconstrução verificável a partir da fonte capturada;
- nenhuma escrita é realizada no Google Drive.
