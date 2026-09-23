# Preços Dinâmicos — extração dirigida 2026 — auditoria de transporte/texto

**Data:** 22/09/2026
**Status:** extração técnica para auditoria; NÃO promover valores sem validação manual contra a página oficial.
**Fonte:** Receita.doc / SEFAZ-RS — Boletins de Preços Dinâmicos, competências jan., fev., abr., mai., jun. e jul./2026.

## Método

- download direto dos PDFs oficiais listados em Receita.doc;
- SHA-256 dos arquivos;
- extração das páginas 1 a 4 por pdftotext -layout;
- renderização a 300 dpi e OCR PSM 6/11 somente como fallback técnico;
- nenhuma interpolação.

## Extração bruta

===== 2026-01 =====
=== PAGE 1 ===
--- pdftotext ---
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edigdo n° 18 | Janeiro 2026 —
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

_ Edicdo n° 18 | Janeiro 2026 —

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
--- OCR PSM 6 ---
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Janeiro de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
LITORAL ft Maior prego 313,21 1,83% 1,83% 0,67%
HORTENSIAS 309,86 -0,19% -0,19% 0,62%
RIO DA VARZEA 302,54 1,83% 1,83% 1,51%
SERRA 300,93 -1,02% -1,02% 0,94%
MEDIO ALTO URUGUAI 297,48 0,25% 0,25% 0,87%
NOROESTE COLONIAL 296,14 -0,62% -0,62% -1,44%
ALTO JACUI 296,01 -0,81% -0,81% -2,63%
CAMPOS DE CIMA DA SERRA 294,91 -0,19% -0,19% -1,09%
METROPOLITANO DELTA DO JACUI 294,69 -0,21% -0,21% -1,71%
VALE DO TAQUARI 294,34 0,29% 0,29% -2,14%
PRODUCAO 294,11 -1,03% -1,03% -1,03%
ALTO DA SERRA DO BOTUCARAI 293,01 0,46% 0,46% -1,16%
VALE DO RIO DOS SINOS 292,88 -0,03% -0,03% -0,42%
NORDESTE 292,73 -0,40% -0,40% 0,05%
VALE DO CAI 291,70 -1,39% -1,39% -1,08%
CELEIRO 290,53 -1,39% -1,39% -1,27%
VALE DO JAGUARI 288,98 -0,10% -0,10% 0,80%
FRONTEIRA NOROESTE 288,70 -0,30% -0,30% -2,60%
MISSOES 288,67 1,26% 1,26% -0,23%
NORTE 285,54 -1,19% -1,19% -4,68%
VALE DO RIO PARDO 282,20 -0,32% -0,32% -1,96%
PARANHANA-ENCOSTA SERRA 280,88 -0,69% -0,69% -1,10%
SUL 279,64 0,10% 0,10% -1,06%
CENTRAL 278,32 -0,61% -0,61% -1,59%
CENTRO SUL 276,10 -0,85% -0,85% -1,02%
FRONTEIRA OESTE 275,41 -1,14% -1,14% -0,38%
CAMPANHA 275,00 -0,54% -0,54% -0,64%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Janeiro de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

LITORAL

ft Maior prego

313,21

1,83%

1,83%

0,67%

HORTENSIAS

309,86

-0,19%

-0,19%

0,62%

RIO DA VARZEA

302,54

1,83%

1,83%

1,51%

SERRA

300,93

-1,02%

-1,02%

0,94%

MEDIO ALTO URUGUAI

297,48

0,25%

0,25%

0,87%

NOROESTE COLONIAL

296,14

-0,62%

-0,62%

-1,44%

ALTO JACUI

296,01

-0,81%

-0,81%

-2,63%

CAMPOS DE CIMA DA SERRA

294,91

-0,19%

-0,19%

-1,09%

METROPOLITANO DELTA DO JACUI

294,69

-0,21%

-0,21%

-1,71%

VALE DO TAQUARI

294,34

0,29%

0,29%

-2,14%

PRODUCAO

294,11

-1,03%

-1,03%

-1,03%

ALTO DA SERRA DO BOTUCARAI

293,01

0,46%

0,46%

-1,16%

VALE DO RIO DOS SINOS

292,88

-0,03%

-0,03%

-0,42%

NORDESTE

292,73

-0,40%

-0,40%

0,05%

VALE DO CAI

291,70

-1,39%

-1,39%

-1,08%

CELEIRO

290,53

-1,39%

-1,39%

-1,27%

RIO GRANDE DO SUL

Média RS

289,83

-0,48%

-0,48%

-1,54%

VALE DO JAGUARI

288,98

-0,10%

-0,10%

0,80%

FRONTEIRA NOROESTE

288,70

-0,30%

-0,30%

-2,60%

MISSOES

288,67

1,26%

1,26%

-0,23%

NORTE

285,54

-1,19%

-1,19%

