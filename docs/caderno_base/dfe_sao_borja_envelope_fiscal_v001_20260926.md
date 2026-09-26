# Envelope fiscal de Documentos Fiscais Eletrônicos — São Borja — v001

**Data da extração:** 2026-09-26  
**Geografia:** São Borja/RS — código IBGE 4318002  
**Fonte primária:** Receita Estadual do Rio Grande do Sul — Receita Dados — Documentos Eletrônicos — arquivos `DFe_Totais_Municipio_YYYY.zip`  
**Período observado:** 2023-01-01 a 2026-09-14  
**Natureza:** dados fiscais observados na fonte + agregações calculadas pelo SBMI.

## 1. Objetivo

Construir um envelope monetário fiscal territorial que possa servir de ponte entre a dimensão de demanda residente e, futuramente, faturamento observado por setor.

Este envelope **não é tamanho de mercado** e **não é market share**.

## 2. Fonte e esquema observado

Arquivos oficiais utilizados:

- `DFe_Totais_Municipio_2023.zip`;
- `DFe_Totais_Municipio_2024.zip`;
- `DFe_Totais_Municipio_2025.zip`;
- `DFe_Totais_Municipio_2026.zip`.

Em cada CSV, o esquema efetivamente observado foi:

`modelo_dfe; dt_emissao; cod_municipio; nome_municipio; qtde_dfe; vlr_total_dfe`.

Os arquivos foram lidos em `cp1252`, delimitador `;`.

A coluna `dados_atualizados_ate`, descrita na nota técnica pública, **não estava presente nos quatro arquivos baixados nesta execução**. A cobertura temporal do arquivo 2026 alcança 14/09/2026.

## 3. Resultados anuais

Os valores abaixo são **somas calculadas pelo SBMI** das linhas diárias oficiais filtradas para São Borja.

| Ano | Modelo | Quantidade de documentos | Valor dos documentos (R$) | Dias observados |
|---|---|---:|---:|---:|
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

Entre anos completos:

- NFC-e nominal: 2024/2023 = **+23,64%**;
- quantidade de NFC-e: 2024/2023 = **+17,39%**;
- NFC-e nominal: 2025/2024 = **+13,99%**;
- quantidade de NFC-e: 2025/2024 = **+8,36%**.

Essas variações são **calculadas** e permanecem nominais. Não demonstram crescimento real de consumo porque ainda não foram deflacionadas nem controladas por composição setorial, formalização, mudanças cadastrais ou alterações de emissão.

## 7. Consequência para a dimensão de mercado

O avanço empírico é relevante porque agora existe um **denominador territorial fiscal amplo observado** para São Borja.

Porém, ainda falta a interseção necessária para os cadernos:

`município × setor/CNAE`

e, idealmente para varejos de mix amplo:

`município × produto/NCM`.

Os dados públicos identificados até aqui divulgam município e CNAE em arquivos distintos. Nenhum rateio por quantidade de CNPJs, estabelecimentos, lojas, vínculos ou remuneração será usado para forçar essa interseção.

## 8. Rastreabilidade

Workflow:
`.github/workflows/dfe-sao-borja-market-dimension-v1.yml`

Execução bem-sucedida:
- push run: `36258514596`;
- job: `108449749903`;
- commit do extrator: `b6f42c8d9622c445ce888a760eab238610402d6c`.

Artifact GitHub:
- ID: `10911616371`;
- digest: `sha256:e69c6550e9a9617a2161aa1816d2cd7b3fc9aed975ff8489b5cf282fd628c146`.

SHA-256 dos pacotes oficiais baixados nesta execução:

- 2023: `dd9d3c006254a2676c4057b6be0f4f0c8eb507b1eefa21848db915903a63ff83`;
- 2024: `54ff8c70670a4cad739ead7e86af0d490514552a7498a6b25e95ad95c6f08458`;
- 2025: `3a87f1d51e76a1fb1a6019047dd5e1f67378b9865ac4b9f5e0cbbcec48e70944`;
- 2026: `056fb082f3719ca60d7a1ba21ccaa9c153a390ff18f11d39908543b4afabbfa4`.

Google Drive — pacote preservado:
- `SBMI_DFe_Sao_Borja_2023_2026_v001.zip`;
- ID: `1-lhcCTLyRYsySFrByBAHD4o7tuGahyS4`.

## 9. Próxima etapa

1. investigar o dataset/painel para cruzamento `município × CNAE`;
2. procurar granularidade `município × NCM`;
3. se a interseção pública não existir, registrar formalmente a limitação e avaliar solicitação agregada à Receita Estadual;
4. apenas depois vincular os valores fiscais aos cinco mercados.
