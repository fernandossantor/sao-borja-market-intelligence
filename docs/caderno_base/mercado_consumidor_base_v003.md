# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar e de renda v003

## Objetivo

Esta versão preserva as camadas anteriores de população, domicílios, economia formal e rendimento domiciliar médio/mediano e incorpora a **distribuição oficial do rendimento nominal mensal domiciliar per capita** de São Borja no Censo 2022. O avanço fecha também o número de moradores do mesmo universo estatístico das tabelas de renda e permite calcular uma massa mensal implícita sem recorrer à população total como denominador incompatível.

Abrangência geográfica: São Borja/RS.  
Período da camada de renda: Censo 2022.  
Data de atualização: 2026-09-08.  
Tabela de sustentação: aba `Mercado_consumidor_base` do Caderno-Base v008.

## 1. Bases territoriais já consolidadas

Permanecem válidos os dados e cuidados documentados nas versões anteriores:

- população Censo 2022: **59.676 pessoas** — IBGE/SIDRA, tabela 4714;
- população estimada 2025: **61.311 pessoas** — IBGE, estimativa oficial;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%** — IBGE/SIDRA, tabela 9879;
- PIB a preços correntes 2023: **R$ 2.550.388.000**;
- PIB per capita 2023: **R$ 42.737,25**.

A soma das quatro categorias domiciliares reportadas é 22.591 domicílios, mas não é relabelada como total oficial sem linha total explicitamente verificada na fonte. PIB e PIB per capita medem produção e **não equivalem a renda domiciliar nem poder de compra**.

## 2. Rendimento domiciliar médio e mediano — tabela 10295

Fonte: IBGE/SIDRA — tabela 10295 — Censo 2022 — São Borja/RS, código 4318002.

### Dados observados

- variável 13431 — rendimento nominal **médio** mensal domiciliar per capita: **R$ 1.568,58**;
- variável 13534 — rendimento nominal **mediano** mensal domiciliar per capita: **R$ 1.100,00**.

Universo: moradores em domicílios particulares permanentes ocupados, **exclusive pensionistas, empregados(as) domésticos(as) e parentes de empregados(as) domésticos(as)**.

Consulta oficial: `https://apisidra.ibge.gov.br/values/t/10295/n6/4318002/v/13431,13534/p/2022/h/y/f/a/d/m`.

Rastreabilidade: workflow `consumer-income-sidra`, run `34269331974`, job `102206631993`, HTTP 200, SHA-256 da resposta bruta `29e84da86e8424d0727325647634b9565e1f181374bf3cedf3c3c64936adea33`.

Pacote preservado no Drive: `sidra_10295_sao_borja_income_2022_official_package.zip`, ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`.

### Cálculos

`R$ 1.568,58 − R$ 1.100,00 = R$ 468,58 por pessoa/mês`

`(1.568,58 / 1.100,00 − 1) × 100 = 42,5982%`

Apresentação: **42,60%**. Natureza: calculado. A diferença entre média e mediana não é medida de desigualdade.

## 3. Distribuição do rendimento domiciliar per capita — tabela 10296

Fonte: IBGE/SIDRA — tabela 10296 — Censo 2022 — São Borja/RS, código 4318002.

Consulta oficial:

`https://apisidra.ibge.gov.br/values/t/10296/n6/4318002/v/13604,1013604/p/2022/c2/0/c86/0/c386/all/h/y/f/a/d/m`

Variáveis:

- `13604`: moradores do mesmo universo das tabelas de rendimento — unidade pessoas;
- `1013604`: percentual do total geral — unidade percentual.

Filtros: sexo Total; cor ou raça Total; todas as classes de rendimento domiciliar per capita associadas à tabela.

### Auditoria

- workflow: `consumer-income-distribution-sidra`;
- run: `34280745734`;
- job: `102244621346`;
- HTTP 200;
- resposta bruta: 14.472 bytes;
- 25 linhas JSON: 1 cabeçalho + 24 linhas de dados;
- SHA-256 da resposta bruta: `c605f8898dbe8ba0af0e22b844078da072e75c9d3a2349da5bee3e6901f2dc09`;
- artifact ID `10077490347`;
- SHA-256 do ZIP do artifact: `29bf70c67b98c2ee7c934bfdc25ab284dbef553eb29245182be7a1c9f3cfa7f8`.

Pacote preservado no Drive: `sidra_10296_sao_borja_income_distribution_2022_v002_official_package.zip`, ID `1eUgoL_9n5oXNtVBWTC-pYRFpCJul2cQA`.

Documento metodológico no Drive: `Distribuição do rendimento domiciliar per capita — SIDRA 10296 — auditoria e incorporação — 20260908`, ID `1NUbnNZ99hhlgoejWGTj1HR1CFcxJpwSnnbf9tHEostQ`.

## 4. Dados observados — distribuição

O universo total da tabela é de **59.038 moradores**. A soma das onze classes não totais reproduz 59.038 pessoas e os percentuais oficiais somam 100,00000%.

| Classe de rendimento nominal mensal domiciliar per capita | Pessoas | Percentual oficial |
|---|---:|---:|
| Até 1/4 de salário mínimo | 2.441 | 4,13463% |
| Mais de 1/4 a 1/2 salário mínimo | 10.917 | 18,49148% |
| Mais de 1/2 a 1 salário mínimo | 20.174 | 34,17121% |
| Mais de 1 a 2 salários mínimos | 15.630 | 26,47447% |
| Mais de 2 a 3 salários mínimos | 4.659 | 7,89153% |
| Mais de 3 a 5 salários mínimos | 2.086 | 3,53332% |
| Mais de 5 a 10 salários mínimos | 1.237 | 2,09526% |
| Mais de 10 a 15 salários mínimos | 286 | 0,48443% |
| Mais de 15 a 20 salários mínimos | 33 | 0,05590% |
| Mais de 20 salários mínimos | 87 | 0,14736% |
| Sem rendimento | 1.488 | 2,52041% |

