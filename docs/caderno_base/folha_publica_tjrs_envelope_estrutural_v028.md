# Caderno-Base Territorial — v028 — envelope estrutural TJRS e fechamento da folha pública

**Data:** 2026-09-12  
**Geografia:** São Borja/RS  
**Escopo:** encerrar, até o limite documental atual, a frente da folha pública dos demais poderes sem criar um subtotal artificialmente homogêneo.

## Artefatos canônicos no Drive

- Planilha v028: `1JiooE7WI2XTGCIh-ugPMh1CoHFhTW8kzOGgQSyrMwzo`
- Caderno narrativo v028: `1Mhqo-zEULoyGVpevBRkIZn7mKkO6VOncE-WygmSWTP4`
- Registro metodológico v028: `1I18n2oOkOIUnlFDs3C742P_ozRzerZP8l_9l_MNnCvE`

Abas novas:

- `TJRS_vencimento_estrutural_v028`
- `TJRS_magistratura_estrutura_v028`
- `Folha_publica_sintese_v028`
- `Auditoria_v028`

## 1. Objeto

A v028 combina:

1. composição oficial dos **32 cargos providos** na Comarca de São Borja, junho/2026;
2. estrutura remuneratória oficial dos cargos efetivos do TJRS, julho/2026.

O cruzamento produz uma **estimativa estrutural do vencimento básico**, e não a folha efetivamente paga.

## 2. Composição dos 32 cargos efetivos

| Cargo | Quantidade |
|---|---:|
| Analista do Poder Judiciário — áreas Administrativa/Judiciária/Serviço Social | 4 |
| Auxiliar de Serviços Gerais | 1 |
| Oficial Ajudante | 1 |
| Oficial de Justiça Estadual | 7 |
| Técnico do Poder Judiciário | 19 |
| **Total** | **32** |

A composição é observada no relatório oficial **Quantitativo de Cargos Providos nas Comarcas**, referência junho/2026.

Controle independente: TLP 1 + TLP 2 registram `LR_EFET = 32` nas unidades de São Borja no fechamento de 2025/início de 2026. A coincidência é classificada como **coerência cruzada forte**, não identidade temporal.

## 3. Vencimentos básicos oficiais — julho/2026

Fonte:

`https://www.tjrs.jus.br/static/2026/08/26-07-estrutura-remuneratoria-do-cargos-efetivos.pdf`

| Cargo | Referência mínima | Valor mínimo | Referência máxima | Valor máximo |
|---|---|---:|---|---:|
| Analista do Poder Judiciário | A1 | R$ 9.226,01 | A15 | R$ 18.452,01 |
| Auxiliar de Serviços Gerais | A1 | R$ 2.463,19 | A12 | R$ 4.926,38 |
| Oficial Ajudante | A1 | R$ 8.491,68 | A12 | R$ 16.983,37 |
| Oficial de Justiça Estadual | A1 | R$ 7.982,58 | A15 | R$ 17.529,42 |
| Técnico do Poder Judiciário | A1 | R$ 4.843,63 | A15 | R$ 11.993,81 |

**Natureza:** DADO OBSERVADO.  
**Unidade:** R$/mês de vencimento básico.  
**Abrangência:** Poder Judiciário do RS.

## 4. Faixa estrutural do vencimento básico

Fórmulas:

`massa_min_cargo = quantidade × vencimento_básico_mínimo`

`massa_max_cargo = quantidade × vencimento_básico_máximo`

Resultados:

| Cargo | Massa básica mínima | Massa básica máxima |
|---|---:|---:|
| Analistas | R$ 36.904,04 | R$ 73.808,04 |
| Auxiliar de Serviços Gerais | R$ 2.463,19 | R$ 4.926,38 |
| Oficial Ajudante | R$ 8.491,68 | R$ 16.983,37 |
| Oficiais de Justiça | R$ 55.878,06 | R$ 122.705,94 |
| Técnicos | R$ 92.028,97 | R$ 227.882,39 |
| **Total** | **R$ 195.765,94** | **R$ 446.306,12** |

**Natureza:** ESTIMATIVA ESTRUTURAL CALCULADA.

O intervalo representa dois extremos mecânicos: todos os cargos na menor ou na maior referência da respectiva carreira.

### Não interpretar como

- folha observada;
- remuneração bruta real;
- remuneração líquida;
- faixa provável da folha;
- piso/teto jurídico da folha real.

