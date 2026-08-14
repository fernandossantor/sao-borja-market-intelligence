# Checkpoint do perfil raw da planilha v005 — 2026-08-14

## Objetivo

Registrar o perfil estrutural e as auditorias locais da primeira fase do
inventário `raw`, preservando o snapshot, as execuções anteriores e os
checkpoints já existentes.

Esta etapa examinou o snapshot local
`spreadsheet-v005-raw-phase1-20260814-001`. Não houve nova obtenção de dados,
acesso ao Google Drive, promoção entre camadas ou publicação da planilha v005.

## Evidências observadas

- O snapshot contém 45 arquivos de dados e `source_manifest.csv`.
- Os arquivos de dados totalizam 3.879.726 bytes.
- Todos os 45 tamanhos e hashes SHA-256 locais coincidem com o manifesto.
- Quarenta e três registros possuem hash upstream comparável.
- Dois registros não possuem `expected_sha256` upstream:
  - `raw/pib/19092428-pib-municipios-rs-2002-2023-serie-historica.xlsx`;
  - `raw/raw_portal_transparencia/Federal/PROGRAMA BOLSA FAMILIA E DO
    CADASTRO UNICO PARA PROGRAMAS SOCIAIS DO GOVERNO FEDERAL.xlsx`.
- A ausência desses dois comparadores foi mantida como limitação de evidência,
  sem ser tratada como igualdade ou divergência upstream.
- Nenhum processo de perfil ou auditoria permaneceu em execução ao final.

## Resultados calculados

### Perfil estrutural final

| Medida | Resultado |
| --- | ---: |
| Arquivos descobertos | 45 |
| Arquivos perfilados | 45 |
| Arquivos com erro | 0 |
| Formatos não suportados | 0 |
| Tabelas perfiladas | 638 |
| Colunas perfiladas | 5.660 |
| Tabelas com baixa confiança de cabeçalho | 8 |
| Assinaturas de esquema | 419 |
| Grupos exatos repetidos | 18 |
| Tabelas em grupos exatos repetidos | 237 |
| Candidatos de similaridade estrutural | 4.789 |

Distribuição final por origem declarada:

| Origem | Arquivos | Tabelas | Assinaturas de esquema |
| --- | ---: | ---: | ---: |
| Agro | 7 | 438 | 262 |
| PIB | 4 | 166 | 155 |
| Fiscal | 28 | 28 | 1 |
| Social | 5 | 5 | 2 |
| Federal | 1 | 1 | 1 |

O caminho histórico
`raw/raw_portal_transparencia/Federal/...` passou a preservar `Federal` como
origem declarada. Outros ramos simples de `raw` continuam usando o primeiro
segmento abaixo de `raw`.

### Auditoria de conteúdo

| Medida | Resultado |
| --- | ---: |
| Tabelas carregadas | 638 |
| Erros de carregamento | 0 |
| Tabelas federais | 1 |
| Tabelas com linhas internas duplicadas | 0 |
| Tabelas com cabeçalho temporal | 33 |
| Falhas de interpretação temporal | 0 |
| Pares federais de sobreposição | 0 |

A única tabela federal contém 33 linhas de dados únicas e período observado de
julho de 2023 a junho de 2026. A triagem estrutural registra 34 linhas
observadas para essa tabela, pois usa critério estrutural distinto da contagem
de linhas de dados da auditoria de conteúdo. As duas medidas não foram
combinadas nem apresentadas como equivalentes.

### Revisão de anomalias final

| Medida | Resultado |
| --- | ---: |
| Pares de conteúdo duplicado | 119 |
| Pares binariamente diferentes | 21 |
| Pares entre tabelas do mesmo arquivo | 98 |
| Pares analíticos entre arquivos | 0 |
| Pares documentais entre arquivos | 21 |
| Grupos de linhas duplicadas | 0 |
| Tabelas temporais | 33 |
| Datas futuras | 0 |
| Datas ambíguas | 0 |
| Possíveis reversões dia/mês | 0 |
| Falhas de interpretação de data | 0 |

Os 21 pares entre arquivos são exclusivamente comparações entre abas `Notas`.
Eles permanecem registrados como `DOCUMENTATION_CONTENT_DUPLICATE`, com
status `PENDING_MANUAL_DISPOSITION`. A classe não comprova redundância
conceitual nem autoriza remoção de arquivos.

## Comparação de execuções

As execuções relevantes são:

- `spreadsheet-v005-raw-phase1-profile-20260814-001`: primeira execução real;
- `spreadsheet-v005-raw-phase1-profile-20260814-002`: correção da origem
  federal e primeira classificação documental;
