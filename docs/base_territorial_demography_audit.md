# Auditoria inicial do bloco demográfico

## Objetivo

Auditar os candidatos demográficos já identificados no mapa de cobertura da Base Territorial Comum antes de escolher séries, calcular indicadores ou abrir nova coleta externa.

Esta etapa responde apenas:

- quais arquivos já aparecem associados à demografia;
- quais são relações primárias e quais são apenas relações secundárias;
- em que estágio do acervo cada arquivo se encontra;
- quais arquivos já possuem perfil estrutural local;
- quais tabelas apresentam sinais estimados de geografia, tempo e medida;
- quais verificações ainda faltam para construir uma camada curada.

Ela não valida substantivamente os dados.

## Entradas

```text
.data/audit/base_territorial/coverage_map/<execução>/coverage_file_inventory.csv
.data/audit/derived_products/<execução>/derived_file_profile.csv
.data/audit/derived_products/<execução>/derived_table_profile.csv
```

O comando escolhe, por padrão, a execução válida mais recente de cada raiz.

## Relações temáticas

### Primária

O arquivo tem `primary_block=demografia`.

### Secundária

O arquivo foi classificado primariamente em outro bloco, mas seu conteúdo ou metadado também inclui demografia em `matched_blocks`.

Uma relação secundária não equivale a uma fonte demográfica dedicada. Relatórios multitemáticos podem servir como contexto, mas não devem ser automaticamente usados como base de cálculo.

## Tipos de candidato

```text
RAW_SOURCE_CANDIDATE
DERIVED_PROCESSED_PRODUCT
ANALYTICAL_CONTAINER
DERIVED_EXPORT_PRODUCT
OTHER_CANDIDATE
```

Esses tipos descrevem o estágio do arquivo no acervo. Eles não indicam qualidade metodológica.

## Sinais estruturais

O módulo reaproveita a auditoria estrutural dos produtos derivados. Os sinais de geografia, tempo, medida e categoria decorrem dos nomes das colunas e são estimativas de utilidade estrutural.

Estados possíveis:

```text
CORE_SIGNALS_PRESENT
PARTIAL_CORE_SIGNALS
NO_CORE_SIGNAL_DETECTED
```

A presença dos três sinais centrais não comprova:

- fonte oficial;
- período correto;
- unidade de medida;
- abrangência geográfica;
- comparabilidade temporal;
- ausência de duplicidade ou revisão metodológica.

## Registro de decisão

Cada candidato recebe pendências explícitas para:

- fonte original;
- período de referência;
- unidade;
- abrangência geográfica;
- comparabilidade;
- reutilização na camada curada.

Até a revisão de conteúdo e de linhagem, nenhum candidato é considerado conceitualmente validado.

## Escopo esperado da futura curadoria

A auditoria deve permitir decidir quais fontes sustentam, quando disponíveis e metodologicamente compatíveis:

- população total;
- população urbana e rural;
- distribuição por sexo;
- distribuição por idade;
- estrutura domiciliar;
- densidade demográfica;
- crescimento intercensitário;
- distribuição territorial intramunicipal;
- comparação municipal, regional ou estadual.

A lista é um roteiro analítico. Ela não afirma que todas essas variáveis já estejam presentes no acervo.

## Execução

```bash
make audit-base-territorial-demography
```

Para substituir uma execução do mesmo dia:

```bash
python -m sbmi.demography_audit_cli --replace
```

Para analisar apenas candidatos primários:

```bash
python -m sbmi.demography_audit_cli --primary-only --replace
```

## Saídas

```text
.data/audit/base_territorial/demography/demography-audit-AAAAMMDD/
├── demography_candidate_inventory.csv
├── demography_table_profile.csv
├── demography_family_summary.csv
├── demography_decision_register.csv
└── demography_audit_summary.csv
```

### `demography_candidate_inventory.csv`

Registra arquivo, relação temática, estágio, papel, método de classificação, perfil estrutural e volume observado.

### `demography_table_profile.csv`

Registra as tabelas localmente perfiladas, os cabeçalhos e os sinais estruturais estimados.

### `demography_family_summary.csv`

Consolida arquivos, bytes, tabelas, linhas e disponibilidade de perfil por família e estágio.

### `demography_decision_register.csv`

Explicita pendências conceituais e a próxima ação recomendada para cada candidato.

### `demography_audit_summary.csv`

Separa indicadores observados, calculados e estimados.

## Limitações

- a auditoria depende da versão mais recente do mapa de cobertura;
- candidatos brutos que não estejam na captura local podem ficar sem perfil estrutural;
- nomes de arquivos e colunas não substituem metadados oficiais;
- produtos em `processed` e `exports` exigem rastreamento de linhagem até a fonte primária;
- relatórios multitemáticos são contexto até confirmação de adequação para cálculo;
- nenhuma tendência, taxa ou comparação é calculada nesta etapa;
- nenhuma nova fonte é coletada;
- nenhum arquivo bruto é modificado;
- nenhuma escrita é realizada no Google Drive.
