# Revisão temática e de linhagem do Censo 2022

## Objetivo

Relacionar as planilhas brutas do Censo 2022 armazenadas no Drive aos produtos `parquet` existentes em `processed/social`, corrigir a classificação temática e preparar uma captura local verificada antes de qualquer reutilização analítica.

A revisão distingue três questões diferentes:

1. **classificação temática:** qual bloco da Base Territorial Comum é o principal para cada tabela;
2. **linhagem nominal:** qual fonte bruta provavelmente originou cada produto processado;
3. **equivalência de conteúdo:** se valores, dimensões, unidades e notas foram preservados.

Somente as duas primeiras questões são tratadas nesta etapa. A equivalência de conteúdo continua pendente.

## Evidência observada na auditoria inicial

A primeira execução do módulo demográfico encontrou:

- 17 produtos processados associados ao Censo 2022;
- um arquivo `exports/census_profile.csv`;
- quatro relatórios PDF com relação demográfica secundária;
- nenhuma planilha bruta dedicada entre os candidatos selecionados.

Essa ausência não significava falta das fontes no Drive. As planilhas estavam em `raw/social`, mas a regra genérica desse caminho havia prevalecido sobre o conteúdo específico dos títulos.

## Revisão temática explícita

Os arquivos com o padrão abaixo passam por revisão específica antes da síntese de cobertura:

```text
raw/**/Censo 2022 - * - São Borja (RS).xlsx
processed/**/Censo 2022 - * - São Borja (RS)_Sheet1.parquet
```

A classificação principal é definida pelo assunto da tabela, e não apenas pela pasta `social` ou pela palavra `Censo`.

### Demografia como bloco principal

- composição domiciliar;
- crescimento populacional;
- pirâmide etária;
- população indígena;
- população por cor ou raça;
- população por sexo;
- população por situação do domicílio;
- população quilombola;
- população residente em favelas;
- território.

### Outros blocos principais com relação demográfica secundária

- **educação:** alfabetização e nível de instrução;
- **infraestrutura e conectividade:** características do entorno, características dos domicílios e meios de transporte mais usados;
- **saúde e condições sociais:** deficiência e autismo;
- **ambiente sociocultural e territorial:** população por religião.

Essa hierarquia evita dois erros:

- tratar toda tabela censitária como demografia primária;
- retirar da base demográfica variáveis que continuam relevantes como relações secundárias.

## Perfil técnico

`exports/census_profile.csv` registra nomes de arquivos, abas, dimensões e primeiras linhas. Ele é documentação técnica produzida por um perfilador histórico, não uma fonte substantiva independente.

Sua classificação correta é:

```text
primary_block=governanca_documentacao
analytical_candidate=false
```

## Identidade de dataset

A identidade nominal é calculada a partir do nome do arquivo:

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
- autoridade da fonte;
- período de referência;
- abrangência geográfica;
- comparabilidade temporal.

## Execução da revisão

Primeiro, reconstrua o mapa com a revisão temática:

```bash
python -m sbmi.base_territorial_coverage_cli --replace
```

Depois, gere o registro de linhagem:

```bash
python -m sbmi.demography_lineage_cli --replace
```

Saídas:

```text
.data/audit/base_territorial/demography_lineage/demography-lineage-AAAAMMDD/
├── demography_lineage_candidates.csv
├── demography_lineage_register.csv
├── demography_classification_corrections.csv
└── demography_lineage_summary.csv
```

## Captura seletiva das fontes brutas

A seleção exige simultaneamente:

- caminho iniciado por `raw/`;
- extensão `.xlsx`;
- título contendo `Censo 2022`;
- título contendo `São Borja (RS)`;
- caminho e chave temática sem duplicidade;
- quantidade esperada explicitamente validada.

Execução:

```bash
make snapshot-base-territorial-demography-census
```

Destino padrão:

```text
.data/snapshots/sources/demography_census/
└── census-2022-sao-borja-sources-20260724/
    ├── raw/...
    └── source_manifest.csv
```

A captura:

- usa a conta de serviço em modo somente leitura;
- seleciona caminhos exatos do inventário;
- valida tamanho e SHA-256 quando disponível;
- não transforma as planilhas;
- não modifica arquivos brutos;
- não escreve no Google Drive.

## Próxima etapa

Para os pares nominais um-para-um, a etapa seguinte será comparar:

- nomes e quantidade de abas;
- quantidade de linhas e colunas;
- cabeçalhos;
- valores;
- tipos;
- valores ausentes;
- unidades e notas;
- identificadores geográficos;
- transformação aplicada entre `xlsx` e `parquet`.

Somente depois dessa comparação uma tabela poderá avançar para curadoria.

## Limitações

- a revisão depende do inventário atual do Drive;
- nomes iguais podem ocultar versões diferentes;
- nomes diferentes podem representar o mesmo conteúdo;
- a correspondência atual é estrutural e nominal;
- os sinais de cabeçalho não substituem metadados oficiais;
- nenhuma nova fonte externa é coletada;
- nenhum arquivo bruto é modificado;
- nenhuma escrita é realizada no Drive;
- nenhum dataset é considerado conceitualmente validado nesta etapa.
