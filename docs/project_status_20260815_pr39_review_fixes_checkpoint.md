# Checkpoint das correções de revisão do PR #39 — 2026-08-15

## Objetivo

Registrar o estado local após a reprodução, correção e validação das três
threads inline abertas no pull request #39, preservando os artefatos e
execuções anteriores.

Esta etapa corrigiu somente o código local e gerou uma nova execução de
auditoria em `.data`. Não houve alteração de arquivos brutos ou históricos,
acesso ao Google Drive, commit, push, resposta ou resolução de threads, nem
atualização material do pull request.

## Contexto do GitHub observado

- Repositório: `fernandossantor/sao-borja-market-intelligence`.
- Pull request: #39, `Audit historical raw spreadsheet inputs`.
- Branch: `feature/new-files-temporal-coverage`.
- Base: `main`.
- Commit revisado: `b0c7779a53b25b472597ec8c86936b911da82e46`.
- Estado observado antes das correções: aberto, não rascunho, mergeável e
  `CLEAN`.
- Check `quality/test`: `SUCCESS`.
- Três threads inline estavam abertas, não resolvidas e não obsoletas.

O acesso ao GitHub nesta etapa foi exclusivamente de leitura.

## Evidências observadas

### Thread 1 — destino padrão do perfil

`src/sbmi/inbox_profile_cli.py` derivava o destino padrão somente do nome do
snapshot. Assim, execuções com escopos diferentes, por exemplo o padrão
`raw/new_files` e o escopo `raw`, podiam selecionar o mesmo diretório e escrever
diretamente sobre os mesmos CSVs.

### Thread 2 — anos abreviados

`parse_temporal_value` e `parse_date_observation` somavam 2000 a anos com dois
dígitos. Um valor como `dez/99` era, portanto, transformado em dezembro de
2099 sem evidência suficiente do século.

Na execução real, foram observados 81 valores com ano abreviado, todos em:

`raw/fiscal/Legais, Voluntárias e Específicas Primária Saúde 2020 - 2026.csv`.

Os valores incluem tokens como `fev/20`, `jan/26` e `dez/25`. O nome do arquivo
fornece contexto, mas não foi usado como prova suficiente para atribuir o
século a cada valor.

### Thread 3 — duplicidade documental no mesmo arquivo

Em `build_content_duplicate_pairs`, a condição de duas abas chamadas `Notas`
era avaliada antes de `same_file`. Duas abas documentais iguais no mesmo
workbook podiam ser classificadas como `DOCUMENTATION_CONTENT_DUPLICATE`, em
vez de `INTRA_FILE_TABLE_DUPLICATE`.

## Alterações implementadas

### Destino por escopo e recusa de sobrescrita

- Foi adicionada `default_output_dir` em `src/sbmi/inbox_profile_cli.py`.
- O nome padrão agora incorpora o escopo de origem de forma determinística:
  - `snapshot-001--raw`;
  - `snapshot-001--raw--new_files`.
- O CLI verifica se o destino existe antes do perfil e lança
  `FileExistsError`.
- A criação do diretório usa `exist_ok=False`.

### Ano abreviado ambíguo

- `parse_temporal_value` passa a retornar `None` para mês textual com ano de
  dois dígitos.
- `parse_date_observation` não atribui século e registra:
  - `parsed_date=None`;
  - `ambiguous=True`;
  - `parse_method=TEXT_MONTH_SHORT_YEAR_AMBIGUOUS`.
- A revisão temporal contabiliza esses valores como ambíguos e como falhas de
  interpretação, sem produzir data futura ou período inventado.

### Precedência intra-arquivo

- `same_file` passa a ser avaliado antes da classe documental.
- Duas abas `Notas` iguais no mesmo arquivo são classificadas como
  `INTRA_FILE_TABLE_DUPLICATE`.
- Abas `Notas` iguais em arquivos distintos continuam classificadas como
  `DOCUMENTATION_CONTENT_DUPLICATE`.

## Arquivos modificados localmente

- `src/sbmi/inbox_profile_cli.py`;
- `src/sbmi/inbox_content_audit.py`;
- `src/sbmi/inbox_anomaly_review.py`;
- `tests/test_inbox_profile.py`;
- `tests/test_inbox_content_audit.py`;
- `tests/test_inbox_anomaly_review.py`.

Este checkpoint é o sétimo arquivo local da etapa.

## Resultados calculados

### Testes direcionados

Foram executados:

```text
pytest -q tests/test_inbox_profile.py tests/test_inbox_content_audit.py tests/test_inbox_anomaly_review.py
```

Resultado: 20 testes aprovados.

### Validação obrigatória

`make verify` foi executado após as correções:

- `sbmi doctor`: `status=ok`;
- Pytest: 297 testes aprovados;
- Ruff: sem achados.

`git diff --check` também passou sem achados.

### Validação de colisão

Uma segunda tentativa controlada de executar o perfil contra o novo destino já
existente terminou com `FileExistsError` antes do perfil. Nenhum CSV existente
foi substituído.

