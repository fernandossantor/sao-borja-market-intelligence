# Validação do staging de `raw/new_files`

## Objetivo

Verificar se a camada local de staging preserva os contratos definidos, a proveniência das linhas, as decisões de exclusão registradas e as quantidades publicadas antes de qualquer integração com bases históricas ou promoção para a camada curada.

## Abrangência

A validação opera exclusivamente sobre:

```text
.data/staging/new_files/<snapshot_id>/
```

Ela não lê novamente os arquivos no Google Drive e não modifica a captura bruta.

## Verificações executadas

### Arquivos e contratos

- presença dos seis arquivos Parquet esperados;
- ausência ou registro de arquivos Parquet inesperados;
- presença e ordem das colunas de negócio e auditoria;
- separação das seis estruturas em contratos distintos.

### Proveniência

- preenchimento de origem, caminho, arquivo, planilha, linha, captura e hash;
- unicidade da chave formada por caminho, planilha e linha de origem;
- coerência entre o nome do arquivo e o caminho registrado;
- coerência entre o nível de governo e o dataset;
- correspondência do identificador da captura;
- formato válido de SHA-256;
- números de linha positivos e inteiros.

### Datas e medidas

- datas não nulas nos datasets temporalmente estruturados;
- datas interpretáveis;
- inexistência de datas posteriores à data da captura;
- medidas numéricas armazenadas como números ou `Decimal`;
- nenhuma imposição de positividade, porque estornos e ajustes podem existir.

### Duplicidades sinalizadas

- coerência entre identificador do grupo, quantidade de ocorrências, classe e status;
- contagem de linhas sinalizadas;
- contagem de grupos;
- cálculo das ocorrências excedentes além da primeira linha de cada grupo.

### Reconciliação do manifesto

Para cada arquivo de origem, a quantidade de linhas publicada no Parquet é comparada com `source_manifest.csv`. Arquivos excluídos do staging devem ter zero linhas publicadas.

Também são identificados caminhos presentes nos Parquets que não constem no manifesto.

### Reconciliação dos indicadores

Os valores de `staging_quality_summary.csv` são recalculados a partir dos Parquets e do manifesto. São comparados:

- tabelas e linhas de origem;
- arquivos e linhas excluídos;
- quantidade de datasets e linhas de staging;
- arquivos e linhas federais;
- linhas de ICMS preservadas;
- linhas de ICMS sinalizadas como repetidas.

## Saídas

```text
.data/audit/new_files/staging_validation/<snapshot_id>/
```

Arquivos:

- `dataset_validation_summary.csv`;
- `manifest_reconciliation.csv`;
- `quality_reconciliation.csv`;
- `validation_issues.csv`;
- `staging_validation_summary.csv`.

## Natureza dos resultados

### Dados observados

- arquivos, colunas e linhas presentes nos Parquets;
- valores de proveniência;
- manifesto e indicadores publicados pelo staging.

### Dados calculados

- faltas e divergências de contrato;
- reconciliações de linhas e indicadores;
- datas mínimas e máximas;
- contagens de duplicidades e inconsistências;
- totais de erros e advertências.

## Critério de aprovação

A validação somente retorna `status=ok` quando não existem erros. Colunas inesperadas ou alterações de ordem são registradas como advertências, pois podem representar evolução deliberada do contrato, mas precisam ser revisadas antes da promoção para a camada curada.

## Limitações

- a validação confirma coerência técnica e rastreabilidade, não a definição conceitual das variáveis;
- valores monetários não são comparados ainda com séries históricas existentes;
- registros repetidos de ICMS permanecem preservados;
- o staging ainda não é uma base canônica;
- a integração com `processed`, `warehouse` e Supabase permanece fora desta etapa.

## Execução

```bash
make validate-inbox-staging
```

Para substituir somente os relatórios locais de uma validação anterior:

```bash
python -m sbmi.inbox_staging_validation_cli --replace
```
