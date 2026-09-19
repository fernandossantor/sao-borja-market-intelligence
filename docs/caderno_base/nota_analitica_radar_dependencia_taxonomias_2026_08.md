# Nota analítica — Radar do Mercado: dependência estadual, taxonomias e sensibilidade de cesta — ago/2026

## 1. Objeto

Esta nota transforma a ingestão do **Radar do Mercado da Receita Estadual/SEFAZ-RS** em leitura mercadológica controlada para o projeto São Borja — Inteligência Mercadológica.

A pergunta é: **quais grupos de produtos e setores industriais apresentam baixa participação de origem interna do Rio Grande do Sul no valor nominal observado pelo Radar, e como a escolha da taxonomia altera essa leitura?**

A análise é estadual. Ela **não mede demanda, market share, retenção ou vazamento de São Borja**.

## 2. Fonte, período, unidade e abrangência

- Fonte: Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos.
- Competência focal: agosto/2026.
- Série auditada: julho/2024 a agosto/2026, 26 competências.
- Abrangência: Rio Grande do Sul.
- Arquivos oficiais: `Composicao_de_Mercado_MM_AAAA.csv`, `Categorias_Produtos.csv` e `Portfolio_NCMs_Setor.csv`.
- Taxonomia aplicada à série: snapshot corrente 2026-08.
- Campo monetário: `vlr_nominal`, em valores nominais publicados pela fonte.
- Componentes: INT, OUF e EXT.
- Cálculo SBMI: `Part.RS = INT / (INT + OUF + EXT)`.

Faixas expressamente documentadas na NT CIET 05/2026:

- **CRÍTICA:** Part.RS < 5%;
- **ALTA:** 5% <= Part.RS < 15%;
- **MÉDIA:** 15% <= Part.RS < 30%.

Acima de 30%, o projeto usa apenas o marcador técnico `FORA_DAS_FAIXAS_NT`; **não se cria uma categoria oficial inexistente**.

## 3. Auditoria de cobertura

### Dados observados e calculados

- 26/26 competências mensais foram baixadas e processadas.
- `Categorias_Produtos.csv`: 13.829 NCM8 únicos, distribuídos em 110 grupos de afinidade na taxonomia corrente.
- Na composição mensal, 109 grupos aparecem ao menos uma vez.
- `Portfolio_NCMs_Setor.csv`: 1.349 NCMs únicos, 49 setores e 18 classes; 48 setores aparecem na composição mensal.
- 1.348 dos 1.349 NCMs do Portfólio também estão em Categorias.
- Cobertura mínima mensal da taxonomia de afinidade:
  - por NCM: **97,9192%**;
  - por valor nominal: **99,9987395%**.
- Em ago/2026, a cobertura por valor chega a **99,9999946%**.

### Limitação metodológica

A taxonomia corrente de 2026-08 foi aplicada retrospectivamente às competências desde jul/2024. Isso produz uma série comparável sob **classificação fixa**, mas não prova que a taxonomia publicada em cada mês histórico era idêntica.

Os grupos de afinidade têm um grupo por NCM no snapshot corrente e podem ser somados quando a cobertura é considerada. Os setores do Portfólio são uma taxonomia de uso industrial na qual um mesmo NCM pode aparecer em mais de um setor; **portanto, os setores do Portfólio não são aditivos entre si**.

## 4. Resultados correntes — ago/2026

### 4.1 Saúde, higiene e cuidados pessoais

Na taxonomia de grupos de afinidade:

| Grupo oficial | NCMs observados | Valor INT+OUF+EXT (R$) | Part.RS | Faixa NT |
|---|---:|---:|---:|---|
| Medicamentos | 209 | 1.676.849.753 | 0,67% | CRÍTICA |
| Vacinas e Soros | 42 | 767.608.500 | 0,15% | CRÍTICA |
| Instrumentos Médicos | 115 | 372.533.947 | 4,26% | CRÍTICA |
| Produtos Farmacêuticos | 47 | 99.423.912 | 1,32% | CRÍTICA |
| Perfumaria e Cosméticos | 56 | 581.264.038 | 6,27% | ALTA |

No Portfólio, **MEDICAMENTOS** (19 NCMs) tem Part.RS de **3,59% — CRÍTICA**, e **COSMÉTICOS** (17 NCMs) de **11,52% — ALTA**.