## Pipeline real executado

Snapshot somente leitura:

`spreadsheet-v005-raw-phase1-20260814-001`.

Identificador novo da etapa:

`spreadsheet-v005-raw-phase1-reviewfix-20260815-001`.

Artefatos novos foram gerados em:

- `.data/audit/new_files/content_profile/spreadsheet-v005-raw-phase1-reviewfix-20260815-001`;
- `.data/audit/new_files/content_audit/spreadsheet-v005-raw-phase1-reviewfix-20260815-001`;
- `.data/audit/new_files/anomaly_review/spreadsheet-v005-raw-phase1-reviewfix-20260815-001`.

Foram produzidos 13 CSVs: quatro de perfil, quatro de auditoria de conteúdo e
cinco de revisão de anomalias.

Resultados principais:

| Medida | Resultado |
| --- | ---: |
| Arquivos descobertos | 45 |
| Arquivos perfilados | 45 |
| Erros de perfil | 0 |
| Tabelas perfiladas | 638 |
| Colunas perfiladas | 5.660 |
| Erros de carregamento | 0 |
| Pares de conteúdo duplicado | 119 |
| Pares binariamente diferentes | 21 |
| Pares intra-arquivo | 98 |
| Pares documentais entre arquivos | 21 |
| Grupos de linhas duplicadas | 0 |
| Tabelas temporais | 33 |
| Datas futuras | 0 |
| Datas abreviadas ambíguas | 81 |
| Falhas de interpretação temporal | 81 |

## Comparação com a execução anterior

Execução anterior preservada:

`spreadsheet-v005-raw-phase1-profile-20260814-003`.

### `IDENTICAL`

- `content_duplicate_pairs.csv`: 119 × 20 nas duas execuções, conteúdo
  idêntico;
- `duplicate_row_groups.csv`: 0 × 12 nas duas execuções, conteúdo idêntico;
- 32 das 33 tabelas em `temporal_table_summary.csv`.

### `EXPECTED_CHANGE`

Somente a tabela fiscal com anos abreviados mudou:

| Indicador | Execução 003 | Execução nova |
| --- | ---: | ---: |
| Valores interpretados | 81 | 0 |
| Falhas de interpretação | 0 | 81 |
| Valores ambíguos | 0 | 81 |
| Período mínimo calculado | 2020-02-01 | ausente |
| Período máximo calculado | 2026-02-01 | ausente |

`temporal_anomalies.csv` passou de zero para 81 linhas. Todas possuem classe
`AMBIGUOUS_DATE` e método `TEXT_MONTH_SHORT_YEAR_AMBIGUOUS`.

A mudança foi classificada como `EXPECTED_CHANGE` porque decorre diretamente
da remoção da inferência não documentada do século.

### `UNEXPLAINED`

Nenhuma diferença foi classificada como `UNEXPLAINED`.

## Estimativas

Nenhuma estimativa, imputação de século ou valor modelado foi produzida.

## Interpretações

- Os três comentários de revisão identificaram falhas reais ou lacunas de
  proteção.
- Os checks anteriores passavam porque os casos-limite não estavam cobertos.
- A nova representação das 81 datas é mais conservadora: preserva o valor
  observado e explicita a ausência de evidência do século.
- O contexto nominal do arquivo pode orientar uma futura revisão manual, mas
  não comprova sozinho o século de cada registro.

## O que pode ser concluído

- As três pendências foram reproduzidas no código e corrigidas localmente.
- Foram adicionados testes automatizados diretamente associados às falhas.
- O pipeline real concluiu sem erro e sem sobrescrita.
- Todas as diferenças observadas em relação à execução `003` estão delimitadas
  e classificadas.
- Nenhum arquivo bruto, snapshot ou resultado histórico foi modificado.

## O que não pode ser concluído

- O século correto das 81 datas abreviadas não foi comprovado.
- As threads ainda não foram aceitas ou resolvidas pelo revisor.
- Os checks remotos ainda não validaram as alterações locais.
- As alterações ainda não estão no PR #39.
- A planilha v005 não está autorizada para publicação por esta etapa.

## Operações externas e estado do Git

- GitHub: consulta somente leitura do PR, revisões, checks e threads.
- Google Drive: não acessado.
- Outros serviços externos: não acessados.
- Commit: não realizado.
- Push: não realizado.
- Pull request: não atualizado materialmente.
- Merge: não realizado.

Ao final da etapa, a branch local permanece
`feature/new-files-temporal-coverage`, com seis arquivos de código/testes
modificados e este checkpoint novo, todos ainda não commitados.

## Próxima ação recomendada

Na retomada:

1. ler este checkpoint e confirmar `git status --short --branch`;
2. revisar o diff final dos sete arquivos;
3. confirmar que os três diretórios de artefatos novos permanecem íntegros;
4. solicitar autorização explícita antes de criar commit e fazer push;
5. após o push e os checks remotos, solicitar autorização específica antes de
   responder ou resolver as três threads no PR #39;
6. não executar merge sem autorização explícita.
