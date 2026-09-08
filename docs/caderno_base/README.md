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
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v004.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v003.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.
- Mercado consumidor corrente: `docs/caderno_base/mercado_consumidor_base_v003.md`.
- Mercado consumidor anterior: `docs/caderno_base/mercado_consumidor_base_v002.md`.

A v008 preserva as abas anteriores e inclui `Diagnostico_integrado`, `VAF_reconciliacao`, `VAF_historico`, `VAF_IPM_exploratorio`, `Matriz_controle_setorial` e `Mercado_consumidor_base`.

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

### Rendimento domiciliar per capita — tabela SIDRA 10295

Lacuna encerrada por consulta oficial direta:

- média nominal mensal per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- diferença: **R$ 468,58**;
- média **42,60%** acima da mediana.

Universo: moradores em domicílios particulares permanentes ocupados, exclusive pensionistas, empregados(as) domésticos(as) e parentes de empregados(as) domésticos(as).

Rastreabilidade: workflow `consumer-income-sidra`, run `34269331974`, job `102206631993`; raw SHA-256 `29e84da86e8424d0727325647634b9565e1f181374bf3cedf3c3c64936adea33`.

Drive:
- pacote ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`;
- documento metodológico ID `1WrVv6dDXeB-nzz8jxl5GLwR2LrPZPrBchKtaQu0KfqY`.

### Distribuição do rendimento — tabela SIDRA 10296

A lacuna de distribuição e denominador compatível também está **ENCERRADA**.

- universo: **59.038 moradores**;
- até 1/4 SM: 2.441 / 4,13463%;
- >1/4 a 1/2 SM: 10.917 / 18,49148%;
- >1/2 a 1 SM: 20.174 / **34,17121%**;
- >1 a 2 SM: 15.630 / 26,47447%;
- >2 a 3 SM: 4.659 / 7,89153%;
- >3 a 5 SM: 2.086 / 3,53332%;
- >5 a 10 SM: 1.237 / 2,09526%;
- >10 a 15 SM: 286 / 0,48443%;
- >15 a 20 SM: 33 / 0,05590%;
- >20 SM: 87 / 0,14736%;
- sem rendimento: 1.488 / 2,52041%.

Agregações calculadas do SBMI:

- sem rendimento ou até 1 SM: **35.020 / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- acima de 2 SM: **8.388 / 14,20780%**;
- acima de 5 SM: **1.643 / 2,78295%**.

Essas agregações não são categorias oficiais nem classes sociais.

Rastreabilidade: workflow `consumer-income-distribution-sidra`, run `34280745734`, job `102244621346`, HTTP 200, raw SHA-256 `c605f8898dbe8ba0af0e22b844078da072e75c9d3a2349da5bee3e6901f2dc09`, artifact ID `10077490347`.

Drive:
- pacote `sidra_10296_sao_borja_income_distribution_2022_v002_official_package.zip`, ID `1eUgoL_9n5oXNtVBWTC-pYRFpCJul2cQA`;
- documento `Distribuição do rendimento domiciliar per capita — SIDRA 10296 — auditoria e incorporação — 20260908`, ID `1NUbnNZ99hhlgoejWGTj1HR1CFcxJpwSnnbf9tHEostQ`.

### Massa mensal implícita de rendimento

Como a média e o denominador pertencem ao mesmo universo estatístico:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Natureza: calculado. Referência: Censo 2022.

Esse valor é **massa mensal implícita de rendimento no universo estatístico**, não renda disponível, consumo efetivo, faturamento comercial, potencial setorial ou montante necessariamente gasto em São Borja.

## Leitura analítica corrente

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes a participação cadastral externa;
- o varejo é o principal nó externo em peso absoluto, enquanto finanças e energia têm dependência funcional externa muito elevada;
- IPM e VAF não se movem mecanicamente na mesma direção;
- 21,31% dos domicílios são unipessoais, justificando hipóteses específicas de conveniência e menor escala;
- a renda domiciliar média de R$ 1.568,58 deve ser lida junto à mediana de R$ 1.100,00 e à distribuição: **85,79% dos moradores do universo estão sem rendimento ou em faixas de até 2 SM per capita**.

Esse último percentual mede participação de pessoas, não participação na massa monetária da renda, e não autoriza inferir classe social ou comportamento de compra.

## Rendas não laborais — estado

A planilha de Programa Bolsa Família já localizada no Drive é **IGD transferido ao FMAS**, recurso administrativo e não benefício recebido pelas famílias. Permanece excluída de renda domiciliar e demanda de consumo.

A fonte oficial do INSS/SUIBE para benefícios emitidos foi identificada e a rotina municipal está em auditoria. O arquivo nacional de julho de 2026 possui cerca de 999 MB compactados e usa os campos `municipio_pagamento`, `municipio_residencia` e `credito`; o portal descreve semanticamente o conteúdo de `credito` como valor líquido. Nenhum valor municipal previdenciário foi canonizado ainda.

## Próxima agenda

Média, mediana, distribuição por faixas e denominador compatível da renda domiciliar do Censo 2022 estão concluídos. Próximos passos:

1. concluir a extração/auditoria dos benefícios previdenciários por **município de residência**;
2. incorporar transferências monetárias efetivamente recebidas pelas famílias;
3. definir posteriormente uma metodologia explícita para capacidade de compra, renda disponível aproximada, retenção local e alocação setorial do gasto;
4. conectar a distribuição de renda aos quatro cadernos setoriais e à matriz de controle territorial;
5. manter fiscalidade, VAF e IPM em trilha conceitual própria.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
