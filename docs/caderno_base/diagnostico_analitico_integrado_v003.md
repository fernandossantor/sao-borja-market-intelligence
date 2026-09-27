# Caderno-Base Territorial — diagnóstico analítico integrado v003

## Atualização desta versão

Esta versão preserva o diagnóstico integrado anterior e incorpora a primeira camada oficial de **rendimento domiciliar per capita** ao mercado consumidor. O foco da atualização é conectar população, estrutura domiciliar, emprego/remuneração e renda das famílias sem transformar grandezas distintas em proxies indevidas.

Abrangência: São Borja/RS.  
Atualização: 2026-09-08.

## 1. Estrutura territorial já consolidada

O diagnóstico anterior permanece válido:

- 6.906 estabelecimentos empresariais no universo empresarial RFB 2026-08;
- 284 de matriz externa, ou 4,1124%;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: 25,1606%;
- participação externa estimada na remuneração de dezembro: 29,6897%;
- peso externo no emprego aproximadamente 6,12 vezes o peso cadastral;
- diferencial de remuneração média implícita externa/local de aproximadamente 22,03%;
- concentração externa especialmente relevante em varejo, finanças, transportes, atacado, energia e logística.

O IPM definitivo permanece fechado em 2003–2026 e o VAF oficial publicado em REAL em 1994–2025. O alinhamento exploratório VAF `t` → IPM `t+2` continua descritivo e não causal.

## 2. Mercado residente e estrutura domiciliar

### Dados observados/estimados

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**.

A soma das quatro categorias reportadas é 22.591 domicílios, mas não é relabelada como total oficial sem linha total explicitamente verificada na fonte.

### Interpretação

A participação de 21,31% de domicílios unipessoais é relevante para segmentação e justifica testar hipóteses de conveniência, menor escala de embalagem e serviços individualizados. Trata-se de hipótese mercadológica, não comportamento de compra observado.

## 3. Rendimento domiciliar per capita — nova evidência oficial

### Dados observados

Fonte: IBGE/SIDRA, tabela 10295, Censo 2022, São Borja/RS, código 4318002.

- variável 13431 — rendimento nominal **médio** mensal domiciliar per capita: **R$ 1.568,58**;
- variável 13534 — rendimento nominal **mediano** mensal domiciliar per capita: **R$ 1.100,00**.

A definição da tabela refere-se aos moradores em domicílios particulares permanentes ocupados, **exclusive pensionistas, empregados(as) domésticos(as) e parentes de empregados(as) domésticos(as)**.

Natureza: observado em fonte oficial.

### Auditoria da recuperação

Consulta oficial:

`https://apisidra.ibge.gov.br/values/t/10295/n6/4318002/v/13431,13534/p/2022/h/y/f/a/d/m`

- workflow: `consumer-income-sidra`;
- run: `34269331974`;
- job: `102206631993`;
- HTTP 200;
- SHA-256 da resposta JSON bruta: `29e84da86e8424d0727325647634b9565e1f181374bf3cedf3c3c64936adea33`;
- artifact ID `10073147229`, ZIP SHA-256 `7c1d5f13cf6445810a376cae8ed929734f0a00254b82354d2c923351c8cced02`.

