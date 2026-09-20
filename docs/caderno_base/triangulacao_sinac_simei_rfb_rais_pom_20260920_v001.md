# Triangulação SINAC/SIMEI × RFB/CNPJ × RAIS × inventários POM — v001

**Data:** 20/09/2026  
**Status:** controle conceitual e diagnóstico; não somar bases  
**Geografia:** São Borja/RS

## 1. Objetivo

Triangular as novas estatísticas SINAC/SIMEI com as demais camadas empresariais já existentes no SBMI sem transformar universos distintos em uma única contagem de mercado.

## 2. Camadas e unidades

| Camada | Referência | Valor/estrutura | Unidade analítica | Uso permitido |
|---|---|---:|---|---|
| RFB/CNPJ | ago/2026 | 7.306 | estabelecimentos ativos | estoque cadastral territorial |
| SINAC | posição 12/09/2026 | 7.176 | optantes | estrutura do Simples Nacional |
| SIMEI | posição 12/09/2026 | 4.883 | optantes | estrutura do MEI dentro do universo tributário correspondente |
| RAIS | 31/12/2024 | 13.125 | vínculos ativos válidos | estrutura do emprego formal |
| POM — bens essenciais | 2026 | 54 linhas; 52 CNPJs documentais validados | operadores inventariados | oferta-alvo do estudo POM |
| POM — saúde/higiene | 2026 | 41 linhas; 37 CNPJs únicos extraíveis | linhas/empresas inventariadas | oferta-alvo do estudo POM |
| POM — bens não essenciais | 2026 | 120 linhas; 103 CNPJs únicos extraíveis | linhas/empresas inventariadas | oferta-alvo do estudo POM |
| POM — serviços/alimentação | 2026 | seção com 80 linhas, mas apenas 3 empresas nomeadas | estrutura de trabalho | NÃO usar como inventário censitário |

## 3. Regra de comparabilidade

### Comparação válida dentro do SINAC/SIMEI

Os totais oficiais estão na mesma posição temporal:

- SINAC: 7.176;
- SIMEI: 4.883;
- razão calculada SIMEI/SINAC: **68,05%**.

Fórmula:

`4.883 / 7.176 × 100 = 68,05%`.

### Comparações que não devem ser feitas

Não calcular:

- “cobertura SINAC/RFB”;
- “participação MEI no total de estabelecimentos RFB” usando SIMEI/SINAC;
- razão POM/RFB como cobertura de mercado;
- estabelecimentos por vínculo RAIS como produtividade;
- soma de SINAC + RFB + POM.

Motivo: competência, unidade estatística, regra cadastral e finalidade das bases são distintas.

A proximidade numérica entre 7.176 optantes SINAC e 7.306 estabelecimentos ativos RFB **não demonstra equivalência dos universos**.

## 4. Recortes POM já obtidos dentro do SINAC/SIMEI

Crosswalk conservador CNAE → mercados POM:

| Mercado | SINAC | % SINAC | SIMEI | % SIMEI | SIMEI/SINAC |
|---|---:|---:|---:|---:|---:|
| Bens essenciais | 688 | 9,59% | 398 | 8,15% | 57,85% |
| Saúde/higiene | 95 | 1,32% | 66 | 1,35% | 69,47% |
| Bens não essenciais | 768 | 10,70% | 456 | 9,34% | 59,38% |
| Serviços | 947 | 13,20% | 728 | 14,91% | 76,87% |
| Alimentação fora do lar | 498 | 6,94% | 378 | 7,74% | 75,90% |

Os cinco recortes somam 2.996 SINAC e 2.026 SIMEI, mas isso é **cobertura taxonômica do recorte**, não participação econômica.

## 5. Leitura estrutural permitida

O recorte sugere maior peso relativo do SIMEI em serviços e alimentação fora do lar do que em bens essenciais e bens não essenciais.

Isso pode ser usado como evidência de **atomização/formalização em microescala** dentro do universo de optantes, mas não mede:

- faturamento;
- emprego;
- sobrevivência;
- market share;
- número de pontos físicos;
- capacidade produtiva.

## 6. Inventários POM não são censos

Os inventários POM cumprem função distinta:

- identificam operadores concretos relevantes para a pesquisa;
- permitem estudar redes, presença digital e formatos;
- podem conter duplicidades, baixas e lacunas;
- não devem ser usados como denominador municipal.

Caso emblemático: em bens essenciais, a camada específica já validou 52 CNPJs documentais em 54 linhas, enquanto o parser textual antigo recuperava 47 CNPJs. Para análises futuras, prevalece a camada documental específica.

## 7. RAIS — pendência de reconciliação identificada

Há uma divergência interna a resolver antes de usar o varejo RAIS na triangulação:

- `Analise_multissetorial`: **2.824 vínculos** no varejo;
- `Controle_externo_setorial`: **2.893 vínculos** para CNAE divisão 47.

A diferença pode decorrer de filtros/universos distintos, mas isso ainda não foi documentado nesta etapa.

**Regra provisória:** não usar 2.824 e 2.893 como se fossem a mesma estatística; reconciliar a linhagem do derivado RAIS antes de qualquer comparação com SINAC/RFB.

## 8. Atualização de controle no Drive

A aba `Simples_SIMEI` foi atualizada para retirar o estado obsoleto “valor pendente”:

- SINAC total = 7.176;
- SINAC por CNAE = 427 linhas reconciliadas ao total;
- SIMEI = 4.883;
- razão SIMEI/SINAC = 68,05%.

Os cross-checks secundários antigos permanecem identificados como não aceitos e não substituem os totais oficiais.

## 9. Próximas ações

1. reconciliar 2.824 × 2.893 na RAIS varejo;
2. construir recortes RFB por classes CNAE exatamente compatíveis com cada crosswalk POM, sem usar a divisão 47 ampla como substituta;
3. revalidar atividade atual dos inventários saúde e não essenciais antes de tratar unidades/raízes como estrutura corrente;
4. preservar o inventário de serviços/alimentação do POM como material de pesquisa, não como censo de operadores.

## 10. Status editorial

O crosswalk SINAC/SIMEI da seção 42.94 permanece válido.

Esta triangulação **não gera novo delta quantitativo por si só**; ela consolida regras de uso e abre uma pendência de reconciliação RAIS.

## 11. Governança

- Caderno-Base v028 read-only;
- nenhuma soma entre bases de conceitos distintos;
- PR #41 aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
