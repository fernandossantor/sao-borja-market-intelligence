# Envelope fiscal de Documentos Fiscais Eletrônicos — São Borja — v001

**Data da extração:** 2026-09-26  
**Geografia:** São Borja/RS — código IBGE 4318002  
**Fonte primária:** Receita Estadual do Rio Grande do Sul — Receita Dados — Documentos Eletrônicos — arquivos `DFe_Totais_Municipio_YYYY.zip`  
**Período observado:** 2018-01-01 a 2026-09-14  
**Natureza:** dados fiscais observados na fonte + agregações calculadas pelo SBMI.

## 1. Objetivo

Construir um envelope monetário fiscal territorial que possa servir de ponte entre a dimensão de demanda residente e, futuramente, faturamento observado por setor.

Este envelope **não é tamanho de mercado** e **não é market share**.

## 2. Fonte e esquema observado

Arquivos oficiais utilizados:

- `DFe_Totais_Municipio_2018.zip`;
- `DFe_Totais_Municipio_2019.zip`;
- `DFe_Totais_Municipio_2020.zip`;
- `DFe_Totais_Municipio_2021.zip`;
- `DFe_Totais_Municipio_2022.zip`;
- `DFe_Totais_Municipio_2023.zip`;
- `DFe_Totais_Municipio_2024.zip`;
- `DFe_Totais_Municipio_2025.zip`;
- `DFe_Totais_Municipio_2026.zip`.

Em cada CSV, o esquema efetivamente observado foi:

`modelo_dfe; dt_emissao; cod_municipio; nome_municipio; qtde_dfe; vlr_total_dfe`.

Os arquivos foram lidos em `cp1252`, delimitador `;`.

A coluna `dados_atualizados_ate`, descrita na nota técnica pública, **não estava presente nos nove arquivos baixados nesta execução consolidada**. Os anos 2018–2025 cobrem os respectivos anos civis completos; o arquivo 2026 alcança 14/09/2026.

## 3. Resultados anuais

Os valores abaixo são **somas calculadas pelo SBMI** das linhas diárias oficiais filtradas para São Borja.

| Ano | Modelo | Quantidade de documentos | Valor dos documentos (R$) | Dias observados |
|---|---|---:|---:|---:|
| 2018 | CT-e | 25.342 | 50.499.004,61 | 365 |
| 2018 | NF-e | 356.500 | 1.751.873.599,30 | 365 |
| 2018 | NFC-e | 7.807.667 | 546.518.503,49 | 365 |
| 2019 | CT-e | 24.840 | 60.710.114,25 | 365 |
| 2019 | NF-e | 382.324 | 1.868.683.046,86 | 365 |
| 2019 | NFC-e | 8.612.694 | 605.200.984,20 | 365 |
| 2020 | CT-e | 25.530 | 68.832.729,62 | 366 |
| 2020 | NF-e | 396.018 | 2.594.269.266,36 | 366 |
| 2020 | NFC-e | 8.215.913 | 637.979.051,83 | 366 |
| 2021 | CT-e | 23.591 | 82.123.413,72 | 365 |
| 2021 | NF-e | 559.179 | 3.429.346.173,38 | 365 |
| 2021 | NFC-e | 8.609.335 | 744.589.628,55 | 365 |
| 2022 | CT-e | 25.403 | 103.921.883,75 | 365 |
| 2022 | NF-e | 606.135 | 3.648.280.848,17 | 365 |
| 2022 | NFC-e | 9.091.375 | 830.930.267,67 | 365 |
| 2023 | CT-e | 24.890 | 124.343.891,46 | 365 |
| 2023 | NF-e | 762.230 | 4.229.579.669,78 | 365 |
| 2023 | NFC-e | 9.654.535 | 843.874.412,06 | 365 |
| 2024 | CT-e | 22.462 | 122.993.400,90 | 366 |
| 2024 | NF-e | 869.080 | 5.227.027.900,84 | 366 |
| 2024 | NFC-e | 11.333.846 | 1.043.404.535,44 | 366 |
| 2025 | CT-e | 23.892 | 141.614.901,12 | 365 |
| 2025 | NF-e | 985.805 | 4.540.927.027,22 | 365 |
| 2025 | NFC-e | 12.281.207 | 1.189.327.276,47 | 365 |
| 2026* | CT-e | 19.529 | 125.781.734,76 | 257 |
| 2026* | NF-e | 742.766 | 3.654.696.242,45 | 257 |
| 2026* | NFC-e | 8.720.416 | 810.740.309,61 | 257 |

`* 2026 = 01/01 a 14/09; não comparar como ano fechado.`

## 4. Indicador calculado: valor médio por documento

Fórmula:

`valor médio por documento = soma(vlr_total_dfe) / soma(qtde_dfe)`.

Para NFC-e:

