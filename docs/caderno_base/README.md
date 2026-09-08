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

- Caderno corrente: `caderno_base_territorial_v009_mercado_consumidor_renda_transferencias_20260908` — Drive ID `15NzQK7LimFA56jJ60pPL0pmpS75FvUxIMPhWH6LkuzM`.
- Versão histórica anterior: `caderno_base_territorial_v008_diagnostico_integrado_20260907` — Drive ID `1NJp_tmQ36NE8YDA2JhmyqjsnB1a7V9ivtAFJW7YLhcU`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v007.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v006.md`.
- Mercado consumidor corrente: `docs/caderno_base/mercado_consumidor_base_v006.md`.
- Mercado consumidor anterior: `docs/caderno_base/mercado_consumidor_base_v005.md`.
- Nota Novo Bolsa Família — série: `docs/caderno_base/novo_bolsa_familia_sao_borja_serie_2026_01_07_v002.md`.
- Nota Novo Bolsa Família — referência julho: `docs/caderno_base/novo_bolsa_familia_sao_borja_202607_v001.md`.
- Nota INSS/SUIBE: `docs/caderno_base/inss_beneficios_residentes_202607_v001.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.
- Documento analítico nativo corrente no Drive: `Caderno-Base — diagnóstico analítico integrado v005 — 20260908` — ID `1QTQGuhnXXcniW4-eJhgH-27e8kv_3gvEFzVoywNy2Gg`.
- Nota nativa corrente do Novo Bolsa Família: `Novo_Bolsa_Familia_Sao_Borja_serie_2026_01_07_v002` — ID `1okus0U8IMDtzHjGZHtpESLsxtTPY2L4kUNLrz-_Sobs`.

A v009 preserva as abas anteriores e acrescenta `NBF_serie_2026` e `NBF_cobertura`, mantendo `Novo_Bolsa_Familia_202607` como referência pontual auditada.

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
- PIB 2023: **R$ 2.550.388.000**;
- PIB per capita 2023: **R$ 42.737,25**;
- rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**, agregação calculada pelo SBMI.

Massa mensal implícita no universo estatístico:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`.

Essa massa não é renda disponível, consumo efetivo, faturamento comercial ou potencial setorial.

### Benefícios emitidos pelo INSS/SUIBE — julho de 2026

- recorte: `municipio_residencia = 19181-RS-SAO BORJA`;
- **14.247 registros emitidos**;
- crédito total: **R$ 24.535.168,54**;
- crédito médio: **R$ 1.722,13**.

A contagem é de registros, não pessoas beneficiárias únicas.

### Novo Bolsa Família — série janeiro–julho de 2026

Fonte: Portal da Transparência / CGU — Dados Abertos — Novo Bolsa Família.

Recorte: `UF = RS`, `NOME MUNICÍPIO = SAO BORJA` após normalização; código Município SIAFI observado `8863`.

Controle de privacidade: **nenhum CPF, NIS ou nome individual foi persistido**.

Resultados calculados:

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo de referência corrente: **R$ 10.514.491,00**;
- ajustes de referências anteriores: **R$ 89.800,00 / 0,84683%**;
- média mensal do fluxo corrente: **R$ 1.502.070,14**;
- variação jan→jul do fluxo corrente: **-0,28973%**;
- variação jan→jul da média por registro corrente: **+1,11650%**;
- coeficiente de variação mensal do fluxo corrente: **0,70509%**.

Ajustes retroativos por competência: jan 2,78741%; fev 0,29716%; mar 2,00992%; abr 0,69774%; mai 0,04012%; jun/jul 0%.

**Competência não equivale automaticamente a referência.** Para comparar o fluxo corrente, o projeto separa parcelas cujo `MÊS REFERÊNCIA` coincide com a competência.

### Cobertura oficial do Novo Bolsa Família

Foram identificados **41 endpoints ZIP mensais consecutivos entre 2023-03 e 2026-07**.

Isso comprova disponibilidade da fonte, não comparabilidade automática de layout/conceito.

Rastreabilidade da série:

- workflow `novo-bolsa-familia-series-2026`;
- run `34288591742`;
- artifact `10080614700`;
- SHA-256 do artifact `68e0548f2daeed4c5d8ad5a2800a3a07f94fb26f84f3e678d41f84cf54974a70`.

Drive:

- pasta bruta `_sao_borja/raw/social/novo_bolsa_familia_portal_transparencia/`, ID `15loZ2NDpNcwIwI4hFTxjsNKjFzaxekhq`;
- pacote série v002: ID `1BzTJVG1nTUKF-vl4riX3dPSdZF1ZEJa7`;
- CSV analítico v002: ID `1nD5kpXmKDrjDuWbITB7CAGUtUDQx1sSt`;
- auditoria de cobertura v002: ID `1XFmz-fQlH64eQ0fGaOhXlj9AhUMeKENN`;
- nota metodológica nativa v002: ID `1okus0U8IMDtzHjGZHtpESLsxtTPY2L4kUNLrz-_Sobs`.

## Correção conceitual — Bolsa Família

A planilha anteriormente localizada no Drive continua classificada como **IGD transferido ao FMAS**, repasse administrativo de gestão, e permanece excluída de renda domiciliar e demanda de consumo.

A base oficial usa `VALOR PARCELA` de favorecidos e constitui transferência monetária registrada no programa. Ainda assim, transferência registrada ≠ consumo observado ≠ retenção local.

## Leitura analítica corrente

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes a participação cadastral externa;
- o varejo é o principal nó externo em peso absoluto, enquanto finanças e energia têm dependência funcional externa muito elevada;
- IPM e VAF não se movem mecanicamente na mesma direção;
- 21,31% dos domicílios são unipessoais;
- **85,79%** dos moradores do universo da tabela 10296 estão sem rendimento ou em faixas de até 2 SM per capita;
- o INSS/SUIBE registra **R$ 24,535 milhões** em benefícios/créditos emitidos a residentes em julho de 2026;
- o Novo Bolsa Família apresenta fluxo corrente médio de **R$ 1,502 milhão/mês** em jan–jul/2026, com baixa dispersão no intervalo.

As referências monetárias de Censo 2022, RAIS 2025, INSS 2026-07 e Novo Bolsa Família 2026 têm universos e conceitos diferentes e **não devem ser somadas diretamente**.

## Rendas e transferências não laborais — estado

A referência municipal do INSS/SUIBE para julho de 2026 está consolidada e a série Novo Bolsa Família janeiro–julho de 2026 está construída.

A lacuna passa a ser **outras transferências monetárias diretamente recebidas por residentes/famílias**, além da extensão longitudinal dessas bases.

## Próxima agenda

1. estender a série Novo Bolsa Família para a cobertura oficial desde 2023-03, validando mudanças de esquema;
2. mapear outras transferências monetárias relevantes em fontes oficiais;
3. avaliar série mensal INSS/SUIBE;
4. somente depois definir metodologia explícita para capacidade de compra, renda disponível aproximada, retenção local e alocação setorial do gasto;
5. conectar renda, benefícios e transferências aos quatro cadernos setoriais e à matriz de controle territorial;
6. manter fiscalidade, VAF e IPM em trilha conceitual própria.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
