# Caderno-Base Territorial — diagnóstico analítico integrado v006

## Atualização desta versão

Esta versão preserva o diagnóstico territorial, empresarial, laboral, fiscal, de renda domiciliar e INSS/SUIBE da v005 e incorpora a primeira referência oficial municipal de **transferência monetária direta do Novo Bolsa Família**, competência julho de 2026.

Abrangência: São Borja/RS.  
Atualização: 2026-09-08.

## 1. Estrutura territorial consolidada

Permanecem válidos:

- 6.906 estabelecimentos empresariais no universo RFB 2026-08;
- 284 de matriz externa, ou 4,1124%;
- 8.595 vínculos empresariais RAIS 2025;
- participação externa estimada no emprego: 25,1606%;
- participação externa estimada na remuneração de dezembro: 29,6897%;
- IPM definitivo 2003–2026;
- VAF oficial publicado em REAL 1994–2025;
- matriz de controle territorial v001 com forte peso funcional externo em setores específicos.

Essas dimensões continuam separadas conceitualmente de renda domiciliar, benefícios, transferências e consumo.

## 2. Mercado residente e renda domiciliar

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- domicílios unipessoais: **4.815 / 21,31%**.

IBGE/SIDRA — Censo 2022:

- rendimento nominal médio mensal domiciliar per capita: **R$ 1.568,58**;
- mediana: **R$ 1.100,00**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM per capita: **50.650 / 85,79220%**, agregação calculada pelo SBMI.

Massa mensal implícita no mesmo universo:

`R$ 1.568,58 × 59.038 = R$ 92.605.826,04/mês`

Essa massa é calculada no universo censitário e não equivale a renda disponível ou consumo.

## 3. Renda formal do trabalho

A RAIS 2025 registra **R$ 23.940.059,71** de remuneração nominal de dezembro informada no recorte empresarial. É um fluxo de vínculos formais empresariais, não renda domiciliar total.

## 4. Benefícios emitidos pelo INSS/SUIBE — julho de 2026

Fonte: INSS Portal de Dados Abertos / SUIBE.

Recorte: `municipio_residencia = 19181-RS-SAO BORJA`.

Resultados calculados a partir dos registros oficiais:

- **14.247 registros emitidos**;
- **14.247 registros com `credito` válido**;
- crédito total: **R$ 24.535.168,54**;
- crédito médio por registro: **R$ 1.722,13**.

A contagem é de registros, não pessoas únicas. As duas espécies literalmente denominadas `AMPARO SOCIAL` respondem por **R$ 4.777.117,64**, ou **19,47049%** do crédito, sem que esse subtotal seja relabelado como toda a assistência social.

## 5. Novo Bolsa Família — julho de 2026

Fonte: Portal da Transparência do Governo Federal / CGU — Dados Abertos — Novo Bolsa Família.

A interface oficial disponibiliza julho de 2026 e gera o endereço `/novo-bolsa-familia/202607`. O arquivo efetivamente observado contém nove campos, entre eles `MÊS COMPETÊNCIA`, `MÊS REFERÊNCIA`, `UF`, `CÓDIGO MUNICÍPIO SIAFI`, `NOME MUNICÍPIO` e `VALOR PARCELA`.

Filtro territorial:

- `UF = RS`;
- `NOME MUNICÍPIO` normalizado = `SAO BORJA`;
- código Município SIAFI observado `8863`.

Resultados calculados a partir dos registros oficiais:

- **2.199 registros/parcela**;
- **2.199 registros com `VALOR PARCELA` válido**;
- soma de `VALOR PARCELA`: **R$ 1.513.564,00**;
- média por registro/parcela: **R$ 688,30**.

Em todos os registros municipais, `MÊS COMPETÊNCIA = 202607` e `MÊS REFERÊNCIA = 202607`.

Como controle agregado de integridade, foram observados **2.198 NIS não vazios distintos** e 1 registro com NIS vazio. Nenhum CPF, NIS ou nome individual foi persistido nos artifacts, Drive, GitHub ou Caderno.

**Não se conclui que 2.199 registros representem 2.199 famílias ou pessoas únicas.**

## 6. Correção conceitual: benefício direto ≠ IGD/FMAS

A planilha do Bolsa Família localizada anteriormente no Drive registra **IGD transferido ao FMAS**, recurso administrativo de gestão. Ela permanece excluída de renda domiciliar e demanda de consumo.

A nova fonte resolve essa lacuna específica: `VALOR PARCELA` é uma medida diretamente ligada aos registros de favorecidos do Novo Bolsa Família, e não a repasse administrativo municipal.

Mesmo assim, transferência registrada ≠ consumo observado ≠ valor retido no território.

## 7. Leitura integrada da renda e transferências residentes

O projeto dispõe agora de quatro referências monetárias de natureza distinta:

