# PE39/2026 — clusters técnicos oficiais — v002

**Data de consolidação:** 20/09/2026  
**Abrangência geográfica:** Município de São Borja/RS  
**Processo:** Pregão Eletrônico 39/2026 — Processo 14698/2026  
**Controle PNCP:** `88489786000101-1-000136/2026`

## Fonte

- PNCP — metadados e itens oficiais do PE39/2026;
- Edital e Anexos do PCE 39/2026;
- Termo de Referência;
- Ata Final gerada em 25/08/2026.

## Unidade de análise

Cada linha do arquivo `technical_clusters_official.csv` é um **cluster técnico normalizado**, que agrega itens de mesma família/especificação quando diferem apenas por cor ou por repartição principal/reservada.

Unidades:
- quantidade: metros;
- valor: R$ correntes do valor estimado do PE39/2026;
- participação: percentual do valor estimado dos 18 condutores prioritários.

Denominador:

`R$ 533.194,40`.

Fórmula:

`participacao_condutores_pct = valor_estimado_cluster / 533.194,40 × 100`.

## Correções em relação à v001

- substitui `SECONDARY_MIRROR_PENDING_OFFICIAL_TR_RECONCILIATION` por `OFFICIAL_PNCP_TR_ATA_RECONCILED`;
- confirma as nove especificações básicas T01–T09;
- confirma T05 como 2.820 m divididos em:
  - item 35: 2.115 m = 75%, parcela principal;
  - item 36: 705 m = 25%, cota reservada ME/EPP;
- preserva a normalização por cluster sem confundir cluster com item licitatório.

## Limitações

- descrição normalizada não acrescenta requisito técnico ausente do documento oficial;
- classificação de proposta ou presença de produto em catálogo não deve ser inferida desta tabela;
- valor estimado não é valor contratado, empenhado ou pago;
- o desenho de benefício/cota é propriedade do certame, não característica mercadológica permanente da categoria.

## Governança

A v001 permanece preservada para trilha de auditoria.  
Caderno-Base v028 permanece read-only.  
PR #41 permanece aberto, draft e sem merge.
