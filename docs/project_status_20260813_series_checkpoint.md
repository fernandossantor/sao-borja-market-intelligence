# Checkpoint consolidado das séries territoriais — 2026-08-13

## Escopo

Este checkpoint consolida a implementação, a integração operacional no
`Makefile` e as validações locais das séries demográficas, econômicas,
empresariais, educacionais e fiscais de São Borja/RS. Os produtos permanecem
separados por conceito e preservam o fluxo `raw → staging → curated → exports`.

## Evidências observadas

- O município de referência nos pipelines oficiais é São Borja, código IBGE
  `4318002`.
- Há capturas preservadas do SIDRA/IBGE para demografia histórica e censitária
  e para PIB municipal.
- As séries de empresas/emprego, educação e finanças públicas usam capturas
  locais do Sebrae/Datawheel com as instituições de origem declaradas nos
  respectivos manifestos.
- O novo snapshot oficial DCA/SICONFI
  `siconfi-dca-4318002-2019-2025-20260813-002510` contém os exercícios de 2019
  a 2025, todos com `audit_status=VERIFIED` no manifesto.
- Cada pipeline publica em diretório identificado pela execução e recusa a
  sobrescrita de execução existente.

## Resultados calculados

As validações preservadas registram:

| Produto | Linhas | Cobertura ou dimensão | Duplicidades | Status |
| --- | ---: | --- | ---: | --- |
| Demografia histórica | 30 | 1991–2025 | 0 | `PASS` |
| Demografia censitária | 492 | 1991–2022 | 0 | `PASS` |
| PIB e VAB municipal | 272 | 3 anos antigos e 20 anos setoriais completos | 0 | `PASS` |
| Empresas e emprego | 30 | 3 indicadores completos, 2016–2025 | 0 | `PASS` |
| Educação | 67 | 11 indicadores, 2005–2025 | 0 | `PASS` |
| Finanças públicas locais | 20 | 15 indicadores, 2019–2025 | 0 | `PASS` |
| DCA/SICONFI oficial | 268 | 18 contas, 7 exercícios | 0 | `PASS` |

A matriz DCA registra 110 combinações `MISSING`. Elas são ausências observadas
na matriz de cobertura e não foram convertidas em zero.

## Integração no Makefile

Os seguintes alvos são a interface operacional consolidada:

```text
snapshot-base-territorial-demography-historical-values
snapshot-base-territorial-demography-census-series
snapshot-base-territorial-economy-gdp-series
build-base-territorial-business-employment-series
build-base-territorial-education-series
build-base-territorial-public-finance-series
snapshot-base-territorial-siconfi-dca
build-base-territorial-siconfi-dca-series
```

`PUBLIC_FINANCE_SOURCE_DIR` permite selecionar a captura local de finanças
públicas. `SICONFI_DCA_SNAPSHOT_ID` define o identificador de uma nova captura.
`SICONFI_DCA_SNAPSHOT_DIR` é obrigatório para a curadoria DCA, evitando a
seleção implícita de um snapshot histórico.

## Comparação com as execuções anteriores

Foram executados novamente os quatro pipelines exclusivamente locais e, após
autorização explícita, os quatro pipelines de captura externa. Os produtos
curados foram comparados por SHA-256:

| Produto | Execução atual | Classificação | Decisão |
| --- | --- | --- | --- |
| Empresas e emprego | `business-employment-series-20260813-002203` | `IDENTICAL` | preservar ambas as execuções |
| Educação | `education-series-20260813-002204` | `IDENTICAL` | preservar ambas as execuções |
| Finanças públicas locais | `public-finance-series-20260813-002204` | `IDENTICAL` | preservar ambas as execuções |
| DCA/SICONFI oficial | `siconfi-dca-series-20260813-002205` | `IDENTICAL` | preservar ambas as execuções |
| Demografia histórica | `demography-historical-values-20260813-002503` | `IDENTICAL` | preservar ambas as execuções |
| Demografia censitária | `demography-census-series-20260813-002505` | `IDENTICAL` | preservar ambas as execuções |
| PIB e VAB municipal | `economy-gdp-series-20260813-002507` | `IDENTICAL` | preservar ambas as execuções |
| Nova captura DCA/SICONFI | `siconfi-dca-series-20260813-002543` | `IDENTICAL` | preservar ambas as execuções |

Os arquivos `validation.csv` atuais também são idênticos aos anteriores. Não
houve diferença `UNEXPLAINED`, promoção substitutiva ou alteração histórica.

## Integração canônica paralela

Foi criado o builder `canonical_territorial_model_series.py`, sem modificar os
builders históricos. Ele preserva integralmente os 1.920 fatos de
`canonical-extended-20260729-200621` e acrescenta somente valores numéricos das
sete famílias novas.

A execução final `canonical-series-20260813-003301` registrou:

- 1.920 fatos herdados e logicamente idênticos ao canônico estendido;
- 1.121 novos fatos promovidos;
- 3.041 fatos totais, 145 indicadores e um território;
- 38 valores censitários e 20 valores de PIB/VAB excluídos como
  ausentes/suprimidos;
- zero chaves duplicadas e zero nulos em campos obrigatórios.

As execuções `canonical-series-20260813-003147` e
`canonical-series-20260813-003301` são `IDENTICAL` por SHA-256 para fatos,
dimensões, reconciliação e validação. Ambas foram preservadas; nenhuma substitui
os produtos `canonical` ou `canonical_extended` anteriores.

