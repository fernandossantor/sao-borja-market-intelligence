# Benchmark territorial — mobilidade e centralidade v001

## Objeto

Comparar São Borja com São Gabriel, Alegrete, Santiago e, como referências funcionais de fronteira, Sant'Ana do Livramento e Uruguaiana em duas dimensões distintas:

1. **mobilidade dos residentes**, pelo Censo 2022;
2. **hierarquia e atração interurbana**, pela REGIC 2018.

As duas fontes não são tratadas como mesmo período, universo ou conceito.

## Fontes

### Censo 2022 — trabalho

IBGE/SIDRA tabela 10329, variável pessoas, resultados preliminares da amostra.

O pipeline preserva:
- outro município;
- país estrangeiro;
- mais de um município ou país;
- trabalho no domicílio;
- retorno ao domicílio ≥3 dias/semana;
- residual de local ignorado quando calculável.

Células suprimidas permanecem ausentes e nunca são convertidas em zero.

### Censo 2022 — estudo

IBGE/SIDRA tabela 10324, variável pessoas, resultados preliminares da amostra.

São preservados:
- outro município;
- país estrangeiro;
- ensino médio;
- graduação;
- pós-graduação.

### REGIC 2018

Bases oficiais:
- Municípios — Hierarquia e região de influência;
- Municípios — Ligações e atração segundo temas.

**IA e PERC_LIG não são pessoas, vendas, faturamento ou market share.**

## Execução

Workflow: `territorial-flows-benchmark`  
Run canônico: `34536030079` — **success**  
Artifact: `10175426211` — `territorial-flows-benchmark-v001`  
SHA-256: `9b6624dcbabbe05da3c684e84c35d69b459181f36fb6b2382e2b423ccc6f7ab2`.

Fontes brutas:
- SIDRA 10329: `ae581b8cf5acb4d337aa46c1e5a4c167b57b67fe2f6f2c80f4b6fb8c61399e10`;
- SIDRA 10324: `db4df8cc4f9958489f85d93f15ffafbb8427f8f03d2445f332d54a39adb5a9be`;
- REGIC hierarquia: `f1d29395964e4827d8294d27b57bcffb36fc47918f91b8ecee4efdbac1cda03e`;
- REGIC ligações/atração: `4c6ed5b8b7c578ce23358b9b7e1b4b46ce9f8fb82c212a11d93ed423d7c60d33`.

Validação:
- 6/6 municípios trabalho;
- 6/6 estudo;
- 6/6 hierarquia;
- 6/6 atração;
- 9 ligações temáticas de entrada para São Borja;
- 16 ligações de saída;
- 1 vínculo hierárquico consolidado incluindo São Borja;
- reconciliação IA com diferença máxima absoluta `3.46e-11`;
- status **PASS**.

## Mobilidade laboral

Trabalham em **outro município**, como % do universo da tabela 10329:

| Município | Pessoas | % |
|---|---:|---:|
| São Borja | 493 | 1,90% |
| Alegrete | 612 | 1,97% |
| São Gabriel | 737 | 3,01% |
| Santiago | 1.207 | 5,25% |
| Sant'Ana do Livramento | 397 | 1,05% |
| Uruguaiana | 587 | 1,12% |

São Borja também registra:
- país estrangeiro: 45 pessoas = 0,17%;
- mais de um município ou país: 420 = 1,62%;
- trabalho no domicílio: 5.318 = 20,54%;
- entre trabalhadores em outro município, retorno ≥3 dias/semana: 45,64%.

**Interpretação:** a saída intermunicipal de trabalhadores residentes de São Borja não é elevada entre os comparáveis por escala.

## Mobilidade educacional

São Borja:
- estudantes: 14.375;
- outro município: 509 = 3,54%;
- país estrangeiro: 245 = 1,70%;
- graduação: 2.327;
- graduação em outro município: 275 = 11,82%.

Graduação em outro município:

| Município | % |
|---|---:|
| São Borja | 11,82% |
| Alegrete | 13,42% |
| São Gabriel | 17,41% |
| Santiago | 18,77% |
| Sant'Ana do Livramento | 12,68% |
| Uruguaiana | 8,58% |

**Interpretação:** São Borja apresenta menor saída intermunicipal de graduandos que os três comparáveis por escala. Isso é compatível com maior retenção educacional local, mas não demonstra causa institucional.

