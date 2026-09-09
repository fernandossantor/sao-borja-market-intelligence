# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa que altere dados, indicadores, método, interpretação ou diagnóstico do Caderno-Base deve atualizar no mesmo ciclo, quando aplicável:

1. derivados auditáveis e sua promoção ao Google Drive;
2. manifestos, metadados, validações e hashes;
3. narrativa analítica em `docs/caderno_base/`;
4. versão corrente da planilha do Caderno-Base no Drive;
5. descrição do PR/branch, separando observado, calculado, estimado, hipótese, interpretação e recomendação.

Versões anteriores permanecem preservadas para auditoria histórica.

## Versão corrente

- Caderno corrente: `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908` — Drive ID `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.
- Versão histórica anterior: `caderno_base_territorial_v010_demanda_bens_essenciais_20260908` — Drive ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v010.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v009.md`.
- Oferta × demanda × controle: `docs/caderno_base/oferta_demanda_controle_bens_essenciais_v007.md`.
- Demanda de bens essenciais: `docs/caderno_base/demanda_potencial_bens_essenciais_v005.md`.
- Mercado consumidor: `docs/caderno_base/mercado_consumidor_base_v006.md`.
- Matriz de fluxos de renda: `docs/caderno_base/matriz_fluxos_renda_transferencias_v001.md`.
- Novo Bolsa Família — série: `docs/caderno_base/novo_bolsa_familia_sao_borja_serie_2026_01_07_v002.md`.
- INSS/SUIBE: `docs/caderno_base/inss_beneficios_residentes_202607_v001.md`.
- VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz territorial setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.

Documentação nativa no Drive:

