# Verificação oficial das fontes censitárias

## Objetivo

Verificar externamente se os 17 temas locais do Censo 2022 correspondem a temas e produtos publicados em plataformas oficiais do IBGE.

A etapa não declara que as planilhas locais sejam arquivos oficiais originalmente baixados. A auditoria interna mostrou que:

- os 17 arquivos foram gravados por `openpyxl`;
- todos receberam propriedades documentais na data da captura local;
- nenhuma planilha contém URL, hyperlink, rótulo de fonte ou instituição;
- a autoridade do arquivo local não foi estabelecida.

Por isso, a verificação distingue:

1. existência do tema e do produto na plataforma oficial;
2. identificação oficial do município e de seu código;
3. origem não comprovada do arquivo local;
4. necessidade de reconciliação dos valores com a fonte oficial.

## Fontes oficiais verificadas

```text
Panorama do Censo Demográfico 2022
https://censo2022.ibge.gov.br/panorama/?localidade=4318002

Catálogo de tabelas e publicações do Censo 2022
https://censo2022.ibge.gov.br/panorama/downloads.html?localidade=4318002

API de Localidades: município de São Borja (RS)
https://servicodados.ibge.gov.br/api/v1/localidades/municipios/4318002
```

Somente os domínios oficiais abaixo são aceitos pelo comando:

```text
censo2022.ibge.gov.br
servicodados.ibge.gov.br
```

## Registro temático

O registro associa cada dataset local a:

- instituição oficial;
- plataforma;
- código municipal 4318002;
- rótulo do tema no Panorama;
- título do produto de divulgação;
- data de divulgação;
- natureza do resultado: universo ou amostra preliminar.

A classificação entre universo e amostra é metodologicamente relevante. Resultados preliminares da amostra não devem ser comparados diretamente com resultados do universo sem explicação do desenho, da população de referência e das medidas utilizadas.

## Estados de verificação

### Autoridade externa

```text
OFFICIAL_PLATFORM_TOPIC_AND_PRODUCT_CONFIRMED
OFFICIAL_VERIFICATION_INCOMPLETE
```

O primeiro estado significa que foram localizados:

- o tema no Panorama;
- o produto no catálogo oficial;
- a data de divulgação;
- o município, a UF e o código 4318002 na API oficial de Localidades do IBGE.

### Origem do arquivo local

```text
LOCAL_FILE_ORIGIN_NOT_ESTABLISHED
LOCAL_FILE_ORIGIN_ESTABLISHED
```

A confirmação da plataforma não transforma automaticamente a planilha local em arquivo oficial. No estado atual, espera-se `LOCAL_FILE_ORIGIN_NOT_ESTABLISHED` para as 17 planilhas.

### Decisão para produtos processados

```text
REBUILD_FROM_OFFICIAL_SOURCE_REQUIRED
OFFICIAL_VALUE_RECONCILIATION_REQUIRED_BEFORE_CURATED_REUSE
```

Os dois produtos em quarentena, composição domiciliar e território, exigem reconstrução a partir da fonte oficial. Os quinze produtos equivalentes às planilhas locais ainda precisam ser confrontados com valores oficiais antes da reutilização curada.

## Execução

```bash
make verify-base-territorial-demography-census-authority
```

Para substituir a execução do mesmo dia:

```bash
python -m sbmi.demography_census_authority_cli --replace
```

## Captura das páginas oficiais

```text
.data/snapshots/web/demography_census_authority/
└── census-authority-AAAAMMDD/
    ├── panorama.html
    ├── downloads.html
    ├── municipality.json
    └── official_page_manifest.csv
```

O manifesto registra URL, status HTTP, tipo de conteúdo, tamanho e SHA-256.

## Saídas da auditoria

```text
.data/audit/base_territorial/demography_census_authority/
└── demography-census-authority-AAAAMMDD/
    ├── demography_census_official_registry.csv
    ├── demography_census_authority_verification.csv
    ├── demography_census_official_pages.csv
    └── demography_census_authority_summary.csv
```

## Limitações

- a presença de um tema na página oficial não prova equivalência dos valores locais;
- o parâmetro de localidade na URL não substitui a conferência dos valores municipais;
- a página Cidades e Estados é protegida por desafio automatizado do Cloudflare e
  retornou HTTP 403 na execução de 24 de julho de 2026; por isso, a identificação
  municipal usa a API oficial de Localidades do IBGE;
- datas de divulgação não são necessariamente datas de referência dos dados;
- produtos do universo e da amostra utilizam bases metodológicas diferentes;
- o catálogo oficial pode ser atualizado após a captura;
- os dois produtos em quarentena não são corrigidos nesta etapa;
- nenhuma tabela é considerada conceitualmente validada;
- nenhum arquivo bruto ou histórico é modificado;
- nenhuma escrita é realizada no Google Drive.

## Próxima etapa

Depois da confirmação externa, a sequência correta é:

1. capturar os downloads oficiais correspondentes aos dois produtos em quarentena;
2. documentar período, unidade, população e categorias;
3. comparar os valores oficiais com as planilhas locais;
4. reconstruir os produtos em nova camada, sem sobrescrever os históricos;
5. validar novamente esquema, valores e proveniência.
