# Demanda residente setorial — POF/RS + IPCA específico — v001

**Data:** 2026-09-26  
**Geografia do resultado:** São Borja/RS  
**População utilizada:** 61.311 pessoas — estimativa IBGE 2025  
**Tamanho médio familiar:** 2,72 pessoas — POF 2017-2018/RS  
**Período monetário final:** preços aproximados de junho de 2026  
**Natureza:** ESTIMATIVAS MODELADAS de demanda residente; não são faturamento observado, mercado capturado ou market share.

## 1. Objetivo

Atualizar a frente de demanda residente dos cinco cadernos com fatores de preços específicos por módulo, substituindo a aplicação indevida de um único fator alimentar a categorias heterogêneas.

A lógica comum é:

`DR_mensal = população × (despesa_familiar_POF / tamanho_médio_familiar) × fator_IPCA_específico`

e:

`DR_anual = DR_mensal × 12`.

## 2. Convenção temporal de atualização

A POF tem período de referência 2017-2018 e não um único mês-base.

Para manter comparabilidade com o modelo canônico de Bens Essenciais, adota-se como convenção principal a acumulação do IPCA específico de **jan/2018 a jun/2026**.

Controle de consistência:

- fator canônico já preservado para Alimentação e bebidas: `1,781742384675`;
- fator recalculado diretamente no SIDRA para jan/2018–jun/2026: `1,7815651422824692`;
- diferença relativa: **-0,00995%**.

A diferença é desprezível para a escala do modelo e confirma que a convenção jan/2018 é compatível com o fator já adotado.

Como sensibilidade, também foram calculados fatores iniciando em jul/2018. A diferença sobre os resultados principais varia aproximadamente entre 0% e -1,9% nos módulos analisados. Portanto, o mês-base é uma fonte de incerteza, mas não altera a ordem de grandeza.

## 3. Fatores de preços específicos

Fonte: IBGE/SIDRA — IPCA, variável 63, classificação 315; tabelas 1419 e 7060.

| Módulo SBMI | Classificação IPCA | Código | Fator jan/2018→jun/2026 |
|---|---|---:|---:|
| Alimentação Fora do Lar | 1201.Alimentação fora do domicílio | 7433 | 1,590068184251 |
| Higiene e Cuidados Pessoais | 6301.Higiene pessoal | 7698 | 1,521859557648 |
| Remédios | 6101.Produtos farmacêuticos | 7662 | 1,497233067692 |
| Vestuário | 4.Vestuário | 7558 | 1,473133343800 |
| Mobiliários e artigos do lar | 31.Móveis e utensílios | 7487 | 1,424601780273 |
| Eletrodomésticos | 3201.Eletrodomésticos e equipamentos | 7522 | 1,356992683697 |
| Serviços pessoais | 7101.Serviços pessoais | 7714 | 1,440282974794 |

**Observação metodológica:** equivalência nominal não significa identidade perfeita entre a taxonomia POF e a taxonomia IPCA. Os fatores são proxies de atualização de preços compatíveis, não índices municipais de São Borja.

## 4. Resultados modelados por módulo

### 4.1 Alimentação Fora do Lar

POF/RS: **R$ 249,69/família/mês**.

Baseline territorial a preços POF:

`61.311 × (249,69 / 2,72) = R$ 5.628.214,56/mês`.

Atualização específica:

`R$ 5.628.214,56 × 1,590068184251 = R$ 8.949.244,90/mês`.

Resultado anual:

**R$ 107.390.938,78/ano**.

Natureza: **ESTIMATIVA MODELADA de demanda residente no conceito POF “alimentação fora do domicílio”**.

O valor anterior de aproximadamente R$ 120,34 milhões/ano, calculado com o fator amplo de Alimentação e bebidas, fica substituído para esta finalidade pelo valor específico. A diferença é de **-10,76%**, decorrente da troca de índice, não de mudança observada do mercado.

### 4.2 Saúde/Higiene/Cuidados Pessoais — núcleo POF

#### Higiene e Cuidados Pessoais

POF/RS: **R$ 139,87/família/mês**.

Demanda modelada:

- mensal: **R$ 4.798.092,84**;
- anual: **R$ 57.577.114,03**.

#### Remédios

POF/RS: **R$ 171,83/família/mês**.

Demanda modelada:

- mensal: **R$ 5.799.063,92**;
- anual: **R$ 69.588.767,08**.

#### Núcleo monetário combinado

`Higiene + Remédios`:

- mensal: **R$ 10.597.156,76**;
- anual: **R$ 127.165.881,11**.

**Limite:** esse valor é uma **cesta-núcleo modelada**, não o tamanho total do mercado Saúde/Higiene. O escopo POM inclui categorias que podem não estar integralmente cobertas por esses dois módulos, como suplementos e itens híbridos; serviços clínicos permanecem fora desse mercado de varejo.