**Interpretação:** o Radar sustenta, em escala estadual, elevada exposição a suprimento originado fora do RS em vários núcleos de saúde, fármacos, instrumentos e cosméticos. Isso pode ser usado como **benchmark de cadeia de suprimentos**, não como medida de vendas externas ou falta de oferta em São Borja.

### 4.2 Bens não essenciais e eletrônicos

Na taxonomia de grupos de afinidade:

| Grupo oficial | Part.RS | Faixa NT |
|---|---:|---|
| Aparelhos Telefônicos | 0,60% | CRÍTICA |
| Eletrônicos de Consumo – Informática/TIC | 1,12% | CRÍTICA |
| Eletrônicos de Consumo – Comunicação/Imagem | 1,04% | CRÍTICA |
| Eletrônicos de Consumo – Áudio/Vídeo | 2,65% | CRÍTICA |
| Brinquedos, Jogos e Artigos de Lazer | 4,35% | CRÍTICA |
| Motocicletas | 0,00% | CRÍTICA |
| Vestuário Tecido (Plano) | 11,72% | ALTA |
| Vestuário de Malha | 13,93% | ALTA |

**Interpretação:** há evidência estadual de forte dependência de origens externas ao RS em vários bens duráveis, eletrônicos, lazer e vestuário. Para São Borja, isso é relevante como contexto de cadeia e concorrência territorial/digital, mas não autoriza calcular “vazamento local” ou share de e-commerce.

### 4.3 Bens essenciais e alimentos

O quadro é heterogêneo:

| Grupo oficial | Part.RS | Faixa NT |
|---|---:|---|
| Café | 0,45% | CRÍTICA |
| Frutas e Hortícolas | 6,42% | ALTA |
| Preparações Alimentícias Diversas | 11,06% | ALTA |
| Cereais e Grãos (exceto soja) | 18,00% | MÉDIA |
| Massas e Panificação | 45,84% | FORA_DAS_FAIXAS_NT |
| Laticínios | 61,79% | FORA_DAS_FAIXAS_NT |

**Interpretação:** o mercado de essenciais não deve ser tratado como um único circuito de abastecimento. A dependência estadual varia fortemente por família de produto. Essa heterogeneidade é mais informativa para decisões de sortimento, fornecedores e riscos de suprimento do que uma média única.

### 4.4 Agro e insumos

No Portfólio:

| Setor oficial | NCMs | Part.RS | Faixa NT |
|---|---:|---:|---|
| DEFENSIVOS AGRÍCOLAS | 7 | 5,22% | ALTA |
| FERTILIZANTES | 9 | 58,64% | FORA_DAS_FAIXAS_NT |
| TRATORES | 7 | 40,54% | FORA_DAS_FAIXAS_NT |
| ARROZ | 4 | 76,47% | FORA_DAS_FAIXAS_NT |

Na taxonomia de afinidade, **Máquinas e Implementos Agrícolas** tem Part.RS de 52,24%, e **Adubos e Fertilizantes** de 60,24%.

**Interpretação:** a hipótese de forte dependência externa não pode ser aplicada uniformemente a toda a cadeia agro. Defensivos mostram baixa participação interna, enquanto fertilizantes, máquinas agrícolas e o recorte do Portfólio para arroz apresentam Part.RS superior a 30% na competência analisada.

## 5. Achado metodológico central: a cesta muda o resultado

O caso de **tratores** mostra por que a seleção de NCMs precisa ser explicitada:

- grupo de afinidade **Tratores**: 13 NCMs, Part.RS = **0,50%**, faixa CRÍTICA;
- setor de Portfólio **TRATORES**: 7 NCMs, Part.RS = **40,54%**, fora das faixas de dependência explicitadas pela NT.

Não é uma contradição da fonte. São **cestas diferentes**, produzidas por taxonomias diferentes.

O arroz mostra o mesmo princípio:

- grupo amplo **Cereais e Grãos (exceto soja)**: 42 NCMs, Part.RS = **18,00%**;
- Portfólio **ARROZ**: 4 NCMs, Part.RS = **76,47%**;
- cesta-piloto SBMI de 7 NCMs de arroz: em ago/2026, INT = R$ 135.978.913 e INT+OUF+EXT = R$ 211.185.938, logo Part.RS = **64,39%**.

Fórmula da cesta-piloto:
`135.978.913 / 211.185.938 = 0,6438824`.

