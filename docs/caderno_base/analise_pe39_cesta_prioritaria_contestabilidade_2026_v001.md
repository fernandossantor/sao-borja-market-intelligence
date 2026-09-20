# PE 39/2026 — cesta prioritária para auditoria de contestabilidade — v001

## 1. Regra

A taxonomia v001 demonstrou que tratar 86 itens com igual prioridade dispersaria esforço.

Foi aplicada uma regra mecânica e reproduzível:

1. calcular `valor_estimado_item = quantidade × valor_unitário_ref`;
2. ordenar os 86 itens por valor estimado decrescente;
3. incluir itens até atingir pelo menos **65%** do valor total estimado.

## 2. Resultado calculado

- universo: 86 itens;
- valor estimado total: **R$ 1.074.671,14**;
- cesta prioritária: **24 itens**;
- valor acumulado: **R$ 703.986,45**;
- participação acumulada: **65,51%**.

A cesta reduz o universo inicial em **72,09% dos itens**, preservando cerca de dois terços do valor estimado.

## 3. Composição da cesta prioritária

| Família | Itens | Valor na cesta | % do total do PE39 |
|---|---:|---:|---:|
| CONDUTORES | 18 | R$ 533.194,40 | 49,61% |
| ILUMINACAO | 2 | R$ 78.882,30 | 7,34% |
| PROTECAO_DISTRIBUICAO | 3 | R$ 71.609,75 | 6,66% |
| FERRAGENS_FIXACAO | 1 | R$ 20.300,00 | 1,89% |

Condutores sozinhos representam **49,61%** de todo o valor estimado do PE39 dentro da cesta selecionada.

## 4. Dez maiores itens por valor estimado

| Rank | Item | Família | Valor estimado |
|---|---:|---|---:|
| 1 | 35 — Cabo PP 4x10mm 1kV | CONDUTORES | R$ 77.514,75 |
| 2 | 60 — Refletor LED 200W | ILUMINACAO | R$ 54.238,30 |
| 3 | 49 — Cabo multiplex 4x16mm 1kV alumínio | CONDUTORES | R$ 45.534,40 |
| 4 | 18 — Cabo flexível 16mm 0,6/1kV azul ATOX | CONDUTORES | R$ 42.500,00 |
| 5 | 25 — Cabo flexível 16mm 0,6/1kV verde ATOX | CONDUTORES | R$ 42.500,00 |
| 6 | 41 — Cabo flexível 16mm 0,6/1kV preto ATOX | CONDUTORES | R$ 32.520,00 |
| 7 | 14 — Caixa CD para 12 disjuntores | PROTECAO_DISTRIBUICAO | R$ 27.474,60 |
| 8 | 8 — Fio plastichumbo cobre 2x2,5mm | CONDUTORES | R$ 27.468,00 |
| 9 | 7 — Fio plastichumbo cobre 2x4,0mm | CONDUTORES | R$ 26.208,00 |
| 10 | 36 — Cabo PP 4x10mm 1kV | CONDUTORES | R$ 25.838,25 |

## 5. Interpretação

A cesta prioritária é um instrumento de **auditoria**, não de compra.

Ela define onde procurar primeiro:

`oferta local equivalente → estoque/disponibilidade → especificação → preço entregue → prazo → habilitação`.

O ganho metodológico é importante: não é necessário auditar os 86 itens com a mesma profundidade para testar se existe contestabilidade local materialmente relevante.

## 6. Gate de oferta local

Um operador só deve entrar como candidato B2G para um item se houver evidência de:

1. CNPJ ativo e presença em São Borja;
2. CNAE/objeto compatível com a família;
3. indício verificável de comercialização do tipo de produto;
4. capacidade de atender quantidade/prazo ou rota realista de abastecimento;
5. habilitação compatível quando o edital exigir.

Presença de loja ou CNAE compatível, isoladamente, é apenas **oferta potencial cadastral**.

## 7. Próxima ação dirigida

O próximo cruzamento deve começar pelos **18 itens de condutores** presentes na cesta, porque eles concentram **R$ 533.194,40**.

Depois:
- iluminação;
- proteção/distribuição;
- ferragens/fixação.

Somente se houver candidato local documentalmente compatível devem ser abertos preço, estoque e habilitação.

## 8. Limitações

- itens e valores de referência ainda vêm de indexador secundário;
- valor de referência não é preço contratado;
- cesta de 65% é regra de priorização SBMI, não classificação oficial;
- exclusão da cauda não significa irrelevância operacional dos itens restantes;
- equivalência técnica ainda precisa de edital/TR oficial.

## 9. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
