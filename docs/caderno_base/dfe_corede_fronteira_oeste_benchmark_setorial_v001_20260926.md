# DFe/NFC-e — benchmark setorial do COREDE Fronteira Oeste — v001

**Data da extração:** 2026-09-26  
**Fonte:** Receita Estadual do Rio Grande do Sul — Receita Dados — modelo semântico público do Power BI de Documentos Fiscais Eletrônicos  
**Geografia:** COREDE Fronteira Oeste/RS  
**Período:** ano de 2025  
**Modelo fiscal:** NFC-e  
**Classificação setorial:** divisão CNAE  
**Unidades:** R$; número de NFC-e; percentuais calculados sobre o total consultado do COREDE  
**Natureza:** valores observados no modelo público + agregações calculadas pelo SBMI.  
**Regra de uso:** **benchmark regional; não é faturamento de São Borja, não é demanda residente e não é market share municipal.**

## 1. Objeto

Explorar a camada setorial que a Receita Estadual expõe no modelo público:

`COREDE × divisão CNAE × modelo DFe × período × valor/quantidade`.

A consulta foi executada diretamente sobre a entidade pública:

`v_PBI_Dfe_Totais_Corede_Setor`

com filtros:

- `corede = FRONTEIRA OESTE`;
- `ano = 2025`;
- `modelo = NFC-e`.

Foram recuperados código e nome da divisão CNAE, soma do valor dos documentos e soma da quantidade de documentos.

## 2. Resultado agregado do COREDE

Total consultado em 2025:

- **valor NFC-e:** R$ 11.129.327.451,44;
- **quantidade NFC-e:** 105.348.009 documentos;
- **divisões CNAE retornadas:** 49, incluindo categoria sem CNAE.

Esses valores abrangem todo o COREDE Fronteira Oeste. Não devem ser comparados como se fossem o mercado de São Borja.

## 3. Divisões mais diretamente relacionadas aos cadernos

| Divisão CNAE | Descrição observada | Valor NFC-e 2025 | Qtde. NFC-e | % do valor do COREDE | Valor médio por documento* |
|---:|---|---:|---:|---:|---:|
| 47 | Comércio varejista | R$ 10.123.462.565,95 | 96.180.616 | 90,9620% | R$ 105,25 |
| 56 | Alimentação | R$ 316.172.104,88 | 4.512.222 | 2,8409% | R$ 70,07 |
| 45 | Comércio e reparação de veículos automotores e motocicletas | R$ 234.892.630,08 | 890.964 | 2,1106% | R$ 263,64 |
| 55 | Alojamento | R$ 10.510.879,96 | 125.394 | 0,0944% | R$ 83,82 |
| 75 | Atividades veterinárias | R$ 3.588.608,60 | 22.859 | 0,0322% | R$ 156,99 |
| 95 | Reparação e manutenção de equipamentos de informática e comunicação e de objetos pessoais e domésticos | R$ 4.468.359,13 | 30.101 | 0,0401% | R$ 148,45 |
| 96 | Outras atividades de serviços pessoais | R$ 702.479,69 | 6.293 | 0,0063% | R$ 111,63 |
| 86 | Atividades de atenção à saúde humana | R$ 32.057,05 | 309 | 0,0003% | R$ 103,74 |

`* valor médio por documento = valor NFC-e / quantidade NFC-e. Não denominar automaticamente “ticket médio do consumidor”.`


## 3A. Série histórica 2023-2025

Foi executada uma segunda consulta pública, mantendo `COREDE = FRONTEIRA OESTE` e `modelo = NFC-e`, mas recuperando a série anual 2023-2025 por divisão CNAE.

### Total NFC-e do COREDE

| Ano | Valor NFC-e | Quantidade | Valor médio/documento |
|---:|---:|---:|---:|
| 2023 | R$ 8.872.450.065,47 | 90.808.849 | R$ 97,70 |
| 2024 | R$ 10.078.977.261,66 | 99.650.104 | R$ 101,14 |
| 2025 | R$ 11.129.327.451,44 | 105.348.009 | R$ 105,64 |

Variações **nominais calculadas**:

- valor total: +13,60% em 2024/2023 e +10,42% em 2025/2024;
- quantidade de documentos: +9,74% e +5,72%, respectivamente;
- 2025 versus 2023: +25,44% em valor e +16,01% em quantidade.

Essas variações não devem ser interpretadas como crescimento real de consumo sem deflação e controle de mudanças de formalização/composição.

### Divisão 47 — Comércio varejista

| Ano | Valor NFC-e | Quantidade | % do valor regional |
|---:|---:|---:|---:|
| 2023 | R$ 8.129.374.041,41 | 84.349.815 | 91,6249% |
| 2024 | R$ 9.219.172.341,39 | 91.986.774 | 91,4693% |
| 2025 | R$ 10.123.462.565,95 | 96.180.616 | 90,9620% |

Variação nominal calculada 2025/2023:
- valor: **+24,53%**;
- quantidade: **+14,03%**.

A participação da divisão 47 no valor regional permanece dominante, mas recua levemente no período. Isso é uma descrição da composição fiscal regional; não identifica quais categorias varejistas ganharam ou perderam participação dentro da divisão.

### Divisão 56 — Alimentação

| Ano | Valor NFC-e | Quantidade | % do valor regional |
|---:|---:|---:|---:|
| 2023 | R$ 237.676.433,30 | 3.376.466 | 2,6788% |
| 2024 | R$ 283.321.723,88 | 4.218.259 | 2,8110% |
| 2025 | R$ 316.172.104,88 | 4.512.222 | 2,8409% |

Variação nominal calculada:
- 2024/2023: +19,20% em valor e +24,93% em quantidade;
- 2025/2024: +11,59% em valor e +6,97% em quantidade;
- 2025/2023: **+33,03% em valor e +33,64% em quantidade**.

O valor médio por documento da divisão 56 foi:
- 2023: R$ 70,39;
- 2024: R$ 67,17;
- 2025: R$ 70,07.

**Interpretação limitada:** no benchmark regional, o avanço nominal de 2023 a 2025 da divisão 56 ocorreu junto com crescimento de magnitude semelhante no número de NFC-e, enquanto o valor médio por documento terminou 2025 próximo ao nível de 2023. Isso não prova crescimento real de volume consumido, pois documento fiscal não equivale necessariamente a unidade de refeição ou consumidor e ainda falta deflação específica.

### Rastreabilidade da série

Workflow:
`.github/workflows/dfe-corede-sector-series-v1.yml`

Execução:
- run: `36263445903`;
- job: `108463502982`;
- commit: `f3c267430d596aecc3209b776d18bf1b25a30a2b`;
- artifact: `10912264032`;
- digest: `sha256:67c01e1555bdc609ede426d4c3e2bd52a55eb808ad3ff196be3ea0361b092b2c`.

Google Drive:
- `SBMI_DFe_COREDE_Fronteira_Oeste_CNAE_2023_2025_NFCe_v001.zip`;
- ID: `1bmG3wbEWxEBreGa7OznmTs3VDcAT1-Ee`.

## 4. Interpretação setorial

### 4.1 Comércio varejista — divisão 47

A divisão 47 responde por aproximadamente **90,96% do valor das NFC-e** na consulta regional de 2025.

Isso confirma que, no recorte de NFC-e, o varejo é o grande agregado emissor no COREDE. Porém, a divisão 47 mistura simultaneamente:

- alimentação para consumo no domicílio;
- medicamentos, higiene e cuidados pessoais;
- vestuário;
- móveis/eletrodomésticos;
- utilidades;
- pet e outras categorias varejistas.

Portanto, **CNAE divisão 47 não separa Bens Essenciais, Saúde/Higiene e Bens Não Essenciais** e não pode servir como denominador direto desses três cadernos.

### 4.2 Alimentação Fora do Lar — divisão 56

A divisão CNAE 56 — `ALIMENTAÇÃO` — apresentou:

- **R$ 316.172.104,88** em NFC-e no COREDE Fronteira Oeste em 2025;
- **4.512.222** documentos;
- **2,8409%** do valor NFC-e regional consultado.

