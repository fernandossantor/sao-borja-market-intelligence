# Caderno-Base Territorial — mercado consumidor: base demográfica, domiciliar, de renda e benefícios v005

## Objetivo

Esta versão preserva as camadas demográfica, domiciliar, econômica, laboral, de rendimento domiciliar e INSS/SUIBE da v004 e incorpora uma primeira referência oficial municipal de **transferência monetária direta do Novo Bolsa Família** para São Borja/RS em julho de 2026.

Abrangência geográfica: São Borja/RS.  
Atualização: 2026-09-08.  
Tabela principal: aba `Mercado_consumidor_base` do Caderno-Base v008.  
Tabelas de sustentação: `INSS_beneficios_202607` e `Novo_Bolsa_Familia_202607`.

## 1. Escala territorial consolidada

- população Censo 2022: **59.676 pessoas** — IBGE/SIDRA;
- população estimada 2025: **61.311 pessoas** — IBGE;
- domicílios unipessoais: **4.815 / 21,31%**;
- nucleares: **13.820 / 61,17%**;
- estendidos: **3.518 / 15,57%**;
- compostos: **438 / 1,94%**;
- PIB 2023: **R$ 2.550.388.000**;
- PIB per capita 2023: **R$ 42.737,25**.

PIB não equivale a renda domiciliar; composição domiciliar não demonstra comportamento de compra.

## 2. Rendimento domiciliar per capita — Censo 2022

Fonte: IBGE/SIDRA, tabelas 10295 e 10296.

Dados observados:

- média nominal mensal per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**.

Agregações calculadas pelo SBMI:

- sem rendimento ou até 1 SM: **35.020 / 59,31773%**;
- sem rendimento ou até 2 SM: **50.650 / 85,79220%**;
- mais de 2 SM: **8.388 / 14,20780%**;
- mais de 5 SM: **1.643 / 2,78295%**.

Essas agregações não são classes sociais oficiais.

## 3. Massa mensal implícita de rendimento domiciliar

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Natureza: **calculado**. Referência: Censo 2022.

O resultado é massa mensal implícita no universo estatístico. Não equivale a renda disponível, consumo, faturamento do comércio ou potencial setorial.

## 4. Renda formal do trabalho — referência distinta

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial, com 7.800 valores informados e 795 ausentes.

Essa massa não é diretamente somável à massa domiciliar do Censo: os universos, períodos e conceitos são distintos.

## 5. Benefícios emitidos pelo INSS/SUIBE — julho de 2026

Fonte: INSS Portal de Dados Abertos / SUIBE — `Benefícios Emitidos Julho 2026`.

Recorte: `municipio_residencia = 19181-RS-SAO BORJA`.

Resultados calculados a partir dos registros oficiais:

- **14.247 registros**;
- **14.247 registros com `credito` válido**;
- soma de `credito`: **R$ 24.535.168,54**;
- crédito médio por registro: **R$ 1.722,13**.

A contagem é de registros, não pessoas beneficiárias únicas. O conjunto contém espécies previdenciárias, acidentárias, assistenciais e legadas; por isso o total não é relabelado como massa previdenciária contributiva.

As duas espécies literalmente denominadas `AMPARO SOCIAL` somam **3.385 registros** e **R$ 4.777.117,64**, equivalentes a **19,47049%** do crédito total. Esse subtotal não representa toda a assistência social.

## 6. Novo Bolsa Família — julho de 2026

Fonte: Portal da Transparência do Governo Federal / CGU — Dados Abertos — Novo Bolsa Família.

A página oficial gerou o link da competência julho de 2026 (`/202607`). O arquivo nacional efetivamente observado possui nove campos: `MÊS COMPETÊNCIA`, `MÊS REFERÊNCIA`, `UF`, `CÓDIGO MUNICÍPIO SIAFI`, `NOME MUNICÍPIO`, `CPF FAVORECIDO`, `NIS FAVORECIDO`, `NOME FAVORECIDO` e `VALOR PARCELA`.

O recorte usa:

- `UF = RS`;
- `NOME MUNICÍPIO`, normalizado, igual a `SAO BORJA`;
- código Município SIAFI observado `8863`.

Em todos os registros municipais, `MÊS COMPETÊNCIA = 202607` e `MÊS REFERÊNCIA = 202607`.

### Resultados calculados a partir dos registros oficiais

- **2.199 registros/parcela**;
- **2.199 registros com `VALOR PARCELA` válido**;
- soma de `VALOR PARCELA`: **R$ 1.513.564,00**;
- média por registro/parcela: **R$ 688,30**.

Controles agregados de integridade:

- **2.198 NIS não vazios distintos** e 1 registro com NIS vazio;
- **1.746 CPF não vazios distintos** e 439 registros com CPF vazio.

Nenhum CPF, NIS ou nome foi persistido no GitHub, artifact final, Drive ou Caderno. Os identificadores foram usados apenas transitoriamente para controles agregados.

**Registro/parcela não equivale automaticamente a família ou pessoa beneficiária única.** O projeto não usa 2.199 como número de famílias sem regra explícita da fonte.

