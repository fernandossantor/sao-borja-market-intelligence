# Checkpoint — 2026-09-08

## Estado geral

O projeto permanece na construção do Caderno-Base Territorial de São Borja, com foco agora em **análise integrada**, evitando repetir auditorias já encerradas. Dados, derivados, documentação e narrativa devem evoluir conjuntamente.

- Drive = dados/fontes e derivados compartilhados;
- GitHub/branch = código, documentação e versionamento;
- PR #41 permanece aberto, draft e **não deve ser mesclado sem autorização explícita**.

## Caderno-Base corrente

- `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908`
- Drive ID `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`
- versão anterior preservada: v010, ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`

A v011 preserva as abas anteriores e acrescenta:

- `Oferta_demanda_controle`;
- `Qualidade_oferta`;
- `Operadores_prejoin_RFB`.

## Documentação corrente no Drive

- diagnóstico integrado v008: `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`;
- nota oferta × demanda × controle v007: `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- checkpoint desta sessão: `1QJpDuq0s_Sfugtp1whEAUYw85qsCGJ_CB7cgcuU2ZCI`.

## Demanda de bens essenciais

Estimativa modelada principal:

- R$ 19.558.852,34/mês;
- R$ 234.706.228,14/ano.

Abrangência: alimentação comprada para consumo no domicílio por residentes.

Fonte/modelo: IBGE POF 2017-2018, Rio Grande do Sul, tabela 1.3.23.3; população oficial estimada 2025 = 61.311; fator de atualização 1,781742384675 do IPCA nacional do grupo Alimentação e bebidas até jun/2026.

Natureza: **ESTIMATIVA MODELADA**, não faturamento observado, market share, renda disponível ou mercado capturado.

## Oferta e capacidade

Censo da Oferta v002:

- 138 linhas brutas POM;
- 135 nomes únicos;
- 54 linhas correntes classificadas como bens essenciais;
- 52 reconciliadas cadastro corrente ↔ POM;
- 19 pendências resolvidas, 32 parciais e 48 abertas.

Esses números descrevem a estrutura documental da oferta; não constituem censo exaustivo de estabelecimentos ativos.

CEMPRE/SIDRA — intensidade de pessoal por empresa 47.11 / 47.12:

- 2022 ≈ 4,73x;
- 2023 ≈ 1,97x.

Interpretação: generalistas apresentam maior escala média nos dois anos observados. A magnitude é instável e empresa não equivale automaticamente a unidade local.

## Controle territorial — varejo amplo

RFB 2026-08, divisão CNAE 47:

- 1.720 estabelecimentos;
- 114 filiais de matriz externa;
- participação cadastral externa = **6,627907%**.

RAIS 2025 × RFB 2026-08:

- 2.893 vínculos;
- participação externa estimada no emprego = **37,460891%**;
- participação externa estimada na remuneração de dezembro = **38,163647%**.

Amplificação funcional:

- emprego / presença cadastral externa = **5,651994x**;
- remuneração / presença cadastral externa ≈ **5,76x**.

Esses indicadores se referem ao varejo amplo e não são market share, participação em vendas, remessa de lucros, retenção ou vazamento territorial.

## Matriz de operadores — pré-join RFB

Derivado:

- `matriz_operadores_bens_essenciais_prejoin_rfb_v001_20260908.xlsx`
- Drive ID `1fSZO0sEqeoGuWgNacZvjQGcN2pdPWYki`

Universo corrente: 54 registros de bens essenciais.

Situação documental:

- 47 registros com CNPJ documental pronto para join oficial com a RFB = **87,04%**;
- 2 CNPJs precisam revisão por duplicidade;
- 5 registros permanecem sem CNPJ validado;
- 52 registros `MATCH_POM`;
- 2 registros `ONLY_CURRENT`.

Dentro do recorte atual, Rede Vivo e Peruzzo possuem dois registros válidos com a mesma base de oito dígitos do CNPJ. Isso é apenas cálculo intrarrecorte; não informa total de lojas, participação ou controle territorial.

### Regra de classificação territorial

Matriz/filial, município da matriz e controle local/externo devem ser preenchidos exclusivamente pelos campos oficiais da RFB.

Não usar `/0001`, razão social, endereço, telefone ou narrativa como substitutos.

## Diagnóstico corrente

**Interpretação:** São Borja apresenta estrutura competitiva assimétrica nos bens essenciais: poucos operadores generalistas de maior escala coexistem com uma rede numerosa de proximidade/especializada. Paralelamente, no varejo amplo, estruturas externas têm peso funcional muito superior à presença cadastral.

Ainda não é possível repartir os R$ 234,7 milhões/ano entre operadores, formatos, empresas locais ou redes externas.

### Indicadores bloqueados

Não calcular ainda:

- market share por operador/formato;
- faturamento médio por simples divisão da demanda pelo número de lojas;
- saturação por contagem bruta;
- parcela da demanda capturada por redes externas aplicando diretamente percentuais da divisão 47;
- retenção/vazamento territorial apenas pela localização da matriz.

## Ponto exato para retomada

### Prioridade 1

Fazer o join exato dos **47 CNPJs documentalmente prontos** com a RFB oficial 2026-08 para preencher:

- situação cadastral;
- CNAE principal oficial;
- matriz/filial;
- município da matriz;
- controle local/externo.

### Prioridade 2

Resolver os 7 registros ainda não prontos:

- 2 duplicidades;
- 5 sem CNPJ validado.

### Prioridade 3

Atualizar no mesmo ciclo:

- matriz de operadores no Drive;
- Caderno-Base;
- documentação explicativa;
- GitHub/PR.

Somente depois: testar concentração por operadores, pressão competitiva e hipóteses de retenção territorial. Market share continuará exigindo vendas observadas ou proxy explicitamente validada.

## Guarda-corpos metodológicos

- separar observado, calculado, estimado, hipótese, interpretação e recomendação;
- não inventar números, fontes ou equivalências;
- não tratar correlação como causalidade;
- não somar Censo, RAIS, INSS e Novo Bolsa Família como parcelas mutuamente exclusivas;
- não equiparar VAF, VAB, IPM, valor adicionado relativo, receita própria ou transferências;
- preservar versões anteriores e rastreabilidade no Drive e GitHub.

## Pergunta-guia da próxima sessão

> Como a demanda residente, a estrutura de formatos e operadores e o controle territorial efetivo das unidades de bens essenciais se articulam para explicar a concorrência local sem fabricar market share ou retenção que os dados ainda não sustentam?
