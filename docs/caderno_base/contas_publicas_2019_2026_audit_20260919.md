# Contas públicas de São Borja — série fiscal anual 2019–2025 e execução parcial 2026

**Data de auditoria:** 19/09/2026  
**Abrangência geográfica:** Município de São Borja/RS — código IBGE 4318002  
**Período:** exercícios fechados 2019–2025 + execução corrente de 2026, sempre mantida separada  
**Status:** série fiscal agregada 2019–2025 fechada; histórico por credor anterior a 2026 ainda aberto  
**Caderno-Base:** v028 permanece read-only; este documento não promove conteúdo automaticamente.

## 1. Objetivo

Construir uma série fiscal comparável para São Borja que permita acompanhar, sem misturar conceitos contábeis:

- receita corrente;
- transferências correntes;
- FPM;
- quota-parte do ICMS;
- Fundeb;
- IPVA;
- ITR;
- despesa empenhada;
- despesa liquidada;
- despesa paga;
- pessoal e encargos;
- juros e encargos da dívida;
- investimentos;
- composição funcional;
- rubricas econômicas selecionadas de bens, serviços e obras.

O plano temporal obrigatório é:

- **2019–2025:** exercícios anuais fechados;
- **2026:** execução parcial/corrente, sem anualização ou projeção automática.

## 2. Fontes e natureza dos dados

### 2.1. Exercícios fechados 2019–2025

**Fonte observada oficial:** Tesouro Nacional — SICONFI, Declaração das Contas Anuais (DCA).

Anexos utilizados:

- DCA Anexo I-C — receitas orçamentárias;
- DCA Anexo I-D — despesas por natureza;
- DCA Anexo I-E — despesas por função.

A coleta oficial foi persistida em:

`docs/data_sources/sao_borja_public_accounts_siconfi_dca_2019_2025/`

A série reconciliada está em:

`docs/data_sources/sao_borja_public_accounts_reconciled_2019_2025/`

### 2.2. Execução corrente 2026

**Fonte observada oficial:** Portal da Transparência da Prefeitura Municipal de São Borja.

Recorte já fechado para a rodada corrente: **01/01/2026 a 18/09/2026**.

- pago total: **R$ 275.649.734,78**;
- 1.930 credores;
- 740 CNPJs;
- 1.190 CPFs;
- pago a CNPJ: **R$ 132.146.080,70**;
- pago a CPF: **R$ 143.503.654,08**.

Esses valores são parciais e não devem ser comparados como se 2026 fosse um exercício completo.

## 3. Auditoria da rota histórica do Portal PMSB

Foi testada a rota atual de despesas/credores para 2019–2026, inclusive com quatro variantes controladas de `dtDataImportacao`.

Resultado observado:

- `/despesas/loadLink/3` responde e produz parâmetros para todos os exercícios;
- 2026 retorna JSON válido no endpoint de credores;
- 2019–2025 retornam HTTP 200, mas o conteúdo é HTML com erro PostgreSQL:
  `invalid input syntax for type numeric: ""`.

Uma segunda auditoria comparou os parâmetros seguros produzidos pelo `loadLink` por exercício. Fora `iExercicio` e `dtFim`, não foi identificado parâmetro comum vazio que explique a falha histórica.

**Interpretação técnica:** trata-se de falha da rota/backend histórico atual, e não de evidência de ausência de dados.

**Decisão:** não forçar a rota nem transformar a falha em zero. O histórico por credor deverá ser buscado em TCE-RS/SIAPC ou outra rota oficial compatível.

## 4. Série fiscal reconciliada 2019–2025

Valores monetários abaixo são **observados na DCA**, em **R$ correntes de cada exercício**. A participação das transferências na receita corrente é **calculada**.