**Diagnóstico metodológico:** antes de usar o Radar para um caderno setorial, a cesta deve ser definida em função da pergunta analítica e registrada com versão, lista de NCMs, regra de inclusão e taxonomia de origem. Não existe “o” indicador de dependência de uma cadeia sem essa delimitação.

## 6. Implicações mercadológicas

### Evidência utilizável

O Radar pode sustentar, como **benchmark estadual de cadeia de suprimentos**:

- alta dependência externa em medicamentos, vacinas, instrumentos médicos e várias famílias eletrônicas;
- dependência elevada em defensivos agrícolas;
- heterogeneidade substantiva entre famílias de alimentos e bens essenciais;
- necessidade de separar produto, cesta e taxonomia antes de inferir vulnerabilidade de suprimento.

### Hipóteses a testar em São Borja

Os dados estaduais tornam plausíveis, mas não provam, hipóteses como:

- varejistas locais de eletrônicos e saúde dependem de distribuidores/fabricantes de fora do RS;
- o grau de contestabilidade externa é diferente entre categorias de essenciais;
- cadeias com Part.RS estadual baixa podem apresentar maior sensibilidade logística, de prazo e de preço.

Essas hipóteses exigem dados locais de fornecedores, compras, estoque, frete ou canais antes de serem tratadas como fatos territoriais.

## 7. Próxima etapa

1. Selecionar, para cada caderno, as cestas com base nas taxonomias oficiais e na pergunta mercadológica.
2. Preservar simultaneamente:
   - grupo de afinidade;
   - Portfólio setorial;
   - cesta SBMI, quando necessária.
3. Calcular tendência jul/2024–ago/2026 para cada cesta selecionada.
4. Cruzar apenas conceitualmente com RFB/CNAE, RAIS e inventários locais; NCM e CNAE medem dimensões diferentes.
5. Não promover para o Caderno-Base v028, que permanece read-only.

## 8. Arquivos auditáveis

- `docs/data_sources/radar_taxonomy_inventory_2026_08/`
- `docs/data_sources/radar_taxonomy_series_2024_07_2026_08/`
- `docs/data_sources/radar_open_data_history_2024_07_2026_08/`
- `docs/data_sources/radar_open_data_current_2026_08/`


## 9. Avanço temporal comparável — jan–ago/2025 × jan–ago/2026

Para evitar comparar 2026 parcial com 2025 anual, foi calculada uma comparação de **mesmo período** usando as agregações mensais já auditadas. O valor comparado é a soma nominal `INT + OUF + EXT`; portanto, sua variação mistura preço, quantidade e composição e **não deve ser lida como crescimento real de demanda física**.

### 9.1 Grupos de afinidade — saúde, higiene e cuidados pessoais

| Grupo | Part.RS jan–ago/2025 | Part.RS jan–ago/2026 | Δ p.p. | Variação nominal INT+OUF+EXT |
|---|---:|---:|---:|---:|
| Medicamentos | 0,69% | 0,66% | -0,03 | +19,34% |
| Vacinas e Soros | 0,00% | 0,07% | +0,06 | +13,83% |
| Instrumentos Médicos | 5,19% | 5,01% | -0,18 | +8,58% |
| Produtos Farmacêuticos | 1,71% | 1,13% | -0,58 | +20,81% |
| Perfumaria e Cosméticos | 5,25% | 5,31% | +0,06 | +7,21% |

**Interpretação:** os principais núcleos de saúde permanecem em patamares muito baixos de participação interna do RS no período comparável. A mudança entre 2025 e 2026 é pequena para medicamentos, instrumentos e cosméticos e não indica redução estrutural da exposição externa.

### 9.2 Grupos de afinidade — bens não essenciais

| Grupo | Part.RS jan–ago/2025 | Part.RS jan–ago/2026 | Δ p.p. | Variação nominal INT+OUF+EXT |
|---|---:|---:|---:|---:|
| Aparelhos Telefônicos | 0,53% | 0,58% | +0,05 | +7,92% |
| Eletrônicos – Informática/TIC | 2,38% | 1,36% | -1,02 | -0,91% |
| Eletrônicos – Comunicação/Imagem | 0,96% | 0,93% | -0,03 | +9,11% |
| Eletrônicos – Áudio/Vídeo | 2,67% | 2,50% | -0,17 | -2,71% |
| Brinquedos/Jogos/Lazer | 6,59% | 4,59% | -1,99 | +15,27% |
| Motocicletas | 0,00% | 0,00% | 0,00 | +20,19% |
| Vestuário Tecido (Plano) | 11,91% | 11,66% | -0,26 | +1,54% |
| Vestuário de Malha | 13,08% | 15,66% | +2,59 | -13,34% |

