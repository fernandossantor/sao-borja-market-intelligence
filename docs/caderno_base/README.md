# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa que altere dados, indicadores, método, interpretação ou diagnóstico do Caderno-Base deve atualizar no mesmo ciclo, quando aplicável:

1. os derivados auditáveis em `.data/exports/` e sua promoção à pasta `_sao_borja/exports/` no Google Drive;
2. os manifestos, metadados, validações e hashes das saídas;
3. a narrativa analítica correspondente em `docs/caderno_base/`;
4. a versão corrente da planilha de controle do Caderno-Base no Drive, criando nova versão quando a mudança representar novo estágio substantivo;
5. a descrição do PR/branch de trabalho, preservando explicitamente o que é observado, calculado, estimado, hipótese, interpretação e recomendação.

Versões anteriores não devem ser sobrescritas quando forem necessárias para auditoria histórica.

## Versão corrente

- Caderno corrente: `caderno_base_territorial_v008_diagnostico_integrado_20260907` — Drive ID `1NJp_tmQ36NE8YDA2JhmyqjsnB1a7V9ivtAFJW7YLhcU`.
- Versão histórica imediatamente anterior: `caderno_base_territorial_v007_fiscalidade_ipm_20260907` — Drive ID `1x83_dMuDQ9ks0mdNnv6mdw_Sopt7-KjIFWrD1rlouz8`.
- Documento analítico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v002.md`.
- Nota fiscal/VAF: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.
- Matriz setorial: `docs/caderno_base/matriz_controle_setorial_v001.md`.
- Mercado consumidor — base territorial: `docs/caderno_base/mercado_consumidor_base_v001.md`.
- Checkpoint de retomada: `docs/caderno_base/checkpoint_20260907.md`.

A v008 preserva todas as abas anteriores e acrescenta, nesta etapa analítica:

- `Diagnostico_integrado`;
- `VAF_reconciliacao`;
- `VAF_historico`;
- `VAF_IPM_exploratorio`;
- `Matriz_controle_setorial`;
- `Mercado_consumidor_base`.

## Estado das bases principais

### Controle empresarial

- Fonte: RFB Dados Abertos CNPJ, competência 2026-08.
- 6.906 estabelecimentos empresariais;
- 284 de matriz externa;
- participação externa cadastral: 4,1124%.

### Emprego e remuneração

- Fonte: RAIS 2025 × RFB 2026-08, compatibilização por CNAE × natureza jurídica.
- 8.595 vínculos empresariais reconciliados;
- participação externa estimada no emprego: 25,1606%;
- participação externa estimada na soma das remunerações médias: 29,0903%;
- participação externa estimada na remuneração de dezembro: 29,6897%;
- auditoria: 7/7 controles PASS, 0 vínculos unmatched.

### IPM definitivo

- Fonte: Receita Estadual/RS — arquivos `DAIM545X`.
- Série canônica: 2003–2026, 24/24 anos.
- Validação: 7/7 controles PASS.
- 2025: 0,527880;
- 2026: 0,533647;
- variação 2026/2025: +1,092483%.

### VAF — Valor Adicionado Municípios

A etapa de fonte para o intervalo em REAL está **CONCLUÍDA**.

- Fonte: Receita Estadual/SEFAZ-RS — consulta oficial Valor Adicionado Municípios.
- Geografia: São Borja/RS, prefixo 117.
- Cobertura canônica publicada: **1994–2025, 32/32 rótulos anuais**.
- Unidade: REAL, valores nominais/correntes publicados pela fonte.
- Terminologia temporal: preserva-se `ano_rotulo_fonte`; o formulário denomina os intervalos como “Anos de Apuração”.
- 2024: R$ 2.907.302.928,34 — maior valor nominal da série.
- 2025: R$ 2.325.966.620,93.
- variação nominal calculada 2025/2024: **-19,9957%**.
- benchmark Sebrae/RS 2009–2019: **11/11 correspondências consecutivas** com SEFAZ 2007–2017 quando arredondado para R$ milhões, sempre com deslocamento de dois anos.

Derivados promovidos ao Drive:

- `_sao_borja/exports/caderno-base-v008-diagnostico-integrado-v001/vaf_sao_borja_1994_2025_oficial_v001.csv`;
- `_sao_borja/exports/caderno-base-v008-diagnostico-integrado-v001/vaf_ipm_alinhamento_exploratorio_v001.csv`;
- `_sao_borja/exports/caderno-base-v008-diagnostico-integrado-v001/matriz_controle_setorial_sao_borja_v001.csv`.

Pacotes brutos e HTMLs oficiais permanecem em `_sao_borja/raw/fiscal/vaf_sefaz_rs`.

### Mercado consumidor — primeira base integrada

A nova aba `Mercado_consumidor_base` conecta, sem fundir conceitos distintos, população, estrutura domiciliar, produção econômica, emprego formal e remuneração.

Dados incorporados:

- população residente — Censo 2022: **59.676 pessoas** — IBGE/SIDRA;
- população estimada 2025: **61.311 pessoas** — IBGE, estimativa oficial;
- diferença calculada entre estimativa 2025 e Censo 2022: **1.635 pessoas / 2,7398%**, explicitamente não tratada como taxa oficial de crescimento;
- domicílios unipessoais — Censo 2022: **4.815 / 21,31%**;
- domicílios nucleares: **13.820 / 61,17%**;
- domicílios estendidos: **3.518 / 15,57%**;
- domicílios compostos: **438 / 1,94%**;
- soma calculada das quatro categorias reportadas: **22.591 domicílios**, sem relabelagem como total oficial;
- PIB a preços correntes 2023: **R$ 2.550.388.000** — SIDRA tabela 5938, unidade original mil R$;
- PIB per capita 2023: **R$ 42.737,25** — IBGE Cidades.

Indicadores transversais calculados apenas para contexto:

- **112,64 estabelecimentos empresariais por mil residentes estimados**;
- **140,19 vínculos empresariais por mil residentes estimados**;
- **1,2446 vínculo empresarial por estabelecimento empresarial**.

Esses indicadores não são taxas oficiais de empreendedorismo, ocupação ou tamanho médio de empresa, pois combinam períodos/universos diferentes e vínculo não equivale a trabalhador único.

A principal lacuna atual é renda domiciliar. Foi identificada a **tabela SIDRA 10295 — Censo 2022**, com rendimento nominal médio e mediano mensal domiciliar per capita em nível municipal. A definição exclui pensionistas, empregados domésticos e parentes de empregados domésticos. Os valores específicos de São Borja ainda não foram incorporados sem recuperação direta da consulta oficial.

A planilha de Bolsa Família localizada no Drive foi classificada corretamente como **IGD transferido ao FMAS**, e não como benefício recebido pelas famílias; portanto, não integra renda domiciliar nem demanda de consumo.

## Mudança de estágio: da auditoria à análise

A prioridade do projeto deixou de ser repetir auditorias já encerradas. Elas funcionam como controles de integridade e somente devem ser reabertas quando houver nova competência, mudança metodológica, falha de integridade ou necessidade específica ainda não coberta.

O foco corrente é **análise territorial integrada**.

Primeiros resultados:

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes sua participação cadastral;
- a remuneração média implícita estimada nas estruturas externas é cerca de 22,03% superior à local dentro do mesmo modelo;
- as quatro maiores divisões CNAE concentram 73,05% da remuneração de dezembro estimada como externa; as seis maiores, 81,91%;
- o varejo é o principal nó externo em peso absoluto: 6,63% de presença cadastral externa na divisão, mas 37,46% do emprego e 38,16% da remuneração de dezembro estimados como externos; responde por 36,41% do total externo de dezembro;
- finanças (96,73% do emprego; 98,70% da remuneração) e energia/utilidades (96,20%; 100%) apresentam dependência funcional externa muito elevada nas métricas disponíveis;
- transporte e serviços de apoio empresarial mostram que baixa presença cadastral externa pode coexistir com maior peso funcional;
- percentuais elevados precisam ser lidos com peso absoluto: serviços pessoais têm 57,57% da remuneração estimada como externa, mas apenas 27 vínculos e 0,60% do total externo de dezembro;
- o IPM apresenta ciclos de perda e recuperação, e não tendência linear;
- no alinhamento exploratório VAF `t` → IPM `t+2`, 15/23 transições têm o mesmo sinal e 8/23 divergem; em todas as divergências, o VAF municipal nominal cresceu enquanto o IPM caiu;
- a estrutura domiciliar acrescenta uma dimensão mercadológica transversal: **21,31% dos domicílios são unipessoais**, o que justifica testar hipóteses de conveniência e consumo em menor escala, sem presumir comportamento de compra.

## Próxima agenda

A matriz setorial v001 e a primeira base demográfica/domiciliar estão concluídas. Próximos passos prioritários:

1. recuperar e preservar o rendimento domiciliar mensal per capita médio e mediano de São Borja na tabela SIDRA 10295;
2. incorporar aposentadorias, pensões e benefícios previdenciários pagos a residentes por fonte oficial;
3. incorporar transferências de renda efetivamente recebidas pelas famílias, distinguindo-as de repasses administrativos aos fundos públicos;
4. só então estruturar uma leitura de capacidade de compra e segmentação econômica do mercado consumidor;
5. conectar essa capacidade de demanda à matriz de controle territorial e aos quatro cadernos setoriais;
6. na fiscalidade, seguir para denominador/índice estadual do VAF, decomposição do IPM e quota-parte monetária efetivamente transferida, sem repetir a coleta municipal já encerrada.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. A regra central continua válida: nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