| Ano | Receita corrente bruta | Transferências correntes brutas | Transferências / receita | FPM bruto | ICMS bruto | Fundeb recebido | Despesa paga |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2019 | R$ 216.276.826,37 | R$ 160.074.494,30 | 74,01% | R$ 33.514.887,07 | R$ 45.216.301,60 | R$ 26.524.660,31 | R$ 191.651.936,23 |
| 2020 | R$ 240.855.632,77 | R$ 186.542.276,38 | 77,45% | R$ 35.122.569,29 | R$ 49.940.271,40 | R$ 31.693.906,49 | R$ 205.274.213,43 |
| 2021 | R$ 275.593.510,00 | R$ 206.740.655,52 | 75,02% | R$ 41.397.727,30 | R$ 59.731.078,36 | R$ 38.803.689,21 | R$ 254.675.811,28 |
| 2022 | R$ 274.248.986,22 | R$ 203.614.581,41 | 74,25% | R$ 47.072.399,25 | R$ 65.085.050,62 | R$ 45.461.394,40 | R$ 281.352.336,48 |
| 2023 | R$ 338.363.000,14 | R$ 251.995.259,04 | 74,47% | R$ 56.730.378,79 | R$ 81.612.527,10 | R$ 56.707.344,45 | R$ 325.447.344,00 |
| 2024 | R$ 378.375.538,79 | R$ 279.065.921,96 | 73,75% | R$ 64.355.742,12 | R$ 88.855.536,97 | R$ 62.224.496,65 | R$ 361.537.093,37 |
| 2025 | R$ 395.601.632,24 | R$ 295.354.550,35 | 74,66% | R$ 70.190.268,39 | R$ 91.970.014,58 | R$ 67.743.039,97 | R$ 394.580.772,11 |

**Cálculo:** a média simples anual de `transferências correntes brutas / receita corrente bruta` em 2019–2025 é **74,64%**.

Essa razão descreve a composição fiscal corrente observada; **não equivale** à dependência econômica total do município, à renda domiciliar, ao VAB da administração pública ou a uma taxa de retenção territorial.

## 5. Transferências realizadas — 2025

Valores observados na DCA:

- FPM bruto: **R$ 70.190.268,39**;
- quota-parte do ICMS bruta: **R$ 91.970.014,58**;
- Fundeb recebido bruto: **R$ 67.743.039,97**;
- IPVA bruto: **R$ 13.264.496,91**;
- ITR bruto: **R$ 2.522.026,39**.

A série completa preserva também as deduções de Fundeb e outras deduções para cálculo dos valores líquidos.

## 6. Despesas anuais

### 6.1. Estágios da despesa

| Ano | Empenhada | Liquidada | Paga |
|---:|---:|---:|---:|
| 2019 | R$ 204.284.306,08 | R$ 197.928.020,66 | R$ 191.651.936,23 |
| 2020 | R$ 222.077.534,06 | R$ 208.685.980,33 | R$ 205.274.213,43 |
| 2021 | R$ 268.051.343,20 | R$ 259.724.394,87 | R$ 254.675.811,28 |
| 2022 | R$ 295.318.628,15 | R$ 284.029.930,71 | R$ 281.352.336,48 |
| 2023 | R$ 347.372.553,24 | R$ 331.409.818,68 | R$ 325.447.344,00 |
| 2024 | R$ 387.550.396,08 | R$ 369.743.938,41 | R$ 361.537.093,37 |
| 2025 | R$ 425.648.386,56 | R$ 406.611.216,65 | R$ 394.580.772,11 |

Empenho, liquidação e pagamento são estágios contábeis distintos e não devem ser tratados como sinônimos.

### 6.2. Componentes selecionados — valores pagos

| Ano | Pessoal e encargos | Juros e encargos da dívida | Investimentos |
|---:|---:|---:|---:|
| 2019 | R$ 113.653.306,50 | R$ 1.650.427,63 | R$ 7.174.407,81 |
| 2020 | R$ 122.131.692,86 | R$ 1.302.671,63 | R$ 7.098.313,68 |
| 2021 | R$ 142.638.657,79 | R$ 2.349.372,51 | R$ 13.161.310,79 |
| 2022 | R$ 157.497.116,40 | R$ 3.323.354,57 | R$ 14.518.094,74 |
| 2023 | R$ 174.343.310,34 | R$ 4.327.864,84 | R$ 24.711.214,02 |
| 2024 | R$ 190.690.607,61 | R$ 5.296.681,56 | R$ 31.066.894,34 |
| 2025 | R$ 212.646.780,71 | R$ 5.359.527,63 | R$ 29.420.914,26 |

