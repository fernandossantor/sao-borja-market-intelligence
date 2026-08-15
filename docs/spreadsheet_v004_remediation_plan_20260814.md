# Plano de remediação da planilha v004 — 2026-08-14

## Objetivo

Definir uma correção incremental da planilha `São Borja — Base Histórica
Sistematizada — 2026-08-13 — v004` sem alterar a versão existente. Uma futura
publicação deve usar novo identificador, tratada neste plano como `v005`, e
somente poderá ser criada após autorização específica para escrita externa.

O plano parte da reconciliação documentada em
`docs/spreadsheet_v004_canonical_reconciliation_20260814.md` e dos artefatos
locais da execução `spreadsheet-v004-vs-canonical-20260814-001`.

## Escopo

O trabalho está dividido em quatro frentes independentes:

1. corrigir a semântica das contagens de cobertura;
2. preparar a inclusão dos 46 fatos canônicos ausentes;
3. manter separados os 589 valores da planilha ainda fora do canônico, com a
   linhagem disponível reconciliada e a promoção bloqueada;
4. acrescentar proveniência verificável à futura publicação.

Este documento não autoriza escrita no Google Drive, promoção de dados ao
canônico, reconstrução de capturas ou substituição de qualquer produto.

## Estado observado

| Medida | Quantidade |
| --- | ---: |
| Fatos no canônico local | 3.041 |
| Valores numéricos na v004 | 3.584 |
| Valores reconciliados | 2.995 |
| Fatos canônicos ausentes na v004 | 46 |
| Valores adicionais na v004 | 589 |

A relação observada é:

```text
3.041 - 46 + 589 = 3.584
```

Não há diferença aritmética não explicada. Isso não elimina as lacunas de
cobertura e proveniência.

## Frente 1 — cobertura

### Problema observado

A v004 não emprega uma definição uniforme para a contagem publicada. Em
Demografia, o valor 102 corresponde às linhas de séries, embora existam 495
valores numéricos. Em Economia, o valor 31 não corresponde às 10 linhas de
séries nem aos 209 valores numéricos. Nas outras seis dimensões, a contagem
coincide com os valores numéricos.

### Alteração planejada

A futura aba de cobertura deve separar explicitamente:

- `series_rows`: quantidade de linhas de séries na matriz;
- `unique_indicators`: quantidade de identificadores únicos;
- `numeric_observations`: quantidade de células numéricas publicadas;
- `reference_period_min`: primeiro período observado;
- `reference_period_max`: último período observado;
- `publication_status`: estado da dimensão;
- `limitations`: restrições de cobertura e comparabilidade.

Nenhuma das três contagens deve ser apresentada sob o rótulo genérico
`linhas publicadas`.

### Critérios de aceitação

- as oito dimensões usam as mesmas definições;
- os totais são recalculados diretamente das abas de dados;
- células vazias não são contadas como observações;
- categorias repetidas contam como linhas de séries, mas não como novos
  indicadores;
- a documentação da aba explica as três métricas.

## Frente 2 — fatos canônicos ausentes

### Escopo observado

| Bloco | Fatos ausentes | Classificação atual |
| --- | ---: | --- |
| Composição domiciliar — Panorama do Censo | 3 | `ERROR` |
| VAB total — metodologia atual | 20 | `ERROR` |
| Impostos líquidos de subsídios — metodologia atual | 20 | `ERROR` |
| Impostos líquidos de subsídios — metodologia 1999–2001 | 3 | `ERROR` |
| **Total** | **46** | **`ERROR`** |

### Preparação local concluída

Uma execução posterior preparou os 46 fatos com:

- chave determinística de indicador, categoria e período;
- unidade e natureza do valor;
- fonte e arquivo de entrada imediata;
- SHA-256 da entrada preservada;
- identificador da execução canônica;
- transformação aplicada;
- limitação e status de comparabilidade;
- posição planejada na matriz da futura planilha.

Os três fatos de composição domiciliar não devem ser combinados com as
categorias SIDRA existentes apenas por proximidade temática. Os 43 fatos
econômicos devem permanecer separados por metodologia.

