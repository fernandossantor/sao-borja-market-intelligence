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
