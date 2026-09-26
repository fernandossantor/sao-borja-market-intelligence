# QA argumentativo e decisório — Cadernos SBMI — v002
**Data:** 25/09/2026  
**Status:** aprovado para revisão humana final; não congelado.

## Critério de auditoria

A unidade narrativa exigida nesta rodada é:

`evidência → contexto → relação → mecanismo → interpretação → implicação → decisão → indicador → limite`.

O QA verifica se os cadernos:
- demonstram o raciocínio em vez de apenas listar indicadores;
- preservam fonte, período, unidade, abrangência e natureza do dado;
- distinguem observado, calculado, estimado, benchmark, hipótese, interpretação e recomendação;
- transformam recomendação em decisão testável;
- evitam linguagem genérica;
- preservam as lacunas monetárias e metodológicas;
- não convertem unidade/cadastro/storefront/CNPJ/raiz/optante em market share;
- não convertem REGIC em gasto;
- não convertem demanda modelada em faturamento;
- não convertem survey/POM em prevalência indevida;
- não confundem contrato com pagamento;
- não inferem causalidade de correlação.

## Documentos correntes

| Documento | Drive ID | Extensão aprox. | Estado |
|---|---|---:|---|
| Caderno Geral v004 | `13yqwDHKJuEag4I0l7XaUZ_oDIg5lh0UvQsmJWc3H2Co` | 133.996 caracteres | PASSA |
| Bens Essenciais v003 | `190arYFyxKq_xynAbqU3fGThlpbJiqPXlmqMOrtRHss0` | 66.721 | PASSA |
| Saúde/Higiene v003 | `1d141fQT3aTMtHoj5el9FOlR0mXqTgcNp2E7QqV28ZjI` | 60.486 | PASSA |
| Bens Não Essenciais v003 | `1uBIiR9pH6wqzIH2T5nO_dRpDEu2Cu-qP3v4cCcs2DDE` | 75.899 | PASSA |
| Alimentação/Serviços v003 | `1pyUYH5APuuRR72XZ9Pd1BjpQDcgDQ1yTNActUkium3Y` | 66.895 | PASSA |

## Alterações materiais da rodada

### Caderno Geral v004
- aprofundadas retenção/captura, implicações, prioridades e acompanhamento;
- integrada a camada editorial dos quatro reports setoriais v003;
- acrescentada `RASTREABILIDADE DAS TESES CENTRAIS — DA EVIDÊNCIA À DECISÃO`;
- preservadas as bases técnicas setoriais v002 como lastro, sem confundi-las com a camada editorial corrente.

### Bens Essenciais v003
- demonstrada integralmente a modelagem de demanda;
- aprofundadas duas missões de compra;
- preço tratado como aquisição, imagem e rentabilidade de cesta;
- conveniência operacionalizada;
- fila, ruptura, divergência de preço e perecibilidade ligados a decisão;
- exercícios, diagnóstico, prioridades, indicadores e considerações finais ampliados;
- 5 trilhas evidência→decisão.

### Saúde/Higiene v003
- aprofundadas quatro missões;
- conveniência, autoridade e digital diferenciados por mecanismo;
- CNES mantido como estrutura institucional, não market share;
- controle de possível subcobertura preservado;
- exercícios, diagnóstico, prioridades, indicadores e considerações finais ampliados;
- 5 trilhas evidência→decisão.

### Bens Não Essenciais v003
- desenvolvido o eixo urgência × adiabilidade × risco × comparabilidade;
- market size não estimável explicitado;
- jornadas presencial/híbrida/digital desenvolvidas;
- físico tratado como redução de risco/tempo;
- preço convertido em custo total de compra;
- REGIC restrita aos grupos compatíveis;
- sortimento ligado a demanda não atendida;
- exercícios, diagnóstico, prioridades, indicadores e considerações finais ampliados;
- 5 trilhas evidência→decisão.

### Alimentação/Serviços v003
- alimentação e serviços separados no nível operacional;
- survey n=153 mantido como descritivo da amostra;
- desenvolvido funil pré-serviço;
- tempo de resposta e automação operacionalizados;
- alimentação aprofundada por qualidade, ocasião, canal, delivery e hospitalidade;
- PNAE/B2G preservado como circuito separado;
- exercícios, diagnóstico, prioridades, indicadores e considerações finais ampliados;
- 6 trilhas evidência→decisão.

## Controles numéricos rechecados

### Bens Essenciais
- demanda modelada mensal: R$ 19.558.852,34;
- anual: R$ 234.706.228,14;
- 54 linhas correntes;
- 52 CNPJs documentais validados;
- 52/54 = 96,30% de prontidão interna, não cobertura municipal.

### Saúde/Higiene
- 23 registros privados CNES;
- 7 raízes;
- 4 raízes multiunidade;
- 20/23 = 86,96%;
- maior raiz 8/23 = 34,78%;
- operação recente fora do recorte mantida como controle de subcobertura.

### BNE
- 122 storefronts;
- sensibilidade 121;
- 109 operator_keys;
- 8 raízes multiunidade;
- 21/122 = 17,21%;
- moda 57;
- pet/vet/agro 20;
- óptica/joalheria/relojoaria 12;
- moda + eletro = 64/122 = 52,46% no crosswalk REGIC direto.

### Alimentação/Serviços
- survey n=153;
- SINAC 947;
- SIMEI 728;
- CNAE 56 = 409;
- PNAE CNPJ pago = R$ 869.843,54;
- local = R$ 327.021,02 = 37,60%;
- externo = R$ 542.822,52 = 62,40%;
- agricultura/agroindústria familiar = 19 contratos e R$ 447.585,44 contratados.

## Resultado

**APROVADO PARA REVISÃO HUMANA FINAL.**

Isso significa:
- a camada textual já não depende de linguagem genérica;
- as decisões possuem indicadores de teste;
- os limites permanecem explícitos;
- as principais cadeias de raciocínio estão documentadas.

Isso **não** significa:
- congelamento editorial definitivo;
- canonicalização em `main`;
- merge do PR #41;
- autorização para nova pesquisa primária;
- autorização para transformar lacunas em estimativas.

## Pendência residual

A única etapa editorial prioritária remanescente é leitura humana integral voltada a:
- ritmo;
- repetição improdutiva;
- coerência de sumário;
- uniformidade terminológica;
- precisão e padronização das referências.

Gráficos e PDF continuam opcionais.
