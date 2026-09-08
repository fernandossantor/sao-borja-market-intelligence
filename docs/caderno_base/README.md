# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa que altere dados, indicadores, método, interpretação ou diagnóstico do Caderno-Base deve atualizar no mesmo ciclo, quando aplicável:

1. derivados auditáveis e sua promoção ao Google Drive;
2. manifestos, metadados, validações e hashes;
3. narrativa analítica em `docs/caderno_base/`;
4. versão corrente da planilha do Caderno-Base no Drive;
5. descrição do PR/branch, separando observado, calculado, estimado, hipótese, interpretação e recomendação.

Versões anteriores permanecem preservadas quando necessárias para auditoria histórica.

## Versão corrente

- Caderno corrente: `caderno_base_territorial_v008_diagnostico_integrado_20260907` — Drive ID `1NJp_tmQ36NE8YDA2JhmyqjsnB1a7V9ivtAFJW7YLhcU`.
- Versão histórica anterior: `caderno_base_territorial_v007_fiscalidade_ipm_20260907` — Drive ID `1x83_dMuDQ9ks0mdNnv6mdw_Sopt7-KjIFWrD1rlouz8`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v005.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v004.md`.
- Mercado consumidor corrente: `docs/caderno_base/mercado_consumidor_base_v004.md`.
- Mercado consumidor anterior: `docs/caderno_base/mercado_consumidor_base_v003.md`.
- Nota INSS/SUIBE: `docs/caderno_base/inss_beneficios_residentes_202607_v001.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.

Documento analítico nativo corrente no Drive: `Caderno-Base — diagnóstico analítico integrado v003 — 20260908`, ID `1tIHJpW3w-HxaCQhSOAvWlHKFYxeEz_axc1owGyMhYmA`.

A v008 preserva as abas anteriores e inclui `Diagnostico_integrado`, `VAF_reconciliacao`, `VAF_historico`, `VAF_IPM_exploratorio`, `Matriz_controle_setorial`, `Mercado_consumidor_base` e, a partir desta etapa, `INSS_beneficios_202607`.

## Estado das bases principais

### Controle empresarial

- RFB Dados Abertos CNPJ, competência 2026-08;
- 6.906 estabelecimentos empresariais no universo analítico;
- 284 de matriz externa;
- participação externa cadastral: **4,1124%**.

### Emprego e remuneração

- RAIS 2025 × RFB 2026-08, compatibilização CNAE × natureza jurídica;
- 8.595 vínculos empresariais;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na soma das remunerações médias: **29,0903%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- auditoria: 7/7 controles PASS, 0 vínculos unmatched.

### IPM definitivo

- Receita Estadual/RS — arquivos `DAIM545X`;
- série canônica 2003–2026, 24/24 anos;
- 2025: 0,527880;
- 2026: 0,533647;
- variação 2026/2025: **+1,092483%**.

### VAF — Valor Adicionado Municípios

A etapa de fonte para o intervalo em REAL está concluída.

- Receita Estadual/SEFAZ-RS;
- São Borja/RS, prefixo 117;
- cobertura 1994–2025, **32/32 rótulos anuais**;
- 2024: R$ 2.907.302.928,34;
- 2025: R$ 2.325.966.620,93;
- variação nominal 2025/2024: **-19,9957%**;
- benchmark Sebrae 2009–2019 ↔ SEFAZ 2007–2017: **11/11 correspondências**, com deslocamento de dois anos;
- alinhamento exploratório VAF `t` → IPM `t+2`: 15/23 sinais concordantes e 8/23 divergentes, sem inferência causal.

## Mercado consumidor — base integrada

### Escala e estrutura domiciliar

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**;
- PIB 2023: **R$ 2.550.388.000**;
- PIB per capita 2023: **R$ 42.737,25**.

PIB não é renda domiciliar e composição domiciliar não demonstra comportamento de compra.

### Rendimento domiciliar per capita — SIDRA 10295/10296

- média nominal mensal per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 1 SM: **35.020 / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- acima de 2 SM: **8.388 / 14,20780%**;
- acima de 5 SM: **1.643 / 2,78295%**.

Essas agregações são calculadas pelo SBMI; não são categorias oficiais nem classes sociais.

### Massa mensal implícita de rendimento

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Natureza: calculado. Referência: Censo 2022.

