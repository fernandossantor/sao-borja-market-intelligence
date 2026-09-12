# Caderno-Base Territorial v025 — fluxos financeiros, demografia empresarial e folha pública

**Data:** 2026-09-12  
**Geografia principal:** São Borja/RS  
**Planilha Drive:** `13z_rmkZriwLaark33q3hY4pzolmOS0SHXtOlmKrAHDE`  
**Documento narrativo Drive:** `19_Z_c9j-qvygt6E2OWVRJu9pj7emPYVYjQ0WNr37ZB8`

## 1. Regra metodológica

A v025 separa explicitamente dados observados, cálculos, interpretações e hipóteses. Não é construído índice sintético de retenção pela soma de VAB, folha, crédito, depósitos, benefícios ou ativos, pois são grandezas de natureza, universo e temporalidade distintos.

## 2. Demografia empresarial — Mapa de Empresas

**Fonte:** MEMP/DREI — Mapa de Empresas — Dados Abertos.  
**Período:** maio–julho/2026.  
**Unidade:** empresas/eventos cadastrais.  
**Geografia:** São Borja/RS.

| Período | Abertas | Fechadas | Ativas | Saldo | Fluxo bruto | Proxy rotatividade |
|---|---:|---:|---:|---:|---:|---:|
| 2026-05 | 82 | 44 | 6.950 | 38 | 126 | 1,81% |
| 2026-06 | 105 | 74 | 6.731 | 31 | 179 | 2,66% |
| 2026-07 | 106 | 59 | 6.825 | 47 | 165 | 2,42% |

No período: 293 aberturas, 177 fechamentos e saldo aritmético de +116, enquanto o estoque caiu 125 empresas entre maio e julho. Portanto, o estoque ativo não reconcilia mecanicamente com `abertas - fechadas`; não usar esses fluxos como coorte de sobrevivência ou taxa oficial de mortalidade.

## 3. SICOR/MDCR — crédito rural municipal

**Fonte:** Banco Central do Brasil — SICOR / Matriz de Dados do Crédito Rural.  
**Endpoint auditado:** `CusteioInvestimentoComercialIndustrialSemFiltros`.  
**Geografia:** São Borja, código IBGE `4318002`.  
**Cobertura:** jan/2013–ago/2026; 164 meses; 3.512 registros agregados.  
**Unidade:** contratos e R$ nominais.

Destaques anuais:
- 2021: R$ 624,05 milhões;
- 2022: R$ 799,11 milhões;
- 2023: R$ 896,44 milhões;
- 2024: R$ 723,89 milhões;
- 2025: R$ 566,69 milhões;
- jan–ago/2026: R$ 263,10 milhões em 462 contratos.

Em jan–ago/2026: 61,11% custeio, 15,69% investimento e 23,20% comercialização. O valor nominal do período ficou 33,46% abaixo de jan–ago/2025 e 55,61% abaixo do mesmo recorte de 2023.

**Limite:** crédito rural não é renda, lucro, produção nem excedente retido. A série deve ser deflacionada antes de interpretações de tendência real.

## 4. ESTBAN — intermediação bancária municipal

**Fonte:** Banco Central do Brasil — ESTBAN, documento 4500.  
**Geografia:** São Borja/RS, código IBGE `4318002`.  
**Extração promovida:** jan/2021–jun/2026; 66 meses; 57 verbetes; sem erros de extração.  
**Unidade:** R$ em saldos de fim de mês.

### 4.1 Operações de crédito e financiamento rural agrícola

| Período | Operações de crédito — 160 | Rural agrícola — 163 | 163 / 160 |
|---|---:|---:|---:|
| 2021-12 | R$ 745.123.351 | R$ 384.696.938 | 51,63% |
| 2022-12 | R$ 847.767.674 | R$ 452.229.747 | 53,34% |
| 2023-12 | R$ 927.149.581 | R$ 510.871.259 | 55,10% |
| 2024-12 | R$ 1.053.904.842 | R$ 569.330.664 | 54,02% |
| 2025-12 | R$ 994.066.629 | R$ 453.884.525 | 45,66% |
| 2026-06 | R$ 1.036.701.306 | R$ 514.467.918 | 49,63% |