A DCA também preserva outras despesas correntes, amortização da dívida e rubricas econômicas selecionadas de material de consumo, distribuição gratuita, passagens, consultoria, serviços PF/PJ, TIC, obras e equipamentos.

## 7. Fórmulas calculadas

### Receita corrente líquida calculada

[
RC_{liq} = RC_{bruta} - Ded_{FUNDEB} - OutrasDed
]

### Transferências correntes líquidas calculadas

[
TC_{liq} = TC_{bruta} - Ded_{FUNDEB} - OutrasDed
]

### Participação das transferências correntes

[
PartTC_t = rac{TC_{bruta,t}}{RC_{bruta,t}} 	imes 100
]

### Variação nominal anual

[
Delta_t = left(rac{Valor_t}{Valor_{t-1}} - 1ight)	imes 100
]

### FPM líquido calculado

[
FPM_{liq} = sum ComponentesFPM_{brutos} - Ded_{FUNDEB} - OutrasDed
]

Os componentes que sustentam o cálculo do FPM permanecem preservados em arquivo de auditoria.

## 8. Controles de reconciliação

A série reconciliada passou pelos seguintes controles:

- os valores anuais de transferências correntes reproduzem, por arredondamento, os sete valores já registrados na matriz exploratória;
- a receita corrente bruta de 2025 reproduz o controle de **R$ 395,602 milhões**;
- a cobertura DCA é completa para 2019–2025 nos anexos I-C, I-D e I-E;
- nenhuma projeção de LOA/LDO foi misturada à série realizada;
- 2026 permanece separado como execução corrente.

## 9. Limitações

1. Os valores são nominais e não foram deflacionados.
2. A DCA é anual; não deve ser usada para fabricar um valor anual fechado de 2026.
3. Rubrica econômica de despesa não equivale ao universo jurídico de licitações e contratos.
4. Despesa paga agregada não identifica automaticamente credor, fornecedor, objeto ou destino territorial.
5. A classificação funcional não é uma classificação de mercado.
6. Histórico por credor 2019–2025 ainda não foi recuperado.
7. Qualquer geografia histórica de fornecedor exigirá cadastro empresarial temporal compatível com cada exercício.
8. Transferências municipais não são VAF, VAB, renda domiciliar ou gasto privado.

## 10. Diagnóstico e continuidade

**Fato observado:** a série fiscal agregada anual 2019–2025 está agora suficientemente auditada para deixar de ser uma lacuna operacional.

**Fato calculado:** as transferências correntes brutas representaram, em média simples anual, 74,64% da receita corrente bruta no período.

**Interpretação:** o município possui peso estrutural elevado de transferências na composição das receitas correntes, mas esse indicador descreve a arquitetura fiscal do governo municipal e não autoriza inferências diretas sobre dependência econômica das famílias ou da produção local.

**Lacuna remanescente:** a principal frente de contas públicas migra da série agregada para o histórico de pagamentos por credor, objetos/instrumentos e geografia temporal dos fornecedores.

**Próxima rota:** TCE-RS/SIAPC para 2019–2025, preservando a execução 2026 do Portal PMSB como camada separada.

## 11. Arquivos auditáveis

- `docs/data_sources/sao_borja_public_accounts_siconfi_dca_2019_2025/`
- `docs/data_sources/sao_borja_public_accounts_reconciled_2019_2025/`
- `docs/data_sources/sao_borja_public_accounts_history_diagnostic_2019_2026/`
- `docs/data_sources/sao_borja_public_accounts_params_diagnostic/`
- `docs/data_sources/sao_borja_transparencia_creditors_2026/`
- `docs/data_sources/sao_borja_transparencia_cnpj_rubricas_2026/`