-4,68%

VALE DO RIO PARDO

282,20

-0,32%

-0,32%

-1,96%

PARANHANA-ENCOSTA SERRA

280,88

-0,69%

-0,69%

-1,10%

SUL

279,64

0,10%

0,10%

-1,06%

CENTRAL

278,32

-0,61%

-0,61%

-1,59%

CENTRO SUL

276,10

-0,85%

-0,85%

-1,02%

FRONTEIRA OESTE

275,41

-1,14%

-1,14%

-0,38%

CAMPANHA

275,00

-0,54%

-0,54%

-0,64%

JACUI CENTRO

273,62

0,51%

0,51%

-0,89%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Janeiro de 2026
Faas
{oy
ore ! Legenda
JX af Hi Preco max
ay” ;
A a ee la
vA A BG
ag a
Preco min
Evolucao PCA-RE
Fevereiro de 2025 até Janeiro de 2026
Evolucao do preco
@JACUI CENTRO @LITORAL @RIO GRANDE DO SUL
320
31100 313,21
51 30
7
300 49 9
93 ; > 2936 5
83
280
27 62
260
fev mar abr mai jun jul ago set out nov dez jan
2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Janeiro de 2026

iF

Legenda

Hi Preco max

| Aged

i

a

Preco min

Evolucao PCA-RE

Fevereiro de 2025 até Janeiro de 2026

Evolucao do preco

@JACUI CENTRO @LITORAL @RIO GRANDE DO SUL

320

313,21

311,00

30

31

300

29

03

29

83

280

27

62

260

mar

abr

mai

jun

jul

ago

set

out

nov

dez

jan

2025

2026

===== 2026-02 =====
=== PAGE 1 ===
--- pdftotext ---
This slide contains the following visuals: slicer ,card. Please refer to the notes on this slide for details
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edicao n° 19 | Fevereiro 2026
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

_ Edicdo n° 19 | Fevereiro 2026 —

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
This slide contains the following visuals: htmlContent443BE3AD55E043BF878BED274D3A6855 ,textbox ,textbox ,shape ,textbox ,shape ,textbox ,image ,Região do Estado ,Mês/Ano. Please refer to the notes on this slide for details
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
This slide contains the following visuals: card ,Evolução do preço ,textbox ,shape ,textbox ,shape ,textbox ,slicer ,textbox. Please refer to the notes on this slide for details
--- OCR PSM 6 ---
°
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Fevereiro de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
HORTENSIAS ft Maior prego 306,19 -1,18% -1,37% -1,79%
LITTORAL 304,75 -2,70% -0,92% -2,01%
CAMPOS DE CIMA DA SERRA 300,79 1,99% 1,79% -1,07%
SERRA 300,12 -0,27% -1,29% -0,59%
MEDIO ALTO URUGUAI 296,97 -0,17% 0,08% -0,97%
ALTO JACUI 296,92 0,31% -0,51% -3,04%
RIO DA VARZEA 296,59 -1,97% -0,17% -1,16%
METROPOLITANO DELTA DO JACUI 296,01 0,45% 0,24% -2,83%
NOROESTE COLONIAL 293,82 -0,79% -1,40% -2,19%
VALE DO CAI 293,54 0,63% -0,77% -0,82%
VALE DO RIO DOS SINOS 293,36 0,16% 0,13% -1,12%
NORDESTE 292,20 -0,18% -0,58% -1,32%
PRODUCAO 291,94 -0,74% -1,77% -3,00%
ALTO DA SERRA DO BOTUCARAI 291,75 -0,43% 0,02% -2,98%
VALE DO TAQUARI 291,30 -1,03% -0,75% -4,42%
MISSOES 289,14 0,16% 1,42% -1,76%
CELEIRO 288,57 -0,68% -2,06% -3,09%
VALE DO JAGUARI 288,01 -0,34% -0,43% -1,81%
FRONTEIRA NOROESTE 286,85 -0,64% -0,94% -4,85%
NORTE 285,10 -0,16% -1,34% -5,37%
VALE DO RIO PARDO 282,21 0,00% -0,31% -1,89%
SUL 281,98 0,84% 0,94% -1,80%
CENTRAL 278,63 0,11% -0,50% -2,27%
CENTRO SUL 278,05 0,71% -0,15% -0,43%
PARANHANA-ENCOSTA SERRA 277,90 -1,06% -1,75% -2,63%
CAMPANHA 276,30 0,47% -0,07% -2,77%
FRONTEIRA OESTE 273,97 -0,52% -1,66% -1,99%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Fevereiro de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

HORTENSIAS

ft Maior prego

306,19

-1,18%

-1,37%

-1,79%

LITORAL

304,75

-2,70%

-0,92%

-2,01%

CAMPOS DE CIMA DA SERRA

300,79

1,99%

1,79%

-1,07%

SERRA

300,12

-0,27%

-1,29%

-0,59%

MEDIO ALTO URUGUAI

296,97

-0,17%

0,08%

-0,97%

ALTO JACUI

296,92

0,31%

-0,51%

-3,04%

RIO DA VARZEA

296,59

-1,97%

-0,17%

-1,16%

METROPOLITANO DELTA DO JACUI

296,01

0,45%

0,24%

-2,83%

NOROESTE COLONIAL

293,82

-0,79%

-1,40%

-2,19%

VALE DO CAI

293,54

0,63%

-0,77%

-0,82%

VALE DO RIO DOS SINOS

293,36

0,16%

0,13%

-1,12%

NORDESTE

292,20

-0,18%

-0,58%

-1,32%

PRODUCAO

291,94

-0,74%

-1,77%

-3,00%

ALTO DA SERRA DO BOTUCARAI

0,02%

291,75

-0,43%

-2,98%

VALE DO TAQUARI

291,30

-1,03%

-0,75%

-4,42%

MISSOES

289,14

0,16%

1,42%

-1,76%

CELEIRO

288,57

-0,68%

-2,06%

-3,09%

RIO GRANDE DO SUL

Média RS

288,33

-0,52%

-0,99%

-2,83%

VALE DO JAGUARI

288,01

-0,34%

-0,43%

-1,81%

FRONTEIRA NOROESTE

286,85

-0,64%

-0,94%

-4,85%

NORTE

285,10

-0,16%

-1,34%

-5,37%

VALE DO RIO PARDO

282,21

0,00%

-0,31%

-1,89%

SUL

281,98

0,84%

0,94%

-1,80%

CENTRAL

278,63

0,11%

-0,50%

-2,27%

CENTRO SUL

278,05

0,71%

-0,15%

-0,43%

PARANHANA-ENCOSTA SERRA

277,90

-1,06%

-1,75%

-2,63%

CAMPANHA

276,30

0,47%

-0,07%

-2,77%

FRONTEIRA OESTE

273,97

-0,52%

-1,66%

-1,99%

JACUI CENTRO

267,47

-2,25%

-1,74%

-2,97%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
This slide contains the following visuals: Evolução do preço ,image ,textbox ,shapeMap ,textbox ,card ,textbox ,shape ,shape ,textbox ,slicer ,card ,slicer. Please refer to the notes on this slide for details
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Fevereiro de 2026
Legenda
Hi Preco max
|| Preco min
Evolucao PCA-RE
Marco de 2025 até Fevereiro de 2026
Evolucao do preco
@HORTENSIAS @JACU! CENTRO @RIO GRANDE DO SUL
320
87
315, 45 31 5
9
306,19
300 292.14 7 06
296,26 296, 77 29
288, 287-15 288,33
280 ,, 2
13 27 2
47
260
mar abr mai jun jul ago set out nov dez jan fev
2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Fevereiro de 2026

Legenda

Hi Preco max

| Preco min

Evolucao PCA-RE

Marco de 2025 até Fevereiro de 2026

Evolucao do preco

@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL

320

87

31

45

31

06

306,19

300

77

296,26

29

15

288,33

280

27

13

27

47

260

mar

abr

mai

jun

jul

ago

set

out

nov

dez

jan

fev

2025

2026

===== 2026-04 =====
=== PAGE 1 ===
--- pdftotext ---
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edigao n° 21| Abril 2026
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

_ Edigdo n° 21 | Abril 2026

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
--- OCR PSM 6 ---
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Abril de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
HORTENSIAS ft Maior prego 314,05 2.16% 1,16% -0,62%
NOROESTE COLONIAL 310,32 4,47% 4,14% -0,33%
RIO DA VARZEA 309,92 3,66% 4,31% 1,90%
SERRA 308,76 1,96% 1,55% 0,31%
MEDIO ALTO URUGUAI 307,88 3,07% 3,75% 1,26%
ALTO JACUI 307,63 2,63% 3,08% -2,17%
VALE DO CAI 305,45 3,74% 3,26% 1,53%
NORDESTE 304,12 3,61% 3,48% 0,01%
CAMPOS DE CIMA DA SERRA 304,02 2,58% 2,89% -1,51%
PRODUCAO 303,87 3,73% 2,25% -1,61%
ALTO DA SERRA DO BOTUCARAI 303,07 3,07% 3,90% -1,35%
LITORAL 302,60 1,61% -1,62% 0,41%
VALE DO TAQUARI 301,98 2,54% 2,89% -2,45%
METROPOLITANO DELTA DO JACUI 301,40 1,78% 2,06% -2,32%
FRONTEIRA NOROESTE 299,80 3,12% 3,53% -3,78%
VALE DO RIO DOS SINOS 299,00 2,36% 2,06% 0,31%
NORTE 297,72 4,10% 3,03% -2,79%
MISSOES 296,62 2,22% 4,05% -0,54%
VALE DO JAGUARI 295,98 2,27% 2,32% 0,49%
CELEIRO 292,96 1,80% -0,57% -2,97%
VALE DO RIO PARDO 291,67 2,93% 3,02% 0,81%
CENTRAL 287,18 2,80% 2,55% -0,25%
SUL 286,92 2,51% 2,71% -1,59%
PARANHANA-ENCOSTA SERRA 286,12 1,47% 1,16% -1,17%
CAMPANHA 285,51 4,03% 3,27% -2,18%
CENTRO SUL 282,90 2,45% 1,59% -0,26%
FRONTEIRA OESTE 281,40 2,49% 1,01% -1,47%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Abril de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

HORTENSIAS

ft Maior prego

314,05

2,16%

1,16%

-0,62%

NOROESTE COLONIAL

310,32

4,47%

4,14%

-0,33%

RIO DA VARZEA

309,92

3,66%

4,31%

1,90%

SERRA

308,76

1,96%

1,55%

0,31%

MEDIO ALTO URUGUAI

307,88

3,07%

3,75%

1,26%

ALTO JACUI

307,63

2,63%

3,08%

-2,17%

VALE DO CAI

305,45

3,74%

3,26%

1,53%

NORDESTE

304,12

3,61%

3,48%

0,01%

CAMPOS DE CIMA DA SERRA

304,02

2,58%

2,89%

-1,51%

PRODUCAO

303,87

3,73%

2,25%

-1,61%

ALTO DA SERRA DO BOTUCARAI

303,07

3,07%

3,90%

-1,35%

LITORAL

302,60

1,61%

-1,62%

0,41%

VALE DO TAQUARI

301,98

2,54%

2,89%

-2,45%

METROPOLITANO DELTA DO JACUI

2,06%

301,40

1,78%

-2,32%

FRONTEIRA NOROESTE

299,80

3,12%

3,53%

-3,78%

VALE DO RIO DOS SINOS

299,00

2,36%

2,06%

0,31%

NORTE

297,72

4,10%

3,03%

-2,79%

MISSOES

296,62

2,22%

4,05%

-0,54%

RIO GRANDE DO SUL

Média RS

296,26

2,92%

1,73%

-0,96%

VALE DO JAGUARI

295,98

2,27%

2,32%

0,49%

CELEIRO

292,96

1,80%

-0,57%

-2,97%

VALE DO RIO PARDO

291,67

2,93%

3,02%

0,81%

CENTRAL

287,18

2,80%

2,55%

-0,25%

SUL

286,92

2,51%

2,71%

-1,59%

PARANHANA-ENCOSTA SERRA

286,12

1,47%

1,16%

-1,17%

CAMPANHA

285,51

4,03%

3,27%

-2,18%

CENTRO SUL

282,90

2,45%

1,59%

-0,26%

FRONTEIRA OESTE

281,40

2,49%

1,01%

-1,47%

JACUI CENTRO

279,37

3,35%

2,63%

-0,40%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Abril de 2026
y mee Legenda
y afi Preco max
ae y a AY, NG 7 (J
wy - "!
: " Preco min
Evolucao PCA-RE

Maio de 2025 até Abril de 2026

Evolucao do preco
@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL
320 3, as
45 314,05
ee
30
"06 ,
an ti 296,26
|
oO e 5 i, 5

280 89? 279 37
sa 7 —_ Sones | Naot aNG

mai jun jul ago set out nov dez jan fev mar abr

2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Abril de 2026

Legenda

ere

= Preco max

ae

N

rt

oy

“pial

| Preco min

Evolucao PCA-RE

Maio de 2025 até Abril de 2026

Evolucao do preco

@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL

320

31

87

45

31

314,05

30

30

300

06

29

280

273,37

ne. 13

27

270

260

mai

jun

ja

ago

out

nov

dez

jan

fev

mar

abr

2025

2026

===== 2026-05 =====
=== PAGE 1 ===
--- pdftotext ---
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edigéo n° 22 | Maio 2026
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

__ Edigdo n° 22 | Maio 2026

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
--- OCR PSM 6 ---
:
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Maio de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
HORTENSIAS # Maior preco 319,44 1,72% 2,90% 0,81%
SERRA 314,78 1,95% 3,53% 2,69%
NOROESTE COLONIAL 313,85 1,14% 5,32% 1,81%
RIO DA VARZEA 309,44 -0,16% 4,15% 2,94%
CAMPOS DE CIMA DA SERRA 309,25 1,72% 4,66% 0,78%
MEDIO ALTO URUGUAI 308,91 0,34% 4,10% 2,70%
NORDESTE 308,06 1,30% 4,82% 2,57%
ALTO JACUI 307,36 -0,09% 2,99% -0,58%
VALE DO TAQUARI 306,82 1,60% 4,54% 0,17%
METROPOLITANO DELTA DO JACUI 306,67 1,75% 3,84% 0,10%
PRODUCAO 306,47 0,85% 3,12% 0,69%
VALE DO CAI 306,35 0,29% 3,56% 2,73%
LITORAL 304,69 0,69% -0,94% 2,04%
FRONTEIRA NOROESTE 304,61 1,60% 5,19% 0,28%
ALTO DA SERRA DO BOTUCARAI 304,60 0,51% 4,43% 0,79%
VALE DO RIO DOS SINOS 303,09 1,37% 3,45% 2,01%
NORTE 299,94 0,74% 3,80% -0,85%
MISSOES 297,91 0,44% 4,50% 1,02%
VALE DO JAGUARI 297,55 0,53% 2,87% 2,65%
CELEIRO 296,19 1,10% 0,53% -0,46%
VALE DO RIO PARDO 295,00 1,14% 4,20% 2,27%
CENTRAL 292,28 1,78% 4,37% 1,64%
CAMPANHA 289,89 1,53% 4,85% 1,19%
SUL 289,82 1,01% 3,75% 0,35%
PARANHANA-ENCOSTA SERRA 289,60 1,22% 2,39% 0,10%
CENTRO SUL 288,09 1,84% 3,45% 0,52%
FRONTEIRA OESTE 285,58 1,49% 2,51% 1,10%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Maio de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

HORTENSIAS

ft Maior prego

319,44

1,72%

2,90%

0,81%

SERRA

314,78

1,95%

3,53%

2,69%

NOROESTE COLONIAL

313,85

1,14%

5,32%

1,81%

RIO DA VARZEA

309,44

-0,16%

4,15%

2,94%

CAMPOS DE CIMA DA SERRA

309,25

1,72%

4,66%

0,78%

MEDIO ALTO URUGUAI

308,91

0,34%

4,10%

2,70%

NORDESTE

308,06

1,30%

4,82%

2,57%

ALTO JACUI

307,36

-0,09%

2,99%

-0,58%

VALE DO TAQUARI

306,82

1,60%

4,54%

0,17%

METROPOLITANO DELTA DO JACUI

306,67

1,75%

3,84%

0,10%

PRODUCAO

306,47

0,85%

3,12%

0,69%

VALE DO CAI

306,35

0,29%

3,56%

2,73%

LITORAL

304,69

0,69%

-0,94%

2,04%

FRONTEIRA NOROESTE

304,61

1,60%

5,19%

0,28%

ALTO DA SERRA DO BOTUCARAI

304,60

0,51%

4,43%

0,79%

VALE DO RIO DOS SINOS

303,09

1,37%

3,45%

2,01%

RIO GRANDE DO SUL

Média RS

300,54

1.44%

3,20%

1,30%

NORTE

299,94

0,74%

3,80%

-0,85%

MISSOES

297,91

0,44%

4,50%

1,02%

VALE DO JAGUARI

297,55

0,53%

2,87%

2,65%

CELEIRO

296,19

1,10%

0,53%

-0,46%

VALE DO RIO PARDO

295,00

1,14%

4,20%

2,27%

CENTRAL

292,28

1,78%

4,37%

1,64%

CAMPANHA

289,89

1,53%

4,85%

1,19%

SUL

289,82

1,01%

3,75%

0,35%

PARANHANA-ENCOSTA SERRA

289,60

1,22%

2,39%

0,10%

CENTRO SUL

288,09

1,84%

3,45%

0,52%

FRONTEIRA OESTE

285,58

1,49%

2,51%

1,10%

JACUI CENTRO

280,67

0,46%

3,10%

0,64%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Maio de 2026
on Nu
Lone” Legenda
LON ONS 8
(eae afi = Preco max
ra > - at oe ’ ? nar
6 7 —_ = \ LAY, oy \o
we q
. Preco min
Evolugao PCA-RE
Junho de 2025 até Maio de 2026
Evolucao do preco
@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL
320
315,87 45 31 44
31
9 4 30
300 06 am. 300,54
297,07 29
288, Ts 85
280 27392 279320 67
Se es 56 : aa ~ = . a _ ~ 279 o 4
260 — —eeue =
jun jul ago set out nov dez jan fev mar abr mai
2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Maio de 2026

MF,

Legenda

= Preco max

1

- a

| Preco min

Evolugao PCA-RE

Junho de 2025 ate Maio de 2026

Evolucao do preco

@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL

320

313,87

31

44

45

31

30

30

,06

300,54

300 39707

29

77

29

280 27

27g

D.67

me

13

27

270

260

set

out

nov

dez

esd

mar

abr

‘ie

jun

jul

ago

jan

2025

2026

04

===== 2026-06 =====
=== PAGE 1 ===
--- pdftotext ---
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edigdo n° 23 | Junho 2026
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

__ Edicdo n° 23 | Junho 2026

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
--- OCR PSM 6 ---
°
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Junho de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
HORTENSIAS ft Maior prego 320,46 0,32% 3,22% 1,45%
NOROESTE COLONIAL 315,70 0,59% 5,94% 3,70%
SERRA 314,92 0,04% 3,58% 1,99%
CAMPOS DE CIMA DA SERRA 311,42 0,70% 5,39% 2,13%
ALTO JACUI 310,30 0,96% 3,97% 0,85%
METROPOLITANO DELTA DO JACUI 309,35 0,87% 4,75% 1,23%
RIO DA VARZEA 309,33 -0,04% 4,11% 2,86%
PRODUCAO 309,09 0,86% 4,01% 1,64%
NORDESTE 308,97 0,29% 5,13% 3,46%
VALE DO TAQUARI 307,38 0,18% 4,73% 1,26%
MEDIO ALTO URUGUAI 307,32 -0,51% 3,57% 3,75%
VALE DO CAI 306,73 0,12% 3,69% 2,88%
ALTO DA SERRA DO BOTUCARAI 305,70 0,36% 4,81% 1,79%
FRONTEIRA NOROESTE 304,36 -0,08% 5,11% 2,76%
LITTORAL 304,11 -0,19% -1,13% 2,46%
VALE DO RIO DOS SINOS 301,39 -0,56% 2.87% 1,27%
NORTE 300,15 0,07% 3,87% 0,24%
VALE DO JAGUARI 298,89 0,45% 3,33% 3,09%
MISSOES 297,77 -0,05% 4,45% 1,96%
VALE DO RIO PARDO 295,22 0,08% 4,28% 2,01%
CENTRAL 291,54 -0,25% 4,11% 1,95%
CAMPANHA 290,89 0,34% 5,21% 2,24%
CELEIRO 290,08 -2,06% -1,55% -1,02%
PARANHANA-ENCOSTA SERRA 289,76 0,06% 2,45% 1,26%
SUL 289,64 -0,06% 3,68% 0,81%
FRONTEIRA OESTE 287,31 0,60% 3,13% 2,38%
CENTRO SUL 286,19 -0,66% 2,77% 0,89%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Junho de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

HORTENSIAS

ft Maior prego

320,46

0,32%

3,22%

1,45%

NOROESTE COLONIAL

315,70

0,59%

5,94%

3,70%

SERRA

314,92

0,04%

3,58%

1,99%

CAMPOS DE CIMA DA SERRA

311,42

0,70%

5,39%

2,13%

ALTO JACUI

310,30

0,96%

3,97%

0,85%

METROPOLITANO DELTA DO JACUI

309,35

0,87%

4,75%

1,23%

RIO DA VARZEA

309,33

-0,04%

4,11%

2,86%

PRODUCAO

309,09

0,86%

4,01%

1,64%

NORDESTE

308,97

0,29%

5,13%

3,46%

VALE DO TAQUARI

307,38

0,18%

4,73%

1,26%

MEDIO ALTO URUGUAI

307,32

-0,51%

3,57%

3,75%

VALE DO CAI

306,73

0,12%

3,69%

2,88%

ALTO DA SERRA DO BOTUCARAI

305,70

0,36%

4,81%

1,79%

FRONTEIRA NOROESTE

304,36

-0,08%

5,11%

2,76%

LITORAL

304,11

-0,19%

-1,13%

2,46%

VALE DO RIO DOS SINOS

301,39

-0,56%

2,87%

1,27%

RIO GRANDE DO SUL

Média RS

301,22

0,23%

3,44%

1,40%

NORTE

300,15

0,07%

3,87%

0,24%

VALE DO JAGUARI

298,89

0,45%

3,33%

3,09%

MISSOES

297,77

-0,05%

4,45%

1,96%

VALE DO RIO PARDO

295,22

0,08%

4,28%

2,01%

CENTRAL

291,54

-0,25%

4,11%

1,95%

CAMPANHA

290,89

0,34%

5,21%

2,24%

CELEIRO

290,08

-2,06%

-1,55%

-1,02%

PARANHANA-ENCOSTA SERRA

289,76

0,06%

2,45%

1,26%

SUL

289,64

-0,06%

3,68%

0,81%

FRONTEIRA OESTE

287,31

0,60%

3,13%

2,38%

CENTRO SUL

286,19

-0,66%

2,77%

0,89%

JACUI CENTRO

274,23

-2,29%

0,74%

-1,68%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Junho de 2026
Legenda
Hi Preco max
|| Preco min
Evolucao PCA-RE
Julho de 2025 até Junho de 2026
Evolucao do preco
@HORTENSIAS @JACU! CENTRO @RIO GRANDE DO SUL
320 3 46
313,45 3 31
86 3
3
,06 ~ 3 22
300 39
292,77 > 2
288, 15 "35
280 27 v
27213 2 27 < 27 23
260
jul ago set out nov dez jan fev mar abr mai jun
2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Junho de 2026

Legenda

Hi Preco max

"

| Preco min

Evolucao PCA-RE

Julho de 2025 até Junho de 2026

Evolucao do preco

@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL

46

320

313,45

86

31

22

300

29

292.77

15

280

27

27

13

27

27

23

260

jul

ago

set

out

nov

dez

jan

fev

mar

abr

mai

jun

2025

2026

===== 2026-07 =====
=== PAGE 1 ===
--- pdftotext ---
--- OCR PSM 6 ---
@ «©
Precos
Dinamicos
Receita Estadual RS
_ Edigao n° 24 | Julho 2026
Li
r%
A £,
& GOVERNO DO ESTADO
RECEITA ESTADUAL RS RIO GRANDE 00 SUL
--- OCR PSM 11 ---
P recos

Dinamicos

Receita Estadual RS

__ Edicao n° 24 | Julho 2026

>

GOVERNO DO ESTADO

RECEITA ESTADUAL RS

ee

=== PAGE 2 ===
--- pdftotext ---
--- OCR PSM 6 ---
Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no
ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como
referéncia a estrutura de consumo das familias gauchas, com base nos dados
extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE
2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar
domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco
da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o
indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,
optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e
produtos. Foram selecionados os produtos mais representativos, em termos de
quantidades consumidas, dentro dos seus respectivos subgrupos de consumo
alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a
unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores
relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de
agregacdo, 0 preco médio é representado como o preco ponderado pelos
respectivos pesos de cada produto. Dessa forma, a metodologia de
determinacao do preco do PCA-RE utiliza os valores de consumo per capita
como multiplicador dos precos de cada produto dentro do escopo do Projeto.
--- OCR PSM 11 ---
Notas

Para a defini¢do dos alimentos que sao objeto do levantamento dos precos no

ambito do Projeto Precos Dinamicos da Receita Estadual, tomou-se como

referéncia a estrutura de consumo das familias gauchas, com base nos dados

extraidos da Pesquisa de Orcamento Familiar mais recente (POF/IBGE

2017/2018), mais especificamente da Tabela 2393 (Aquisicdo alimentar

domiciliar per capita).

Para facilitar a harmonizacao entre a POF e os produtos atuais, como 0 Preco

da Cesta de Alimentos da Receita Estadual (PCA-RE), ou futuros, como o

indice de Inflacdo de Alimentos dos Precos Dindmicos da Receita Estadual,

optou-se por adotar a taxonomia da Tabela 2393, a saber: grupos, subgrupos e

produtos. Foram selecionados os produtos mais representativos, em termos de

quantidades consumidas, dentro dos seus respectivos subgrupos de consumo

alimentar. Desta selecao, resultaram 80 produtos, que passaram a constituir a

unidade basica de analise, agreg ados em 30 subgrupos e 12 grupos.

Ainda, com os dados extraidos da POF, foram utilizados também os valores

relativos ao consumo per capita de cada nivel. Ao subir em cada nivel de

agregacdo, 0 preco médio é representado como o preco ponderado pelos

respectivos pesos de cada produto. Dessa forma, a metodologia de

determinacao do preco do PCA-RE utiliza os valores de consumo per capita

como multiplicador dos precos de cada produto dentro do escopo do Projeto.

=== PAGE 3 ===
--- pdftotext ---
--- OCR PSM 6 ---
:
1. Preco da Cesta de Alimentos (PCA-RE)
PCA-RE por Regiao do RS
Julho de 2026
COREDE Valor (R$) Variagao Variagao Variagao
. Més Ano 12 Meses
HORTENSIAS # Maior preco 318,70 -0,55% 2,66% 1,68%
SERRA 312,87 -0,65% 2,91% 2,15%
NOROESTE COLONIAL 309,71 -1,90% 3,93% 2,47%
NORDESTE 306,86 -0,68% 4,41% 3,76%
CAMPOS DE CIMA DA SERRA 306,65 -1,53% 3,78% 1,36%
MEDIO ALTO URUGUAI 305,52 -0,59% 2,96% 3,28%
PRODUCAO 304,30 -1,55% 2,39% 1,38%
VALE DO CAI 304,03 -0,88% 2,78% 3,29%
RIO DA VARZEA 303,71 -1,82% 2,22% 1,44%
ALTO DA SERRA DO BOTUCARAI 303,56 -0,70% 4,07% 1,57%
ALTO JACUI 303,47 -2,20% 1,68% -0,56%
METROPOLITANO DELTA DO JACUI 302,79 -2,12% 2,53% 1,27%
VALE DO TAQUARI 302,49 -1,59% 3,07% 0,33%
LITORAL 300,99 -1,02% -2,15% 2,72%
FRONTEIRA NOROESTE 300,30 -1,34% 3,70% 1,87%
VALE DO JAGUARI 300,03 0,38% 3,72% 3,53%
VALE DO RIO DOS SINOS 298,45 -0,98% 1,87% 2,32%
NORTE 298,28 -0,62% 3,22% 4,02%
MISSOES 295,69 -0,70% 3,72% 2,18%
VALE DO RIO PARDO 292,13 -1,05% 3,19% 1,05%
PARANHANA-ENCOSTA SERRA 287,26 -0,86% 1,56% 1,63%
CAMPANHA 287,05 -1,32% 3,82% 2,68%
SUL 286,49 -1,09% 2,56% 0,93%
CELEIRO 285,69 -1,51% -3,04% -1,56%
CENTRO SUL 284,20 -0,70% 2,05% 0,32%
FRONTEIRA OESTE 282,74 -1,59% 1,49% 1,14%
CENTRAL 282,34 -3,16% 0,82% -0,47%
--- OCR PSM 11 ---
1. Preco da Cesta de Alimentos (PCA-RE)

PCA-RE por Regiao do RS

Julho de 2026

COREDE

Valor (R$)

Variacao

Variagao

Variagao

Més

Ano

12 Meses

HORTENSIAS

ft Maior prego

318,70

-0,55%

2,66%

1,68%

SERRA

312,87

-0,65%

2,91%

2,15%

NOROESTE COLONIAL

309,71

-1,90%

3,93%

2,47%

NORDESTE

306,86

-0,68%

4,41%

3,76%

CAMPOS DE CIMA DA SERRA

306,65

-1,53%

3,78%

1,36%

MEDIO ALTO URUGUAI

305,52

-0,59%

2,96%

3,28%

PRODUCAO

304,30

-1,55%

2,39%

1,38%

VALE DO CAI

304,03

-0,88%

2,78%

3,29%

RIO DA VARZEA

303,71

-1,82%

2,22%

1,44%

ALTO DA SERRA DO BOTUCARAI

303,56

-0,70%

4,07%

1,57%

ALTO JACUI

303,47

-2,20%

1,68%

-0,56%

METROPOLITANO DELTA DO JACUI

302,79

-2,12%

2,53%

1,27%

VALE DO TAQUARI

302,49

-1,59%

3,07%

0,33%

LITORAL

300,99

-1,02%

-2,15%

2,72%

FRONTEIRA NOROESTE

300,30

-1,34%

3,70%

1,87%

VALE DO JAGUARI

300,03

0,38%

3,72%

3,53%

VALE DO RIO DOS SINOS

298,45

-0,98%

1,87%

2,32%

NORTE

298,28

-0,62%

3,22%

4,02%

RIO GRANDE DO SUL

Média RS

296,84

-1,45%

1,93%

1,39%

MISSOES

295,69

-0,70%

3,72%

2,18%

VALE DO RIO PARDO

292,13

-1,05%

3,19%

1,05%

PARANHANA-ENCOSTA SERRA

287,26

-0,86%

1,56%

1,63%

CAMPANHA

287,05

-1,32%

3,82%

2,68%

SUL

286,49

-1,09%

2,56%

0,93%

CELEIRO

285,69

-1,51%

-3,04%

-1,56%

CENTRO SUL

284,20

-0,70%

2,05%

0,32%

FRONTEIRA OESTE

282,74

-1,59%

1,49%

1,14%

CENTRAL

282,34

-3,16%

0,82%

-0,47%

JACUI CENTRO

271,31

-1,07%

-0,34%

-0,30%

# Menor preco

=== PAGE 4 ===
--- pdftotext ---
--- OCR PSM 6 ---
PCA-RE por Regiao do RS
Julho de 2026
Legenda
Hi Preco max
|| Preco min
Evolucao PCA-RE
Agosto de 2025 até Julho de 2026
Evolucao do preco
@HORTENSIAS @JACU! CENTRO @ RIO GRANDE DO SUL
320 3
31 318,70
a
3
06 ' 3 2
: er ee es
2 a1 ‘
288; 15 "85
280 27 7
27 27
31
26
260
ago set out nov dez jan fev mar abr mai jun jul
2025 2026
--- OCR PSM 11 ---
PCA-RE por Regiao do RS

Julho de 2026

Legenda

Hi Preco max

"

| Preco min

Evolucao PCA-RE

Agosto de 2025 até Julho de 2026

Evolucao do preco

@HORTENSIAS @JACUI CENTRO @RIO GRANDE DO SUL

320

318,70

86

31

30

300

29

296,84

28

15

280

27

P53

27

27

26

31

260

ago

set

out

nov

dez

jan

fev

mar

abr

mai

jun

jul

2025

2026

os



## Governança

- tratar OCR como camada auxiliar, nunca como dado observado definitivo;
- validar manualmente Fronteira Oeste e Rio Grande do Sul antes de atualizar o seed;
- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge.