O pacote local
`spreadsheet-v005-missing-facts-publication-package-20260814-001` registrou 46
fatos, 46 células únicas e três entradas upstream distintas. Os hashes dos
arquivos originais e imediatos foram recalculados e coincidiram. A URL e o
horário de obtenção do XLSX censitário não estão comprovados nos manifestos
preservados e foram registrados como `EVIDENCE_NOT_AVAILABLE`, sem inferência.

### Critérios de aceitação

- 46 fatos preparados e 46 fatos publicados;
- zero colisões de indicador, categoria, período e tipo de valor;
- zero sobrescritas de células preexistentes;
- unidades e metodologias preservadas;
- reconciliação exata contra o canônico local.

## Frente 3 — valores adicionais da v004

### Escopo observado

| Bloco | Valores adicionais | Reconciliação de linhagem | Decisão atual |
| --- | ---: | --- | --- |
| Demografia | 9 | conteúdo e hashes locais reconciliados | preservar sem promover |
| Retrato empresarial | 11 | arquivo citado no Drive, conteúdo e hash reconciliados | preservar sem promover |
| Despesas públicas por função | 569 | conteúdo e hashes DCA locais reconciliados | preservar sem promover |
| **Total** | **589** | **589 valores reconciliados** | **preservar sem promover** |

### Política planejada

Os valores podem permanecer na futura planilha como conteúdo publicado
preexistente, desde que sejam identificados como ainda não integrados ao
canônico. A permanência na planilha e a reconciliação da linhagem disponível
não constituem aprovação metodológica nem promoção para `curated`.

As auditorias locais próprias registraram:

- Demografia: nove valores reconciliados com as capturas SIDRA preservadas;
- Empresas: onze valores reconciliados com o arquivo citado pela v004, cujo
  SHA-256 binário foi recalculado;
- Finanças: 569 valores reconciliados com as capturas DCA preservadas.

Ainda é necessário modelar explicitamente os três blocos em pipelines
canônicos incrementais antes de qualquer promoção. As quatro séries fiscais
sem observações numéricas permanecem registradas separadamente como séries
vazias, sem valores a reconciliar.

### Critérios de aceitação

- todos os 589 valores reconciliados e rotulados como fora do canônico;
- nenhuma classificação `UNEXPLAINED`;
- zero conflitos de conteúdo ou valores sem evidência de origem disponível;
- nenhuma agregação entre conceitos incompatíveis;
- nenhuma promoção automática;
- decisão individual de preservação, quarentena ou futura promoção por bloco.

## Frente 4 — proveniência

### Lacunas observadas

As abas de metadados da v004 não registram por linha:

- SHA-256 do arquivo original;
- identificador ou caminho da captura;
- URL original e URL final efetivamente obtida;
- data e hora de obtenção;
- identificador da execução;
- tamanho do arquivo de entrada;
- transformações aplicadas.

### Estrutura planejada

A futura publicação deve incluir um manifesto próprio, separado das matrizes
analíticas, com pelo menos:

- identificador estável do registro;
- indicador e categoria;
- período de referência;
- instituição e fonte declarada;
- URL original e URL final;
- data e hora de obtenção;
- arquivo ou captura de origem;
- tamanho em bytes e SHA-256;
- execução produtora;
- transformação;
- status de auditoria;
- limitações conhecidas.

O manifesto deve permitir rastrear cada valor até sua entrada imediata e,
quando possível, até a fonte original. Campos indisponíveis devem registrar
ausência de evidência, nunca valores presumidos.

### Critérios de aceitação

- 100% dos valores possuem vínculo com um registro de manifesto;
- hashes são recalculados e comparados com os manifestos locais disponíveis;
- URLs finais respeitam HTTPS, domínio e tipo de conteúdo esperados;
- diferenças de linhagem permanecem explícitas;
- nenhuma credencial ou token é incluído.

## Estratégia de publicação futura

### Pacote integrado local

