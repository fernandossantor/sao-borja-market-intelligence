# Checkpoint da planilha v005 e do inventário raw — 2026-08-14

## Objetivo

Registrar o estado comprovado ao encerrar o trabalho de 2026-08-14, permitindo
retomada sem dependência do histórico da conversa. O trabalho prepara uma nova
planilha consolidada com os dados confiáveis já existentes em
`_sao_borja/raw`, preservando os arquivos brutos e a planilha v004.

## Diretório e Git

- Diretório confirmado: `/workspaces/sao-borja-market-intelligence`.
- Branch: `feature/new-files-temporal-coverage`.
- Arquivos não rastreados:
  - `docs/spreadsheet_v004_canonical_reconciliation_20260814.md`;
  - `docs/spreadsheet_v004_remediation_plan_20260814.md`;
  - `docs/spreadsheet_v005_prepublication_checklist_20260814.md`.
- Este checkpoint também permanece sem commit.
- Não houve commit, push, criação ou atualização de pull request, nem merge.

## Decisão de governança do responsável

O responsável esclareceu e autorizou que todos os datasets preexistentes em
`_sao_borja/raw` sejam tratados como entradas confiáveis do projeto e
organizados em uma nova planilha consolidada, exclusivamente dentro de
`new_files`.

Essa decisão é registrada como `PROJECT_TRUSTED_INPUT`. Ela não elimina a
separação obrigatória entre conceitos, períodos, unidades, métodos e fontes,
nem autoriza alteração dos arquivos brutos ou da v004. Downloads de grande
volume e escritas externas continuam sujeitos a apresentação prévia de escopo,
volume e riscos.

## Evidências observadas

### Planilha v004 e destino

