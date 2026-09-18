# Boletim Econômico-Tributário RS — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Auditar o Boletim Econômico-Tributário (BET) da Receita Estadual do Rio Grande do Sul para identificar quais indicadores podem ser extraídos de forma reproduzível para São Borja, COREDE Fronteira Oeste e Rio Grande do Sul, sem alterar os dados já consolidados no SBMI.

## Fonte oficial

https://receitadoc.sefaz.rs.gov.br/boletins/

## Achados observados — etapa 1A

1. A página oficial descreve o BET como panorama detalhado da atividade econômica estadual, incluindo:
   - nível de atividade;
   - demografia de estabelecimentos;
   - recortes por setor e categoria;
   - recortes por COREDE/municípios;
   - desempenho da arrecadação estadual.

2. O arquivo público disponível na página reúne edições desde 24/05/2024 até, no momento desta auditoria, a edição 29 de 08/09/2026.

3. A edição 13, de 09/12/2024, documenta uma mudança de fonte:
   - edições 1 e 2: sistemas de inteligência da Receita Federal, em razão de indisponibilidade temporária dos sistemas da SEFAZ-RS;
   - a partir da edição 3: dados dos sistemas da Receita Estadual;
   - a partir da edição 9: periodicidade mensal.

4. A edição 13 informa uso de operações de contribuintes de ICMS e de documentos NF-e/NFC-e para parte dos indicadores.

5. A edição 13 contém tabelas por COREDE para volume de vendas da indústria. No exemplo de novembro de 2024, a Fronteira Oeste aparece com:
   - participação no total estadual: 1,2%;
   - novembro/2023: R$ 786,4 milhões;
   - novembro/2024: R$ 572,8 milhões;
   - variação interanual: -27,2%.

**Classificação:** dado observado histórico, contextualizado no período posterior às enchentes de 2024. Não utilizar esse valor como diagnóstico corrente de 2026.

6. A metodologia daquela edição registra atualização monetária dos valores de vendas industriais pelo D-ICMS, índice composto por 26% do IPCA e 74% do IGP-DI.

## Inconsistência documental identificada

A página atual dos boletins menciona que a publicação surgiu durante as enchentes de “maio de 2025”, enquanto o próprio arquivo contém edições desde maio de 2024 e a edição 13 faz referência às enchentes de maio de 2024.

**Tratamento:** registrar como inconsistência da página institucional. Não corrigir silenciosamente a fonte. Para cronologia do produto, prevalecem as datas observadas nas próprias edições arquivadas.

## O que ainda não foi concluído

Ainda não foi extraída uma série municipal de São Borja das edições recentes.

A descrição oficial confirma a existência de recortes por municípios, mas é necessário localizar:
- em quais tabelas/edições atuais São Borja aparece;
- qual indicador municipal é publicado;
- periodicidade;
- unidade;
- definição metodológica;
- possibilidade de extração reproduzível.

## Próxima subetapa — 1B

Localizar nas edições mais recentes do BET os indicadores municipais e montar uma tabela de auditoria:

`edicao | periodo_referencia | indicador | setor/categoria | geografia | valor | unidade | fonte_documental | observacao_metodologica`

Prioridade geográfica:
1. São Borja;
2. COREDE Fronteira Oeste;
3. Rio Grande do Sul.

Nenhum resultado será promovido às bases canônicas antes da conclusão desta subetapa.


## Tentativa de subetapa 1B — 17/09/2026

A página oficial foi revalidada e confirma:
- edição 29 publicada em 08/09/2026;
- arquivo histórico contínuo desde a edição 01, de 24/05/2024;
- descrição explícita de recortes por COREDE/municípios.

Foi tentada a abertura automatizada das edições recentes 22, 23, 24 e 29. Os links oficiais dos PDFs foram identificados, mas o mecanismo de leitura disponível retornou erro de cache para esses arquivos nesta sessão.

**Decisão metodológica:** não preencher valores municipais de São Borja a partir de fontes secundárias, snippets ou inferências enquanto a tabela oficial recente não puder ser lida de forma verificável.

A etapa 1B permanece aberta. O achado válido até aqui é a **capacidade territorial declarada da fonte**, não uma série municipal já extraída.

Como evidência adicional de estrutura regional, edições oficiais antigas indexadas publicamente permitem recuperar tabelas de vendas industriais por COREDE; isso confirma a consistência histórica do recorte Fronteira Oeste, mas não substitui a extração municipal atual.


## Subetapa 1C — fallback regional de validação

Como a extração municipal recente de São Borja ainda não foi obtida de forma verificável, foi montado um **seed regional oficial** para o COREDE Fronteira Oeste usando edições do BET que estão indexadas e legíveis.

O seed não substitui a subetapa 1B e não será promovido como série canônica.

Arquivo:

`docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`

Observações incluídas:
- ed. 04 — período 15/05 a 11/06/2024;
- ed. 08 — 01 a 15/07/2024;
- ed. 09 — julho/2024 completo;
- Edição Expointer — 01 a 25/08/2024;
- ed. 11 — setembro/2024 completo.

Todas as observações são do indicador **volume de vendas da indústria por COREDE**, em valores corrigidos pelo D-ICMS (26% IPCA e 74% IGP-DI), conforme as notas metodológicas dos boletins.

### Cuidado de comparabilidade

Os períodos parciais e completos não devem ser encadeados como uma única série mensal sem tratamento.

A utilidade do seed é:
- validar estrutura dos campos;
- comprovar a granularidade COREDE;
- testar o pipeline de ingestão;
- criar fallback regional enquanto a série municipal recente não é recuperada.

Não usar essas variações de 2024 como diagnóstico corrente de 2026.

## Retomada da subetapa 1B — 18/09/2026

A página oficial Receita.doc foi reaberta e a descrição atual do produto confirma explicitamente que o BET inclui **nível de atividade, demografia de estabelecimentos por setor, categoria e COREDE/municípios**, além do desempenho da arrecadação estadual.

Edições mais recentes confirmadas na listagem oficial:
- ed. 28 — 07/08/2026;
- ed. 29 — 08/09/2026.

### Tentativa de recuperação das edições recentes

- ed. 29: o PDF oficial foi identificado, mas o acesso automatizado retornou **cache miss**;
- ed. 28: o PDF oficial foi identificado, mas o mecanismo web recusou a leitura por **tamanho do conteúdo**;
- tentativa de download direto no ambiente de execução também não concluiu.

### Resultado

A existência da granularidade municipal é **confirmada pela descrição oficial da fonte**. A série municipal recente de São Borja, entretanto, ainda não foi extraída de forma reproduzível.

Nenhum valor municipal foi estimado, interpolado ou copiado de fonte secundária.

### Próximo passo operacional

Quando um dos PDFs recentes puder ser lido integralmente, registrar:
`edicao | periodo_referencia | indicador | setor/categoria | municipio | valor | unidade | fonte | nota_metodologica`

e testar São Borja antes de qualquer promoção.
