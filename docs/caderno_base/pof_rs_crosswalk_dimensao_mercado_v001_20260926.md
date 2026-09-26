# POF RS — crosswalk para dimensão de mercado dos cinco cadernos — v001

**Data:** 2026-09-26  
**Fonte primária:** IBGE — Pesquisa de Orçamentos Familiares 2017-2018 — Primeiros resultados — tabelas por Unidade da Federação  
**Geografia da fonte:** Rio Grande do Sul  
**Unidade:** R$/família/mês, preços do período 2017-2018  
**Natureza:** dados observados da POF + cálculos/modelagens explicitamente identificados.

## 1. Objetivo

Criar um crosswalk auditável entre categorias monetárias da POF/RS e os cinco mercados do SBMI, sem transformar automaticamente categorias da POF em mercados totais municipais.

## 2. Controles da fonte

Na tabela `1.3.23.1`, a POF informa:

- número de famílias no RS: **4.155.820**;
- tamanho médio da família: **2,72 pessoas**.

Na tabela `1.3.23.3`, os mesmos valores aparecem novamente para a estrutura de despesa alimentar.

O valor de **2,72** é, portanto, observado na POF/RS e continua sendo o denominador familiar utilizado na territorialização per capita.

## 3. Crosswalk inicial

| Setor SBMI | Módulo | Tabela/linha POF | R$/família/mês | Status |
|---|---|---|---:|---|
| Bens Essenciais | Alimentação no domicílio | 1.3.23.3 / linha 9 | 487,00 | incluir; já canônico |
| Alimentação Fora do Lar | Alimentação fora do domicílio | 1.3.23.3 / linha 93 | 249,69 | incluir |
| Saúde/Higiene/Cuidados Pessoais | Higiene e Cuidados Pessoais | 1.3.23.1 / linha 46 | 139,87 | incluir |
| Saúde/Higiene/Cuidados Pessoais | Remédios | 1.3.23.1 / linha 52 | 171,83 | incluir como módulo separado |
| Bens Não Essenciais | Mobiliários e artigos do lar | 1.3.23.1 / linha 28 | 85,18 | incluir como módulo |
| Bens Não Essenciais | Eletrodomésticos | 1.3.23.1 / linha 29 | 74,66 | incluir como módulo |
| Bens Não Essenciais | Vestuário | 1.3.23.1 / linha 31 | 183,53 | incluir como módulo |
| Serviços | Serviços pessoais | 1.3.23.1 / linha 86 | 47,28 | submercado apenas |

## 4. Alimentação Fora do Lar

A POF/RS observa:

- alimentação total: **R$ 736,69/família/mês**;
- alimentação no domicílio: **R$ 487,00**;
- alimentação fora do domicílio: **R$ 249,69**.

Controle aritmético:

`487,00 + 249,69 = 736,69`.

A tabela `1.3.23.4` registra que alimentação fora do domicílio corresponde a **33,9% da despesa alimentar** no RS.

Subitens observados da despesa média familiar mensal fora do domicílio incluem:

- almoço e jantar: **R$ 185,89**;
- café/leite/café com leite/chocolate: **R$ 4,33**;
- sanduíches e salgados: **R$ 18,06**;
- refrigerantes e outras bebidas não alcoólicas: **R$ 6,82**;
- lanches: **R$ 14,73**.

Esses valores são estaduais, 2017-2018, e não descrevem frequência ou ticket de São Borja.

## 5. Saúde/Higiene/Cuidados Pessoais

A categoria POF `Higiene e Cuidados Pessoais` registra **R$ 139,87/família/mês** e inclui, entre outros:

- perfume: R$ 31,12;
- produtos para cabelo: R$ 20,44;
- sabonete: R$ 9,82;
- instrumentos e produtos de uso pessoal: R$ 78,48.

Separadamente, dentro de `Assistência à saúde`, a POF registra:

- remédios: **R$ 171,83/família/mês**;
- plano/seguro saúde: R$ 97,28;
- consulta e tratamento dentário: R$ 16,50;
- consulta médica: R$ 17,20;
- tratamento médico e ambulatorial: R$ 5,22.

**Decisão metodológica:** o caderno de Saúde/Higiene é predominantemente orientado ao varejo de farmácias, higiene, beleza e cuidados pessoais. Portanto, não se promove a categoria inteira `Assistência à saúde` para o market size do caderno. `Remédios` e `Higiene e Cuidados Pessoais` formam módulos monetários distintos.

A soma:

`139,87 + 171,83 = R$ 311,70/família/mês`

é apenas uma **cesta-núcleo candidata**, não o mercado total do caderno: suplementos e outras categorias podem não estar integralmente representados, enquanto serviços de saúde são deliberadamente excluídos.

## 6. Bens Não Essenciais

Três módulos diretamente compatíveis com o escopo POM:

- Vestuário: **R$ 183,53/família/mês**;
- Mobiliários e artigos do lar: **R$ 85,18**;
- Eletrodomésticos: **R$ 74,66**.

A soma dos três:

`183,53 + 85,18 + 74,66 = R$ 343,37/família/mês`.

Natureza: **cesta modular calculada**.

