# Serviços — estrutura SINAC/SIMEI por submercados POM — v001

**Data:** 20/09/2026  
**Posição dos optantes:** 12/09/2026  
**Geografia:** São Borja/RS  
**Fonte:** Receita Federal — Estatísticas do Simples Nacional  
**Recorte:** crosswalk conservador CNAE → mercado POM de Serviços  
**Status:** aprofundamento setorial do bloco 42.94.

## 1. Objeto

Decompor os **947 optantes SINAC** e **728 optantes SIMEI** classificados no recorte conservador de Serviços segundo os submercados efetivamente delimitados pelo POM.

Regra:

> os valores medem optantes por CNAE no recorte, não empresas ativas equivalentes, faturamento, emprego, market share ou volume de demanda.

## 2. Estrutura por submercado

| Submercado POM | SINAC | % do recorte SINAC | SIMEI | % do recorte SIMEI | SIMEI/SINAC |
|---|---:|---:|---:|---:|---:|
| Salões de beleza e barbearias | 385 | 40,65% | 370 | 50,82% | 96,10% |
| Oficinas automotivas | 318 | 33,58% | 261 | 35,85% | 82,08% |
| Clínicas e consultórios — recorte CNAE POM | 106 | 11,19% | 0 | 0,00% | 0,00% |
| Assistências técnicas e reparos | 100 | 10,56% | 84 | 11,54% | 84,00% |
| Hotelaria e alojamento | 27 | 2,85% | 6 | 0,82% | 22,22% |
| Lavanderias | 11 | 1,16% | 7 | 0,96% | 63,64% |
| **Total** | **947** | **100,00%** | **728** | **100,00%** | **76,87%** |

## 3. Concentração do recorte em serviços pessoais e automotivos

Salões/barbearias + oficinas:

- SINAC: `385 + 318 = 703`;
- `703 / 947 × 100 = 74,23%`;
- SIMEI: `370 + 261 = 631`;
- `631 / 728 × 100 = 86,68%`.

**Dado calculado:** esses dois submercados respondem por 74,23% dos optantes SINAC e 86,68% dos optantes SIMEI do recorte conservador de Serviços.

Isso descreve a composição do recorte POM/CNAE, não a participação econômica dos dois segmentos no mercado municipal de serviços.

## 4. Salões de beleza e barbearias

- 385 SINAC;
- 370 SIMEI;
- SIMEI/SINAC = **96,10%**.

É o maior submercado do recorte tanto em SINAC quanto em SIMEI.

**Interpretação:** a estrutura tributária observada é fortemente associada à microescala formal dentro deste recorte.

Não inferir:

- baixa renda;
- baixa produtividade;
- informalidade;
- quantidade de pontos físicos;
- participação das atividades no gasto das famílias.

## 5. Oficinas automotivas

- 318 SINAC;
- 261 SIMEI;
- SIMEI/SINAC = **82,08%**.

O resultado reforça que oficinas constituem um dos grandes blocos formais do mercado de serviços estudado.

A leitura pode ser triangulada futuramente com:

- frota;
- divisão 45/estrutura empresarial;
- emprego formal;
- jornada POM;
- preço e disponibilidade de peças.

Essas bases não devem ser somadas.

## 6. Clínicas e consultórios

O recorte conservador registra:

- 106 SINAC;
- nenhuma ocorrência SIMEI na extração corrente do crosswalk.

A ausência de linhas SIMEI **não deve ser interpretada isoladamente como inexistência de microempresas ou pequenos prestadores de saúde**. Ela descreve apenas o resultado da fotografia SIMEI e das regras CNAE usadas no recorte.

## 7. Assistências técnicas e reparos

- 100 SINAC;
- 84 SIMEI;
- SIMEI/SINAC = **84,00%**.

Esse bloco é relevante para bens duráveis porque reparação e pós-venda podem funcionar como extensão do mercado de bens não essenciais, ainda que sejam contabilizados separadamente como serviços.

Não somar oferta de reparação ao número de varejistas de bens não essenciais.

## 8. Hotelaria e alojamento

- 27 SINAC;
- 6 SIMEI.

O número complementa, mas não substitui, o Cadastur:

- SINAC/SIMEI = estrutura de optantes por CNAE;
- Cadastur = cadastro turístico formal, com regras próprias e capacidade declarada em categorias específicas.

Não comparar 27 optantes com os 2 meios de hospedagem Cadastur como se uma base estivesse “errada”. Os universos são distintos.

## 9. Relação com o survey POM

O survey POM mede comportamento declarado de consumidores:

- pesquisa online;
- preço;
- atendimento;
- tempo de resposta;
- avaliações;
- agendamento;
- automação.

SINAC/SIMEI mede composição formal dos optantes no recorte CNAE.

A triangulação adequada é:

`estrutura de oferta formal por submercado + jornada declarada do consumidor`.

Ela não permite calcular demanda, faturamento ou market share.

## 10. Implicação mercadológica

O mercado de Serviços delimitado pelo POM é estruturalmente heterogêneo.

A fotografia SINAC/SIMEI mostra predominância numérica de:

1. serviços pessoais de beleza;
2. manutenção automotiva;
3. saúde ambulatorial/consultórios;
4. reparos/assistência técnica.

Isso recomenda que o caderno evite um diagnóstico único de “serviços” e organize implicações por submercado e jornada.

## 11. Artefato estruturado

- `docs/data_sources/sinac_simei_services_structure_20260920_v001.csv`.

## 12. Decisão editorial

**PROMOVER COMO APROFUNDAMENTO DO DELTA SINAC/SIMEI NO CADERNO DE SERVIÇOS E ALIMENTAÇÃO FORA DO LAR.**

Manter explícitos:

- posição 12/09/2026;
- unidade optantes;
- recorte CNAE/POM;
- diferença conceitual frente a RFB, RAIS, Cadastur e survey POM.

## 13. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
