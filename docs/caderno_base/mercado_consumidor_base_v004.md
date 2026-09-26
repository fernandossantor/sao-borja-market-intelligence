# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar, de renda e benefícios v004

## Objetivo

Esta versão preserva as camadas demográfica, domiciliar, econômica, laboral e de rendimento domiciliar das versões anteriores e incorpora uma primeira camada oficial de **renda não laboral registrada pelo INSS/SUIBE** para residentes de São Borja/RS em julho de 2026.

Abrangência geográfica: São Borja/RS.  
Atualização: 2026-09-08.  
Tabela principal: aba `Mercado_consumidor_base` do Caderno-Base v008.  
Tabela de sustentação previdenciária: aba `INSS_beneficios_202607`.

## 1. Escala territorial já consolidada

Dados observados ou calculados já preservados:

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

### Dados observados

- rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**.

### Distribuição observada

| Classe | Pessoas | Percentual oficial |
|---|---:|---:|
| Até 1/4 SM | 2.441 | 4,13463% |
| >1/4 a 1/2 SM | 10.917 | 18,49148% |
| >1/2 a 1 SM | 20.174 | 34,17121% |
| >1 a 2 SM | 15.630 | 26,47447% |
| >2 a 3 SM | 4.659 | 7,89153% |
| >3 a 5 SM | 2.086 | 3,53332% |
| >5 a 10 SM | 1.237 | 2,09526% |
| >10 a 15 SM | 286 | 0,48443% |
| >15 a 20 SM | 33 | 0,05590% |
| >20 SM | 87 | 0,14736% |
| Sem rendimento | 1.488 | 2,52041% |

Agregações calculadas pelo SBMI:

- sem rendimento ou até 1 SM: **35.020 / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- mais de 2 SM: **8.388 / 14,20780%**;
- mais de 5 SM: **1.643 / 2,78295%**.

Essas agregações não são classes sociais oficiais.

## 3. Massa mensal implícita de rendimento domiciliar

Com média e denominador do mesmo universo:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Natureza: **calculado**. Referência: Censo 2022.

O resultado é massa mensal implícita no universo estatístico. Não equivale a renda disponível, consumo, faturamento do comércio ou potencial setorial.

## 4. Renda formal do trabalho — referência distinta

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial, com 7.800 valores informados e 795 ausentes.

Essa massa não é diretamente somável à massa domiciliar do Censo: os universos, períodos e conceitos são distintos. A RAIS cobre vínculos empresariais formais; o Censo mede rendimento domiciliar per capita de moradores no universo estatístico definido pelo IBGE.

## 5. Benefícios emitidos pelo INSS/SUIBE — julho de 2026

Fonte: INSS Portal de Dados Abertos / SUIBE, conjunto `Benefícios Emitidos`, recurso `Benefícios Emitidos Julho 2026`.

O recorte territorial usa **exclusivamente** o campo `municipio_residencia` e o literal oficial completo:

`19181-RS-SAO BORJA`

A auditoria identificou uma particularidade de layout: cabeçalho separado por vírgulas e registros por ponto e vírgula; `credito` usa vírgula decimal. A rotina foi corrigida antes da canonização.

### Resultados calculados a partir dos registros oficiais

- **14.247 registros** de benefícios/créditos emitidos a residentes de São Borja/RS;
- **14.247 registros com `credito` válido**;
- soma de `credito`: **R$ 24.535.168,54** em 2026-07;
- crédito médio por registro: **R$ 1.722,13**.

A contagem é de registros, **não de pessoas beneficiárias únicas**.

## 6. Composição por espécie

A nova aba `INSS_beneficios_202607` preserva as **27 espécies literais** observadas no recorte, com registros, soma de `credito` e participações calculadas.

As seis maiores espécies em valor representam a maior parte do fluxo mensal:

| Espécie literal | Registros | Crédito (R$) | % do crédito |
|---|---:|---:|---:|
| APOSENTADORIA POR IDADE | 3.787 | 6.264.831,82 | 25,53409% |
| PENSAO POR MORTE PREVIDENCIARIA | 2.642 | 4.424.751,50 | 18,03432% |
| APOSENTADORIA POR TEMPO DE CONTRIBUICAO | 1.647 | 4.145.792,27 | 16,89735% |
| APOSENTADORIA POR INCAPACIDADE PERMANENTE PREVIDENCIARIA | 1.689 | 2.923.245,53 | 11,91451% |
| AMPARO SOCIAL AO IDOSO | 1.656 | 2.447.049,37 | 9,97364% |
| AMPARO SOCIAL PESSOA PORTADORA DEFICIENCIA | 1.729 | 2.330.068,27 | 9,49685% |

