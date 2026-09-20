# Preços Dinâmicos — Fronteira Oeste como benchmark regional de São Borja — ago/2026 — v002

**Data:** 20/09/2026  
**Competência:** agosto/2026  
**Geografia pública:** COREDE Fronteira Oeste e Rio Grande do Sul  
**Fonte:** Receita Estadual/SEFAZ-RS — Preços Dinâmicos / Boletim ed. 25  
**Base:** NFC-e, com processamento metodológico documentado nas NT CIET 01/2026 e 04/2026  
**Status:** benchmark regional apto à inclusão; não é preço municipal de São Borja.

## 1. Regra territorial

A publicação pública de preços é agregada por COREDE.

São Borja pertence ao **COREDE Fronteira Oeste**.

Portanto:

> `Fronteira Oeste = região de referência de São Borja`.

Nunca escrever:
> “preço de São Borja”

quando o dado publicado é do COREDE.

## 2. Natureza do indicador

O projeto utiliza NFC-e de vendas formais a consumidor final.

O preço é processado por:
1. NCM de 8 dígitos;
2. mineração de texto;
3. remoção de outliers pelo método de Tukey;
4. mediana das observações restantes.

Logo, o indicador é **preço mediano processado**, não preço médio simples nem preço de uma loja específica.

## 3. PCA-RE — agosto/2026

COREDE Fronteira Oeste:
- **R$ 284,19**;
- variação mensal: **+0,51%**;
- acumulado no ano: **+2,01%**;
- 12 meses: **+3,22%**.

Rio Grande do Sul:
- **R$ 298,61**;
- variação mensal: **+0,60%**;
- acumulado no ano: **+2,54%**;
- 12 meses: **+3,49%**.

### Diferença de nível

`(284,19 / 298,61 - 1) × 100 = -4,83%`.

**Dado calculado:** o PCA-RE da Fronteira Oeste estava 4,83% abaixo do nível estadual em agosto/2026.

Isso não significa que toda família de São Borja pagava 4,83% menos por alimentos.

## 4. Inflação alimentar por faixa de renda

ICA-RE 12 meses — Fronteira Oeste:

- <2 SM: **2,23%**;
- 2 a 3 SM: **1,94%**;
- 3 a 6 SM: **2,26%**;
- 6 a 10 SM: **2,73%**;
- 10 a 15 SM: **2,64%**;
- 15 a 25 SM: **3,84%**;
- >25 SM: **4,29%**;
- média regional: **3,23%**.

Média estadual: **3,49%**.

Diferença:

`3,23% - 3,49% = -0,26 p.p.`.

### Interpretação

A pressão alimentar acumulada em 12 meses estava ligeiramente abaixo da média estadual no agregado regional, mas não de maneira uniforme entre faixas de renda.

Os estratos superiores apresentavam inflação acumulada maior que os estratos inferiores nessa competência.

Não converter isso em diferença de “custo de vida total”: o indicador é restrito à cesta alimentar e segue pesos específicos da metodologia.

## 5. Hortaliças

Fronteira Oeste:
- preço agregado: **R$ 5,58**;
- mês: **-6,88%**;
- ano: **+6,31%**;
- 12 meses: **+18,69%**.

Rio Grande do Sul:
- **R$ 6,50**;
- mês: **-7,27%**;
- ano: **+16,28%**;
- 12 meses: **+22,45%**.

### Interpretação

O grupo mostra que uma queda mensal pode coexistir com forte inflação acumulada em 12 meses.

Por isso, leitura de uma única variação mensal é insuficiente para diagnóstico de pressão de preços.

## 6. Cebola

Fronteira Oeste:
- **R$ 5,43**;
- mês: **-13,10%**;
- ano: **+117,60%**;
- 12 meses: **+101,93%**.

RS:
- **R$ 5,99**;
- mês: **-11,80%**;
- ano: **+101,39%**;
- 12 meses: **+102,89%**.

### Interpretação

A cebola ilustra choque de preço muito intenso no período acumulado, apesar da correção mensal de agosto.

Não atribuir o choque a clima, oferta, logística ou sazonalidade sem evidência adicional específica.

## 7. Valor analítico para o Caderno-Base

O bloco acrescenta ao território uma dimensão que faltava:

- pressão regional de preços de alimentos;
- comparação Fronteira Oeste × RS;
- exposição diferenciada por faixa de renda;
- volatilidade por grupo/produto.

Isso melhora a interpretação de:
- renda disponível;
- vulnerabilidade de consumo;
- bens essenciais;
- alimentação fora do lar.

## 8. Relação com Bens Essenciais

O Radar mostra **origem do abastecimento estadual**.

Preços Dinâmicos mostra **preço mediano regional ao consumidor final**.

Esses indicadores são complementares, mas não permitem afirmar causalidade:

`dependência externa estadual → preço regional`

não é uma relação automaticamente demonstrada.

Para testar causalidade seriam necessários controles de:
- safra/oferta;
- frete;
- preços de atacado;
- tributação;
- concorrência;
- sazonalidade.

## 9. Relação com Alimentação Fora do Lar

O PCA-RE e os preços de alimentos podem ser usados como contexto upstream dos custos do foodservice.

Não são:
- custo efetivo de aquisição de restaurantes;
- inflação dos cardápios;
- margem do setor;
- preço de refeições.

Para isso são necessárias bases específicas do canal foodservice ou pesquisa primária.

## 10. Inconsistência documental preservada

A NT CIET 01/2026 registra **29 subgrupos**.

O boletim de agosto/2026 registra **30 subgrupos**.

Não foi localizada explicação documental para a mudança.

Regra:
**não harmonizar silenciosamente.**

## 11. Status de promoção

**PROMOVER COMO BENCHMARK REGIONAL**, com o rótulo explícito:

> COREDE Fronteira Oeste — região de referência de São Borja.

Promover:
- ao sucessor do Caderno-Base;
- ao caderno Bens Essenciais;
- como contexto de custo no caderno Serviços e Alimentação Fora do Lar.

## 12. Artefatos

- `docs/data_sources/precos_dinamicos_fronteira_oeste_agosto2026_v001.csv`;
- `docs/data_sources/precos_dinamicos_rs_auditoria_v001.md`;
- `docs/caderno_base/analise_precos_dinamicos_fronteira_oeste_20260920_v002.md`.

## 13. Próxima etapa

1. recuperar série mensal completa Fronteira Oeste × RS;
2. priorizar PCA-RE, arroz, feijão, leite, pão, carnes, frango, ovos, óleo, café, frutas e hortaliças;
3. separar nível de preço, variação mensal, acumulada no ano e 12 meses;
4. integrar com renda somente com geografia e período explicitados;
5. manter custo regional separado de gasto municipal observado.

## 14. Governança

- Caderno-Base v028 permanece read-only;
- inclusão apenas no sucessor;
- PR #41 permanece aberto, draft e sem merge.
