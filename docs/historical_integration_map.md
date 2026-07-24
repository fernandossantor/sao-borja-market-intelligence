# Mapeamento de integração com o acervo histórico

## Objetivo

Relacionar as 33 fontes ativas do staging de `raw/new_files` com arquivos existentes em `processed`, `warehouse` e `exports`, usando somente metadados e nomes de arquivos antes de qualquer download seletivo ou comparação de conteúdo.

## Escopo

Entradas locais:

- `.data/manifests/google_drive_inventory.csv`;
- `.data/staging/new_files/<snapshot_id>/source_manifest.csv`.

Escopos históricos avaliados por padrão:

- `processed`;
- `warehouse`;
- `exports`.

A rotina ignora pastas e restringe a comparação lexical a extensões potencialmente tabulares ou de banco de dados. Arquivos de outros formatos continuam contabilizados no resumo do escopo, mas não geram candidatos por nome.

## Classificações

### `EXACT_SHA256`

O arquivo ativo e o arquivo histórico possuem o mesmo SHA-256 informado pelo Google Drive. Essa igualdade indica identidade binária, não preferência metodológica nem autorização de exclusão.

### `EXACT_NORMALIZED_NAME`

Os nomes sem extensão são iguais após normalização de caixa, acentos, separadores e sufixos típicos de cópia. Essa igualdade não prova igualdade de conteúdo.

### `STRONG_NAME_MATCH`

Há elevada similaridade lexical segundo sequência de caracteres e conjuntos de palavras. É uma estimativa para priorização de inspeção.

### `POSSIBLE_NAME_MATCH`

Há indício lexical moderado. A relação pode ser temática, histórica ou meramente nominal.

## Medidas calculadas

- Jaccard entre palavras dos nomes;
- contenção do menor conjunto de palavras;
- similaridade de sequência;
- escore máximo derivado dessas medidas;
- posição do candidato para cada fonte ativa.

Essas medidas não permitem concluir duplicidade, complementaridade ou conflito. Tais classificações exigem inspeção estrutural e de conteúdo.

## Saídas

```text
.data/audit/historical_integration_map/<snapshot_id>/
```

Arquivos:

- `historical_scope_summary.csv`: quantidade, volume e extensões por escopo;
- `staging_source_mapping_summary.csv`: situação de cada fonte ativa;
- `historical_integration_candidates.csv`: até cinco candidatos por fonte, por padrão;
- `historical_integration_summary.csv`: indicadores agregados com natureza observada ou calculada.

## Segurança e governança

- nenhum arquivo histórico é baixado nesta etapa;
- nenhum arquivo bruto, de staging ou do Google Drive é alterado;
- não há promoção para `curated`;
- os candidatos devem orientar uma captura seletiva posterior;
- fontes sem candidato nominal não são tratadas como conteúdo necessariamente novo.

## Execução

```bash
make map-historical-integration
```

Para substituir um relatório local já existente:

```bash
python -m sbmi.historical_integration_map_cli --replace
```
