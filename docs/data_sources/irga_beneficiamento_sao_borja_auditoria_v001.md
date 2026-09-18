# IRGA — beneficiamento de arroz — subconjunto identificável de São Borja

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Construir um indicador territorial conservador de beneficiamento de arroz associado a São Borja usando duas fontes independentes:

1. **IRGA** — ranking oficial anual das indústrias de beneficiamento;
2. **Sindarroz-RS** — localização institucional dos associados por município.

O resultado é deliberadamente denominado **subconjunto identificável de São Borja**, e não “beneficiamento total de São Borja”.

## Empresas identificadas

A página institucional do Sindarroz-RS lista em São Borja:
- Cerealista Albaruska Ltda.;
- Cerealista Streck Ltda.;
- Ciagro Alimentos Ltda.;
- Pirahy Alimentos Ltda.

As quatro aparecem nos rankings oficiais do IRGA de 2023 e 2024.

Para a Pirahy, o site oficial da empresa também confirma sede e plantas em São Borja.

## Dados observados — IRGA

### 2023

- Pirahy: 216.780 t; 3ª posição; 3,79%; 2 unidades ativas.
- Albaruska: 45.837 t; 30ª posição; 0,80%; 1 unidade.
- Ciagro: 20.814 t; 64ª posição; 0,36%; 1 unidade.
- Cerealista Streck: 20.188 t; 67ª posição; 0,35%; 1 unidade.
- Total das indústrias do RS: 5.722.235 t; 157 unidades.

### 2024 — ranking corrigido

- Pirahy: 237.880 t; 3ª posição; 4,55%; 2 unidades ativas.
- Albaruska: 42.580 t; 35ª posição; 0,81%; 1 unidade.
- Ciagro: 27.017 t; 47ª posição; 0,52%; 1 unidade.
- Cerealista Streck: 17.556 t; 66ª posição; 0,34%; 1 unidade.
- Total das indústrias do RS: 5.233.168 t; 157 unidades.

## Cálculos SBMI

### Subconjunto identificável — volume

2023:

`216.780 + 45.837 + 20.814 + 20.188 = 303.619 t`

2024:

`237.880 + 42.580 + 27.017 + 17.556 = 325.033 t`

Variação:

`((325.033 / 303.619) - 1) × 100 = +7,05%`

### Subconjunto identificável — participação estadual

Soma das participações publicadas pelo IRGA:

2023:

`3,79 + 0,80 + 0,36 + 0,35 = 5,30%`

2024:

`4,55 + 0,81 + 0,52 + 0,34 = 6,22%`

Variação:

`6,22 - 5,30 = +0,92 ponto percentual`

### Total estadual

`((5.233.168 / 5.722.235) - 1) × 100 = -8,55%`

## Interpretação

No subconjunto de quatro empresas cuja localização em São Borja pôde ser cruzada institucionalmente, o beneficiamento aumentou **7,05%** de 2023 para 2024, enquanto o volume total das indústrias gaúchas caiu **8,55%**.

A participação mínima identificável desse subconjunto passou de **5,30% para 6,22%** do beneficiamento estadual, avanço de **0,92 p.p.**

Isso é evidência de fortalecimento relativo do **subconjunto identificado**, não uma medida do market share total de São Borja.

## Destaques empresariais

Pirahy:
- manteve a 3ª posição estadual;
- volume: 216.780 t → 237.880 t;
- variação calculada: **+9,73%**;
- participação: 3,79% → 4,55%, ou **+0,76 p.p.**

Ciagro:
- 64ª → 47ª posição;
- 20.814 t → 27.017 t;
- variação calculada: **+29,80%**;
- participação: 0,36% → 0,52%, ou **+0,16 p.p.**

Albaruska:
- 30ª → 35ª;
- 45.837 t → 42.580 t;
- **-7,11%**.

Cerealista Streck:
- 67ª → 66ª;
- 20.188 t → 17.556 t;
- **-13,04%**.

## Limitações

1. O ranking IRGA é por **empresa**, não por município.
2. A territorialização usa a localização institucional do Sindarroz-RS e, para Pirahy, também o site oficial da empresa.
3. A lista do Sindarroz não é um censo de todas as beneficiadoras locais.
4. A v028 do SBMI identifica 20 estabelecimentos ativos no CNAE 10.61-9/01; portanto, as quatro empresas desta auditoria formam apenas um subconjunto nominal verificável.
5. Não atribuir às demais unidades cadastrais tonelagem não publicada.
6. Participação no beneficiamento físico não é market share financeiro, valor adicionado ou participação nas vendas.

## Uso no piloto do Radar

O indicador resolve parte da pergunta de **posição produtiva estadual**:

- São Borja possui cadeia primária relevante;
- possui elo industrial local material;
- e um subconjunto nominalmente identificável respondeu por pelo menos 6,22% do beneficiamento estadual em 2024.

O Radar continua necessário para:
- demanda financeira por NCM;
- origem do abastecimento;
- entradas OUF;
- importações;
- mercados consumidores;
- concorrentes;
- market share financeiro.

## Fontes

IRGA — Ranking Beneficiamento 2023:
https://irga.rs.gov.br/upload/arquivos/202407/12130753-ranking-total-2023.pdf

IRGA — Ranking Beneficiamento 2024 corrigido:
https://irga.rs.gov.br/upload/arquivos/202507/21123010-ranking-beneficiamento-2024.pdf

Sindarroz-RS — associados por município:
https://sindarroz-rs.ind.br/site/associados.php?cidade=0&pagina=6

Pirahy / Prato Fino — história:
https://www.pratofino.com.br/a-pirahy/
