# Caderno-Base Territorial — v026

**Data:** 2026-09-12  
**Escopo:** agro × financiamento × preços/produção e folha pública dos demais poderes  
**Geografia principal:** São Borja/RS  
**Governança:** PR #41 deve permanecer **aberto, draft e sem merge** até autorização explícita.

## Artefatos canônicos no Drive

- Planilha técnica v026: `1taW8Ha_FSyGWNKYd3aPMjESpEcBhsF7-GJj17s5tBD4`
- Caderno narrativo v026: `1xCGpLs4K4-Dv520uz3wa9A82h7YeczeMpM5liuVikSo`
- Registro metodológico v026: `1fLFJLHaKn1wJUlDHuE-tTNUWxa4P2DP-YV8yTp2Xq9s`
- Arquivo bruto PAM/SIDRA preservado: `17wXDK_ZRHScJkiRhfRLbtEReqs_FmsJq` — **Área plantada e colhida SB original.xlsx**

Novas abas da planilha:

- `Agro_preco_producao_v026`
- `DPERS_folha_auditoria_v026`
- `TJRS_folha_auditoria_v026`
- `Auditoria_v026`

## 1. Objeto

A v026 retoma o cruzamento aberto na v025 entre:

1. SICOR — fluxo de crédito rural;
2. ESTBAN — saldos bancários por município;
3. VAB agropecuário — valor adicionado;
4. PAM/SIDRA 5457 — quantidade, área, rendimento e valor da produção;
5. choques climáticos/sanitários já registrados nas versões anteriores.

Depois, avança na territorialização da folha pública dos demais poderes/instituições estaduais, começando por DPERS e TJRS.

## 2. Auditoria conceitual

Os conceitos **não são intercambiáveis**:

| Indicador | Natureza | Unidade/estoque-fluxo | Regra de uso |
|---|---|---|---|
| SICOR | crédito rural contratado | R$; fluxo | intensidade/escala do financiamento |
| ESTBAN | contas bancárias municipais | R$; saldo de fim de mês | estrutura contábil bancária |
| VAB agropecuário | valor adicionado | R$ correntes | geração de valor setorial |
| PAM — valor da produção | valor bruto corrente da produção | mil R$ | escala monetária bruta da produção |
| PAM — rendimento | produtividade física | kg/ha | produção física por área |

**Controle:** não somar esses indicadores nem interpretar razões entre eles como dívida, lucro, patrimônio, retenção financeira ou causalidade.

## 3. PAM/SIDRA — dados observados

**Fonte:** IBGE, Produção Agrícola Municipal, SIDRA tabela 5457.  
**Período:** 2019–2024.  
**Geografia:** São Borja/RS.  
**Culturas selecionadas:** arroz, soja, milho e trigo.

### Quantidade produzida — toneladas

| Ano | Arroz | Soja | Milho | Trigo |
|---:|---:|---:|---:|---:|
| 2019 | 288.852 | 157.400 | 38.000 | 35.100 |
| 2020 | 312.887 | 138.000 | 48.000 | 24.000 |
| 2021 | 306.400 | 156.000 | 36.000 | 54.000 |
| 2022 | 267.114 | 82.500 | 45.600 | 75.000 |
| 2023 | 259.613 | 129.600 | 70.200 | 45.000 |
| 2024 | 236.977 | 267.000 | 96.000 | 72.000 |

### Valor da produção — mil R$ correntes

| Ano | Arroz | Soja | Milho | Trigo |
|---:|---:|---:|---:|---:|
| 2019 | 242.636 | 165.270 | 19.304 | 21.622 |
| 2020 | 306.864 | 219.063 | 33.600 | 37.440 |
| 2021 | 496.981 | 421.200 | 45.360 | 71.820 |
| 2022 | 388.050 | 250.767 | 69.768 | 113.250 |
| 2023 | 437.708 | 265.680 | 93.577 | 41.580 |
| 2024 | 483.400 | 516.111 | 76.800 | 77.155 |

### Área colhida — hectares

