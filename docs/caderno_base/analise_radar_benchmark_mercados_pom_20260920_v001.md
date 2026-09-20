# Radar do Mercado — benchmark estadual para os mercados POM — ago/2026 — v001

**Data:** 20/09/2026  
**Competência focal:** agosto/2026  
**Série auditada disponível:** julho/2024 a agosto/2026  
**Geografia:** Rio Grande do Sul  
**Fonte:** Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos  
**Taxonomia:** grupos de afinidade, snapshot 2026-08  
**Unidade monetária:** R$ nominais publicados pela fonte  
**Status:** benchmark estadual setorial, apto à inclusão como contexto; não é indicador municipal.

## 1. Regra metodológica

O Radar decompõe o mercado do RS, por produto/NCM, em:

- `INT`: origem interna do Rio Grande do Sul;
- `OUF`: origem em outras unidades da federação;
- `EXT`: origem exterior.

Cálculo:

`Part.RS = INT / (INT + OUF + EXT)`.

Faixas documentadas na NT CIET 05/2026:

- **CRÍTICA:** Part.RS < 5%;
- **ALTA:** 5% a <15%;
- **MÉDIA:** 15% a <30%.

Valores superiores a 30% recebem no SBMI apenas o marcador técnico `FORA_DAS_FAIXAS_NT`. Não se cria uma quarta categoria oficial.

## 2. Controle territorial

Todos os valores deste bloco são **estaduais**.

Eles não significam:
- demanda de São Borja;
- market share de empresas locais;
- vazamento de renda municipal;
- origem dos fornecedores efetivamente utilizados pelos estabelecimentos locais.

A aplicação ao projeto é:

`estrutura estadual de abastecimento → contexto de cadeia → teste posterior de aderência territorial`.

## 3. Bens essenciais — heterogeneidade de abastecimento

Competência ago/2026:

| Grupo de afinidade | Mercado RS nominal | Part.RS | Origem externa ao RS | Faixa NT |
|---|---:|---:|---:|---|
| Café | R$ 179,35 mi | 0,45% | 99,55% | CRÍTICA |
| Frutas e Hortícolas | R$ 416,56 mi | 6,42% | 93,58% | ALTA |
| Preparações Alimentícias Diversas | R$ 253,15 mi | 11,06% | 88,94% | ALTA |
| Cereais e Grãos, exceto soja | R$ 800,70 mi | 18,00% | 82,00% | MÉDIA |
| Massas e Panificação | R$ 649,16 mi | 45,84% | 54,16% | fora das faixas NT |
| Laticínios | R$ 824,65 mi | 61,79% | 38,21% | fora das faixas NT |
| Carnes de Bovinos | R$ 1,362 bi | 60,55% | 39,45% | fora das faixas NT |
| Carnes de Frango | R$ 458,13 mi | 65,39% | 34,61% | fora das faixas NT |
| Óleos e Gorduras | R$ 441,92 mi | 46,07% | 53,93% | fora das faixas NT |
| Ovos | R$ 36,49 mi | 34,86% | 65,14% | fora das faixas NT |

### Interpretação

O abastecimento de bens essenciais não forma uma única cadeia.

Café, frutas/hortícolas e preparações alimentícias apresentam forte dependência de origem externa ao RS, enquanto carnes, laticínios e panificação possuem participação interna muito maior.

Para o caderno de Bens Essenciais, isso é mais informativo do que uma média setorial única.

## 4. Saúde, higiene e cuidados pessoais

| Grupo | Mercado RS nominal | Part.RS | Origem externa ao RS | Faixa NT |
|---|---:|---:|---:|---|
| Medicamentos | R$ 1,677 bi | 0,67% | 99,33% | CRÍTICA |
| Vacinas e Soros | R$ 767,61 mi | 0,15% | 99,85% | CRÍTICA |
| Instrumentos Médicos | R$ 372,53 mi | 4,26% | 95,74% | CRÍTICA |
| Produtos Farmacêuticos | R$ 99,42 mi | 1,32% | 98,68% | CRÍTICA |
| Perfumaria e Cosméticos | R$ 581,26 mi | 6,27% | 93,73% | ALTA |

### Interpretação

A cadeia estadual de saúde/higiene apresenta exposição externa muito elevada nos grupos selecionados.

Isso ajuda a contextualizar:
- dependência de distribuidores/fabricantes de fora do RS;
- sensibilidade potencial a logística e prazo;
- necessidade de separar oferta varejista local da origem industrial dos produtos.

Não autoriza afirmar que uma farmácia ou perfumaria de São Borja compra diretamente de fora do RS.

## 5. Bens não essenciais

