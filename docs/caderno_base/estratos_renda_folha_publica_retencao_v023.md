# Base Territorial v023 — estratos de renda, folha pública não municipal e retenção financeira

**Data:** 2026-09-12  
**Abrangência:** São Borja/RS  
**Planilha Drive:** `1batazM_AWCZxSfMmcxiR7CO4tl8Tk5xFx7LOLs-r3x4`  
**Documento narrativo:** `1cfauL4H1W09McoqxyyQ_BIRXwgfrmrbRAAZ9rku1vM8`

## 1. População por estratos de renda

A expressão "classe social" foi reformulada para **classes oficiais de rendimento domiciliar per capita do Censo 2022** e estratos operacionais SBMI. Não foram fabricadas classes ABEP A/B/C/D/E, porque o Critério Brasil utiliza pontuação domiciliar baseada em bens, serviços, escolaridade e características do domicílio, e não uma conversão direta de renda.

Fonte canônica: IBGE, Censo Demográfico 2022, SIDRA tabela 10296, São Borja. Universo compatível: **59.038 pessoas**.

### Faixas oficiais observadas

- Sem rendimento: 1.488 — 2,52%.
- Até 1/4 SM: 2.441 — 4,13%.
- Mais de 1/4 a 1/2 SM: 10.917 — 18,49%.
- Mais de 1/2 a 1 SM: 20.174 — 34,17%.
- Mais de 1 a 2 SM: 15.630 — 26,47%.
- Mais de 2 a 3 SM: 4.659 — 7,89%.
- Mais de 3 a 5 SM: 2.086 — 3,53%.
- Mais de 5 a 10 SM: 1.237 — 2,10%.
- Mais de 10 a 15 SM: 286 — 0,48%.
- Mais de 15 a 20 SM: 33 — 0,06%.
- Mais de 20 SM: 87 — 0,15%.

### Agregações calculadas pelo SBMI

- Sem rendimento ou até 1 SM: **35.020 pessoas — 59,32%**.
- Sem rendimento ou até 2 SM: **50.650 — 85,79%**.
- Acima de 2 SM: **8.388 — 14,21%**.
- Acima de 5 SM: **1.643 — 2,78%**.

Estratos operacionais para leitura mercadológica:

- sem renda ou até 1/2 SM: 25,15%;
- >1/2 a 1 SM: 34,17%;
- >1 a 2 SM: 26,47%;
- >2 a 5 SM: 11,42%;
- >5 SM: 2,78%.

Controle conceitual: rendimento domiciliar per capita não mede patrimônio, acesso a crédito ou classe econômica ABEP.

## 2. Emprego formal × VAB no mesmo ano

A v023 substitui como referência canônica o contraste adjacente 2021×2022 da v022 por **RAIS 2021 × VAB 2021**.

Dados observados — RAIS 2021, São Borja:

- Agropecuária: 1.416 vínculos — 12,41%.
- Indústria: 1.139 — 9,99%.
- Construção: 929 — 8,14%.
- Comércio: 3.117 — 27,33%.
- Serviços: 4.805 — 42,13%.
- Total dos cinco grupamentos: 11.406 vínculos.

Comparação calculada com o VAB 2021:

- agro: 12,41% do emprego vs. 33,87% do VAB = **−21,46 p.p.**;
- indústria + construção: 18,13% do emprego vs. 11,67% do VAB industrial = **+6,46 p.p.**;
- comércio + serviços: 69,45% do emprego vs. 54,46% do terciário amplo = **+15,00 p.p.**.

Interpretação: o agro é âncora de geração de valor; comércio e serviços são âncoras predominantes do emprego formal e da circulação cotidiana de remunerações.

Limitação: mesmo no mesmo ano, RAIS e VAB não têm universos setoriais perfeitamente equivalentes. O resultado não é produtividade por trabalhador.

## 3. Folha pública federal e estadual — auditoria RAIS 2025

Foi executado pipeline auditável sobre os microdados RAIS 2025/MTE-PDET, com vínculo ativo em 31/12, não abandonado, classificação por natureza jurídica e dois critérios territoriais.

### Município do trabalho

- Federal: **3 vínculos**; 1 remuneração de dezembro válida; massa observada **R$ 797,00**.
- Estadual: **0 vínculos recuperados**.

### Município do estabelecimento

- Federal: **10 vínculos**; massa de dezembro **R$ 106.622,31**.
- Estadual: **0 vínculos recuperados**.
- Empresa Pública/Sociedade de Economia Mista, esfera controladora não identificável só pela natureza: **58 vínculos**; massa de dezembro **R$ 546.572,19**.
- Municipal, usado apenas como controle: **2.322 vínculos**, 2.171 remunerações válidas; massa de dezembro **R$ 10.078.416,56**.