| Ano | Arroz | Soja | Milho | Trigo |
|---:|---:|---:|---:|---:|
| 2019 | 38.406 | 57.000 | 5.000 | 13.000 |
| 2020 | 37.584 | 70.000 | 6.000 | 16.000 |
| 2021 | 38.300 | 70.000 | 4.000 | 20.000 |
| 2022 | 31.822 | 85.000 | 10.000 | 25.000 |
| 2023 | 28.124 | 98.000 | 15.000 | 30.000 |
| 2024 | 29.152 | 105.000 | 15.000 | 30.000 |

## 4. Dados calculados

### 4.1 Preço implícito da produção

Fórmula:

[
P_{implícito} = rac{Valor\ da\ produção\ (mil\ R\$) \times 1.000}{Quantidade\ produzida\ (t)}
]

**Natureza:** DADO CALCULADO.  
**Limitação:** média derivada da PAM; **não é cotação de mercado**, preço contratual nem preço individual recebido por produtor.

| Ano | Arroz R$/t | Soja R$/t | Milho R$/t | Trigo R$/t |
|---:|---:|---:|---:|---:|
| 2019 | 840,00 | 1.050,00 | 508,00 | 616,01 |
| 2020 | 980,75 | 1.587,41 | 700,00 | 1.560,00 |
| 2021 | 1.622,00 | 2.700,00 | 1.260,00 | 1.330,00 |
| 2022 | 1.452,75 | 3.039,60 | 1.530,00 | 1.510,00 |
| 2023 | 1.686,00 | 2.050,00 | 1.333,01 | 924,00 |
| 2024 | 2.039,86 | 1.933,00 | 800,00 | 1.071,60 |

### 4.2 Valor bruto agregado das quatro culturas

| Ano | Valor bruto | Variação nominal a/a |
|---:|---:|---:|
| 2019 | R$ 448,832 mi | — |
| 2020 | R$ 596,967 mi | +33,00% |
| 2021 | R$ 1,035 bi | +73,44% |
| 2022 | R$ 821,835 mi | −20,62% |
| 2023 | R$ 838,545 mi | +2,03% |
| 2024 | R$ 1,153 bi | +37,56% |

**Controle:** valor bruto da produção **não é VAB** e pode superar o VAB agropecuário.

### 4.3 Escala SICOR × valor bruto

| Ano | SICOR nominal | SICOR real-proxy ago/2026 | Valor bruto 4 culturas | SICOR / valor bruto |
|---:|---:|---:|---:|---:|
| 2019 | R$ 335,627 mi | R$ 490,170 mi | R$ 448,832 mi | 74,78% |
| 2020 | R$ 347,868 mi | R$ 493,290 mi | R$ 596,967 mi | 58,27% |
| 2021 | R$ 624,046 mi | R$ 814,843 mi | R$ 1,035 bi | 60,27% |
| 2022 | R$ 799,109 mi | R$ 953,739 mi | R$ 821,835 mi | 97,23% |
| 2023 | R$ 896,439 mi | R$ 1,026 bi | R$ 838,545 mi | 106,90% |
| 2024 | R$ 723,888 mi | R$ 793,268 mi | R$ 1,153 bi | 62,76% |

A razão é somente uma comparação de **escala financeira/econômica**. O universo do SICOR não coincide perfeitamente com as quatro culturas.

## 5. Cruzamento com VAB agropecuário

VAB agro canonizado no projeto:

| Ano | VAB agro | SICOR/VAB | valor bruto 4 culturas/VAB |
|---:|---:|---:|---:|
| 2019 | R$ 316,131 mi | 106,17% | 141,98% |
| 2020 | R$ 405,902 mi | 85,70% | 147,07% |
| 2021 | R$ 795,875 mi | 78,41% | 130,09% |

**Controle:** razão superior a 100% não significa inconsistência. O numerador e denominador possuem conceitos diferentes.

## 6. Interpretação dos choques

### 2020

**Dados observados:** queda da produtividade de soja e trigo; comportamento físico distinto para arroz e milho.  
**Dados calculados:** os preços implícitos aumentaram nas quatro culturas.

**Interpretação:** a expansão nominal do VAB agro não pode ser atribuída a uma melhora física generalizada. Preços, composição, área e quantidade precisam ser separados.

### 2021

O VAB agro passou de R$ 405,902 mi para R$ 795,875 mi. O SICOR real-proxy cresceu 65,19%. No mesmo intervalo, os preços implícitos subiram 65,38% no arroz, 70,09% na soja e 80,00% no milho.

