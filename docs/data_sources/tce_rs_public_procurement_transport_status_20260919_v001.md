# TCE-RS — compras públicas — estado das rotas oficiais — 19/09/2026

**Status:** exploratório — não canônico.  
**Objeto:** documentar as rotas oficiais para contratos e execução da despesa da Prefeitura Municipal de São Borja e separar falha de transporte de ausência de dados.

## Rotas confirmadas

### LicitaCon — Contratos Consolidado 2026

Fonte oficial: TCE-RS / Dados Abertos / LicitaCon.

Recurso anual confirmado:

`https://dados.tce.rs.gov.br/dados/licitacon/contrato/ano/2026.csv.zip`

O conjunto anual contém contratos dos órgãos jurisdicionados e inclui o campo `CD_ORGAO`, permitindo filtrar a Prefeitura Municipal de São Borja pelo código **58000**.

Finalidade no modelo: contrato, fornecedor, objeto e valor contratual.

### SIAPC — Despesa Orçamentária por Empenhos 2026

Fonte oficial: TCE-RS / Dados Abertos / SIAPC.

Rota por órgão documentada pelo TCE-RS:

`https://dados.tce.rs.gov.br/dados/municipal/empenhos/2026/58000.csv.zip`

O conjunto contém empenhos, liquidações e pagamentos, com identificação do credor por CPF/CNPJ.

Finalidade no modelo: pagamento ao credor como variável preferencial para a primeira rodada de saída financeira administrativa.

## Tentativas automatizadas

### SIAPC

Workflow: `.github/workflows/siapc-sao-borja-empenhos-2026.yml`  
Run: **35450165179**  
Resultado: **falha de transporte**.

O runner não conseguiu estabelecer conexão TCP/HTTPS com `dados.tce.rs.gov.br:443`; as tentativas expiraram após 30 segundos de conexão. Nenhum byte da base foi materializado.

### LicitaCon

Workflow: `.github/workflows/licitacon-sao-borja-procurement-2026.yml`  
Run: **35450307630**  
Resultado: **falha de transporte**.

Mesmo usando o recurso anual oficial confirmado, a conexão com `dados.tce.rs.gov.br:443` expirou antes de receber bytes.

## Interpretação

As falhas **não invalidam a fonte, o leiaute ou a existência dos dados**. Elas demonstram apenas bloqueio/indisponibilidade do host de arquivos para o ambiente do GitHub Actions nesta execução.

Portanto:

- a rota metodológica está fechada;
- a materialização dos bytes permanece pendente;
- nenhum percentual local/externo pode ser calculado enquanto os arquivos não forem obtidos;
- não é correto substituir a ausência do download por inferência a partir de contratos isolados, notícias, nomes de fornecedores ou valores agregados.

## Rota alternativa oficial

O Portal da Transparência da Prefeitura de São Borja, operado sobre plataforma DBSeller/e-Cidade, publica consulta de despesas por credor e informa atualização diária. A própria página “Origem dos Dados” informa que a despesa consultada apresenta valores empenhado, anulado, liquidado e pago com movimentação do exercício.

Essa rota será auditada como **fonte oficial municipal alternativa** para tentar materializar pagamento por credor, preservando o TCE-RS como fonte de referência/reconciliação.

## Critério de fechamento

A lacuna de compras públicas só será considerada fechada quando houver, para período explicitado:

1. CPF/CNPJ ou identificador inequívoco do credor;
2. valor de pagamento separado de empenho e liquidação;
3. classificação cadastral do CNPJ via RFB;
4. total elegível reconciliado;
5. documentação de local/external segundo regras explícitas;
6. preservação de CPF/outros casos em categoria separada, sem inferir localidade.

