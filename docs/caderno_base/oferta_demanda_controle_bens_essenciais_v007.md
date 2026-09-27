# Oferta, demanda e controle territorial — bens essenciais — v007

Atualização: 2026-09-08. Abrangência: São Borja/RS.

## 1. Objetivo

Integrar a demanda potencial residente de alimentação no domicílio, o inventário documental da oferta, a proxy de capacidade competitiva e os indicadores agregados de controle territorial do varejo, sem fabricar market share, saturação ou retenção territorial.

## 2. Demanda

**Estimativa modelada principal:** R$ 234.706.228,14/ano e R$ 19.558.852,34/mês.

Fonte/fórmula: IBGE POF 2017-2018, tabela 1.3.23.3 do Rio Grande do Sul; população oficial estimada de São Borja em 2025, 61.311 pessoas; fator acumulado 1,781742384675 do IPCA nacional do grupo Alimentação e bebidas até jun/2026.

`61.311 × (487 / 2,72) × 1,781742384675 × 12`.

Abrangência: alimentação comprada para consumo no domicílio por residentes.

Limitação: não é faturamento observado, mercado capturado, renda disponível ou totalidade dos bens essenciais.

## 3. Oferta — qualidade do inventário

Censo da Oferta v002:

- 138 linhas brutas no inventário POM;
- 135 nomes únicos;
- 54 linhas da base corrente classificadas como bens essenciais;
- 52 registros reconciliados cadastro corrente ↔ POM;
- 19 pendências resolvidas, 32 parciais e 48 abertas.

Esses números são **cálculos documentais**, não um censo exaustivo de estabelecimentos ativos. Um mesmo nome pode representar mais de uma unidade física e a ausência de correspondência não prova inexistência operacional.

A maior incerteza não é a diferença de três registros entre linhas brutas e nomes únicos, mas o status operacional, a cobertura efetiva e o porte de cada unidade.

## 4. Capacidade competitiva — CEMPRE/SIDRA

Na classe 47.11-3 — hipermercados e supermercados — a intensidade de pessoal por empresa é maior que na classe 47.12-1 — minimercados, mercearias e armazéns — nos dois anos observados:

- 2022: razão 47.11 / 47.12 ≈ **4,73 vezes**;
- 2023: razão ≈ **1,97 vez**.

**Interpretação:** a direção de maior escala dos generalistas é sustentada.

**Limitação:** a magnitude é instável. Além disso, empresa e unidade local não são universos equivalentes no CEMPRE; pessoal por empresa não deve ser convertido automaticamente em pessoal por loja.

A antiga simulação que combina contagens POM com razões CEMPRE permanece exclusivamente como **análise de sensibilidade** e não é market share.

## 5. Controle territorial — varejo amplo

Fonte cadastral: RFB Dados Abertos CNPJ, competência 2026-08; divisão CNAE 47, que inclui varejo alimentar e não alimentar.

- 1.720 estabelecimentos;
- 114 filiais de matriz externa;
- participação cadastral externa = `114 / 1.720 × 100` = **6,627907%**.

Fonte laboral/remuneratória: RAIS 2025 × RFB 2026-08, modelo por células CNAE × natureza jurídica.

- 2.893 vínculos;
- 1.083,743584 vínculos externos estimados;
- participação externa estimada no emprego = **37,460891%**;
- remuneração de dezembro = **R$ 6.782.037,30**;
- remuneração de dezembro externa estimada = **R$ 2.588.273,00**;
- participação externa estimada na remuneração de dezembro = **38,163647%**.

Emprego e remuneração externos são estimativas agregadas do modelo, não identificação direta por estabelecimento ou operador.

## 6. Amplificação funcional externa

Emprego:

`37,460891% / 6,627907% = 5,651994 vezes`.

Remuneração de dezembro:

`38,163647% / 6,627907% ≈ 5,76 vezes`.

**Interpretação:** estruturas externas têm peso funcional muito maior que sua presença cadastral no varejo amplo.

Essas razões **não são** market share, participação em faturamento, remessa de lucros, retenção/vazamento territorial ou parcela da demanda alimentar capturada por redes externas.

