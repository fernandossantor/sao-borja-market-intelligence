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

A plataforma atual é uma aplicação Phoenix LiveView. O HTML recebido por uma requisição HTTP simples contém o município, o ano e os rótulos estruturais, mas não contém as pontuações numéricas dos agregados. Os valores são publicados somente depois que o navegador estabelece a conexão LiveView.

A paginação da tabela geral também não se mostrou reproduzível por requisições HTTP simples. Em testes reais, o parâmetro `page` não expôs São Borja em 2024, embora o município estivesse disponível na plataforma.

O contrato adotado é o scorecard municipal direto, renderizado em Chromium:

```text
https://ipsbrasil.org.br/explore/scorecard/4318002?year=<ANO>
```

A captura só é concluída quando o DOM renderizado contém:

- São Borja;
- o marcador explícito da edição;
- os quinze rótulos de dimensões e componentes;
- uma pontuação para cada um desses quinze rótulos;
- uma pontuação geral do IPS;
- ao menos dezesseis candidatos numéricos válidos na escala de 0 a 100.

## Preparação do navegador

A dependência do navegador é opcional porque os demais módulos do projeto não precisam de Chromium.

```bash
make bootstrap-browser
```

O comando instala:

- o pacote Python do Playwright;
- o Chromium compatível com a versão do Playwright;
- as bibliotecas de sistema exigidas pelo Chromium no Linux.

A instalação usa o modo oficial `playwright install --with-deps chromium`. No Codespace, a etapa de dependências do sistema pode acionar `apt` por meio de `sudo` e produzir uma saída extensa. O GitHub Actions continua executando os testes com renderizadores simulados e não baixa um navegador.

Um Chromium baixado sem as bibliotecas do sistema não é suficiente. Erros como `libatk-1.0.so.0: cannot open shared object file` indicam que o navegador foi instalado, mas suas dependências Linux ainda não foram instaladas.

Algumas imagens de Codespaces incluem repositórios APT de terceiros. Caso uma dessas fontes esteja inválida, como ocorreu com `dl.yarnpkg.com`, o script `scripts/install_playwright_chromium.sh` desativa temporariamente apenas os arquivos de configuração que apontam para essa origem, instala as dependências oficiais do Chromium e restaura os arquivos ao terminar. A fonte externa não é apagada nem alterada permanentemente.

## Captura

```bash
make snapshot-social-ips-published
```

Saída padrão:

```text
.data/snapshots/web/social_ips/ips-brasil-rendered-published-2024-2026/
├── ips_brasil_scorecard_2024.html
├── ips_brasil_scorecard_2024.txt
├── ips_brasil_scorecard_2025.html
├── ips_brasil_scorecard_2025.txt
├── ips_brasil_scorecard_2026.html
├── ips_brasil_scorecard_2026.txt
└── web_manifest.csv
```

O arquivo HTML preserva o DOM final. O TXT preserva o texto efetivamente visível no navegador e é a entrada usada pelo builder.

Controles:

- somente páginas públicas;
- município e código IBGE validados;
- marcador da edição validado;
- presença das quinze dimensões e componentes validada;
- presença das dezesseis pontuações validada;
- HTML e texto registrados separadamente com tamanho e SHA-256;
- publicação atômica;
- nenhuma operação no Google Drive.

A captura HTTP estática anterior, quando existir localmente em `ips-brasil-published-2024-2026`, deve ser preservada apenas como evidência técnica de que o HTML desconectado não contém o contrato numérico. Ela não é aceita pelo builder.

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
- URLs, tamanhos e hashes do DOM e do texto renderizados.

### Dados calculados

- formato longo dos agregados;
- chaves normalizadas para integração técnica;
- classificação estrutural em índice, dimensão e componente.

Essa classificação estrutural serve à organização interna e não substitui a nomenclatura metodológica oficial.

## Indicadores individuais

Os nomes dos indicadores individuais aparecem no scorecard, mas seus valores numéricos não estão publicados no texto renderizado. Por isso, o módulo registra:

```text
individual_indicator_values_status=NOT_PUBLISHED_AS_NUMERIC_VALUES_IN_RENDERED_SCORECARD
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
harmonized_series_status=NOT_INCLUDED_REQUIRES_SEPARATE_LIVEVIEW_FLOW
```

## Limitações

- a estrutura renderizada do scorecard pode mudar;
- a captura depende de Chromium e da conexão LiveView pública;
- o produto não contém valores dos indicadores individuais;
- a captura municipal não substitui a base nacional integral;
- o retrato atual e a série harmonizada não devem ser misturados;
- nenhum resultado autoriza inferência causal.
