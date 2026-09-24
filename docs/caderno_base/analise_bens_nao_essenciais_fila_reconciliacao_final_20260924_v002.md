# Bens não essenciais — fila priorizada de reconciliação final v002 — 24/09/2026

## 1. Atualização

A fila v002 incorpora o lote 19 e o universo candidato reconciliado v002.

Contagem atual de registros de controle:

- **P0: 13**;
- **P1: 21**;
- **P2: 12**;
- **P3: 37**;
- **P4: 57**.

Total: **140 registros de controle**.

A redução de P0 de 22 para 13 decorre de decisões explícitas no lote 19; não representa redução de nove lojas nem alteração automática da oferta.

## 2. P0 remanescentes

Permanecem bloqueios diretos:

- linha 100 — Loja Marlin Fashion — CNPJ inapto;
- linha 120 — Pimentas Boutique Sensual — sem evidência independente;
- linha 122 — 7 Povos Kids — conflito cadastral;
- linha 125 — Loja CHICMI — sem CNPJ/evidência suficiente;
- linha 126 — Loja do Ramada — apenas presença histórica;
- linha 132 — Loja Portal — presença atual, identidade jurídica pendente;
- linha 134 — Elegância Moda e Acessórios — sem identificação;
- linha 144 — Mundi Calçados — situação cadastral pendente;
- linha 147 — Ciranda Boutique — situação cadastral pendente;
- linha 154 — Akazzo — sem identificação;
- linha 188 — Bicho Mimado — CNPJ inapto, marca aparentemente operacional;
- linha 189 — Pet House — presença atual, identidade jurídica pendente;
- linha 190 — Ponto dos Pets — situação cadastral corrente pendente.

## 3. P1

A quantidade de P1 passou a 21 porque:

- Americanas deixou de ser P1 após confirmação do CNPJ corrente;
- Excêntrica e Rilu passaram de P0 para P1;
- permanecem 11 CNPJs adicionais de raízes que exigem validação de função física;
- permanecem vínculos marca↔CNPJ, homonímias, sucessões e correções de duplicidade.

## 4. Regra de continuidade

Antes do primeiro recálculo exploratório:

1. resolver os 13 P0;
2. decidir os P1 que podem alterar o número de storefronts;
3. permitir que P2–P4 permaneçam documentados quando não alterarem o denominador-base.

## 5. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- não houve recálculo de oferta, operadores, raízes ou concentração.

## 6. Artefato

`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v002.csv`
