# Inventário HEAD das despesas estaduais

O inventário consulta os metadados públicos da CAGE no CKAN do Estado do RS e
executa somente requisições HTTP `HEAD` para os arquivos mensais de despesas
entre 2012 e 2026.

São registrados status HTTP, redirecionamentos, tipo de conteúdo e
`Content-Length`. Nenhum corpo de ZIP ou CSV é baixado. Redirecionamentos são
aceitos somente quando permanecem no domínio `dados.rs.gov.br`.

Ausência de `Content-Length`, resposta não 2xx e falha de `HEAD` são
preservadas como limitações; o pipeline não tenta corrigir isso com `GET`.
Nomes e URLs catalográficos não são usados como prova de conteúdo.

Execução:

```bash
python -m sbmi.state_rs_expense_head_inventory_cli
```
