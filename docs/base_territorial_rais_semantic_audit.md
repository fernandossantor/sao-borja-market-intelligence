# Auditoria semântica da família RAIS

## Objetivo

Auditar localmente os produtos históricos agrupados sob `processed/rais` e os
exports `rais_*`, sem presumir que o nome da pasta comprove origem, autoridade
ou equivalência conceitual.

## Escopo

A rotina registra arquivos, tamanhos, linhas, colunas, esquemas, hashes,
duplicidades binárias, contratos dos exports, cobertura semântica, períodos
futuros e colunas monetárias textuais. As funções atribuídas aos arquivos são
apenas pistas derivadas do nome e ficam marcadas como `FILE_NAME_ONLY`.

## Decisões

- nenhum arquivo é removido por duplicidade;
- anos futuros não são classificados automaticamente como projeção ou erro;
- valores monetários não são convertidos sem contrato de localidade e unidade;
- produtos históricos não são promovidos para `curated`;
- `promotion_allowed=0` até revisão de fonte, metodologia e comparabilidade.

## Produtos

Cada execução cria um destino exclusivo contendo:

- `rais_processed_inventory.csv`;
- `rais_export_contracts.csv`;
- `rais_exact_duplicate_groups.csv`;
- `rais_semantic_mapping_summary.csv`;
- `rais_semantic_issues.csv`;
- `rais_semantic_summary.csv`;
- `rais_semantic_manifest.csv`.

A escrita é atômica, preserva hashes e recusa sobrescrita.

## Limitações

- igualdade binária não determina redundância conceitual;
- nomes e estruturas não comprovam autoridade da fonte;
- o diagnóstico de período futuro não prova projeção;
- o conteúdo das tabelas SIDRA candidatas não é validado contra a API;
- nenhuma inferência econômica ou causal é produzida.

## Execução

```bash
make audit-base-territorial-rais-semantics
```
