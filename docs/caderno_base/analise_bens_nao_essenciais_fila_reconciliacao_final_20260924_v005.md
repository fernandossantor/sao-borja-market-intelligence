# Bens não essenciais — fila priorizada de reconciliação final v005 — 24/09/2026

## 1. Atualização

A v005 incorpora o lote 23 e o universo candidato v005.

Contagem:

- **P0: 1 registros de controle**;
- **P1: 18 registros de controle**;
- **P2: 17 registros de controle**;
- **P3: 37 registros de controle**;
- **P4: 67 registros de controle**;

Total: **140 registros de controle**.

## 2. Efeito do lote 23

Seis registros deixam P1 porque sua função para o cenário-base foi decidida:

- Quero-Quero `96.418.264/0028-59` — storefront distinto;
- Quero-Quero `96.418.264/0533-30` — unidade jurídica ativa, mas não adicionada como storefront-base;
- Tottal Casa & Lazer `92.012.467/0094-79` — storefront distinto;
- Por Menos `92.012.467/0121-86` — storefront distinto;
- Tech Box `92.012.467/0265-60` — storefront distinto;
- Pormenos `92.012.467/0451-90` — storefront distinto.

## 3. Estado da fila

Permanece apenas um P0:

- 7 Povos Kids — conflito cadastral ativa × baixada.

Os P1 restantes concentram:

- CNPJs adicionais cuja função física ainda pode alterar o número de unidades;
- sucessões e homonímias;
- candidatos marca↔CNPJ;
- operadores atuais sem identidade jurídica fechada.

## 4. Próxima sequência P1

Priorizar:

1. M.H. Moda Íntima;
2. Brasil Free Shop;
3. RM2S;
4. João e Maria Pet;
5. Barraca Missões;
6. Requinte;
7. Pompéia;
8. sucessões/homonímias de Amei, Veterinária São Francisco, Excêntrica e Rilu.

## 5. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Nenhum indicador canônico foi recalculado.

## 6. Artefato

`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v005.csv`