### 4.3 Bens Não Essenciais — módulos POF diretamente defensáveis

#### Mobiliários e artigos do lar

- POF/RS: R$ 85,18/família/mês;
- mensal atualizado: **R$ 2.735.272,59**;
- anual atualizado: **R$ 32.823.271,13**.

#### Eletrodomésticos

- POF/RS: R$ 74,66/família/mês;
- mensal atualizado: **R$ 2.283.678,63**;
- anual atualizado: **R$ 27.404.143,52**.

#### Vestuário

- POF/RS: R$ 183,53/família/mês;
- mensal atualizado: **R$ 6.094.226,90**;
- anual atualizado: **R$ 73.130.722,82**.

#### Soma dos três módulos

- mensal: **R$ 11.113.178,12**;
- anual: **R$ 133.358.137,47**.

Natureza: **SOMA CALCULADA DE MÓDULOS**, não market size integral de Bens Não Essenciais.

O caderno inclui outras frentes — por exemplo, categorias pet/vet/agro, decoração, utilidades e outros bens — cuja correspondência monetária ainda precisa ser definida. A soma atual deve ser tratada como **piso modular conhecido**, sem extrapolação para o mercado total.

### 4.4 Serviços — submercado de serviços pessoais

POF/RS: **R$ 47,28/família/mês**.

Demanda modelada:

- mensal: **R$ 1.534.951,97**;
- anual: **R$ 18.419.423,64**.

Esse valor representa somente o submercado POF de **Serviços pessoais**. Não representa o conjunto de Serviços do caderno, que inclui atividades heterogêneas como oficinas, assistência técnica, hotelaria, lavanderias e outras.

## 5. Quadro consolidado

| Mercado / módulo | Mensal — preços jun/2026 | Anual — preços jun/2026 | Status |
|---|---:|---:|---|
| Bens Essenciais — alimentação no domicílio | R$ 19.558.852,34 | R$ 234.706.228,14 | benchmark canônico existente |
| Alimentação Fora do Lar | R$ 8.949.244,90 | R$ 107.390.938,78 | demanda residente modelada |
| Saúde/Higiene — Higiene | R$ 4.798.092,84 | R$ 57.577.114,03 | módulo |
| Saúde/Higiene — Remédios | R$ 5.799.063,92 | R$ 69.588.767,08 | módulo |
| Saúde/Higiene — núcleo Higiene + Remédios | R$ 10.597.156,76 | R$ 127.165.881,11 | cesta-núcleo; não mercado total |
| Bens Não Essenciais — Móveis/artigos do lar | R$ 2.735.272,59 | R$ 32.823.271,13 | módulo |
| Bens Não Essenciais — Eletrodomésticos | R$ 2.283.678,63 | R$ 27.404.143,52 | módulo |
| Bens Não Essenciais — Vestuário | R$ 6.094.226,90 | R$ 73.130.722,82 | módulo |
| Bens Não Essenciais — soma dos 3 módulos | R$ 11.113.178,12 | R$ 133.358.137,47 | piso modular; não mercado total |
| Serviços — Serviços pessoais | R$ 1.534.951,97 | R$ 18.419.423,64 | submercado somente |

## 6. O que estes números permitem concluir

**Permitem:**
- estimar ordens de grandeza da carteira de consumo dos residentes;
- comparar módulos sob uma metodologia comum;
- estabelecer denominadores de demanda residente para futuras análises de retenção/vazamento, desde que seja obtida a origem/destino do gasto;
- orientar desenho de pesquisa primária.

**Não permitem:**
- afirmar faturamento das empresas de São Borja;
- afirmar mercado capturado no município;
- repartir valores entre empresas;
- calcular market share;
- inferir demanda não residente;
- inferir retenção territorial.

## 7. Rastreabilidade

Workflow:
`.github/workflows/ipca-market-dimension-factor-discovery-v1.yml`

Run de validação específica:
`36264970897`.

Artifact:
`10914205219`.

Digest:
`sha256:0ea63afd06d8061cfad890938285d8ce45cfefb14dae47bb2c14f7e3d416ab8e`.

Drive:
`SBMI_IPCA_fatores_dimensao_mercado_v001.zip`  
ID: `1hYTpuFiL93RzfQJ6M9QFWe1-cHw36msB`.

POF crosswalk:
`SBMI_POF_RS_market_crosswalk_v001.zip`  
ID: `1OpNbR9_IAaXU-pdjsiLyvG8hOuXG1Asi`.

## 8. Próximo passo

A demanda residente agora possui valores modelados defensáveis em vários módulos. O próximo gargalo passa a ser a **oferta monetária territorial**, especialmente a interseção `São Borja × setor/produto × valor fiscal`.
