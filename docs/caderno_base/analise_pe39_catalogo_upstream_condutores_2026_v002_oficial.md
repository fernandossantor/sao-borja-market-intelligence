# PE39/2026 — catálogo upstream de condutores / Cigame — v002 — reconciliação oficial

**Data:** 20/09/2026  
**Status:** aprofundamento dirigido após reconciliação do Edital/TR e da Ata Final  
**Unidade analítica:** `objeto/grupo de produto × oferta local × participação × escala × habilitação × preço/frete/logística`

## 1. Correção de enquadramento

A v001 utilizou a relação histórica Iluminar–Cigame, documentada no POM 2025, como uma rota observável para testar se produtos tecnicamente próximos aos condutores do PE39 estavam acessíveis em catálogo upstream.

Essa evidência continua válida, mas deve ser lida de forma estritamente **operator-neutral**:

- Cigame é uma rota upstream documental observada em um caso;
- a relação histórica de uma empresa com a distribuidora não é atributo do mercado local;
- catálogo não prova estoque, crédito, prazo, preço, capacidade local nem participação;
- a Ata Final demonstrou que o universo relevante de fornecedores e marcas é mais amplo do que essa única rota.

## 2. Mudança de qualidade da especificação

Na v001, os nove clusters ainda dependiam do espelho secundário do certame.

A auditoria oficial do PNCP/Edital/TR confirmou as descrições básicas dos 18 itens prioritários e dos nove clusters T01–T09. Portanto, a comparação de catálogo passa a usar **especificações oficiais do PE39**, não apenas descrição secundária.

Também foi confirmado que:
- item 35 = parcela principal de 2.115 m;
- item 36 = cota reservada ME/EPP de 705 m;
- total T05 = 2.820 m;
- repartição = 75%/25%.

## 3. Resultado por cluster após reconciliação oficial

| Cluster | Valor estimado | Evidência Cigame | Estado v002 |
|---|---:|---|---|
| T01 | R$ 26.208,00 | cabo chumbo cobre PVC 70°C 2x4mm, 450/750V | STRONG_UPSTREAM_MATCH_OFFICIAL_SPEC |
| T02 | R$ 27.468,00 | produto exato não localizado na busca dirigida | NOT_DEMONSTRATED_IN_PUBLIC_CATALOG |
| T03 | R$ 117.520,00 | 16mm² 0,6/1kV ATOX em parte das cores | PARTIAL_COLOR_MATCH_OFFICIAL_SPEC |
| T04 | R$ 19.836,00 | PP 2x2,5mm encontrado em 500V, PE39 exige 1kV | BLOCKED_VOLTAGE_MISMATCH_CONFIRMED |
| T05 | R$ 103.353,00 | 4x10mm/1kV HEPR/ATOX encontrados, mas PE39 exige PP | BLOCKED_CONSTRUCTION_MISMATCH_CONFIRMED |
| T06 | R$ 45.534,40 | quadruplex 3x16+16mm; PE39 informa multiplex 4x16mm² 1kV Al | POTENTIAL_ARCHITECTURE_MATCH_NOT_EQUIVALENT |
| T07 | R$ 50.520,00 | flexível Cu 6mm² PVC 70°C nas três cores | STRONG_UPSTREAM_MATCH_OFFICIAL_SPEC |
| T08 | R$ 68.850,00 | família 10mm² PVC 70°C localizada parcialmente por cor | PARTIAL_COLOR_MATCH_OFFICIAL_SPEC |
| T09 | R$ 73.905,00 | flexível Cu 25mm² PVC 70°C nas três cores | STRONG_UPSTREAM_MATCH_OFFICIAL_SPEC |

## 4. Cobertura documental upstream

Os matches fortes permanecem:
- T01;
- T07;
- T09.

Valor estimado conjunto:

`R$ 26.208,00 + R$ 50.520,00 + R$ 73.905,00 = R$ 150.633,00`.

Participação nos R$ 533.194,40 dos condutores prioritários:

`R$ 150.633,00 / R$ 533.194,40 × 100 = 28,25%`.

### Classificação do indicador

**Dado calculado:** 28,25%.