## 7. Duas espécies literalmente denominadas AMPARO SOCIAL

Soma restrita às duas categorias cujo nome na fonte contém literalmente `AMPARO SOCIAL`:

- registros: `1.656 + 1.729 = 3.385`;
- crédito: `R$ 2.447.049,37 + R$ 2.330.068,27 = R$ 4.777.117,64`;
- participação nos registros: `3.385 / 14.247 × 100 = 23,75939%`;
- participação no crédito: `4.777.117,64 / 24.535.168,54 × 100 = 19,47049%`.

Natureza: **calculado**.

Esse subtotal não é chamado de total da assistência social ou de benefícios não contributivos. Há categorias legadas e outras espécies cuja classificação exigiria regra jurídica explícita.

## 8. Auditoria territorial

A fonte contém literais `SAO BORJA` associados a outras UFs. Esses registros foram preservados no diagnóstico de fonte, mas excluídos do recorte canônico de São Borja/RS. O campo `uf` dos **14.247** registros selecionados é `RIO GRANDE DO SUL` em todos os casos.

Não foi aplicada correção automática aos registros anômalos.

## 9. Interpretação mercadológica

A nova camada confirma a relevância de rendas não laborais para a economia residente. Em julho de 2026, o INSS/SUIBE registra **R$ 24,535 milhões** de créditos de benefícios emitidos a residentes de São Borja/RS.

Esse valor não deve ser comparado mecanicamente com a massa implícita de R$ 92,606 milhões do Censo 2022 nem com os R$ 23,940 milhões de remuneração RAIS de dezembro de 2025. As três grandezas têm períodos e universos diferentes.

O resultado é útil para caracterizar escala monetária e composição dos fluxos de benefícios. Ainda não demonstra quanto desse recurso é gasto em São Borja, em quais setores, por quais canais ou com qual propensão marginal a consumir.

## 10. Limitações

- registro emitido ≠ pessoa beneficiária única;
- crédito mensal ≠ renda anual;
- crédito de benefício ≠ consumo efetivo;
- total INSS/SUIBE ≠ massa previdenciária contributiva, pois o conjunto inclui espécies assistenciais, acidentárias e legadas;
- Censo 2022, RAIS 2025 e INSS 2026-07 não devem ser somados sem harmonização metodológica;
- não há evidência ainda sobre retenção local, poupança, endividamento ou alocação setorial do gasto.

## 11. Rastreabilidade

Workflow: `inss-benefits-residence-extract`.  
Run: `34282566426`.  
Artifact: `10078228209`.  
SHA-256 do artifact: `2f75523301768374ee1e9a908480ca850d93d6fe661407991ade50f9c800ba87`.  
SHA-256 do CSV municipal: `eb9e2536026d460892ea64cf672bf3cc26da1231bbf552f3ddd51d4c6945996c`.

Drive:

- pasta: `_sao_borja/raw/social/inss_suibe_beneficios_emitidos/`, ID `1gIN6tmhHg-r7lPBlpCnGHNggZCj568vO`;
- pacote: `inss_emitidos_sao_borja_rs_residencia_202607_v007_official_package.zip`, ID `11lAy2Dtlw20tzhOb8Y4ltkbpyZPDhbOs`;
- nota metodológica: `INSS_SUIBE_Sao_Borja_residencia_202607_v001`, ID `1bn5C6u1GII4eHrDwUnDRgTA27VR_YK4yL-QChWk_ncI`.

## 12. Lacuna remanescente prioritária

A principal lacuna de renda não laboral passa a ser **transferências monetárias diretamente recebidas pelas famílias** em fonte oficial. A planilha de Bolsa Família já localizada no Drive permanece classificada como **IGD transferido ao FMAS**, recurso administrativo de gestão, e continua excluída de renda domiciliar e demanda de consumo.

## 13. Próxima agenda

A etapa previdenciária mensal de julho de 2026 está encerrada como primeira referência oficial municipal. Próximos passos:

1. recuperar transferências monetárias efetivamente recebidas pelas famílias;
2. avaliar a construção de série mensal INSS/SUIBE, repetindo a mesma auditoria territorial;
3. somente depois definir uma metodologia explícita para renda disponível aproximada e capacidade de compra;
4. conectar renda, benefícios e distribuição aos quatro cadernos setoriais e à matriz de controle territorial.
