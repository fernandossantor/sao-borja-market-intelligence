# Caderno-Base Territorial — diagnóstico analítico integrado v009

Atualização: 2026-09-08.  
Abrangência: São Borja/RS.

## 1. Avanço desta versão

A v009 documental incorpora ao diagnóstico integrado o primeiro **benchmark estadual de demanda potencial para alimentação no domicílio**, baseado na POF 2017-2018 do Rio Grande do Sul, atualizado aproximadamente para preços de junho de 2026 e aplicado à população oficial estimada de São Borja em 2025.

O Caderno-Base correspondente passa para a versão **v010**, preservando a v009 anterior como histórico.

## 2. Estrutura territorial e oferta

Permanecem válidos:

- 6.906 estabelecimentos empresariais no universo RFB 2026-08;
- 284 de matriz externa, ou **4,1124%**;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- razão peso externo no emprego / peso cadastral: **6,12 vezes**.

No varejo (CNAE 47):

- presença cadastral externa: **6,63%**;
- emprego externo estimado: **37,46%**;
- remuneração de dezembro externa estimada: **38,16%**;
- participação do varejo no total externo de remuneração de dezembro: **36,41%**.

**Interpretação:** a base empresarial é majoritariamente local em número de estabelecimentos, mas estruturas externas têm peso funcional muito maior em segmentos específicos. O varejo é o principal nó externo em peso absoluto.

## 3. Mercado residente e renda

IBGE/Censo 2022 e estimativas oficiais:

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- rendimento domiciliar per capita médio: **R$ 1.568,58/mês**;
- mediana: **R$ 1.100,00/mês**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM per capita: **50.650 / 85,79220%**.