**Interpretação:** a exposição externa permanece elevada na maior parte dos grupos. Vestuário de malha mostra aumento da Part.RS no agregado jan–ago, enquanto brinquedos e informática/TIC recuam. A classificação também depende do período: vestuário de malha fica em **MÉDIA** no agregado jan–ago/2026 (15,66%), embora a fotografia de ago/2026 isoladamente esteja em **ALTA** (13,93%).

### 9.3 Grupos de afinidade — bens essenciais e alimentos

| Grupo | Part.RS jan–ago/2025 | Part.RS jan–ago/2026 | Δ p.p. | Variação nominal INT+OUF+EXT |
|---|---:|---:|---:|---:|
| Café | 0,67% | 0,46% | -0,21 | +7,25% |
| Frutas e Hortícolas | 6,89% | 7,51% | +0,62 | +2,44% |
| Preparações Alimentícias Diversas | 10,45% | 10,91% | +0,46 | +0,27% |
| Cereais e Grãos (exceto soja) | 30,58% | 29,27% | -1,31 | -18,10% |
| Massas e Panificação | 44,44% | 45,93% | +1,48 | +9,29% |
| Laticínios | 64,70% | 64,03% | -0,67 | -0,91% |

**Interpretação:** permanece confirmada a heterogeneidade entre famílias. Cereais/Grãos cruza o limite de 30% entre os agregados de mesmo período, mostrando que a classificação pode mudar conforme a janela temporal; por isso, não se deve substituir a série por uma única competência.

### 9.4 Grupos de afinidade — agro

| Grupo | Part.RS jan–ago/2025 | Part.RS jan–ago/2026 | Δ p.p. | Variação nominal INT+OUF+EXT |
|---|---:|---:|---:|---:|
| Máquinas e Implementos Agrícolas | 54,71% | 49,95% | -4,76 | -18,90% |
| Adubos e Fertilizantes | 36,97% | 39,29% | +2,32 | -17,99% |
| Tratores | 0,76% | 0,88% | +0,12 | +0,45% |

### 9.5 Portfólio setorial — mesmo período

| Setor | Part.RS jan–ago/2025 | Part.RS jan–ago/2026 | Δ p.p. | Variação nominal INT+OUF+EXT |
|---|---:|---:|---:|---:|
| MEDICAMENTOS | 2,90% | 3,02% | +0,11 | +12,19% |
| COSMÉTICOS | 9,89% | 10,28% | +0,38 | +8,43% |
| DEFENSIVOS AGRÍCOLAS | 6,86% | 8,63% | +1,77 | -16,05% |
| FERTILIZANTES | 36,65% | 38,94% | +2,29 | -17,86% |
| TRATORES | 35,01% | 39,38% | +4,37 | -10,43% |
| ARROZ | 78,93% | 80,03% | +1,10 | -20,08% |
| PRODUTOS DE LIMPEZA | 32,40% | 33,41% | +1,01 | +7,13% |
| VESTUÁRIO | 29,92% | 28,60% | -1,32 | +1,14% |
| ELETROELETRÔNICO | 31,77% | 31,59% | -0,18 | -0,17% |
| ALIMENTOS | 54,10% | 54,43% | +0,33 | +6,22% |

**Achado adicional de sensibilidade:** no mesmo período jan–ago/2026, `Tratores` permanece em **0,88%** no grupo de afinidade, enquanto o Portfólio `TRATORES` registra **39,38%**. A diferença continua sendo explicada pelo universo NCM, não por inconsistência do Radar.

### 9.6 Consequência para a etapa seguinte

A etapa de tendência está **parcialmente fechada** para grupos oficiais e setores do Portfólio. Ainda falta definir as **cestas finais de cada caderno** quando a pergunta analítica exigir um recorte próprio do SBMI. A regra de promoção permanece: mesma janela temporal para comparação, cesta documentada, taxonomia explícita e nenhuma conversão de Part.RS estadual em vazamento municipal.
