# Checklist de pré-publicação da planilha v005 — 2026-08-14

## Objetivo

Registrar os controles necessários antes de qualquer criação ou escrita da
futura planilha v005, distinguindo o que foi validado localmente do que depende
de autorização e verificação externa. Este checklist não autoriza acesso ou
escrita no Google Drive.

## Evidências observadas

- A planilha v004 permanece a referência externa preservada, com ID
  `1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM`.
- O pacote integrado local usa a execução
  `spreadsheet-v005-integrated-package-20260814-001`.
- Dez componentes foram fixados por caminho, tamanho e SHA-256.
- Os 46 fatos ausentes possuem payload, posição planejada e vínculo de
  proveniência.
- Os 589 valores adicionais permanecem separados do canônico.
- A pasta autorizada `new_files` possui ID declarado
  `14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`; seu pai autorizado `_sao_borja` possui
  ID declarado `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.
- A relação atual entre esses IDs foi revalidada por leitura de metadados: a
  pasta `new_files` mantém `_sao_borja` como pai, e a v004 mantém `new_files`
  como pai.
- O inventário externo retornou 16 filhos diretos em `new_files`: cinco
  planilhas, dois JSONs, dois CSVs e sete pastas.
- Não foi encontrada colisão nominal para `São Borja — Base Histórica
  Sistematizada — 2026-08-14 — v005`.
- A v004 mantém o título esperado e 19 abas. A leitura não examinou células nem
  forneceu checksum criptográfico da planilha nativa.
- Uma leitura posterior examinou nove faixas-sentinela, limitadas à cobertura,
  aos cabeçalhos de Demografia e Economia e às linhas planejadas nessas duas
  dimensões.
- Os quatro blocos de linhas planejadas permanecem vazios e as 46 células
  propostas continuam sem colisão observada.
- A v004 ainda apresenta a inconsistência conhecida no campo `Linhas
  publicadas`: Demografia registra 102 linhas de séries, enquanto Economia
  registra 31 sob uma semântica diferente.

## Resultados calculados

| Controle local | Resultado | Estado |
| --- | ---: | --- |
| Linhas de séries propostas | 413 | `PASS` |
| Indicadores únicos propostos | 319 | `PASS` |
| Observações numéricas propostas | 3.630 | `PASS` |
| Fatos canônicos representados | 3.041 | `PASS` |
| Valores não canônicos preservados | 589 | `PASS` |
| Payloads novos | 46 | `PASS` |
| Células novas únicas | 46 | `PASS` |
| Séries não canônicas verificadas e não modeladas | 111 | `PASS` |
| Séries vazias sem valores | 4 | `PASS` |
| Conflitos ou linhagens não comprovadas | 0 | `PASS` |
| Diferenças `UNEXPLAINED` | 0 | `PASS` |
| Operações externas realizadas pelo pacote | 0 | `PASS` |

## Checklist local

- [x] Preservar a v004 sem edição, renomeação, movimentação ou exclusão.
- [x] Usar novo identificador de execução para cada pacote local.
- [x] Preparar os 46 fatos sem sobrescrever células existentes.
- [x] Manter separadas as metodologias econômicas de 1999–2001 e de 2002 em
  diante.
- [x] Preservar os 589 valores adicionais sem promoção automática.
- [x] Vincular os 46 payloads a fatos, fontes e hashes.
- [x] Registrar campos sem evidência como `EVIDENCE_NOT_AVAILABLE`.
- [x] Fixar os componentes do pacote integrado por SHA-256.
- [x] Validar contagens, chaves e células planejadas.
- [x] Manter todos os payloads como `PREPARED_NOT_PUBLISHED`.

## Checklist externo pendente

- [x] Obter autorização específica para inventário externo somente leitura.
- [x] Confirmar que `new_files` mantém como pai a pasta `_sao_borja` pelos IDs
  imutáveis autorizados.
- [x] Inventariar nomes, IDs, tipos, caminhos e checksums disponíveis no
  destino, registrando explicitamente quando o Drive não os fornece.
- [x] Confirmar que não existe colisão com o nome determinístico proposto para
  a v005.
- [x] Revalidar o ID, título e estrutura de 19 abas da v004.
- [x] Obter autorização específica para leitura limitada de células-sentinela.
- [x] Revalidar cabeçalhos, células-sentinela e dimensões efetivamente
  preenchidas da v004.
- [x] Classificar as diferenças de metadados entre a leitura externa atual e o
  inventário local; nenhuma diferença `UNEXPLAINED` foi observada.
- [x] Interromper diante de qualquer diferença `UNEXPLAINED`; nenhuma foi
  encontrada no escopo de metadados.
- [ ] Obter autorização separada para eventual criação de novo arquivo.
- [ ] Obter autorização separada para eventual escrita de dados e metadados.

O inventário está registrado localmente na execução
`spreadsheet-v005-drive-preflight-inventory-20260814-001`, com dez validações
`PASS` e uma limitação referente à ausência de checksum da planilha nativa.

A leitura de células está registrada na execução
`spreadsheet-v005-v004-sentinel-read-20260814-001`, com nove validações `PASS`,
duas limitações e uma inconsistência conhecida. As limitações registram a
ausência de checksum das células e o fato de nove faixas delimitadas não
comprovarem identidade integral da planilha.

## Bloqueio de governança

A exceção atual de escrita no Drive autoriza coletas de São Borja provenientes
de SIDRA/IBGE, Panorama do Censo 2022, IBGE Cidades, Sebrae/Datawheel e IPS
Brasil, somente nas dimensões já existentes e dentro de `new_files`.

A planilha consolidada proposta também preserva blocos cuja origem declarada
inclui outras famílias, como RAIS, educação, IDSC e dados fiscais. Portanto,
não está comprovado que a criação ou cópia integral da v005 esteja contida na
exceção atual. Autorização conversacional isolada não elimina essa restrição do
repositório.

Estado atual: `BLOCKED_BY_DRIVE_WRITE_SCOPE` para criação ou escrita da
planilha consolidada. O inventário externo e a leitura sentinela já foram
executados separadamente, com apresentação prévia de objetivo, escopo, volume
e riscos e autorização explícita para cada operação.

## Estimativas

Nenhuma estimativa, imputação ou inferência numérica foi produzida. A análise
do escopo de escrita é uma interpretação conservadora das regras vigentes.

## Interpretações

- O pacote está tecnicamente pronto para inventário externo e revisão humana.
- Prontidão técnica local não equivale a autorização de publicação.
- A reversão permanece simples enquanto nenhuma planilha externa nova for
  criada: basta não promover o pacote local.

## O que pode ser concluído

- Os componentes locais necessários para a proposta v005 estão consolidados,
  reconciliados e fixados por hash.
- Não há diferença aritmética ou de junção sem explicação no pacote integrado.
- Uma leitura externa delimitada pode verificar o estado atual sem modificar o
  Drive.

## O que não pode ser concluído

- Que a ausência de colisão nominal exclua equivalência de conteúdo com outro
  arquivo do destino.
- Que a v004 externa permaneça integralmente idêntica em conteúdo ao
  inventário local anterior, pois somente nove faixas foram relidas e não há
  checksum nativo.
- Que a exceção vigente permita criar ou copiar integralmente a planilha
  consolidada v005.
- Que qualquer payload possa ser publicado sem nova decisão explícita.

## Próxima ação recomendada

Resolver o bloqueio `BLOCKED_BY_DRIVE_WRITE_SCOPE` antes de solicitar criação
ou escrita da planilha consolidada. A decisão deve confirmar se o escopo de
governança será ampliado ou se a futura publicação será reduzida estritamente
às fontes autorizadas, sem alterar a v004.

## Estado de operações externas e Git

Este checklist foi criado somente no Codespace. Nenhum serviço externo foi
acessado e nenhum arquivo histórico foi modificado. Não houve commit, push,
criação ou atualização de pull request, nem merge.