### Decisão metodológica

Os resultados federal/estadual são **fragmentos observados**, não totais territoriais. Eles são incompatíveis com a presença institucional oficialmente verificável em São Borja e demonstram subcobertura/cadastro centralizado para o objetivo proposto.

Portanto, a RAIS não será usada como estimativa final da folha pública federal+estadual. Ela permanece como fonte de controle e diagnóstico de cobertura.

## 4. Nova metodologia — instituição × unidade de exercício × portal de transparência

Inventário inicial de presenças oficiais verificadas:

### Federal

- Universidade Federal do Pampa — Campus São Borja.
- Instituto Federal Farroupilha — Campus São Borja.
- 2º Regimento de Cavalaria Mecanizado.
- Delegacia da Polícia Federal em São Borja.
- Unidade Operacional da Polícia Rodoviária Federal.
- Inspetoria da Receita Federal.

O IFFar informa, na página do Campus São Borja consultada, **61 docentes efetivos, 53 técnicos-administrativos efetivos e 9 docentes substitutos**. Terceirizados e estagiários permanecem fora da folha de servidores até classificação adequada.

### Estadual

- Brigada Militar — 2º BPAF.
- Brigada Militar — 3º BABM.
- Polícia Civil — DPPA de São Borja.
- Ministério Público do RS — unidades de São Borja.
- Defensoria Pública do Estado — São Borja.

O inventário não é exaustivo. Ainda devem ser mapeados Judiciário, IGP, educação estadual, saúde estadual, SUSEPE e demais estruturas com pessoal efetivamente lotado/exercendo no município.

Indicador-alvo: **massa mensal bruta de remuneração dos vínculos federais e estaduais com exercício/lotação em São Borja**.

Limitações futuras a preservar: folha bruta ≠ renda líquida; local de exercício ≠ residência; remuneração ≠ gasto local; não somar automaticamente a INSS, Bolsa Família ou massa empresarial.

## 5. Aprofundamento da retenção financeira do agro

Fontes oficiais identificadas:

### Banco Central — ESTBAN

Permite observar saldos bancários por município, incluindo depósitos, crédito e contas selecionadas do balancete. Uso pretendido: acompanhar escala da intermediação financeira local e razões entre crédito e depósitos ao longo do tempo.

Limitação: não identifica origem setorial dos depósitos, residência econômica do titular ou lucro agropecuário.

### Banco Central — SICOR / Matriz de Dados do Crédito Rural

Permite observar operações e valores de crédito rural por município, finalidade, fonte de recursos e período. Uso: mensurar a intensidade do financiamento rural e separar crédito de renda própria.

Limitação: crédito contratado não é lucro nem retenção do excedente; o gasto financiado pode ocorrer com fornecedores externos.

### Propriedade e patrimônio

RFB/CNPJ/QSA pode apoiar controle formal da estrutura societária, mas não determina beneficiário econômico final ou local de investimento do lucro. ITBI e dados imobiliários podem ser explorados como proxies, desde que não se atribua automaticamente a origem dos recursos ao agro.

Não está autorizado criar índice sintético de retenção somando VAB, salários, depósitos, crédito e patrimônio.

## 6. Estado v023

- População por “classe social”: **concluída como estratos de renda**, sem falsa conversão ABEP.
- Emprego × VAB same-year: **canonizado para 2021**.
- Folha federal/estadual: **ainda não quantificada**; RAIS mostrou-se insuficiente como fonte final.
- Inventário institucional: **iniciado**, com instituições federais e estaduais oficialmente verificadas.
- Retenção financeira agro: **fontes oficiais ESTBAN/SICOR identificadas**, extração quantitativa é próxima etapa.
- Retenção patrimonial: **não mensurada**.

## 7. Rastreabilidade

Planilha Drive v023: `1batazM_AWCZxSfMmcxiR7CO4tl8Tk5xFx7LOLs-r3x4`.

Documento narrativo v023: `1cfauL4H1W09McoqxyyQ_BIRXwgfrmrbRAAZ9rku1vM8`.

Abas v023: `Estratos_renda_v023`, `Folha_publica_v023`, `Fontes_folha_publica_v023`, `Auditoria_v023`, `Emprego_VAB_2021_v023`, `Retencao_financeira_fontes_v023`, `Inventario_instituicoes_publicas_v023`.

PR #41 deve permanecer **aberto, draft e sem merge** até autorização explícita do usuário.