## 7. Diagnóstico integrado

**Fato:** o benchmark modelado de demanda alimentar residente é de aproximadamente R$ 234,7 milhões/ano.

**Fato:** a oferta documentada combina grandes formatos generalistas, mercados/minimercados e varejo alimentar especializado, mas o inventário não é censo completo de lojas ativas.

**Calculado:** os generalistas 47.11 mostram maior intensidade de pessoal por empresa que 47.12 nos dois anos comparados, com magnitude variável.

**Observado + estimado:** na divisão 47, estruturas externas representam 6,63% da presença cadastral, porém aproximadamente 37,46% do emprego e 38,16% da remuneração de dezembro no modelo.

**Interpretação:** a estrutura competitiva é **assimétrica**. Poucos operadores generalistas de maior escala coexistem com uma rede numerosa de vizinhança e especializados; ao mesmo tempo, redes externas têm peso funcional desproporcional no varejo amplo. Isso torna o controle territorial uma dimensão relevante da concorrência, mas não demonstra participação nas vendas.

## 8. Indicadores bloqueados

Nesta etapa, não calcular:

- market share por operador ou formato;
- faturamento médio dividindo R$ 234,7 milhões pelo número de lojas;
- saturação da oferta baseada apenas em contagem de estabelecimentos;
- retenção ou vazamento territorial com base na localização da matriz;
- participação das redes externas na demanda alimentar aplicando diretamente os percentuais da divisão 47.

Faltam principalmente vendas por operador ou proxy validada, porte por unidade, situação cadastral/operacional consolidada e destino/origem do gasto — inclusive outros municípios, Argentina e comércio eletrônico.

## 9. Matriz pré-join RFB

Foi construída a matriz `matriz_operadores_bens_essenciais_prejoin_rfb_v001_20260908.xlsx` para as 54 linhas correntes de bens essenciais.

**Dados calculados:**

- CNPJ documental OK: **47/54**, ou **87,03704%**;
- CNPJ em revisão por duplicidade: **2**;
- sem CNPJ: **5**;
- MATCH_POM: **52**;
- ONLY_CURRENT: **2**.

O CNPJ base — primeiros oito dígitos — é usado apenas como identificador de agrupamento, nunca como regra territorial. Duas bases com CNPJ OK aparecem em mais de uma unidade do recorte: Rede Vivo e Peruzzo, duas unidades mapeadas cada. Esse cálculo não representa o total de unidades das redes e não determina matriz/filial.

**Controle metodológico:** `controle_local_externo` e `municipio_matriz` permanecem `PENDENTE_RFB_OFICIAL`. Nenhum operador é classificado por terminação `/0001`, endereço, telefone, razão social ou narrativa documental.

**Interpretação:** aproximadamente 87% das linhas correntes já estão tecnicamente prontas para um join exato com a RFB 2026-08. Essa taxa mede prontidão da base atual, **não cobertura da oferta municipal**.

## 10. Próxima prioridade

Executar o join exato dos 47 CNPJs prontos com a RFB 2026-08 e resolver os sete registros ainda sem CNPJ validado, completando:

`operador × formato × CNPJ/unidade × situação cadastral × CNAE × matriz/filial × município da matriz × controle local/externo × proxy de porte × confiança da reconciliação`.

A classificação local/externa deve usar exclusivamente os campos oficiais da RFB. Só depois será defensável testar concentração por operadores, pressão competitiva e hipóteses de retenção territorial. Market share continuará exigindo vendas ou proxy explicitamente validada.

## 11. Rastreabilidade

- Caderno-Base v011: Drive `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`;
- demanda v005: Drive `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- Censo da Oferta v002: Drive `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- proxy capacidade/oferta v007: Drive `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- matriz pré-join RFB v001: Drive `1fSZO0sEqeoGuWgNacZvjQGcN2pdPWYki`;
- nota nativa no Drive: `Oferta, demanda e controle territorial — bens essenciais — v007 — 20260908`, ID `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- diagnóstico integrado nativo v008: Drive `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`.
