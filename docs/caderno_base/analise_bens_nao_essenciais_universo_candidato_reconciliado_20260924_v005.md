# Bens não essenciais — universo candidato reconciliado v005 — 24/09/2026

## 1. Atualização

A v005 incorpora o lote 23 de reconciliação P1.

O universo permanece com **140 registros de controle**. A mudança é qualitativa: seis registros externos deixam de bloquear a definição de storefront no cenário-base.

## 2. Quero-Quero

- `96.418.264/0028-59` passa a ser **storefront distinto** na Rua General Marques, 694 e corrige uma duplicidade do inventário.
- `96.418.264/0533-30` permanece como estabelecimento jurídico ativo da raiz, mas **não é contado como storefront no cenário-base** por ausência de evidência operacional suficiente.

O CNPJ original `96.418.264/0357-81`, Rua Coronel Aparício Mariense, 2635, permanece como a outra unidade comercial conhecida.

## 3. Grazziotin

Quatro CNPJs adicionais passam a ser elegíveis como storefronts distintos:

- Tottal Casa & Lazer — `92.012.467/0094-79`;
- Por Menos — `92.012.467/0121-86`;
- Tech Box — `92.012.467/0265-60`;
- Pormenos — `92.012.467/0451-90`.

A raiz comum deve permanecer explícita para análises de rede/concentração, sem fundir as unidades.

## 4. Efeito sobre o cenário-base

Cinco registros do lote entram como storefronts elegíveis e um permanece apenas na camada jurídica/sensibilidade.

Isso **não corresponde a +5 lojas líquidas em relação ao inventário original**, porque Quero-Quero `/0028-59` corrige uma linha duplicada que já ocupava posição no inventário.

O efeito líquido será calculado somente na consolidação do cenário-base completo.

## 5. Bloqueio remanescente

O único P0 continua sendo 7 Povos Kids.

A fila P1 é reduzida ao retirar os seis casos cuja função física foi decidida no lote 23.

## 6. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- nenhum indicador canônico foi recalculado.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_universo_candidato_reconciliado_20260924_v005.csv`
