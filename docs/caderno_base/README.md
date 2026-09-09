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

- Caderno corrente: `caderno_base_territorial_v010_demanda_bens_essenciais_20260908` — Drive ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.
- Versão histórica anterior: `caderno_base_territorial_v009_mercado_consumidor_renda_transferencias_20260908` — Drive ID `15NzQK7LimFA56jJ60pPL0pmpS75FvUxIMPhWH6LkuzM`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v009.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v008.md`.
- Mercado consumidor: `docs/caderno_base/mercado_consumidor_base_v006.md`.
- Demanda de bens essenciais: `docs/caderno_base/demanda_potencial_bens_essenciais_v005.md`.
- Matriz de fluxos de renda/transferências: `docs/caderno_base/matriz_fluxos_renda_transferencias_v001.md`.
- Nota Novo Bolsa Família — série: `docs/caderno_base/novo_bolsa_familia_sao_borja_serie_2026_01_07_v002.md`.
- Nota INSS/SUIBE: `docs/caderno_base/inss_beneficios_residentes_202607_v001.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.

Documentação nativa no Drive:

- diagnóstico integrado corrente: `Caderno-Base — diagnóstico analítico integrado v007 — 20260908`, ID `1xmPKHpSGqeafoN3_T7cP_kLbryiGWI-0i8j4FcMxkv4`;
- demanda de bens essenciais: `Demanda potencial de bens essenciais — São Borja — v005 — 20260908`, ID `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`;
- matriz monetária: `Matriz de fluxos de renda e transferências — v001 — 20260908`, ID `1E4TghI46on_azi360vKFt7SAl65SA-hjbec6jRm4RY4`;
- nota Novo Bolsa Família: `Novo_Bolsa_Familia_Sao_Borja_serie_2026_01_07_v002`, ID `1okus0U8IMDtzHjGZHtpESLsxtTPY2L4kUNLrz-_Sobs`.

A v010 preserva as abas anteriores e acrescenta `Bens_essenciais_demanda` e `POF_RS_classes`.

## Estado das bases principais

### Controle empresarial

- RFB Dados Abertos CNPJ, competência 2026-08;
- 6.906 estabelecimentos empresariais no universo analítico;
- 284 de matriz externa;
- participação externa cadastral: **4,1124%**.

### Emprego e remuneração

- RAIS 2025 × RFB 2026-08;
- 8.595 vínculos empresariais;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na soma das remunerações médias: **29,0903%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- auditoria: 7/7 controles PASS, 0 vínculos unmatched.

### IPM definitivo

- Receita Estadual/RS — `DAIM545X`;
- série 2003–2026, 24/24 anos;
- 2025: 0,527880;
- 2026: 0,533647;
- variação 2026/2025: **+1,092483%**.

### VAF — Valor Adicionado Municípios

- Receita Estadual/SEFAZ-RS;
- São Borja/RS, prefixo 117;
- cobertura 1994–2025, **32/32 rótulos anuais**;
- 2024: R$ 2.907.302.928,34;
- 2025: R$ 2.325.966.620,93;
- variação nominal 2025/2024: **-19,9957%**;
- benchmark Sebrae 2009–2019 ↔ SEFAZ 2007–2017: **11/11 correspondências**;
- alinhamento exploratório VAF `t` → IPM `t+2`: 15/23 sinais concordantes e 8/23 divergentes, sem inferência causal.

## Mercado consumidor — base integrada

### Escala e renda domiciliar

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**.

