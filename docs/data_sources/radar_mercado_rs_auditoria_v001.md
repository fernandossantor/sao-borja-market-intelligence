# Radar do Mercado da Receita Estadual — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Auditar o Radar do Mercado da Receita Estadual como fonte de inteligência mercadológica para estrutura de demanda, origem da oferta, fluxos comerciais, concorrência e oportunidades produtivas.

## Fontes

- Painel oficial: https://receitadados.sefaz.rs.gov.br/desenvolve-rs/radar-do-mercado-da-receita-estadual/
- Nota Técnica CIET 05/2026 — **Radar de Mercado da Receita Estadual**, publicada em 30/06/2026. Link oficial: https://receitadoc.sefaz.rs.gov.br/media/rhwdpvaz/nota_tecnica_radar_mercado_v1.pdf
- Material institucional sobre a versão ampliada lançada em 30/06/2026.

## Achados observados — etapa 4A

### Natureza

A versão ampliada de 2026 utiliza a base de NF-e para produzir indicadores econômicos estratégicos da indústria.

A divulgação institucional informa atualização mensal e utilização da totalidade das operações fiscais registradas no Estado.

### Dimensões confirmadas

O painel permite, conforme documentação institucional:
- visualizar perfil de vendas da indústria gaúcha;
- mapear origem dos produtos comprados no RS;
- identificar destino da produção gaúcha por UF e país;
- identificar mercados consumidores;
- identificar principais concorrentes;
- medir composição de mercado/market share por produto;
- distinguir origem entre produção local, compras de outras UFs e importações;
- mapear carências de atendimento da demanda pela produção local;
- classificar dependência externa;
- identificar oportunidades de expansão, substituição de importações e fortalecimento de cadeias.

### Unidade de produto

A documentação e exemplos publicados usam produtos/NCM como eixo analítico.

### Geografia

Foi confirmada evidência de dimensão municipal em visualizações derivadas do Radar, mas a granularidade não deve ser presumida para todos os indicadores.

Status atual:
- RS: confirmado;
- UF/país em fluxos: confirmado;
- município: presente em parte das visualizações/modelo;
- COREDE: ainda não confirmado para todos os indicadores.

### Regra SBMI

Não afirmar que um indicador é municipal apenas porque outro visual do Radar usa município.

A auditoria deverá registrar página por página:

`pagina | indicador | conceito | produto/NCM | periodo | unidade | geografia_disponivel | filtros | extraivel | limitacao`

## Aplicações prioritárias ao SBMI

1. **Lacunas de oferta**
   - demanda relevante no RS;
   - baixa produção interna;
   - dependência de outras UFs/importações.

2. **Cadeias relacionadas a São Borja**
   - cruzar produtos/NCM com setores/CNAEs locais;
   - avaliar se há produção local em mercados com dependência externa estadual;
   - identificar potenciais fornecedores e concorrentes.

3. **Benchmark territorial**
   - quando houver município, comparar São Borja com outros polos;
   - quando não houver município, manter o indicador estadual como contexto de mercado.

## Limitações

- o painel é orientado principalmente à indústria e fluxos de mercadorias;
- não representa diretamente demanda final das famílias;
- market share estadual não é market share municipal;
- produto/NCM e CNAE são classificações distintas e exigem mapeamento metodológico;
- oportunidade de mercado não equivale a viabilidade econômica de investimento.

## Próxima subetapa — 4B

Auditar o painel interativo página por página e construir uma matriz de granularidade e filtros antes de qualquer extração setorial.


## Etapa 4B — matriz de dimensões verificáveis

### Limitação técnica da auditoria do Power BI

O portal oficial incorpora o Radar por um relatório público do Power BI:

`https://app.powerbi.com/view?r=eyJrIjoiYzMxNWUyMDQtYWVjOC00MTcxLWJhN2ItY2NjYTk2MWEwNmNjIiwidCI6IjgzYmQwOTBiLTc1NmUtNGEwMi1hNTEyLWU1ZWEwMmMwMzA0MSJ9`

O HTML público do Receita Dados confirma o iframe, mas o conteúdo interno do relatório é carregado client-side. Nesta auditoria não foi possível recuperar de forma confiável os **nomes atuais das páginas** nem a lista completa de filtros diretamente do Power BI.