## Estimativas

Nenhuma estimativa, interpolação ou imputação foi produzida nesta etapa.

## Interpretações

- A integração ao `Makefile` fornece pontos de entrada reproduzíveis, mas não
  torna conceitualmente equivalentes as famílias de indicadores.
- A igualdade binária das quatro reexecuções locais comprova reprodutibilidade
  para as mesmas entradas; não comprova autoridade além da proveniência já
  registrada nos manifestos.
- A série local de finanças públicas via Sebrae/Datawheel e a série oficial
  DCA/SICONFI devem permanecer separadas até reconciliação semântica específica.

## O que pode ser concluído

- Os oito CLIs estão integrados ao `Makefile` com comandos expansíveis.
- Os quatro pipelines locais executam de ponta a ponta, geram IDs próprios e
  reproduzem exatamente os produtos anteriores.
- As validações examinadas não registram chaves duplicadas ou falhas.
- Não há resíduos `.partial` em `.data` após as execuções.

## O que não pode ser concluído

- A disponibilidade dos endpoints foi observada somente no instante desta
  execução e não garante disponibilidade futura.
- Não foi realizada comparação conceitual de equivalência entre famílias. A
  integração ao modelo territorial foi apenas paralela e aditiva, sem promover
  ou substituir os produtos canônicos históricos.
- Cobertura temporal não implica comparabilidade metodológica entre anos,
  tabelas ou fontes.

## Validação executada

- `make verify`: 274 testes aprovados e Ruff aprovado.
- Expansão com `make -n` dos oito novos alvos: aprovada.
- Pipelines reais locais: empresas/emprego, educação, finanças públicas e
  curadoria DCA/SICONFI.
- Pipelines reais externos autorizados: demografia histórica, demografia
  censitária, PIB/VAB municipal e captura DCA/SICONFI.
- Pipeline real da extensão canônica executado duas vezes e comparado por hash.
- Manifestos, validações, cobertura DCA, hashes dos produtos curados e resíduos
  parciais foram examinados.

## Artefatos e arquivos

Arquivos de código/documentação desta etapa:

- `Makefile`, modificado;
- `src/sbmi/canonical_territorial_model_series.py`, criado;
- `src/sbmi/canonical_territorial_model_series_cli.py`, criado;
- `tests/test_canonical_territorial_model_series.py`, criado;
- `docs/canonical_territorial_model_series.md`, criado;
- `docs/project_status_20260813_series_checkpoint.md`, criado.

As oito novas execuções de produto geraram artefatos reconstruíveis em `.data`,
nas camadas aplicáveis `raw`, `staging`, `curated`, `exports` e `audit`. Nenhum
arquivo bruto ou histórico foi modificado, removido, renomeado ou sobrescrito.

## Operações externas e estado de Git

Foram realizadas, após autorização explícita, consultas de baixo volume aos
endpoints oficiais SIDRA/IBGE, FTP/IBGE e DCA/SICONFI. O volume DCA foi de
3.516.945 bytes; o arquivo histórico de PIB teve 2.249.860 bytes, e as demais
respostas foram menores que 200 kB cada. Durante as capturas não houve escrita
no Google Drive; posteriormente, a publicação autorizada criou e preencheu a
nova planilha `v003`, conforme a seção seguinte. Não houve commit, push, criação
ou atualização de pull request, nem merge. O trabalho permanece na branch
`feature/new-files-temporal-coverage`, junto das alterações anteriores ainda
não commitadas.

## Publicação na planilha histórica

A planilha preexistente `v002` foi preservada sem alteração. Foi criada uma
nova cópia dentro de `new_files`:

- título: `São Borja — Base Histórica Sistematizada — 2026-08-13 — v003`;
- ID: `1k15_YX8ufRE1y4xw3BrcmvlY16PEeqXDFe_V2rNl06E`;
- pasta pai: `new_files`, ID `14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`;
- pai confirmado de `new_files`: `_sao_borja`, ID
  `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.

A dimensão de finanças públicas foi publicada no mesmo contrato matricial das
demais dimensões:

- 288 valores observados, de 2019 a 2025;
- 56 linhas de indicador: 15 da série local auditada e 41 combinações
  conta/medida DCA/SICONFI observadas;
- 56 registros de metadados;
- valores somente nas subcolunas `Absoluto`;
- ausências preservadas como células vazias;
- contas, medidas e estágios mantidos separadamente.

Foram atualizadas somente na nova cópia as abas
`09_Financas_Publicas_Dados`, `09_Financas_Publicas_Metadados`,
`01_Cobertura`, `00_Leia_me` e `10_Fontes_Metodo`. A leitura de retorno
reconciliou as 288 células numéricas, 56 IDs, 56 metadados e os anos 2019–2025.
Cabeçalhos, agrupamentos anuais, congelamento e formatação foram verificados
pela API do Google Sheets. A planilha `v002` permaneceu com o registro fiscal
`BLOQUEADO` e com o mesmo horário de modificação observado antes da cópia.

## Recomendações

Próxima ação recomendada: revisar em pull request o mapeamento, a reconciliação
e as limitações conceituais. Somente após essa revisão deve ser decidida uma
eventual promoção do produto paralelo; os canônicos históricos devem permanecer
preservados.
