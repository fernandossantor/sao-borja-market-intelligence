# CHECKPOINT DE TRANSIÇÃO — RECEITA ESTADUAL RS + FECOMÉRCIO + RADAR/ARROZ

**Data:** 18/09/2026  
**Projeto:** São Borja — Inteligência Mercadológica (SBMI)  
**Status:** exploratório — não canônico  
**Finalidade:** retomar em novo chat sem depender do histórico desta conversa.

---

## 1. REGRA DE PRESERVAÇÃO

Nada desta frente exploratória foi promovido automaticamente ao projeto canônico.

Regras vigentes:

- não modificar cadernos ou planilhas canônicas sem decisão explícita;
- não substituir séries já auditadas;
- manter novos dados como `exploratorio`;
- registrar fonte, período, unidade, geografia e limitações;
- não converter dado regional/estadual em dado municipal;
- não preencher lacunas por inferência;
- promover somente após validação metodológica.

### PR #41

Estado verificado em 18/09/2026:

- `state = open`
- `draft = true`
- `merged = false`
- head: `feature/cnpj-territorial-control-v1`
- head SHA: `6f3d94b620a1e9368a187eff343bf8572e45d1b5`

**Regra:** não alterar, fechar ou mesclar o PR #41 sem autorização explícita.

### Branch exploratória

`explore/receita-estadual-rs-market-intel-v1`

A investigação Receita Estadual/Fecomércio/Radar está isolada nessa branch.

---

## 2. ATENÇÃO À VERSÃO CANÔNICA MAIS RECENTE

Durante a retomada de 18/09/2026 foi identificado no Drive um Caderno-Base técnico mais recente do que a v016 mencionada no corpo do PR #41:

**caderno_base_territorial_v028_analise_integrada_20260913**

Drive ID:
`17Sk5Hu_CQ-hKJYTNEfYSN4F97MiuZrfrU9o_VxEg0Rc`

A v028 foi usada **somente para leitura** nesta auditoria.

Nenhuma célula ou documento canônico da v028 foi alterado.

Também existem artefatos v029 no Drive, mas a planilha técnica v028 é a base integrada usada nesta retomada.

---

## 3. ARTEFATOS DE CONTROLE NO DRIVE

### Documento-mestre da auditoria

**Auditoria Receita Estadual RS — integração exploratória SBMI — v001 — 20260917**

ID:
`1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`

Foi atualizado em 18/09/2026 com:
- capacidade local do arroz;
- IRGA;
- correção da NT CIET 05/2026;
- manutenção das pendências do Radar/BET.

### Matriz estruturada de fontes

**Matriz de fontes exploratórias — Receita Estadual + Fecomércio — v001 — 20260917**

ID:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Abas atuais:

1. `Fontes`
2. `PCA_seed`
3. `BET_FO_seed`
4. `Radar_matriz`
5. `Radar_piloto_arroz`
6. `Radar_arroz_cap_local`

A aba `Fontes` já inclui o IRGA como fonte complementar oficial.

### Checkpoint anterior

**Checkpoint — Receita Estadual + Fecomércio — SBMI — 20260917**

ID:
`1TvPM1JKyRON2JXU0UJt4drKRmbuVhJkxUaopDn6fqdo`

Recebeu ERRATA em 18/09/2026 sobre a NT CIET 05/2026.

---

## 4. ESTADO DAS FONTES

### 4.1 Boletim Econômico-Tributário — BET

Status:
- Etapa 1A concluída;
- Etapa 1B municipal permanece aberta.

Confirmado oficialmente:
- nível de atividade;
- demografia de estabelecimentos;
- setor/categoria;
- recortes por COREDE/municípios;
- arrecadação.

Periodicidade:
- mensal a partir da edição 09.

Pendência:
- obter série recente diretamente para São Borja de forma verificável.

Problema:
- PDFs recentes foram identificados, mas o servidor/ambiente retornou falhas de cache/recuperação.

Regra:
- não preencher São Borja por snippets, imprensa ou inferência.

Fallback regional:
`docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`

---

### 4.2 Preços Dinâmicos

Status:
- Etapa 2A concluída;
- Etapa 2B parcial.

Metodologia confirmada:
- NFC-e;
- coleta diária;
- caráter censitário das vendas formais acobertadas;
- 80 produtos;
- 29 subgrupos;
- 12 grupos;
- NCM 8 dígitos;
- mineração de texto;
- Tukey para outliers;
- preço mediano;
- publicação diária/mensal.

Geografia pública:
- 28 COREDES + RS.

Regra:
**São Borja → COREDE Fronteira Oeste como referência regional.**

Nunca rotular preço da Fronteira Oeste como preço de São Borja.

