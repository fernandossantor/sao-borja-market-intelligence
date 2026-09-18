# Preços Dinâmicos da Receita Estadual — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Auditar o produto Preços Dinâmicos da Receita Estadual do Rio Grande do Sul para avaliar sua incorporação ao SBMI como fonte regional de ambiente de preços, sem alterar qualquer base ou caderno consolidado.

## Fontes oficiais

- Painel: https://receitadados.sefaz.rs.gov.br/desenvolve-rs/precos-dinamicos-da-re/
- Nota Técnica CIET 01/2026: https://receitadoc.sefaz.rs.gov.br/media/m41pmsex/nt01_26-pre%C3%A7os-dinamicos-v20260302.pdf
- Boletins: https://receitadoc.sefaz.rs.gov.br/boletins/

## Achados observados — etapa 2A

### Natureza dos dados

O projeto coleta e divulga preços pagos em transações formalizadas pelas famílias gaúchas na aquisição de itens de consumo.

A fonte primária é a NFC-e emitida por estabelecimentos atacadistas e varejistas do Rio Grande do Sul.

### Cobertura e periodicidade

A NT CIET 01/2026 informa:

- coleta diária;
- caráter censitário das vendas formais a consumidor final acobertadas por NFC-e;
- inclusão de estabelecimentos do regime geral e do Simples Nacional;
- atualização diária do painel no dia seguinte à emissão da nota;
- publicação também em séries mensais e boletins mensais.

A base consultada recebe aproximadamente:
- 29,2 milhões de registros/dia;
- derivados de cerca de 6,6 milhões de NFC-e/dia;
- para os 80 alimentos selecionados, cerca de 12,8 milhões de registros de 3,6 milhões de NFC-e.

Esses números são os informados na NT CIET 01/2026 e devem ser tratados como referência metodológica do documento, não como contagem auditada pelo SBMI.

### Unidade analítica

A seleção atual contém:
- 80 produtos;
- 29 subgrupos;
- 12 grupos;
- cobertura de 98,84% da quantidade per capita total de alimentos consumida pelo indivíduo médio gaúcho segundo a POF/IBGE 2017/2018.

A unidade básica é o produto.

### Determinação do preço

O processamento oficial:
1. filtra por NCM de 8 dígitos;
2. aplica mineração de texto;
3. remove outliers pelo método de Tukey;
4. calcula a mediana das observações dentro do intervalo esperado.

Portanto, o indicador deve ser tratado como **preço mediano processado pela Receita Estadual**, não como preço médio simples nem como preço observado em um estabelecimento específico.

### Geografia

A Receita informa que o cruzamento da NFC-e com o Cadastro de Contribuintes permite associar os emitentes ao município de emissão.

Contudo, a publicação dos preços é agregada aos 28 COREDES para preservar precisão estatística.

Assim:

- Município: existe na base de origem, mas não é a granularidade pública publicada;
- COREDE: granularidade regional pública;
- Rio Grande do Sul: disponível.

A NT CIET 02/2026 confirma explicitamente:

**São Borja → COREDE Fronteira Oeste.**

Regra SBMI:
- nunca rotular um dado de Fronteira Oeste como “São Borja”;
- usar “COREDE Fronteira Oeste — região de referência de São Borja”.

### Âncoras históricas oficiais para validação

Foram localizados boletins oficiais indexados que permitem testar a consistência do recorte regional:

- julho/2024: PCA-RE da Fronteira Oeste = R$ 248,70;
- novembro/2024: PCA-RE da Fronteira Oeste = R$ 270,33.

Esses valores são apenas âncoras históricas de validação da extração. Não representam o estado corrente de 2026.

## Aplicações mercadológicas no SBMI

Potencial de uso:
- pressão regional de preços;
- sazonalidade;
- comparação Fronteira Oeste × RS;
- evolução de itens relevantes para bens essenciais;
- insumos de alimentação fora do lar;
- leitura do poder de compra em conjunto com renda e emprego.

Não usar diretamente para:
- afirmar preço praticado em São Borja;
- estimar volume de consumo municipal;
- inferir gasto municipal;
- medir market share de estabelecimentos.

## Estrutura proposta de tabela exploratória

`periodo | periodicidade | corede | grupo | subgrupo | produto | ncm | preco_mediano | unidade | variacao_mes | variacao_12m | fonte | status`

Status inicial: `exploratorio`.

## Próxima subetapa — 2B

Extrair uma série mensal reproduzível para **COREDE Fronteira Oeste** e **Rio Grande do Sul**, priorizando:

1. PCA-RE;
2. arroz;
3. feijão-preto;
4. leite;
5. pão francês;
6. carne bovina/cortes disponíveis;
7. frango;
8. ovos;
9. óleo de soja;
10. café;
11. frutas e hortaliças de maior peso.

A extração só será promovida se for possível documentar período, unidade, transformação e fonte oficial de cada observação.


## Extensão metodológica identificada — NT CIET 04/2026

A auditoria da página de boletins identificou a Nota Técnica CIET 04/2026, que amplia o projeto para **Preço da Cesta de Alimentos por Faixa de Renda (PCA-RE-r)** e **Inflação da Cesta de Alimentos por Faixa de Renda (ICA-RE-r)**.

### Faixas de renda

As classes são definidas em salários mínimos:

- r1: < 2 SM;
- r2: 2 a 3 SM;
- r3: 3 a 6 SM;
- r4: 6 a 10 SM;
- r5: 10 a 15 SM;
- r6: 15 a 25 SM;
- r7: > 25 SM.

### Fonte e ponderação

Mantém-se a mesma base NFC-e e o mesmo pré-processamento dos Preços Dinâmicos.

Os pesos por faixa de renda derivam da POF/IBGE 2017/2018, especialmente da Tabela 6972, com estrutura de despesas de alimentação no domicílio por classes de rendimento.

A NT publica matriz de pesos por produto e faixa de renda. Exemplos que mostram diferenças relevantes no padrão de consumo:

- arroz branco: peso de 16,268 em <2 SM e 26,355 em >25 SM;
- feijão-preto: 4,060 em <2 SM e 5,184 em >25 SM;
- pão francês: 9,256 em <2 SM e 9,954 em >25 SM;
- leite integral: 30,314 em <2 SM e 68,223 em >25 SM.

Esses valores são **ponderadores da metodologia**, não quantidades de compra observadas pelo SBMI.

### Fórmula

O PCA-RE-r é definido como soma ponderada dos preços mensais medianos:

`PCA(r,t) = Σ w(i,r) * P(i,t)`

O ICA-RE-r é divulgado como variações:
- mensal;
- acumulada em 12 meses;
- acumulada no ano.

### Periodicidade e geografia

A divulgação é mensal para itens, subgrupos, grupos e cesta.

A NT informa tempo médio de aproximadamente 16 dias entre o evento e a publicação dos resultados mensais.

A cobertura contempla todo o RS e os 28 COREDES, permitindo comparar inflação alimentar por faixa de renda e território.

### Valor para o SBMI

Este subproduto é potencialmente mais útil do que um único PCA-RE agregado para análises de:

- pressão do custo alimentar sobre famílias de baixa renda;
- diferenças de exposição à inflação alimentar;
- leitura de poder de compra por segmentos;
- comparação Fronteira Oeste × RS por faixa de renda.

Regra: não combinar automaticamente faixa de renda da POF com distribuição municipal de renda sem explicitar conceitos e períodos distintos.

## Subetapa 2B — estado parcial

A página oficial do Receita.doc expõe links diretos para boletins mensais de agosto/2024 a agosto/2026. Os PDFs mais recentes de 2026 foram identificados, porém o mecanismo automatizado de leitura não conseguiu recuperar seu conteúdo nesta sessão (cache miss/timeout).

Foi criado um **seed de validação**, apenas com observações que puderam ser verificadas em fontes oficiais acessíveis, para testar o esquema da futura série. Esse seed não constitui uma série completa nem dado canônico.

## Subetapa 2C — boletim agosto/2026 extraído

Foi recebido e auditado o boletim **Preços Dinâmicos — edição 25, agosto/2026**.

### Atualização metodológica do próprio boletim

O documento reafirma:
- referência à POF/IBGE 2017/2018, Tabela 2393;
- adoção da taxonomia grupo > subgrupo > produto;
- 80 produtos;
- 12 grupos;
- ponderação por consumo per capita da POF.

**Inconsistência documental a preservar:** o boletim de agosto/2026 informa **30 subgrupos**, enquanto a NT CIET 01/2026 anteriormente auditada registrava **29 subgrupos**. Não foi encontrada, nesta etapa, explicação documental para a mudança. Não harmonizar silenciosamente.

### Fronteira Oeste — PCA-RE agosto/2026

- valor: **R$ 284,19**;
- variação mensal: **+0,51%**;
- variação no ano: **+2,01%**;
- variação em 12 meses: **+3,22%**.

Rio Grande do Sul:
- R$ 298,61;
- +0,60% no mês;
- +2,54% no ano;
- +3,49% em 12 meses.

Cálculo SBMI:
`(284,19 / 298,61 - 1) × 100 = -4,83%`.

Assim, o nível do PCA-RE da Fronteira Oeste estava 4,83% abaixo da média estadual naquele mês.

### ICA-RE em 12 meses — Fronteira Oeste

- <2 SM: 2,23%;
- 2 a 3 SM: 1,94%;
- 3 a 6 SM: 2,26%;
- 6 a 10 SM: 2,73%;
- 10 a 15 SM: 2,64%;
- 15 a 25 SM: 3,84%;
- >25 SM: 4,29%;
- média: **3,23%**.

Média RS: **3,49%**.

Interpretação permitida: no agregado, a inflação alimentar regional em 12 meses estava 0,26 p.p. abaixo da média estadual, mas o resultado não é uniforme por faixa de renda.

### Hortaliças

Fronteira Oeste:
- R$ 5,58;
- -6,88% no mês;
- +6,31% no ano;
- +18,69% em 12 meses.

RS:
- R$ 6,50;
- -7,27% no mês;
- +16,28% no ano;
- +22,45% em 12 meses.

### Cebola

Fronteira Oeste:
- R$ 5,43;
- -13,10% no mês;
- +117,60% no ano;
- +101,93% em 12 meses.

RS:
- R$ 5,99;
- -11,80% no mês;
- +101,39% no ano;
- +102,89% em 12 meses.

### Arquivo estruturado

`docs/data_sources/precos_dinamicos_fronteira_oeste_agosto2026_v001.csv`

Regra territorial mantida: Fronteira Oeste é região de referência de São Borja, não preço municipal.
