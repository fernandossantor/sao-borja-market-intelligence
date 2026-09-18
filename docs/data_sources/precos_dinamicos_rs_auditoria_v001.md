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