Ela não é market size total de bens não essenciais. O POM inclui outras frentes, como pet/vet/agro, decoração, utilidades e categorias cuja correspondência POF ainda precisa ser definida. Também é necessário evitar dupla contagem de subitens já contidos em categorias superiores.

## 7. Serviços

A POF registra **Serviços pessoais = R$ 47,28/família/mês**, com:

- cabeleireiro: R$ 29,52;
- manicuro e pedicuro: R$ 7,65;
- consertos de artigos pessoais: R$ 1,99;
- outras: R$ 8,12.

Essa categoria pode apoiar um **submercado de serviços pessoais**, mas não representa o universo do caderno de Serviços, que contém oficinas, clínicas, hotelaria, lavanderias, assistência técnica e outras atividades.

Portanto, Serviços permanece sem market size agregado pela POF.

## 8. Territorialização intermediária — preços POF 2017-2018

Para produzir uma etapa intermediária comparável, usa-se:

- população de São Borja estimada 2025: **61.311 pessoas**;
- tamanho médio da família POF/RS: **2,72 pessoas**.

Fórmula:

`baseline mensal = 61.311 × (despesa familiar mensal POF / 2,72)`.

Estes valores **não estão atualizados a preços de 2026** e misturam uma população de referência 2025 com padrões de gasto POF 2017-2018. São somente baselines de escala para a próxima etapa de atualização monetária.

| Módulo | Baseline mensal a preços POF | Baseline anual a preços POF |
|---|---:|---:|
| Alimentação no domicílio | R$ 10.977.373,90 | R$ 131.728.486,76 |
| Alimentação fora do domicílio | R$ 5.628.214,56 | R$ 67.538.574,66 |
| Higiene e Cuidados Pessoais | R$ 3.152.782,93 | R$ 37.833.395,16 |
| Remédios | R$ 3.873.187,18 | R$ 46.478.246,16 |
| Mobiliários e artigos do lar | R$ 1.920.026,10 | R$ 23.040.313,15 |
| Eletrodomésticos | R$ 1.682.896,79 | R$ 20.194.761,44 |
| Vestuário | R$ 4.136.914,64 | R$ 49.642.975,72 |
| Serviços pessoais | R$ 1.065.729,44 | R$ 12.788.753,29 |

## 9. Atualização monetária

A atualização monetária foi aprofundada com fatores IPCA específicos por módulo, combinando as tabelas SIDRA 1419 e 7060 e acumulando as variações mensais de janeiro/2018 a junho/2026.

O fator canônico de Bens Essenciais permanece:

`Alimentação e bebidas = 1,781742384675`.

O novo pipeline reproduziu esse fator por composição das variações mensais publicadas em **1,781565142282**, diferença relativa de apenas **-0,00995%**. O pequeno resíduo é compatível com a acumulação de taxas mensais publicadas com arredondamento; por governança, o fator canônico anterior é preservado.

Para **Alimentação Fora do Lar**, existe índice mais aderente:

- IPCA `1201.Alimentação fora do domicílio`;
- código c315 = **7433**;
- fator jan/2018–jun/2026 = **1,590068184251**.

Assim, a estimativa corrente substitui a sensibilidade provisória baseada no grupo alimentar geral:

`61.311 × (249,69 / 2,72) × 1,590068184251 = R$ 8.949.244,90/mês`

`R$ 8.949.244,90 × 12 = R$ 107.390.938,78/ano`.

**Natureza: ESTIMATIVA MODELADA DE DEMANDA RESIDENTE.**

O valor provisório anterior de **R$ 120.336.341,08/ano**, obtido com o fator geral `Alimentação e bebidas`, fica **substituído**. A diferença é metodológica e não representa retração do mercado.

Os demais fatores específicos e estimativas por módulo estão documentados em:
`docs/caderno_base/demanda_residente_modulos_setoriais_v001_20260926.md`.

## 10. Rastreabilidade

Workflows:

- inspeção: `.github/workflows/pof-rs-market-dimension-v1.yml`;
- crosswalk: `.github/workflows/pof-rs-market-crosswalk-v1.yml`.

Execuções bem-sucedidas:

- inspeção push: `36258305260`;
- inspeção PR: `36258308907`;
- crosswalk push: `36258547920`;
- crosswalk PR: `36258552415`.

Artifact crosswalk:
- ID: `10911900788`;
- digest: `sha256:0556a3b5d142ea0142fc1f62ef0bb38144d74b54a500ab1bbc534481df3b5880`.

Google Drive:
- pacote `SBMI_POF_RS_market_crosswalk_v001.zip`;
- ID `1OpNbR9_IAaXU-pdjsiLyvG8hOuXG1Asi`.

## 11. Próxima etapa

1. construir fatores de atualização de preços compatíveis para:
   - Higiene/Cuidados Pessoais;
   - Produtos farmacêuticos/Remédios;
   - Vestuário;
   - Móveis/artigos do lar;
   - Eletrodomésticos;
   - Serviços pessoais;
2. preservar cada módulo separadamente;
3. somente depois avaliar a soma de módulos em uma dimensão setorial mais ampla;
4. confrontar demanda residente estimada com faturamento fiscal observado quando houver recorte territorial-setorial compatível.