- `spreadsheet-v005-raw-phase1-profile-20260814-003`: correção final do
  indicador de diferença binária na revisão de anomalias.

A execução `002` reduziu indevidamente
`content_duplicate_binary_different_pairs` de 21 para zero ao associar esse
indicador à classe analítica. A diferença foi classificada como `ERROR`, a
execução foi preservada e um teste automatizado foi acrescentado. A execução
`003` restaurou o valor 21 calculando diretamente `binary_same=False`.

A comparação final registrou:

| Classificação | Artefatos |
| --- | ---: |
| `IDENTICAL` | 13 |
| `EXPECTED_CHANGE` | 9 |
| `UNEXPLAINED` | 0 |

As mudanças esperadas estão limitadas à origem declarada, às sínteses que
dependem dessa origem, à classe documental e ao indicador corrigido. Todas as
execuções foram preservadas.

## Estimativas

Nenhuma estimativa, imputação ou valor modelado foi produzido. Candidatos de
similaridade estrutural são heurísticos e não constituem equivalência de
conteúdo ou compatibilidade conceitual.

## Interpretações

- O lote está estruturalmente legível e íntegro contra seus hashes locais.
- A separação das abas `Notas` reduz falso sinal de duplicidade analítica sem
  ocultar o conteúdo documental repetido.
- A classificação `Federal` permite incluir a tabela na auditoria própria,
  mas uma única tabela não produz comparação de sobreposição entre fontes.
- Aprovação técnica dos pipelines não comprova autoridade, comparabilidade ou
  aptidão para promoção dos dados.

## O que pode ser concluído

- Os 45 arquivos foram perfilados sem erro.
- Os resultados finais estão reconciliados com as mudanças de código
  delimitadas.
- Não há diferença `UNEXPLAINED` entre as execuções comparadas.
- A regressão intermediária foi preservada, explicada, corrigida e coberta por
  teste automatizado.
- Nenhum arquivo bruto, snapshot ou produto histórico foi alterado.

## O que não pode ser concluído

- Que os dois arquivos sem `expected_sha256` sejam iguais às versões upstream.
- Que correspondência estrutural comprove equivalência de conteúdo.
- Que as abas documentais repetidas possam ser removidas.
- Que a ausência de anomalias temporais prove comparabilidade metodológica.
- Que o lote esteja autorizado para promoção, integração à v005 ou publicação.

## Arquivos e artefatos

Arquivos de código e testes alterados nesta etapa:

- `.devcontainer/devcontainer.json`;
- `src/sbmi/inbox_structure_triage.py`;
- `src/sbmi/inbox_anomaly_review.py`;
- `src/sbmi/inbox_anomaly_review_cli.py`;
- `tests/test_inbox_structure_triage.py`;
- `tests/test_inbox_anomaly_review.py`.

Artefatos novos em `.data`, sem sobrescrita:

- `content_profile/spreadsheet-v005-raw-phase1-profile-20260814-002`;
- `structure_triage/spreadsheet-v005-raw-phase1-profile-20260814-002`;
- `content_audit/spreadsheet-v005-raw-phase1-profile-20260814-002`;
- `anomaly_review/spreadsheet-v005-raw-phase1-profile-20260814-002`;
- `anomaly_review/spreadsheet-v005-raw-phase1-profile-20260814-003`;
- `run_comparison/spreadsheet-v005-raw-phase1-001-vs-003-20260814-001`.

## Testes e validações

- 15 testes direcionados passaram após a primeira correção.
- 11 testes direcionados passaram após a correção da regressão.
- `make verify` passou com 295 testes.
- `sbmi doctor` retornou `status=ok`.
- Ruff passou sem achados.
- `git diff --check` passou.
- `.devcontainer/devcontainer.json` foi validado como JSON.
- Os CSVs finais foram relidos e a comparação foi validada após publicação
  atômica.

## Operações externas e Git

Nenhum serviço externo foi acessado. Não houve download, escrita no Drive,
commit, push, criação ou atualização de pull request, nem merge.

A branch permanece `feature/new-files-temporal-coverage`. As alterações locais
anteriores foram preservadas e não foram separadas ou descartadas.

## Próxima ação recomendada

Revisar o diff completo da branch e os cinco documentos ainda não commitados.
Após essa revisão, solicitar autorização explícita antes de criar commit,
enviar a branch ou atualizar pull request.

A criação ou escrita da planilha v005 permanece bloqueada por
`BLOCKED_BY_DRIVE_WRITE_SCOPE` até decisão explícita sobre o escopo externo.
