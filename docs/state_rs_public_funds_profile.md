# Perfil agregado dos recursos públicos estaduais

O perfilador lê em fluxo os CSVs contidos no snapshot estadual imutável. Ele
publica somente nomes de colunas, hashes e contagens agregadas por recurso,
ano e correspondência territorial exata com São Borja.

Valores de CNPJ, credor, favorecido, beneficiário, ordenador, histórico,
objeto, justificativa, banco e agência não são persistidos. Nenhuma linha é
promovida para `staging`, `curated` ou `exports`.

Linhas cuja quantidade de campos difere do cabeçalho não são realinhadas por
heurística: elas são excluídas das contagens territorial e temporal e
registradas como `WARN` no relatório de validação.

A correspondência territorial normaliza caixa, acentos e espaços, mas exige
igualdade integral do nome municipal. Uma ocorrência nominal não comprova que
o gasto representa ingresso econômico no território.

O recurso `agreements_layout` apresenta estrutura tabular igual à das bases de
convênios. Sua função permanece metodologicamente ambígua até comparação de
conteúdo e metadados; o perfil não o reclassifica automaticamente.

Execução:

```bash
python -m sbmi.state_rs_public_funds_profile_cli
```
