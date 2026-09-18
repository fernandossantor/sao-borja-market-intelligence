# Estrutura competitiva — concentração do footprint externo e dualidade de mercado — 18/09/2026

**Status:** exploratório — não canônico  
**Abrangência:** São Borja/RS  
**Fontes:** RFB/CNPJ 2026-08 + RAIS 2025 + modelo territorial RAIS×RFB já auditado na v006/v028.

## 1. Pergunta

O número de empresas locais e externas não responde sozinho à pergunta concorrencial.

A análise procura separar:
- **presença cadastral**: quantos estabelecimentos existem;
- **escala funcional estimada**: quanto emprego e remuneração formal está associado às estruturas externas;
- **concentração setorial**: em quais atividades o footprint externo é mais relevante.

## 2. Concentração do footprint externo

Quatro divisões concentram a maior parte da remuneração externa estimada de dezembro:

- Comércio varejista: 36,41%;
- Serviços financeiros: 15,01%;
- Transporte terrestre: 11,45%;
- Comércio atacadista: 10,18%.

Cálculo:

`36,41 + 15,01 + 11,45 + 10,18 = 73,05%`.

Essas quatro divisões representam 180 das 323 filiais de matriz externa:

`180 / 323 × 100 = 55,73%`.

### Interpretação

O footprint empresarial externo não está distribuído uniformemente. Ele se concentra fortemente em atividades que mediam:
- consumo das famílias;
- crédito e pagamentos;
- circulação de mercadorias;
- distribuição atacadista.

Essa concentração não demonstra vazamento de renda, remessa de lucros ou domínio de mercado. Ela indica **onde a concorrência de redes externas possui maior peso funcional no modelo**.

## 3. Proxy de escala formal

Para compreender por que poucas filiais podem ter peso funcional alto, foi calculado um proxy cross-period:

`vínculos externos estimados por filial externa`

comparado a:

`vínculos locais estimados por estabelecimento local`.

A razão entre ambos é registrada apenas como **proxy de escala formal**, pois:
- RAIS = 2025;
- RFB = 2026-08;
- vínculos externos são estimados;
- não representa produtividade, faturamento ou market share.

Resultados selecionados:

### Varejo
- externo: 9,51 vínculos estimados por filial;
- local: 1,13 vínculo por estabelecimento;
- razão: 8,44.

### Transporte terrestre
- externo: 6,77;
- local: 0,69;
- razão: 9,87.

### Atacado
- externo: 6,23;
- local: 2,73;
- razão: 2,28.

### Armazenamento
- externo: 9,22;
- local: 4,32;
- razão: 2,13.

### Veículos/reparação
- externo: 5,29;
- local: 0,56;
- razão: 9,50.

As razões de finanças, arquitetura/engenharia e alguns serviços tornam-se extremas por bases locais pequenas ou por poucas filiais externas; foram preservadas no CSV, mas **não devem ser usadas isoladamente em interpretação**.

## 4. Estrutura dual de mercado — interpretação territorial

Quando esta análise é combinada com a estrutura cadastral das atividades predominantemente locais, surge um padrão consistente:

### Camada A — negócios locais numerosos e fragmentados
Exemplos:
- alimentação;
- alojamento;
- saúde;
- serviços profissionais;
- publicidade/pesquisa;
- serviços pessoais;
- pequenas atividades industriais e de manutenção.

Nesses grupos, a participação de matrizes locais é elevada.

### Camada B — redes externas de maior escala funcional
Exemplos mais claros:
- varejo;
- finanças;
- transporte;
- atacado;
- armazenamento.

Neles, a presença externa cadastral pode ser relativamente pequena, mas o peso estimado no emprego/remuneração é muito maior.

### Interpretação

São Borja não deve ser descrita simplesmente como economia de “empresas locais” ou de “redes externas”.

A evidência sugere uma **estrutura dual**:
- tecido local amplo, especialmente em serviços de contato, hospitalidade, atividades profissionais e micro/pequenos operadores;
- redes externas com maior escala formal em setores padronizáveis, financeiros, distributivos e logísticos.

Isso é uma interpretação, não uma classificação oficial.

## 5. Implicações mercadológicas

Para concorrência:
- contar estabelecimentos é insuficiente;
- comparar escala, emprego, remuneração e controle territorial acrescenta informação.

Para desenvolvimento local:
- a questão não é apenas atrair empresas;
- importa também elevar escala, produtividade, cooperação e acesso a mercados dos operadores locais.

Para cadernos setoriais:
- varejo deve considerar redes externas como concorrentes funcionalmente grandes;
- serviços locais devem ser avaliados pela capacidade de capturar demanda recorrente e extralocal;
- B2B deve testar se operadores locais conseguem fornecer para agroindústria, logística e grandes redes.

## 6. O que ainda falta

- faturamento/vendas por setor e controle territorial;
- compras de fornecedores locais versus externos;
- lucro/reinvestimento;
- dados de market share;
- encadeamentos B2B;
- porte/regime tributário via Simples/SIMEI.

Arquivo estruturado:
`external_footprint_concentracao_20260918_v001.csv`.
