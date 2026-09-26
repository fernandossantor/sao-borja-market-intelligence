# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar e de renda v001

## Objetivo

Este documento inicia a integração entre a estrutura empresarial já consolidada no Caderno-Base e a dimensão da demanda residente. O foco é construir uma base metodologicamente controlada para analisar população, domicílios, renda e capacidade de compra sem tratar PIB, remuneração formal, benefícios sociais ou estimativas populacionais como grandezas equivalentes.

Abrangência geográfica: São Borja/RS.  
Períodos principais: Censo 2022; PIB 2023; estimativa populacional 2025; RAIS 2025; RFB 2026-08.  
Data de atualização: 2026-09-08.

A tabela de sustentação está na aba `Mercado_consumidor_base` do Caderno-Base v008.

---

## 1. População: dimensão do mercado residente

### Dados observados em fonte oficial

- População residente — Censo Demográfico 2022: **59.676 pessoas**.
  - Fonte: IBGE/SIDRA, tabela 4714, variável 93.
  - Natureza: observado.
  - Referência: 2022.
- População estimada — 2025: **61.311 pessoas**.
  - Fonte: IBGE, Estimativas da População 2025, município 4318002.
  - Natureza: estimativa oficial publicada.
  - Referência: 2025.

### Cálculos contextuais

`61.311 − 59.676 = 1.635 pessoas`

`(61.311 / 59.676 − 1) × 100 = 2,7398%`

Esses cálculos expressam apenas a diferença entre a estimativa oficial de 2025 e a população censitária de 2022. **Não constituem taxa oficial de crescimento demográfico**, porque confrontam uma contagem censitária com uma estimativa intercensitária.

### Interpretação

A população estimada de aproximadamente 61,3 mil habitantes pode ser utilizada como referência atual de escala para dimensionamentos mercadológicos exploratórios. Quando a análise exigir comparabilidade temporal estrita, deve-se retornar às séries demográficas construídas com metodologia compatível.

---

## 2. Estrutura domiciliar

Fonte: IBGE/SIDRA, tabela 9879, Censo 2022.

| Composição domiciliar | Domicílios | Participação informada |
|---|---:|---:|
| Unipessoal | 4.815 | 21,31% |
| Nuclear | 13.820 | 61,17% |
| Estendida | 3.518 | 15,57% |
| Composta | 438 | 1,94% |

Soma calculada das quatro categorias reportadas:

`4.815 + 13.820 + 3.518 + 438 = 22.591 domicílios`

O projeto preserva o rótulo **“soma das quatro categorias reportadas”**. Não se relabela esse resultado como total oficial de domicílios sem uma linha total explicitamente verificada na mesma fonte.

### Interpretação mercadológica

Os **21,31% de domicílios unipessoais** constituem um segmento quantitativamente relevante. Como hipótese mercadológica, essa composição pode favorecer demanda por conveniência, embalagens e porções de menor escala, serviços individualizados e soluções de consumo desenhadas para uma única pessoa.

Essa é uma **hipótese**, não um comportamento observado: composição domiciliar não mede gasto, preferência, frequência de compra nem disposição a pagar.

---

## 3. Escala econômica não é capacidade de compra

### PIB municipal

- PIB a preços correntes — 2023: **R$ 2.550.388.000**.
- Fonte: IBGE/SIDRA, tabela 5938, variável 37.
- A unidade original da tabela é **mil reais**; o valor publicado `2.550.388` foi convertido para reais por multiplicação por 1.000.
- Natureza: dado observado, com conversão de unidade calculada.

### PIB per capita

- PIB per capita — 2023: **R$ 42.737,25 por pessoa**.
- Fonte: IBGE Cidades — São Borja.
- Natureza: observado em fonte oficial.

### Limitação conceitual

**PIB e PIB per capita não equivalem a renda disponível das famílias, rendimento domiciliar per capita, salário médio ou potencial de consumo.** O PIB mede a produção gerada no território e pode incluir rendas apropriadas fora dele, bem como atividades que não se convertem diretamente em consumo das famílias residentes.

---

## 4. Mercado formal empresarial em relação à escala populacional

Bases utilizadas:

- 6.906 estabelecimentos empresariais — RFB 2026-08;
- 8.595 vínculos empresariais — RAIS 2025;
- 61.311 residentes — estimativa oficial 2025.

### Indicadores calculados — apenas contextuais

**Estabelecimentos empresariais por mil residentes estimados**

`6.906 / 61.311 × 1.000 = 112,64`

**Vínculos empresariais formais por mil residentes estimados**

`8.595 / 61.311 × 1.000 = 140,19`

**Vínculos empresariais por estabelecimento empresarial**

`8.595 / 6.906 = 1,2446`

