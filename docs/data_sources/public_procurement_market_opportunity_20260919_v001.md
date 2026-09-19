# PMSB — compras/contratações e sinais de oportunidade territorial — v001

**Status:** exploratório — não canônico.  
**Período dos pagamentos:** 01/01/2026 a 18/09/2026.  
**Fonte de pagamentos:** Portal da Transparência da Prefeitura de São Borja.  
**Fonte cadastral:** Receita Federal do Brasil — CNPJ, competência 2026-08; bytes transportados por espelho nesta execução.  
**Universo-base:** CORE_PROCUREMENT = R$ 72.039.491,18.

## 1. Leitura principal

A evidência não sustenta uma formulação simples de que “as compras públicas saem de São Borja”.

No núcleo de rubricas compatíveis com aquisição/contratação:

- **60,73%** foram pagos a CNPJ ativo em São Borja;
- **74,87%** foram pagos a CNPJ local ou a raiz empresarial com estabelecimento ativo no município;
- **25,13%** foram pagos a CNPJs sem footprint ativo local.

Entretanto, o agregado é fortemente influenciado por um arranjo institucional de saúde: a **Fundação Ivan Goulart** respondeu por R$ 28.342.657,23, ou **39,34%** do core.

Sem esse credor, a presença local ampliada cai para **58,57%** e a exposição a credores sem footprint local sobe para **41,43%**.

A conclusão adequada é, portanto, de **heterogeneidade territorial da contratação pública**, e não de retenção alta ou vazamento alto de forma uniforme.

## 2. O divisor central é o tipo de aquisição

### Serviços PJ genéricos

As duas rubricas de serviços PJ genéricos somam R$ 51,041 milhões.

Presença local ativa/ampliada:
- com Fundação Ivan Goulart: **91,22%**;
- sensibilidade sem Fundação: **80,27%**.

Logo, mesmo controlando o maior caso institucional, os serviços genéricos permanecem majoritariamente ancorados em fornecedores com presença local de primeira ordem.

### Bens, materiais e equipamentos

Material de consumo + bens/serviços para distribuição gratuita + equipamentos e material permanente somam **R$ 16,763 milhões**.

- presença local ativa/ampliada: **25,90%**;
- credores sem footprint ativo local: **74,09%**.

Este é o sinal mais forte de exposição externa observado no core.

A interpretação permitida é que a Prefeitura compra uma parcela relevante desses itens de fornecedores juridicamente externos e sem estabelecimento ativo da mesma raiz no município.

Não é permitido concluir, sem dados adicionais, que 74,09% “sai definitivamente” da economia local nem que toda essa demanda seria substituível por oferta local.

### Obras e instalações

R$ 2,857 milhões pagos.

- presença local/ampliada: **91,75%**;
- externos sem footprint local: **8,25%**.

A primeira rodada da execução de obras está fortemente associada a empresas locais ou grupos com footprint local.

Isso não informa a origem dos materiais, máquinas, financiamento ou subcontratações.

### TIC, consultoria e passagens

Somadas, essas três categorias representam R$ 1,379 milhão.

- presença local/ampliada: **29,76%**;
- externos sem footprint local: **70,24%**.

Separadamente:
- TIC: **66,37%** externos;
- consultoria: **89,74%** externos;
- passagens/locomoção: **85,87%** externos.

O conjunto é compatível com maior contestabilidade extralocal em serviços especializados, digitais, de rede ou de escala.

## 3. Finalidade orçamentária

O core está concentrado em poucas funções:

- Saúde: R$ 39,520 milhões = **54,86%** do core;
- Urbanismo: R$ 12,309 milhões = **17,09%**;
- Educação: R$ 7,704 milhões = **10,69%**;
- Administração: R$ 6,234 milhões = **8,65%**;
- Assistência Social: R$ 2,439 milhões = **3,39%**.

Na Saúde, a presença local ampliada é **81,20%**, mas a Fundação Ivan Goulart responde por **71,72%** de todo o core da função. Retirado esse caso, a presença local ampliada da Saúde cai para aproximadamente **33,51%**, enquanto a exposição externa sobe para **66,49%**.

Isto revela uma estrutura bifurcada:
- prestação institucional/local de serviços de saúde fortemente ancorada;
- aquisições e serviços complementares com exposição externa elevada.

Urbanismo apresenta **83,41%** de presença local ampliada, porém apenas **25,98%** em CNPJ local estrito, mostrando a importância de empresas externas com footprint operacional no município.

Educação apresenta **67,36%** de presença local ampliada; Administração está praticamente dividida em 50/50; Assistência Social possui **53,49%** de exposição externa; Transporte, embora de menor volume, apresenta **87,91%** de exposição externa.

## 4. Geografia da parcela externa

Dos R$ 18,103 milhões pagos a credores sem footprint ativo local:

- **60,87%** estão sediados em outros municípios do Rio Grande do Sul;
- **39,13%** estão sediados em outras UFs.

Assim, a principal competição pelo fornecimento público é **intermunicipal dentro do próprio RS**, e não exclusivamente interestadual.

Os maiores polos cadastrais externos são Porto Alegre, Curitiba, Brasília, Pinhalzinho/SC e Santo Antônio das Missões.

## 5. Implicação mercadológica

Os dados permitem substituir a hipótese genérica “o poder público injeta recursos, mas compra fora” por formulação mais precisa:

> **A capacidade de retenção da primeira rodada do gasto público municipal depende fortemente da natureza da compra. Serviços presenciais e obras apresentam maior ancoragem local; bens padronizados, materiais, equipamentos e parte dos serviços especializados apresentam exposição externa muito superior.**

Isto cria uma agenda concreta para inteligência de mercado:

- identificar, entre os R$ 12,420 milhões externos em bens/materiais/equipamentos, quais itens possuem oferta local potencialmente competitiva;
- separar ausência efetiva de fornecedor local de perda por preço, escala, habilitação, logística ou desenho da compra;
- mapear TIC e serviços profissionais em que existe demanda pública recorrente, mas baixa captura municipal;
- medir cadeia subsequente das grandes contratações locais para verificar se a primeira rodada local gera compras e trabalho também locais.

Esses itens são **hipóteses de oportunidade**, não recomendações automáticas de substituição de fornecedor.

## 6. Controles

- CORE_PROCUREMENT é classificação econômica por rubrica, não identificação jurídica perfeita de contrato/licitação;
- presença local da raiz não prova execução pela filial local;
- CNPJ local não prova origem local de insumos;
- CNPJ externo não equivale a vazamento integral;
- valores de 2026 cobrem apenas 01/01 a 18/09 e não incluem Restos a Pagar segundo o Portal;
- a camada RFB permanece exploratória até reconciliação com o host oficial/hash.

