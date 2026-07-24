# Base Territorial Comum — IPS Brasil publicado

## Objeto

Este módulo incorpora os agregados municipais de São Borja nas edições originalmente publicadas do IPS Brasil em 2024, 2025 e 2026.

## Delimitação

- fonte: scorecard municipal público do site oficial do IPS Brasil;
- município: São Borja;
- código IBGE: `4318002`;
- período: edições de 2024, 2025 e 2026;
- unidade: pontuação de 0 a 100;
- conteúdo: índice geral, três dimensões e doze componentes;
- finalidade: registrar o retrato de 2026 e preservar as edições anteriores sem produzir comparações temporais metodologicamente indevidas.

## Contrato técnico observado

A plataforma atual é uma aplicação Phoenix LiveView. O botão de download depende do evento `open_download_modal`, e a série harmonizada depende de interações LiveView.

A paginação da tabela geral não se mostrou reproduzível por requisições HTTP simples. Em testes reais, o parâmetro `page` não expôs São Borja em 2024, embora o município estivesse disponível na plataforma.

O contrato adotado passa a ser o scorecard municipal direto:

```text
https://ipsbrasil.org.br/explore/scorecard/4318002?year=<ANO>
```

As três edições retornaram páginas distintas, contendo o município, o código IBGE, o marcador explícito do ano, três dimensões e doze componentes.

## Captura

```bash
make snapshot-social-ips-published
```

Saída padrão:

```text
.data/snapshots/web/social_ips/ips-brasil-published-2024-2026/
├── ips_brasil_scorecard_2024.html
├── ips_brasil_scorecard_2025.html
├── ips_brasil_scorecard_2026.html
└── web_manifest.csv
```

Controles:

- somente páginas públicas;
- município e código IBGE validados;
- marcador da edição validado;
- presença das quinze dimensões e componentes validada;
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
├── ips_published_summary_2024_2026.csv
├── ips_2026_summary.csv
└── ips_metadata.json
```

### Dados observados

- pontuação geral do IPS;
- pontuações das três dimensões;
- pontuações dos doze componentes;
- município e código IBGE;
- anos das edições;
- URLs, tamanhos e hashes das páginas.

### Dados calculados

- formato longo dos agregados;
- chaves normalizadas para integração técnica;
- classificação estrutural em índice, dimensão e componente.

Essa classificação estrutural serve à organização interna e não substitui a nomenclatura metodológica oficial.

## Indicadores individuais

Os nomes dos indicadores individuais aparecem no scorecard, mas seus valores numéricos não estão publicados no HTML capturado. Por isso, o módulo registra:

```text
individual_indicator_values_status=NOT_PUBLISHED_AS_NUMERIC_VALUES_IN_SCORECARD_HTML
```

Nenhum valor individual será inferido a partir de cor, classe visual, posição relativa ou outra característica gráfica.

## Comparabilidade

O IPS Brasil informa que as edições originalmente publicadas não são estritamente comparáveis devido a mudanças de indicadores e tratamentos estatísticos.

Por isso, o módulo registra:

```text
comparability_status=NOT_STRICTLY_COMPARABLE_ACROSS_EDITIONS
temporal_change_calculated=0
```

Não são calculadas taxas de crescimento, diferenças ou tendências entre essas edições.

## Série harmonizada

A série temporal oficial recalcula 2024 e 2025 com os indicadores e parâmetros de 2026. Ela é conceitualmente diferente das edições originalmente publicadas e será construída em módulo separado.

Situação atual:

```text
harmonized_series_status=NOT_INCLUDED_REQUIRES_LIVEVIEW_EVENT
```

## Limitações

- a estrutura HTML do scorecard pode mudar;
- o produto não contém valores dos indicadores individuais;
- a captura municipal não substitui a base nacional integral;
- o retrato atual e a série harmonizada não devem ser misturados;
- nenhum resultado autoriza inferência causal.
