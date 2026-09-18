# NT CIET 05/2026 - recuperação e auditoria de acesso

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório - não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objeto

Registrar de forma reproduzível o esforço de recuperação e auditoria da **NOTA TÉCNICA CIET 05/2026 - RADAR DE MERCADO DA RECEITA ESTADUAL**, antes de incorporar qualquer detalhe metodológico ao SBMI.

## Identificação oficial confirmada

Fonte: Receita.doc / Receita Estadual do Rio Grande do Sul.

- título: **NOTA TÉCNICA CIET 05/2026 - RADAR DE MERCADO DA RECEITA ESTADUAL**;
- publicação: **30/06/2026**;
- URL oficial: https://receitadoc.sefaz.rs.gov.br/media/rhwdpvaz/nota_tecnica_radar_mercado_v1.pdf;
- página de listagem: https://receitadoc.sefaz.rs.gov.br/boletins/.

A página oficial de Boletins/Notas Técnicas foi recuperada e lista a NT CIET 05/2026 com a data acima.

## Resultado da recuperação integral em 18/09/2026

**O PDF integral não foi recuperado nesta sessão.**

Tentativas efetuadas:
- abertura direta do URL oficial do PDF;
- acesso pelo link da página oficial Receita.doc;
- busca pelo título exato e pelo nome do arquivo;
- tentativa de download direto do arquivo;
- busca no Drive do projeto;
- verificação do painel público do Radar no Receita Dados.

O servidor do Receita.doc retornou timeout/cache para o PDF. O painel do Radar, por sua vez, é incorporado via Power BI e carrega seu conteúdo internamente no cliente, sem exposição textual confiável das páginas e filtros pelo mecanismo utilizado nesta auditoria.

## Regra de não inferência

Até que o PDF integral seja efetivamente lido:
- não atribuir à NT 05/2026 fórmula, universo, definição de demanda, regras de sigilo, filtros, periodicidade específica de cada indicador ou tratamento de NCM que não estejam verificáveis em fonte pública independente;
- não confundir a divulgação institucional do Radar com o conteúdo integral da Nota Técnica;
- não preencher campos quantitativos do piloto do arroz por aproximação.

## Evidência institucional verificável que corrobora o escopo, mas não substitui a NT

A página oficial do Radar no Receita Dados identifica o produto como parte do Desenvolve-RS e o disponibiliza em painel Power BI.

Divulgação institucional da versão ampliada, lançada em 30/06/2026, informa que o Radar:
- utiliza dados da NF-e;
- trabalha com operações fiscais do Estado;
- permite examinar consumidores, concorrentes e composição de mercado;
- distingue produção local, compras de outras UFs e importações;
- mapeia lacunas de atendimento da demanda pela produção local.

Fonte institucional republicada pela Associação Gaúcha de Municípios:
https://agm.org.br/com-base-em-dados-fiscais-governo-do-estado-lanca-painel-que-identifica-lacunas-de-producao-e-oportunidades-para-investir-no-rs/

Essa evidência sustenta apenas o **escopo público divulgado** do Radar, não sua metodologia completa.

## Fallback oficial compatível para a camada estadual do arroz

Enquanto os valores internos do Radar por NCM permanecerem inacessíveis, foi identificado um fallback oficial de comércio exterior produzido pelo **Departamento de Economia e Estatística - DEE/SPGG-RS**, com dados brutos do **Comex Stat/MDIC**.

### 3º trimestre de 2024 - NCMs do piloto encontrados na NT DEE 102

Fonte:
https://dee.rs.gov.br/upload/arquivos/202502/18160426-nt-dee-102-indicadores-do-agronegocio-do-rs-exportacoes-e-emprego-formal-no-3-trimestre-de-2024.pdf

Na Tabela A.3, geografia Rio Grande do Sul, período 3º trimestre de 2024:

- NCM **10064000 - Arroz quebrado**: US$ 65.459.780 FOB; participação de 1,4% nas exportações do agronegócio; variação interanual do valor +73,7%; quantidade +49,3%; preço +16,5%.
- NCM **10063021 - Arroz semibranqueado ou branqueado**: US$ 35.360.813 FOB; participação de 0,8%; variação do valor +15,7%; quantidade -6,8%; preço +23,1%.
- NCM **10063011 - Arroz semibranqueado ou branqueado**: US$ 16.412.640 FOB; participação de 0,4%; variação do valor +68,1%; quantidade +39,9%; preço +17,8%.

**Natureza:** DADOS OBSERVADOS em publicação oficial, cuja fonte bruta é o Comex Stat/MDIC.

**Limitação:** esses valores são **exportações**, não demanda interna do RS, não produção vendida dentro do Estado, não entradas de outras UFs e não market share do Radar.