## 7. Distinção entre Novo Bolsa Família e IGD/FMAS

A planilha do Bolsa Família anteriormente localizada no Drive permanece classificada como **IGD transferido ao Fundo Municipal de Assistência Social**, recurso administrativo de gestão. Ela continua excluída de renda domiciliar e demanda de consumo.

A nova extração é conceitualmente diferente: `VALOR PARCELA` pertence à base de favorecidos do Novo Bolsa Família e representa transferência monetária registrada no programa.

Mesmo nesse caso, valor registrado/disponibilizado não equivale a consumo efetivo nem a valor necessariamente retido no município.

## 8. Quatro referências monetárias e a regra de não soma

O Caderno-Base dispõe agora de quatro referências de natureza diferente:

- **R$ 92.605.826,04/mês** — massa implícita do rendimento domiciliar, Censo 2022, calculada;
- **R$ 23.940.059,71** — remuneração nominal de dezembro informada na RAIS 2025;
- **R$ 24.535.168,54** — crédito de benefícios emitidos pelo INSS/SUIBE em julho de 2026;
- **R$ 1.513.564,00** — soma de `VALOR PARCELA` do Novo Bolsa Família em julho de 2026.

Essas grandezas **não devem ser somadas mecanicamente**. Os universos e conceitos são distintos e pode haver sobreposição de pessoas entre programas e fontes. A utilidade analítica, nesta etapa, é mostrar a pluralidade das fontes de renda e transferência que sustentam a economia residente.

## 9. Interpretação mercadológica

A incorporação do Novo Bolsa Família resolve uma lacuna específica: o projeto passa a ter uma fonte oficial de transferência monetária diretamente registrada no programa, em vez de confundir repasses administrativos de gestão com benefício às pessoas.

Em julho de 2026, o fluxo observado no Novo Bolsa Família foi de **R$ 1,514 milhão**. O resultado é material como camada de caracterização da renda não laboral, mas não informa quanto foi gasto no comércio local, quais categorias absorveram o recurso ou a propensão a consumir dos favorecidos.

A leitura combinada com Censo, RAIS e INSS/SUIBE reforça que a capacidade econômica residente não pode ser descrita apenas pela renda formal do trabalho. Isso é uma **interpretação**, não uma estimativa de renda total corrente.

## 10. Limitações

- registros/parcela do Novo Bolsa Família ≠ famílias;
- registros INSS/SUIBE ≠ pessoas beneficiárias únicas;
- valor mensal ≠ renda anual;
- transferência monetária ≠ consumo efetivo;
- não há medição de retenção local, poupança, endividamento ou alocação setorial do gasto;
- a série mensal do Novo Bolsa Família ainda não foi construída;
- o arquivo Novo Bolsa Família 202607 observado não contém `DATA DISPONIBILIZAÇÃO`; não se transpõem campos de outras versões da fonte;
- Censo 2022, RAIS 2025, INSS 2026-07 e Novo Bolsa Família 2026-07 não devem ser somados sem metodologia explícita de harmonização e controle de sobreposições.

## 11. Rastreabilidade — Novo Bolsa Família

- workflow: `novo-bolsa-familia-sao-borja-extract`;
- run: `34284691474`;
- job: `102257430159`;
- artifact: `10079014259`;
- SHA-256 do artifact: `41a27542e9b94ce07606ea7cb15868d6aafc67c073f7c8d86e21b9bc7d44c15e`;
- SHA-256 do ZIP nacional: `f66e621bfdbb945cf324679e216d3d3b42d2029f39be7f646e046fd28b4c30d4`;
- SHA-256 do CSV agregado municipal: `fc4ab012979f5802567bd028f2b87ad2fbb208d5dec99fb02bc24323a9c5d07e`.

Drive:

- pasta bruta: ID `15loZ2NDpNcwIwI4hFTxjsNKjFzaxekhq`;
- pacote final agregado e sem PII: ID `1am7E0ILJCp26z9X8MjLu7sdSxqYRN1jn`;
- CSV agregado: ID `1cR1KfPWe_MMwGF9KHHrwNoGJYT5RcjUs`;
- nota metodológica nativa: ID `11LpVM7KSmgzZ7hk6Hl5eZix_FVAzPhMP9tRfXheaDNc`.

## 12. Lacuna remanescente

O Novo Bolsa Família está incorporado. A lacuna passa a ser **outras transferências monetárias diretamente recebidas por residentes/famílias**, sempre separando benefício monetário de repasse administrativo.

## 13. Próxima agenda

1. construir série mensal do Novo Bolsa Família com a mesma regra de privacidade e filtro territorial;
2. mapear outras transferências monetárias relevantes em fontes oficiais;
3. avaliar série mensal INSS/SUIBE;
4. somente depois definir metodologia explícita para renda disponível aproximada, capacidade de compra e retenção local;
5. conectar distribuição de renda e fontes de transferência aos quatro cadernos setoriais e à matriz de controle territorial.
