# Triagem estrutural de `raw/new_files`

## Objetivo

Resumir as estruturas identificadas no perfil local e localizar candidatos de sobreposição parcial antes de qualquer consolidação de bases.

A rotina trabalha somente com os relatórios produzidos pelo perfil estrutural. Ela não altera a captura local e não acessa o Google Drive.

## Entradas

Por padrão, são utilizados os arquivos da captura perfilada mais recente:

```text
.data/audit/new_files/content_profile/<snapshot_id>/sheet_profile.csv
.data/audit/new_files/content_profile/<snapshot_id>/column_profile.csv
```

## Saídas

```text
.data/audit/new_files/structure_triage/<snapshot_id>/
```

Arquivos gerados:

- `table_registry.csv`: registro por tabela, origem declarada, dimensões, período observado e grupo estrutural;
- `schema_summary.csv`: resumo por assinatura exata de cabeçalhos;
- `source_summary.csv`: tabelas, arquivos e assinaturas por origem declarada;
- `header_similarity_candidates.csv`: pares de tabelas com sobreposição parcial estimada de cabeçalhos.

## Classificações

- `REPEATED_EXACT`: a assinatura normalizada dos cabeçalhos aparece em mais de uma tabela;
- `SINGLETON`: a assinatura aparece uma única vez;
- `NO_SIGNATURE`: não foi possível calcular uma assinatura estrutural.

## Similaridade parcial

A rotina compara tabelas com assinaturas diferentes por três medidas calculadas:

- Jaccard entre os conjuntos de cabeçalhos;
- contenção do menor conjunto de cabeçalhos no maior;
- similaridade da sequência ordenada dos cabeçalhos.

Um par é registrado quando o Jaccard é pelo menos 0,60 ou a contenção é pelo menos 0,80. A classificação é:

- `NEAR_SCHEMA`: Jaccard igual ou superior a 0,80;
- `PARTIAL_SCHEMA`: demais pares que superam os limiares.

## Natureza dos resultados

### Dados observados

- caminhos e origens declaradas;
- dimensões e anos já registrados no perfil;
- igualdade exata da assinatura de cabeçalhos.

### Dados calculados

- tamanho dos grupos estruturais;
- quantidades por origem;
- índices de Jaccard, contenção e similaridade sequencial.

### Hipóteses para investigação

Os pares listados em `header_similarity_candidates.csv` são candidatos de sobreposição estrutural. Eles não comprovam:

- igualdade de conteúdo;
- continuidade temporal;
- mesma unidade de medida;
- mesma abrangência territorial;
- mesma chave de identificação;
- possibilidade de consolidação automática.

## Execução

```bash
make triage-inbox-structure
```
