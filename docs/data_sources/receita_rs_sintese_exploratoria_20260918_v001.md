# Receita Estadual RS — síntese exploratória integrada — 18/09/2026

**Versão:** v001  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## 1. Objetivo

Integrar, sem promoção canônica, as novas evidências documentais recebidas em 18/09/2026:

- NT CIET 05/2026 — Radar de Mercado;
- BET — resultados consolidados de agosto/2026;
- BET Comércio Exterior — ed. 07 / agosto/2026;
- Preços Dinâmicos — ed. 25 / agosto/2026;
- Volume de Vendas da Indústria de Transformação — ed. 03 / 1º trimestre de 2026.

O foco é ampliar a leitura territorial de São Borja e da Fronteira Oeste e preparar o próximo ciclo de extração do piloto do arroz.

## 2. Dados observados

### 2.1 Radar — metodologia fechada

A NT CIET 05/2026 confirma:
- base principal NFe + MDIC/Siscomex para comércio exterior;
- Regime Geral + Simples Nacional;
- NCM de 8 dígitos e setor industrial;
- atualização mensal;
- páginas Oportunidades, Mercado Nacional, Competitividade RS, Perfil de Vendas, Composição de Mercado e Dados Abertos;
- seis bases CSV públicas.

Fórmula oficial:
`Part.RS = INT / (INT + OUF + EXT)`.

Dependência:
- crítica: <5%;
- alta: 5%-15%;
- média: 15%-30%.

A NT corrente **não documenta município** como geografia do Radar.

### 2.2 Fronteira Oeste — atividade industrial em agosto/2026

BET:
- 25.218 estabelecimentos ativos na Fronteira Oeste, sem MEI;
- 607.659 no RS;
- vendas industriais da Fronteira Oeste: participação de 1,3% no RS;
- variação interanual das vendas industriais: **-5,3%**;
- RS: **-3,5%**;
- realizado vs previsto na Fronteira Oeste: **+0,8%**;
- realizado vs previsto no RS: **-8,5%**.

A tabela municipal exibida não contém São Borja.

### 2.3 Fronteira Oeste — comércio exterior e vendas

BET Comércio Exterior, acumulado set/2025-ago/2026:
- exportações da Fronteira Oeste: **US$ 322,2 milhões**, +27,43%;
- total de vendas da Fronteira Oeste: **US$ 5.673,1 milhões**, +12,84%;
- RS, tabela de COREDES: exportações US$ 24.044,9 milhões, +2,89%;
- vendas US$ 242.300,2 milhões, +14,24%.

Contexto de produtos:
- Cereais e Grãos (exceto soja), exportações: **US$ 1.278,5 milhões**, +7,3%;
- importações: **US$ 227,2 milhões**, -32,5%.

Contexto industrial:
- AGRO: US$ 12.031,6 milhões exportados, +18,98%;
- ALIMENTOS: US$ 982,4 milhões, +9,81%.

### 2.4 Preços de alimentos — Fronteira Oeste

Agosto/2026:
- PCA-RE Fronteira Oeste: **R$ 284,19**;
- PCA-RE RS: **R$ 298,61**;
- ICA-RE 12m médio Fronteira Oeste: **3,23%**;
- ICA-RE 12m RS: **3,49%**.

Faixas de renda — ICA-RE 12m na Fronteira Oeste:
- <2 SM: 2,23%;
- 2-3 SM: 1,94%;
- 3-6 SM: 2,26%;
- 6-10 SM: 2,73%;
- 10-15 SM: 2,64%;
- 15-25 SM: 3,84%;
- >25 SM: 4,29%.

Hortaliças:
- Fronteira Oeste: R$ 5,58; +18,69% em 12m;
- RS: R$ 6,50; +22,45%.

Cebola:
- Fronteira Oeste: R$ 5,43; +101,93% em 12m;
- RS: R$ 5,99; +102,89%.

### 2.5 Indústria de alimentos — RS

1º trimestre/2026:
- indústria de transformação: +1,9%;
- produtos alimentícios: +6,5%;
- alimentos — interno RS: +5,0%;
- alimentos — OUF: +1,4%;
- alimentos — exterior: +20,5%.

Agosto/2026:
- indústria total: -3,5% interanual;
- alimentos: +1,3%.

## 3. Dados calculados

### 3.1 PCA-RE Fronteira Oeste vs RS

`(284,19 / 298,61 - 1) × 100 = -4,83%`

O nível do PCA-RE da Fronteira Oeste ficou 4,83% abaixo da média estadual em agosto/2026.

### 3.2 ICA-RE médio

`3,23 - 3,49 = -0,26 p.p.`

A inflação alimentar média em 12 meses na Fronteira Oeste ficou 0,26 p.p. abaixo da média estadual.

### 3.3 Intensidade exportadora calculada

Fronteira Oeste:

`322,2 / 5.673,1 × 100 = 5,68%`

RS:

`24.044,9 / 242.300,2 × 100 = 9,92%`

Diferença:

`5,68 - 9,92 = -4,24 p.p.`

Esse indicador é cálculo SBMI, não KPI oficial do BET.

### 3.4 Desempenho industrial regional

`-5,3 - (-3,5) = -1,8 p.p.`

A retração industrial da Fronteira Oeste em agosto foi 1,8 p.p. mais intensa que a média estadual.

### 3.5 Alimentos vs indústria

1º trimestre:

`6,5 - 1,9 = +4,6 p.p.`

Agosto:

`1,3 - (-3,5) = +4,8 p.p.`

Em dois recortes temporais distintos, produtos alimentícios apresentaram desempenho relativo superior à indústria agregada.

## 4. Interpretações

### 4.1 Cadeia do arroz deve ser tratada como cadeia instalada, não como oportunidade de entrada

A capacidade local já auditada em São Borja — produção primária, beneficiamento, emprego formal e operadores — combinada com a metodologia agora conhecida do Radar desloca a pergunta de:

> “há mercado para instalar esta atividade?”

para:

> “qual parcela do mercado gaúcho é atendida pelo RS, qual a dependência de OUF/EXT e como a capacidade de São Borja pode ampliar participação, destinos e valor agregado?”

### 4.2 Há sinais simultâneos de fraqueza industrial regional e expansão externa

Fatos:
- vendas industriais da Fronteira Oeste: -5,3% em agosto;
- exportações da região: +27,43% nos últimos 12 meses;
- vendas totais: +12,84%.

Interpretação:
os indicadores apontam cadências diferentes entre o pulso industrial mensal e a inserção comercial externa anualizada.

**Não é possível concluir causalidade** nem afirmar que exportações compensaram a retração industrial sem decomposição setorial e temporal compatível.

### 4.3 A Fronteira Oeste exporta menos intensamente que o RS, apesar de crescer mais rápido

O crescimento das exportações regionais foi elevado, mas a razão exportações/vendas calculada foi 5,68%, contra 9,92% no RS.

Interpretação:
há espaço para investigar se cadeias já instaladas — especialmente agroindustriais — possuem potencial de aprofundar sua inserção fora da região/estado.

Isso é uma hipótese de investigação, não uma meta ou prova de capacidade ociosa.

### 4.4 Alimentos mostram resiliência relativa no contexto estadual

Produtos alimentícios cresceram 6,5% no 1º trimestre de 2026, frente a 1,9% da indústria total, e +1,3% em agosto, quando a indústria total recuou 3,5%.

Interpretação:
o ambiente estadual recente é relativamente favorável ao setor de alimentos em comparação com a indústria agregada.

Para São Borja, isso fortalece a relevância analítica das cadeias de processamento de alimentos, mas não comprova desempenho local.

### 4.5 Pressão de preços alimentares regional abaixo da média estadual, com heterogeneidade por renda

PCA-RE e ICA-RE médios da Fronteira Oeste ficaram abaixo dos valores estaduais.

Entretanto, as faixas de 15-25 SM e >25 SM registraram ICA-RE de 3,84% e 4,29%, acima da média regional e, no caso de >25 SM, também acima do RS.

Interpretação:
a exposição à inflação alimentar não é uniforme por faixa de renda.

Limite:
as faixas derivam da ponderação da POF e não representam a distribuição de renda corrente de São Borja.

## 5. Implicações para o piloto do arroz

A próxima extração decisiva deve preencher, para os sete NCMs:

`NCM → INT → OUF → EXT → Part.RS → dependência → UFs fornecedoras → destinos OUF → países origem/destino`

Prioridade de bases:
1. Composição de Mercado;
2. Exportações por NCM;
3. Importações por NCM;
4. Categorias de Produtos;
5. Portfólio NCM por Setor;
6. Saídas por Setor.

A NT indica que essas bases estão disponíveis em CSV. O principal bloqueio remanescente não é metodológico, mas **obter os arquivos brutos da página Dados Abertos**.

## 6. Recomendações exploratórias

1. **Radar/NCM arroz — prioridade máxima:** baixar os CSVs e executar o filtro dos sete NCMs.
2. **Fronteira Oeste — construir painel de pulso regional:** vendas industriais, exportações, PCA/ICA e emprego em janelas compatíveis.
3. **Arroz — separar três mercados:** mercado interno do RS, mercado interestadual e mercado externo.
4. **Valor agregado local:** depois de dimensionar fluxos, investigar produtos derivados, marcas, embalagem, distribuição e destinos das beneficiadoras locais.
5. **Consumidor regional:** usar preços e renda apenas como contexto; não converter indicadores COREDE em comportamento municipal sem dado adicional.

## 7. Limitações

- Radar: valores dos sete NCMs ainda não extraídos dos CSVs/painel.
- BET municipal: São Borja não aparece no quadro municipal da edição recebida.
- Preços Dinâmicos: publicação pública é COREDE, não município.
- BET Comex: categoria “Cereais e Grãos (exceto soja)” é mais ampla que arroz.
- Todos os novos resultados permanecem exploratórios e não canônicos.
