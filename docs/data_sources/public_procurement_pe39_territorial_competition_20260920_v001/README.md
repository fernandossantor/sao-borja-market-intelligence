# PE39/2026 — estrutura competitiva territorial dos 18 condutores prioritários

**Data:** 20/09/2026

## Fontes
- universo, propostas finais, classificação e arrematantes: Ata Final oficial do PE39/2026, PNCP;
- territorialização cadastral: RFB Dados Abertos CNPJ, competência 2026-08, arquivo previamente consolidado em
  `public_procurement_pe39_participants_20260920_v001`.

## Unidade observacional
`item licitatório × CNPJ participante`.

O arquivo `participant_item_matrix.csv` contém 194 observações, 18 itens e 22 CNPJs únicos.

## Derivados
- `item_summary.csv`: composição territorial e resultado por item;
- `participant_summary.csv`: amplitude de participação, vitórias, desclassificações e posição de preço;
- `best_valid_offer_by_geo_item.csv`: melhor oferta final válida em São Borja, demais municípios do RS e outras UFs;
- `cluster_winner_geography.csv`: distribuição territorial dos arrematantes por cluster;
- `summary.json`: indicadores agregados e validações.

## Regras
- preço relativo ao vencedor é calculado somente para `Arrematante` ou `Classificado`;
- propostas `Desclassificado` não entram como preço competitivo válido;
- item 7 permanece fracassado e não recebe vencedor artificial;
- `SAO_BORJA`, `RS_OTHER` e `OTHER_UF` são classes cadastrais, não distâncias logísticas.

## Limitação territorial
A execução corrente da territorialização RFB utilizou espelho de transporte controlado.
Portanto, 21 classificações externas permanecem exploratórias até reconciliação de bytes/hash ou
reexecução pelo host oficial. O participante local possui confirmação independente no projeto.

Localidade cadastral não equivale a origem do produto, estoque, capital, escala, retenção econômica,
custo de frete ou capacidade de entrega.

## Governança
Caderno-Base v028 permanece read-only. PR #41 permanece aberto, draft e sem merge.
