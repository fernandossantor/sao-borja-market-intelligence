# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar, de renda e transferências v006

## Objetivo

Preservar as camadas demográfica, domiciliar, econômica, laboral, de rendimento domiciliar, INSS/SUIBE e Novo Bolsa Família já consolidadas e avançar da referência pontual de julho para uma **série mensal janeiro–julho de 2026** do Novo Bolsa Família.

Abrangência geográfica: São Borja/RS.  
Atualização: 2026-09-08.  
Caderno corrente: v009.  
Tabela principal: aba `Mercado_consumidor_base`.  
Tabelas de sustentação: `INSS_beneficios_202607`, `Novo_Bolsa_Familia_202607`, `NBF_serie_2026` e `NBF_cobertura`.

## 1. Escala territorial

Dados observados:

- população Censo 2022: **59.676 pessoas** — IBGE/SIDRA;
- população estimada 2025: **61.311 pessoas** — IBGE;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**;
- PIB 2023: **R$ 2.550.388.000**;
- PIB per capita 2023: **R$ 42.737,25**.

PIB não equivale a renda domiciliar; composição domiciliar não demonstra comportamento de compra.

## 2. Rendimento domiciliar per capita — Censo 2022

Fonte: IBGE/SIDRA, tabelas 10295 e 10296.

Dados observados:

- média nominal mensal per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível: **59.038 moradores**.

Agregações calculadas pelo SBMI:

- sem rendimento ou até 1 SM: **35.020 / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- mais de 2 SM: **8.388 / 14,20780%**;
- mais de 5 SM: **1.643 / 2,78295%**.

Essas agregações não são classes sociais oficiais.

## 3. Massa mensal implícita de rendimento domiciliar

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Natureza: **calculado**. Referência: Censo 2022.

Não equivale a renda disponível, consumo efetivo, faturamento comercial ou potencial setorial.

## 4. Renda formal do trabalho

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial.

Essa grandeza não é diretamente somável à massa domiciliar do Censo: os universos, períodos e conceitos são distintos.

## 5. Benefícios emitidos pelo INSS/SUIBE — julho de 2026

Fonte: INSS Portal de Dados Abertos / SUIBE.

Recorte: `municipio_residencia = 19181-RS-SAO BORJA`.

Resultados calculados:

- **14.247 registros**;
- soma de `credito`: **R$ 24.535.168,54**;
- crédito médio: **R$ 1.722,13 por registro**.

A contagem é de registros, não pessoas únicas. As duas espécies literalmente denominadas `AMPARO SOCIAL` somam **R$ 4.777.117,64**, ou **19,47049%** do crédito total, sem que isso seja relabelado como toda a assistência social.

## 6. Novo Bolsa Família — série janeiro–julho de 2026

Fonte: Portal da Transparência / CGU — Dados Abertos — Novo Bolsa Família.

Filtro territorial:

- `UF = RS`;
- `NOME MUNICÍPIO` normalizado = `SAO BORJA`;
- SIAFI observado `8863`.

Controle de privacidade: CPF, NIS e nomes foram processados apenas transitoriamente; nenhuma informação individual foi persistida.

### Resultados calculados

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo cuja referência coincide com a competência: **R$ 10.514.491,00**;
- ajustes de referências anteriores: **R$ 89.800,00**;
- participação dos ajustes anteriores: **0,84683%**;
- média mensal do fluxo total: **R$ 1.514.898,71**;
- média mensal do fluxo corrente: **R$ 1.502.070,14**.

### Variação janeiro→julho

- fluxo total: **-3,06906%**;
- fluxo corrente: **-0,28973%**;
- registros de referência corrente: **-1,39013%**;
- média por registro corrente: **+1,11650%**.

Coeficiente de variação mensal do fluxo corrente: **0,70509%**.

## 7. Competência e referência

O total de uma competência pode incluir parcelas referentes a meses anteriores. Ajustes retroativos como proporção do valor total:

