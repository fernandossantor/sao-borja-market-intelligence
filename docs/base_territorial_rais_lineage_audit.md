# Auditoria de linhagem RAIS

## Objetivo

Comparar fontes preservadas em `raw/rais` com produtos históricos em
`processed/rais`, sem reconstruir, substituir ou promover dados.

## Método

- o par `RAIS SB 2024.csv`/Parquet é declarado explicitamente;
- pares XLSX/Parquet são apenas candidatos formados por nome de arquivo e aba;
- planilhas são lidas com `header=None` e somente margens totalmente vazias são
  removidas;
- valores são canonicalizados sem esconder diferenças textuais ou numéricas;
- todos os pares candidatos são comparados célula a célula.

## Classificações

- `CONTENT_EQUIVALENT`: conteúdo equivalente sob a canonicalização documentada;
- `VALUE_DIFFERENCE`: mesmas dimensões, mas valores divergentes;
- `STRUCTURAL_DIFFERENCE`: dimensões divergentes;
- `NO_NOMINAL_CANDIDATE`: nenhuma hipótese de par pelo nome.

Diferenças de valor são separadas em perda de separador decimal, valor bruto
perdido, valor processado adicionado e outras diferenças.

## Decisões

- equivalência de conteúdo confirma apenas o vínculo de conteúdo observado;
- autoridade, metodologia e adequação analítica continuam não comprovadas;
- qualquer diferença bloqueia o produto processado;
- arquivos `.xls` sem leitor disponível permanecem `NOT_ASSESSED`;
- nenhum arquivo histórico é removido ou substituído;
- `promotion_allowed=0`.

## Mapa de prioridade

O mapa explícito dos pares está documentado em
[`base_territorial_rais_priority_map.md`](base_territorial_rais_priority_map.md).
A decisão atual é não reconstruir: o único par declarado explicitamente já é
`CONTENT_EQUIVALENT`, e os demais não possuem simultaneamente necessidade de
reconstrução, proveniência suficiente e contrato conceitual validado.

## Produtos

- `rais_raw_inventory.csv`;
- `rais_lineage_pairs.csv`;
- `rais_lineage_difference_summary.csv`;
- `rais_lineage_issues.csv`;
- `rais_lineage_summary.csv`;
- `rais_lineage_manifest.csv`.

A escrita usa destino exclusivo, diretório parcial, promoção atômica e recusa
sobrescrita.

## Limitações

- nomes de arquivos e abas formam candidatos, não comprovam linhagem;
- os layouts `.xls` ainda dependem de leitor específico;
- arquivos sem candidato nominal exigem mapeamento explícito;
- a causa histórica das diferenças não é inferida;
- nenhuma análise econômica ou causal é produzida.

## Execução

```bash
make audit-base-territorial-rais-lineage
```
