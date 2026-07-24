# Base Territorial Comum — IDSC-BR 2025

## Objeto

Esta etapa retoma o módulo social da Base Territorial Comum a partir do arquivo `Base_de_Dados_IDSC-BR_2025.xlsx` e migra os builders históricos de resumo e factsheet para o pacote portátil `sbmi`.

## Delimitação

- fonte: arquivo IDSC-BR 2025 preservado em `raw/social`;
- período de referência: 2025;
- abrangência geográfica: município de São Borja;
- unidade: pontuação e posições conforme os campos do arquivo de origem;
- finalidade: reproduzir, caracterizar e tornar auditáveis os produtos históricos do IDSC.

## Captura da fonte

```bash
make snapshot-social-idsc-source
```

A rotina baixa somente:

```text
raw/social/Base_de_Dados_IDSC-BR_2025.xlsx
```

A captura é publicada em:

```text
.data/snapshots/sources/social_idsc/idsc-br-2025/
```

Controles:

- Google Drive API em modo somente leitura;
- correspondência exata do caminho no inventário;
- verificação de tamanho e SHA-256;
- publicação atômica;
- nenhuma alteração no arquivo bruto ou no Drive.

## Construção dos produtos

```bash
make build-social-idsc
```

Produtos:

```text
.data/curated/base_territorial/social/idsc/2025/
├── social_idsc_summary.csv
├── social_idsc_factsheet.csv
├── historical_comparison.csv
└── social_idsc_metadata.json
```

O builder:

1. lê a planilha `Todos os Dados`;
2. exige uma única linha correspondente a São Borja;
3. identifica as colunas `Goal N Score`;
4. produz o ranking dos ODS;
5. reproduz o factsheet histórico;
6. compara os resultados com os CSVs históricos preservados em `exports`.

## Natureza dos resultados

### Dados observados

- valores presentes na linha de São Borja;
- pontuação geral;
- classificação nacional;
- valores faltantes;
- pontuações dos ODS;
- número de linhas e colunas da fonte;
- hash da fonte.

### Dados calculados

- ordenação dos ODS;
- ranking interno dos ODS;
- identificação do ODS mais forte e mais fraco;
- contagem de classes.

### Classificação heurística do projeto

As classes abaixo reproduzem o builder histórico e **não são tratadas como nomenclatura oficial da fonte**:

- excelente: pontuação maior ou igual a 80;
- forte: maior ou igual a 70 e menor que 80;
- intermediário: maior ou igual a 50 e menor que 70;
- frágil: maior ou igual a 30 e menor que 50;
- crítico: menor que 30.

Essa natureza é registrada como:

```text
calculated_project_heuristic
```

## Comparação histórica

Os novos resultados são comparados, sem substituição, com:

```text
exports/social_idsc_summary.csv
exports/social_idsc_factsheet.csv
```

Classes de comparação:

- `IDENTICAL`;
- `DIFFERENT`;
- `MISSING_BASELINE`;
- `BASELINE_SCHEMA_MISMATCH`.

Uma divergência não autoriza substituição automática. Ela deve ser investigada como possível mudança de fonte, método, ordenação, tipo ou implementação.

## Limitações

- a metodologia oficial completa do IDSC-BR não é revalidada nesta etapa;
- a escala das pontuações é preservada conforme o arquivo, sem inferência adicional;
- as classes qualitativas são heurísticas internas;
- reprodução técnica não comprova validade causal ou substantiva;
- análises comparativas com outros municípios ou anos exigirão auditoria metodológica própria.
