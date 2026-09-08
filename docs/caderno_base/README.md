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
- Mercado consumidor — base territorial corrente: `docs/caderno_base/mercado_consumidor_base_v002.md`.
- Mercado consumidor — versão histórica anterior: `docs/caderno_base/mercado_consumidor_base_v001.md`.
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

### Mercado consumidor — base integrada

A aba `Mercado_consumidor_base` conecta, sem fundir conceitos distintos, população, estrutura domiciliar, produção econômica, emprego formal, remuneração e agora **rendimento domiciliar per capita**.

Dados já incorporados:

- população residente — Censo 2022: **59.676 pessoas** — IBGE/SIDRA;
- população estimada 2025: **61.311 pessoas** — IBGE, estimativa oficial;
- diferença calculada estimativa 2025/Censo 2022: **1.635 pessoas / 2,7398%**, explicitamente não tratada como taxa oficial de crescimento;
- domicílios unipessoais — Censo 2022: **4.815 / 21,31%**;
- domicílios nucleares: **13.820 / 61,17%**;
- domicílios estendidos: **3.518 / 15,57%**;
- domicílios compostos: **438 / 1,94%**;
- soma calculada das quatro categorias reportadas: **22.591 domicílios**, sem relabelagem como total oficial;
- PIB a preços correntes 2023: **R$ 2.550.388.000** — SIDRA tabela 5938;
- PIB per capita 2023: **R$ 42.737,25** — IBGE Cidades.

#### Rendimento domiciliar per capita — Censo 2022

A lacuna de média e mediana foi **ENCERRADA** por extração direta da API oficial IBGE/SIDRA, tabela 10295:

- variável 13431 — rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- variável 13534 — rendimento nominal mediano mensal domiciliar per capita: **R$ 1.100,00**;
- diferença calculada média − mediana: **R$ 468,58**;
- média **42,5982%** acima da mediana, apresentada como **42,60%**.

Definição da fonte: moradores em domicílios particulares permanentes ocupados, **exclusive pensionistas, empregados(as) domésticos(as) e parentes de empregados(as) domésticos(as)**.

Rastreabilidade:

- workflow `consumer-income-sidra`;
- run `34269331974`, job `102206631993`, success;
- HTTP 200;
- SHA-256 JSON bruto `29e84da86e8424d0727325647634b9565e1f181374bf3cedf3c3c64936adea33`;
- artifact ID `10073147229`, ZIP SHA-256 `7c1d5f13cf6445810a376cae8ed929734f0a00254b82354d2c923351c8cced02`;
- pacote preservado no Drive: `01_fontes_e_coletas/demografia/renda_domiciliar/sidra_10295_sao_borja_income_2022_official_package.zip`, ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`;
- documentação Drive: `Renda domiciliar per capita — SIDRA 10295 — auditoria e incorporação — 20260908`, ID `1WrVv6dDXeB-nzz8jxl5GLwR2LrPZPrBchKtaQu0KfqY`.

Interpretação controlada: a mediana abaixo da média recomenda não representar o consumidor típico somente pela média. A mediana fornece referência central menos sensível aos valores superiores. A diferença é compatível com assimetria à direita, mas **não constitui medida de desigualdade** e não permite inferir Gini, quantis ou concentração.

Limitação crítica: **não multiplicar a média pela população total** para estimar massa de renda. Antes disso deve ser recuperado o número de moradores do mesmo universo da tabela 10295.

Indicadores transversais calculados apenas para contexto:

- **112,64 estabelecimentos empresariais por mil residentes estimados**;
- **140,19 vínculos empresariais por mil residentes estimados**;
- **1,2446 vínculo empresarial por estabelecimento empresarial**.

Eles não são taxas oficiais de empreendedorismo, ocupação ou tamanho médio de empresa.

A planilha de Bolsa Família localizada no Drive permanece classificada corretamente como **IGD transferido ao FMAS**, não benefício recebido pelas famílias, e está excluída de renda domiciliar e demanda de consumo.

## Mudança de estágio: da auditoria à análise

Auditorias encerradas funcionam como controles de integridade e só devem ser reabertas por nova competência, mudança metodológica, falha de integridade ou lacuna específica.

O foco corrente é **análise territorial integrada**.

Resultados centrais até aqui:

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes sua participação cadastral;
- a remuneração média implícita estimada nas estruturas externas é cerca de 22,03% superior à local dentro do mesmo modelo;
- as quatro maiores divisões CNAE concentram 73,05% da remuneração de dezembro estimada como externa; as seis maiores, 81,91%;
- o varejo é o principal nó externo em peso absoluto: 6,63% de presença cadastral externa, 37,46% do emprego e 38,16% da remuneração de dezembro estimados como externos;
- finanças e energia/utilidades apresentam dependência funcional externa muito elevada nas métricas disponíveis;
- o IPM apresenta ciclos de perda e recuperação, não tendência linear;
- no alinhamento VAF `t` → IPM `t+2`, 15/23 transições têm o mesmo sinal e 8/23 divergem; em todas as divergências, o VAF nominal municipal cresceu enquanto o IPM caiu;
- **21,31% dos domicílios são unipessoais**, justificando testar hipóteses de conveniência e consumo em menor escala;
- a renda domiciliar per capita possui **média de R$ 1.568,58 e mediana de R$ 1.100,00**, tornando a mediana uma referência central importante para a leitura de mercado.

## Próxima agenda

A matriz setorial v001, a base demográfica/domiciliar e a média/mediana do rendimento domiciliar per capita estão concluídas. Próximos passos prioritários:

1. recuperar a **distribuição municipal da renda por faixas/quantis** e o **número de moradores do mesmo universo** da tabela 10295;
2. incorporar aposentadorias, pensões e benefícios previdenciários pagos a residentes por fonte oficial;
3. incorporar transferências monetárias efetivamente recebidas pelas famílias, distinguindo-as de repasses administrativos;
4. somente então estruturar massa de renda, capacidade de compra e segmentação econômica do mercado consumidor;
5. conectar essa capacidade de demanda à matriz de controle territorial e aos quatro cadernos setoriais;
6. na fiscalidade, seguir para denominador/índice estadual do VAF, decomposição do IPM e quota-parte monetária efetivamente transferida, sem repetir a coleta municipal já encerrada.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. A regra central continua válida: nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