- jan: 2,78741%;
- fev: 0,29716%;
- mar: 2,00992%;
- abr: 0,69774%;
- mai: 0,04012%;
- jun: 0%;
- jul: 0%.

Não foram observadas referências futuras nas sete competências.

**Interpretação metodológica:** o fluxo de referência corrente é mais adequado para comparação mensal do que o total bruto da competência, pois reduz o efeito de acertos retroativos.

## 8. Cobertura oficial disponível

Foram identificados **41 endpoints ZIP mensais consecutivos entre 2023-03 e 2026-07**.

Natureza: disponibilidade observada na fonte oficial.

Limitação: disponibilidade não assegura comparabilidade automática de esquema. A expansão histórica exigirá validação competência a competência quando houver mudança estrutural.

## 9. Leitura mercadológica

No intervalo janeiro–julho de 2026, o fluxo corrente do Novo Bolsa Família permaneceu aproximadamente entre **R$ 1,49 milhão e R$ 1,52 milhão por mês**.

**Interpretação:** a transferência aparece como fluxo recorrente e de baixa dispersão no período observado, devendo integrar a caracterização das fontes de renda não laboral do mercado residente.

Não se conclui:

- quanto foi gasto em São Borja;
- quais setores absorveram o recurso;
- qual a propensão a consumir dos favorecidos;
- qual a sobreposição com renda do trabalho ou INSS/SUIBE;
- qual a renda total corrente dos residentes.

## 10. Referências monetárias e regra de não soma

O Caderno trabalha com grandezas distintas:

- **R$ 92.605.826,04/mês** — massa implícita de rendimento domiciliar, Censo 2022;
- **R$ 23.940.059,71** — remuneração nominal de dezembro, RAIS 2025;
- **R$ 24.535.168,54** — benefícios/créditos INSS/SUIBE, julho de 2026;
- **R$ 1.502.070,14/mês** — média do fluxo corrente do Novo Bolsa Família, jan–jul 2026.

Essas grandezas **não devem ser somadas mecanicamente**. Há diferenças de universo, período, conceito e possível sobreposição de pessoas.

## 11. Implicações para os quatro cadernos setoriais

As camadas de renda e transferência devem funcionar como **base de escala e segmentação**, não como multiplicadores automáticos de consumo.

Hipóteses sobre comércio de bens essenciais, saúde/higiene, bens não essenciais e serviços/alimentação precisam ser testadas com dados de hábitos de compra, comportamento, pesquisa primária ou outras fontes específicas.

## 12. Rastreabilidade

Novo Bolsa Família — série v002:

- workflow `novo-bolsa-familia-series-2026`;
- run `34288591742`;
- artifact `10080614700`;
- SHA-256 `68e0548f2daeed4c5d8ad5a2800a3a07f94fb26f84f3e678d41f84cf54974a70`.

Drive:

- pacote v002: ID `1BzTJVG1nTUKF-vl4riX3dPSdZF1ZEJa7`;
- CSV analítico v002: ID `1nD5kpXmKDrjDuWbITB7CAGUtUDQx1sSt`;
- cobertura v002: ID `1XFmz-fQlH64eQ0fGaOhXlj9AhUMeKENN`;
- nota nativa v002: ID `1okus0U8IMDtzHjGZHtpESLsxtTPY2L4kUNLrz-_Sobs`.

Caderno corrente: `caderno_base_territorial_v009_mercado_consumidor_renda_transferencias_20260908`, ID `15NzQK7LimFA56jJ60pPL0pmpS75FvUxIMPhWH6LkuzM`.

## 13. Próxima agenda

1. estender a série Novo Bolsa Família para 2023-03 em diante, validando mudanças de esquema;
2. mapear outras transferências monetárias diretamente recebidas por residentes/famílias;
3. avaliar série mensal INSS/SUIBE;
4. depois estruturar metodologia explícita para renda disponível aproximada, capacidade de compra, retenção local e alocação setorial do gasto;
5. conectar as fontes de renda/transferência à matriz de controle territorial e aos quatro cadernos setoriais.