Massa mensal implícita:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`.

Essa massa é calculada e não equivale a renda disponível, consumo efetivo, faturamento ou potencial setorial.

### Benefícios INSS/SUIBE — julho de 2026

- 14.247 registros emitidos;
- crédito total: **R$ 24.535.168,54**;
- crédito médio: **R$ 1.722,13**.

Registro não equivale a pessoa única.

### Novo Bolsa Família — janeiro–julho de 2026

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo corrente: **R$ 10.514.491,00**;
- ajustes retroativos: **R$ 89.800,00 / 0,84683%**;
- média mensal corrente: **R$ 1.502.070,14**;
- variação jan→jul: **-0,28973%**;
- CV mensal: **0,70509%**.

Cobertura oficial identificada: **2023-03 a 2026-07, 41 competências consecutivas**. Disponibilidade do ZIP não garante comparabilidade automática de esquema.

As camadas Censo, RAIS, INSS e Novo Bolsa Família **não são somadas diretamente**.

## Demanda de bens essenciais — modelo v005

### Fonte principal

IBGE — POF 2017-2018 — tabelas por Unidade da Federação, Rio Grande do Sul, tabela `1.3.23.3`.

Dados observados no total estadual:

- alimentação total: **R$ 736,69/família/mês**;
- alimentação no domicílio: **R$ 487,00/família/mês**;
- fora do domicílio: **R$ 249,69/família/mês**;
- tamanho médio familiar: **2,72 pessoas**.

Cálculo per capita:

`R$ 487,00 / 2,72 = R$ 179,04412/pessoa/mês`.

Atualização monetária preservada no modelo: fator **1,781742384675** do IPCA nacional do grupo Alimentação e bebidas até junho de 2026.

Benchmark atualizado: aproximadamente **R$ 319,01/pessoa/mês**.

### Cenário principal

População oficial estimada 2025: **61.311 pessoas**.

- demanda mensal modelada: **R$ 19.558.852,34**;
- demanda anual modelada: **R$ 234.706.228,14**.

Natureza: **ESTIMATIVA MODELADA** do núcleo alimentar comprado para consumo no domicílio. Não é faturamento observado nem mercado capturado.

### Comparadores

- RS/2025: **R$ 234.706.228,14/ano**;
- Região Sul/2025: **R$ 223.342.012,82/ano**;
- Brasil/2025: **R$ 193.255.019,83/ano**.

RS versus Sul: **+5,08826%**. Essa diferença decorre da referência geográfica e **não é crescimento observado do mercado**.

### Classes POF e renda local

Na POF RS, alimentação no domicílio varia de **R$ 248,57/família/mês** na menor classe a **R$ 1.253,49** na maior; o gasto per capita calculado varia de aproximadamente **R$ 120,67 a R$ 449,28**.

A participação do gasto alimentar realizada no domicílio é **66,11%** no total estadual e **78,94%** na menor classe.

A v005 **não aplica calibração por renda municipal**: a POF usa rendimento total + variação patrimonial familiar; o Censo municipal consolidado usa rendimento domiciliar per capita. Não se cria equivalência artificial entre as classificações.

### Rastreabilidade POF

- workflow `pof-rs-food-source-discovery`;
- run `34293228168`;
- artifact `10082136959`;
- pacote oficial: 1.409.382 bytes;
- SHA-256: `7be3b0c5852d02ee886cf59265d0301278ff36d3d53445cab63ba7a25b525048`;
- `43RS.xls.xlsx`: 58.216 bytes;
- SHA-256: `a32c3201cc201d669c65d3f46f50033bdad2e810d603a41d3731ffe64976d975`.

Drive:

- fonte raw: ID `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- derivado POF RS: ID `11xTjsR4AkTALlySBBomX4N20REIvG95ucKF3gjyRsfA`;
- modelo demanda v005: ID `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`.

## Leitura integrada oferta × demanda

- o varejo é o principal nó externo em peso absoluto;
- o mercado residente apresenta concentração numérica nas faixas inferiores de rendimento;
- benefícios e transferências representam fluxos monetários recorrentes;
- o núcleo alimentar no domicílio tem benchmark modelado de aproximadamente **R$ 234,7 milhões/ano**.

**Interpretação/hipótese:** o próximo problema mercadológico é compreender como essa demanda se distribui entre formatos, empresas, canais e territórios. Ainda não há dado para repartir o mercado entre firmas locais e redes externas, medir retenção territorial ou inferir vazamento monetário.

## Próxima agenda

1. investigar destino e canais do gasto alimentar;
2. estimar atração/evasão de compras, incluindo Argentina, outros municípios e comércio eletrônico;
3. construir proxy de capacidade/porte da oferta por formato e operador;
4. avançar, somente com dados compatíveis, para retenção territorial e pressão competitiva;
5. manter a hipótese de sensibilidade dos bens essenciais a fluxos recorrentes de renda/transferências como hipótese a testar;
6. continuar séries de renda/transferências quando agregarem valor à interpretação do comportamento.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
