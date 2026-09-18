# Fechamento das rotas oficiais de fontes secundárias — 18/09/2026

**Status:** exploratório — não canônico  
**Abrangência:** São Borja/RS  
**Objetivo:** transformar a agenda de lacunas secundárias em rotas reproduzíveis de extração, sem preencher valores que ainda não foram efetivamente obtidos.

## 1. Resultado desta etapa

Cinco rotas oficiais ficaram metodologicamente suficientemente definidas para execução posterior:

- SINAC/SIMEI;
- ANP — vendas municipais;
- ANP — revendedores em operação/API;
- Comex Stat municipal;
- Cadastur.

BET municipal permanece com granularidade confirmada, mas sem valor recente de São Borja reproduzido.

Nenhum valor municipal faltante foi preenchido por snippet, extrapolação ou fonte secundária.

## 2. SINAC/SIMEI

Fonte: Receita Federal / Simples Nacional.

A página oficial consultada apresenta:

- **Optantes por UF e Município — Simei**;
- ano 2026;
- posição consolidada até **12/09/2026**;
- seleção de UF e municípios.

### Estado

**Rota oficial confirmada; valor de São Borja pendente.**

O formulário depende de interação que não foi reproduzida de modo auditável no ambiente corrente.

### Regra

O número secundário já encontrado em outras fontes continua fora da camada aceita.

Só será utilizado valor:
- retornado pela consulta oficial;
- ou reproduzido a partir de arquivo oficial primário de mesma competência.

## 3. ANP — vendas anuais por município

Fonte: Agência Nacional do Petróleo, Gás Natural e Biocombustíveis.

A página oficial estava atualizada em **18/09/2026 12:38**.

Para a granularidade municipal, os arquivos disponibilizados chegam a 2024:

- gasolina C: litros, 1990–2024;
- etanol hidratado: litros, 1990–2024;
- óleo diesel: litros, 1990–2024;
- GLP: kg, 1990–2024;
- outros derivados possuem séries e unidades próprias.

Os arquivos municipais indicados na página foram atualizados em 05/01/2026.

### Metadado auditado — gasolina C

Colunas oficiais:
- ANO;
- GRANDE REGIÃO;
- UF;
- MUNICÍPIO;
- CÓDIGO IBGE;
- VENDAS.

VENDAS = total anual vendido de gasolina em **litros**.

A fonte informa:
- até 2006: Demonstrativo de Controle de Produtos — DCP;
- desde 2007: SIMP;
- até 2006, vendas + consumo próprio das distribuidoras;
- desde 2007, apenas vendas.

### Uso permitido

Contexto de:
- abastecimento;
- mobilidade;
- intensidade de consumo de combustíveis.

### Uso proibido

Não converter volume vendido em:
- turismo;
- fluxo de argentinos;
- tráfego da ponte;
- número de clientes;
- gasto de visitantes.

O volume pode ser usado apenas como **proxy complementar**, sempre com essa limitação.

## 4. ANP — revendedores varejistas em operação

A base cadastral oficial estava atualizada em **18/09/2026 07:50** e declara explicitamente abranger revendedores que estão **em operação**.

Schema visível no CSV:

`CODIGOISIMP; AUTORIZACAO; DATAPUBLICACAO; RAZAOSOCIAL; CNPJ; ENDERECO; COMPLEMENTO; BAIRRO; CEP; UF; MUNICIPIO; BANDEIRA; DATAVINCULACAO`.

Além do CSV, a ANP documenta uma API de revendedores.

Consulta municipal documentada:

`https://revendedoresapi.anp.gov.br/v1/combustivel?municipio=SAO%20BORJA&uf=RS`

O manual informa que a API pode devolver, além dos dados cadastrais:
- classe;
- produto;
- tancagem;
- unidade de medida;
- quantidade de bicos;
- latitude/longitude;
- dados de validação geográfica;
- situação constatada;
- status SIGAF.

### Estado

**Rota e schema confirmados; resposta municipal ainda não materializada.**

## 5. Comex Stat — base municipal

Fonte: MDIC/SECEX.

Página atualizada em 04/09/2026.

Últimos dados disponíveis:
**janeiro–agosto de 2026**.