Massa mensal implícita no universo estatístico:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`.

Natureza: **calculado**. Não equivale a renda disponível, consumo efetivo, faturamento ou potencial setorial.

## 4. Renda formal, INSS/SUIBE e Novo Bolsa Família

RAIS 2025:

- remuneração nominal de dezembro informada: **R$ 23.940.059,71**.

INSS/SUIBE, julho de 2026:

- 14.247 registros;
- crédito total: **R$ 24.535.168,54**;
- média: **R$ 1.722,13/registro**.

Novo Bolsa Família, janeiro–julho de 2026:

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo de referência corrente: **R$ 10.514.491,00**;
- média mensal corrente: **R$ 1.502.070,14**;
- variação jan→jul: **-0,28973%**;
- CV mensal: **0,70509%**.

As camadas monetárias **não são somadas diretamente** porque diferem em período, universo, conceito e podem se sobrepor individualmente.

## 5. Demanda potencial de bens essenciais — benchmark POF RS

Fonte observada: IBGE — POF 2017-2018 — tabela `1.3.23.3`, Rio Grande do Sul.

Dados observados no total estadual:

- alimentação total: **R$ 736,69/família/mês**;
- alimentação no domicílio: **R$ 487,00/família/mês**;
- alimentação fora do domicílio: **R$ 249,69/família/mês**;
- tamanho médio familiar: **2,72 pessoas**.

Cálculo per capita:

`487 / 2,72 = R$ 179,04412/pessoa/mês` na base POF.

Atualização monetária usada no modelo:

- fator IPCA Alimentação e bebidas: **1,781742384675**;
- benchmark atualizado: aproximadamente **R$ 319,01/pessoa/mês**, preços de junho de 2026.

Cenário principal, população oficial estimada de 2025:

- mensal: **R$ 19.558.852,34**;
- anual: **R$ 234.706.228,14**.

Natureza: **ESTIMATIVA MODELADA**.

Esse valor representa ordem de grandeza do núcleo alimentar comprado para consumo no domicílio por residentes. Não é faturamento observado, mercado efetivamente capturado nem renda disponível.

## 6. Mudança de benchmark: RS versus Região Sul

Comparador regional com a mesma população e atualização monetária:

- RS: **R$ 234.706.228,14/ano**;
- Região Sul: **R$ 223.342.012,82/ano**.

Diferença:

`(234.706.228,14 / 223.342.012,82 - 1) × 100 = +5,08826%`.

**Interpretação:** +5,09% é efeito de maior especificidade geográfica do benchmark. **Não é crescimento temporal do mercado.**

## 7. Classes de rendimento da POF e controle conceitual

Na POF RS, a despesa no domicílio varia de **R$ 248,57/família/mês** na classe de até R$ 1.908, inclusive sem rendimento, a **R$ 1.253,49** na classe acima de R$ 23.850.

Per capita calculado na base POF: aproximadamente **R$ 120,67 a R$ 449,28/pessoa/mês**.

A parcela do gasto alimentar realizada no domicílio é **66,11%** no total estadual e **78,94%** na classe mais baixa.

**Interpretação limitada à fonte estadual:** classes inferiores apresentam menor gasto alimentar absoluto, mas maior parcela do gasto alimentar é realizada no domicílio.

A v005 **não calibra o benchmark pela renda municipal**. A POF classifica por **rendimento total + variação patrimonial mensal familiar**; o Censo municipal consolidado usa **rendimento domiciliar per capita**. Não se faz correspondência direta entre essas categorias.

## 8. Integração oferta × demanda

**Fato:** o varejo tem peso funcional externo muito superior ao seu peso cadastral e é o principal nó externo em termos absolutos.

**Fato:** o benchmark modelado do núcleo alimentar residente é de aproximadamente **R$ 234,7 milhões/ano**.

**Interpretação/hipótese:** o problema mercadológico passa a ser investigar como essa demanda se distribui entre formatos, empresas, canais e territórios — e não apenas dimensionar sua ordem de grandeza.

Não existe evidência para repartir os R$ 234,7 milhões entre empresas locais e redes externas, medir retenção local ou inferir vazamento monetário.

## 9. Dados faltantes prioritários

- gasto por categoria e formato;
- destino geográfico das compras;
- compras na Argentina e outros municípios;
- comércio eletrônico;
- participação de empresas locais e redes externas nas vendas;
- proxy de capacidade/porte da oferta;
- preços locais;
- estrutura de fornecedores;
- ponte conceitualmente compatível de renda ou pesquisa primária de gasto.

## 10. Rastreabilidade POF / demanda

Workflow: `pof-rs-food-source-discovery`.

- run: `34293228168`;
- artifact: `10082136959`;
- pacote oficial: **1.409.382 bytes**;
- SHA-256 pacote: `7be3b0c5852d02ee886cf59265d0301278ff36d3d53445cab63ba7a25b525048`;
- arquivo `43RS.xls.xlsx`: **58.216 bytes**;
- SHA-256 43RS: `a32c3201cc201d669c65d3f46f50033bdad2e810d603a41d3731ffe64976d975`.

Drive:

- fonte oficial raw: ID `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- derivado POF RS: ID `11xTjsR4AkTALlySBBomX4N20REIvG95ucKF3gjyRsfA`;
- modelo demanda v005: ID `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- documento específico de demanda: ID `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`;
- documento analítico nativo corrente: ID `1xmPKHpSGqeafoN3_T7cP_kLbryiGWI-0i8j4FcMxkv4`;
- Caderno-Base v010: ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.

## 11. Estado do Caderno

Caderno corrente: `caderno_base_territorial_v010_demanda_bens_essenciais_20260908`.

A v010 preserva todas as abas da v009 e acrescenta:

- `Bens_essenciais_demanda`;
- `POF_RS_classes`.

A aba `Diagnostico_integrado` também incorpora o benchmark, a diferença RS/Sul e a decisão metodológica de não calibrar a renda local por equivalência artificial.

## 12. Próxima agenda

1. investigar destino e canais do gasto alimentar;
2. estimar atração/evasão de compras, incluindo Argentina, outros municípios e comércio eletrônico;
3. construir proxy de capacidade/porte da oferta por formato e operador;
4. só depois aproximar retenção territorial e pressão competitiva;
5. manter a hipótese de maior sensibilidade dos bens essenciais a fluxos recorrentes de renda/transferências como hipótese a testar, não como conclusão;
6. continuar a extensão das séries de NBF/INSS quando elas agregarem valor analítico ao comportamento e à capacidade econômica.