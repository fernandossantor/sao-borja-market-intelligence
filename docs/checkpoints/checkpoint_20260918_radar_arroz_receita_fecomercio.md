# Checkpoint — Receita Estadual, Radar, Fecomércio e piloto do arroz — 2026-09-18

## Estado de preservação

Todo o trabalho desta frente continua **exploratório**.

Nenhum caderno, planilha ou base canônica foi alterado nesta rodada.

Base técnica mais recente identificada no Drive e usada somente em leitura:
- `caderno_base_territorial_v028_analise_integrada_20260913`
- Drive ID: `17Sk5Hu_CQ-hKJYTNEfYSN4F97MiuZrfrU9o_VxEg0Rc`

Documento narrativo correspondente consultado em leitura:
- `Caderno-Base Territorial — São Borja — v028 — análise integrada territorial — 20260913`
- Drive ID: `1EdWubBnx7kUqTDdeXBafOf9cw_l9IT9gizORycVAMFI`

### PR #41

Estado reconfirmado em 18/09/2026:
- state: open
- draft: true
- merged: false
- head: `feature/cnpj-territorial-control-v1`
- head SHA: `6f3d94b620a1e9368a187eff343bf8572e45d1b5`

Regra: **não alterar, mesclar ou fechar o PR #41 sem autorização explícita**.

### Branch exploratória

`explore/receita-estadual-rs-market-intel-v1`

Último commit criado nesta sequência:
`94d07642fd07e6aa83da278b1815706f89180872`

## Artefatos de controle

Documento-mestre:
`1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`

Matriz exploratória:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Abas:
- Fontes
- PCA_seed
- BET_FO_seed
- Radar_matriz
- Radar_piloto_arroz
- Radar_arroz_cap_local

## BET

Etapa 1A concluída.

Etapa 1B aberta:
recuperar série recente diretamente para São Borja.

Os PDFs recentes, inclusive a edição 29, foram identificados, mas continuam apresentando falha de recuperação automática/cache.

Regra:
não preencher série municipal a partir de snippets, notícia secundária ou inferência.

Fallback regional:
`docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`

## Preços Dinâmicos / PCA-RE / ICA-RE

Etapa 2A concluída.

Metodologia:
- NFC-e;
- coleta diária;
- vendas formais a consumidor final;
- 80 produtos;
- 29 subgrupos;
- 12 grupos;
- NCM 8 dígitos;
- mineração de texto;
- Tukey;
- mediana;
- publicação diária e mensal.

Geografia pública:
28 COREDES + RS.

Regra:
São Borja usa COREDE Fronteira Oeste como referência regional, nunca como dado municipal.

Etapa 2B parcial:
`docs/data_sources/pca_re_validacao_seed_v001.csv`

PCA-RE-r / ICA-RE-r:
metodologia auditada pela NT CIET 04/2026; faixas de <2 SM a >25 SM; NFC-e + POF/IBGE; RS + 28 COREDES.

## Cesta Nutricional Familiar

Etapa 3A concluída.

Instituições:
Receita Estadual RS + PUCRS DataSocial + GPCA/PUCRS.

Permite composição familiar, hábito alimentar, faixa etária e COREDE.

Cruzamento com renda municipal será sempre indicador calculado pelo SBMI.

## Radar do Mercado

Etapa 4B concluída até o limite verificável.

Arquivo:
`docs/data_sources/radar_mercado_dimensoes_v001.csv`

Dimensões confirmadas:
- demanda estadual por produto/NCM;
- produção interna do RS;
- entradas de outras UFs;
- importações;
- market share;
- destino por UF/país;
- mercados consumidores;
- concorrentes;
- dependência externa.

Granularidade municipal:
há evidência histórica de mapas por município, mas ainda não está confirmado que todos os indicadores da versão 2026 aceitem município.

### NT CIET 05/2026 — correção

A anotação anterior de “nota não localizada” está superada.

A página oficial do Receita.doc lista:

**NOTA TÉCNICA CIET 05/2026 — RADAR DE MERCADO DA RECEITA ESTADUAL**

Data: 30/06/2026.

URL:
`https://receitadoc.sefaz.rs.gov.br/media/rhwdpvaz/nota_tecnica_radar_mercado_v1.pdf`

Confirmados:
- existência;
- título;
- data;
- URL.

Limitação:
o PDF ainda não foi recuperado integralmente por timeout/cache; detalhes internos só entram após leitura verificável.

## Piloto do arroz — Etapa 4C

Modelo:
`mercado estadual por NCM → capacidade territorial local → hipótese mercadológica`

NCMs:
- 10062010
- 10062020
- 10063011
- 10063019
- 10063021
- 10063029
- 10064000

CNAEs:
- 0111-3/01 — Cultivo de arroz
- 1061-9/01 — Beneficiamento de arroz
- 1061-9/02 — Fabricação de produtos do arroz

