# INSS/SUIBE — benefícios emitidos a residentes de São Borja/RS — julho de 2026

## Objetivo

Incorporar ao Caderno-Base Territorial uma medida oficial de renda não laboral associada a benefícios emitidos pelo INSS/SUIBE para residentes de São Borja/RS, preservando a distinção entre registros emitidos, pessoas beneficiárias, espécies de benefício e valores monetários.

## Fonte, período, unidade e abrangência

- **Fonte:** INSS — Portal de Dados Abertos / SUIBE, conjunto `Benefícios Emitidos`, recurso `Benefícios Emitidos Julho 2026`.
- **Período de referência:** 2026-07.
- **Abrangência geográfica:** São Borja/RS, pelo campo oficial `municipio_residencia`.
- **Literal canônico do recorte:** `19181-RS-SAO BORJA`.
- **Campo monetário:** `credito`. O portal descreve o conjunto como contendo valor líquido; o CSV usa literalmente o cabeçalho `credito`.
- **Unidade monetária:** reais correntes da competência 2026-07.

## Auditoria de layout e integridade

O arquivo nacional compactado possui **999.063.765 bytes**, SHA-256 `a523d14ef4b7cc93c73dbcd2a248164bccad8e12a1adcd6589c53ab5b8d40e4f`. O membro CSV descompactado possui aproximadamente **8,41 GB**.

A fonte possui uma particularidade de layout confirmada por auditoria amostral: o cabeçalho é separado por vírgulas, enquanto os registros são separados por ponto e vírgula; `credito` usa vírgula decimal. A rotina municipal foi ajustada explicitamente a esse arranjo.

Foram observados literais contendo `SAO BORJA` associados a outras UFs no campo `municipio_residencia`. Esses registros são preservados como anomalia da fonte, mas **excluídos** do recorte São Borja/RS. Não são corrigidos nem reinterpretados.

## Resultados calculados a partir dos registros oficiais

- **14.247 registros** com `municipio_residencia = 19181-RS-SAO BORJA`;
- **14.247 registros com `credito` válido**;
- **R$ 24.535.168,54** de soma de `credito` em julho de 2026;
- **R$ 1.722,13 por registro emitido**, calculado por `24.535.168,54 / 14.247`.

A contagem é de **registros de benefícios/créditos emitidos**, não de pessoas beneficiárias únicas.

## Tabela por espécie

A aba `INSS_beneficios_202607` do Caderno-Base v008 preserva as 27 espécies literais da fonte, com número de registros, soma de `credito` e participações calculadas.

As maiores espécies em soma de crédito são:

| Espécie literal | Registros | Crédito (R$) | Participação no crédito |
|---|---:|---:|---:|
| APOSENTADORIA POR IDADE | 3.787 | 6.264.831,82 | 25,53409% |
| PENSAO POR MORTE PREVIDENCIARIA | 2.642 | 4.424.751,50 | 18,03432% |
| APOSENTADORIA POR TEMPO DE CONTRIBUICAO | 1.647 | 4.145.792,27 | 16,89735% |
| APOSENTADORIA POR INCAPACIDADE PERMANENTE PREVIDENCIARIA | 1.689 | 2.923.245,53 | 11,91451% |
| AMPARO SOCIAL AO IDOSO | 1.656 | 2.447.049,37 | 9,97364% |
| AMPARO SOCIAL PESSOA PORTADORA DEFICIENCIA | 1.729 | 2.330.068,27 | 9,49685% |

As duas espécies literalmente denominadas `AMPARO SOCIAL` somam:

- **3.385 registros**;
- **R$ 4.777.117,64**;
- **23,75939%** dos registros;
- **19,47049%** do crédito total.

Esse subtotal **não é relabelado** como total da assistência social ou dos benefícios não contributivos, porque a base contém categorias legadas e outras espécies cuja classificação jurídico-previdenciária exigiria regra específica.

## Limitações

1. Registro emitido não equivale a pessoa beneficiária única: a base usada não contém identificador que permita deduplicação individual.
2. O total de R$ 24,535 milhões é **mensal**. Não deve ser multiplicado automaticamente por 12.
3. Crédito de benefício não equivale a consumo efetivo, renda disponível ou valor necessariamente retido em São Borja.
4. O conjunto combina benefícios previdenciários, acidentários, assistenciais e categorias legadas; portanto, o total deve ser denominado **crédito de benefícios emitidos pelo INSS/SUIBE a residentes**, e não “massa previdenciária contributiva”.
5. A comparação com Censo 2022 e RAIS 2025 exige explicitar diferenças de período, universo e conceito; as massas não devem ser somadas diretamente.

## Implicação mercadológica

O dado acrescenta uma camada mensal de **renda não laboral registrada**. Ele complementa a renda domiciliar do Censo 2022 e a remuneração formal RAIS 2025, mas não substitui nenhuma delas. A presença relevante das duas espécies literalmente denominadas `AMPARO SOCIAL` também mostra que o fluxo do INSS/SUIBE mistura previdência e proteção social.

O uso permitido nesta etapa é caracterizar **escala monetária e composição por espécie**. Ainda não é permitido inferir propensão a consumir, alocação setorial do gasto, retenção local ou renda disponível.

## Reprodutibilidade e preservação

- workflow: `inss-benefits-residence-extract`;
- run validado: `34282566426`;
- artifact: `10078228209`;
- SHA-256 do artifact ZIP: `2f75523301768374ee1e9a908480ca850d93d6fe661407991ade50f9c800ba87`;
- SHA-256 do CSV municipal: `eb9e2536026d460892ea64cf672bf3cc26da1231bbf552f3ddd51d4c6945996c`.

Google Drive:

- pasta bruta: `_sao_borja/raw/social/inss_suibe_beneficios_emitidos/`, ID `1gIN6tmhHg-r7lPBlpCnGHNggZCj568vO`;
- pacote preservado: `inss_emitidos_sao_borja_rs_residencia_202607_v007_official_package.zip`, ID `11lAy2Dtlw20tzhOb8Y4ltkbpyZPDhbOs`;
- documento metodológico: `INSS_SUIBE_Sao_Borja_residencia_202607_v001`, ID `1bn5C6u1GII4eHrDwUnDRgTA27VR_YK4yL-QChWk_ncI`.

O arquivo nacional de aproximadamente 1 GB foi usado temporariamente na execução e não foi duplicado no Drive do projeto; o pacote preservado contém metadados oficiais, auditoria, diagnóstico, validação, recorte municipal completo e tabelas derivadas por tipo e espécie.
