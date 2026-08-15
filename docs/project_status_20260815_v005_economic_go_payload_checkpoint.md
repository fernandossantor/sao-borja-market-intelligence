# Checkpoint do payload econômico reduzido da v005 — 2026-08-15

## Objetivo

Derivar localmente um payload contendo somente os 43 fatos econômicos
classificados como `GO` na decisão de escopo da v005, excluindo os três fatos
domiciliares em quarentena e sem realizar escrita externa.

## Evidências observadas

- O payload anterior `spreadsheet-v005-write-payload-20260814-001` contém 46
  valores, seis linhas descritivas, seis linhas de metadados e três fontes.
- Os 43 fatos econômicos pertencem a dois registros de fonte:
  - `gdp_old_1999_2001_zip`, com 3 fatos;
  - `gdp_current_sidra_5938_json`, com 40 fatos.
- Os três fatos excluídos pertencem a `census_household_xlsx` e permanecem em
  `QUARANTINE` por lacunas documentadas de URL e horário de obtenção.
- Todos os valores econômicos têm como destino `03_Economia_Dados`.
- As linhas descritivas e de metadados econômicas são três em cada payload.

## Resultados calculados

O pacote reduzido contém:

| Medida | Resultado |
| --- | ---: |
| Blocos `GO` | 2 |
| Fatos econômicos | 43 |
| Linhas descritivas | 3 |
| Linhas de metadados | 3 |
| Células de valor | 43 |
| Células planejadas | 85 |
| Registros de fonte | 2 |
| Fatos domiciliares excluídos | 3 |
| Escritas externas | 0 |

As 85 células planejadas são a soma determinística de 15 células descritivas,
27 células de metadados e 43 células de valor.

## Pipeline real executado

1. releitura dos três payloads originais;
2. seleção dos 43 `fact_id` associados às duas fontes econômicas `GO`;
3. filtro independente por aba econômica para linhas e metadados;
4. exclusão dos três fatos domiciliares;
5. comparação de cada `fact_id`, célula, ano e valor com o manifesto dos 46
   fatos;
6. criação em diretório parcial;
7. validação independente;
8. promoção atômica ao destino final novo.

Nenhum payload foi marcado como publicado. Todos mantêm
`PREPARED_NOT_PUBLISHED`.

## Artefatos gerados

Execução:

`spreadsheet-v005-economic-go-payload-20260815-001`

Diretório:

`.data/audit/base_territorial/spreadsheet_reconciliation/spreadsheet-v005-economic-go-payload-20260815-001`

| Arquivo | SHA-256 |
| --- | --- |
| `value_cell_payload.csv` | `97a89bd2343d6b0aa0c26c6741f56b37545446419b4dd84685a33841a23ed921` |
| `data_row_payload.csv` | `ac6322edca5ce621b234e6bdc547ba9df1f6228cca95ea7cbae888d9353ffb56` |
| `metadata_row_payload.csv` | `b2ebf8fec10bdf419b81968f390464d7a98268b936187a92e014771f82f95acc` |
| `source_records.csv` | `b7229fc8bf33b9b0e655b270b8cb96bb8f8c5c300af674f6f35a1db6d835b5e6` |
| `payload_summary.csv` | `9ac8cd4b4557e3d423cabf8c5b6eca2d965c924359ad2d0a5f7a106e8ac30496` |
| `comparison.csv` | `4d5531a76c54f34e7df520f2c91b3c838c50c96d67d025c2607d474cf2a70b29` |
| `source_manifest.csv` | `c82b273c536b5881ccb27b821f22cd586894a89cc1f7c707b5c3a7591e885b38` |
| `validation.csv` | `97dfec3a3331e351383a57cc6186bd7d23199822d7af03be2023804c437fd06f` |

O manifesto registra seis entradas imediatas com caminho, tamanho, hash e
execução produtora.

## Validações

As 13 validações registradas passaram:

- 43 fatos `GO` presentes e únicos;
- 43 células de valor únicas;
- somente a aba econômica de valores;
- três linhas descritivas e três linhas de metadados;
- duas fontes econômicas;
- três fatos domiciliares excluídos;
- 85 células planejadas reconciliadas;
- seis entradas fixadas no manifesto;
- nenhuma diferença inexplicada;
- status `PREPARED_NOT_PUBLISHED`;
- zero escritas externas.

A validação independente também comparou os 43 valores numéricos e anos com o
manifesto dos fatos e recalculou os seis hashes de entrada.

## Comparação com o pacote anterior

| Indicador | Anterior | Atual | Classificação |
| --- | ---: | ---: | --- |
| Linhas descritivas | 6 | 3 | `EXPECTED_CHANGE` |
| Linhas de metadados | 6 | 3 | `EXPECTED_CHANGE` |
| Células de valor | 46 | 43 | `EXPECTED_CHANGE` |
| Células planejadas | 130 | 85 | `EXPECTED_CHANGE` |
| Fontes | 3 | 2 | `EXPECTED_CHANGE` |
| Diferenças inexplicadas | 0 | 0 | `IDENTICAL` |

Todas as reduções decorrem exclusivamente da remoção dos três fatos
domiciliares e de suas linhas descritivas e de metadados.

## Estimativas

Nenhuma estimativa, imputação ou transformação de valor foi realizada.

## Interpretações

- O pacote está tecnicamente delimitado às duas fontes econômicas classificadas
  como `GO`.
- A preparação local não equivale a autorização de escrita externa.
- A separação metodológica entre o PIB de 1999–2001 e a série de 2002 em
  diante deve ser preservada em qualquer publicação futura.

## O que pode ser concluído

- Todos e somente os 43 fatos econômicos `GO` estão no payload reduzido.
- Os valores, anos, células e vínculos de fonte reconciliam com o pacote
  anterior.
- Os três fatos domiciliares em quarentena não estão no payload.
- Não há diferença `UNEXPLAINED`.
- Nenhum arquivo histórico foi modificado.

## O que não pode ser concluído

- Que o payload já esteja autorizado para escrita.
- Que o destino externo continue sem colisões desde o último inventário.
- Que as células de destino permaneçam vazias ou idênticas ao último estado
  lido.
- Que a publicação possa ocorrer sem novo preflight e autorização específica.
- Que os blocos em `QUARANTINE` ou `BLOCKED` possam ser adicionados.

## Operações externas e Git

- Google Drive: não acessado.
- GitHub: somente o push anterior do checkpoint de decisão de escopo; nenhum
  acesso externo foi realizado durante a geração deste payload.
- Arquivos históricos: não modificados.
- Branch: `feature/v005-scope-decision`.
- Commit deste checkpoint: não realizado.
- Push deste checkpoint: não realizado.
- Pull request: não criado.
- Merge: não realizado.

## Próxima ação recomendada

Revisar o diff documental e registrar este checkpoint na branch. Depois,
preparar um preflight externo estritamente de leitura para confirmar a pasta
autorizada, colisões de nome e o estado atual das células de destino. O acesso
externo deve ter objetivo, escopo, volume, riscos e autorização apresentados
antes da execução. Nenhuma escrita deve ocorrer no preflight.
