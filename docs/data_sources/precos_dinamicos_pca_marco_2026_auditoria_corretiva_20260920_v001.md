# Preços Dinâmicos — PCA-RE março/2026 — auditoria corretiva do valor estadual — v001

**Data da auditoria:** 20/09/2026  
**Indicador:** PCA-RE — Preço da Cesta de Alimentos  
**Competência:** março/2026  
**Geografias relacionadas:** Rio Grande do Sul e COREDE Fronteira Oeste  
**Status:** correção de transcrição no seed; série histórica continua incompleta.

## 1. Problema detectado

O seed histórico registrava para março/2026:

- Fronteira Oeste: R$ 274,55;
- Rio Grande do Sul: R$ 289,85;
- variação estadual no mês: -0,17%;
- variação estadual em 12 meses: -2,84%.

A combinação entre valor e variação mensal motivou reauditoria.

## 2. Fonte primária

Portal do Estado do Rio Grande do Sul / Secretaria da Fazenda — Ascom Sefaz.

Título: **Preço médio da cesta de alimentos tem queda em março no Rio Grande do Sul**  
Publicação: **02/04/2026 às 18h27**  
URL: https://www.estado.rs.gov.br/preco-medio-da-cesta-de-alimentos-tem-queda-em-marco-no-rio-grande-do-sul

A publicação oficial informa:

- PCA-RE estadual em março/2026: **R$ 287,85**;
- variação mensal: **-0,17%**;
- variação em 12 meses: **-2,84%**.

## 3. Checagem calculada

Fevereiro/2026: R$ 288,33.

Fórmula:

`(287,85 / 288,33 - 1) × 100 = -0,1665%`

Arredondamento a duas casas: **-0,17%**.

A checagem é consistente com a variação mensal publicada.

## 4. Conclusão de auditoria

**Dado observado corrigido:** o valor estadual de março/2026 é **R$ 287,85**.

**Classificação do valor anterior R$ 289,85:** erro de transcrição no seed.

A correção não altera as demais taxas estaduais já registradas para março:

- mês: -0,17%;
- ano: -1,16%;
- 12 meses: -2,84%.

## 5. Efeito no comparativo Fronteira Oeste × RS

Mantendo o valor observado da Fronteira Oeste em R$ 274,55:

`(274,55 / 287,85 - 1) × 100 = -4,6205%`

**Dado calculado corrigido:** Fronteira Oeste estava **4,62% abaixo** do nível estadual em março/2026.

O cálculo anterior de -5,28% fica invalidado porque dependia do valor estadual incorreto.

## 6. Artefatos corrigidos

- `docs/data_sources/precos_dinamicos_pca_fo_rs_historico_seed_20260920_v001.csv`;
- `docs/caderno_base/analise_precos_dinamicos_serie_historica_seed_20260920_v001.md`;
- aba `PCA_seed` da matriz exploratória no Drive.

## 7. Limitações

- a série mensal FO × RS de 2026 ainda possui lacunas;
- não interpolar competências ausentes;
- a correção estadual não fornece, por si só, os valores faltantes da Fronteira Oeste;
- não calcular tendência mensal, volatilidade ou sazonalidade enquanto a cobertura continuar incompleta.

## 8. Status editorial

Correção de controle da série seed. **Não gera novo Delta_cadernos isoladamente.**

O benchmark promovido de agosto/2026 permanece válido.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
