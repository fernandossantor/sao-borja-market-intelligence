# Matriz temporal das fontes complementares

## Objetivo

Registrar, para cada dimensão, indicador, ano e fonte, se existe evidência
observada entre 1996 e 2026. A matriz combina a presença do modelo canônico
com os contratos complementares já classificados, sem declarar equivalência
entre indicadores e sem promover valores.

## Regras

- somente as dez dimensões existentes são aceitas;
- anos intermediários nunca são inferidos a partir do primeiro e do último ano;
- cada célula recebe `OBSERVED` ou `GAP`;
- nomes semelhantes permanecem como contratos distintos;
- duplicidades, chaves técnicas e contratos descartados não entram na fila;
- a prioridade mede volume temporal observado, não qualidade ou autoridade.

## Saídas

```text
.data/audit/base_territorial/complementary_temporal_matrix/<run_id>/
├── temporal_evidence_matrix.csv
├── indicator_temporal_coverage.csv
├── dimension_priority.csv
└── validation.csv
```

Execução:

```bash
make audit-complementary-temporal-matrix
```
