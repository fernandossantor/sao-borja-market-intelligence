# Caderno-Base Territorial — diagnóstico analítico integrado v005

## Atualização desta versão

Esta versão preserva o diagnóstico territorial, empresarial, laboral, fiscal e de renda domiciliar da v004 e incorpora a primeira referência oficial municipal de **benefícios emitidos pelo INSS/SUIBE a residentes de São Borja/RS**, competência julho de 2026.

Abrangência: São Borja/RS.  
Atualização: 2026-09-08.

## 1. Estrutura territorial já consolidada

Permanecem válidos:

- 6.906 estabelecimentos empresariais no universo RFB 2026-08;
- 284 de matriz externa, ou 4,1124%;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: 25,1606%;
- participação externa estimada na remuneração de dezembro: 29,6897%;
- IPM definitivo 2003–2026;
- VAF oficial publicado em REAL 1994–2025;
- matriz de controle territorial v001 com forte peso funcional externo em setores específicos.

Essas dimensões continuam separadas conceitualmente de renda domiciliar, benefícios e consumo.

## 2. Mercado residente e domicílios

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**.

A presença de domicílios unipessoais permanece hipótese relevante de segmentação, sem inferência automática sobre gasto.

## 3. Rendimento domiciliar per capita — Censo 2022

Fonte: IBGE/SIDRA, tabelas 10295 e 10296.

Dados observados:

- média nominal mensal per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível: **59.038 moradores**.

Agregações calculadas:

- sem rendimento ou até 1 SM: **59,31773%**;
- sem rendimento ou até 2 SM: **85,79220%**;
- mais de 2 SM: **14,20780%**;
- mais de 5 SM: **2,78295%**.

Massa mensal implícita no mesmo universo:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Essa massa não equivale a renda disponível ou consumo.

## 4. Renda formal do trabalho

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial. Trata-se de um fluxo mensal de vínculos formais empresariais, não de renda domiciliar total.

## 5. Benefícios emitidos pelo INSS/SUIBE — julho de 2026

Fonte: INSS Portal de Dados Abertos / SUIBE — `Benefícios Emitidos Julho 2026`.

O recorte canônico utiliza `municipio_residencia = 19181-RS-SAO BORJA`.

Resultados calculados a partir dos registros oficiais:

- **14.247 registros emitidos**;
- **14.247 registros com `credito` válido**;
- **R$ 24.535.168,54** de crédito total mensal;
- **R$ 1.722,13** por registro emitido.

A fonte não permite tratar 14.247 registros como 14.247 pessoas únicas.

A auditoria territorial também identificou registros contendo `SAO BORJA` associados a outras UFs; eles foram preservados como anomalia de fonte e excluídos do recorte de São Borja/RS.

## 6. Composição do fluxo de benefícios

As seis maiores espécies por valor são:

| Espécie literal | Registros | Crédito (R$) | % do crédito |
|---|---:|---:|---:|
| APOSENTADORIA POR IDADE | 3.787 | 6.264.831,82 | 25,53409% |
| PENSAO POR MORTE PREVIDENCIARIA | 2.642 | 4.424.751,50 | 18,03432% |
| APOSENTADORIA POR TEMPO DE CONTRIBUICAO | 1.647 | 4.145.792,27 | 16,89735% |
| APOSENTADORIA POR INCAPACIDADE PERMANENTE PREVIDENCIARIA | 1.689 | 2.923.245,53 | 11,91451% |
| AMPARO SOCIAL AO IDOSO | 1.656 | 2.447.049,37 | 9,97364% |
| AMPARO SOCIAL PESSOA PORTADORA DEFICIENCIA | 1.729 | 2.330.068,27 | 9,49685% |

As duas espécies literalmente denominadas `AMPARO SOCIAL` somam **3.385 registros**, **R$ 4.777.117,64**, **23,75939% dos registros** e **19,47049% do crédito**.

Esse subtotal não é o total da assistência social nem dos benefícios não contributivos; categorias legadas permanecem sem classificação agregada até definição jurídica explícita.

## 7. Leitura integrada da renda residente

O projeto dispõe agora de três referências monetárias mensais de natureza distinta:

- **R$ 92.605.826,04/mês** — massa implícita de rendimento domiciliar no universo do Censo 2022, calculada;
- **R$ 23.940.059,71** — remuneração nominal de dezembro informada na RAIS 2025, observada no recorte empresarial formal;
- **R$ 24.535.168,54** — crédito de benefícios emitidos pelo INSS/SUIBE a residentes em julho de 2026, calculado a partir dos registros oficiais.

