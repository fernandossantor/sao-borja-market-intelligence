# Descoberta controlada de fontes oficiais para produtos censitários

## Objetivo

Capturar e inspecionar as páginas oficiais de resultados associadas aos dois
produtos demográficos em quarentena:

- composição domiciliar;
- território.

A etapa registra links observados nas páginas. Ela não baixa bases, não atribui
equivalência conceitual e não reconstrói produtos.

## Entradas oficiais

```text
Composição domiciliar e óbitos informados: Resultados do universo
https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-2022.html?edicao=41639&t=resultados

População e Domicílios - Primeiros Resultados
https://www.ibge.gov.br/estatisticas/sociais/populacao/22827-censo-demografico-2022.html?edicao=37225&t=resultados
```

As URLs foram observadas no catálogo oficial previamente capturado. A presença
de um link na página não comprova que ele corresponda às medidas das planilhas
locais.

## Execução

```bash
make discover-base-territorial-demography-census-official-products
```

## Saídas

```text
.data/snapshots/web/demography_census_official_products/
└── official-products-discovery-<data-hora>/
    ├── household_composition.html
    ├── population_households.html
    └── official_product_page_manifest.csv

.data/audit/base_territorial/demography_census_official_discovery/
└── official-products-discovery-<data-hora>/
    ├── official_product_link_register.csv
    ├── official_download_candidate_register.csv
    └── official_discovery_summary.csv
```

O manifesto registra título do produto, URL solicitada, URL final, status HTTP,
tipo de conteúdo, bytes, SHA-256 e arquivo local.

## Classificação dos links

```text
SIDRA_LINK
DIRECT_FILE_LINK
DOWNLOAD_PAGE_LINK
TABLE_OR_RESULTS_LINK
OTHER_OFFICIAL_LINK
NON_OFFICIAL_LINK
```

As classes são calculadas a partir do domínio, caminho e texto do link. Elas
servem apenas para triagem técnica. Todos os candidatos recebem:

```text
conceptual_equivalence_status=NOT_ASSESSED
```

## Controles

- captura restrita às duas URLs oficiais registradas;
- HTTPS obrigatório;
- timeout e limite de bytes;
- conteúdo HTML obrigatório;
- respostas HTTP de erro preservadas com corpo, status e SHA-256;
- desafios Cloudflare registrados sem tentativa de contorno;
- SHA-256 das respostas;
- publicação atômica;
- recusa de sobrescrita;
- nenhuma escrita no Google Drive;
- nenhum download de base;
- nenhuma modificação em arquivos brutos ou históricos.

## Limitações

- desafios automatizados podem impedir a captura;
- links gerados apenas por JavaScript podem não aparecer no HTML;
- uma página pode listar múltiplas tabelas sem correspondência inequívoca;
- domínio oficial não comprova adequação conceitual;
- nenhum valor local é validado nesta etapa.
