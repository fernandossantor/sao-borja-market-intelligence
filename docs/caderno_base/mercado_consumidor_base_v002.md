# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar e de renda v002

## Objetivo

Esta versão atualiza a base de mercado consumidor do Caderno-Base com a recuperação direta, auditável e oficial do rendimento nominal mensal domiciliar per capita médio e mediano de São Borja no Censo 2022. O objetivo permanece construir a dimensão da demanda residente sem tratar população, PIB, remuneração formal, renda domiciliar e benefícios como grandezas equivalentes.

Abrangência geográfica: São Borja/RS.  
Períodos principais: Censo 2022; PIB 2023; estimativa populacional 2025; RAIS 2025; RFB 2026-08.  
Data de atualização: 2026-09-08.

Tabela de sustentação: aba `Mercado_consumidor_base` do Caderno-Base v008.

---

## 1. População: dimensão do mercado residente

### Dados observados em fonte oficial

- População residente — Censo Demográfico 2022: **59.676 pessoas**.
  - Fonte: IBGE/SIDRA, tabela 4714, variável 93.
  - Natureza: observado.
- População estimada — 2025: **61.311 pessoas**.
  - Fonte: IBGE, Estimativas da População 2025, município 4318002.
  - Natureza: estimativa oficial publicada.

### Cálculos contextuais

`61.311 − 59.676 = 1.635 pessoas`

`(61.311 / 59.676 − 1) × 100 = 2,7398%`

Esses cálculos expressam apenas a diferença entre estimativa 2025 e Censo 2022. **Não constituem taxa oficial de crescimento demográfico**, porque confrontam uma estimativa intercensitária com uma contagem censitária.

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

O projeto preserva o rótulo **“soma das quatro categorias reportadas”** e não o relabela como total oficial sem linha total explicitamente verificada na mesma fonte.

### Interpretação mercadológica

Os **21,31% de domicílios unipessoais** constituem um segmento quantitativamente relevante. Como hipótese mercadológica, essa composição pode favorecer demanda por conveniência, embalagens/porções menores e serviços individualizados.

A hipótese não deve ser confundida com comportamento observado: composição domiciliar não mede gasto, preferência, frequência de compra ou disposição a pagar.

---

## 3. Escala econômica não é capacidade de compra

- PIB a preços correntes — 2023: **R$ 2.550.388.000**.
  - Fonte: IBGE/SIDRA, tabela 5938, variável 37.
  - Unidade original: mil reais; conversão para reais por multiplicação por 1.000.
- PIB per capita — 2023: **R$ 42.737,25 por pessoa**.
  - Fonte: IBGE Cidades — São Borja.

**PIB e PIB per capita não equivalem a renda disponível, rendimento domiciliar per capita, salário médio ou potencial de consumo.** PIB mede produção no território e pode incluir rendas apropriadas fora dele e atividades sem conversão direta em consumo das famílias residentes.

---

## 4. Mercado formal empresarial em relação à escala populacional

Bases:

- 6.906 estabelecimentos empresariais — RFB 2026-08;
- 8.595 vínculos empresariais — RAIS 2025;
- 61.311 residentes — estimativa oficial 2025.

Indicadores calculados — apenas contextuais:

`6.906 / 61.311 × 1.000 = 112,64 estabelecimentos empresariais por mil residentes estimados`

`8.595 / 61.311 × 1.000 = 140,19 vínculos empresariais por mil residentes estimados`

`8.595 / 6.906 = 1,2446 vínculo empresarial por estabelecimento`

Esses indicadores **não são taxas oficiais**. Vínculo não equivale a pessoa ocupada única; a população inclui pessoas fora do mercado de trabalho; e RAIS 2025 e RFB 2026-08 não têm referência temporal idêntica.

---

## 5. Renda formal do trabalho já disponível

No recorte empresarial da RAIS 2025:

- remuneração nominal de dezembro informada: **R$ 23.940.059,71**;
- 7.800 valores informados e 795 ausentes;
- participação externa estimada nessa remuneração: **29,689702%**.

A remuneração de dezembro é um fluxo mensal do emprego formal empresarial analisado. **Não é massa salarial anual, renda domiciliar total nem renda disponível para consumo.**

---

## 6. Rendimento domiciliar per capita — dado oficial recuperado

### Fonte primária

IBGE/SIDRA — tabela 10295 — Censo Demográfico 2022.

Consulta oficial utilizada:

`https://apisidra.ibge.gov.br/values/t/10295/n6/4318002/v/13431,13534/p/2022/h/y/f/a/d/m`

Geografia: São Borja/RS, código IBGE `4318002`.  
Período: 2022.  
Unidade publicada: Reais.

### Dados observados

**Variável 13431 — rendimento nominal médio mensal domiciliar per capita:** **R$ 1.568,58**.

**Variável 13534 — rendimento nominal mediano mensal domiciliar per capita:** **R$ 1.100,00**.

A definição das duas variáveis refere-se aos moradores em domicílios particulares permanentes ocupados e exclui aqueles cuja condição no domicílio era **pensionista, empregado(a) doméstico(a) ou parente do(a) empregado(a) doméstico(a)**.

