# Minuta — solicitação à Receita Estadual — DFe agregada para dimensão de mercado — v001

**Data:** 2026-09-26  
**Destinatário inicial recomendado:** Receita Estadual do RS — Receita Dados / Fale Conosco  
**Canal alternativo/formal:** SIC/LAI — pedido de informação ou abertura de dados  
**Projeto:** São Borja — Inteligência Mercadológica  
**Geografia:** São Borja/RS — IBGE 4318002

## Assunto sugerido

**Disponibilidade de dados agregados de DFe por município e CNAE — São Borja/RS**

## Texto sugerido

Prezados(as),

Estou desenvolvendo um projeto acadêmico de inteligência mercadológica territorial voltado ao município de São Borja/RS e gostaria de verificar a disponibilidade de um recorte **exclusivamente agregado** dos Documentos Fiscais Eletrônicos já mantidos pela Receita Estadual.

O portal Receita Dados disponibiliza publicamente séries por município e, separadamente, séries por setor/CNAE no nível de COREDE. Para fins de dimensionamento de mercados locais, a necessidade mínima é combinar essas duas dimensões, sem qualquer identificação de contribuinte ou consumidor.

Gostaria de saber se existe, em base/visão já sistematizada, possibilidade de fornecimento da seguinte tabela para São Borja/RS (IBGE 4318002), de janeiro de 2023 até a última competência fechada disponível:

`ano-mês | município | modelo DFe | CNAE classe/grupo/divisão | quantidade de documentos | valor total dos documentos | quantidade de contribuintes da célula | indicador de supressão`.

Modelos prioritários:
- NFC-e, preservada separadamente;
- NF-e, preservada separadamente.

A **classe CNAE** é preferencial. Caso a regra de sigilo não permita essa granularidade, grupo ou divisão são adequados. Aceito integralmente a política estatística de sigilo utilizada pela Receita, inclusive:
- supressão de células com poucos contribuintes;
- agregação ao nível CNAE superior;
- arredondamento;
- omissão de categorias residuais.

Não são solicitados CNPJ, CPF, razão social, chave de documento ou qualquer microdado fiscal.

Se já existir visão agregada por **NCM**, seria também útil saber se é possível fornecer:

`ano-mês | município | modelo DFe | NCM8/NCM4 | valor | quantidade | número de contribuintes | indicador de supressão`.

Caso uma extração integral por NCM represente volume excessivo, o projeto dispõe de uma lista previamente auditada de **3.424 NCM8 prioritários**, organizada em 43 grupos de produto relacionados aos mercados estudados, que pode ser encaminhada como filtro.

Solicito também, se possível, os metadados mínimos necessários para interpretação:
- CFOPs considerados em NF-e;
- tratamento de cancelamentos, devoluções e notas de ajuste;
- regra territorial utilizada;
- regra de sigilo/supressão;
- eventual mudança metodológica no período.

Caso esse recorte não exista de forma sistematizada ou não possa ser fornecido, uma resposta indicando **quais dimensões agregadas estão disponíveis** e a limitação técnica/metodológica já será suficiente para orientar o projeto.

A finalidade é exclusivamente acadêmica e analítica, sem identificação de empresas ou contribuintes.

Agradeço desde já pela orientação.

Atenciosamente,

[Nome]  
[Instituição / vínculo acadêmico]  
[E-mail]  
[Telefone, se desejado]

## Anexos recomendados

1. especificação técnica:
   `receita_dfe_especificacao_extracao_municipio_setor_v001_20260926.md`;
2. se solicitado, pacote NCM prioritário:
   `radar_ncm_priority_request.csv`;
3. nota metodológica explicando que não se pretende obter microdados.

## Observação sobre canal

Para uma primeira consulta de viabilidade, utilizar o Fale Conosco / Receita Dados.

Se a resposta indicar necessidade de pedido formal, o texto pode ser reaproveitado no SIC/LAI como pedido de acesso/abertura de dados, enfatizando que se busca **exportação de visão agregada já existente**, se disponível, e não produção de análise individualizada.
