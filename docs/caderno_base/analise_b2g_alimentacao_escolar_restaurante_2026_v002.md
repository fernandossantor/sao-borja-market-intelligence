# Alimentação escolar — contestabilidade B2G por canal institucional — São Borja — 2026 — v002

## 1. Objetivo

Aprofundar o canal de agricultura/agroindústria familiar da alimentação escolar e explicar por que ele não deve ser analisado com a mesma lógica competitiva dos distribuidores CNPJ.

Esta versão complementa a v001 e preserva a regra:

**contrato ≠ pagamento**.

## 2. Base contratual observada

O piso documental já auditado contém **19 contratos** de 2026 vinculados às Chamadas Públicas 01/2026 e 02/2026, somando:

**R$ 447.585,44 contratados**.

Cálculos sobre os 19 contratos:

- média: **R$ 23.557,13**;
- mediana: **R$ 31.923,50**;
- 7 contratos têm valor ≥ R$ 39.000,00;
- 6 contratos têm valor ≥ R$ 39.900,00;
- maior contrato observado: **R$ 40.000,00**.

Esses valores são contratuais e não devem ser somados aos R$ 869.843,54 pagos a CNPJ no CORE_PROCUREMENT.

## 3. Achado normativo: limite individual de R$ 40 mil

A Resolução CD/FNDE nº 4, de 26/02/2026, estabelece limite individual de comercialização de **R$ 40.000,00 por ano civil, por Entidade Executora e por CAF**.

Para fornecedores individuais e grupos informais, os contratos individuais devem respeitar esse teto.

### Interpretação

A concentração de vários contratos logo abaixo de R$ 40 mil é **compatível com um limite normativo explícito**, e não deve ser interpretada como evidência de escala ótima de produção ou de demanda espontaneamente concentrada nesse patamar.

O teto regula a escala institucional acessível por CAF individual.

## 4. Seleção: localidade é critério de prioridade

Nas regras vigentes do PNAE em 2026, após habilitação, a seleção dos projetos de venda por alimento/item prioriza sucessivamente:

1. localidade;
2. grupos prioritários;
3. produção orgânica/agroecológica;
4. forma de organização.

A hierarquia territorial começa pelo fornecedor local e avança para região geográfica imediata, intermediária, estado e país.

### Implicação

No canal agricultura familiar, **a localidade não é apenas uma variável de custo/frete; é também critério institucional de seleção**.

Isso muda a leitura de contestabilidade:

- no canal CNPJ/distribuidor, presença local precisa disputar preço, escala, logística e habilitação;
- no canal PNAE/CAF, o desenho institucional já cria preferência territorial, desde que o fornecedor esteja habilitado e tenha produto/escala compatíveis.

## 5. Preço: formação administrativa, não menor lance

Segundo a orientação FNDE vigente, o preço da agricultura familiar é formado pela Entidade Executora com pesquisa por alimento/item e deve considerar condições locais de fornecimento, incluindo:

- local de entrega;
- frequência;
- apresentação/beneficiamento;
- sazonalidade;
- disponibilidade de produção.

### Implicação

A variável `preço/frete` deve ser tratada como parte da **formação do preço de aquisição e da viabilidade logística**, não como simples diferença entre lance vencedor e segundo colocado.

## 6. Habilitação

Para fornecedor individual, a regra vigente exige, entre outros elementos:

- CPF;
- CAF Pessoa Física válida;
- projeto de venda;
- documentação higiênico-sanitária pertinente;
- declaração de produção própria.

Assim, a barreira B2G neste canal é diferente da de um supermercado/distribuidor convencional.

## 7. Arquitetura competitiva revisada

A alimentação escolar possui pelo menos dois circuitos que não devem ser agregados sem controle:

### A. Canal empresarial CNPJ

Pagamentos observados:
- R$ 869.843,54;
- presença local: R$ 327.021,02 = 37,60%;
- externo: R$ 542.822,52 = 62,40%.

Aqui a próxima unidade é grupo de produto × fornecedor × preço/volume/logística.

### B. Agricultura/agroindústria familiar

Piso documental:
- 19 contratos;
- R$ 447.585,44 contratados;
- limite individual regulatório de R$ 40 mil/CAF/ano/EEx;
- prioridade territorial na seleção;
- preço de referência formado pela Entidade Executora.

Aqui a próxima unidade é:
`fornecedor/CAF → localidade → produto → valor contratado → pagamento executado → entrega`.

## 8. O que não concluir

Ainda não é possível afirmar:

- que os R$ 447.585,44 foram pagos;
- que todos os 19 fornecedores são de São Borja;
- que o canal familiar capturou R$ 447.585,44 de renda local;
- que contratos próximos de R$ 40 mil indicam concentração econômica;
- que o percentual de 37,60% local no universo CNPJ representa a alimentação escolar total;
- que a preferência territorial garante contratação local em todos os itens.

## 9. Próxima ação dirigida

1. identificar município/localidade e CAF dos 19 fornecedores;
2. classificar cada contrato por grupo de alimento;
3. reconciliar empenho/liquidação/pagamento a CPF/PF;
4. medir contratação e execução por localidade;
5. identificar itens para os quais não houve oferta local;
6. comparar esses itens com o canal empresarial CNPJ;
7. só então calcular captura territorial da alimentação escolar.

## 10. Métricas a produzir

- valor contratado por fornecedor/CAF;
- valor efetivamente pago por fornecedor;
- participação local por canal;
- contratos no teto / próximos do teto;
- grupos de alimento por localidade;
- frequência e local de entrega;
- preço unitário de referência;
- diferença entre quantidade contratada e executada.

## 11. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`;
- valores contratuais permanecem separados de pagamentos.