- diagnóstico integrado corrente: `Caderno-Base — diagnóstico analítico integrado v008 — 20260908`, ID `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`;
- oferta, demanda e controle: `Oferta, demanda e controle territorial — bens essenciais — v007 — 20260908`, ID `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- demanda de bens essenciais: `Demanda potencial de bens essenciais — São Borja — v005 — 20260908`, ID `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`;
- matriz monetária: ID `1E4TghI46on_azi360vKFt7SAl65SA-hjbec6jRm4RY4`.

A v011 preserva todas as abas da v010 e acrescenta `Oferta_demanda_controle` e `Qualidade_oferta`.

## Estado das bases principais

### Controle empresarial

RFB Dados Abertos CNPJ, competência 2026-08:

- 6.906 estabelecimentos empresariais no universo analítico;
- 284 de matriz externa;
- participação externa cadastral: **4,1124%**.

### Emprego e remuneração

RAIS 2025 × RFB 2026-08:

- 8.595 vínculos empresariais;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na soma das remunerações médias: **29,0903%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- auditoria: 7/7 controles PASS, 0 vínculos unmatched.

### Fiscalidade

IPM definitivo — Receita Estadual/RS:

- série 2003–2026, 24/24 anos;
- 2025: 0,527880;
- 2026: 0,533647;
- 2026/2025: **+1,092483%**.

VAF oficial — SEFAZ-RS:

- 1994–2025, 32/32 rótulos anuais;
- 2024: R$ 2.907.302.928,34;
- 2025: R$ 2.325.966.620,93;
- variação nominal: **-19,9957%**;
- Sebrae ↔ SEFAZ: 11/11 correspondências no deslocamento empírico de dois anos;
- VAF `t` → IPM `t+2`: 15/23 sinais concordantes e 8/23 divergentes; análise exploratória, não causal.

## Mercado consumidor — escala, renda e transferências

- população Censo 2022: **59.676**;
- população estimada 2025: **61.311**;
- domicílios unipessoais: **4.815 / 21,31%**;
- rendimento domiciliar per capita médio: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível: **59.038 moradores**;
- sem rendimento ou até 2 SM per capita: **50.650 / 85,79220%**;
- massa mensal implícita: **R$ 92.605.826,04/mês**, calculada e não equivalente a renda disponível ou consumo.

INSS/SUIBE, jul/2026:

- 14.247 registros;
- crédito total: **R$ 24.535.168,54**.

Novo Bolsa Família, jan–jul/2026:

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo corrente: **R$ 10.514.491,00**;
- média mensal corrente: **R$ 1.502.070,14**;
- variação jan→jul: **-0,28973%**;
- CV mensal: **0,70509%**.

As camadas Censo, RAIS, INSS e Novo Bolsa Família **não são somadas diretamente**.

## Demanda de bens essenciais — modelo v005

Fonte principal: IBGE POF 2017-2018, Rio Grande do Sul, tabela `1.3.23.3`.

- alimentação no domicílio: **R$ 487,00/família/mês**;
- tamanho médio familiar: **2,72 pessoas**;
- gasto per capita calculado: **R$ 179,04412/mês** na base POF;
- fator de preços até jun/2026: **1,781742384675**;
- benchmark atualizado: **≈R$ 319,01/pessoa/mês**.

Com população oficial estimada 2025:

- **R$ 19.558.852,34/mês**;
- **R$ 234.706.228,14/ano**.

Natureza: **ESTIMATIVA MODELADA** de alimentação comprada para consumo no domicílio. Não é faturamento observado ou mercado capturado.

O benchmark RS é **+5,08826%** superior ao comparador Região Sul no mesmo cenário; diferença geográfica, não crescimento temporal.

A v005 não calibra a demanda por renda municipal porque POF e Censo usam conceitos/classes de renda diferentes.

## Oferta × demanda × controle — estágio v007/v011

### Qualidade do inventário

Censo da Oferta v002:

- 138 linhas brutas POM;
- 135 nomes únicos;
- 54 linhas correntes classificadas como bens essenciais;
- 52 reconciliadas cadastro corrente ↔ POM;
- 19 pendências resolvidas, 32 parciais e 48 abertas.

Esses números permitem **leitura estrutural**, não censo exato de lojas ativas. Não usar 138 ou 135 como denominador de market share/saturação.

### Capacidade por formato

IBGE CEMPRE/SIDRA:

- intensidade 47.11-3 / 47.12-1 em 2022: **≈4,73x**;
- em 2023: **≈1,97x**.

A direção de maior escala dos hiper/supermercados é sustentada, mas a magnitude é instável. Empresa ≠ unidade local.

### Controle territorial no varejo amplo — divisão 47

RFB 2026-08:

- 1.720 estabelecimentos;
- 114 filiais de matriz externa;
- participação cadastral externa: **6,627907%**.

RAIS 2025 × RFB:

- 2.893 vínculos;
- participação externa estimada no emprego: **37,460891%**;
- remuneração de dezembro: R$ 6.782.037,30;
- remuneração externa estimada: R$ 2.588.273,00;
- participação externa estimada na remuneração: **38,163647%**.

Amplificação funcional:

- emprego/cadastro externo: **5,651994x**;
- remuneração/cadastro externo: **≈5,76x**.

Essas razões se referem ao varejo amplo e **não são market share, vazamento ou retenção territorial**.

### Diagnóstico

**Interpretação:** a estrutura competitiva é assimétrica: poucos generalistas de maior escala coexistem com rede numerosa de vizinhança/especializados; paralelamente, estruturas externas possuem peso funcional muito superior à presença cadastral no varejo amplo.

Ainda não existe base para repartir os **R$ 234,7 milhões/ano** entre firmas locais e redes externas.

## Indicadores bloqueados

Não calcular nesta etapa:

- market share por operador/formato;
- faturamento médio dividindo a demanda pelo número de lojas;
- saturação baseada em contagem bruta;
- parcela da demanda capturada por redes externas aplicando diretamente o percentual G47;
- retenção/vazamento territorial a partir da localização da matriz.

## Próxima prioridade

Construir para o universo reconciliado:

`operador × formato × CNPJ/unidade × situação cadastral × CNAE × matriz/filial × município da matriz × controle local/externo × proxy de porte × confiança`.

A classificação local/externa deve usar exclusivamente os campos oficiais da RFB. Depois dessa matriz, avançar para comportamento e destino do gasto — formato, operador, canal e território, incluindo Argentina, outros municípios e comércio eletrônico.

## Rastreabilidade da etapa

- fonte POF raw: Drive `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- derivado POF RS: `11xTjsR4AkTALlySBBomX4N20REIvG95ucKF3gjyRsfA`;
- demanda v005: `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- Censo da Oferta v002: `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- proxy oferta/capacidade v007: `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- Caderno v011: `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
