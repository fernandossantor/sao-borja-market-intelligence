# Revisão de linhagem demográfica

## Objetivo

Relacionar as planilhas brutas do Censo 2022 armazenadas no Drive aos produtos `parquet` existentes em `processed/social`, antes de qualquer reutilização analítica.

A revisão usa identidade nominal normalizada e estágio do arquivo. Portanto, ela identifica correspondências prováveis, mas não comprova equivalência de conteúdo.

## Motivação

A auditoria inicial encontrou:

- 17 produtos processados do Censo 2022;
- um arquivo `exports/census_profile.csv`;
- quatro relatórios PDF com relação demográfica secundária;
- nenhuma fonte bruta do Censo entre os candidatos selecionados pelo mapa.

A ausência das planilhas brutas na seleção ocorreu porque `raw/social/*` havia sido classificado genericamente no bloco social. A revisão de linhagem não depende dessa classificação temática e procura explicitamente arquivos com o padrão:

```text
raw/social/Censo 2022 - *.xlsx
processed/social/Censo 2022 - *_Sheet1.parquet
```

## Identidade de dataset

A identidade é calculada a partir do nome do arquivo:

1. remove-se a extensão;
2. remove-se o sufixo `_Sheet<numero>` dos produtos processados;
3. normalizam-se acentos, caixa, espaços e pontuação.

Exemplo:

```text
raw/social/Censo 2022 - Crescimento Populacional - São Borja (RS).xlsx
processed/social/Censo 2022 - Crescimento Populacional - São Borja (RS)_Sheet1.parquet
```

Ambos produzem a mesma identidade nominal.

## Estados de linhagem

```text
MATCHED_ONE_TO_ONE_BY_NAME
RAW_ONLY
PROCESSED_ONLY
AMBIGUOUS_MULTIPLE_CANDIDATES
```

`MATCHED_ONE_TO_ONE_BY_NAME` significa apenas que existe uma planilha bruta e um produto processado com o mesmo nome normalizado.

Ele não comprova:

- igualdade de células;
- transformação correta;
- preservação de unidades;
- fonte oficial;
- período de referência;
- abrangência geográfica;
- comparabilidade temporal.

## Correções propostas ao mapa

A revisão gera uma tabela de recomendações, sem alterar silenciosamente o mapa de cobertura:

- planilhas `raw/social/Censo 2022 - *.xlsx` devem ser tratadas como fontes primárias do bloco demográfico;
- `exports/census_profile.csv` deve ser tratado como perfil técnico, e não como base demográfica substantiva;
- os produtos `processed/social/*.parquet` permanecem derivados até comparação com as fontes brutas.

## Execução

```bash
make audit-base-territorial-demography-lineage
```

Para substituir uma execução do mesmo dia:

```bash
python -m sbmi.demography_lineage_cli --replace
```

## Saídas

```text
.data/audit/base_territorial/demography_lineage/demography-lineage-AAAAMMDD/
├── demography_lineage_candidates.csv
├── demography_lineage_register.csv
├── demography_classification_corrections.csv
└── demography_lineage_summary.csv
```

## Próxima etapa

Para os pares nominais um-para-um, a próxima etapa é capturar seletivamente as planilhas brutas e comparar:

- nomes e quantidade de abas;
- quantidade de linhas e colunas;
- cabeçalhos;
- valores;
- tipos;
- valores ausentes;
- unidades e notas;
- identificadores geográficos;
- transformação aplicada entre `xlsx` e `parquet`.

Somente depois dessa comparação uma série poderá avançar para curadoria.

## Limitações

- a revisão depende do inventário atual do Drive;
- nomes iguais podem ocultar versões diferentes;
- nomes diferentes podem representar o mesmo conteúdo;
- a correspondência é estrutural e nominal;
- nenhuma nova fonte externa é coletada;
- nenhum arquivo bruto é modificado;
- nenhuma escrita é realizada no Drive;
- nenhum dataset é considerado conceitualmente validado nesta etapa.
