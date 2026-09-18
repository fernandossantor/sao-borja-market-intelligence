# Comex Stat — plano de extração para a cadeia do arroz

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — extração pendente  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Adicionar ao piloto do arroz uma camada oficial de comércio exterior sem confundir:
- fluxos internacionais;
- fluxos interestaduais;
- demanda estadual;
- localização física da produção.

## Fonte oficial

MDIC/SECEX — Comex Stat e Base de Dados Abertos.

Página oficial:
https://www.gov.br/mdic/pt-br/assuntos/comercio-exterior/estatisticas/base-de-dados-bruta

Documentação oficial da API:
https://api-comexstat.mdic.gov.br/docs

A Secex informa que a versão atual do Comex Stat possui serviço de consumo por API e dados atualizados mensalmente.

## Duas granularidades distintas

### 1. Base geral — NCM

Layout oficial:
- ano;
- mês;
- NCM;
- unidade estatística;
- país;
- UF de origem/destino do produto;
- via;
- URF;
- quantidade estatística;
- kg líquido;
- valor FOB;
- no caso de importações, frete/seguro/CIF quando aplicável.

**Uso no piloto:**
filtrar `SG_UF_NCM = RS` e os sete NCMs do arroz já definidos.

Permite:
- exportações do RS por NCM;
- importações do RS por NCM;
- países;
- peso;
- valor FOB;
- série mensal.

### 2. Base municipal — SH4

Layout oficial:
- ano;
- mês;
- SH4;
- país;
- UF do domicílio fiscal da empresa;
- município do domicílio fiscal da empresa exportadora/importadora;
- kg líquido;
- valor FOB.

**Uso no piloto:**
- município: São Borja;
- SH4: `1006` — arroz;
- exportação e importação.

### Limitação conceitual fundamental

Na base municipal, o município corresponde ao **domicílio fiscal da empresa exportadora/importadora**.

Portanto, os dados não devem ser descritos como:
> “arroz produzido fisicamente em São Borja e exportado”.

Descrição permitida:
> “exportações/importações declaradas por empresas domiciliadas em São Borja no SH4 1006”.

Essa distinção é necessária porque uma empresa pode comercializar produto originado em outra localidade.

Na base geral por UF/NCM, a dimensão é a UF do produto conforme a metodologia do Comex Stat, e não o município da empresa.

## Consultas planejadas

### RS — NCM de 8 dígitos

NCMs:
- 10062010
- 10062020
- 10063011
- 10063019
- 10063021
- 10063029
- 10064000

Períodos:
- 2023;
- 2024;
- 2025;
- jan-ago/2026.

Métricas:
- kg líquido;
- valor FOB;
- quantidade estatística quando compatível.

Detalhamento:
- NCM;
- país;
- mês.

### São Borja — SH4 1006

Períodos:
- 2023;
- 2024;
- 2025;
- jan-ago/2026.

Métricas:
- kg líquido;
- valor FOB.

Detalhamento:
- país;
- mês;
- município.

## Estado técnico desta sessão

A existência da API e dos arquivos CSV oficiais foi confirmada.

Os arquivos anuais de grande porte retornaram timeout/502 no mecanismo de download disponível nesta sessão, e a execução local não possui resolução de rede para chamar a API diretamente.

Por isso, **nenhum valor de comércio exterior foi preenchido**.

A estrutura de consulta está pronta para execução em ambiente com acesso HTTP à API/arquivos, inclusive no Codespaces do projeto.

## Relação com o Radar

Comex Stat pode preencher:
- exportações internacionais;
- importações internacionais;
- mercados externos;
- série por NCM no RS;
- série por SH4 para empresas domiciliadas em São Borja.

Comex Stat **não** substitui o Radar para:
- demanda total dentro do RS;
- entradas de outras UFs;
- produção interna destinada ao mercado gaúcho;
- market share do mercado interno gaúcho;
- fornecedores/concorrentes domésticos.

Portanto, as duas fontes são complementares.

## Retomada operacional dos arquivos municipais — 18/09/2026

A página oficial de Dados Abertos do MDIC foi revalidada.

Estado publicado:
- página atualizada em **04/09/2026**;
- últimos dados: **janeiro–agosto de 2026**.

Layout municipal oficial:
`CO_ANO; CO_MES; SH4; CO_PAIS; SG_UF_MUN; CO_MUN; KG_LIQUIDO; VL_FOB`.

Links diretos de 2026 confirmados pela própria página oficial:
- exportação municipal: `https://balanca.mdic.gov.br/balanca/bd/comexstat-bd/mun/EXP_2026_MUN.csv`;
- importação municipal: `https://balanca.mdic.gov.br/balanca/bd/comexstat-bd/mun/IMP_2026_MUN.csv`.

Nova tentativa de abertura dos dois CSVs no ambiente disponível:
- exportação: timeout;
- importação: timeout.

Consequência:
os arquivos estão documentalmente localizados, mas os bytes continuam indisponíveis para filtragem nesta sessão.

Nenhum valor de São Borja foi inferido.

O bloqueio permanece estritamente operacional.
