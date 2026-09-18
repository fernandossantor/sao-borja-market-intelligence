# Radar do Mercado — piloto Arroz / São Borja

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Criar o primeiro piloto controlado de cruzamento entre:

`oportunidade estadual por NCM → cadeia produtiva local → capacidade territorial → hipótese mercadológica`

sem converter demanda estadual em demanda municipal.

## Justificativa territorial

O Caderno Setorial de Bens Essenciais registra, com base em documentação municipal/Emater já incorporada ao projeto, forte presença histórica de **arroz** na base agropecuária de São Borja.

Essa evidência é suficiente para selecionar a cadeia como **piloto de auditoria**, mas não prova, por si só:
- capacidade industrial corrente;
- volume atual de beneficiamento;
- participação de São Borja na oferta estadual;
- viabilidade de expansão.

Esses pontos deverão ser verificados em bases canônicas do SBMI e, quando possível, no próprio Radar.

## Correspondência CNAE — fonte oficial CONCLA/IBGE

### Elo primário

**0111-3/01 — Cultivo de arroz**

A busca oficial da CONCLA associa a subclasse ao cultivo de arroz e ao beneficiamento quando atividade complementar ao cultivo.

### Elo industrial principal

**1061-9/01 — Beneficiamento de arroz**

A CONCLA/IBGE informa que compreende:
- arroz descascado;
- moído;
- branqueado;
- polido;
- parboilizado;
- convertido.

### Elo industrial derivado

**1061-9/02 — Fabricação de produtos do arroz**

Compreende, entre outros:
- farinha de arroz;
- flocos;
- outros produtos de arroz.

## Cesta piloto de NCM

Fonte de classificação: Sumário Executivo de Arroz do Ministério da Agricultura e Pecuária, referência 2026, e tabela NCM vigente/CLASSIF da Receita Federal.

### Arroz descascado

- `10062010` — arroz descascado (cargo/castanho), parboilizado;
- `10062020` — arroz descascado (cargo/castanho), não parboilizado.

### Arroz semibranqueado ou branqueado

- `10063011` — parboilizado, polido ou brunido;
- `10063019` — outros, parboilizados;
- `10063021` — não parboilizado, polido ou brunido;
- `10063029` — outros, não parboilizados.

### Subproduto

- `10064000` — arroz quebrado.

## Variáveis a buscar no Radar para cada NCM

1. demanda financeira no RS;
2. participação da produção interna do RS;
3. participação/valor de entradas de outras UFs;
4. participação/valor de importações;
5. classificação de dependência externa, se disponível;
6. variação temporal, se o painel permitir;
7. localização municipal da produção, se a versão atual mantiver esse visual;
8. principais mercados consumidores/destinos, quando disponível;
9. principais concorrentes, quando disponível.

## Variáveis locais a cruzar no SBMI

Para São Borja, usar apenas bases já auditadas ou que venham a ser auditadas:

- CNPJ/CNAE local;
- emprego formal;
- VAF/IPM, quando compatível;
- produção agropecuária oficial;
- localização de estabelecimentos industriais;
- evidência documental de operadores da cadeia.

## Estrutura analítica

Para cada NCM:

`demanda_RS → oferta_RS → OUF → importação → dependência → capacidade_local → hipótese`

Exemplo de interpretação permitida:

> “O produto X apresenta dependência externa relevante no mercado gaúcho. São Borja possui evidência de atividade produtiva relacionada à cadeia do arroz. Isso justifica investigar capacidade, escala, logística e acesso ao mercado estadual.”

Interpretação não permitida sem dado adicional:

> “São Borja possui mercado não atendido de R$ X.”

## Limitações

- a demanda do Radar é estadual;
- CNAE e NCM descrevem dimensões diferentes;
- presença de CNAE não mede capacidade instalada;
- produção agrícola não implica beneficiamento industrial local;
- dependência externa estadual não garante vantagem competitiva em São Borja;
- custos logísticos, escala, produtividade e contratos não estão automaticamente resolvidos pelo Radar.

## Próxima etapa

Preencher a matriz piloto com os valores do Radar quando a leitura confiável do Power BI for possível ou quando os mesmos indicadores aparecerem em documentação pública verificável.

Até lá, a tabela permanece como **esqueleto auditável**, sem preenchimento numérico especulativo.


## Etapa 4C.1 — capacidade local auditada

A retomada em 18/09/2026 identificou que o Caderno-Base técnico mais recente no Drive é a **v028 — análise integrada**, posterior à v016 registrada no corpo do PR #41. A v028 foi usada **somente em leitura** nesta auditoria; não foi modificada.

