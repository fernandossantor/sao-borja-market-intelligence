# Caderno-Base Territorial — diagnóstico analítico integrado v010

Atualização: 2026-09-08. Caderno correspondente no Drive: `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908`.

## Síntese desta versão

A v011 integra a **ordem de grandeza da demanda residente de alimentação no domicílio**, a **estrutura documental da oferta**, uma **proxy de capacidade competitiva por formato**, o **controle territorial agregado do varejo** e a preparação do universo de operadores para join oficial com a RFB.

Conclusões metodológicas:

1. já é possível caracterizar uma estrutura competitiva assimétrica;
2. 47 das 54 linhas correntes já possuem CNPJ documental utilizável no próximo join;
3. ainda **não** é possível calcular market share, saturação ou retenção territorial por operador.

## 1. Demanda residente — núcleo alimentar

**Estimativa modelada:** R$ 234.706.228,14/ano e R$ 19.558.852,34/mês.

Base: POF RS 2017-2018, tabela 1.3.23.3; gasto no domicílio R$ 487,00/família/mês; tamanho familiar 2,72; população oficial estimada de São Borja 2025 = 61.311; atualização pelo IPCA nacional do grupo Alimentação e bebidas até jun/2026.

`61.311 × (487 / 2,72) × 1,781742384675 × 12`.

Natureza: **estimativa modelada**, não faturamento observado ou mercado capturado.

## 2. Oferta — qualidade e cobertura documental

Censo da Oferta v002:

- 138 linhas brutas no inventário POM;
- 135 nomes únicos;
- 54 linhas correntes classificadas como bens essenciais;
- 52 reconciliadas entre cadastro corrente e POM;
- 19 pendências resolvidas, 32 parciais e 48 abertas.

**Interpretação:** os dados permitem leitura estrutural de formatos e operadores, mas não um denominador censitário exato de lojas ativas.

## 3. Capacidade competitiva

CEMPRE/SIDRA sustenta maior intensidade de pessoal por empresa no grupo 47.11-3 — hipermercados e supermercados — do que em 47.12-1 — minimercados, mercearias e armazéns:

- 2022: razão ≈ 4,73x;
- 2023: razão ≈ 1,97x.

A direção é consistente, mas a magnitude varia fortemente. Empresa e unidade local não são universos equivalentes, portanto pessoal/empresa não é pessoal/loja.

## 4. Controle territorial — varejo amplo

RFB 2026-08, divisão CNAE 47:

- 1.720 estabelecimentos;
- 114 filiais de matriz externa;
- participação cadastral externa: **6,627907%**.

RAIS 2025 × RFB 2026-08:

- 2.893 vínculos;
- 1.083,743584 vínculos externos estimados;
- participação externa estimada no emprego: **37,460891%**;
- remuneração de dezembro: R$ 6.782.037,30;
- remuneração externa estimada: R$ 2.588.273,00;
- participação externa estimada na remuneração: **38,163647%**.

Amplificação funcional calculada:

- emprego / presença cadastral: **5,651994x**;
- remuneração / presença cadastral: **≈5,76x**.

Esses indicadores se referem ao **varejo amplo**, não especificamente ao subconjunto alimentar, e não medem participação em vendas.

## 5. Matriz de operadores — pré-join RFB

Foi criado o derivado `matriz_operadores_bens_essenciais_prejoin_rfb_v001_20260908.xlsx` para as 54 linhas correntes.

**Calculado:**

- CNPJ documental OK: **47/54 = 87,03704%**;
- CNPJ em revisão por duplicidade: **2**;
- sem CNPJ: **5**;
- MATCH_POM: **52**;
- ONLY_CURRENT: **2**.

O CNPJ base é usado somente como identificador de agrupamento. Duas bases com status OK possuem mais de uma unidade mapeada no recorte: Rede Vivo e Peruzzo, com duas unidades cada. Isso não informa o total de lojas dessas redes nem determina matriz/filial.

**Controle metodológico:** as colunas `controle_local_externo` e `municipio_matriz` permanecem `PENDENTE_RFB_OFICIAL`. Não é usada heurística `/0001`, endereço, telefone, razão social ou narrativa documental para classificar controle territorial.

**Interpretação:** aproximadamente 87% da base corrente está tecnicamente pronta para o join exato com a RFB 2026-08. Essa taxa é de prontidão operacional, não cobertura do mercado.

## 6. Diagnóstico

**Fatos:**

- há um benchmark modelado relevante de demanda alimentar residente, de aproximadamente R$ 234,7 milhões/ano;
- a oferta documentada combina operadores generalistas de maior escala, mercados/minimercados e especializados;
- a base de oferta ainda contém lacunas de cobertura/status e não é censo completo;
- no varejo amplo, estruturas externas têm peso laboral e remuneratório muito superior ao seu peso cadastral;
- 47 das 54 linhas correntes já dispõem de CNPJ documental apto ao join oficial.

**Interpretação:** São Borja apresenta uma estrutura competitiva **assimétrica**: poucos nós generalistas de maior capacidade coexistem com uma rede numerosa de proximidade/especializada. Redes externas são funcionalmente relevantes no varejo, mas os dados ainda não demonstram qual parcela da demanda alimentar é capturada por elas.

## 7. O que não pode ser concluído

Não há base para afirmar:

- market share de operadores ou formatos;
- faturamento médio por estabelecimento;
- saturação do mercado pela simples contagem de lojas;
- parcela dos R$ 234,7 milhões capturada por empresas locais ou externas;
- retenção ou vazamento territorial;
- efeito causal do controle externo sobre salários, preços ou circulação monetária.

## 8. Próxima prioridade analítica

Executar o join exato dos **47 CNPJs prontos** com a RFB 2026-08 e resolver os **7 registros** ainda sem CNPJ validado, completando:

`operador × formato × CNPJ/unidade × situação cadastral × CNAE × matriz/filial × município da matriz × controle local/externo × proxy de porte × confiança`.

A classificação local/externa deve usar os campos oficiais da RFB. Essa matriz é o passo necessário para sair do agregado da divisão 47 e chegar aos operadores efetivamente relevantes para bens essenciais.

Depois dela, a segunda lacuna central será comportamento/destino do gasto: compras por formato, operador, canal e território, incluindo outros municípios, Argentina e comércio eletrônico.

## 9. Continuidade das demais dimensões

Permanecem canônicos e conceitualmente separados:

- controle empresarial RFB 2026-08;
- emprego/remuneração RAIS 2025 × RFB;
- IPM definitivo 2003–2026;
- VAF oficial 1994–2025;
- renda domiciliar Censo 2022;
- INSS/SUIBE jul/2026;
- Novo Bolsa Família jan–jul/2026;
- regra de não soma das diferentes camadas monetárias.

## 10. Rastreabilidade

- Caderno v011: Drive `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`;
- diagnóstico nativo v008: Drive `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`;
- nota oferta-demanda-controle: Drive `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- proxy oferta/capacidade v007: Drive `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- matriz pré-join RFB: Drive `1fSZO0sEqeoGuWgNacZvjQGcN2pdPWYki`;
- Censo da Oferta v002: Drive `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- demanda v005: Drive `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`.