- v004: `1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM`.
- `new_files`: `14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`.
- `_sao_borja`: `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.
- `new_files` mantém `_sao_borja` como pai.
- A v004 mantém `new_files` como pai, o título esperado e 19 abas.
- Foram inventariados 16 filhos diretos em `new_files`.
- Não existe colisão nominal com o nome proposto
  `São Borja — Base Histórica Sistematizada — 2026-08-14 — v005`.
- Nove faixas-sentinela da v004 foram lidas; os quatro blocos de linhas
  planejadas permanecem vazios e as 46 células propostas não apresentaram
  colisão.
- A v004 mantém a inconsistência conhecida no campo `Linhas publicadas`:
  Demografia registra 102 e Economia registra 31 sob definições diferentes.

### Inventário de `_sao_borja/raw`

- Pasta `raw`: `1MSSafSodD8jqtuaMo7T_ChYSd6bHCxiL`.
- Pai confirmado: `_sao_borja`.
- Nove ramos de primeiro nível.
- Vinte e uma subpastas abaixo de `raw`.
- Cento e sessenta e três arquivos:
  - 82 XLSX;
  - 64 CSV;
  - 15 PDF;
  - 2 XLS.
- Tamanho conhecido: 1.791.906.869 bytes.
- Nenhum arquivo foi baixado durante o inventário de 2026-08-14.

## Resultados calculados

### Proposta integrada da v005

| Medida | Resultado |
| --- | ---: |
| Linhas de séries | 413 |
| Indicadores únicos | 319 |
| Observações numéricas | 3.630 |
| Fatos canônicos representados | 3.041 |
| Valores adicionais preservados | 589 |
| Séries adicionais verificadas e não modeladas | 111 |
| Séries vazias sem valores | 4 |
| Diferenças `UNEXPLAINED` | 0 |

A decomposição aprovada é:

```text
3.041 fatos canônicos + 589 valores adicionais = 3.630 observações
```

Os 46 fatos ausentes da v004 possuem payload, células únicas, manifesto de
fontes e status `PREPARED_NOT_PUBLISHED`.

### Reconciliação do inventário raw com `.data`

| Classe | Arquivos | Interpretação |
| --- | ---: | --- |
| `EXACT_CONTENT_MATCH` | 69 | SHA-256 local igual ao histórico |
| `LOCAL_HASH_ONLY` | 3 | SHA-256 local sem comparador upstream histórico |
| `SOURCE_UPDATE` | 1 | mesmo ID, tamanho e modificação alterados |
| `NOT_LOCALLY_MATERIALIZED` | 90 | conteúdo ainda não disponível localmente |
| **Total** | **163** | partição completa |

O único `SOURCE_UPDATE` é o arquivo federal de Bolsa Família e Cadastro Único.
Seu tamanho passou de 7.352 para 10.240 bytes, diferença de 2.888 bytes. O hash
histórico não representa seu conteúdo atual.

O escopo máximo ainda não materializado corresponde a 91 arquivos e
1.725.957.956 bytes. Nenhum download desse conjunto foi executado.

## Primeira fase recomendada de download

Retomar com um lote pequeno de 45 arquivos tabulares e 3.879.726 bytes:

| Ramo | Arquivos | Bytes |
| --- | ---: | ---: |
| Fiscal | 28 | 533.715 |
| Agro | 7 | 496.426 |
| PIB | 4 | 1.758.963 |
| Social | 5 | 1.080.382 |
| Transparência — arquivo atualizado | 1 | 10.240 |
| **Total** | **45** | **3.879.726** |

Antes dessa obtenção, apresentar objetivo, lista exata, destino local novo,
timeout, recusa de colisões, validação de tamanho e SHA-256, riscos e solicitar
autorização explícita. Não incluir nessa primeira fase:

- 31 arquivos institucionais, que concentram aproximadamente 1,55 GiB;
- 15 PDFs documentais, que somam aproximadamente 55,8 MiB.

## Artefatos locais principais

Todos estão em `.data`, são ignorados pelo Git e usam identificadores próprios:

- `spreadsheet-v005-missing-facts-publication-package-20260814-001`;
- `spreadsheet-v005-integrated-package-20260814-001`;
- `spreadsheet-v005-drive-preflight-inventory-20260814-001`;
- `spreadsheet-v005-v004-sentinel-read-20260814-001`;
- `spreadsheet-v005-raw-drive-inventory-20260814-001`;
- `spreadsheet-v005-raw-local-reconciliation-20260814-001`.

Também permanecem válidos os pacotes anteriores de payload, cobertura,
reconciliação canônica, linhagem dos 589 valores e prontidão de promoção.

## Estimativas

Não foram produzidas estimativas analíticas, imputações ou valores modelados.
Conversões para MiB/GiB são apenas apresentações aproximadas dos bytes
observados.

## Interpretações

- O universo de arquivos brutos está completamente inventariado por
  metadados.
- A decisão `PROJECT_TRUSTED_INPUT` autoriza seu uso como entrada, mas nomes e
  tamanhos não provam conteúdo ou equivalência conceitual.
- Os 72 arquivos já disponíveis localmente podem ser reutilizados sem novo
  download; 69 têm comparação criptográfica aprovada e três têm apenas hash
  local.
- A obtenção faseada evita baixar aproximadamente 1,61 GiB antes de validar os
  blocos menores e mais diretamente tabulares.
- PDFs devem ser catalogados como documentos-fonte; qualquer dado extraído
  deles precisa manter citação de página e natureza própria.

## O que pode ser concluído

- A proposta local da v005 está aritmeticamente reconciliada e sem diferença
  `UNEXPLAINED`.
- Os 163 arquivos de `raw` têm IDs únicos e pertencem à hierarquia autorizada.
- Sessenta e nove arquivos possuem igualdade binária comprovada com cópias
  locais; zero hashes comparáveis divergiram.
- A primeira fase de obtenção pode ser limitada a 45 arquivos e menos de
  4 MB.
- Nenhum bruto, snapshot histórico ou planilha externa foi modificado.

## O que não pode ser concluído

- Que os 91 arquivos ainda não materializados mantenham o conteúdo descrito
  pelos hashes históricos.
- Que os três arquivos `LOCAL_HASH_ONLY` sejam iguais a uma versão upstream
  hasheada, pois esse comparador não existe.
- Que confiança da entrada prove compatibilidade conceitual entre datasets.
- Que PDFs possam ser convertidos automaticamente em séries tabulares.
- Que a planilha v005 já tenha sido criada ou publicada.

## Testes e validações

Na validação final desta sessão:

- a partição `69 + 3 + 1 + 90 = 163` foi aprovada;
- 69 de 69 hashes comparáveis coincidiram;
- a diferença de 2.888 bytes foi explicada;
- os nove ramos, incluindo `extracted` vazio, foram preservados;
- `git diff --check` foi aprovado;
- `make verify` registrou `sbmi doctor` com `status=ok`;
- 290 testes passaram;
- Ruff passou sem achados.

## Operações externas

Foram realizadas somente:

- leituras de metadados das pastas e da v004;
- listagens de pastas;
- leitura de nove faixas-sentinela da v004.

Não houve download de arquivos raw, criação, cópia, escrita, movimentação,
renomeação ou exclusão no Drive.

## Próxima ação recomendada

1. reler este checkpoint e confirmar o diretório exato;
2. recalcular os 45 arquivos e 3.879.726 bytes da primeira fase a partir de
   `spreadsheet-v005-raw-local-reconciliation-20260814-001`;
3. apresentar a lista, destino local, riscos e validações;
4. solicitar autorização explícita para o download delimitado;
5. baixar para novo snapshot parcial, validar tamanho e SHA-256 e publicar o
   snapshot local atomicamente;
6. perfilar esquemas e conteúdo antes de integrá-los à planilha;
7. manter os arquivos institucionais e PDFs fora dessa primeira fase.

## Estado final

O trabalho foi interrompido de forma segura ao final de uma etapa validada.
Não há processo em execução, diretório `.partial` conhecido, operação externa
pendente, commit, push ou pull request em andamento.