Layout oficial da base municipal:

`CO_ANO; CO_MES; SH4; CO_PAIS; SG_UF_MUN; CO_MUN; KG_LIQUIDO; VL_FOB`.

A própria fonte define:
- SG_UF_MUN = UF da empresa declarante;
- CO_MUN = município da empresa declarante.

### Consequência metodológica

O município identifica o **domicílio fiscal da empresa exportadora/importadora**.

Não demonstra que a mercadoria:
- foi produzida fisicamente em São Borja;
- foi embarcada em São Borja;
- cruzou a Ponte de São Borja;
- corresponde a uma NCM específica de 8 dígitos.

A granularidade municipal é SH4.

### Estado

Links 2026 identificados:
- exportação: `EXP_2026_MUN.csv`;
- importação: `IMP_2026_MUN.csv`.

O host de arquivos retornou erro 502 no ambiente de auditoria.

Nenhum valor foi inferido.

## 6. Cadastur

Fonte: Ministério do Turismo — Dados Abertos.

O catálogo oficial apresenta **15 conjuntos de dados** relacionados ao cadastro do Ministério, com recursos em CSV/XLS/XLSX para categorias turísticas.

Para Meios de Hospedagem, há série histórica e recurso de **2º trimestre de 2026**, atualizado em **02/07/2026**.

Categorias incluem, entre outras:
- meios de hospedagem;
- agências de turismo;
- guias;
- organizadores de eventos;
- transportadoras turísticas;
- restaurantes, cafeterias e bares;
- locadoras;
- parques;
- infraestrutura para eventos.

### Cobertura institucional

A própria descrição diferencia:
- cadastro **obrigatório** para acampamentos turísticos, agências, guias, parques temáticos, organizadores de eventos, meios de hospedagem e transportadoras turísticas;
- cadastro **opcional** para restaurantes/cafeterias/bares e diversas outras atividades.

### Consequência

Cadastur não pode ser utilizado como censo uniforme de toda a oferta turística.

Para categorias de cadastro obrigatório, ele é uma medida da oferta **formalmente cadastrada**, sujeita às regras do sistema e à validade cadastral.

Para categorias opcionais, a subcobertura é estrutural.

### Estado

**Fonte, periodicidade e cobertura conceitual auditadas; contagem de São Borja 2T2026 ainda pendente.**

## 7. Parser reproduzível criado

Foi adicionado ao branch exploratório:

`src/sbmi/secondary_official_sources.py`

com filtros que:
- usam CÓDIGO IBGE 4318002 + UF para vendas ANP;
- normalizam município/UF para cadastro corrente ANP;
- usam CO_MUN 4318002 + SG_UF_MUN=RS para Comex municipal;
- preservam SH4;
- recusam schemas incompletos em vez de adivinhar colunas.

Testes sintéticos:

`tests/test_secondary_official_sources.py`.

O módulo **não faz download e não promove dados**. Ele somente prepara a etapa de staging após os bytes oficiais serem materializados.

## 8. Estado após a rodada

| Fonte | Conceito | Geografia | Período atual auditado | Valor São Borja |
|---|---|---|---|---|
| SINAC/SIMEI | optantes | município | posição 12/09/2026 | pendente |
| ANP vendas | volume anual vendido | município | até 2024 | pendente |
| ANP revendedores | estabelecimentos em operação | município | 18/09/2026 | pendente |
| Comex Stat | domicílio fiscal + SH4 | município | jan–ago/2026 | pendente |
| Cadastur | prestadores cadastrados | município | 2T2026 | pendente |
| BET | atividade/demografia empresarial | município | edições 2026 | pendente |

A etapa reduz incerteza **metodológica**, mas não cria observações municipais inexistentes.

## 9. Próxima execução

A sequência fica:

1. tentar materializar a resposta da API ANP para São Borja;
2. materializar os CSVs municipais ANP e filtrar 4318002;
3. materializar XLSX Cadastur 2T2026 e auditar schema;
4. reproduzir SINAC/SIMEI para São Borja;
5. repetir Comex quando `balanca.mdic.gov.br` responder;
6. prosseguir BET municipal.

Nenhuma base ou caderno canônico deve ser alterado antes de decisão explícita de promoção.