- **R$ 92.605.826,04/mês** — massa implícita do rendimento domiciliar no Censo 2022, calculada;
- **R$ 23.940.059,71** — remuneração nominal de dezembro informada na RAIS 2025;
- **R$ 24.535.168,54** — crédito de benefícios emitidos pelo INSS/SUIBE em julho de 2026;
- **R$ 1.513.564,00** — soma de `VALOR PARCELA` do Novo Bolsa Família em julho de 2026.

Essas grandezas **não devem ser somadas mecanicamente**. Períodos, universos e conceitos diferem, e pode haver sobreposição de pessoas entre fontes e programas.

O avanço analítico não é a produção de uma “renda total” artificial, mas a decomposição das diferentes fontes que sustentam a capacidade econômica residente.

## 8. Diagnóstico mercadológico atualizado

### Fatos sustentados

São Borja possui mercado residente próximo de 60 mil pessoas, base empresarial numericamente local, setores com dependência funcional externa elevada, concentração numérica da população do universo do Censo nas faixas de até 2 SM per capita, fluxo mensal de **R$ 24,535 milhões** em benefícios INSS/SUIBE e **R$ 1,514 milhão** em parcelas do Novo Bolsa Família na competência julho de 2026.

### Interpretação

A renda e as transferências não laborais têm escala material para a economia residente e precisam integrar a caracterização do consumidor. O Novo Bolsa Família acrescenta evidência direta de transferência monetária e elimina a necessidade de usar, indevidamente, o IGD/FMAS como proxy de benefício às famílias.

A coexistência de renda do trabalho, benefícios previdenciários/assistenciais e transferência do Novo Bolsa Família mostra que a estrutura da capacidade econômica residente é multifuente. Isso **não** é uma estimativa de renda total corrente nem uma afirmação sobre gasto local.

### O que ainda não pode ser concluído

Ainda não é possível afirmar:

- quantas famílias correspondem aos 2.199 registros do Novo Bolsa Família;
- quantas pessoas únicas correspondem aos 14.247 registros do INSS/SUIBE;
- qual parcela dos fluxos é renda disponível;
- quanto é consumido em São Borja e quanto sai do território;
- como os recursos se distribuem entre os quatro mercados setoriais;
- qual a propensão a consumir por fonte de renda ou espécie de benefício;
- qual a sobreposição individual entre Novo Bolsa Família, INSS/SUIBE, renda do trabalho e demais transferências;
- qual a renda total corrente dos residentes em 2026.

## 9. Implicações para os quatro cadernos setoriais

As camadas de renda e transferência devem ser usadas como **base de escala e segmentação**, não por multiplicadores arbitrários de consumo.

Hipóteses setoriais sobre bens essenciais, saúde/higiene, bens não essenciais e serviços/alimentação deverão ser testadas com dados de hábitos de compra, pesquisas primárias ou outras fontes comportamentais. A composição da renda, isoladamente, não demonstra destino do gasto.

## 10. Rastreabilidade — Novo Bolsa Família

Workflow: `novo-bolsa-familia-sao-borja-extract`.  
Run: `34284691474`.  
Job: `102257430159`.  
Artifact: `10079014259`.  
SHA-256 do artifact: `41a27542e9b94ce07606ea7cb15868d6aafc67c073f7c8d86e21b9bc7d44c15e`.  
SHA-256 do ZIP nacional: `f66e621bfdbb945cf324679e216d3d3b42d2029f39be7f646e046fd28b4c30d4`.  
SHA-256 do CSV agregado municipal: `fc4ab012979f5802567bd028f2b87ad2fbb208d5dec99fb02bc24323a9c5d07e`.

Drive:

- pasta bruta: ID `15loZ2NDpNcwIwI4hFTxjsNKjFzaxekhq`;
- pacote agregado sem PII: ID `1am7E0ILJCp26z9X8MjLu7sdSxqYRN1jn`;
- CSV agregado: ID `1cR1KfPWe_MMwGF9KHHrwNoGJYT5RcjUs`;
- nota metodológica nativa: ID `11LpVM7KSmgzZ7hk6Hl5eZix_FVAzPhMP9tRfXheaDNc`.

Caderno-Base v008:

- `Mercado_consumidor_base` atualizado;
- `Diagnostico_integrado` atualizado;
- nova aba `Novo_Bolsa_Familia_202607`, exclusivamente agregada e sem dados pessoais.

## 11. Próxima agenda

A primeira referência oficial municipal do Novo Bolsa Família está encerrada para julho de 2026. As prioridades passam a ser:

1. construir série mensal do Novo Bolsa Família com a mesma regra territorial e de privacidade;
2. mapear outras transferências monetárias diretamente recebidas por residentes/famílias, sempre separando benefício de repasse administrativo;
3. avaliar série mensal INSS/SUIBE;
4. somente depois estruturar metodologia explícita para renda disponível aproximada, capacidade de compra e retenção local;
5. conectar renda, benefícios e transferências aos quatro cadernos setoriais e à matriz de controle territorial;
6. preservar fiscalidade, VAF e IPM em trilha conceitual própria.