Por isso, a matriz abaixo registra **dimensões analíticas confirmadas**, e não inventa títulos de páginas.

### Dimensões atuais confirmadas por fonte institucional — versão ampliada 2026

#### 1. Demanda estadual por produto

Conceito documentado:
- produtos com maior demanda interna no Rio Grande do Sul;
- detalhamento por produto;
- eixo classificatório por NCM confirmado por documentação e usos publicados do Radar.

Geografia:
- demanda: Rio Grande do Sul.

Uso SBMI:
- identificar produtos com mercado estadual relevante;
- cruzar depois com setores e capacidades presentes em São Borja.

Limitação:
- demanda estadual não é demanda municipal.

#### 2. Composição/origem do abastecimento

Conceito documentado:
- para cada produto, distinguir:
  - produção local (RS);
  - compras de outras unidades da federação;
  - importações.

Geografia:
- mercado consumidor: RS;
- origem: RS / outras UFs / exterior.

Uso SBMI:
- medir dependência externa estadual;
- identificar lacunas produtivas e oportunidades de substituição de oferta externa.

#### 3. Market share por produto no mercado gaúcho

Conceito documentado:
- composição de mercado dos produtos associados aos setores industriais;
- participação da produção gaúcha, entradas de outras UFs e importações.

Unidade:
- participação percentual / composição de mercado;
- volume financeiro associado ao produto quando disponibilizado.

Limitação:
- market share do RS não é market share de São Borja.

#### 4. Destino da produção industrial gaúcha

Conceito documentado:
- destino da produção discriminado por unidade da federação e país.

Geografia:
- origem: RS;
- destino: UF e país.

Uso SBMI:
- contextualizar mercados externos de cadeias em que São Borja possua operadores/produtores;
- identificar mercados consumidores potenciais.

#### 5. Mercados consumidores e concorrentes

A divulgação oficial da versão 2026 informa identificação de:
- mercados consumidores;
- principais concorrentes de cada setor produtivo.

A granularidade exata desses visuais ainda não foi recuperada do Power BI.

Status:
- dimensão confirmada;
- filtros e geografia pendentes.

#### 6. Dependência externa / carência de produção local

Conceito documentado:
- produtos com demanda interna relevante e baixa produção local;
- classificação por níveis de dependência externa.

Uso SBMI:
- triagem de oportunidades, nunca prova de viabilidade econômica local.

### Evidência histórica de granularidade municipal

Publicação acadêmica de 2025 que utilizou diretamente o Radar mostra visualizações intituladas, entre outras:

- “Mapa do setor de Máquinas e Equipamentos por Município/RS em 2023”;
- “Mapa de calor do setor de Metalurgia por Município/RS em 2023”.

Isso confirma que a estrutura do Radar já continha **município** para localização/volume de produção industrial.

Classificação dessa evidência:
- fonte secundária acadêmica que declara uso direto do Radar;
- referência temporal: dados de 2023, acesso ao Radar em 2025;
- **não suficiente para afirmar que o filtro municipal está disponível em todas as páginas da versão ampliada de 2026**.

### Estrutura setorial — evidência histórica de uso

A mesma publicação descreve a taxonomia do Desenvolve RS em três níveis:
- Atividades;
- Áreas;
- Setores.

As Atividades citadas são:
- Produção Primária;
- Indústrias;
- Atacado;
- Varejo;
- Serviços.

Essa taxonomia será tratada como **evidência histórica/auxiliar** até confirmação direta no painel atual.

### Conclusão territorial da 4B

No estado atual da auditoria:

| Dimensão | Menor geografia confirmada | São Borja diretamente utilizável? |
|---|---|---|
| Demanda por NCM | RS | Não |
| Origem do abastecimento | RS / OUF / exterior | Não |
| Market share por produto | RS | Não |
| Destino da produção | UF / país | Não como mercado de origem municipal |
| Mercados consumidores | a auditar | Ainda não |
| Concorrentes | a auditar | Ainda não |
| Localização/volume de produção | Município — evidência histórica | **Potencialmente sim** |
| Dependência externa | RS | Não |

### Implicação para o SBMI

O Radar deve ser integrado em duas camadas distintas:

1. **Camada estadual de oportunidade**
   - NCM;
   - demanda;
   - produção interna;
   - entradas OUF;
   - importações;
   - dependência externa;
   - market share.