**Significado permitido:** parcela do valor estimado da cesta para a qual uma rota upstream específica possui match forte em catálogo público, agora reconciliado com a especificação oficial.

**Não significa:**
- 28,25% de capacidade local;
- 28,25% de estoque local;
- 28,25% de participação potencial;
- market share;
- acesso de todos os operadores locais à Cigame;
- preço competitivo.

## 5. Mismatches agora confirmados por fonte oficial

### T04 — PP 2x2,5mm 1kV

O PE39 oficial exige **1kV**. O produto Cigame localizado na busca anterior é **500V**.

Status: `BLOCKED_VOLTAGE_MISMATCH_CONFIRMED`.

Não usar como equivalente.

### T05 — PP 4x10mm 1kV

O PE39 oficial exige **CABO PP 4 X 10,00 MM 1KV**. Os produtos Cigame anteriormente localizados eram 4x10mm/1kV em construções HEPR/ATOX, sem demonstração de construção PP.

Status: `BLOCKED_CONSTRUCTION_MISMATCH_CONFIRMED`.

A confirmação oficial fortalece o bloqueio técnico anterior.

## 6. T06 permanece arquiteturalmente indeterminado

A especificação oficial confirma “CABO MULTIPLEX 4 X 16,00 MM 1KV - ALUMÍNIO”.

O catálogo Cigame localizado traz arquitetura quadruplex 3x16+16mm. Há proximidade funcional, mas a descrição oficial não fornece base suficiente para declarar equivalência entre as construções.

Status: `POTENTIAL_ARCHITECTURE_MATCH_NOT_EQUIVALENT`.

## 7. Reinterpretação após a Ata Final

A Ata Final muda a função analítica do catálogo upstream.

**Dado observado:** o certame atraiu múltiplos distribuidores/fornecedores e ao menos um operador cadastralmente local apresentou propostas nas 18 linhas prioritárias.

**Interpretação:** a questão já não pode ser formulada como “há acesso upstream possível?”. Há evidência de que o mercado consegue formar propostas para a cesta. O problema passa a ser explicar a conversão:

`rota de abastecimento → custo de aquisição → frete/logística → capital/estoque → preço entregue → diligência/habilitação → resultado`.

A Cigame continua útil como **uma rota comparável** para investigar custo e disponibilidade, não como explicação do mercado local.

## 8. Implicação para a contestabilidade territorial

A evidência conjunta permite separar:

1. **acesso documental a catálogo upstream:** observado em parte da cesta;
2. **participação B2G local:** observada no PE39;
3. **classificação processual:** observada em 15/18 linhas para ao menos um operador local;
4. **competitividade de preço:** desfavorável nas 15 linhas comparáveis desse operador;
5. **capacidade física/estoque:** ainda não observada;
6. **execução posterior:** ainda não observada.

Nenhum desses gates deve ser usado como proxy dos demais.

## 9. Próxima ação dirigida

O próximo teste upstream deve ser condicionado à territorialização completa dos participantes:

- identificar todos os participantes locais ou com footprint local;
- somente para esses operadores, levantar rotas de abastecimento documentadas;
- comparar marcas/modelos efetivamente ofertados no PE39 com fornecedores upstream;
- testar se a diferença de preço pode ser associada a rota de compra, escala, crédito, frete ou outro mecanismo observável;
- preservar T04/T05 bloqueados na rota Cigame enquanto os mismatches permanecerem.

## 10. Fontes e limitações

**Fontes:**
- PNCP — PE39/2026, Edital, Termo de Referência e Ata Final;
- catálogo público Cigame, consulta de 20/09/2026;
- POM 2025 para a relação histórica de um operador com a Cigame.

**Limitações:**
- catálogo público ≠ estoque;
- relação de 2025 ≠ compra em 2026;
- produto upstream ≠ disponibilidade para um operador local;
- classificação em licitação ≠ validação técnica integral para todo não vencedor;
- percentuais usam valores estimados do PE39, não compras executadas;
- a rota Cigame não deve ser extrapolada para o conjunto dos operadores.

## 11. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`;
- a v001 permanece preservada como trilha de auditoria.
