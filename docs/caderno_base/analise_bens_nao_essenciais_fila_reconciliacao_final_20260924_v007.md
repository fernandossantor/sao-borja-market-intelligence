# Bens não essenciais — fila priorizada de reconciliação final v007 — 24/09/2026

## 1. Atualização

A v007 incorpora o fechamento P1 do lote 25.

Contagem:

- **P0: 1 registros de controle**;
- **P2: 33 registros de controle**;
- **P3: 35 registros de controle**;
- **P4: 71 registros de controle**;

Total: **140 registros de controle**.

## 2. Estado da fila

- **P0:** permanece apenas 7 Povos Kids;
- **P1:** 0 registros;
- **P2:** concentra reconciliações jurídicas e cadastrais não bloqueantes do número de storefronts;
- P3/P4 permanecem como confirmação/editorial/histórico.

## 3. Consequência analítica

A condição estabelecida para um primeiro recálculo exploratório está quase satisfeita:

- todos os P1 que podiam adicionar/remover storefronts foram decididos;
- o único P0 pode ser tratado por cenário de sensibilidade.

O próximo passo é construir uma tabela de storefronts reconciliados e calcular:

1. cenário-base conservador — sem 7 Povos Kids;
2. cenário de sensibilidade — incluindo 7 Povos Kids.

Nenhum desses resultados deve ser promovido a indicador canônico neste estágio.

## 4. Governança

- v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge.

## 5. Artefato

`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v007.csv`
