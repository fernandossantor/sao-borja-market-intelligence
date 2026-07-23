# Auditoria de conteúdo de `raw/new_files`

## Objetivo

Examinar os conteúdos da captura local para identificar períodos observados, duplicidades internas e sobreposições de linhas entre as tabelas federais antes de qualquer consolidação.

A rotina lê somente a captura imutável e o perfil estrutural já produzido. Ela não acessa nem altera o Google Drive.

## Correção metodológica dos períodos

A detecção anterior de anos pesquisava sequências de quatro dígitos em todas as células. Esse procedimento pode interpretar partes de códigos, identificadores, empenhos, CPF/CNPJ ou outros números como anos.

Nesta etapa, datas são interpretadas somente quando existe uma coluna temporal explicitamente reconhecida, como:

- `mes_ano`;
- `data`;
- `competencia`;
- `ano_mes`;
- `mes_competencia`;
- `data_pagamento`;
- `data_lancamento`.

Por isso, os intervalos produzidos nesta auditoria substituem, para fins temporais, os intervalos heurísticos gerais do perfil estrutural.

## Saídas

```text
.data/audit/new_files/content_audit/<snapshot_id>/
```

Arquivos gerados:

- `content_audit_summary.csv`: indicadores agregados e natureza de cada indicador;
- `table_content_summary.csv`: linhas, duplicidades internas, coluna temporal, taxa de interpretação e período por tabela;
- `federal_row_overlap_candidates.csv`: pares federais com pelo menos uma linha normalizada em comum;
- `content_audit_errors.csv`: erros por tabela, quando existirem.

## Normalização de conteúdo

A comparação entre linhas:

- remove espaços excedentes;
- ignora diferenças de maiúsculas e minúsculas;
- remove marcas diacríticas para a comparação;
- preserva a posição das colunas;
- representa datas e números de forma estável;
- calcula SHA-256 por linha e por conjunto de linhas.

A normalização serve para localizar candidatos. Ela não prova equivalência metodológica entre fontes.

## Classes de sobreposição federal

- `IDENTICAL_NORMALIZED_CONTENT`: os arquivos possuem o mesmo multiconjunto de linhas normalizadas;
- `LEFT_CONTAINED_IN_RIGHT`: todas as linhas únicas da tabela esquerda aparecem na direita;
- `RIGHT_CONTAINED_IN_LEFT`: todas as linhas únicas da tabela direita aparecem na esquerda;
- `PARTIAL_ROW_OVERLAP`: existe interseção, mas nenhuma tabela está integralmente contida na outra.

## Natureza dos resultados

### Dados observados

- valores das colunas temporais reconhecidas;
- quantidade de linhas carregadas;
- arquivos, planilhas e caminhos;
- presença de colunas temporais.

### Dados calculados

- linhas únicas normalizadas;
- duplicidades internas;
- períodos mínimo e máximo após interpretação das datas;
- hashes de conteúdo;
- interseções, Jaccard e contenção entre tabelas federais.

### Hipóteses

Um par classificado como idêntico, contido ou parcialmente sobreposto é candidato a revisão. A classificação não comprova:

- mesma unidade de medida;
- mesma abrangência territorial;
- mesma definição de programa ou ação;
- duplicidade administrativa;
- possibilidade de exclusão ou consolidação automática.

## Execução

```bash
make audit-inbox-content
```
