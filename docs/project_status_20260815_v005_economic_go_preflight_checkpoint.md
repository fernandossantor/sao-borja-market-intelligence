# Checkpoint do preflight econômico reduzido da v005 — 2026-08-15

## Objetivo

Executar, com autorização explícita, um preflight estritamente de leitura no
Google Drive e na planilha v004 para confirmar a hierarquia autorizada, o
inventário imediato do destino, colisões nominais e o estado das 85 células do
payload econômico reduzido.

Nenhuma criação, cópia, edição, movimentação, exclusão ou escrita foi
realizada no Google Drive.

## Escopo externo autorizado e executado

- raiz `_sao_borja`:
  `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`;
- destino `new_files`:
  `14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`;
- planilha de referência v004:
  `1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM`;
- cinco leituras delimitadas nas abas econômicas;
- horário de registro local da captura: `2026-08-15T22:16:30Z`.

Foram realizadas cinco ações de grounding/inventário: metadados das duas
pastas, listagem dos filhos imediatos de `new_files`, metadados do arquivo v004
e metadados estruturais da planilha. Depois foram realizadas cinco leituras de
faixa com `UNFORMATTED_VALUE`.

## Evidências observadas

- A pasta `_sao_borja` foi identificada pelo ID imutável esperado.
- `new_files` foi identificada pelo ID esperado e mantém `_sao_borja` como pai.
- A v004 mantém `new_files` como pai.
- A v004 mantém o título
  `São Borja — Base Histórica Sistematizada — 2026-08-13 — v004`.
- O horário remoto de modificação da v004 continua
  `2026-08-13T01:28:01.039Z`.
- A planilha contém 19 abas; as abas econômicas observadas foram:
  - `03_Economia_Dados`, `sheetId=891239557`;
  - `03_Economia_Metadados`, `sheetId=246990528`.
- O destino contém 16 filhos imediatos:
  - 5 planilhas;
  - 2 arquivos JSON;
  - 2 arquivos CSV;
  - 7 pastas.
- Não existe filho imediato com título nominal v005 ou com o nome candidato
  `São Borja — Base Histórica Sistematizada — 2026-08-15 — v005`.

## Faixas lidas

| Aba | Faixa | Células lidas | Células-alvo | Linhas retornadas |
| --- | --- | ---: | ---: | ---: |
| `03_Economia_Dados` | `A13:E15` | 15 | 15 | 0 |
| `03_Economia_Metadados` | `A12:I14` | 27 | 27 | 0 |
| `03_Economia_Dados` | `O13:U13` | 7 | 3 | 0 |
| `03_Economia_Dados` | `X14:CC14` | 58 | 20 | 0 |
| `03_Economia_Dados` | `X15:CC15` | 58 | 20 | 0 |

Foram lidas 165 células em retângulos delimitados. O conjunto de decisão
contém 85 células-alvo: 15 descritivas, 27 de metadados e 43 de valor. As
células intermediárias nas faixas anuais foram ignoradas na decisão.

Todas as cinco respostas retornaram listas de valores vazias. Assim, nenhuma
das 85 células-alvo possui valor observado na leitura atual.

## Resultados calculados

| Medida | Resultado |
| --- | ---: |
| Relação pai autorizada | 1 `PASS` |
| Filhos imediatos | 16 |
| Colisões nominais v005 | 0 |
| Abas da planilha | 19 |
| Faixas delimitadas | 5 |
| Células lidas | 165 |
| Células-alvo | 85 |
| Células-alvo com valor | 0 |
| Escritas externas | 0 |

## Comparação com o preflight anterior

- Os 16 IDs e todos os metadados retornados dos filhos são `IDENTICAL` ao
  inventário de 2026-08-14.
- O horário de modificação da v004 é `IDENTICAL`.
- As linhas econômicas e os metadados permanecem vazios: `IDENTICAL`.
- As 43 células econômicas de valor permanecem em faixas vazias: `IDENTICAL`.
- O escopo passou de nove faixas sentinela amplas para cinco faixas somente
  econômicas: `EXPECTED_CHANGE`.
- Diferenças `UNEXPLAINED`: zero.

O arquivo `child_inventory.csv` atual é byte a byte idêntico ao anterior,
confirmado por comparação local e pelo SHA-256
`ca38c8e20473300c69ebf4877ee854d2af95cfcbbaffc866e3b59e30b728a671`.

