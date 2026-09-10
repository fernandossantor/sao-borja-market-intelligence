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

## Checkpoint corrente

- `docs/caderno_base/checkpoint_20260909.md` — estado consolidado ao encerramento de 2026-09-09.
- Checkpoint histórico anterior: `docs/caderno_base/checkpoint_20260908.md`.

## Versão corrente

- Caderno: `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908` — Drive `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.
- Histórico imediato: v010 — Drive `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.
- Diagnóstico corrente: `docs/caderno_base/diagnostico_analitico_integrado_v010.md`.
- Oferta × demanda × controle: `docs/caderno_base/oferta_demanda_controle_bens_essenciais_v007.md`.
- Operadores pré-join: `docs/caderno_base/operadores_bens_essenciais_prejoin_rfb_v002.md`.
- Demanda: `docs/caderno_base/demanda_potencial_bens_essenciais_v005.md`.
- Mercado consumidor: `docs/caderno_base/mercado_consumidor_base_v006.md`.
- Matriz monetária: `docs/caderno_base/matriz_fluxos_renda_transferencias_v001.md`.

Documentos nativos no Drive:

- diagnóstico integrado v008 — `1WT02AzJXg-oGasuTOmtyV6XCppxXNdyBFBXFZuRa_Jw`;
- oferta, demanda e controle v007 — `1FjNvckIa49ULYyca3AMipugWFpzQtx2a0uLGlKZHdP4`;
- demanda de bens essenciais v005 — `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`;
- operadores pré-join RFB v002 — `1u8l0ll_TmR4PabMuNfAQvLlUFiyFcBjkLlV4G9BJyOg`.

A v011 preserva as abas anteriores e contém `Oferta_demanda_controle`, `Qualidade_oferta` e `Operadores_prejoin_RFB`.

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
- 52 reconciliadas com o POM.

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

## Matriz de operadores — pré-join RFB v002

Derivado: `matriz_operadores_bens_essenciais_prejoin_rfb_v002_20260909.xlsx` — Drive `12IKd7-zipN29iAYa16HNcoBT6PFa8k2S`.

- 54 linhas correntes;
- **52 CNPJs documentais prontos = 96,2963%**;
- 0 duplicidades documentais pendentes;
- 2 linhas ainda sem CNPJ documental suficientemente confiável;
- 52 `MATCH_POM` e 2 `ONLY_CURRENT`.

Pendências restantes: `Bedi Padaria e Confeitaria (Mercearia)` e `Sabor mineiro da Lu Delícias caseiras`.

`controle_local_externo` e `municipio_matriz` permanecem pendentes da RFB oficial. É proibido substituir o join oficial por heurística `/0001`, endereço, telefone ou narrativa documental.

## Join oficial dos 52 CNPJs — bloqueio atual

Workflow: `.github/workflows/bens-essenciais-operadores-rfb-join.yml`.

Run **34417653207**: **failure** no passo de download/scan dos arquivos oficiais da RFB.

Causa observada: timeout de conexão HTTPS com `dadosabertos.rfb.gov.br:443`; o runner não recebeu bytes após as tentativas configuradas. A matriz final e o artifact não foram produzidos.

Natureza do bloqueio: **infraestrutura/acesso à fonte externa**, não falha conceitual da regra territorial e não evidência de problema nos 52 CNPJs preparados.

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

1. testar novamente a disponibilidade do endpoint oficial da RFB;
2. verificar a existência de cópia canônica já preservada dos arquivos RFB 2026-08 antes de baixar novamente;
3. obter de forma íntegra `Municipios.zip` e `Estabelecimentos0..9.zip`;
4. executar o join exato dos **52 CNPJs**;
5. promover resultado ao Drive e sincronizar Caderno, diagnóstico, README e PR;
6. resolver separadamente os 2 operadores ainda sem CNPJ validado;
7. depois avançar para destino do gasto por formato, operador, canal e território — inclusive Argentina, outros municípios e comércio eletrônico.

## Rastreabilidade principal

- checkpoint 20260909: `docs/caderno_base/checkpoint_20260909.md`;
- POF raw: Drive `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- demanda v005: `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- Censo da Oferta v002: `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- proxy oferta/capacidade v007: `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- matriz pré-join v002: `12IKd7-zipN29iAYa16HNcoBT6PFa8k2S`;
- Caderno v011: `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`;
- run RFB com falha de conectividade: `34417653207`.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. O PR #41 permanece **aberto, draft e sem merge** até autorização explícita.