| Ano | Valor médio/documento NFC-e |
|---|---:|
| 2018 | R$ 70,00 |
| 2019 | R$ 70,27 |
| 2020 | R$ 77,65 |
| 2021 | R$ 86,49 |
| 2022 | R$ 91,40 |
| 2023 | R$ 87,41 |
| 2024 | R$ 92,06 |
| 2025 | R$ 96,84 |
| 2026* | R$ 92,97 |

Este indicador **não deve ser denominado ticket médio de consumo** sem auditoria adicional. É apenas o quociente entre valor fiscal agregado e quantidade de documentos do mesmo modelo.

## 5. Leitura metodológica

### NFC-e

A NFC-e é a camada mais próxima de transações formais com consumidor final entre as três modalidades presentes no arquivo municipal.

Mesmo assim, o total municipal de NFC-e:

- agrega todos os setores emissores;
- não identifica a categoria comprada no arquivo municipal;
- não identifica residência do consumidor;
- não mede vendas informais;
- não separa demanda residente de demanda não residente;
- não informa, por si só, o mercado capturado de qualquer um dos cinco cadernos.

Portanto, **R$ 1,189 bilhão de NFC-e em 2025 é envelope fiscal municipal amplo, não market size do varejo nem consumo dos residentes**.

### NF-e

A NF-e possui valor muito superior ao da NFC-e e inclui operações empresariais de natureza distinta do varejo final. A nota técnica da Receita Estadual aplica uma relação específica de CFOPs ao conjunto divulgado.

Por isso, NF-e **não pode ser somada mecanicamente à NFC-e para produzir consumo ou faturamento varejista**.

### CT-e

CT-e é preservado na série por fidelidade ao arquivo municipal, mas não integra a primeira modelagem dos cinco mercados de consumo.

## 6. Comparação temporal restrita

A série histórica foi ampliada para 2018–2025 em anos completos.

Variações nominais anuais da NFC-e calculadas a partir dos totais observados:

| Comparação | Valor NFC-e | Quantidade NFC-e |
|---|---:|---:|
| 2019/2018 | +10,74% | +10,31% |
| 2020/2019 | +5,42% | -4,61% |
| 2021/2020 | +16,71% | +4,79% |
| 2022/2021 | +11,59% | +5,60% |
| 2023/2022 | +1,56% | +6,19% |
| 2024/2023 | +23,64% | +17,39% |
| 2025/2024 | +13,99% | +8,36% |

Essas variações são **calculadas** e permanecem nominais. Não demonstram crescimento real de consumo porque ainda precisam ser deflacionadas e controladas por composição setorial, formalização, mudanças cadastrais e alterações de emissão.

O salto de valor/documento em 2020–2022 e a desaceleração nominal em 2023 são fatos descritivos da série fiscal; sua explicação causal não é inferida nesta etapa.

## 7. Consequência para a dimensão de mercado

O avanço empírico é relevante porque agora existe um **denominador territorial fiscal amplo observado** para São Borja.

Porém, ainda falta a interseção necessária para os cadernos:

`município × setor/CNAE`

e, idealmente para varejos de mix amplo:

`município × produto/NCM`.

Os dados públicos identificados até aqui divulgam município e CNAE em arquivos distintos. Nenhum rateio por quantidade de CNPJs, estabelecimentos, lojas, vínculos ou remuneração será usado para forçar essa interseção.

## 8. Rastreabilidade

### Extração original 2023–2026

Workflow:
`.github/workflows/dfe-sao-borja-market-dimension-v1.yml`

Execução:
- push run: `36258514596`;
- job: `108449749903`;
- commit do extrator: `b6f42c8d9622c445ce888a760eab238610402d6c`;
- artifact: `10911616371`;
- digest: `sha256:e69c6550e9a9617a2161aa1816d2cd7b3fc9aed975ff8489b5cf282fd628c146`.

Drive:
- `SBMI_DFe_Sao_Borja_2023_2026_v001.zip`;
- ID: `1-lhcCTLyRYsySFrByBAHD4o7tuGahyS4`.

### Série pública ampliada 2018–2026

Workflow:
`.github/workflows/download-public-series-bulk-v1.yml`

Execução:
- run: `36275562165`;
- commit: `2d3c7decd30141cceb81064513dc51b71bdc46a1`;
- artifact DFe município: `10916617398`;
- digest: `sha256:450a1131cd6ceb7d1dd8dd30dbd722eba042e4e25e1b9b5b30129ecc32b873aa`.

Drive:
- `SBMI_DFe_Municipio_2018_2026_v001.zip`;
- ID: `1DuirpWKYP4Pwu8qxyEU_B6le0MXnfD-j`.

A série ampliada foi obtida diretamente dos mesmos padrões oficiais de URL, preservando os arquivos anuais originais sem transformação.

## 9. Próxima etapa

1. investigar o dataset/painel para cruzamento `município × CNAE`;
2. procurar granularidade `município × NCM`;
3. se a interseção pública não existir, registrar formalmente a limitação e avaliar solicitação agregada à Receita Estadual;
4. apenas depois vincular os valores fiscais aos cinco mercados.
