# Prioridades práticas da auditoria

## Objetivo

Este registro consolida somente decisões ainda úteis para o projeto. Estados
diagnósticos antigos de origem ou autoridade não são tratados como pendências
quando não afetam duplicidade, interpretação ou transformação.

## 1. Correção reconstruída e integrada — concluída

A execução `demography-census-rebuild-20260729-001426` reconstruiu os dois
produtos em novos destinos de staging e curated. Os históricos permanecem
preservados.

Os dois produtos processados históricos apresentam:

| Produto | Coluna afetada | Células | Diferença observada | Decisão |
|---|---|---:|---|---|
| Composição domiciliar | `porcentagem_de_domicilios` | 3 | fator 100 | reconstruir a partir do arquivo bruto, preservando decimais |
| Território | medidas decimais | 2 | fator 100 | reconstruir a partir do arquivo bruto, preservando decimais |

Os outros 15 pares censitários são equivalentes após canonicalização e não
precisam de nova investigação de conteúdo. A reconstrução deve criar novos
produtos, comparar com os históricos e manter os históricos preservados.

O modelo canônico consome os dois produtos reconstruídos. A execução
`canonical-territorial-20260729-153151` foi comparada com
`canonical-territorial-20260729-025938`: os seis produtos possuem hashes
idênticos e a comparação foi classificada como `IDENTICAL`. O encerramento está
documentado em
[`base_territorial_demography_census_integration.md`](base_territorial_demography_census_integration.md).

## 2. Regra de curadoria das repetições estaduais — resolvida

O arquivo estadual de repasses municipais contém 10 grupos de linhas
estritamente idênticas, com 29 ocorrências e 19 ocorrências excedentes. Todos os
grupos estão na aba `Planilha2` e referem-se a IPVA.

A igualdade de todos os campos observados não comprova lançamento indevido,
pois não foi observada chave transacional capaz de distinguir repasses
legítimos iguais. Decisão atual:

- preservar todas as linhas e sua proveniência;
- manter a sinalização de repetição estrita;
- aplicar `PRESERVE_OCCURRENCES_BLOCK_AGGREGATION`;
- não deduplicar nem somar silenciosamente;
- permitir somente análises de sensibilidade explicitamente rotuladas;
- manter `promotion_allowed=0` enquanto os demais bloqueios fiscais não forem
  resolvidos.

A auditoria registra a decisão por grupo em
`state_repetition_decisions.csv`.

## 3. Encerrar como duplicidade de conteúdo — resolvido

Os arquivos de cofinanciamento da proteção social básica, com e sem sufixo
`(1)`, possuem 64 linhas e conteúdo normalizado idêntico, apesar de hashes
binários diferentes.

A cópia com sufixo já foi excluída do staging. Ambos os arquivos brutos devem
permanecer preservados. Não há ação adicional necessária.

## 4. Excluir da cobertura analítica — prioridade baixa

O inventário registra 15 grupos de duplicidade binária exata:

- 14 grupos em produtos derivados, principalmente layouts, notas ou arquivos
  auxiliares;
- 1 grupo de observações BACEN repetido nas pastas de aposentados e
  pensionistas.

Esses arquivos não devem ser apagados. Para fins de cobertura e seleção de
indicadores, cada grupo conta no máximo uma vez e arquivos meramente técnicos
não contam como evidência analítica própria.

## Ordem recomendada atualizada

1. não gastar nova etapa com duplicidades auxiliares já classificadas;
2. manter os contratos fiscais bloqueados até resolver seus bloqueios próprios.
