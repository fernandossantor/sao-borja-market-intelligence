# Auditoria de `raw/new_files`

## Objetivo

Avaliar a caixa de entrada `raw/new_files` sem mover, excluir, renomear ou baixar os arquivos do Google Drive.

A primeira etapa usa exclusivamente os metadados registrados no inventário local da API do Drive.

## Classificações

- `UNIQUE_BY_SHA256`: o SHA-256 aparece uma única vez no inventário completo. Isso indica unicidade física observada, não unicidade conceitual.
- `MISSING_SHA256`: a API não forneceu SHA-256 para o arquivo.
- `EXACT_DUPLICATE_OUTSIDE_INBOX`: o mesmo SHA-256 aparece dentro de `raw/new_files` e em outra parte da árvore.
- `EXACT_DUPLICATE_WITHIN_INBOX`: o mesmo SHA-256 aparece mais de uma vez dentro de `raw/new_files`, sem correspondência fora dela.

Nenhuma classificação autoriza exclusão automática.

## Execução

```bash
make gdrive-audit-inbox
```

O comando lê:

```text
.data/manifests/google_drive_inventory.csv
```

E grava localmente:

```text
.data/audit/new_files/new_files_summary.csv
.data/audit/new_files/new_files_by_source.csv
.data/audit/new_files/new_files_file_classification.csv
```

Esses arquivos permanecem fora do Git.

## Interpretação

A igualdade de SHA-256 comprova igualdade física do conteúdo binário observado. Ela não determina:

- qual cópia deve ser preservada;
- se nomes e localizações têm função documental distinta;
- se há sobreposição parcial entre planilhas diferentes;
- se duas bases cobrem períodos, estágios orçamentários ou conceitos metodológicos distintos.

Arquivos classificados como `UNIQUE_BY_SHA256` ainda podem ser duplicados conceituais ou versões alternativas. Essa avaliação exigirá inspeção de esquema, período, fonte, unidade e abrangência geográfica em uma etapa posterior.