Seed:
`docs/data_sources/pca_re_validacao_seed_v001.csv`

---

### 4.3 PCA-RE-r / ICA-RE-r por faixa de renda

Metodologia auditada pela NT CIET 04/2026.

Faixas:
- < 2 SM;
- 2–3 SM;
- 3–6 SM;
- 6–10 SM;
- 10–15 SM;
- 15–25 SM;
- > 25 SM.

Fonte:
- NFC-e;
- ponderadores POF/IBGE — Tabela 6972.

Geografia:
- RS + 28 COREDES.

Uso:
- pressão da inflação alimentar por segmento de renda.

Limitação:
- pesos POF não equivalem à distribuição atual de renda de São Borja.

---

### 4.4 Cesta Nutricional Familiar

Status:
- Etapa 3A concluída.

Parceria:
- Receita Estadual RS;
- PUCRS DataSocial;
- GPCA/PUCRS.

Permite:
- composição familiar;
- hábito alimentar;
- idade;
- COREDE.

Regra:
qualquer cruzamento com renda municipal será **dado calculado pelo SBMI**, não observação municipal.

---

### 4.5 Radar do Mercado

Status:
- 4B concluída até o limite verificável;
- 4C piloto do arroz em andamento;
- 4C.1 capacidade local auditada.

Dimensões confirmadas institucionalmente:
- demanda por produto/NCM;
- produção interna RS;
- entradas de outras UFs;
- importações;
- market share;
- destino por UF/país;
- mercados consumidores;
- concorrentes;
- dependência externa.

Limitação:
o Power BI carrega conteúdo client-side; valores e filtros atuais não foram recuperados de forma estruturada/confiável.

Há evidência histórica de visualizações por município, mas isso não autoriza assumir município em todas as páginas de 2026.

---

## 5. CORREÇÃO IMPORTANTE — NT CIET 05/2026

A anotação anterior de que a NT CIET 05/2026 não havia sido localizada estava incorreta.

A página oficial do Receita.doc lista:

**NOTA TÉCNICA CIET 05/2026 — RADAR DE MERCADO DA RECEITA ESTADUAL**

Publicação:
**30/06/2026**

URL oficial:
https://receitadoc.sefaz.rs.gov.br/media/rhwdpvaz/nota_tecnica_radar_mercado_v1.pdf

Situação:
- existência: confirmada;
- título: confirmado;
- data: confirmada;
- URL: confirmado;
- conteúdo integral: ainda não recuperado por timeout/cache.

Regra:
não atribuir metodologia específica à NT 05/2026 antes de leitura verificável do PDF.

Documentação corrigida:
- `docs/data_sources/radar_mercado_rs_auditoria_v001.md`
- checkpoint 17/09;
- documento-mestre no Drive.

---

## 6. PILOTO DO RADAR — CADEIA DO ARROZ

### Objetivo analítico

Modelo:

`oportunidade/posição estadual por NCM → capacidade territorial local → hipótese mercadológica`

### NCMs piloto

- `10062010`
- `10062020`
- `10063011`
- `10063019`
- `10063021`
- `10063029`
- `10064000`

CNAEs relacionados:

- `0111-3/01` — Cultivo de arroz;
- `1061-9/01` — Beneficiamento de arroz;
- `1061-9/02` — Fabricação de produtos do arroz.

Arquivos:

- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`
- `docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv`

---

## 7. CAPACIDADE LOCAL DO ARROZ — ACHADO CENTRAL

A retomada de 18/09/2026 demonstrou que o arroz não é apenas uma atividade primária em São Borja: há **elo agroindustrial local materialmente documentado**.

### 7.1 Produção primária — IRGA

#### Safra 2023/2024 — São Borja

- área semeada: **31.166 ha**
- área perdida: **2.014 ha**
- área colhida: **29.152 ha**
- produtividade: **8.129 kg/ha**
- produção: **236.977 t**

Fonte:
IRGA — Produtividades Municipais Safra 2023/24.

#### Safra 2024/2025

- produção: **306.703,95 t**
- ranking RS: **8º**
- ranking Fronteira Oeste: **4º**, atrás de Uruguaiana, Itaqui e Alegrete.

Fonte:
IRGA/SEAPI — publicação de 13/06/2025.

### Cálculo SBMI

Variação entre as duas safras:

`((306.703,95 / 236.977) - 1) × 100 = 29,42%`

Natureza:
**DADO CALCULADO**.

Limite:
não atribuir causalidade; não representa automaticamente receita, VAB ou market share.

---

## 8. BENEFICIAMENTO DE ARROZ — BASE CANÔNICA v028

CNAE:
**10.61-9/01 — Beneficiamento de arroz**

Camada:
RAIS 2025 × RFB, consolidada no Caderno-Base v028.

Resultados:

- **20 estabelecimentos ativos**
- **19 matrizes**
- **1 filial de raiz com matriz em São Borja**
- **953 vínculos formais**
- **R$ 3.491.039,35** de massa de remuneração em dezembro/2025
- **97,34%** dos vínculos da divisão 10 no recorte
- **98,69%** da massa salarial de dezembro da divisão 10 no recorte

Comparação local — divisão 01:
- 192 vínculos;
- R$ 593.208,92 de massa de remuneração de dezembro.

Interpretação já existente na v028:
**encadeamento agroindustrial local material**.

Limite:
não se conhece, pela base atual, o destino de lucros, aplicações, poupança, patrimônio ou reinvestimentos.

---

## 9. VALIDAÇÃO HISTÓRICA — IBGE/CEMPRE 2022

Tabela 9418 — São Borja.

Grupo 10.6:
- 23 empresas/organizações;
- 994 pessoas ocupadas;
- 960 assalariadas;
- R$ 42,945 milhões em salários e remunerações no ano.

Classe 10.61-9:
- 21 empresas/organizações;
- pessoal e remuneração suprimidos como `X`.

Cálculo:

`21 / 23 × 100 = 91,30%`

Interpretação permitida:
91,30% dos estabelecimentos do grupo 10.6 pertenciam à classe 10.61-9 em 2022.

Interpretação NÃO permitida:
atribuir 91,30% do emprego ou dos salários do grupo ao arroz, pois essas variáveis estão suprimidas na classe.

---

## 10. IRGA FORMALIZADO COMO FONTE

Novo arquivo:

`docs/data_sources/irga_arroz_sao_borja_auditoria_v001.md`

Função da fonte:
**capacidade produtiva física municipal**.

Regra de integração:

- IRGA/IBGE → capacidade física;
- RAIS/RFB → capacidade agroindustrial e emprego;
- Radar → demanda, oferta estadual, concorrência, dependência externa e mercados.

Não confundir:

`produção municipal ≠ demanda municipal`

---

## 11. MUDANÇA DA PERGUNTA ANALÍTICA DO PILOTO

Antes:

> Existe uma oportunidade produtiva de arroz que poderia ser instalada em São Borja?

Depois da auditoria local:

> **Como a cadeia produtiva e agroindustrial já instalada em São Borja se posiciona diante da demanda gaúcha, da produção interna do RS, das entradas de outras UFs, das importações, dos concorrentes e dos mercados consumidores?**

Portanto, para arroz o foco passa de **entrada/implantação** para:

- posição competitiva;
- expansão;
- mercados;
- encadeamentos;
- dependência externa estadual;
- concorrência;
- destinos;
- eventual espaço para maior captura de valor local.

---

## 12. O QUE O RADAR AINDA NÃO RESPONDEU NO PILOTO

Campos quantitativos continuam vazios por decisão metodológica:

- demanda RS por NCM;
- produção interna RS por NCM;
- entradas de outras UFs;
- importações;
- dependência externa;
- market share;
- mercados consumidores;
- concorrentes;
- participação de São Borja na oferta estadual.

Não preencher por aproximação.

---

## 13. OBSERVATÓRIO DO COMÉRCIO — FECOMÉRCIO-RS / IFEP-RS

Fonte:
https://observatorio.fecomercio-rs.org.br/page/home

Rota de origem dos dados:
https://observatorio.fecomercio-rs.org.br/page/fonte-dos-dados

Fontes confirmadas externamente:
- Receita Federal;
- Ministério do Trabalho.

Não assumir que sejam as únicas.

Granularidade:
há evidência de pelo menos parte dos indicadores em nível municipal.

Regra:
- se apenas reorganizar fonte primária já canônica, manter a primária como referência;
- indicador próprio IFEP exige definição, metodologia, periodicidade, geografia e limitações.

Arquivo:
`docs/data_sources/observatorio_fecomercio_rs_auditoria_v001.md`

Pendência:
transcrever integralmente a área “Fonte dos dados” quando tecnicamente possível.

---

## 14. OUTRAS FONTES INVENTARIADAS

### BET Comércio Exterior

Arquivo:
`docs/data_sources/bet_comercio_exterior_rs_auditoria_v001.md`

Status:
inventariado; granularidade municipal não confirmada.

### Volume de Vendas da Indústria do RS

Arquivo:
`docs/data_sources/volume_vendas_industria_rs_auditoria_v001.md`

Status:
edição 02 auditada.

Uso:
benchmark estadual, nunca desempenho municipal.

---

## 15. ARQUIVOS PRINCIPAIS DA BRANCH EXPLORATÓRIA

- `docs/data_sources/receita_estadual_rs_auditoria_v001.md`
- `docs/data_sources/bet_rs_auditoria_v001.md`
- `docs/data_sources/precos_dinamicos_rs_auditoria_v001.md`
- `docs/data_sources/cesta_nutricional_rs_auditoria_v001.md`
- `docs/data_sources/radar_mercado_rs_auditoria_v001.md`
- `docs/data_sources/observatorio_fecomercio_rs_auditoria_v001.md`
- `docs/data_sources/volume_vendas_industria_rs_auditoria_v001.md`
- `docs/data_sources/bet_comercio_exterior_rs_auditoria_v001.md`
- `docs/data_sources/irga_arroz_sao_borja_auditoria_v001.md`
- `docs/data_sources/matriz_fontes_exploratorias_receita_fecomercio_v001.csv`
- `docs/data_sources/pca_re_validacao_seed_v001.csv`
- `docs/data_sources/bet_fronteira_oeste_validacao_seed_v001.csv`
- `docs/data_sources/radar_mercado_dimensoes_v001.csv`
- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`
- `docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv`

