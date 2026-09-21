# Preços Dinâmicos — série histórica PCA-RE Fronteira Oeste × RS — seed auditável — v001

**Data:** 20/09/2026  
**Fonte:** Receita Estadual/SEFAZ-RS — Boletins de Preços Dinâmicos  
**Indicador:** PCA-RE — Preço da Cesta de Alimentos  
**Geografias:** COREDE Fronteira Oeste e Rio Grande do Sul  
**Status:** série parcial em construção; não substituir o benchmark de agosto/2026 já promovido.

## 1. Objetivo

Construir uma série mensal reproduzível Fronteira Oeste × Rio Grande do Sul sem interpolar, estimar ou reconstruir silenciosamente competências ausentes.

Regra:

> somente observações diretamente verificadas em publicação oficial entram como DADO_OBSERVADO.

## 2. Observações validadas no seed

| Competência | Fronteira Oeste | RS | Situação |
|---|---:|---:|---|
| jul/2024 | R$ 248,70 | R$ 258,80 | âncora histórica oficial |
| nov/2024 | R$ 270,33 | R$ 283,92 | âncora histórica oficial |
| mar/2026 | R$ 274,55 | R$ 287,85 | observação corrigida após auditoria cruzada |
| ago/2026 | R$ 284,19 | R$ 298,61 | benchmark corrente já promovido |

## 3. Março/2026 — nova validação

Tabela oficial do boletim de referência março/2026:

### COREDE Fronteira Oeste
- PCA-RE: **R$ 274,55**;
- variação mensal: **+0,21%**;
- acumulado no ano: **-1,45%**;
- 12 meses: **-3,22%**.

### Rio Grande do Sul
- PCA-RE: **R$ 287,85**;
- variação mensal: **-0,17%**;
- acumulado no ano: **-1,16%**;
- 12 meses: **-2,84%**.

### Diferença de nível

Fórmula:

`(274,55 / 287,85 - 1) × 100 = -4,62%`.

**Dado calculado:** em março/2026, o PCA-RE da Fronteira Oeste estava aproximadamente **4,62% abaixo** do nível estadual.

Isso não significa que famílias de São Borja pagavam 5,28% menos nem que todos os itens tinham preços inferiores.

## 3.1. Auditoria corretiva do valor estadual de março/2026

**Dado observado em fonte primária:** o Portal do Estado do Rio Grande do Sul, em notícia da Secretaria da Fazenda publicada em 02/04/2026, informa PCA-RE estadual de **R$ 287,85**, queda mensal de **0,17%** e variação de **-2,84% em 12 meses**.

**Checagem calculada de consistência:** fevereiro/2026 havia fechado em R$ 288,33. A variação de R$ 288,33 para R$ 287,85 é de aproximadamente **-0,17%**, coerente com a variação mensal publicada.

O valor **R$ 289,85**, antes transcrito no seed, é incompatível com a fonte primária e com a própria variação mensal. Foi, portanto, classificado como **erro de transcrição** e invalidado.

Fonte primária: Portal do Estado do Rio Grande do Sul / Ascom Sefaz, 02/04/2026, “Preço médio da cesta de alimentos tem queda em março no Rio Grande do Sul”.

## 4. Leitura temporal permitida

Entre março e agosto de 2026:

- Fronteira Oeste: R$ 274,55 → R$ 284,19;
- RS: R$ 287,85 → R$ 298,61.

Esse avanço de nível é descritivo e não substitui a série mensal intermediária.

Não calcular volatilidade, sazonalidade, tendência mensal ou decomposição por produto enquanto as competências faltantes não forem preenchidas.

## 5. Lacunas atuais

Para a sequência mensal de 2026, permanecem não reproduzidas no seed:

- janeiro;
- fevereiro;
- abril;
- maio;
- junho;
- julho.

Os boletins oficiais existem, mas parte dos PDFs/visuais não foi recuperável de forma estável na sessão de auditoria.

Não reconstruir valores a partir de percentuais arredondados de meses posteriores.

## 6. Próximo gate

Prioridade de preenchimento:

1. PCA-RE FO × RS — jan–ago/2026 completo;
2. arroz;
3. feijão;
4. leite;
5. pão;
6. carnes;
7. frango;
8. ovos;
9. óleo;
10. café;
11. frutas/hortaliças.

Cada observação deve registrar:

- competência;
- produto/grupo;
- unidade;
- geografia;
- valor;
- variação mensal;
- acumulado no ano;
- 12 meses;
- fonte;
- natureza do dado.

## 7. Status editorial

**NÃO CRIAR NOVO DELTA APENAS PELO SEED.**

O bloco de agosto/2026 da seção 42.96 continua sendo o benchmark regional maduro.

A série histórica será promovida somente quando possuir cobertura mensal suficiente para sustentar leitura temporal sem saltos arbitrários.

## 8. Artefato estruturado

- `docs/data_sources/precos_dinamicos_pca_fo_rs_historico_seed_20260920_v001.csv`.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- novas evidências entram apenas no sucessor;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