Arquivos:
- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`

## Capacidade local do arroz — Etapa 4C.1

### Produção primária — IRGA

Safra 2023/2024 — São Borja:
- 31.166 ha semeados;
- 2.014 ha perdidos;
- 29.152 ha colhidos;
- 8.129 kg/ha;
- 236.977 t produzidas.

Safra 2024/2025:
- 306.703,95 t;
- 8º maior produtor do RS;
- 4º da Fronteira Oeste.

Dado calculado:
`((306.703,95 / 236.977) - 1) × 100 = 29,42%`

Limitação:
não atribuir a variação isoladamente a área, produtividade, clima, preço, crédito ou decisões de plantio.

### Capacidade agroindustrial — v028

CNAE 10.61-9/01:
- 20 estabelecimentos ativos;
- 19 matrizes;
- 1 filial de raiz com matriz em São Borja;
- 953 vínculos formais;
- R$ 3.491.039,35 de massa de remuneração em dezembro/2025;
- 97,34% dos vínculos da divisão 10 no recorte;
- 98,69% da massa salarial de dezembro da divisão 10 no recorte.

Interpretação já consolidada:
encadeamento agroindustrial local material.

Limite:
destino de lucros, poupança, aplicações, patrimônio e reinvestimentos permanece não verificado.

### Validação histórica — IBGE/CEMPRE 2022

Grupo 10.6:
- 23 empresas/organizações;
- 994 pessoas ocupadas;
- 960 assalariadas;
- R$ 42,945 milhões em salários e outras remunerações.

Classe 10.61-9:
- 21 empresas/organizações;
- emprego/remuneração suprimidos como X.

Cálculo:
`21 / 23 × 100 = 91,30%`

Pode-se afirmar a participação dos estabelecimentos; não se pode transferir a mesma proporção a emprego ou salários.

### Mudança da pergunta analítica

Para arroz, a questão passa a ser:

> **como a capacidade produtiva e agroindustrial já instalada em São Borja se posiciona diante da demanda gaúcha, da produção interna do RS, das entradas de outras UFs, das importações, dos concorrentes e dos mercados consumidores?**

O foco passa de mera prospecção de entrada para posicionamento, expansão, concorrência, mercados e integração da cadeia existente.

Artefato:
`docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv`

Aba:
`Radar_arroz_cap_local`

## IRGA — fonte complementar formalizada

Arquivo:
`docs/data_sources/irga_arroz_sao_borja_auditoria_v001.md`

Função:
capacidade produtiva física municipal.

Arquitetura:
- IRGA/IBGE → produção física municipal;
- RAIS/RFB → estrutura agroindustrial e emprego local;
- Radar → demanda, origem da oferta, dependência externa, concorrência e mercados no RS.

Regra:
produção municipal ≠ demanda municipal.

## Observatório do Comércio — Fecomércio-RS / IFEP-RS

Fonte:
`https://observatorio.fecomercio-rs.org.br/page/home`

Rota:
`https://observatorio.fecomercio-rs.org.br/page/fonte-dos-dados`

Fontes confirmadas até aqui:
- Receita Federal;
- Ministério do Trabalho.

Não assumir que sejam as únicas.

Pendência:
transcrever a seção “Fonte dos dados” e montar matriz de proveniência por indicador.

## Outras fontes

BET Comércio Exterior:
`docs/data_sources/bet_comercio_exterior_rs_auditoria_v001.md`

Volume de Vendas da Indústria do RS:
`docs/data_sources/volume_vendas_industria_rs_auditoria_v001.md`

Uso:
contexto/benchmark estadual; não atribuir a São Borja.

## Arquivos principais da branch

- `docs/data_sources/receita_estadual_rs_auditoria_v001.md`
- `docs/data_sources/bet_rs_auditoria_v001.md`
- `docs/data_sources/precos_dinamicos_rs_auditoria_v001.md`
- `docs/data_sources/cesta_nutricional_rs_auditoria_v001.md`
- `docs/data_sources/radar_mercado_rs_auditoria_v001.md`
- `docs/data_sources/radar_mercado_dimensoes_v001.csv`
- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`
- `docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv`
- `docs/data_sources/irga_arroz_sao_borja_auditoria_v001.md`
- `docs/data_sources/observatorio_fecomercio_rs_auditoria_v001.md`
- `docs/data_sources/volume_vendas_industria_rs_auditoria_v001.md`
- `docs/data_sources/bet_comercio_exterior_rs_auditoria_v001.md`
- `docs/data_sources/matriz_fontes_exploratorias_receita_fecomercio_v001.csv`
- `docs/data_sources/pca_re_validacao_seed_v001.csv`
- `docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`

## Próxima sequência

1. Recuperar e ler integralmente a NT CIET 05/2026.
2. Para os sete NCMs do arroz, recuperar de forma verificável demanda RS, produção interna, entradas de OUF, importações, dependência externa, market share, mercados, concorrentes e eventual localização municipal.
3. Se o Power BI continuar inacessível, procurar fontes oficiais compatíveis, mantendo-as separadas do Radar.
4. Retomar BET municipal de São Borja.
5. Auditar “Fonte dos dados” do Observatório Fecomércio.
6. Somente então decidir eventual promoção aos cadernos.

## Regra de retomada

- trabalhar na branch exploratória;
- não alterar/mesclar PR #41;
- não modificar bases/cadernos canônicos;
- manter dados novos como exploratórios;
- separar observado, calculado, estimativa, interpretação e recomendação;
- registrar fonte, período, unidade, geografia e limitação;
- não converter dado estadual/COREDE em municipal;
- não confundir produção física com demanda, faturamento, VAB ou market share;
- promover somente após validação e autorização explícita.
