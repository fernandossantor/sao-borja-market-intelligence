# DFe — auditoria da interseção território × setor — v001

**Data:** 2026-09-26  
**Fonte:** Receita Estadual do Rio Grande do Sul — Receita Dados / Power BI público  
**Objetivo:** verificar se os dados públicos permitem obter diretamente `São Borja × setor/CNAE × valor de DFe` sem rateios por CNPJ, lojas, empregos ou outros proxies estruturais.

## 1. Resultado da auditoria

**Conclusão:** a interseção pública direta `município × CNAE` **não foi encontrada** nos datasets e modelos públicos auditados.

A Receita expõe, em modelos separados:

### Modelo territorial municipal

Entidade observada no Power BI:

`v_PBI_Dfe_Totais_Municipio`

Campo territorial observado:

`nome_municipio`.

Os relatórios públicos “Quantidade - Município” e “Valor - Município” utilizam esse modelo.

Na auditoria do esquema:
- ocorrência de município: alta;
- ocorrência de CNAE: zero.

### Modelo setorial regional

Entidade observada no Power BI:

`v_PBI_Dfe_Totais_Corede_Setor`.

Os relatórios “Quantidade - Setor” e “Valor - Setor” utilizam esse modelo.

Campos setoriais observados incluem CNAE por divisão, além de COREDE, modelo fiscal, ano, valor e quantidade.

Na auditoria do esquema:
- ocorrência de CNAE/setor: presente;
- ocorrência de município: zero.

Portanto, os relatórios não representam duas visualizações de um mesmo cubo público com as duas dimensões simultâneas; são modelos distintos.

## 2. Implicação metodológica

Não é defensável derivar `São Borja × CNAE` multiplicando:

- total municipal × participação setorial do COREDE;
- total municipal × número de CNPJs;
- total municipal × número de lojas;
- total municipal × empregos;
- total municipal × remuneração;
- qualquer combinação dessas variáveis.

Esses procedimentos criariam uma estimativa por alocação, e não faturamento observado.

A regra do projeto permanece:

**CNPJ, lojas, vínculos, folha e presença cadastral não são proxies de faturamento ou market share.**

## 3. Envelope municipal observado

Para São Borja, NFC-e:

| Ano | Valor dos documentos |
|---|---:|
| 2023 | R$ 843.874.412,06 |
| 2024 | R$ 1.043.404.535,44 |
| 2025 | R$ 1.189.327.276,47 |
| 2026* | R$ 810.740.309,61 |

`* 01/01 a 14/09/2026`.

Esses valores permanecem como **envelope fiscal municipal amplo**.

## 4. Benchmark setorial observado — COREDE Fronteira Oeste

O modelo público `v_PBI_Dfe_Totais_Corede_Setor` permitiu consultar NFC-e por divisão CNAE.

### Total NFC-e — Fronteira Oeste

| Ano | Valor | Quantidade |
|---|---:|---:|
| 2023 | R$ 8.872.450.065,47 | 90.808.849 |
| 2024 | R$ 10.078.977.261,66 | 99.650.104 |
| 2025 | R$ 11.129.327.451,44 | 105.348.009 |

### Divisão 47 — Comércio varejista

| Ano | Valor | Participação no valor NFC-e do COREDE |
|---|---:|---:|
| 2023 | R$ 8.129.374.041,41 | 91,624906% |
| 2024 | R$ 9.219.172.341,39 | 91,469324% |
| 2025 | R$ 10.123.462.565,95 | 90,962034% |

### Divisão 56 — Alimentação

| Ano | Valor | Participação no valor NFC-e do COREDE |
|---|---:|---:|
| 2023 | R$ 237.676.433,30 | 2,678814% |
| 2024 | R$ 283.321.723,88 | 2,811017% |
| 2025 | R$ 316.172.104,88 | 2,840891% |

Esses valores são **dados fiscais observados regionais**, não estimativas de São Borja.

## 5. Indicador territorial amplo calculado

Em 2025:

`NFC-e São Borja / NFC-e Fronteira Oeste = 1.189.327.276,47 / 11.129.327.451,44 = 10,686425%`.

Assim, São Borja respondeu por aproximadamente **10,69% do valor total de NFC-e observado no COREDE Fronteira Oeste em 2025**.

Esse indicador é válido apenas para o **envelope total de NFC-e**, pois numerador e denominador têm o mesmo conceito fiscal.

Ele **não pode** ser aplicado às divisões 47 ou 56 para inferir o faturamento setorial de São Borja.

## 6. Radar do Mercado — utilidade e limite

A auditoria do “Radar do Mercado” da Receita Estadual encontrou estrutura rica por NCM e grupos de afinidade, inclusive:

- `d_ncms`;
- `grupo_afinidade_final`;
- `ncm8`, `ncm4`;
- entidades e medidas de market share estadual, entradas, fornecedores, concorrentes e UF de origem/destino.

Entretanto, no modelo auditado:
- município: não observado;
- COREDE: não observado;
- CNAE municipal: não observado.

Portanto, o Radar é útil para:
- taxonomia NCM;
- agrupamentos de produto;
- benchmarks estaduais;
- análise de dependência de compras externas ao RS.

Ele não resolve o denominador de market share local de São Borja.

## 7. Rastreabilidade

### Envelope municipal

Workflow:
`dfe-sao-borja-market-dimension-v1`.

Run:
`36258514596`.

Drive:
`SBMI_DFe_Sao_Borja_2023_2026_v001.zip`  
ID: `1-lhcCTLyRYsySFrByBAHD4o7tuGahyS4`.

### COREDE × setor

Workflow:
`dfe-corede-sector-series-v1`.

Run:
`36264971112`.

Artifact:
`10913254771`.

Digest:
`sha256:323eb2942fcf7d71c9ac4c488d76236cf0edccbbf54be72db2710105c2e3f00f`.

Drive:
`SBMI_DFe_COREDE_setor_2023_2025_v001.zip`  
ID: `1TzWMgprG0j1MYoUBDr3F6hUzHgwO-Zh7`.

### Auditoria dos modelos públicos

Workflow:
`dfe-powerbi-schema-discovery-v1`.

Run:
`36265009880`.

Artifact:
`10913855756`.

Digest:
`sha256:1db296128723444d59faf63fd48e6acf5cdcf4d166553f6c8080c4cf2c1bd37f`.

Drive:
`SBMI_DFe_schema_publico_territorio_setor_v001.zip`  
ID: `1KfdT4cyUj_blK86Hu4XsgCfBPdn0_U_J`.

## 8. Decisão

A frente pública DFe fica classificada assim:

- **município × valor total:** observado;
- **COREDE × setor/CNAE × valor:** observado;
- **estado × CNAE classe × valor:** observado em arquivos próprios;
- **município × setor/CNAE × valor:** não localizado publicamente;
- **município × NCM × valor:** não localizado publicamente.

A obtenção dos dois últimos recortes exige outra fonte, solicitação institucional agregada ou disponibilização específica pela Receita Estadual.
