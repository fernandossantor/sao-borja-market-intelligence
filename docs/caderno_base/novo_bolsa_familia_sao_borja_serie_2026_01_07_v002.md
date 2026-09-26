# Novo Bolsa Família — São Borja/RS — série mensal janeiro–julho de 2026 v002

## 1. Objetivo

Consolidar uma série mensal auditável do Novo Bolsa Família para São Borja/RS, distinguindo **mês de competência** de **mês de referência**, mantendo controle de privacidade e separando benefício monetário direto de repasses administrativos como IGD/FMAS.

## 2. Fonte, período, unidade e abrangência

- **Fonte:** Portal da Transparência do Governo Federal / Controladoria-Geral da União — Dados Abertos — Novo Bolsa Família.
- **Página oficial:** `https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia`.
- **Padrão de download:** `/download-de-dados/novo-bolsa-familia/YYYYMM`.
- **Período processado nesta versão:** 2026-01 a 2026-07.
- **Abrangência:** São Borja/RS.
- **Filtro territorial:** `UF = RS` e `NOME MUNICÍPIO` normalizado = `SAO BORJA`.
- **Código Município SIAFI observado:** `8863`.
- **Campo monetário:** `VALOR PARCELA`.
- **Unidade:** reais correntes.

Os arquivos nacionais foram processados transitoriamente. Nenhum CPF, NIS ou nome individual foi persistido em GitHub, artifacts finais, Drive ou Caderno-Base.

## 3. Cobertura oficial disponível

Auditoria específica de disponibilidade identificou **41 endpoints ZIP mensais consecutivos entre 2023-03 e 2026-07**.

Natureza: **observado** quanto à disponibilidade do endpoint oficial.

Limitação: a existência do ZIP não garante comparabilidade integral de layout, esquema ou regra entre competências. A extensão histórica deverá validar cada mudança metodológica observada.

## 4. Método

Para cada competência de 2026-01 a 2026-07:

1. baixar transitoriamente o ZIP oficial;
2. validar integridade do download e formato ZIP;
3. identificar o esquema efetivamente observado;
4. filtrar `UF = RS` e município normalizado `SAO BORJA`;
5. validar o SIAFI `8863`;
6. exigir `MÊS COMPETÊNCIA` igual ao rótulo do arquivo;
7. somar `VALOR PARCELA`;
8. decompor o fluxo segundo `MÊS REFERÊNCIA`: corrente, anterior e futura;
9. manter apenas agregados, manifestos, esquemas e validações.

A decomposição é necessária porque um arquivo de competência pode conter parcelas com referência a meses anteriores.

## 5. Série observada e calculada

| Competência | Registros total | Valor total (R$) | Registros referência corrente | Valor referência corrente (R$) | Ajustes anteriores (R$) | % ajustes anteriores |
|---|---:|---:|---:|---:|---:|---:|
| 2026-01 | 2.341 | 1.561.487,00 | 2.230 | 1.517.962,00 | 43.525,00 | 2,78741% |
| 2026-02 | 2.230 | 1.514.338,00 | 2.218 | 1.509.838,00 | 4.500,00 | 0,29716% |
| 2026-03 | 2.241 | 1.526.179,00 | 2.195 | 1.495.504,00 | 30.675,00 | 2,00992% |
| 2026-04 | 2.202 | 1.504.863,00 | 2.190 | 1.494.363,00 | 10.500,00 | 0,69774% |
| 2026-05 | 2.191 | 1.495.366,00 | 2.190 | 1.494.766,00 | 600,00 | 0,04012% |
| 2026-06 | 2.174 | 1.488.494,00 | 2.174 | 1.488.494,00 | 0,00 | 0,00000% |
| 2026-07 | 2.199 | 1.513.564,00 | 2.199 | 1.513.564,00 | 0,00 | 0,00000% |

Não foram observadas referências futuras nas sete competências.

## 6. Indicadores calculados

Fórmulas preservadas no Caderno-Base v009, aba `NBF_serie_2026`:

- fluxo total jan–jul: `SUM(valor_competencia_total)` = **R$ 10.604.291,00**;
- fluxo de referência corrente: `SUM(valor_referencia_corrente)` = **R$ 10.514.491,00**;
- ajustes de referências anteriores: **R$ 89.800,00**;
- participação dos ajustes anteriores: `89.800 / 10.604.291 × 100` = **0,84683%**;
- média mensal do fluxo total: **R$ 1.514.898,71**;
- média mensal da referência corrente: **R$ 1.502.070,14**;
- variação jan→jul do fluxo total: **-3,06906%**;
- variação jan→jul da referência corrente: **-0,28973%**;
- variação jan→jul dos registros de referência corrente: **-1,39013%**;
- variação jan→jul da média por registro corrente: **+1,11650%**, de R$ 680,70 para R$ 688,30;
- coeficiente de variação populacional mensal da referência corrente: **0,70509%**.

## 7. Interpretação

**Interpretação:** entre janeiro e julho de 2026, o fluxo de referência corrente permaneceu aproximadamente entre **R$ 1,49 milhão e R$ 1,52 milhão por mês**, com baixa dispersão no intervalo observado.

Isso acrescenta evidência de **recorrência** da transferência monetária para a economia residente, mas não demonstra estabilidade futura, sazonalidade estrutural, renda disponível líquida, consumo efetivo, faturamento local ou retenção territorial.

A separação entre competência e referência evita interpretar como crescimento corrente valores que são, em parte, acertos retroativos.

## 8. Limitações

- registro/parcela ≠ família ou pessoa única;
- valor registrado ≠ consumo observado;
- transferência monetária ≠ valor necessariamente gasto em São Borja;
- sete meses são insuficientes para inferência robusta de sazonalidade;
- não há harmonização individual com INSS/SUIBE, RAIS ou Censo;
- não se deve somar mecanicamente as massas monetárias de Censo 2022, RAIS 2025, INSS 2026-07 e Novo Bolsa Família 2026 sem metodologia explícita de universos e sobreposição.

## 9. Rastreabilidade e preservação

- workflow: `novo-bolsa-familia-series-2026`;
- run: `34288591742`;
- artifact: `10080614700`;
- SHA-256 do artifact: `68e0548f2daeed4c5d8ad5a2800a3a07f94fb26f84f3e678d41f84cf54974a70`.

Google Drive:

- pacote série v002: ID `1BzTJVG1nTUKF-vl4riX3dPSdZF1ZEJa7`;
- CSV analítico v002: ID `1nD5kpXmKDrjDuWbITB7CAGUtUDQx1sSt`;
- auditoria de cobertura v002: ID `1XFmz-fQlH64eQ0fGaOhXlj9AhUMeKENN`;
- nota metodológica nativa v002: ID `1okus0U8IMDtzHjGZHtpESLsxtTPY2L4kUNLrz-_Sobs`.

## 10. Incorporação ao Caderno-Base

Caderno corrente: `caderno_base_territorial_v009_mercado_consumidor_renda_transferencias_20260908`, Drive ID `15NzQK7LimFA56jJ60pPL0pmpS75FvUxIMPhWH6LkuzM`.

Abas específicas:

- `NBF_serie_2026` — série mensal, decomposição competência/referência e fórmulas;
- `NBF_cobertura` — disponibilidade oficial 2023-03 a 2026-07;
- `Novo_Bolsa_Familia_202607` — referência pontual auditada preservada.

## 11. Próxima agenda

Estender a série para as competências oficiais anteriores já identificadas desde 2023-03, validando mudanças de esquema antes de produzir indicadores longitudinais, médias móveis ou sazonalidade.