| Grupo | Mercado RS nominal | Part.RS | Origem externa ao RS | Faixa NT |
|---|---:|---:|---:|---|
| Eletrodomésticos | R$ 819,88 mi | 15,09% | 84,91% | MÉDIA |
| Aparelhos Telefônicos | R$ 435,88 mi | 0,60% | 99,40% | CRÍTICA |
| Eletrônicos — Informática/TIC | R$ 350,53 mi | 1,12% | 98,88% | CRÍTICA |
| Eletrônicos — Comunicação/Imagem | R$ 192,55 mi | 1,04% | 98,96% | CRÍTICA |
| Eletrônicos — Áudio/Vídeo | R$ 128,08 mi | 2,65% | 97,35% | CRÍTICA |
| Brinquedos/Jogos/Lazer | R$ 235,26 mi | 4,35% | 95,65% | CRÍTICA |
| Vestuário Tecido | R$ 409,27 mi | 11,72% | 88,28% | ALTA |
| Vestuário de Malha | R$ 558,22 mi | 13,93% | 86,07% | ALTA |
| Mobiliário e Iluminação | R$ 967,14 mi | 52,24% | 47,76% | fora das faixas NT |
| Calçados | R$ 827,35 mi | 53,69% | 46,31% | fora das faixas NT |

### Interpretação

O contexto estadual de bens não essenciais é fortemente assimétrico.

Eletrônicos, telefonia, lazer e vestuário dependem muito mais de oferta originada fora do RS do que mobiliário e calçados.

Isso qualifica a análise da competição local/digital, mas não mede evasão de consumo de São Borja.

## 6. Tendência de mesmo período

A série já auditada permite comparar jan–ago/2025 com jan–ago/2026 sem misturar ano parcial e ano completo.

Achados selecionados:

### Saúde
- Medicamentos: Part.RS 0,69% → 0,66%;
- Instrumentos Médicos: 5,19% → 5,01%;
- Perfumaria/Cosméticos: 5,25% → 5,31%.

A exposição externa permanece estruturalmente elevada.

### Não essenciais
- Telefones: 0,53% → 0,58%;
- Informática/TIC: 2,38% → 1,36%;
- Brinquedos/Jogos/Lazer: 6,59% → 4,59%;
- Vestuário Tecido: 11,91% → 11,66%;
- Vestuário Malha: 13,08% → 15,66%.

### Essenciais
- Café: 0,67% → 0,46%;
- Frutas/Hortícolas: 6,89% → 7,51%;
- Preparações Alimentícias: 10,45% → 10,91%;
- Cereais/Grãos: 30,58% → 29,27%;
- Massas/Panificação: 44,44% → 45,93%;
- Laticínios: 64,70% → 64,03%.

### Limitação temporal

A variação do valor nominal `INT+OUF+EXT` mistura preço, quantidade e composição.

Não deve ser interpretada como crescimento real da demanda física.

## 7. Sensibilidade à taxonomia

O Radar contém taxonomias distintas.

Exemplo já auditado:

- afinidade `Tratores`: 13 NCMs, Part.RS 0,50% em ago/2026;
- Portfólio `TRATORES`: 7 NCMs, Part.RS 40,54%.

O arroz apresenta o mesmo problema de cesta:
- Cereais e Grãos: 42 NCMs, 18,00%;
- Portfólio ARROZ: 4 NCMs, 76,47%;
- cesta SBMI arroz: 7 NCMs, 64,39%.

### Regra editorial

Não existe um único indicador de “dependência” de uma cadeia sem:
- taxonomia;
- lista de NCMs;
- período;
- regra de inclusão.

## 8. Uso nos cadernos

### Bens Essenciais
Usar o Radar para demonstrar heterogeneidade de origem de abastecimento entre famílias de produtos.

### Saúde/Higiene
Usar como benchmark estadual de forte dependência externa em fármacos, instrumentos e cosméticos.

### Bens Não Essenciais
Usar para diferenciar bens com forte exposição externa, como eletrônicos e vestuário, de cadeias com maior produção interna.

### Serviços/Alimentação fora do lar
Os grupos alimentares podem ser utilizados apenas como contexto upstream de insumos do foodservice. O Radar não mede serviços.

## 9. Artefatos

- `docs/data_sources/radar_pom_benchmark_20260920_v001.csv`;
- `docs/caderno_base/nota_analitica_radar_dependencia_taxonomias_2026_08.md`;
- `docs/data_sources/radar_taxonomy_series_2024_07_2026_08/`;
- `docs/data_sources/radar_open_data_history_2024_07_2026_08/`.

## 10. Status de promoção

**PROMOVER COMO BENCHMARK ESTADUAL**, nunca como dado municipal.

O Caderno-Base deve receber a metodologia e a leitura transversal de dependência/origem; os cadernos setoriais devem receber apenas os grupos aderentes ao seu escopo.

## 11. Governança

- Caderno-Base v028 permanece read-only;
- inclusão apenas no sucessor;
- PR #41 permanece aberto, draft e sem merge.