Pacote preservado no Drive: `01_fontes_e_coletas/demografia/renda_domiciliar/sidra_10295_sao_borja_income_2022_official_package.zip`, ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`.

## 4. Cálculos derivados e interpretação

Diferença absoluta:

`1.568,58 − 1.100,00 = R$ 468,58 por pessoa/mês`

Diferença relativa da média em relação à mediana:

`(1.568,58 / 1.100,00 − 1) × 100 = 42,5982%`

Apresentação: **42,60%**.

Natureza: calculado.

### Interpretação

A mediana substancialmente inferior à média é relevante para a leitura mercadológica. A média é mais sensível aos valores superiores da distribuição; a mediana fornece uma referência central menos influenciada por esses valores. Por isso, o consumidor típico não deve ser representado apenas pela média de R$ 1.568,58.

A distância entre média e mediana é compatível com assimetria à direita, mas **não é uma medida de desigualdade**. Não permite inferir Gini, quantis, concentração ou peso dos estratos superiores sem a distribuição completa.

## 5. Escala econômica versus renda das famílias

O PIB municipal de 2023 permanece em R$ 2.550.388.000 e o PIB per capita em R$ 42.737,25. Esses indicadores medem produção territorial e **não equivalem** ao rendimento domiciliar per capita médio de R$ 1.568,58/mês ou mediano de R$ 1.100,00/mês.

A remuneração nominal de dezembro informada na RAIS 2025, R$ 23.940.059,71, também mede outro fenômeno: fluxo do trabalho formal empresarial observado no mês, e não renda total das famílias.

## 6. Limitação para massa de renda e capacidade de compra

A recuperação da média e mediana encerra uma lacuna importante, mas **não autoriza calcular massa mensal de renda** multiplicando a média pela população total.

Não utilizar:

`R$ 1.568,58 × 59.676`

nem

`R$ 1.568,58 × 61.311`

como massa de renda. Para esse cálculo, é necessário recuperar o número de moradores correspondente exatamente ao mesmo universo da tabela 10295 e preservar a mesma referência temporal.

Também permanecem necessárias faixas/quantis para segmentação econômica robusta.

## 7. Rendas não laborais

As próximas lacunas prioritárias são:

- aposentadorias, pensões e benefícios previdenciários pagos a residentes;
- transferências monetárias efetivamente recebidas pelas famílias;
- distribuição municipal do rendimento por faixas/quantis;
- número de moradores do universo da tabela 10295.

A planilha de Bolsa Família já localizada no Drive é de **IGD transferido ao FMAS**, recurso administrativo de gestão. Ela permanece excluída de renda familiar e potencial de consumo.

## 8. Diagnóstico atualizado

### Fatos

São Borja possui mercado residente próximo de 60 mil pessoas; 21,31% dos domicílios são unipessoais; a base empresarial é numericamente local, mas estruturas externas têm peso laboral/remuneratório desproporcional; e o rendimento domiciliar per capita do Censo 2022 apresenta média de R$ 1.568,58 e mediana de R$ 1.100,00 no universo definido pela tabela 10295.

### Interpretação

A nova camada de renda permite avançar da mera escala populacional/econômica para uma primeira noção de **posição econômica central das famílias**. A mediana de R$ 1.100,00 sugere que análises de mercado baseadas apenas na média podem superdimensionar a referência do consumidor central.

Isso não significa que o mercado esteja restrito à mediana nem que todos os domicílios tenham capacidade de compra semelhante. Ao contrário, a diferença entre média e mediana reforça a necessidade de segmentação por distribuição de renda antes de estimar demanda monetária por setor.

## 9. Próxima agenda

1. recuperar distribuição por faixas/quantis e número de moradores do mesmo universo da tabela 10295;
2. incorporar rendas previdenciárias pagas a residentes;
3. incorporar transferências monetárias efetivamente recebidas pelas famílias;
4. construir, somente então, massa de renda/capacidade de compra com denominadores compatíveis;
5. integrar a demanda às tipologias de controle territorial e aos quatro cadernos setoriais;
6. manter fiscalidade, VAF e IPM em trilha própria, sem tratar produção, transferência pública e renda domiciliar como equivalentes.

## 10. Artefatos

- Caderno-Base v008 — aba `Mercado_consumidor_base` e `Resumo` atualizadas;
- `docs/caderno_base/mercado_consumidor_base_v002.md`;
- Drive Doc `Renda domiciliar per capita — SIDRA 10295 — auditoria e incorporação — 20260908`, ID `1WrVv6dDXeB-nzz8jxl5GLwR2LrPZPrBchKtaQu0KfqY`;
- pacote oficial SIDRA no Drive, ID `1BXmiVuMD6LdvIOeCWQGY0SwVD1qj64jz`;
- documentação e derivados anteriores permanecem preservados para rastreabilidade.