Esse valor é massa mensal implícita de rendimento no universo estatístico, não renda disponível, consumo efetivo, faturamento comercial ou potencial setorial.

### Benefícios emitidos pelo INSS/SUIBE — julho de 2026

A primeira referência oficial municipal está **ENCERRADA** para a competência 2026-07.

Fonte: INSS Portal de Dados Abertos / SUIBE — `Benefícios Emitidos Julho 2026`.

Recorte canônico: `municipio_residencia = 19181-RS-SAO BORJA`.

Resultados calculados a partir dos registros oficiais:

- **14.247 registros emitidos**;
- **14.247 registros com `credito` válido**;
- crédito total: **R$ 24.535.168,54**;
- crédito médio por registro: **R$ 1.722,13**.

A contagem é de registros, não pessoas beneficiárias únicas.

As duas espécies literalmente denominadas `AMPARO SOCIAL` somam:

- **3.385 registros**;
- **R$ 4.777.117,64**;
- **23,75939%** dos registros;
- **19,47049%** do crédito total.

Esse subtotal não é relabelado como total da assistência social ou dos benefícios não contributivos.

A aba `INSS_beneficios_202607` preserva **27 espécies literais**, número de registros, soma de `credito` e participações calculadas. O recorte municipal exclui registros anômalos da fonte que contêm `SAO BORJA` associado a outras UFs.

Rastreabilidade:

- workflow `inss-benefits-residence-extract`;
- run `34282566426`;
- artifact `10078228209`;
- SHA-256 do artifact `2f75523301768374ee1e9a908480ca850d93d6fe661407991ade50f9c800ba87`;
- SHA-256 do CSV municipal `eb9e2536026d460892ea64cf672bf3cc26da1231bbf552f3ddd51d4c6945996c`.

Drive:

- pasta `_sao_borja/raw/social/inss_suibe_beneficios_emitidos/`, ID `1gIN6tmhHg-r7lPBlpCnGHNggZCj568vO`;
- pacote oficial municipal ID `11lAy2Dtlw20tzhOb8Y4ltkbpyZPDhbOs`;
- nota metodológica ID `1bn5C6u1GII4eHrDwUnDRgTA27VR_YK4yL-QChWk_ncI`.

## Leitura analítica corrente

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes a participação cadastral externa;
- o varejo é o principal nó externo em peso absoluto, enquanto finanças e energia têm dependência funcional externa muito elevada;
- IPM e VAF não se movem mecanicamente na mesma direção;
- 21,31% dos domicílios são unipessoais, justificando hipóteses específicas de conveniência e menor escala;
- a renda domiciliar média de R$ 1.568,58 deve ser lida junto à mediana de R$ 1.100,00 e à distribuição: **85,79% dos moradores do universo estão sem rendimento ou em faixas de até 2 SM per capita**;
- o INSS/SUIBE acrescenta um fluxo de **R$ 24,535 milhões** em benefícios emitidos a residentes na competência observada, demonstrando que a caracterização da renda local não pode se apoiar apenas na remuneração formal do trabalho.

As três referências monetárias mensais — Censo 2022, RAIS 2025 e INSS 2026-07 — têm períodos, universos e conceitos diferentes e **não devem ser somadas diretamente**.

## Rendas não laborais — estado

A lacuna de uma primeira referência oficial municipal do INSS/SUIBE está encerrada para julho de 2026.

A planilha de Programa Bolsa Família já localizada no Drive permanece classificada como **IGD transferido ao FMAS**, recurso administrativo e não benefício monetário recebido pelas famílias. Continua excluída de renda domiciliar e demanda de consumo.

A lacuna prioritária remanescente é recuperar **transferências monetárias efetivamente recebidas pelas famílias** em fonte oficial.

## Próxima agenda

1. recuperar transferências monetárias diretamente recebidas pelas famílias, distinguindo-as de repasses administrativos;
2. avaliar série mensal INSS/SUIBE, repetindo a mesma regra territorial e auditoria de layout;
3. somente após essas camadas definir metodologia explícita para capacidade de compra, renda disponível aproximada, retenção local e alocação setorial do gasto;
4. conectar renda, benefícios e distribuição aos quatro cadernos setoriais e à matriz de controle territorial;
5. manter fiscalidade, VAF e IPM em trilha conceitual própria.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
