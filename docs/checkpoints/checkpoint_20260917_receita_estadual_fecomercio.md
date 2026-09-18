# Checkpoint — Receita Estadual RS + Fecomércio — 2026-09-17

## Estado de preservação

O trabalho desta rodada permanece **inteiramente exploratório**.

### Projeto canônico

Nenhum caderno, planilha ou base consolidada do SBMI foi alterado.

### PR #41

Estado verificado em 17/09/2026:

- state: open
- draft: true
- merged: false
- head: feature/cnpj-territorial-control-v1
- head SHA: 6f3d94b620a1e9368a187eff343bf8572e45d1b5

Regra mantida: **não mesclar nem alterar o PR #41 sem autorização explícita**.

### Branch exploratória

`explore/receita-estadual-rs-market-intel-v1`

Último commit desta rodada:
`2c656b7bb69a77df208b36e93859d08a5470ab9a`

Toda a documentação e os seeds desta investigação estão isolados nessa branch.

## Drive — artefatos de controle

Documento-mestre:
`1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`

Matriz exploratória:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Abas atuais:
- Fontes
- PCA_seed
- BET_FO_seed
- Radar_matriz
- Radar_piloto_arroz

## Estado por fonte

### BET
- 1A concluída.
- 1B aberta: recuperar série municipal recente de São Borja.
- Não preencher valores municipais por snippets ou inferência.
- Fallback regional: `bet_fronteira_oeste_validacao_seed_v001.csv`.

### Preços Dinâmicos
- 2A concluída.
- NFC-e; coleta diária; 80 produtos; 29 subgrupos; 12 grupos; NCM 8 dígitos; Tukey; mediana.
- Publicação: 28 COREDES + RS.
- São Borja usa COREDE Fronteira Oeste como referência regional.
- 2B parcial: `pca_re_validacao_seed_v001.csv`.

### PCA-RE-r / ICA-RE-r
- Metodologia auditada pela NT CIET 04/2026.
- Faixas: <2; 2–3; 3–6; 6–10; 10–15; 15–25; >25 salários mínimos.
- Fonte: NFC-e + pesos POF/IBGE.
- Geografia: RS + 28 COREDES.
- Não confundir pesos POF com distribuição corrente de renda de São Borja.

### Cesta Nutricional Familiar
- 3A concluída.
- Receita Estadual + PUCRS DataSocial + GPCA/PUCRS.
- Perfis por composição familiar, hábito alimentar, idade e COREDE.
- Cruzamentos com renda municipal serão indicadores calculados pelo SBMI.

### Radar do Mercado
- 4B concluída até o limite verificável.
- Dimensões confirmadas: demanda por produto/NCM, produção RS, outras UFs, importações, market share, destino, consumidores, concorrentes e dependência externa.
- Power BI client-side: páginas e filtros atuais não recuperados integralmente.
- Município existe em evidência histórica, mas não assumir para todos os indicadores de 2026.
- Referência anterior a “NT CIET 05/2026” removida como fonte válida por não ter sido localizada oficialmente.

## Etapa 4C — piloto do arroz

Modelo:
`oportunidade estadual por NCM → capacidade territorial local → hipótese mercadológica`

CNAEs:
- 0111-3/01 — Cultivo de arroz
- 1061-9/01 — Beneficiamento de arroz
- 1061-9/02 — Fabricação de produtos do arroz

NCMs:
- 10062010
- 10062020
- 10063011
- 10063019
- 10063021
- 10063029
- 10064000

Arquivos:
- `radar_piloto_arroz_v001.md`
- `radar_piloto_arroz_ncm_v001.csv`

Campos quantitativos permanecem vazios por decisão metodológica.

## Observatório do Comércio — Fecomércio-RS / IFEP-RS

Fonte:
https://observatorio.fecomercio-rs.org.br/page/home

Rota:
https://observatorio.fecomercio-rs.org.br/page/fonte-dos-dados

Fontes confirmadas externamente:
- Receita Federal
- Ministério do Trabalho

Não assumir que sejam as únicas.

Granularidade municipal existe em pelo menos parte dos indicadores.

Regra:
- fonte primária permanece principal quando já canônica;
- indicadores próprios do IFEP exigem documentação de metodologia, periodicidade, geografia e limitações.

## Outras fontes inventariadas

BET Comércio Exterior:
- inventariado;
- granularidade municipal ainda não confirmada.

Volume de Vendas da Indústria do RS:
- edição 02 auditada;
- uso apenas como benchmark estadual.

## Arquivos principais na branch

- `docs/data_sources/receita_estadual_rs_auditoria_v001.md`
- `docs/data_sources/bet_rs_auditoria_v001.md`
- `docs/data_sources/precos_dinamicos_rs_auditoria_v001.md`
- `docs/data_sources/cesta_nutricional_rs_auditoria_v001.md`
- `docs/data_sources/radar_mercado_rs_auditoria_v001.md`
- `docs/data_sources/observatorio_fecomercio_rs_auditoria_v001.md`
- `docs/data_sources/volume_vendas_industria_rs_auditoria_v001.md`
- `docs/data_sources/bet_comercio_exterior_rs_auditoria_v001.md`
- `docs/data_sources/matriz_fontes_exploratorias_receita_fecomercio_v001.csv`
- `docs/data_sources/pca_re_validacao_seed_v001.csv`
- `docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`
- `docs/data_sources/radar_mercado_dimensoes_v001.csv`
- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`

## Próxima sequência

1. Radar/arroz: recuperar valores verificáveis para os NCMs piloto.
2. Capacidade local: cruzar com CNPJ/CNAE, emprego, VAF/IPM, produção oficial e operadores locais.
3. BET municipal: retomar extração recente de São Borja.
4. Fecomércio: transcrever “Fonte dos dados” e montar matriz de proveniência.
5. Só depois decidir eventual promoção para cadernos.

## Regra de retomada

- trabalhar primeiro na branch exploratória;
- não alterar PR #41;
- não modificar bases/cadernos canônicos;
- manter dados novos como exploratórios;
- registrar fonte, período, unidade, geografia e limitação;
- promover somente após validação e autorização explícita.