### Produção primária — fonte oficial IRGA

Safra 2023/2024 — São Borja:
- área semeada: **31.166 ha**;
- área perdida: **2.014 ha**;
- área colhida: **29.152 ha**;
- produtividade: **8.129 kg/ha**;
- produção: **236.977 t**.

Fonte oficial:
IRGA — Produtividades Municipais Safra 2023/24.

Safra 2024/2025:
- produção de São Borja: **306.703,95 t**;
- posição no RS: **8º maior produtor**;
- posição na Fronteira Oeste: **4º**, atrás de Uruguaiana, Itaqui e Alegrete.

Fonte:
IRGA/SEAPI, notícia de encerramento da colheita publicada em 13/06/2025.

### Cálculo SBMI

Variação da produção entre as duas safras:

`((306.703,95 / 236.977) - 1) × 100 = 29,42%`

**Natureza:** dado calculado.

A variação mede mudança de volume produzido entre duas safras; não demonstra causa nem tendência estrutural.

### Agroindústria local — base canônica v028

O Caderno-Base Territorial v028 registra para **CNAE 10.61-9/01 — Beneficiamento de arroz**, com base na camada RAIS 2025 × RFB:

- **20 estabelecimentos ativos**;
- **19 matrizes**;
- **1 filial pertencente a raiz com matriz em São Borja**;
- portanto, no recorte cadastral, todos os 20 estabelecimentos pertencem a raízes com matriz local;
- **953 vínculos formais**;
- **R$ 3.491.039,35** de massa de remuneração em dezembro/2025;
- **97,34%** dos vínculos da divisão 10 no recorte utilizado;
- **98,69%** da massa salarial de dezembro da divisão 10 no recorte utilizado.

O mesmo caderno compara com a divisão 01 — agricultura, pecuária e serviços relacionados:
- **192 vínculos**;
- **R$ 593.208,92** de massa de remuneração de dezembro.

A v028 interpreta o beneficiamento de arroz como um encadeamento agroindustrial local material, mas mantém como **não verificado** o destino de lucros, poupança, aplicações, imóveis e reinvestimentos.

### Evidência histórica independente — IBGE/CEMPRE 2022

Tabela 9418 — São Borja:

Grupo **10.6 — Moagem, fabricação de produtos amiláceos e de alimentos para animais**:
- 23 empresas/organizações;
- 994 pessoas ocupadas;
- 960 assalariadas;
- R$ 42,945 milhões em salários e outras remunerações no ano.

Classe **10.61-9 — Beneficiamento de arroz e fabricação de produtos do arroz**:
- 21 empresas/organizações;
- pessoal ocupado, assalariados e remunerações: **suprimidos (X)** pelo IBGE.

Cálculo estrutural permitido:
`21 / 23 × 100 = 91,30%`

Assim, 91,30% dos estabelecimentos do grupo 10.6 pertenciam à classe 10.61-9 em 2022.

**Não é permitido inferir que 91,30% do emprego ou da remuneração do grupo também eram do arroz**, porque esses valores da classe estão explicitamente suprimidos.

## Diagnóstico parcial do piloto

### Fato observado

São Borja apresenta simultaneamente:
1. produção primária relevante e recente de arroz;
2. presença agroindustrial local expressiva no beneficiamento;
3. forte ancoragem cadastral local das unidades de beneficiamento;
4. massa de emprego e remuneração formal material nesse elo.

### Interpretação

A condição local já é suficientemente forte para que o Radar não seja usado apenas para procurar uma “atividade potencialmente instalável”. Para arroz, a pergunta de inteligência mercadológica passa a ser:

> **qual é a posição competitiva da cadeia já instalada em São Borja diante da demanda gaúcha, da produção estadual, das entradas de outras UFs, das importações, dos destinos e dos concorrentes?**

Essa é uma mudança de foco importante: de **oportunidade de entrada** para **expansão, posicionamento, mercado e encadeamento de uma capacidade local já comprovada**.

### O que permanece não respondido

Sem os valores do Radar, ainda não é possível concluir:
- tamanho da demanda estadual dos NCMs selecionados;
- parcela atendida por produção gaúcha;
- dependência de outras UFs/importações;
- participação de São Borja na oferta estadual;
- market share das empresas locais;
- mercados compradores específicos das unidades de São Borja;
- margens, lucros ou retenção financeira local.

Arquivo estruturado desta camada:
`docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv`