O valor superior de R$ 446.306,12 **não é teto da folha TJRS/São Borja**.

## 5. Itens não cobertos pela faixa

A faixa exclui:

- posição real de cada servidor na carreira;
- vantagens pessoais;
- gratificações;
- funções gratificadas;
- cargos em comissão;
- auxílios;
- indenizações;
- parcelas eventuais;
- servidores não efetivos/cedidos/requisitados;
- magistrados.

## 6. Magistratura

Fonte:

`https://www.tjrs.jus.br/static/2026/08/2026-07-estrutura-remuneratoria-dos-membros-da-magistratura.pdf`

Referência julho/2026:

| Cargo/referência | Subsídio |
|---|---:|
| Juiz de Direito — inicial | R$ 30.505,36 |
| Juiz de Direito — intermediária | R$ 33.894,84 |
| Juiz de Direito — final | R$ 37.660,94 |
| Juiz de Direito Substituto — inicial | R$ 30.505,36 |
| Juiz de Direito Substituto — intermediária | R$ 33.894,84 |
| Juiz de Direito Substituto — final | R$ 37.660,94 |
| Pretor | R$ 28.978,00 |
| Desembargador | R$ 41.845,49 |

**Status:** estrutura unitária observada; massa local **não calculada**.

Falta a contagem canônica dos magistrados lotados/exercendo em São Borja por referência. Não multiplicar quantidade de varas por subsídio médio.

## 7. Cargos em comissão e funções de confiança

Tabela oficial localizada:

`https://www.tjrs.jus.br/static/2026/08/2026-07-estrutura-remuneratoria-dos-cargos-em-comissao-e-funcoes-de-confianca.pdf`

**Status:** estrutura estadual observada; massa local não estimada.

A TLP 1 registra quatro vínculos sem vínculo nas unidades judiciárias de São Borja no fechamento de 2025, mas isso não permite atribuir automaticamente símbolos de CC/FG.

## 8. Correção metodológica do subtotal

A base v025 de **R$ 9.551.979,21/mês** é uma ordem de grandeza documental com conceitos remuneratórios diferentes:

- federal civil parcial: remuneração básica bruta;
- Executivo estadual: remuneração bruta;
- MPRS: Total Bruto da folha NORMAL.

A DPERS adicionou envelopes próprios; o TJRS agora adiciona um envelope teórico de vencimento básico.

Por isso, as somas abaixo são apenas **SENSIBILIDADES ARITMÉTICAS NÃO CANÔNICAS**:

| Cenário | Resultado |
|---|---:|
| Base v025 + TJRS básico mínimo | R$ 9.747.745,15 |
| Base v025 + TJRS básico máximo | R$ 9.998.285,33 |
| Base + DPERS estrito recorrente + TJRS mínimo | R$ 9.814.209,59 |
| Base + DPERS estrito recorrente + TJRS máximo | R$ 10.064.749,77 |
| Base + DPERS ampliado provável + TJRS mínimo | R$ 9.823.435,58 |
| Base + DPERS ampliado provável + TJRS máximo | R$ 10.073.975,76 |

Nenhum desses números deve ser publicado como **folha pública total** ou **subtotal homogêneo**.

## 9. Estado dos demais poderes

- **MPRS:** promovido; 12 vínculos lotados; Total Bruto jul/2026 R$ 277.055,29.
- **DPERS:** envelopes estrito e ampliado promovidos com ressalvas documentais.
- **TJRS:** roster/lotações e estrutura efetiva promovidos; folha real ainda pendente.
- **TCE-RS:** sem unidade fixa local identificada; não promovido, não interpretar como zero.
- **ALRS:** presença funcional local não demonstrada; não promovido, não interpretar como zero.

## 10. Lacunas remanescentes da folha pública não municipal

1. TJRS — output estruturado da folha por lotação, magistratura local e CC/FG.
2. Forças Armadas — presença institucional observada; folha municipal ainda não territorializada.
3. PF/PRF — presença institucional observada; UORG/UF da base federal usada não permite territorialização segura.
4. DPERS — roster oficial mensal completo ainda desejável.
5. TCE-RS/ALRS — reabrir apenas diante de nova evidência funcional local.

## 11. Governança

PR #41 permanece:

- **aberto**;
- **draft**;
- **sem merge**.

Branch: `feature/cnpj-territorial-control-v1`.

Nenhuma integração à `main` está autorizada sem aprovação explícita.
