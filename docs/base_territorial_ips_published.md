# Base Territorial Comum — IPS Brasil publicado

## Objeto

Este módulo incorpora o perfil municipal de São Borja nas edições originalmente publicadas do IPS Brasil em 2024, 2025 e 2026.

## Delimitação

- fonte: tabela pública do site oficial do IPS Brasil;
- município: São Borja;
- código IBGE: `4318002`;
- período: edições de 2024, 2025 e 2026;
- unidade: preservada conforme cada campo publicado;
- finalidade: registrar o retrato de 2026 e preservar as edições anteriores sem produzir comparações temporais metodologicamente indevidas.

## Contrato técnico observado

A plataforma atual é uma aplicação Phoenix LiveView. O botão de download depende do evento `open_download_modal`, e a série harmonizada depende de interações LiveView. A tabela pública, porém, permanece disponível como HTML paginado por parâmetros de consulta.

O módulo usa páginas ordenadas por código IBGE:

```text
https://ipsbrasil.org.br/explore/data
?page=499
&per_page=10
&sort_by=code
&sort_order=asc
&year=<ANO>
```

A rotina exige que o código `4318002` esteja presente na página. Caso a paginação oficial mude, a captura é interrompida sem publicar resultados parciais.

## Captura

```bash
make snapshot-social-ips-published
```

Saída padrão:

```text
.data/snapshots/web/social_ips/ips-brasil-published-2024-2026/
├── ips_brasil_published_2024.html
├── ips_brasil_published_2025.html
├── ips_brasil_published_2026.html
└── web_manifest.csv
```

Controles:

- somente páginas públicas;
- código IBGE validado no conteúdo;
- status HTTP e tipo de conteúdo validados;
- SHA-256 e tamanho registrados;
- publicação atômica;
- nenhuma operação no Google Drive.

## Construção

```bash
make build-social-ips-published
```

Saída padrão:

```text
.data/curated/base_territorial/social/ips/published_2024_2026/
├── ips_published_editions_long.csv
├── ips_2026_full_profile.csv
├── ips_2026_summary.csv
└── ips_metadata.json
```

### Dados observados

- valores publicados na linha municipal;
- rótulos das colunas;
- município e UF apresentados;
- anos das edições;
- URLs, tamanhos e hashes das páginas.

### Dados calculados

- formato longo da tabela;
- chaves normalizadas para integração técnica;
- classificação estrutural em metadado, índice, dimensão, componente e indicador.

Essa classificação estrutural serve à organização interna e não substitui a nomenclatura metodológica oficial.

## Comparabilidade

O próprio IPS Brasil informa que as edições originalmente publicadas em 2024, 2025 e 2026 não são estritamente comparáveis devido a mudanças de indicadores e tratamentos estatísticos.

Por isso, o módulo registra:

```text
comparability_status=NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS
temporal_change_calculated=0
```

Não são calculadas taxas de crescimento, diferenças ou tendências entre essas edições.

## Série harmonizada

A série temporal oficial recalcula 2024 e 2025 com os 57 indicadores e parâmetros de 2026. Ela é conceitualmente diferente das edições originalmente publicadas e será construída em módulo separado.

Situação atual:

```text
harmonized_series_status=NOT_INCLUDED_REQUIRES_LIVEVIEW_EVENT
```

## Limitações

- a paginação HTML é um contrato público observado, mas pode mudar;
- as unidades ainda precisam ser vinculadas ao catálogo metodológico oficial;
- a captura municipal não substitui a base nacional integral;
- o retrato atual e a série harmonizada não devem ser misturados;
- nenhum resultado autoriza inferência causal.
