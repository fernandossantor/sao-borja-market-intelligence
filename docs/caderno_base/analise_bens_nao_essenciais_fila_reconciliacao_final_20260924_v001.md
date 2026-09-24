# Bens não essenciais — fila priorizada de reconciliação final — 24/09/2026

## 1. Objetivo

Esta fila transforma o universo candidato reconciliado em uma sequência de trabalho orientada por **impacto potencial sobre o denominador**.

A prioridade é uma classificação calculada do SBMI; não é dado de fonte.

## 2. Critérios

- **P0 — bloqueio direto de inclusão/exclusão:** casos que podem decidir se uma operação entra ou sai da oferta corrente.
- **P1 — bloqueio de identidade/unidade:** casos que podem alterar número de unidades, sucessão, duplicidade, homonímia ou vínculo marca↔CNPJ.
- **P2 — inclusão provável com reconciliação:** não bloqueia a existência da operação, mas precisa ser fechada antes do universo canônico.
- **P3 — pendência não bloqueante para recálculo exploratório:** ativo/relevante com questão de marca, endereço ou metadado.
- **P4 — confirmação de rotina/histórico:** não deve bloquear cálculo exploratório.

## 3. Contagem

- P0: **22 registros**;
- P1: **20 registros**;
- P2: **8 registros**;
- P3: **37 registros**;
- P4: **48 registros**;

Bloqueios P0+P1: **42 registros de controle**.

Esses 42 registros não equivalem a 42 operadores, pois podem existir pares original/substituto, várias filiais da mesma raiz e registros históricos/candidatos da mesma marca.

## 4. Grupos de ação

- `CONFIRMACAO_DE_ROTINA`: 48;
- `AJUSTE_METADADO_NAO_BLOQUEANTE`: 37;
- `VALIDAR_FUNCAO_FISICA_E_STORE_FRONT`: 11;
- `CONFIRMAR_STATUS_ATUAL`: 10;
- `RECONCILIACAO_FINAL`: 8;
- `PROVAR_VINCULO_MARCA_CNPJ`: 5;
- `BUSCAR_SUCESSOR_OU_CONTINUIDADE`: 4;
- `RECONCILIAR_INCLUSAO`: 4;
- `VALIDAR_PRESENCA_ATUAL_E_IDENTIDADE`: 3;
- `VALIDAR_SUBSTITUICAO_SUCESSAO`: 3;
- `VALIDAR_PERTENCIMENTO_SETORIAL`: 1;
- `VALIDAR_DUPLICIDADE_E_UNIDADE`: 1;

## 5. Ordem operacional recomendada

1. **P0 — confirmar status atual e continuidade/sucessão** dos CNPJs originais baixados, inaptos, conflitantes ou sem situação corrente.
2. **P0 — validar pertencimento ao escopo** de registros que podem sair do universo BNE.
3. **P0 — decidir linhas sem CNPJ** que têm presença atual ou apenas evidência histórica.
4. **P1 — validar função física** dos CNPJs adicionais de raízes multiunidade.
5. **P1 — resolver substituições, duplicidades, homonímias e vínculos marca↔CNPJ**.
6. Só então preparar um primeiro recálculo exploratório com cenário-base e faixa de incerteza.

## 6. Regra para o primeiro recálculo exploratório

O recálculo exploratório pode começar quando:

- todos os **P0** tiverem decisão provisória de inclusão/exclusão; e
- os **P1** que possam adicionar ou remover storefronts tiverem, no mínimo, uma decisão operacional explícita.

P2–P4 podem permanecer como pendências documentadas, desde que não alterem o denominador do cenário-base.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v001.csv`