Controle sazonal, sempre junho: participação rural agrícola no crédito = 49,45% (2021), 49,91% (2022), 51,59% (2023), 55,55% (2024), 47,64% (2025) e 49,63% (2026).

**Interpretação:** a agropecuária também constitui âncora da intermediação financeira local. Em jun/2026, aproximadamente metade do saldo de operações de crédito contabilizado para São Borja estava no verbete de financiamento rural agrícola.

**Limite:** isso não mede destino de lucro, riqueza dos residentes ou retenção patrimonial. O local de contabilização bancária pode divergir do local econômico final e verbetes hierárquicos não são aditivos.

### 4.2 Depósitos

- Poupança: R$ 227,82 mi em dez/2021 → R$ 170,07 mi em jun/2026.
- Depósitos a prazo: R$ 261,81 mi → R$ 150,02 mi.

Essas variações nominais **não** são evidência suficiente de fuga de capital. Mudanças de produto, instituição e booking podem alterar os saldos locais.

## 5. Folha pública — MPRS

**Fonte:** Ministério Público do Rio Grande do Sul — Portal da Transparência — Contracheque.  
**Competência:** jul/2026; folha NORMAL.  
**Territorialização:** `lotacao_s` contendo São Borja.  
**Grupos:** servidores ativos e membros ativos.

O JavaScript oficial do portal foi auditado para os campos de remuneração, confirmando `indenizacoes_tf` como **Indenizações (8)** e `total_creditos_tf` como **Total Bruto (9)**.

Resultados:
- servidores: 9 vínculos; Total Bruto R$ 134.074,97; líquido R$ 108.539,39;
- membros: 3 vínculos; Total Bruto R$ 142.980,32; líquido R$ 101.847,54;
- total: 12 vínculos; **Total Bruto R$ 277.055,29**; líquido R$ 210.386,93.

Lotação explícita inclui Promotorias Civil, Criminal e Especializada e a Secretaria-Geral da Promotoria de Justiça de São Borja.

Somado apenas como **ordem de grandeza documental** ao subtotal já auditado da v024, o conjunto federal civil parcial + Executivo estadual + MPRS alcança **R$ 9.551.979,21/mês**. Não é total consolidado da folha pública não municipal e os conceitos remuneratórios não são perfeitamente idênticos.

## 6. Diagnóstico v025

1. A hipótese de alta mortalidade/rotatividade empresarial continua **não verificada**: há somente três meses e não há benchmark; além disso, estoque e fluxos cadastrais não reconciliam mecanicamente.
2. A hipótese do agro como **âncora financeira** foi fortalecida: SICOR demonstra elevada escala de financiamento e ESTBAN mostra o rural agrícola em torno de metade das operações de crédito locais.
3. A hipótese de que o excedente agropecuário seja predominantemente gasto/investido fora de São Borja permanece **não verificada**. ESTBAN e SICOR não observam destino patrimonial do lucro.
4. A folha pública não municipal é uma âncora material de circulação cotidiana e continua subestimada no subtotal disponível; o MPRS comprova mais uma camada fora do Executivo estadual.

## 7. Próximas prioridades

- ampliar Mapa de Empresas e construir benchmark;
- deflacionar SICOR/ESTBAN e cruzar com produção, preços e choques climáticos;
- decompor ESTBAN por instituição e auditar a mudança no verbete 167 a partir de 2025;
- avançar em TJRS, DPERS, TCE e Legislativo, mantendo cada poder separado;
- territorializar Forças Armadas, PF e PRF somente se houver fonte oficial segura;
- avançar na retenção patrimonial por fontes imobiliárias/ITBI, propriedade societária e outras evidências adequadas.

## 8. Governança

O PR #41 deve permanecer **aberto, draft e sem merge** até autorização explícita.
