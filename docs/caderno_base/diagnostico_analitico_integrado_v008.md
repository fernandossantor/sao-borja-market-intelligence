# Caderno-Base Territorial — diagnóstico analítico integrado v008

## Atualização desta versão

Esta versão preserva a estrutura territorial, laboral, fiscal, domiciliar e de transferências da v007 e acrescenta uma **matriz explícita de fluxos de renda e transferências**, com uma regra central: **as diferentes camadas monetárias não são somadas diretamente** porque períodos, universos, conceitos e pessoas podem se sobrepor.

Abrangência: São Borja/RS.  
Atualização: 2026-09-08.

## 1. Estrutura territorial e oferta

Dados já consolidados:

- 6.906 estabelecimentos empresariais no universo RFB 2026-08;
- 284 de matriz externa: **4,1124%**;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- peso laboral externo / peso cadastral externo: **6,12 vezes**.

No varejo (CNAE 47):

- presença cadastral externa: **6,63%**;
- emprego externo estimado: **37,46%**;
- remuneração de dezembro externa estimada: **38,16%**;
- participação do varejo no total externo de remuneração de dezembro: **36,41%**.

**Interpretação:** a base empresarial é predominantemente local em número, mas estruturas externas têm peso funcional muito maior em segmentos específicos, sobretudo no varejo, finanças, transporte e energia.

## 2. Mercado residente e distribuição de renda

IBGE/SIDRA — Censo 2022:

- população: **59.676 pessoas**;
- estimativa oficial 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- rendimento domiciliar per capita médio: **R$ 1.568,58/mês**;
- mediana: **R$ 1.100,00/mês**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM per capita: **50.650 / 85,79220%**.

