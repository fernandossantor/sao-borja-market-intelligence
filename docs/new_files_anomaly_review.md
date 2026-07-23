# Revisão de anomalias de `raw/new_files`

## Objetivo

Detalhar os achados da auditoria de conteúdo antes de qualquer decisão de exclusão, consolidação ou transformação das bases.

A rotina trabalha somente com a captura local imutável e com o perfil estrutural. Ela não acessa nem altera o Google Drive.

## Achados que motivaram a revisão

- um par federal com conteúdo normalizado idêntico;
- uma tabela estadual com 19 linhas excedentes por repetição;
- datas estaduais posteriores à data da captura;
- aviso de interpretação genérica de datas, que exige inspeção explícita do formato de origem.

## Saídas

```text
.data/audit/new_files/anomaly_review/<snapshot_id>/
```

Arquivos produzidos:

- `anomaly_review_summary.csv`: indicadores agregados e natureza de cada indicador;
- `content_duplicate_pairs.csv`: pares com conteúdo normalizado idêntico, SHA-256 binário e sugestão heurística de arquivo principal;
- `duplicate_row_groups.csv`: grupos de linhas repetidas, quantidade de ocorrências, números das linhas de origem e valores observados em JSON;
- `temporal_table_summary.csv`: resumo por tabela temporal, tipos de origem, período, ambiguidades e valores futuros;
- `temporal_anomalies.csv`: cada valor temporal futuro, ambíguo ou não interpretado.

## Duplicidade de arquivos

A rotina distingue:

- `EXACT_DUPLICATE`: conteúdo e arquivo binário idênticos;
- `CONTENT_DUPLICATE`: conteúdo tabular normalizado idêntico, mas arquivo binário diferente.

Quando apenas um dos nomes termina em sufixo como `(1)`, o arquivo sem o sufixo é indicado como candidato principal por `COPY_SUFFIX_HEURISTIC`.

Essa indicação é uma recomendação operacional provisória. Nenhum arquivo é excluído ou movido automaticamente.

## Linhas repetidas

Cada grupo é classificado como:

- `STRICT_EXACT_ROW`: todas as ocorrências são idênticas sem normalização;
- `NORMALIZED_EQUIVALENT_ROW`: as ocorrências coincidem após normalização de espaços, caixa e diacríticos.

A presença de linhas repetidas não comprova erro da fonte. Repasses distintos podem compartilhar todos os campos disponíveis. A decisão exige revisão da fonte e da granularidade.

## Auditoria temporal

As datas são interpretadas apenas por formatos explícitos. A data da captura funciona como referência para identificar valores futuros.

Classes registradas:

- `FUTURE_DATE`: data interpretada posterior à captura;
- `AMBIGUOUS_DATE`: texto compatível tanto com dia/mês quanto com mês/dia;
- `AMBIGUOUS_DATE_POSSIBLE_REVERSAL`: a leitura dia/mês produz data futura, mas a alternativa mês/dia não;
- `PARSE_FAILURE`: valor não vazio que não corresponde aos formatos reconhecidos.

Datas futuras podem ser válidas em bases orçamentárias ou planejadas. A classificação apenas exige validação metodológica.

## Natureza dos resultados

### Dados observados

- valores e tipos originais das células temporais;
- números das linhas de origem;
- caminhos e nomes dos arquivos;
- hashes binários locais.

### Dados calculados

- hashes normalizados de linhas e conteúdo;
- grupos e excesso de linhas repetidas;
- datas interpretadas e alternativas;
- contagens de valores futuros ou ambíguos.

### Recomendações provisórias

- preservar o arquivo sem `(1)` como candidato principal quando o conteúdo é idêntico;
- manter o arquivo com `(1)` até o encerramento formal da auditoria;
- não remover linhas estaduais antes de confirmar a granularidade e a origem;
- não usar datas estaduais futuras em séries históricas antes de validar o formato.

## Execução

```bash
make review-inbox-anomalies
```
