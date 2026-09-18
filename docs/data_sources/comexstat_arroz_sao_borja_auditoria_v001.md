# Comex Stat / MDIC — piloto da cadeia do arroz em São Borja

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — fonte complementar oficial  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Adicionar ao piloto do arroz uma dimensão oficial de comércio exterior municipal.

A fonte **não substitui o Radar do Mercado**, porque mede exportações/importações internacionais e não a demanda interna do Rio Grande do Sul.

## Fonte oficial

Ministério do Desenvolvimento, Indústria, Comércio e Serviços — SECEX.

Página de dados abertos:
https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta

Comex Stat:
https://comexstat.mdic.gov.br/pt/home

## Atualização

A página oficial consultada em 18/09/2026 informa dados disponíveis até **janeiro–agosto de 2026**.

Periodicidade:
mensal.

Série:
desde 1997.

## Duas bases que NÃO devem ser confundidas

### Dados gerais por NCM

Maior detalhe de produto:
**NCM de 8 dígitos**.

Campos publicados incluem:
- ano;
- mês;
- NCM;
- país;
- UF de origem/destino do produto;
- via;
- URF;
- quantidade estatística;
- kg líquido;
- valor FOB.

Para exportações, a UF nesta base representa a **UF produtora da mercadoria**, independentemente do município fiscal da empresa exportadora.

### Dados por município

Maior detalhe público de produto:
**SH4**.

Layout oficial:
- ano;
- mês;
- SH4;
- país;
- UF do domicílio fiscal da empresa;
- município do domicílio fiscal da empresa;
- kg líquido;
- valor FOB.

Para exportações municipais, o critério é o **domicílio fiscal do exportador**, e não necessariamente o município onde a mercadoria foi produzida.

## Limitação de sigilo

O MDIC informa que não disponibiliza NCM + município no mesmo nível de detalhe, porque a combinação poderia revelar informações econômicas de empresas.

Portanto:

- NCM 8 dígitos + município: **não publicável** no Comex Stat;
- SH4 + município: **publicável**.

Essa limitação é metodológica e deve ser preservada no SBMI.

## Correspondência do piloto do arroz

Todos os NCMs selecionados no piloto:

- 10062010
- 10062020
- 10063011
- 10063019
- 10063021
- 10063029
- 10064000

pertencem à posição:

**SH4 1006 — Arroz**.

Assim, o Comex Stat permite analisar a cadeia municipal de São Borja no exterior em **SH4 1006**, mas não separar publicamente, no nível municipal, arroz parboilizado, não parboilizado, quebrado etc.

## Variáveis úteis ao SBMI

Para São Borja / SH4 1006:

- exportações em US$ FOB;
- exportações em kg líquido;
- destinos por país;
- importações em US$ FOB;
- importações em kg líquido;
- países de origem;
- série mensal/anual;
- participação do arroz na pauta municipal, calculável com denominador municipal total;
- saldo físico e financeiro externo, desde que exportações/importações sejam comparadas com cautela metodológica.

## Uso no piloto

A arquitetura passa a ter quatro camadas:

1. **IRGA / IBGE PAM**
   - produção física municipal.

2. **RAIS / RFB / CEMPRE**
   - emprego, estabelecimentos e ancoragem agroindustrial.

3. **Comex Stat**
   - inserção internacional do domicílio fiscal das empresas de São Borja em SH4 1006.

4. **Radar do Mercado**
   - mercado interno gaúcho, origem da oferta, dependência externa, concorrentes e destinos internos/externos conforme o painel.

## Regra de interpretação

Formulação permitida:

> Empresas exportadoras domiciliadas em São Borja registraram exportações de arroz (SH4 1006) no valor/volume observado pelo Comex Stat.

Formulação não permitida:

> Todo arroz exportado por empresas domiciliadas em São Borja foi produzido em São Borja.

Também não é permitido atribuir os dados municipais a empresas específicas.

## Situação da extração

Os arquivos CSV oficiais de 2025 e 2026 foram identificados:

- `EXP_2025_MUN.csv`
- `EXP_2026_MUN.csv`

Nesta sessão, o host `balanca.mdic.gov.br` retornou erro 502/indisponibilidade para download automatizado.

Por isso, **nenhum valor municipal foi preenchido nesta etapa**.

Foi criado apenas o esquema auditável para posterior ingestão.

## Estrutura esperada de extração

Filtro:
- `CO_MUN = 4318002` — São Borja;
- `SH4 = 1006`.

Campos a preservar:
- CO_ANO;
- CO_MES;
- SH4;
- CO_PAIS;
- SG_UF_MUN;
- CO_MUN;
- KG_LIQUIDO;
- VL_FOB.

Após extração, anexar tabela de países para decodificar `CO_PAIS`.

## Limitações

- município = domicílio fiscal da empresa declarante;
- SH4 agrega todos os NCMs do arroz;
- exportação não mede produção local total;
- importação municipal não implica consumo final local;
- valor FOB não é faturamento líquido da empresa;
- fluxo externo não substitui mercado doméstico;
- não comparar diretamente a UF produtora da base NCM com a UF de domicílio da base municipal.
