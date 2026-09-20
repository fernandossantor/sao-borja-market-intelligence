# Nota de correção — FPM na série SICONFI/DCA — hierarquia de contas 2022–2025

**Data da correção:** 20/09/2026  
**Geografia:** São Borja/RS  
**Fonte:** Tesouro Nacional — SICONFI/DCA, Anexo I-C  
**Unidade:** R$ correntes por exercício

## 1. Problema identificado

A auditoria analítica da série fiscal reconciliada revelou dupla contagem do FPM em 2022–2025. A extração anterior somava a conta agregada de FPM e suas contas-filhas, embora os valores dos filhos já estivessem contidos no pai.

A mudança decorre da estrutura hierárquica observada a partir de 2022. Exemplo de 2022:

- conta agregada FPM: R$ 48.899.545,72;
- cota mensal: R$ 46.403.103,10;
- cota adicional de julho: R$ 2.114.404,04.

Os dois filhos somam exatamente o valor do agregado. Somar pai + filhos produzia R$ 97.417.052,86 e duplicava a grandeza.

## 2. Regra corrigida

A regra canônica passou a ser:

1. identificar todas as contas cujo rótulo corresponde ao FPM;
2. verificar a hierarquia dos códigos;
3. quando existir conta agregada ancestral, manter o pai e excluir seus filhos da soma;
4. quando não existir pai agregador explícito — estrutura observada em 2019–2021 — somar apenas os componentes disjuntos;
5. preservar todas as candidatas no arquivo de auditoria e marcar quais foram selecionadas.

## 3. Valores corrigidos

| Ano | FPM bruto anterior | FPM bruto corrigido | Natureza da correção |
|---:|---:|---:|---|
| 2019 | R$ 33.514.887,07 | R$ 33.514.887,07 | sem alteração |
| 2020 | R$ 32.481.383,49 | R$ 32.481.383,49 | sem alteração |
| 2021 | R$ 42.878.260,89 | R$ 42.878.260,89 | sem alteração |
| 2022 | R$ 97.417.052,86 | **R$ 48.899.545,72** | remoção de pai+filhos duplicados |
| 2023 | R$ 116.295.525,78 | **R$ 58.147.762,89** | remoção de pai+filhos duplicados |
| 2024 | R$ 133.927.772,52 | **R$ 66.963.886,26** | remoção de pai+filhos duplicados |
| 2025 | R$ 150.752.908,66 | **R$ 75.376.454,33** | remoção de pai+filhos duplicados |

Valores líquidos corrigidos após dedução Fundeb:

- 2022: R$ 39.618.925,36;
- 2023: R$ 47.565.835,14;
- 2024: R$ 54.824.338,86;
- 2025: R$ 61.955.700,64.

## 4. Impacto analítico

A correção altera somente os indicadores derivados do subcomponente **FPM**. Não altera:

- receita corrente bruta;
- transferências correntes brutas;
- participação transferências/receita;
- despesa paga;
- VAF;
- conclusões já registradas sobre ritmos distintos entre VAF e circuito fiscal.

O pipeline foi corrigido no workflow `sao-borja-public-accounts-dca-series-reconcile.yml`, commit **a8f005e034fc10e6c6d4bf294df3ada4a352362c**. A reexecução concluiu com sucesso e passou a produzir a série canônica com seleção hierárquica não sobreposta.

## 5. Controle editorial

Qualquer tabela, gráfico ou nota futura que apresente FPM 2022–2025 deve usar a série corrigida. O Caderno-Base v028 permanece read-only e não foi alterado.