Massa mensal implícita no mesmo universo:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`.

Natureza: **calculado**. Não equivale a renda disponível, consumo, faturamento ou potencial setorial.

## 3. Camadas monetárias observadas/calculadas

A nova aba `Matriz_fluxos_renda` registra as seguintes referências:

| Camada | Valor | Referência | Natureza |
|---|---:|---|---|
| Massa implícita de rendimento domiciliar | R$ 92.605.826,04/mês | Censo 2022 | calculado |
| Remuneração nominal de dezembro informada — RAIS | R$ 23.940.059,71 | dez/2025 | observado |
| Crédito INSS/SUIBE emitido a residentes | R$ 24.535.168,54 | jul/2026 | calculado a partir de registros oficiais |
| Novo Bolsa Família — média mensal do fluxo corrente | R$ 1.502.070,14/mês | jan–jul/2026 | calculado a partir de registros oficiais |
| Novo Bolsa Família — fluxo corrente em julho | R$ 1.513.564,00 | jul/2026 | calculado a partir de registros oficiais |

## 4. Regra de não soma

**Controle metodológico:** não existe “total agregado” dessas camadas nesta etapa.

Razões:

- Censo, RAIS, INSS e Novo Bolsa Família não têm a mesma referência temporal;
- moradores, vínculos, benefícios e registros/parcela não são o mesmo universo;
- as fontes medem conceitos diferentes;
- pessoas e rendimentos podem se sobrepor entre as bases.

Somar as grandezas produziria dupla contagem potencial e uma estimativa de renda corrente não sustentada.

**Interpretação:** o objetivo analítico é decompor a capacidade econômica residente em camadas e entender sua função, não fabricar uma massa única.

## 5. Novo Bolsa Família — recorrência

Série janeiro–julho de 2026:

- fluxo total por competência: **R$ 10.604.291,00**;
- fluxo de referência corrente: **R$ 10.514.491,00**;
- ajustes de referências anteriores: **R$ 89.800,00 / 0,84683%**;
- média mensal do fluxo corrente: **R$ 1.502.070,14**;
- variação jan→jul do fluxo corrente: **-0,28973%**;
- coeficiente de variação mensal: **0,70509%**.

**Interpretação:** o fluxo corrente permaneceu aproximadamente entre R$ 1,49 milhão e R$ 1,52 milhão/mês nas sete competências. Isso descreve recorrência e baixa dispersão no intervalo observado, não estabilidade futura, sazonalidade ou padrão de consumo.

## 6. Comparação contextual de magnitude — julho de 2026

Cálculo:

`R$ 1.513.564,00 / R$ 24.535.168,54 × 100 = 6,16896%`.

**Leitura permitida:** a magnitude do Novo Bolsa Família em julho corresponde a aproximadamente **6,17%** do crédito INSS/SUIBE registrado a residentes no mesmo mês.

**Leitura proibida:** não é participação do NBF em uma renda total nem em um conjunto mutuamente exclusivo de transferências.

## 7. Integração oferta × demanda

Fatos combinados:

- o varejo é o principal nó externo em peso absoluto;
- 85,79220% dos moradores do universo da tabela SIDRA 10296 estão sem rendimento ou em faixas de até 2 SM per capita;
- INSS/SUIBE registra fluxo mensal material de benefícios a residentes;
- Novo Bolsa Família apresenta fluxo corrente médio próximo de R$ 1,5 milhão/mês em jan–jul/2026.

**Interpretação/hipótese:** São Borja combina um mercado consumidor numericamente concentrado nas faixas inferiores de renda com fluxos recorrentes de benefícios/transferências e uma oferta varejista na qual redes de matriz externa têm peso funcional maior que seu peso cadastral. O varejo, portanto, é um ponto prioritário para investigar **circulação monetária, destino do gasto e retenção territorial**.

Isso não demonstra que redes externas capturem uma parcela específica da renda residente. Também não demonstra “vazamento” monetário.

## 8. Pergunta analítica reformulada

A pergunta mais útil deixa de ser:

> “Quanto dá a soma das rendas?”

E passa a ser:

> “Como as diferentes fontes de renda e transferência estruturam a capacidade econômica dos segmentos residentes, em quais mercados e canais se convertem em demanda e quanto dessa demanda é retido por empresas e cadeias locais?”

Essa reformulação orienta os próximos passos para comportamento, destino do gasto, fornecedores e área de influência.

## 9. Dados faltantes

Ainda não é possível concluir:

- quanto das rendas/transferências é efetivamente consumido;
- quanto é gasto em São Borja ou fora do município;
- quanto é absorvido por empresas locais ou redes externas;
- como os recursos se distribuem entre os quatro cadernos setoriais;
- qual a propensão a consumir segundo fonte de renda;
- qual a sobreposição individual entre RAIS, INSS/SUIBE e Novo Bolsa Família;
- qual a renda total corrente dos residentes.

Dados necessários:

- gasto por categoria e segmento;
- canais e locais de compra;
- compras fora do município e comércio eletrônico;
- participação de empresas locais/externas nas vendas;
- fornecedores e compras empresariais locais/externas;
- endividamento, poupança e deduções;
- harmonização temporal e controle de sobreposição para qualquer estimativa de renda corrente.

## 10. Implicações para os quatro cadernos setoriais

As camadas monetárias devem ser usadas como **base de escala e segmentação**, não como multiplicadores automáticos de consumo.

A hipótese de que bens essenciais sejam mais sensíveis a fluxos recorrentes de benefícios e transferências é plausível como agenda de investigação, mas deve ser testada com dados comportamentais ou pesquisa primária.

A mesma regra vale para saúde/higiene, bens não essenciais e serviços/alimentação: fonte de renda não determina automaticamente destino do gasto.

## 11. Rastreabilidade

Caderno corrente: `caderno_base_territorial_v009_mercado_consumidor_renda_transferencias_20260908`, Drive ID `15NzQK7LimFA56jJ60pPL0pmpS75FvUxIMPhWH6LkuzM`.

Aba: `Matriz_fluxos_renda`, sheet ID `120000020`.

Documento nativo integrado corrente no Drive: `Caderno-Base — diagnóstico analítico integrado v006 — 20260908`, ID `1gf-bTqEXoEs5L5HCrZH6l1PZ3HiXYhfeuTdO3v-y8Zo`.

Nota nativa da matriz: `Matriz de fluxos de renda e transferências — v001 — 20260908`, ID `1E4TghI46on_azi360vKFt7SAl65SA-hjbec6jRm4RY4`.

Nota GitHub específica: `docs/caderno_base/matriz_fluxos_renda_transferencias_v001.md`.

## 12. Próxima agenda

1. estender a série Novo Bolsa Família para 2023-03 em diante, validando mudanças de esquema;
2. avaliar série mensal INSS/SUIBE;
3. mapear outras transferências monetárias relevantes;
4. avançar para dados de comportamento/destino do gasto;
5. estruturar, somente com bases compatíveis, metodologia de renda disponível aproximada e retenção territorial;
6. conectar a matriz monetária à matriz de controle territorial e aos quatro cadernos setoriais;
7. manter fiscalidade, VAF e IPM em trilha conceitual própria.