A execução
`spreadsheet-v005-integrated-package-20260814-001` consolidou, sem modificar
as entradas:

- o manifesto dos 46 fatos e das três fontes upstream;
- os payloads de seis linhas de dados, seis linhas de metadados e 46 células;
- a proposta uniforme de cobertura;
- os 589 valores adicionais preservados e as decisões de prontidão.

Dez componentes foram fixados por tamanho e SHA-256. As 16 validações
integradas foram aprovadas, com 413 linhas de séries, 319 indicadores únicos e
3.630 observações numéricas propostas. O pacote permanece exclusivamente
local e todos os payloads estão marcados como `PREPARED_NOT_PUBLISHED`.

Uma eventual publicação deve seguir:

```text
inventário da v004
  → construção de cópia de trabalho com novo identificador
  → aplicação das mudanças em escopo delimitado
  → validação integral
  → reconciliação v005 × canônico
  → decisão explícita de publicação
```

Requisitos operacionais:

1. preservar a v004 sem edição, renomeação, movimentação ou exclusão;
2. confirmar o destino autorizado antes de qualquer escrita;
3. recusar colisões de nome, ID ou caminho;
4. aplicar mudanças em produto novo;
5. validar antes da disponibilização final;
6. manter manifesto da operação externa;
7. interromper a publicação diante de qualquer diferença `UNEXPLAINED`.

Copiar ou criar uma planilha no Drive, mesmo sem publicá-la como definitiva,
é escrita externa e exige autorização específica.

## Validação da futura v005

A validação deve examinar:

- esquema e cabeçalhos das abas;
- unicidade das chaves de séries;
- tipos e unidades;
- células ausentes e duplicidades;
- cobertura temporal;
- contagens por dimensão;
- correspondência célula a célula com o canônico;
- preservação dos 589 valores adicionais;
- hashes e proveniência;
- comparação com a v004;
- classificação e justificativa de todas as diferenças.

Critérios globais:

```text
fatos canônicos representados = 3.041
fatos canônicos ausentes = 0
diferenças UNEXPLAINED = 0
sobrescritas da v004 = 0
```

A aprovação de fórmulas ou testes automatizados não substitui a inspeção das
abas e dos artefatos produzidos.

## Estratégia de reversão

Como a v004 permanece imutável, a reversão consiste em não promover a nova
publicação. Uma execução parcial deve ser removida apenas quando isso puder ser
feito com segurança e sem atingir artefatos preexistentes. Se uma planilha
nova já tiver sido criada externamente, qualquer exclusão exigirá autorização
específica; na ausência dela, o produto deve permanecer identificado como
rascunho ou quarentena.

## O que pode ser concluído

- As quatro frentes necessárias estão delimitadas.
- Os totais usados no planejamento reconciliam com a auditoria local.
- É possível corrigir a cobertura sem promover os 589 valores ao canônico.
- A preservação da v004 permite comparação e reversão não destrutiva.
- Os 46 fatos e o pacote integrado da proposta v005 estão preparados e
  validados localmente.

## O que não pode ser concluído

- Que a preparação local dos 46 fatos autorize escrita externa.
- Que a linhagem reconciliada dos 589 valores seja suficiente para promoção
  sem modelagem conceitual e integração incremental ao canônico.
- Que uma v005 possa ser publicada sem inventário atualizado do destino.
- Que os campos de proveniência ausentes possam ser preenchidos sem consultar
  evidências de origem.

## Próximas autorizações necessárias

Devem permanecer separadas:

1. leitura externa para inventariar novamente a planilha e o destino;
2. preparação local dos 46 fatos e do manifesto completo;
3. criação da nova planilha no Drive;
4. escrita dos dados e metadados;
5. publicação ou disponibilização da v005.

Nenhuma dessas operações é autorizada por este plano.

## Estado desta etapa

Esta etapa cria somente documentação local. Não acessa serviços externos, não
modifica `.data`, não executa pipeline de transformação e não altera arquivos
brutos, snapshots ou produtos históricos. Não realiza commit, push, criação ou
atualização de pull request, nem merge.
