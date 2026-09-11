# Caderno-Base Territorial — diagnóstico analítico integrado v004

## Atualização desta versão

Esta versão preserva o diagnóstico territorial, empresarial, laboral e fiscal anterior e incorpora a **distribuição oficial do rendimento domiciliar per capita** do Censo 2022, o denominador compatível desse universo e uma massa mensal implícita de rendimento. O avanço muda a camada de mercado consumidor de uma descrição baseada apenas em população, domicílios, média e mediana para uma primeira estrutura quantitativa da distribuição da renda.

Abrangência: São Borja/RS.  
Atualização: 2026-09-08.

## 1. Estrutura territorial já consolidada

Permanecem válidos os principais resultados anteriores:

- 6.906 estabelecimentos empresariais no universo RFB 2026-08;
- 284 de matriz externa, ou 4,1124%;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: 25,1606%;
- participação externa estimada na remuneração de dezembro: 29,6897%;
- IPM definitivo 2003–2026;
- VAF oficial publicado em REAL 1994–2025;
- matriz de controle territorial v001 com forte peso funcional externo em varejo, finanças, transportes, atacado, energia e logística.

Essas dimensões permanecem separadas conceitualmente de renda domiciliar e consumo.

## 2. Mercado residente e composição domiciliar

Dados já consolidados:

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**.

A presença de 21,31% de domicílios unipessoais segue sendo relevante como hipótese de segmentação por conveniência e menor escala de consumo, sem inferência automática sobre comportamento de compra.

## 3. Rendimento domiciliar — posição central

Fonte: IBGE/SIDRA, tabela 10295, Censo 2022.

Dados observados:

- rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- rendimento nominal mediano mensal domiciliar per capita: **R$ 1.100,00**.

Cálculos:

- diferença absoluta: **R$ 468,58**;
- média **42,5982%** acima da mediana, apresentada como **42,60%**.

A diferença não é uma medida de desigualdade. A mediana é uma referência central menos sensível aos valores superiores e, portanto, deve acompanhar a média na caracterização mercadológica.

## 4. Distribuição oficial do rendimento domiciliar per capita

Fonte: IBGE/SIDRA, tabela 10296, Censo 2022, São Borja/RS.

Universo observado: **59.038 moradores** em domicílios particulares permanentes ocupados, exclusive pensionistas, empregados(as) domésticos(as) e parentes de empregados(as) domésticos(as).

A consulta oficial foi recuperada pelo workflow `consumer-income-distribution-sidra`, run `34280745734`, job `102244621346`, HTTP 200, com SHA-256 da resposta bruta `c605f8898dbe8ba0af0e22b844078da072e75c9d3a2349da5bee3e6901f2dc09`.

Distribuição observada:

| Classe de rendimento per capita | Pessoas | % |
|---|---:|---:|
| Até 1/4 SM | 2.441 | 4,13463 |
| >1/4 a 1/2 SM | 10.917 | 18,49148 |
| >1/2 a 1 SM | 20.174 | 34,17121 |
| >1 a 2 SM | 15.630 | 26,47447 |
| >2 a 3 SM | 4.659 | 7,89153 |
| >3 a 5 SM | 2.086 | 3,53332 |
| >5 a 10 SM | 1.237 | 2,09526 |
| >10 a 15 SM | 286 | 0,48443 |
| >15 a 20 SM | 33 | 0,05590 |
| >20 SM | 87 | 0,14736 |
| Sem rendimento | 1.488 | 2,52041 |

A maior classe individual é **mais de 1/2 a 1 salário mínimo**, com 34,17121%.

## 5. Agregações analíticas

Natureza: calculado a partir das classes oficiais.

- sem rendimento ou até 1 SM: **35.020 pessoas / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- mais de 2 SM: **8.388 / 14,20780%**;
- mais de 5 SM: **1.643 / 2,78295%**.

Essas agregações não constituem categorias oficiais nem classes sociais. Elas descrevem a distribuição de pessoas por faixas de rendimento domiciliar per capita.

## 6. Massa mensal implícita de rendimento

