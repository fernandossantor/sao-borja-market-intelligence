# Staging auditado de `raw/new_files`

## Objetivo

Construir uma camada derivada, local e reproduzível a partir da captura validada de `raw/new_files`, sem modificar os arquivos brutos e sem realizar operações no Google Drive.

## Decisões aplicadas

### Bases federais

As 29 planilhas federais possuem o mesmo contrato de 12 colunas. A auditoria identificou um par com conteúdo normalizado idêntico:

- `COFINANCIAMENTO DA PROTECAO SOCIAL BASICA.xlsx`;
- `COFINANCIAMENTO DA PROTECAO SOCIAL BASICA(1).xlsx`.

A camada de staging inclui o arquivo sem sufixo e exclui apenas da camada derivada o arquivo com `(1)`, com base na heurística `COPY_SUFFIX_HEURISTIC`. Ambos permanecem preservados na captura bruta.

### Base estadual de ICMS

As 3.818 linhas são mantidas integralmente. Os 10 grupos de repetição, correspondentes a 19 ocorrências excedentes, recebem campos de sinalização e permanecem com status de validação pendente. Não ocorre deduplicação automática.

### Demais bases

As demais bases estaduais e municipais permanecem separadas porque possuem estruturas, granularidades e conceitos distintos.

## Contratos produzidos

- `federal_transferencias`;
- `estadual_icms`;
- `estadual_transferencias`;
- `municipal_despesas_instituicao`;
- `municipal_despesas_elemento`;
- `municipal_receita_elemento`.

Cada contrato exige correspondência exata dos cabeçalhos normalizados. Estruturas desconhecidas interrompem a construção do staging.

## Transformações

- datas são convertidas apenas pelos formatos explícitos já validados na revisão de anomalias;
- medidas numéricas são convertidas para representação decimal sem arredondamento imposto;
- códigos e descrições são preservados como valores observados;
- cada linha recebe proveniência de arquivo, planilha, linha de origem e captura;
- cada linha recebe SHA-256 calculado sobre os valores observados;
- o ano extraído do nome do arquivo é registrado separadamente como metadado derivado, sem substituir períodos internos.

## Campos de auditoria

Entre os campos adicionais estão:

- `_source_level`;
- `_source_path`;
- `_source_file`;
- `_source_sheet`;
- `_source_row`;
- `_snapshot_id`;
- `_reference_year_filename`;
- `_row_sha256`;
- `_duplicate_group_id`;
- `_duplicate_occurrence_count`;
- `_duplicate_class`;
- `_duplicate_review_status`.

## Saídas

```text
.data/staging/new_files/<snapshot_id>/
```

O diretório contém um arquivo Parquet por contrato, além de:

- `source_manifest.csv`;
- `staging_quality_summary.csv`.

A publicação é atômica e recusa sobrescrita de um staging existente.

## Natureza dos resultados

### Dados observados

- valores e linhas dos arquivos capturados;
- cabeçalhos;
- origem, arquivo, planilha e linha;
- quantidade de registros de entrada.

### Dados calculados

- conversões de datas e números;
- hashes de linha;
- sinalizadores de repetição;
- quantidades de saída;
- ano encontrado no nome do arquivo.

### Decisão operacional derivada

A exclusão da cópia com `(1)` ocorre somente no staging e baseia-se no conteúdo normalizado idêntico combinado com o sufixo típico de cópia. Não há exclusão do arquivo bruto.

## Limitações

- igualdade de conteúdo não determina qual arquivo é oficialmente preferencial;
- linhas repetidas na base de ICMS não são tratadas como erros sem validação da fonte;
- os contratos desta etapa não substituem a documentação metodológica das fontes;
- a unidade das medidas monetárias continua sendo a unidade declarada ou implícita na fonte e deve ser documentada na camada curada;
- o staging permanece local e reconstruível.

## Execução

```bash
make build-inbox-staging
```