## Artefatos gerados

Execução:

`spreadsheet-v005-economic-go-preflight-20260815-001`

Diretório:

`.data/audit/base_territorial/spreadsheet_reconciliation/spreadsheet-v005-economic-go-preflight-20260815-001`

| Arquivo | SHA-256 |
| --- | --- |
| `target_metadata.csv` | `10d73072c0d435ce56ab2637990d20d2e0f85336d1ead5d1339f61171a670538` |
| `child_inventory.csv` | `ca38c8e20473300c69ebf4877ee854d2af95cfcbbaffc866e3b59e30b728a671` |
| `range_inventory.csv` | `05cd48d4b2a19aea3f6adaa821c111b81d1f4863cda856129d0e2324cc6b9376` |
| `collision_check.csv` | `e206340df54b540718c0f53bd18f6490dfe8144b667d9b2004547a3580ae4fcd` |
| `comparison.csv` | `0392669fcd573c0d6fd8eafb97b6e54314a116722f966fe90b4d36c3e248947f` |
| `source_manifest.csv` | `0f4510246e0aa61527ee0ee226622b524196dd9231bfe1322248740342fdafa3` |
| `preflight_summary.csv` | `3c2f29261291c86339ad8596c94f34b99285b75754cb33b5da76a7a67e97b785` |
| `validation.csv` | `d3face1826f68265287b9624404629c64e9b13621e9921bb095164752799f3cd` |

O manifesto fixa sete entradas locais por caminho, tamanho e SHA-256.

## Validações

Quinze verificações passaram:

- IDs e nomes das pastas;
- relação pai–filho autorizada;
- identidade e pai da v004;
- 19 abas;
- 16 filhos e inventário idêntico;
- zero colisões nominais;
- cinco faixas delimitadas;
- 85 alvos em faixas sem valores;
- estado compatível com a leitura anterior;
- sete entradas e hashes coincidentes;
- zero diferenças inexplicadas;
- zero escritas externas.

Duas limitações foram registradas:

1. o conector não fornece checksum de células nativas;
2. a leitura de valores simples não comprova ausência de formatação, fórmulas,
   notas ou validações.

## Estimativas

Nenhuma estimativa ou imputação foi realizada.

## Interpretações

- O destino e a planilha de referência permanecem corretamente posicionados.
- Não há colisão nominal observada para a v005 candidata.
- O payload econômico não colide com valores atualmente observados nas 85
  células-alvo.
- A ausência de valores não comprova que uma futura escrita preserve todos os
  controles nativos da planilha.
- O preflight não constitui autorização para criar, copiar ou editar uma
  planilha.

## O que pode ser concluído

- A hierarquia externa atende aos IDs exigidos pela governança.
- O inventário imediato está inalterado desde o preflight anterior.
- Nenhum arquivo v005 nominal foi observado no destino.
- As 85 células-alvo estão sem valores observados.
- Não ocorreu escrita externa.

## O que não pode ser concluído

- Que as células não tenham formatação, fórmula vazia, nota ou validação.
- Que a v004 seja integralmente idêntica à leitura anterior.
- Que a criação de uma nova planilha esteja autorizada por este preflight.
- Que uma futura escrita seja segura sem verificação imediatamente anterior e
  controle de revisão.
- Que blocos em `QUARANTINE` ou `BLOCKED` possam ser publicados.

## Operações externas e Git

- Google Drive: dez ações somente de leitura, sendo cinco de
  grounding/inventário e cinco leituras de faixa.
- Google Drive writes: zero.
- Outros serviços externos: não acessados nesta etapa.
- Arquivos históricos: não modificados.
- Branch: `feature/v005-scope-decision`.
- Commit deste checkpoint: não realizado.
- Push deste checkpoint: não realizado.
- Pull request: não criado.
- Merge: não realizado.

## Próxima ação recomendada

Revisar e registrar este checkpoint na branch. Antes de qualquer escrita,
definir explicitamente a estratégia externa: criar uma nova planilha v005
reduzida dentro de `new_files` ou preservar o payload apenas localmente. Uma
eventual criação deve ter nome determinístico novo, recusar colisões, copiar a
v004 sem alterá-la, aplicar somente as 85 células autorizadas, registrar os
IDs e validar por releitura. Essa escrita exige autorização específica.