## Componente internacional

Trabalho em país estrangeiro:
- São Borja 0,17%;
- Sant'Ana do Livramento 5,41%;
- Uruguaiana 0,43%.

Estudo em país estrangeiro:
- São Borja 1,70%;
- Sant'Ana do Livramento 7,93%;
- Uruguaiana 0,15%.

São Gabriel possui célula de estudo em país estrangeiro suprimida.

**Interpretação:** em São Borja, o componente internacional aparece proporcionalmente mais no estudo que no trabalho. A tabela não identifica país ou instituição.

## Hierarquia REGIC

São Borja:
- **Centro Sub-Regional B (3B)**;
- vinculação imediata: **Uruguaiana — Centro Sub-Regional A (3A)**.

Apenas **Maçambará** possui vínculo hierárquico consolidado que inclui São Borja, em subordinação múltipla a Itaqui e São Borja.

## Atração funcional

Nove municípios aparecem com alguma ligação temática de entrada para São Borja:
Maçambará, Santo Antônio das Missões, Itaqui, Garruchos, Itacurubi, São Luiz Gonzaga, Unistalda, Santiago e Uruguaiana.

Maiores participações gerais estimadas para São Borja:
- Maçambará 27,33%;
- Santo Antônio das Missões 12,04%;
- Itaqui 10,41%;
- Garruchos 9,33%;
- Itacurubi 4,47%.

Essas participações são indicadores REGIC, não participação de vendas.

## IA geral — benchmark

| Município | IA geral |
|---|---:|
| Sant'Ana do Livramento | 41.410,17 |
| Uruguaiana | 23.005,21 |
| Alegrete | 16.695,42 |
| Santiago | 15.622,60 |
| São Gabriel | 11.826,41 |
| São Borja | 9.929,76 |

São Borja apresenta o menor IA geral entre as seis referências selecionadas.

## Centralidade seletiva

IA de São Borja:
- vestuário/calçados 13.037,63;
- móveis/eletroeletrônicos 10.525,92;
- saúde baixa/média 16.262,55;
- saúde alta 2.993,50;
- ensino superior 3.847,40;
- cultura 16.595,07;
- esportes 3.278,78;
- transporte coletivo 32.756,73.

**Interpretação:** a centralidade não é uniformemente fraca ou forte; varia por função.

## Orientação de saída — REGIC 2018

Participação geral estimada:
- Porto Alegre 37,32%;
- Santa Maria 20,00%;
- residual “Outros / Não circula jornal” 13,67%;
- Santo Ângelo 4,54%;
- Uruguaiana 4,00%;
- Ijuí 3,67%.

Temas:
- vestuário → Porto Alegre 26,67%;
- móveis/eletro → Porto Alegre 26,67%;
- saúde baixa/média → Santa Maria 36,67%;
- saúde alta → Porto Alegre 40,00%;
- ensino superior → Santa Maria 33,33%.

## Diagnóstico

O Censo não sustenta narrativa de saída generalizada dos residentes de São Borja para trabalho. A graduação também apresenta retenção relativa maior que nos três comparáveis por escala.

Em contraste, a REGIC mostra **centralidade externa limitada e seletiva**: área hierárquica direta estreita, ligações funcionais com nove municípios e dependência de centros superiores em funções especializadas.

A pergunta mercadológica passa a ser: **em quais categorias São Borja transforma oferta local em atração regional e em quais categorias o gasto/orientação se desloca para centros superiores ou outros canais?**

## Drive

Derivados: `1i95-MMLE5llDxiLYAAPhWBmJ7pQK3TOT`  
ZIP integral: `1pJvnU1KahrhUT2C50FCPWHFFd6roZJ0c`  
Documento nativo: `1BOM2psN2VmLW1Hr9iqc7mulR-c_VtJyX5AGrmDzWTlg`.

## Limitações

- Censo 2022 e REGIC 2018 têm períodos/metodologias distintos.
- Mobilidade não identifica destino na tabela SIDRA usada.
- Células suprimidas não são imputadas.
- REGIC 2018 antecede mudanças pós-pandemia e expansão recente do comércio eletrônico.
- IA/PERC_LIG não medem consumidores, vendas, market share ou vazamento monetário.
