# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa que altere dados, indicadores, método, interpretação ou diagnóstico deve, quando aplicável, sincronizar:

1. derivados auditáveis no Google Drive;
2. manifestos/metadados/validações;
3. narrativa em `docs/caderno_base/`;
4. versão corrente do Caderno-Base no Drive;
5. descrição do PR/branch.

Dado observado, cálculo, estimativa, hipótese, interpretação e recomendação permanecem separados. Versões anteriores são preservadas para auditoria histórica.

## Versão corrente

- Caderno: `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908` — Drive `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.
- Histórico imediato: v010 — Drive `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.
- Diagnóstico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v010.md`.
- Oferta × demanda × controle: `docs/caderno_base/oferta_demanda_controle_bens_essenciais_v007.md`.
- Demanda: `docs/caderno_base/demanda_potencial_bens_essenciais_v005.md`.
- Mercado consumidor: `docs/caderno_base/mercado_consumidor_base_v006.md`.
- Matriz monetária: `docs/caderno_base/matriz_fluxos_renda_transferencias_v001.md`.

Documentos nativos no Drive:

- diagnóstico integrado v008 — `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`;
- oferta, demanda e controle v007 — `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- demanda de bens essenciais v005 — `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`.

A v011 preserva as abas anteriores e acrescenta `Oferta_demanda_controle`, `Qualidade_oferta` e `Operadores_prejoin_RFB`.

## Estado analítico consolidado

### Estrutura empresarial e trabalho

- RFB 2026-08: 6.906 estabelecimentos empresariais; 284 de matriz externa; **4,1124%**.
- RAIS 2025 × RFB: 8.595 vínculos; emprego externo estimado **25,1606%**; remuneração de dezembro externa estimada **29,6897%**.

### Fiscalidade

- IPM definitivo: 2003–2026; 2026 = 0,533647; variação 2026/2025 = **+1,092483%**.
- VAF oficial: 1994–2025; 2025 = R$ 2.325.966.620,93; variação nominal 2025/2024 = **-19,9957%**.

### Mercado residente

- população estimada 2025: **61.311**;
- renda domiciliar per capita média Censo 2022: **R$ 1.568,58**; mediana **R$ 1.100,00**;
- 85,79220% do universo compatível sem rendimento ou até 2 SM per capita;
- INSS/SUIBE jul/2026: **R$ 24.535.168,54**;
- Novo Bolsa Família jan–jul/2026: fluxo corrente médio **R$ 1.502.070,14/mês**.

As camadas monetárias não são somadas diretamente.

## Bens essenciais — demanda, oferta e controle

### Demanda v005

IBGE POF RS 2017-2018 + população oficial 2025 + atualização de preços:

- benchmark mensal: **R$ 19.558.852,34**;
- benchmark anual: **R$ 234.706.228,14**.

Natureza: **estimativa modelada** de alimentação comprada para consumo no domicílio; não é faturamento observado ou mercado capturado.

### Qualidade da oferta

Censo da Oferta v002:

- 138 linhas brutas POM;
- 135 nomes únicos;
- 54 linhas correntes de bens essenciais;
- 52 reconciliadas com o POM;
- 19 pendências resolvidas, 32 parciais e 48 abertas.

O inventário sustenta leitura estrutural, não censo exato de lojas ativas.

### Capacidade por formato

CEMPRE/SIDRA: a razão de intensidade de pessoal 47.11-3 / 47.12-1 foi **≈4,73x em 2022** e **≈1,97x em 2023**. A direção de maior escala dos generalistas é sustentada, mas a magnitude é instável; empresa ≠ unidade local.

### Controle territorial — varejo amplo G47

- presença cadastral externa: **6,627907%**;
- emprego externo estimado: **37,460891%**;
- remuneração de dezembro externa estimada: **38,163647%**;
- amplificação funcional emprego/cadastro: **5,651994x**;
- amplificação remuneração/cadastro: **≈5,76x**.

Essas razões não são market share, faturamento, retenção ou vazamento.

## Matriz de operadores — pré-join RFB

Derivado: `matriz_operadores_bens_essenciais_prejoin_rfb_v001_20260908.xlsx` — Drive `1fSZO0sEqeoGuWgNacZvjQGcN2pdPWYki`.

- 54 linhas correntes;
- **47 CNPJs documentais OK = 87,03704%** de prontidão técnica para o join;
- 2 CNPJs em revisão por duplicidade;
- 5 linhas sem CNPJ;
- 52 MATCH_POM e 2 ONLY_CURRENT.

Duas bases CNPJ com status OK possuem mais de uma unidade mapeada no recorte: Rede Vivo e Peruzzo, duas unidades cada. O CNPJ base é somente identificador; isso não informa total da rede nem matriz/filial.

`controle_local_externo` e `municipio_matriz` permanecem **PENDENTE_RFB_OFICIAL**. É proibido substituir o join oficial por heurística `/0001`, endereço, telefone ou narrativa documental.

## Diagnóstico corrente

**Interpretação:** a estrutura competitiva dos bens essenciais é assimétrica: poucos operadores generalistas de maior escala coexistem com rede numerosa de proximidade/especializados; no varejo amplo, estruturas externas têm peso funcional muito superior à presença cadastral.

Ainda não é possível repartir os **R$ 234,7 milhões/ano** entre operadores locais e externos.

## Indicadores bloqueados

Não calcular ainda:

- market share por operador/formato;
- faturamento médio dividindo demanda por contagem de lojas;
- saturação por simples número de estabelecimentos;
- participação das redes externas na demanda alimentar aplicando diretamente o G47;
- retenção/vazamento com base apenas na localização da matriz.

## Próxima prioridade

Executar o join exato dos **47 CNPJs prontos** com os campos oficiais da RFB 2026-08 e resolver os **7 registros** sem CNPJ validado, completando:

`operador × formato × CNPJ/unidade × situação cadastral × CNAE × matriz/filial × município da matriz × controle local/externo × proxy de porte × confiança`.

Depois, avançar para destino do gasto por formato, operador, canal e território — inclusive Argentina, outros municípios e comércio eletrônico.

## Rastreabilidade principal

- POF raw: Drive `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- demanda v005: `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- Censo da Oferta v002: `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- proxy oferta/capacidade v007: `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- matriz pré-join: `1fSZO0sEqeoGuWgNacZvjQGcN2pdPWYki`;
- Caderno v011: `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`.