Commits recentes relevantes:
- `44a85f8...` — cruza piloto do arroz com capacidade local;
- `88a34b2...` — capacidade local confirmada na auditoria do Radar;
- `dc81563...` — documenta IRGA;
- `539a312...` — adiciona IRGA à matriz;
- `a2c9d45...` — corrige localização da NT CIET 05/2026;
- `91fb487...` — errata no checkpoint anterior;
- `94d0764...` — separa natureza do dado e status canônico no CSV do piloto.

---

## 16. PRÓXIMA ORDEM DE TRABALHO

### PRIORIDADE 1 — NT CIET 05/2026

Tentar recuperar e ler integralmente a Nota Técnica CIET 05/2026.

Objetivo:
documentar com precisão:
- universo fiscal;
- conceitos de demanda;
- conceitos de produção interna;
- entradas de outras UFs;
- importações;
- market share;
- granularidade territorial;
- periodicidade;
- filtros;
- limitações.

### PRIORIDADE 2 — PILOTO DO ARROZ / CAMADA ESTADUAL

Para os sete NCMs selecionados, tentar obter valores verificáveis de:

- demanda RS;
- produção RS;
- outras UFs;
- importações;
- dependência externa;
- concorrentes;
- mercados consumidores;
- destino da produção;
- localização municipal quando disponível.

Se o Power BI continuar inacessível, usar outra fonte oficial compatível, **mas registrar claramente que não é dado do Radar**.

### PRIORIDADE 3 — BET MUNICIPAL

Retomar extração recente de São Borja.

Não usar fonte secundária para preencher lacuna municipal.

### PRIORIDADE 4 — FECOMÉRCIO

Transcrever “Fonte dos dados” e montar:

`indicador → fonte original → produtor → periodicidade → menor geografia → unidade → transformação IFEP → uso SBMI`

### PRIORIDADE 5 — DECISÃO DE PROMOÇÃO

Somente quando as auditorias estiverem suficientemente completas:
- decidir o que vai ao Caderno-Base;
- o que vai aos cadernos setoriais;
- o que fica apenas como benchmark/contexto;
- criar documentação de promoção.

---

## 17. PROMPT CURTO PARA ABRIR O NOVO CHAT

Copiar a mensagem abaixo no novo chat:

> **Continuar o projeto São Borja — Inteligência Mercadológica a partir do checkpoint de 18/09/2026 — Receita Estadual + Fecomércio + Radar/Arroz.**
>
> O trabalho está isolado na branch `explore/receita-estadual-rs-market-intel-v1`. O PR #41 deve permanecer aberto, draft e sem merge. Não alterar bases/cadernos canônicos sem autorização.
>
> O Caderno-Base técnico usado apenas para leitura é a v028, Drive ID `17Sk5Hu_CQ-hKJYTNEfYSN4F97MiuZrfrU9o_VxEg0Rc`.
>
> Documento-mestre da auditoria: `1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`.
>
> Matriz exploratória: `1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`.
>
> No piloto do arroz, a capacidade local já está auditada: IRGA + Caderno-Base v028/RAIS-RFB + CEMPRE. A prioridade agora é recuperar e auditar integralmente a **NT CIET 05/2026 — Radar de Mercado**, e depois preencher, apenas com dados verificáveis, a camada estadual dos NCMs do arroz (demanda RS, produção RS, outras UFs, importações, dependência, concorrentes e mercados). Em seguida, retomar BET municipal e Fecomércio.
>
> Ler o checkpoint novo antes de executar qualquer alteração e manter toda nova evidência como exploratória até decisão explícita de promoção.