2. **Camada territorial de capacidade/oferta**
   - município de localização das indústrias, quando o visual atual permitir;
   - cruzamento posterior com CNAE/CNPJ/VAF/emprego já auditados no SBMI.

A análise correta não será:
> “São Borja demanda R$ X deste produto”.

Mas sim:
> “O mercado gaúcho apresenta demanda e dependência externa para determinado produto; São Borja possui ou não capacidades produtivas relacionadas que justificam investigação de oportunidade”.

Isso mantém separadas **demanda estadual** e **capacidade territorial local**.

## Próxima subetapa — 4C

1. testar, por evidência pública acessível, quais setores/produtos do Radar possuem mapa municipal na versão atual;
2. selecionar uma pequena cesta piloto de NCMs associados a cadeias já relevantes em São Borja;
3. construir o primeiro cruzamento exploratório:
   `NCM / oportunidade estadual → CNAE/capacidade local → evidência municipal existente → hipótese mercadológica`;
4. manter toda hipótese como exploratória até validação.


## Etapa 4C — piloto iniciado: cadeia do arroz

Foi selecionada a cadeia do arroz como primeiro teste controlado do método `oportunidade estadual por NCM → capacidade territorial local`.

### Base territorial usada para seleção

O Caderno Setorial de Bens Essenciais registra, a partir de documentação municipal/Emater já incorporada ao projeto, forte presença histórica de arroz na base agropecuária de São Borja.

Isso justifica a **seleção do piloto**, mas não será tratado como prova de capacidade industrial corrente.

### CNAE oficial associado

Fonte CONCLA/IBGE:

- `0111-3/01` — Cultivo de arroz;
- `1061-9/01` — Beneficiamento de arroz;
- `1061-9/02` — Fabricação de produtos do arroz.

### NCM piloto

Fonte: Ministério da Agricultura e Pecuária — Sumário Executivo Arroz 2026; nomenclatura vigente consultável no CLASSIF/RFB.

Cesta inicial:
- `10062010`;
- `10062020`;
- `10063011`;
- `10063019`;
- `10063021`;
- `10063029`;
- `10064000`.

O objetivo é recuperar, para cada código:
- demanda no RS;
- produção interna;
- entradas de outras UFs;
- importações;
- dependência externa;
- localização municipal da produção, se disponível;
- mercados consumidores;
- concorrentes.

Arquivos criados:

- `docs/data_sources/radar_piloto_arroz_v001.md`
- `docs/data_sources/radar_piloto_arroz_ncm_v001.csv`

Planilha exploratória do Drive:
- nova aba `Radar_piloto_arroz`.

Nenhum valor foi preenchido por inferência. Os campos quantitativos permanecem pendentes até leitura verificável do Radar.


## Etapa 4C.1 — capacidade territorial local confirmada

Em 18/09/2026, a auditoria passou a usar como **fonte de leitura** o Caderno-Base técnico v028 — análise integrada (17Sk5Hu_CQ-hKJYTNEfYSN4F97MiuZrfrU9o_VxEg0Rc), que é posterior à v016 registrada no corpo do PR #41.

**Regra de preservação:** a v028 foi apenas consultada; não foi editada, duplicada nem promovida pela branch exploratória.

### Achado principal

A cadeia do arroz em São Borja já possui capacidade territorial materialmente documentada. O elo de beneficiamento não é uma hipótese de instalação futura.

Na camada canônica RAIS 2025 × RFB do projeto, o CNAE 10.61-9/01 apresenta:
- 20 estabelecimentos ativos;
- 19 matrizes;
- 1 filial de raiz cuja matriz também está em São Borja;
- 953 vínculos formais;
- R$ 3.491.039,35 de massa de remuneração de dezembro/2025;
- 97,34% dos vínculos da divisão 10 no recorte;
- 98,69% da massa de remuneração de dezembro da divisão 10 no recorte.

A própria v028 qualifica esse elo como um encadeamento agroindustrial local material e alerta para não generalizá-lo a toda a indústria ou a todo o agro.

### Validação histórica independente

IBGE/CEMPRE — Tabela 9418, São Borja, 2022:

Grupo 10.6:
- 23 empresas/organizações;
- 994 pessoas ocupadas;
- 960 assalariadas;
- R$ 42,945 milhões em salários e outras remunerações.

Classe 10.61-9:
- 21 empresas/organizações;
- demais variáveis de pessoal/remuneração suprimidas como X.

Cálculo: 21 / 23 × 100 = 91,30% dos estabelecimentos do grupo 10.6 pertenciam à classe 10.61-9.

Não inferir a mesma proporção para emprego ou remuneração.

### Produção primária recente

IRGA — safra 2023/2024, São Borja:
- 31.166 ha semeados;
- 2.014 ha perdidos;
- 29.152 ha colhidos;
- 8.129 kg/ha;
- 236.977 t.

IRGA/SEAPI — safra 2024/2025:
- 306.703,95 t;
- 8º maior produtor do RS;
- 4º da Fronteira Oeste.

Cálculo SBMI: ((306.703,95 / 236.977) - 1) × 100 = 29,42%.

### Mudança na pergunta analítica

Para arroz, o Radar não será mais usado prioritariamente para perguntar “há uma atividade que poderia existir em São Borja?”.

A pergunta passa a ser:

> **como a capacidade produtiva e agroindustrial já instalada em São Borja se posiciona diante da demanda estadual, da produção gaúcha, das entradas de outras UFs, das importações, dos concorrentes e dos mercados consumidores?**

Essa mudança evita confundir oportunidade de entrada com oportunidade de expansão/posicionamento de uma cadeia já presente.

### Arquivo estruturado

docs/data_sources/radar_piloto_arroz_capacidade_local_v001.csv

Planilha exploratória: aba Radar_arroz_cap_local.

### Pendências do Radar

Continuam sem valor preenchido:
- demanda RS por NCM;
- produção interna RS por NCM;
- entradas de outras UFs;
- importações;
- dependência externa;
- market share;
- mercados consumidores;
- concorrentes.

Nenhum desses campos será inferido a partir da força local da cadeia.


## Errata de fonte — 18/09/2026

A Nota Técnica CIET 05/2026 foi localizada na página oficial de Boletins/Notas Técnicas do Receita.doc, com publicação em 30/06/2026.

A anotação anterior de “nota técnica não localizada” estava incorreta e foi substituída.

Nesta sessão, o arquivo PDF oficial foi identificado pelo link institucional, porém seu conteúdo integral não pôde ser recuperado automaticamente por timeout/cache. Portanto:
- a existência, o título, a data e o URL são **confirmados oficialmente**;
- detalhes metodológicos adicionais do PDF só serão incorporados após leitura verificável do conteúdo;
- nenhuma informação metodológica será atribuída à NT 05/2026 apenas por inferência.

## Atualização 18/09/2026 - recuperação da NT CIET 05 e fallback estadual por NCM

Foi executada nova tentativa de recuperação integral da **NT CIET 05/2026 - Radar de Mercado da Receita Estadual** a partir da página oficial de Boletins/Notas Técnicas da Receita Estadual.

### Identificação oficial reconfirmada

- página Receita.doc: a NT 05/2026 está listada entre as Notas Técnicas;
- data de publicação: 30/06/2026;
- URL oficial: `https://receitadoc.sefaz.rs.gov.br/media/rhwdpvaz/nota_tecnica_radar_mercado_v1.pdf`.

### Resultado técnico

O link oficial do PDF continua retornando timeout/cache no mecanismo de recuperação. Assim, **o texto integral da NT permanece não lido** e nenhum detalhe metodológico novo foi atribuído à nota.

A auditoria específica das tentativas e das regras de não inferência foi registrada em:

`docs/data_sources/nt_ciet_05_2026_recuperacao_v001.md`

### Fallback oficial - não Radar

Como previsto no checkpoint, foram buscadas fontes oficiais compatíveis para a camada estadual dos NCMs do arroz, sem substituir semanticamente os indicadores do Radar.

A **Nota Técnica DEE 102**, com dados brutos do Comex Stat/MDIC, contém valores estaduais de exportação no 3º trimestre de 2024 para três NCMs da cesta piloto:

- `10064000` - US$ 65.459.780 FOB;
- `10063021` - US$ 35.360.813 FOB;
- `10063011` - US$ 16.412.640 FOB.

Esses valores foram preservados em:

`docs/data_sources/arroz_ncm_estado_fallback_oficial_v001.csv`

Classificação: **DADO OBSERVADO - fallback oficial não Radar**.

Limitação obrigatória: exportação estadual por NCM não equivale a demanda interna gaúcha, produção interna destinada ao RS, entradas de outras UFs, importações totais do mercado interno, dependência externa ou market share do Radar.

A divulgação oficial da NT DEE 135 informa adicionalmente que, no 2º trimestre de 2026, o valor exportado de arroz pelo RS cresceu 14,8% frente ao mesmo trimestre de 2025, com acréscimo de US$ 13,6 milhões. O texto público consultado não desagrega esse resultado por NCM; por isso ele foi mantido apenas como contexto agregado.

### Decisão de preservação

Os campos quantitativos de `radar_piloto_arroz_ncm_v001.csv` associados à demanda/origem da oferta/dependência permanecem vazios.

Não houve alteração de bases ou cadernos canônicos.

## Etapa 4D — leitura integral da NT CIET 05/2026

O PDF integral da Nota Técnica foi recebido e lido em 18/09/2026. Isso resolve a principal pendência metodológica da auditoria.

### Fontes, universo e periodicidade

A NT confirma:
- NFe como base principal;
- MDIC/Siscomex como complemento no comércio exterior;
- Regime Geral + Simples Nacional;
- granularidade por Setor industrial e NCM de 8 dígitos;
- atualização mensal com consolidação do mês imediatamente anterior.

### Oportunidades — regras exatas

A página trabalha com:
- operações efetivas;
- acumulado dos últimos 12 meses comparado aos 12 meses anteriores;
- correção financeira pelo D-ICMS.

Fórmula oficial:

`Part. RS = INT / (INT + OUF + EXT)`

Faixas:
- crítica: <5%;
- alta: 5% a 15%;
- média: 15% a 30%.

O indicador de volume financeiro saindo do RS corresponde à soma das entradas OUF + EXT.

### Mercado Nacional

Foram confirmadas três perspectivas distintas:
- Consumidores: estados que compram da indústria do RS;
- Fornecedores: estados que abastecem o RS em NCM/Categoria;
- Concorrentes: estados cujas vendas concorrem com a produção industrial gaúcha no mercado interno.

Nesta página, operações exteriores são excluídas.

### Competitividade RS

A NT confirma:
- análise setorial;
- portfólio Top 90% dos NCMs de maior volume de saída do setor;
- série mensal de INT/OUF/EXT em 24 meses;
- market share acumulado em 12 meses.

Fórmula do market share INT no mês m:

`ΣINT_12m / Σ(INT + OUF + EXT)_12m`

### Perfil de Vendas e Composição de Mercado

Perfil de Vendas:
- para onde a produção gaúcha é vendida;
- produto/categoria ou setor;
- INT, OUF e EXT;
- UFs destinatárias;
- países via Siscomex.

Composição de Mercado:
- de onde vem o que o RS consome;
- INT, OUF e EXT;
- visão por setor ou NCM;
- UFs de origem;
- países via Siscomex.

### Dados Abertos — nova prioridade operacional

A página Dados Abertos disponibiliza seis CSVs:
1. Saídas por Setor;
2. Exportações por NCM;
3. Composição de Mercado;
4. Importações por NCM;
5. Portfólio de NCMs por Setor;
6. Categorias de Produtos.

A NT informa atualização mensal incremental para as quatro bases de fluxo; Portfólio é substitutivo e Categorias é ocasional.

**Decisão:** a via preferencial para o SBMI passa a ser a ingestão reproduzível desses CSVs, não a extração visual do Power BI.

### Geografia municipal — revisão

A NT 05/2026 não documenta município como filtro/geografia das páginas correntes.

Consequência:
- evidência municipal de versões anteriores permanece apenas como histórico;
- o piloto de São Borja deve manter a capacidade local em IRGA/RAIS/RFB/CEMPRE e usar o Radar para a camada estadual/nacional/internacional;
- nenhum indicador atual do Radar será rotulado como municipal sem evidência direta adicional.

### Arquivos derivados

- `radar_nt_ciet_05_2026_dicionario_v001.csv`;
- `radar_mercado_dimensoes_v001.csv` revisado para a metodologia oficial.
