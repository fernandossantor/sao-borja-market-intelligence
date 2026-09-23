# Preços Dinâmicos — PCA-RE Fronteira Oeste × Rio Grande do Sul — jan–ago/2026 — v002

**Data da consolidação:** 22/09/2026  
**Fonte:** Receita Estadual/SEFAZ-RS — Boletins de Preços Dinâmicos  
**Indicador:** PCA-RE — Preço da Cesta de Alimentos da Receita Estadual  
**Geografias:** COREDE Fronteira Oeste e Rio Grande do Sul  
**Unidade:** R$ para o nível do PCA-RE; % para variações  
**Status:** série mensal jan–ago/2026 fechada sem interpolação; pronta para promoção como benchmark regional.

## 1. Objeto

Fechar a série mensal de 2026 que estava incompleta no seed de 20/09, preservando separadamente:

- valores observados/transcritos das tabelas oficiais;
- taxas oficiais publicadas;
- diferenças FO/RS calculadas pelo SBMI.

A série descreve o **COREDE Fronteira Oeste**, não o município de São Borja.

## 2. Série mensal consolidada

| Competência | FO PCA-RE | FO mês | FO ano | FO 12m | RS PCA-RE | RS mês | RS ano | RS 12m | FO vs RS |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| jan/2026 | R$ 275,41 | -1,14% | -1,14% | -0,38% | R$ 289,83 | -0,48% | -0,48% | -1,54% | -4,98% |
| fev/2026 | R$ 273,97 | -0,52% | -1,66% | -1,99% | R$ 288,33 | -0,52% | -0,99% | -2,83% | -4,98% |
| mar/2026 | R$ 274,55 | +0,21% | -1,45% | -3,22% | R$ 287,85 | -0,17% | -1,16% | -2,84% | -4,62% |
| abr/2026 | R$ 281,40 | +2,49% | +1,01% | -1,47% | R$ 296,26 | +2,92% | +1,73% | -0,96% | -5,02% |
| mai/2026 | R$ 285,58 | +1,49% | +2,51% | +1,10% | R$ 300,54 | +1,44% | +3,20% | +1,30% | -4,98% |
| jun/2026 | R$ 287,31 | +0,60% | +3,13% | +2,38% | R$ 301,22 | +0,23% | +3,44% | +1,40% | -4,62% |
| jul/2026 | R$ 282,74 | -1,59% | +1,49% | +1,14% | R$ 296,84 | -1,45% | +1,93% | +1,39% | -4,75% |
| ago/2026 | R$ 284,19 | +0,51% | +2,01% | +3,22% | R$ 298,61 | +0,60% | +2,54% | +3,49% | -4,83% |

## 3. Natureza dos dados

### Dados observados

Os níveis e as três taxas de cada geografia são transcrições das tabelas oficiais mensais da Receita Estadual.

Exceção de controle já documentada:

- o valor estadual de março foi corrigido para **R$ 287,85** após auditoria cruzada;
- o valor anteriormente transcrito como R$ 289,85 foi invalidado;
- a taxa mensal de -0,17% permaneceu e é coerente com fevereiro.

### Dados calculados

A coluna **FO vs RS** usa:

`(PCA_FO / PCA_RS - 1) × 100`.

Exemplo de agosto:

`(284,19 / 298,61 - 1) × 100 = -4,83%`.

## 4. Leitura temporal

### 4.1 Movimento comum das duas geografias

A série apresenta movimento semelhante:

- queda no início do ano;
- avanço mais forte entre abril e junho;
- recuo em julho;
- recuperação parcial em agosto.

Não se atribui causalidade comum apenas pela co-movimentação.

### 4.2 Pontos de mínimo e máximo

**Fronteira Oeste**
- mínimo jan–ago: **R$ 273,97 em fevereiro**;
- máximo jan–ago: **R$ 287,31 em junho**.

**Rio Grande do Sul**
- mínimo jan–ago: **R$ 287,85 em março**;
- máximo jan–ago: **R$ 301,22 em junho**.

### 4.3 Diferença de nível regional

Em todos os oito meses, o PCA-RE da Fronteira Oeste ficou abaixo da média estadual.

Faixa observada da diferença calculada:

- menor distância: **-4,62%** em março e junho;
- maior distância: **-5,02%** em abril;
- média simples das oito diferenças mensais: **-4,85%**.

A média simples é um resumo calculado do período, não um índice oficial.

### 4.4 Janeiro → agosto

Variação calculada entre os níveis de janeiro e agosto:

- FO: `(284,19 / 275,41 - 1) × 100 = +3,19%`;
- RS: `(298,61 / 289,83 - 1) × 100 = +3,03%`.

**Não chamar esses dois cálculos de “inflação acumulada oficial”.** São apenas mudanças entre dois níveis mensais. As taxas oficiais acumuladas no ano em agosto são:

- FO: **+2,01%**;
- RS: **+2,54%**.

## 5. Implicação mercadológica permitida

A série adiciona uma camada regional contínua de ambiente de preços alimentares:

- permite acompanhar pressão de preços mês a mês;
- contextualiza bens essenciais e alimentação fora do lar;
- permite comparar o nível regional com o estadual sem municipalizar o dado;
- ajuda a separar choque pontual de trajetória recente.

A persistência de um nível regional cerca de 4,6% a 5,0% inferior ao estadual é um fato descritivo da série, não evidência de menor custo de vida geral em São Borja.

## 6. O que não concluir

A série não demonstra:

- preço pago especificamente por famílias de São Borja;
- custo de compra de restaurantes;
- custo de vida municipal;
- renda disponível;
- margem do varejo;
- causalidade entre origem do abastecimento e preços;
- que todos os itens da cesta sejam mais baratos na Fronteira Oeste.

## 7. Fontes e auditabilidade

Boletins oficiais utilizados:

- janeiro/2026 — publicado em 03/02/2026;
- fevereiro/2026 — 03/03/2026;
- março/2026 — 01/04/2026, com correção estadual triangulada em publicação oficial de 02/04/2026;
- abril/2026 — 04/05/2026;
- maio/2026 — 01/06/2026;
- junho/2026 — 01/07/2026;
- julho/2026 — 01/08/2026;
- agosto/2026 — 01/09/2026.

Artefatos de auditoria:

- `docs/data_sources/precos_dinamicos_2026_target_extract_20260922_v001.md`;
- `docs/data_sources/precos_dinamicos_rs_jun_jul_2026_ocr_target_20260922_v001.md`;
- `docs/data_sources/precos_dinamicos_pca_marco_2026_auditoria_corretiva_20260920_v001.md`;
- `docs/data_sources/precos_dinamicos_pca_fo_rs_2026_jan_ago_v002.csv`.

## 8. Status editorial

**PROMOVER AO SUCESSOR COMO SÉRIE REGIONAL COMPLETA JAN–AGO/2026.**

Este bloco supera o status de seed da seção 42.98 porque as oito competências consecutivas de janeiro a agosto estão reproduzidas, sem interpolação.

O delta anterior de agosto/2026 continua válido como fotografia corrente; a nova série acrescenta a dimensão temporal.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
