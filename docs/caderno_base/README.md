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

A v008 preserva todas as abas anteriores e acrescenta:

- `Diagnostico_integrado`;
- `VAF_reconciliacao`;
- `VAF_historico`;
- `VAF_IPM_exploratorio`.

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
- `_sao_borja/exports/caderno-base-v008-diagnostico-integrado-v001/vaf_ipm_alinhamento_exploratorio_v001.csv`.

Pacotes brutos e HTMLs oficiais permanecem em `_sao_borja/raw/fiscal/vaf_sefaz_rs`.

## Mudança de estágio: da auditoria à análise

A prioridade do projeto deixa de ser repetir auditorias já encerradas. Elas passam a funcionar como controles de integridade e somente devem ser reabertas quando houver nova competência, mudança metodológica, falha de integridade ou necessidade específica ainda não coberta.

O foco corrente é **análise territorial integrada**.

Primeiros resultados:

- o peso estimado das estruturas externas no emprego é aproximadamente 6,12 vezes sua participação cadastral;
- a remuneração média implícita estimada nas estruturas externas é cerca de 22,03% superior à local dentro do mesmo modelo;
- as quatro maiores divisões CNAE concentram 73,05% da remuneração de dezembro estimada como externa; as seis maiores, 81,91%;
- o varejo é o principal nó de emprego externo estimado;
- o IPM apresenta ciclos de perda e recuperação, e não tendência linear;
- no alinhamento exploratório VAF `t` → IPM `t+2`, 15/23 transições têm o mesmo sinal e 8/23 divergem; em todas as divergências, o VAF municipal nominal cresceu enquanto o IPM caiu. Isso reforça que o VAF nominal municipal, isoladamente, não explica a participação relativa do município no ICMS.

## Próxima agenda

1. construir matriz setorial de controle territorial — cadastro × emprego × remuneração;
2. integrar estrutura empresarial com consumidores, renda, população e mercado de trabalho;
3. classificar setores em base local forte, presença externa complementar, dependência funcional externa e setores estratégicos de rede;
4. na fiscalidade, buscar denominador/índice estadual, decomposição dos critérios do IPM e quota-parte monetária efetivamente transferida, em vez de repetir a coleta do VAF municipal;
5. transformar os resultados em narrativa explicativa e diagnóstica para o Caderno-Base e, posteriormente, para os quatro cadernos setoriais.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. A regra central continua válida: nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
