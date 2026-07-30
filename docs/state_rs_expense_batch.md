# Lote mensal de despesas estaduais

O pipeline usa o inventário `HEAD` como contrato de URLs e tamanhos. O lote
inicial contém janeiro a abril de 2026, totalizando 51.899.110 bytes
compactados e limitado a 60 MB.

Cada arquivo é baixado em diretório parcial, validado como ZIP e lido em
fluxo. O CSV não é extraído para disco. Divergência de tamanho, domínio,
esquema, ano, mês ou valor numérico impede a publicação.

O staging contém somente registros com correspondência territorial exata para
São Borja e exclui CNPJ, favorecido, beneficiário, histórico, objeto, banco,
agência e demais campos pessoais ou textuais livres.

Fase, tipo e valor do gasto permanecem separados. O pipeline não calcula um
total financeiro canônico e não promove dados para `curated` ou `exports`.

Execução:

```bash
python -m sbmi.state_rs_expense_batch_cli
```