A maior classe individual é **mais de 1/2 a 1 salário mínimo**, com 20.174 moradores e 34,17121% do universo; a segunda é **mais de 1 a 2 salários mínimos**, com 15.630 e 26,47447%.

Natureza: observado em fonte oficial.

## 5. Agregações analíticas do SBMI

As agregações abaixo são **calculadas** e não correspondem a categorias oficiais únicas da tabela.

### Sem rendimento ou até 1 salário mínimo

`2,52041 + 4,13463 + 18,49148 + 34,17121 = 59,31773%`

Equivalente a **35.020 pessoas**.

### Sem rendimento ou até 2 salários mínimos

`59,31773 + 26,47447 = 85,79220%`

Equivalente a **50.650 pessoas**.

### Mais de 2 salários mínimos

`100 − 85,79220 = 14,20780%`

Equivalente a **8.388 pessoas**.

### Mais de 5 salários mínimos

`2,09526 + 0,48443 + 0,05590 + 0,14736 = 2,78295%`

Equivalente a **1.643 pessoas**.

Essas agregações não devem ser chamadas automaticamente de classes sociais ou estratos de consumo; são apenas consolidações das categorias oficiais de rendimento per capita.

## 6. Massa mensal implícita de rendimento no universo estatístico

A recuperação de 59.038 moradores permite usar um denominador compatível com a média da tabela 10295:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04 por mês`

Natureza: **calculado**.  
Unidade: R$/mês.  
Período: Censo 2022.  
Abrangência: universo estatístico das tabelas 10295/10296 em São Borja.

O resultado deve ser denominado **massa mensal implícita de rendimento domiciliar no universo estatístico**. Não equivale a renda disponível, consumo efetivo, faturamento do comércio, potencial de consumo setorial nem montante necessariamente gasto ou retido no município. Também não deve ser anualizado mecanicamente sem objetivo e metodologia explícitos.

## 7. Interpretação mercadológica

A distribuição torna mais precisa a leitura já sugerida pela diferença entre média e mediana. **85,79220%** dos moradores do universo estão sem rendimento ou nas classes de até dois salários mínimos de rendimento domiciliar per capita. Por isso, a média de R$ 1.568,58 não deve ser usada isoladamente como representação do consumidor central; a mediana de R$ 1.100,00 é uma referência complementar importante.

Isso não significa que 85,79% da renda monetária esteja nas faixas inferiores — o indicador mede **participação de pessoas**, não participação no total monetário da renda. Também não demonstra comportamento de compra, elasticidade, preferência, endividamento ou disposição a pagar.

A implicação para os cadernos setoriais é metodológica: análises de demanda devem considerar distribuição e segmentação, evitando a fórmula simplista `população × renda média` como sinônimo de mercado potencial.

## 8. Relação com a renda formal do trabalho

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial, com 7.800 valores informados e 795 ausentes. Esse fluxo mensal específico do trabalho formal não é comparável diretamente à massa implícita de R$ 92,61 milhões como se ambos medissem o mesmo fenômeno: a RAIS cobre vínculos empresariais formais e outra referência temporal; a renda domiciliar inclui diferentes fontes de rendimento e segue o universo censitário definido pelo IBGE.

A diferença entre as grandezas reforça a necessidade de incorporar rendas não laborais em fonte própria, e não de estimá-las por subtração.

## 9. Rendas não laborais — lacunas remanescentes

As principais lacunas da camada de renda passam a ser:

1. aposentadorias, pensões e benefícios previdenciários pagos a residentes, em fonte oficial;
2. transferências monetárias efetivamente recebidas pelas famílias, em fonte oficial;
3. posteriormente, parâmetros para estimar renda disponível, retenção local e alocação setorial do gasto.

A planilha de Programa Bolsa Família localizada anteriormente no Drive permanece classificada como **IGD transferido ao FMAS**, recurso administrativo de gestão e não benefício monetário às famílias. Ela não integra renda domiciliar nem demanda de consumo.

## 10. Diagnóstico atualizado

### Fatos

São Borja possui mercado residente próximo de 60 mil pessoas. No universo censitário de rendimento domiciliar per capita, são 59.038 moradores; a média mensal é R$ 1.568,58, a mediana R$ 1.100,00, e 85,79220% dos moradores estão sem rendimento ou em classes de até dois salários mínimos per capita.

### Cálculo

A massa mensal implícita de rendimento no mesmo universo é **R$ 92.605.826,04**.

### Interpretação

A camada de renda já permite caracterizar a posição central e a distribuição da capacidade econômica dos residentes com muito mais precisão do que PIB per capita ou salário formal isolado. A estrutura observada recomenda segmentação econômica e leitura diferenciada dos quatro mercados setoriais.

### O que ainda não pode ser concluído

Não é possível converter R$ 92,61 milhões em “potencial de consumo de São Borja” sem evidências adicionais sobre rendas não laborais, tributação e outras deduções, poupança/endividamento, consumo fora do município, retenção local e distribuição do gasto entre categorias. Tampouco é possível inferir concentração monetária da renda apenas pela distribuição de pessoas em faixas.

## 11. Próxima agenda

A distribuição de renda e o denominador compatível estão **encerrados como lacunas de fonte** para o Censo 2022. A prioridade passa a ser previdência e transferências monetárias efetivamente recebidas pelos residentes/famílias. Depois dessas camadas, o projeto poderá estruturar uma medida de capacidade de compra com hipóteses explicitadas e conectá-la à matriz de controle territorial e aos quatro cadernos setoriais.
