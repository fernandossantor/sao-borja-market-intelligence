# Validação dos produtos derivados existentes

## Finalidade

Esta etapa não reconstrói `processed`, `exports` nem `warehouse` e não trata a repetição entre essas camadas e `raw` como anomalia. Esses diretórios contêm produtos derivados das fontes brutas; a relação entre eles é esperada.

O objetivo é verificar se os produtos já construídos:

1. estão íntegros e legíveis;
2. apresentam estruturas observáveis e registros utilizáveis;
3. contêm dimensões compatíveis com análise territorial, temporal, categorial e quantitativa;
4. podem ser preservados como produtos históricos ou exigem revisão seletiva.

## Escopo observado em 23 de julho de 2026

- `processed`: 802 arquivos Parquet;
- `exports`: 117 CSV, 2 JSON e 1 Parquet;
- `warehouse`: 1 DuckDB e 1 arquivo WAL auxiliar;
- volume conhecido: aproximadamente 250 MB.

## Processo

### 1. Captura verificada

```bash
make snapshot-derived-products
```

A rotina:

- usa Google Drive API com escopo somente leitura;
- seleciona `processed`, `exports` e `warehouse`;
- preserva os caminhos relativos;
- valida tamanho e SHA-256;
- não executa builders;
- não modifica o Drive;
- publica a captura apenas após concluir todas as verificações.

Saída padrão:

```text
.data/snapshots/derived_products/derived-products-20260723/
```

### 2. Auditoria estrutural

```bash
make audit-derived-products
```

A rotina lê os produtos existentes:

- Parquet: metadados, número de linhas e esquema;
- CSV/TSV/TXT: cabeçalho, linhas e regularidade da largura;
- JSON: estrutura superior, registros e chaves;
- DuckDB: catálogo, tabelas, colunas e linhas;
- WAL: registrado como arquivo auxiliar.

Saída padrão:

```text
.data/audit/derived_products/derived-products-20260723/
```

Relatórios:

- `derived_file_profile.csv`;
- `derived_table_profile.csv`;
- `derived_family_summary.csv`;
- `derived_exact_duplicates.csv`;
- `derived_products_audit_summary.csv`.

## Natureza dos resultados

### Dados observados

- legibilidade;
- formato;
- tamanho;
- quantidade de tabelas;
- quantidade de linhas;
- cabeçalhos;
- assinaturas estruturais;
- duplicidades físicas por SHA-256.

### Estimativas heurísticas

Os sinais de geografia, tempo, medida e categoria são inferidos somente pelos nomes das colunas. A classificação `ANALYTICAL_SIGNAL_PRESENT` indica que a estrutura parece adequada à análise, mas não comprova correção conceitual, unidade, abrangência ou comparabilidade.

### Interpretação posterior

Somente famílias com erro, vazio, estrutura inesperada ou baixa utilidade estimada serão rastreadas seletivamente até os arquivos brutos e builders. Não haverá reprocessamento geral por padrão.

## Limitações

- integridade técnica não comprova correção metodológica;
- número de linhas não comprova completude;
- esquema estável não comprova comparabilidade temporal;
- duplicidade entre camadas derivadas pode ser intencional;
- a utilidade analítica final exige avaliação do significado das variáveis e das necessidades da Base Territorial Comum.