**Interpretação:** movimento compatível com ciclo muito favorável ao agro; **não prova direção causal** entre crédito e VAB.

### 2022–2023

Em 2022, a soja caiu a 971 kg/ha; em 2023 recuperou para 1.322 kg/ha, ainda muito abaixo de 2019. Mesmo assim, o SICOR real-proxy cresceu 17,05% em 2022 e mais 7,62% em 2023, quando atingiu o pico de R$ 1,026 bi.

### 2024

Quantidade produzida frente a 2023:

- soja: **+106,02%**;
- milho: **+36,75%**;
- trigo: **+60,00%**.

Valor bruto das quatro culturas: **+37,56%**.  
SICOR real-proxy: **−22,72%**.

**Diagnóstico:** os ciclos creditício, físico e monetário podem divergir fortemente no mesmo ano. A base rejeita explicações mecânicas contemporâneas, mas não identifica causalidade nem defasagem temporal específica.

## 7. ESTBAN

A conclusão da v025 permanece válida:

- o financiamento rural agrícola representou entre **47,64% e 55,55%** das operações de crédito bancário no recorte de junho de 2021–2026;
- o agro é uma âncora persistente da intermediação financeira local;
- a queda real-proxy de poupança e depósitos a prazo **não permite inferir fuga de capital**, porque a fonte não identifica origem setorial nem destino econômico final.

A hipótese de retenção/vazamento patrimonial do excedente agropecuário segue **NÃO VERIFICADA**.

## 8. Folha pública — DPERS

**Fonte:** Defensoria Pública do Estado do Rio Grande do Sul — Portal da Transparência.  
**Competência:** julho/2026.

Arquivos auditados:

| Arquivo | Linhas | Campo territorial | “São Borja” nas linhas |
|---|---:|---|---:|
| servidores ativos | 881 | não | 0 |
| defensores ativos | 449 | não | 0 |

A folha é estruturada e permite auditar componentes remuneratórios, mas não possui comarca, lotação, município, unidade ou sede.

Atos oficiais complementares confirmam unidades e movimentações em São Borja, porém o quadro mensal é dinâmico: há afastamento, vaga na 3ª Defensoria e designações temporárias por acumulação.

**Status:** **BLOQUEADO PARA PROMOÇÃO COMO TOTAL MENSAL**.

**Não é possível concluir:** número total de vínculos ou massa salarial DPERS efetivamente territorializável em São Borja em jul/2026.

**Dados faltantes:** roster mensal completo por unidade/exercício e regra documental para afastamentos, acumulações e designações parciais.

## 9. Folha pública — TJRS

Fontes oficiais confirmadas:

- Folha de Pagamento de Pessoal Consolidada do TJRS;
- API de Dados Abertos / Swagger oficial.

O runner GitHub do projeto sofreu timeout ao consultar as rotas da aplicação Swagger. A existência da API está confirmada, mas o schema remuneratório ainda não foi demonstrado quanto a comarca, foro, lotação ou unidade.

**Status:** **EM AUDITORIA — nenhum valor territorial promovido**.

**Critério de promoção:**

1. campo territorial explícito na própria fonte remuneratória; **ou**
2. roster oficial mensal reconciliável de forma reproduzível com a folha nominal.

Não inferir lotação por cargo, nome, notícia ou atuação processual isolada.

## 10. Próxima fila técnica

1. DPERS — obter/reconstruir roster mensal completo de jul/2026 e reconciliar com os CSVs oficiais.
2. TJRS — extrair schema Swagger por rota alternativa; testar filtros de unidade/comarca/foro.
3. Se a API não territorializar, procurar roster oficial mensal do Foro/Comarca de São Borja e fazer crosswalk documental.
4. Depois, verificar presença territorial material de TCE-RS e ALRS antes de tentar quantificação.
5. Preservar resultados negativos de auditoria; “não territorializável com segurança” é um resultado, não uma lacuna a preencher por inferência.

## 11. Governança

- PR #41: **ABERTO**
- estado: **DRAFT**
- branch: `feature/cnpj-territorial-control-v1`
- merge: **PROIBIDO sem autorização explícita do usuário**
