# BET Comércio Exterior — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Fonte oficial

https://receitadoc.sefaz.rs.gov.br/boletins/

## Descrição oficial

A Receita Estadual define o BET Comércio Exterior como publicação mensal direcionada a gestores públicos, pesquisadores e profissionais de setores econômicos.

A página institucional informa que o periódico apresenta:
- níveis de importações;
- níveis de exportações;
- principais produtos comercializados;
- volumes exportados aos principais blocos comerciais internacionais;
- efeitos de novas parcerias econômicas;
- efeitos de tarifas aplicadas aos exportadores do RS.

## Periodicidade observada

Edições publicadas em 2026:
- Ed. 01 — fev/26;
- Ed. 02 — mar/26;
- Ed. 03 — abr/26;
- Ed. 04 — mai/26;
- Ed. 05 — jun/26;
- Ed. 06 — jul/26.

Periodicidade declarada: mensal.

## Geografia

A descrição pública confirma RS, blocos e parceiros internacionais.

**Ainda não está confirmada abertura municipal para São Borja ou COREDE.**

## Aplicações potenciais ao SBMI

- contexto do ambiente externo para cadeias exportadoras locais;
- produtos relevantes para a pauta estadual;
- mercados de destino;
- exposição a tarifas e mudanças comerciais;
- comparação com setores produtivos presentes em São Borja.

## Limitação e próxima etapa

O PDF da edição 06 foi identificado na página oficial, mas não pôde ser recuperado pelo mecanismo automatizado nesta sessão.

A auditoria de conteúdo fica aberta até leitura verificável da publicação. Não serão inferidos produtos, países ou valores específicos sem o documento.

## Edição 07 — agosto/2026 — conteúdo auditado

Foi recebido e auditado o **BET Comércio Exterior — edição 07**, datado de 17/09/2026, com resultados consolidados de agosto/2026.

Janela principal:
**01/09/2025 a 31/08/2026**, comparada a **01/09/2024 a 31/08/2025**.

### Granularidade regional confirmada

A edição contém tabela por COREDE, resolvendo a pendência anterior.

Fronteira Oeste:
- exportações: **US$ 322,2 milhões**;
- variação das exportações: **+27,43%**;
- total de vendas: **US$ 5.673,1 milhões**;
- variação do total de vendas: **+12,84%**.

RS — total da tabela de COREDES:
- exportações: US$ 24.044,9 milhões;
- variação: +2,89%;
- vendas: US$ 242.300,2 milhões;
- variação: +14,24%.

### Cálculo exploratório — intensidade exportadora

Fronteira Oeste:
`322,2 / 5.673,1 × 100 = 5,68%`.

RS:
`24.044,9 / 242.300,2 × 100 = 9,92%`.

**Natureza:** dado calculado pelo SBMI, não indicador oficial do boletim.

Interpretação: as exportações da Fronteira Oeste cresceram muito acima do agregado regional do RS no período, mas sua participação nas vendas totais permaneceu menor que a razão estadual calculada.

### Contexto para a cadeia do arroz

Categoria ampla **Cereais e Grãos (exceto soja)**:
- exportações: **US$ 1.278,5 milhões**, +7,3%;
- importações: **US$ 227,2 milhões**, -32,5%.

Limitação:
a categoria inclui arroz e outros cereais; não pode ser usada como valor específico da cadeia do arroz.

Indústria:
- AGRO: US$ 12.031,6 milhões exportados; +18,98%;
- ALIMENTOS: US$ 982,4 milhões; +9,81%.

Esses recortes são contextuais e não substituem os sete NCMs do piloto.

### Arquivo estruturado

`docs/data_sources/bet_comex_ed07_fronteira_oeste_v001.csv`
