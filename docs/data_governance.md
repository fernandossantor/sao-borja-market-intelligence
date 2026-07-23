# Governança de dados

## Estados dos arquivos

Cada arquivo ou dataset deve receber um dos seguintes estados:

- `PENDING_AUDIT`: recebido, mas ainda não incorporado;
- `CANONICAL`: fonte ou resultado oficial em uso;
- `GENERATED`: artefato reproduzível gerado pelo pipeline;
- `LEGACY`: preservado para referência, mas fora do fluxo atual;
- `TEMPORARY`: intermediário descartável;
- `DUPLICATE`: duplicata comprovada;
- `INDETERMINATE`: classificação ainda não concluída.

A pasta `raw/new_files` inicia com o estado `PENDING_AUDIT`.

## Manifesto mínimo

O inventário de arquivos deve registrar, quando disponível:

| Campo | Descrição |
|---|---|
| `dataset_id` | Identificador estável do dataset |
| `drive_file_id` | Identificador do arquivo no Google Drive |
| `relative_path` | Caminho relativo dentro do projeto |
| `file_name` | Nome original |
| `extension` | Extensão |
| `size_bytes` | Tamanho em bytes |
| `created_at` | Data de criação no armazenamento |
| `modified_at` | Data de modificação no armazenamento |
| `sha256` | Hash binário do arquivo |
| `source_name` | Instituição ou sistema de origem |
| `source_url` | Endereço da fonte, quando conhecido |
| `reference_period` | Período coberto |
| `geographic_scope` | Abrangência territorial |
| `unit` | Unidade dos valores |
| `audit_status` | Estado de auditoria |
| `limitations` | Limitações conhecidas |

## Duplicidades

A auditoria deve distinguir:

1. `EXACT_DUPLICATE`: mesmo hash SHA-256;
2. `CONTENT_DUPLICATE`: conteúdo tabular equivalente após normalização;
3. `PARTIAL_OVERLAP`: parte das observações ou períodos coincide;
4. `COMPLEMENTARY`: mesma temática, mas escopo ou granularidade complementar;
5. `CONFLICT`: valores incompatíveis para as mesmas chaves e conceitos;
6. `UNIQUE`: não foi encontrada sobreposição relevante.

Nomes semelhantes ou totais próximos não são prova de duplicidade.

## Novos arquivos fiscais

### Federal

As planilhas em `raw/new_files/Federal` devem ser comparadas com as fontes já consolidadas em `raw/fiscal`. Não devem ser somadas antes da verificação de programa, favorecido, competência, valor e origem.

### Estadual

Transferências estaduais e repasses de ICMS formam uma fonte distinta das transferências federais. A origem governamental deve permanecer explícita em todas as tabelas.

### Municipal

Receitas e despesas municipais não são equivalentes a transferências recebidas. A fase orçamentária e o conceito contábil devem ser identificados antes da consolidação: previsto, arrecadado, empenhado, liquidado ou pago.

## Substituição de resultados

Uma nova execução só pode substituir um resultado anterior depois de comparação de:

- esquema;
- quantidade de linhas;
- chaves e duplicidades;
- valores ausentes;
- cobertura temporal e territorial;
- totais e indicadores principais;
- hash do arquivo final.

Cada diferença deve ser classificada como `IDENTICAL`, `EXPECTED_CHANGE`, `SOURCE_UPDATE`, `METHODOLOGY_CHANGE`, `ERROR` ou `UNEXPLAINED`.