Essas grandezas **não devem ser somadas** nesta etapa. Elas têm universos, períodos e conceitos diferentes. O valor analítico está em mostrar que a capacidade econômica residente não pode ser reconstruída apenas pela renda do trabalho formal.

## 8. Diagnóstico mercadológico atualizado

### Fatos sustentados

São Borja possui mercado residente próximo de 60 mil pessoas, base empresarial numericamente local, setores com dependência funcional externa elevada, distribuição de renda domiciliar per capita concentrada em número de pessoas nas faixas até dois salários mínimos e um fluxo mensal de benefícios INSS/SUIBE de aproximadamente **R$ 24,5 milhões** para residentes na competência observada.

### Interpretação

A presença de benefícios representa uma dimensão monetária material para a economia residente e precisa integrar a caracterização do consumidor. O dado não autoriza afirmar que R$ 24,5 milhões sejam integralmente consumidos no município, mas demonstra que uma leitura apoiada apenas em salários formais subestima fontes relevantes de renda não laboral.

A composição também é importante: aproximadamente **19,47% do crédito** está nas duas espécies literalmente denominadas `AMPARO SOCIAL`. Isso indica que previdência e proteção social coexistem no fluxo observado pelo INSS/SUIBE e não devem ser tratados como um bloco homogêneo contributivo.

### O que ainda não pode ser concluído

Ainda não é possível afirmar:

- quantas pessoas únicas recebem os 14.247 registros emitidos;
- qual parcela do crédito mensal é renda disponível;
- quanto é gasto em São Borja e quanto sai do território;
- como o gasto se distribui entre os quatro mercados setoriais;
- qual a propensão a consumir de cada espécie de benefício;
- qual o total de transferências monetárias diretamente recebidas pelas famílias fora do INSS;
- qual a renda total corrente dos residentes em 2026.

## 9. Implicações para os quatro cadernos setoriais

A nova camada não deve gerar uma regra simples de `benefícios × propensão de consumo`. Ela deve entrar como **base de segmentação e escala**, articulada com:

- distribuição de rendimento domiciliar per capita;
- estrutura domiciliar;
- renda formal do trabalho;
- matriz de controle territorial por setor;
- pesquisas primárias de hábitos e critérios de escolha, quando disponíveis.

Setores de bens essenciais, saúde/higiene, bens não essenciais e serviços/alimentação podem responder de forma diferente a renda previdenciária e assistencial; qualquer diferenciação deve ser testada e não presumida.

## 10. Auditoria e rastreabilidade

Workflow: `inss-benefits-residence-extract`.  
Run: `34282566426`.  
Artifact: `10078228209`.  
SHA-256 do artifact: `2f75523301768374ee1e9a908480ca850d93d6fe661407991ade50f9c800ba87`.  
SHA-256 do CSV municipal: `eb9e2536026d460892ea64cf672bf3cc26da1231bbf552f3ddd51d4c6945996c`.

Drive:

- pasta: `_sao_borja/raw/social/inss_suibe_beneficios_emitidos/`, ID `1gIN6tmhHg-r7lPBlpCnGHNggZCj568vO`;
- pacote oficial municipal: ID `11lAy2Dtlw20tzhOb8Y4ltkbpyZPDhbOs`;
- nota metodológica: ID `1bn5C6u1GII4eHrDwUnDRgTA27VR_YK4yL-QChWk_ncI`.

Caderno-Base v008:

- `Mercado_consumidor_base` atualizado;
- nova aba `INSS_beneficios_202607` com 27 espécies e fórmulas de participação.

## 11. Próxima agenda

A lacuna de uma primeira referência oficial municipal de benefícios INSS/SUIBE está encerrada para julho de 2026. As prioridades passam a ser:

1. recuperar transferências monetárias efetivamente recebidas pelas famílias em fonte oficial, distinguindo-as de repasses administrativos;
2. avaliar série mensal INSS/SUIBE para medir estabilidade, sazonalidade e mudanças de composição;
3. somente depois estruturar metodologia explícita para renda disponível aproximada e capacidade de compra;
4. conectar renda, benefícios e distribuição aos quatro cadernos setoriais e à matriz de controle territorial;
5. preservar fiscalidade, VAF e IPM em trilha conceitual própria.
