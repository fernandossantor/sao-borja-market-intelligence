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

- Caderno corrente: `caderno_base_territorial_v008_diagnostico_integrado_20260907` — Drive ID `1NJp_tmQ36NE8YDA2JhmyqjsnB1a7V9ivtAFJW7YLhcU`.
- Versão histórica anterior: `caderno_base_territorial_v007_fiscalidade_ipm_20260907` — Drive ID `1x83_dMuDQ9ks0mdNnv6mdw_Sopt7-KjIFWrD1rlouz8`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v006.md`.
- Documento analítico anterior: `docs/caderno_base/diagnostico_analitico_integrado_v005.md`.
- Mercado consumidor corrente: `docs/caderno_base/mercado_consumidor_base_v005.md`.
- Mercado consumidor anterior: `docs/caderno_base/mercado_consumidor_base_v004.md`.
- Nota Novo Bolsa Família: `docs/caderno_base/novo_bolsa_familia_sao_borja_202607_v001.md`.
- Nota INSS/SUIBE: `docs/caderno_base/inss_beneficios_residentes_202607_v001.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.

A v008 preserva as abas anteriores e inclui `Diagnostico_integrado`, `VAF_reconciliacao`, `VAF_historico`, `VAF_IPM_exploratorio`, `Matriz_controle_setorial`, `Mercado_consumidor_base`, `INSS_beneficios_202607` e `Novo_Bolsa_Familia_202607`.

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
- benchmark Sebrae 2009–2019 ↔ SEFAZ 2007–2017: **11/11 correspondências**, deslocamento de dois anos;
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

Primeira referência oficial municipal **ENCERRADA** para 2026-07.

- recorte: `municipio_residencia = 19181-RS-SAO BORJA`;
- **14.247 registros emitidos**;
- **14.247 registros com `credito` válido**;
- crédito total: **R$ 24.535.168,54**;
- crédito médio por registro: **R$ 1.722,13**.

A contagem é de registros, não pessoas beneficiárias únicas. As duas espécies literalmente denominadas `AMPARO SOCIAL` somam **R$ 4.777.117,64**, ou **19,47049%** do crédito total, sem que isso seja relabelado como toda a assistência social.

### Novo Bolsa Família — julho de 2026

Primeira referência oficial municipal **ENCERRADA** para 2026-07.

Fonte: Portal da Transparência / CGU — Dados Abertos — Novo Bolsa Família.

Recorte: `UF = RS`, `NOME MUNICÍPIO = SAO BORJA` após normalização; código Município SIAFI observado `8863`.

Resultados calculados a partir dos registros oficiais:

- **2.199 registros/parcela**;
- **2.199 registros com `VALOR PARCELA` válido**;
- soma de `VALOR PARCELA`: **R$ 1.513.564,00**;
- média por registro/parcela: **R$ 688,30**.

Em todos os registros municipais, `MÊS COMPETÊNCIA = 202607` e `MÊS REFERÊNCIA = 202607`.

Controles agregados: 2.198 NIS não vazios distintos, 1 NIS vazio; 1.746 CPF não vazios distintos, 439 CPF vazios. **Nenhum CPF, NIS ou nome individual foi persistido** no GitHub, Drive, Caderno ou artifact final.

Registro/parcela **não equivale automaticamente a família ou pessoa única**.

O arquivo 202607 efetivamente observado possui nove campos e **não contém `DATA DISPONIBILIZAÇÃO`**; o projeto usa somente o esquema observado, sem transpor silenciosamente campos de outras versões.

Rastreabilidade:

- workflow `novo-bolsa-familia-sao-borja-extract`;
- run `34284691474`;
- job `102257430159`;
- artifact `10079014259`;
- SHA-256 do artifact `41a27542e9b94ce07606ea7cb15868d6aafc67c073f7c8d86e21b9bc7d44c15e`;
- SHA-256 do ZIP nacional `f66e621bfdbb945cf324679e216d3d3b42d2029f39be7f646e046fd28b4c30d4`.

Drive:

- pasta `_sao_borja/raw/social/novo_bolsa_familia_portal_transparencia/`, ID `15loZ2NDpNcwIwI4hFTxjsNKjFzaxekhq`;
- pacote final agregado e sem PII: ID `1am7E0ILJCp26z9X8MjLu7sdSxqYRN1jn`;
- CSV agregado: ID `1cR1KfPWe_MMwGF9KHHrwNoGJYT5RcjUs`;
- nota metodológica nativa: ID `11LpVM7KSmgzZ7hk6Hl5eZix_FVAzPhMP9tRfXheaDNc`.

## Correção conceitual — Bolsa Família

A planilha anteriormente localizada no Drive continua classificada como **IGD transferido ao FMAS**, isto é, repasse administrativo de gestão, e permanece excluída de renda domiciliar e demanda de consumo.

A nova extração usa `VALOR PARCELA` da base oficial de favorecidos e é conceitualmente uma transferência monetária direta registrada no programa. Ainda assim, transferência registrada ≠ consumo observado ≠ retenção local.

## Leitura analítica corrente

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes a participação cadastral externa;
- o varejo é o principal nó externo em peso absoluto, enquanto finanças e energia têm dependência funcional externa muito elevada;
- IPM e VAF não se movem mecanicamente na mesma direção;
- 21,31% dos domicílios são unipessoais;
- **85,79%** dos moradores do universo da tabela 10296 estão sem rendimento ou em faixas de até 2 SM per capita;
- o INSS/SUIBE acrescenta um fluxo de **R$ 24,535 milhões** em benefícios emitidos a residentes em julho de 2026;
- o Novo Bolsa Família acrescenta **R$ 1,514 milhão** em `VALOR PARCELA` na mesma competência.

As quatro referências monetárias — Censo 2022, RAIS 2025, INSS 2026-07 e Novo Bolsa Família 2026-07 — têm universos e conceitos diferentes e **não devem ser somadas diretamente**. Pode haver sobreposição de pessoas entre fontes e programas.

## Rendas e transferências não laborais — estado

A primeira referência oficial municipal do INSS/SUIBE e a primeira referência oficial municipal do Novo Bolsa Família estão encerradas para julho de 2026.

A lacuna passa a ser **outras transferências monetárias diretamente recebidas por residentes/famílias**, sempre separando benefício monetário de repasse administrativo.

## Próxima agenda

1. construir série mensal do Novo Bolsa Família com a mesma regra de privacidade e filtro territorial;
2. mapear outras transferências monetárias relevantes em fontes oficiais;
3. avaliar série mensal INSS/SUIBE;
4. somente depois definir metodologia explícita para capacidade de compra, renda disponível aproximada, retenção local e alocação setorial do gasto;
5. conectar renda, benefícios e transferências aos quatro cadernos setoriais e à matriz de controle territorial;
6. manter fiscalidade, VAF e IPM em trilha conceitual própria.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. Nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