## Etapa 4C.2 — posição produtiva estadual e fontes complementares

### Beneficiamento estadual — IRGA

Ranking 2023:
- total RS: **5.722.235 t**;
- 157 unidades ativas.

Ranking 2024 corrigido:
- total RS: **5.233.168 t**;
- 157 unidades ativas.

Cálculo SBMI:

`((5.233.168 / 5.722.235) - 1) × 100 = -8,55%`

### Subconjunto nominalmente identificável de São Borja

Com crosswalk institucional IRGA + Sindarroz-RS, foram identificadas quatro empresas em São Borja presentes nos dois rankings:
- Pirahy Alimentos;
- Cerealista Albaruska;
- Ciagro Alimentos;
- Cerealista Streck.

Beneficiamento somado:
- 2023: **303.619 t**;
- 2024: **325.033 t**.

Variação:
`((325.033 / 303.619) - 1) × 100 = +7,05%`

Participação somada no RS:
- 2023: **5,30%**;
- 2024: **6,22%**;
- variação: **+0,92 p.p.**

Esse indicador é denominado **mínimo identificável** porque:
- não cobre os 20 estabelecimentos ativos do CNAE 10.61-9/01 registrados na v028;
- a lista do Sindarroz-RS não é censo;
- o ranking IRGA é por empresa, não por município.

Portanto, **6,22% não é o market share total de São Borja**.

### Destaques individuais

Pirahy:
- 3ª posição em 2023 e 2024;
- 216.780 t → 237.880 t;
- +9,73%;
- 3,79% → 4,55% do beneficiamento estadual.

Ciagro:
- 64ª → 47ª posição;
- 20.814 t → 27.017 t;
- +29,80%.

### Pulso estadual mais recente

Série IRGA/Taxa CDO “Beneficiamento e saídas de arroz — base casca”:

jan–abr/2025:
**2.331.192 t**.

jan–abr/2026:
**2.578.193 t**.

Cálculo:
`((2.578.193 / 2.331.192) - 1) × 100 = +10,60%`

A comparação cobre apenas quatro meses e usa uma série diferente do ranking anual por empresa.

### RS360 — escala econômica histórica

Publicação oficial da Sefaz/RS de 23/04/2024 informa, para a indústria arrozeira:
- **R$ 20,28 bilhões** em vendas acumuladas em 12 meses;
- crescimento de **17,3%**;
- aumento absoluto de **R$ 2,99 bilhões**;
- vendas para outras UFs: **+32%**.

Esse dado é estadual e setorial; não equivale a NCM individual nem a faturamento de São Borja.

### Comex Stat — próxima camada

A API e os dados abertos do MDIC/SECEX foram confirmados.

Plano:
- RS: sete NCMs do piloto em nível de 8 dígitos;
- São Borja: SH4 `1006` no módulo municipal;
- métricas: kg líquido, valor FOB e países.

Limitação:
no módulo municipal, município = **domicílio fiscal da empresa exportadora/importadora**, não origem física da mercadoria.

Arquivos novos:
- `docs/data_sources/irga_beneficiamento_sao_borja_identificado_v001.csv`
- `docs/data_sources/irga_beneficiamento_sao_borja_auditoria_v001.md`
- `docs/data_sources/arroz_contexto_mercado_estadual_v001.csv`
- `docs/data_sources/rs360_arroz_auditoria_v001.md`
- `docs/data_sources/comexstat_arroz_plano_extracao_v001.md`

Planilha exploratória:
- `IRGA_benef_SB`;
- `Arroz_contexto_RS`.

## Diagnóstico atualizado

Já é possível afirmar, com evidências separadas:

**DADO OBSERVADO/CALCULADO**
- São Borja é grande produtor primário de arroz;
- possui estrutura de beneficiamento local material;
- possui empresas locais com participação mensurável no beneficiamento estadual;
- o subconjunto identificável dessas empresas ganhou participação relativa entre 2023 e 2024;
- o mercado estadual da indústria arrozeira possui elevada escala de vendas e relevante circulação interestadual.

**INTERPRETAÇÃO**
A cadeia do arroz é um caso prioritário de inteligência de mercado territorial porque São Borja combina produção agrícola, transformação industrial e operadores com alcance estadual.

**AINDA NÃO CONCLUÍVEL**
- demanda estadual por cada NCM;
- dependência de OUF/importações por produto;
- market share financeiro de São Borja;
- origem/destino doméstico específico das empresas locais;
- faturamento ou lucro das empresas;
- causalidade entre produção primária e desempenho industrial.