Natureza: **observado em fonte oficial**.

### Rastreabilidade da extração

- workflow: `consumer-income-sidra`;
- run: `34269331974`;
- job: `102206631993`;
- HTTP: `200`;
- resposta bruta: 1.785 bytes;
- SHA-256 do JSON bruto: `29e84da86e8424d0727325647634b9565e1f181374bf3cedf3c3c64936adea33`;
- artifact GitHub: `sidra-10295-sao-borja-income-2022`, ID `10073147229`;
- SHA-256 do ZIP do artifact: `7c1d5f13cf6445810a376cae8ed929734f0a00254b82354d2c923351c8cced02`.

O pacote foi promovido ao Drive em `01_fontes_e_coletas/demografia/renda_domiciliar/sidra_10295_sao_borja_income_2022_official_package.zip`, Drive ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`.

A documentação específica no Drive é `Renda domiciliar per capita — SIDRA 10295 — auditoria e incorporação — 20260908`, ID `1WrVv6dDXeB-nzz8jxl5GLwR2LrPZPrBchKtaQu0KfqY`.

---

## 7. Cálculos derivados média × mediana

### Diferença absoluta

`R$ 1.568,58 − R$ 1.100,00 = R$ 468,58 por pessoa/mês`

### Diferença relativa

`(1.568,58 / 1.100,00 − 1) × 100 = 42,5982%`

Apresentação arredondada: **42,60%**.

Natureza: **calculado**. Esses resultados não são indicadores oficiais do IBGE.

### Interpretação

A mediana substancialmente abaixo da média mostra que a média não deve ser usada isoladamente como retrato do consumidor típico. Para representar a posição central do universo da tabela, a mediana de **R$ 1.100,00** é menos sensível aos valores superiores do que a média de **R$ 1.568,58**.

A distância é compatível com assimetria à direita da distribuição, mas essa é uma **interpretação**, não uma medida de desigualdade. Média e mediana isoladamente não permitem calcular Gini, quantis, participação dos estratos superiores ou concentração de renda.

---

## 8. Limitações e lacunas remanescentes

Os valores da tabela 10295 **não equivalem** a:

- renda disponível;
- salário médio;
- PIB per capita;
- renda total do domicílio;
- gasto mensal de consumo.

Também **não se deve multiplicar R$ 1.568,58 pela população total de 59.676 habitantes do Censo 2022 ou pela estimativa de 61.311 em 2025** para estimar massa mensal de renda. Para isso, deve ser recuperado o número de moradores correspondente ao **mesmo universo da tabela 10295**.

A lacuna sobre o nível central de rendimento domiciliar per capita está encerrada, mas permanecem prioritárias:

1. distribuição municipal por faixas/quantis;
2. número de moradores do mesmo universo da tabela 10295;
3. aposentadorias, pensões e benefícios previdenciários pagos a residentes;
4. transferências monetárias efetivamente recebidas pelas famílias.

---

## 9. Rendas não laborais e controle conceitual

A planilha localizada no Drive para **Programa Bolsa Família e Cadastro Único** registra transferências do **Índice de Gestão Descentralizada ao Fundo Municipal de Assistência Social (FMAS)**. Trata-se de recurso administrativo de gestão, e não benefício monetário recebido pelas famílias.

Consequentemente, esses valores **não são renda familiar, transferência às famílias ou demanda de consumo**. A análise deverá buscar benefícios efetivamente pagos aos residentes/famílias por fonte oficial.

---

## 10. Diagnóstico parcial atualizado

### Fatos sustentados

São Borja possui um mercado residente da ordem de 60 mil pessoas, aproximadamente um quinto dos domicílios é unipessoal e o Censo 2022 registra rendimento domiciliar per capita **médio de R$ 1.568,58 e mediano de R$ 1.100,00** no universo definido pela tabela 10295.

### Interpretação

A incorporação da mediana melhora materialmente a leitura de mercado: o potencial consumidor não deve ser descrito por uma média única, especialmente quando a mediana é **R$ 468,58 inferior**. Para planejamento mercadológico, a mediana deve funcionar como referência central complementar e mais conservadora, enquanto a média permanece útil para dimensionamentos que respeitem o universo da fonte.

### O que ainda não pode ser concluído

Ainda não é possível estimar de forma robusta:

- massa monetária mensal disponível às famílias;
- distribuição municipal por classes ou faixas de renda;
- desigualdade municipal a partir desses dois indicadores;
- participação de aposentadorias/pensões e programas sociais na renda local;
- parcela da renda efetivamente gasta no município;
- potencial monetário de consumo por setor.

---

## 11. Próxima ação

A prioridade deixa de ser recuperar média e mediana — etapa concluída — e passa a ser **fechar a estrutura da renda das famílias**: distribuição da renda, denominador do mesmo universo, previdência e transferências monetárias efetivamente recebidas.

Somente depois dessa camada será metodologicamente adequado estruturar capacidade de compra e segmentação econômica do mercado consumidor e conectá-las aos quatro cadernos setoriais.