Com a média e o denominador do mesmo universo:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04 por mês`

Natureza: calculado.  
Referência: Censo 2022.  
Unidade: R$/mês.

O resultado é uma **massa mensal implícita de rendimento no universo estatístico**. Não equivale a renda disponível, consumo efetivo, faturamento do varejo, potencial de consumo setorial ou recursos necessariamente gastos no município.

## 7. Interpretação do mercado consumidor

A distribuição modifica qualitativamente a leitura da demanda residente. A média de R$ 1.568,58 pode superdimensionar a referência do consumidor central se utilizada isoladamente: a mediana é R$ 1.100,00 e 85,79220% dos moradores do universo estão sem rendimento ou em faixas de até dois salários mínimos per capita.

Isso não significa que 85,79% da renda monetária esteja concentrada nessas faixas. O indicador mede proporção de pessoas, e não participação no total da renda. Também não informa gasto, poupança, endividamento, preferência ou consumo fora do município.

A implicação mercadológica é que os quatro cadernos setoriais deverão trabalhar com **segmentação de demanda**, evitando representar o mercado por um consumidor médio único.

## 8. Relação com emprego e remuneração formal

A RAIS 2025 registra R$ 23.940.059,71 de remuneração nominal de dezembro informada no recorte empresarial. A massa domiciliar implícita de R$ 92,61 milhões não deve ser tratada como simples múltiplo ou complemento da RAIS: os universos, conceitos e períodos são diferentes.

A comparação apenas demonstra que a renda das famílias não pode ser reconstruída exclusivamente pelo emprego formal empresarial. Rendas previdenciárias, transferências e outras fontes devem ser incorporadas diretamente por fontes apropriadas.

## 9. Diagnóstico integrado atualizado

### Fatos sustentados

São Borja combina uma base empresarial numericamente local, peso laboral/remuneratório externo desproporcional em setores específicos, mercado residente próximo de 60 mil pessoas, estrutura domiciliar com presença relevante de domicílios unipessoais e uma distribuição de rendimento per capita fortemente concentrada, em número de moradores, nas faixas até dois salários mínimos.

### Interpretação

O mercado local não pode ser descrito adequadamente apenas por tamanho populacional, PIB per capita ou renda média. A estrutura empresarial indica quem controla e emprega; a renda domiciliar indica a capacidade econômica dos residentes; a distribuição mostra que essa capacidade é heterogênea. A análise setorial deve cruzar essas três dimensões sem fundi-las em um índice único.

### O que ainda não pode ser concluído

Ainda não é possível afirmar:

- qual parcela da massa de rendimento é efetivamente disponível para consumo;
- quanto é gasto em São Borja e quanto é direcionado para outros territórios/canais;
- como o gasto se distribui entre bens essenciais, saúde/higiene, bens não essenciais, serviços e alimentação fora do lar;
- qual é o peso de aposentadorias, pensões e transferências monetárias na renda local;
- qual é a concentração monetária da renda apenas a partir das faixas de pessoas.

## 10. Próxima agenda

As lacunas de média, mediana, distribuição e denominador compatível da renda domiciliar do Censo 2022 estão encerradas. As prioridades passam a ser:

1. recuperar benefícios previdenciários emitidos/pagos a residentes de São Borja por fonte oficial, preservando município de residência e sem confundir registros com pessoas únicas;
2. recuperar transferências monetárias efetivamente recebidas por famílias, distinguindo-as de repasses administrativos;
3. definir, somente após essas camadas, uma metodologia explícita para capacidade de compra, renda disponível aproximada e retenção local do gasto;
4. conectar a distribuição de renda aos quatro mercados setoriais e à matriz de controle territorial.

## 11. Artefatos

- Caderno-Base v008 — abas `Mercado_consumidor_base` e `Resumo` atualizadas;
- `docs/caderno_base/mercado_consumidor_base_v003.md`;
- pacote SIDRA 10295 no Drive — ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`;
- pacote SIDRA 10296 no Drive — ID `1eUgoL_9n5oXNtVBWTC-pYRFpCJul2cQA`;
- Drive Doc SIDRA 10295 — ID `1WrVv6dDXeB-nzz8jxl5GLwR2LrPZPrBchKtaQu0KfqY`;
- Drive Doc SIDRA 10296 — ID `1NUbnNZ99hhlgoejWGTj1HR1CFcxJpwSnnbf9tHEostQ`.