Entre os cinco mercados, este é o encaixe CNAE-divisão mais próximo de um dos objetos editoriais: Alimentação Fora do Lar.

Mesmo assim, ele permanece **benchmark regional**. Não é lícito aplicar a participação populacional de São Borja, número de estabelecimentos, CNPJs, empregos ou qualquer outro rateio para produzir faturamento municipal.

### 4.3 Serviços

As divisões 55, 75, 86, 95 e 96 possuem NFC-e, mas o caderno Serviços é mais amplo e parte relevante do setor é documentada por NFS-e/ISS, não NFC-e.

Consequentemente, a camada DFe regional não substitui a rota municipal de NFS-e já especificada.

### 4.4 Saúde/Higiene

A divisão 86 refere-se a serviços de atenção à saúde humana e não ao varejo farmacêutico. Farmácias e drogarias pertencem ao comércio varejista, portanto seus valores estão misturados na divisão 47 no nível de divisão CNAE.

Logo, o benchmark regional por divisão não resolve o denominador de Saúde/Higiene.

## 5. O que o benchmark acrescenta

### Dado observado

Há uma camada fiscal regional-setorial pública que permite:
- mensurar valor e quantidade de DFe por divisão CNAE;
- selecionar modelo fiscal;
- observar o COREDE Fronteira Oeste.

### Interpretação

Essa camada é útil para:
- contextualizar estrutura setorial formal regional;
- avaliar sazonalidade e evolução por divisão;
- identificar divisões com correspondência razoável a mercados específicos;
- conferir se um setor tem materialidade fiscal suficiente para aprofundamento.

### O que ela não resolve

Não fornece:
- `São Borja × CNAE`;
- `São Borja × NCM`;
- origem/residência do consumidor;
- faturamento empresarial individual;
- market share.

## 6. Comparabilidade com a demanda residente

Não calcular razões do tipo:

`Demanda residente São Borja / DFe setor Fronteira Oeste`.

A geografia, o conceito e a população de referência são distintos.

Exemplo:
- DR Alimentação Fora do Lar de São Borja: estimativa modelada de gasto de residentes;
- divisão 56 do COREDE: valor fiscal observado de NFC-e emitida por estabelecimentos de toda a Fronteira Oeste, incluindo consumo de residentes e não residentes de vários municípios.

A relação entre essas grandezas é informativa apenas em nível qualitativo/metodológico, não como taxa de captura.

## 7. Consequência para market share

O benchmark regional **não desbloqueia market share municipal**.

Para market share em São Borja continua sendo necessário obter:
- denominador monetário `São Borja × categoria/setor × período`;
- numerador empresarial no mesmo perímetro.

Não serão usados:
- rateio do COREDE por população;
- rateio por CNPJ/lojas;
- vínculos ou remuneração;
- proporção do total municipal de DFe pela composição regional.

## 8. Rastreabilidade

Workflow:
`.github/workflows/dfe-corede-sector-query-v1.yml`

Execução final com CSV decodificado:
- run: `36263264355`;
- commit: `b444f92a76abadef18e13a701625b6b03e69941a`;
- artifact: `10912758889`;
- digest: `sha256:50d2509f0ab0ca0ab3ce1d2009b45d3ed92c01312f994a5cc7d373010a9ee116`.

Google Drive:
- `SBMI_DFe_COREDE_Fronteira_Oeste_CNAE_2025_NFCe_v001.zip`;
- ID: `1T9b7q_JII1sHzeH8oiShYdNydHhPZQEe`.

O pacote contém o resultado bruto da consulta, resumo e CSV decodificado por divisão CNAE.

## 9. Próximo aprofundamento

1. manter a série 2023-2025 como benchmark regional e, quando pertinente, ampliá-la historicamente;
2. manter essa série como **benchmark regional**, nunca como estimativa municipal;
3. buscar dado oficial agregado `município × CNAE` por solicitação à Receita Estadual;
4. para Serviços, priorizar NFS-e municipal;
5. para Saúde/Higiene, manter auditoria separada de Farmácia Popular/BNAFAR e buscar dado fiscal varejista mais granular.
