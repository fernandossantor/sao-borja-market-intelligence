# Reconciliação e staging estadual

O pipeline compara em memória os registros de `agreements_layout` e
`agreements_expense` por conteúdo integral e por identidade estável. Somente
contagens agregadas são publicadas; os hashes usados na comparação não são
persistidos.

Por prudência, `agreements_layout` permanece em quarentena mesmo quando houver
sobreposição mensurável. O staging recebe apenas correspondências territoriais
exatas de `agreements_expense`, `partnerships` e despesas estaduais válidas.

O produto exclui CNPJ, credor, favorecido, beneficiário, ordenador, histórico,
objeto, justificativa, banco e agência. Valores permanecem em colunas
semanticamente separadas e não são somados entre famílias.

Linhas estruturalmente irregulares continuam em quarentena. O staging não é
promovido automaticamente para `curated` ou `exports`.

Execução:

```bash
python -m sbmi.state_rs_public_funds_staging_cli
```