Esses indicadores **não são taxas oficiais**. No segundo caso, vínculo não equivale a pessoa ocupada única e o denominador inclui toda a população. No terceiro, RAIS 2025 e RFB 2026-08 não possuem referência temporal idêntica e os universos não coincidem perfeitamente; portanto, não se deve chamar o resultado de tamanho médio oficial da empresa.

---

## 5. Renda formal do trabalho já disponível

No recorte empresarial da RAIS 2025:

- remuneração nominal de dezembro informada: **R$ 23.940.059,71**;
- 7.800 valores informados e 795 ausentes;
- participação externa estimada nessa remuneração: **29,689702%**.

A remuneração de dezembro é um fluxo mensal específico do emprego formal empresarial analisado. **Não é massa salarial anual, renda domiciliar total nem renda disponível para consumo.** A participação externa estimada também não informa quanto da renda é efetivamente gasta ou retida em São Borja.

---

## 6. Renda domiciliar: principal lacuna para o próximo salto analítico

Foi identificada a fonte oficial apropriada para a próxima etapa:

**IBGE/SIDRA — tabela 10295 — Censo Demográfico 2022**.

A tabela disponibiliza, inclusive em nível municipal:

- valor do rendimento nominal **médio** mensal domiciliar per capita;
- valor do rendimento nominal **mediano** mensal domiciliar per capita;
- número de moradores no universo da tabela;
- percentual correspondente.

A definição exclui moradores cuja condição no domicílio era **pensionista, empregado(a) doméstico(a) ou parente do(a) empregado(a) doméstico(a)**. Essa restrição deverá ser preservada nas notas metodológicas.

Os valores específicos de São Borja ainda **não foram incorporados**, pois a recuperação direta da consulta oficial não foi concluída nesta sessão. O projeto não preencherá a lacuna com estimativas ou fontes secundárias enquanto o dado oficial estiver disponível para recuperação.

Quando a consulta for obtida, a média e a mediana devem ser incorporadas diretamente. Qualquer tentativa de transformar a média per capita em massa mensal de renda deverá utilizar o **número de moradores do mesmo universo da tabela 10295**, e não automaticamente a população censitária total.

---

## 7. Rendas não laborais — lacunas prioritárias

Além da renda do trabalho, a capacidade de compra local pode ser sustentada por fluxos não laborais relevantes. As próximas fontes a incorporar são:

1. aposentadorias, pensões e benefícios previdenciários pagos a residentes — INSS/BEPS ou fonte oficial equivalente;
2. transferências de renda efetivamente recebidas pelas famílias — MDS/Portal da Transparência;
3. posteriormente, quando houver base adequada, outras rendas de capital e transferências.

### Exclusão metodológica já confirmada

A planilha localizada no Drive para **Programa Bolsa Família e Cadastro Único** registra transferências do **Índice de Gestão Descentralizada ao Fundo Municipal de Assistência Social (FMAS)**. Trata-se de recurso administrativo destinado à gestão do programa, e não do benefício monetário recebido pelas famílias.

Consequentemente, esses valores **não serão tratados como renda familiar, transferência às famílias ou demanda de consumo**.

---

## 8. Diagnóstico parcial

### Fatos sustentados

São Borja possui um mercado residente da ordem de 60 mil pessoas, com aproximadamente um quinto dos domicílios classificados como unipessoais no Censo 2022. A economia territorial gerou PIB corrente de R$ 2,55 bilhões em 2023, enquanto o recorte empresarial da RAIS registra 8.595 vínculos em 2025. Esses indicadores dimensionam população, estrutura domiciliar, produção e parte do emprego formal, mas medem fenômenos diferentes.

### Interpretação

A base atual já permite abandonar uma ideia excessivamente simples de “mercado = população × PIB per capita”. Para inteligência mercadológica, a capacidade de demanda precisa ser reconstruída a partir de **quem reside no território, como os domicílios são compostos, quais fontes geram renda às famílias e como essa renda se distribui**.

A presença expressiva de domicílios unipessoais já introduz uma dimensão comportamental/mercadológica transversal que deverá ser cruzada, mais adiante, com os quatro mercados setoriais.

### O que ainda não pode ser concluído

Ainda não é possível estimar de forma robusta:

- massa monetária mensal disponível às famílias;
- poder de compra médio ou mediano do domicílio;
- distribuição municipal da renda por faixas;
- participação de aposentadorias/pensões e programas sociais na renda local;
- parcela da renda gerada localmente que é consumida no município;
- potencial monetário de consumo por setor.

---

## 9. Próxima ação

A prioridade imediata é recuperar e preservar os valores municipais da **tabela SIDRA 10295** para São Borja e, em seguida, incorporar previdência e transferências efetivamente recebidas por famílias.

Somente depois dessa camada será adequado avançar para uma estimativa de capacidade de compra e segmentação econômica do mercado consumidor.
