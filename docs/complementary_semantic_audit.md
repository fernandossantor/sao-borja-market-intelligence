# Auditoria semântica das fontes complementares

## Objetivo

Classificar os contratos coletados do Censo 2022, IBGE Cidades, Observatório
Sebrae e IPS Brasil antes de qualquer integração ao modelo territorial
canônico.

A auditoria não modifica capturas, não grava no Google Drive e não promove
linhas ao modelo canônico.

## Classes

- `CONTENT_DUPLICATE`: conteúdo reconciliado por nome, período e valor;
- `PARTIAL_OVERLAP`: fonte, conceito ou período sobrepõe parcialmente uma base
  existente, sem equivalência integral comprovada;
- `COMPLEMENTARY`: medida ainda não representada no módulo local comparado;
- `CONFLICT`: mesmo indicador e período com valor divergente;
- `UNIQUE`: chave técnica ou categoria sem papel de medida analítica.

`UNIQUE` não significa que a informação deva ser integrada. Chaves
territoriais, períodos e desagregações recebem
`EXCLUDE_TECHNICAL_KEY`.

## Regras

1. Os dez blocos analíticos existentes são preservados.
2. No Sebrae, somente campos declarados em `measures` são tratados como
   medidas. Campos de `drilldowns` e identificadores são chaves técnicas.
3. As sobreposições com RAIS, SIDRA, censo e staging fiscal permanecem
   `PARTIAL_OVERLAP` até comparação conceitual e de valores específica.
4. Os dezesseis agregados IPS são comparados com o módulo IPS publicado por
   nome normalizado, edição e valor.
5. Indicadores individuais IPS ausentes no módulo existente são
   `COMPLEMENTARY`, mas continuam sujeitos à revisão de unidade, fonte
   primária e comparabilidade.
6. Correspondência nominal isolada nunca produz `CONTENT_DUPLICATE`.

## Saídas

```text
.data/audit/base_territorial/complementary_semantic_audit/<audit_id>/
├── indicator_semantic_register.csv
├── classification_summary.csv
├── dimension_summary.csv
├── ips_reconciliation.csv
└── validation.csv
```

Execução:

```bash
python -m sbmi.complementary_semantic_audit_cli
```