### Contexto agregado mais recente - 2º trimestre de 2026

Em notícia oficial do Governo do RS sobre a NT DEE 135, o arroz apresentou **variação de +14,8% no valor exportado**, com **acréscimo de US$ 13,6 milhões** frente ao segundo trimestre de 2025.

Fonte:
https://estado.rs.gov.br/divulgada-nota-tecnica-sobre-as-exportacoes-do-agronegocio-do-rs-no-segundo-trimestre-de-2026

**Natureza:** DADO OBSERVADO agregado da cadeia do arroz.

**Limitação:** não há desagregação por NCM no texto público consultado; por isso o dado não será distribuído entre os sete NCMs do piloto.

## Decisão de preenchimento

Os campos do arquivo `radar_piloto_arroz_ncm_v001.csv` relativos a **demanda RS, produção interna, entradas de outras UFs, importações, dependência externa e market share** permanecem sem preenchimento.

Os dados de exportação oficiais acima são preservados em arquivo separado, explicitamente classificado como **fallback complementar - não Radar**.

## Arquivo estruturado associado

`docs/data_sources/arroz_ncm_estado_fallback_oficial_v001.csv`

## Próximo passo

1. recuperar os bytes integrais da NT CIET 05/2026 por canal estável;
2. auditar página a página conceitos, fórmulas, universo, período, unidade, geografia, filtros e limitações;
3. só então preencher os campos do Radar que correspondam exatamente aos conceitos documentados;
4. manter o fallback de exportações separado, sem substituição semântica da demanda/market share internos.

## Atualização posterior — PDF integral recebido e auditado em 18/09/2026

O estado anterior deste arquivo, que registrava impossibilidade técnica de leitura integral, foi **superado** após o recebimento direto do PDF oficial da NT CIET 05/2026.

Arquivo auditado:
`nota_tecnica_radar_mercado_v1.pdf`

### Achados metodológicos confirmados

1. **Fontes primárias**
   - NFe como base principal;
   - MDIC/Siscomex como complemento para rastrear países de destino/origem no comércio exterior.

2. **Cobertura tributária**
   - Regime Geral;
   - Simples Nacional.

3. **Granularidade**
   - Setor industrial;
   - NCM de 8 dígitos;
   - Categorias agregadas de NCM.

4. **Tempestividade**
   - atualização mensal;
   - mês imediatamente anterior disponível nos primeiros dias úteis.

5. **Página Oportunidades**
   - usa apenas CFOPs de operações efetivas;
   - janela LTM de 12 meses, comparada aos 12 meses anteriores;
   - valores corrigidos pelo D-ICMS;
   - Part. RS = INT / (INT + OUF + EXT);
   - dependência crítica: Part. RS < 5%;
   - dependência alta: 5% a 15%;
   - dependência média: 15% a 30%;
   - volume financeiro saindo do RS = OUF + EXT.

6. **Mercado Nacional**
   - Consumidores: estados que compram da indústria do RS;
   - Fornecedores: estados que vendem produtos ao RS, por NCM/Categoria;
   - Concorrentes: estados que disputam o mercado gaúcho com a produção local;
   - exterior excluído dessa página.

7. **Competitividade RS**
   - análise exclusivamente setorial;
   - portfólio Top 90% das NCMs que representam as maiores saídas do setor;
   - valores mensais por INT/OUF/EXT em 24 meses;
   - market share móvel de 12 meses.

8. **Perfil de Vendas**
   - agregação por Produto/Categoria ou Setor;
   - destino INT/OUF/EXT;
   - detalhamento de UFs;
   - países via Siscomex.

9. **Composição de Mercado**
   - origem do consumo do RS em INT/OUF/EXT;
   - visão por Setor ou NCM;
   - detalhamento de UFs e países.

10. **Dados Abertos**
    - seis bases em CSV:
      1. Saídas por Setor;
      2. Exportações por NCM;
      3. Composição de Mercado;
      4. Importações por NCM;
      5. Portfólio de NCMs por Setor;
      6. Categorias de Produtos.

### Consequência metodológica para o SBMI

A estratégia de extração deve mudar de **raspagem do Power BI** para **ingestão dos CSVs da página Dados Abertos**, quando os arquivos forem acessíveis.

A evidência municipal encontrada em material histórico de 2023 permanece registrada apenas como histórica. A NT 05/2026 não documenta município como geografia de nenhuma das páginas correntes.

### Artefato derivado

Foi criado:
`docs/data_sources/radar_nt_ciet_05_2026_dicionario_v001.csv`

com a tradução estruturada de páginas, indicadores, fórmulas, filtros, geografia, unidade, atualização e limitações.
