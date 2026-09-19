# Nota analítica — contas públicas, VAF e conversão territorial — São Borja — 2019–2025

## 1. Objeto e finalidade

Esta nota integra duas séries oficiais já auditadas do projeto para apoiar a leitura do modelo territorial:

`entrada exógena / produção territorial → cadeia produtiva → VAB → apropriação primária → renda residente → gasto local → recirculação empresarial → saída/vazamento → resultados territoriais`.

O objetivo é responder a uma pergunta específica: **os fluxos fiscais municipais e o VAF apresentam a mesma dinâmica temporal, ou devem ser tratados como circuitos distintos na análise mercadológica?**

A nota **não** estima taxa de retenção local, multiplicador, renda domiciliar, market size nem efeito causal das transferências.

## 2. Fontes, período, unidade e abrangência

### Contas públicas

- Fonte: Tesouro Nacional / SICONFI — DCA.
- Geografia: São Borja/RS.
- Período: 2019–2025, exercícios fechados.
- Unidade: R$ correntes/nominais.
- Variáveis observadas: receita corrente bruta, transferências correntes brutas e despesa total paga.
- Arquivo auditável do projeto: `docs/data_sources/sao_borja_public_accounts_reconciled_2019_2025/fiscal_series_2019_2025.csv`.

### VAF

- Fonte: Receita Estadual/SEFAZ-RS — Valor Adicionado Municípios.
- Geografia: São Borja/RS.
- Período utilizado nesta nota: rótulos oficiais 2019–2025.
- Unidade: R$ correntes/nominais.
- Terminologia temporal preservada: **Anos de Apuração** / `ano_rotulo_fonte`.
- Série canônica: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`.

## 3. Dados observados

| Ano | Receita corrente bruta (R$ mi) | Transferências correntes brutas (R$ mi) | Transferências / receita corrente | Despesa total paga (R$ mi) | VAF publicado (R$ mi) |
|---:|---:|---:|---:|---:|---:|
| 2019 | 212,254 | 160,074 | 75,42% | 191,652 | 1.548,064 |
| 2020 | 237,825 | 186,542 | 78,44% | 204,997 | 1.844,857 |
| 2021 | 261,745 | 206,741 | 78,99% | 226,187 | 2.331,374 |
| 2022 | 308,858 | 203,615 | 65,93% | 280,509 | 2.353,301 |
| 2023 | 342,261 | 251,995 | 73,63% | 313,795 | 2.449,438 |
| 2024 | 370,103 | 279,066 | 75,40% | 350,894 | 2.907,303 |
| 2025 | 395,602 | 295,355 | 74,66% | 367,749 | 2.325,967 |

Média calculada da participação das transferências correntes brutas na receita corrente bruta, 2019–2025: **74,6361%**.

## 4. Cálculos reproduzíveis

### Variação nominal anual

`variação_t = (valor_t / valor_t-1 - 1) × 100`

### Variação acumulada 2019–2025

- receita corrente bruta: **+86,38%**;
- transferências correntes brutas: **+84,51%**;
- despesa total paga: **+91,88%**;
- VAF publicado: **+50,25%**.

### Variação nominal 2025 / 2024

- receita corrente bruta: **+6,89%**;
- transferências correntes brutas: **+5,84%**;
- despesa total paga: **+4,80%**;
- VAF publicado: **-19,9957%**.

### Relações de escala entre séries

As razões abaixo são apenas comparações dimensionais entre grandezas de conceitos distintos; **não são decomposição do VAF nem participação fiscal no VAF**.

`razão = fluxo fiscal / VAF publicado × 100`

| Ano | Receita corrente / VAF | Transferências correntes / VAF | Despesa paga / VAF |
|---:|---:|---:|---:|
| 2019 | 13,71% | 10,34% | 12,38% |
| 2020 | 12,89% | 10,11% | 11,11% |
| 2021 | 11,23% | 8,87% | 9,70% |
| 2022 | 13,12% | 8,65% | 11,92% |
| 2023 | 13,97% | 10,29% | 12,81% |
| 2024 | 12,73% | 9,60% | 12,07% |
| 2025 | 17,01% | 12,70% | 15,81% |

O salto dessas razões em 2025 resulta simultaneamente da queda do denominador VAF e do crescimento nominal dos fluxos fiscais; não deve ser lido como mudança de “participação” contábil.

## 5. Interpretação

### 5.1 Fato observado

Em 2025, o VAF publicado recuou aproximadamente **20,0% nominalmente**, enquanto receita corrente, transferências correntes e despesa paga continuaram crescendo nominalmente.

### 5.2 Interpretação

A evidência é compatível com a existência de **ritmos temporais distintos entre o circuito produtivo captado pelo VAF e o circuito fiscal municipal**. Os fluxos orçamentários municipais não acompanham mecanicamente as oscilações anuais do VAF.

Isto reforça a necessidade de analisar São Borja por circuitos econômicos articulados, e não por um único indicador-síntese. Em especial, o orçamento municipal contém forte componente de transferências intergovernamentais, que constitui entrada financeira externa ao orçamento local e pode manter execução pública elevada em momentos em que um indicador produtivo municipal recua.

### 5.3 O que não é possível concluir

Os dados não permitem afirmar que:

- transferências municipais se transformam integralmente em renda domiciliar;
- despesa pública paga permanece integralmente em São Borja;
- crescimento do gasto público compensa economicamente queda do VAF;
- transferências causam estabilização do consumo privado;
- VAF mede faturamento, renda disponível ou caixa das empresas;
- a relação fluxo fiscal / VAF seja um coeficiente econômico estrutural.

## 6. Implicação para a tese de conversão territorial

A leitura recomendada para o Caderno-Base é separar pelo menos três etapas:

1. **entrada fiscal externa:** transferências intergovernamentais recebidas pelo município;
2. **execução pública:** transformação dessas e de outras receitas em despesa paga;
3. **retenção territorial da despesa:** parcela que chega a residentes, organizações e fornecedores com capacidade de recircular localmente.

As etapas 1 e 2 têm evidência observada. A etapa 3 possui evidência parcial para 2026, mas ainda depende da reconciliação cadastral RFB e da construção histórica por credor para eventual promoção.

## 7. Diagnóstico mercadológico

**Dado observado:** o orçamento municipal possui elevada participação de transferências correntes, com média anual de 74,64% da receita corrente bruta em 2019–2025.

**Dado calculado:** entre 2019 e 2025, receita corrente, transferências e despesa paga cresceram nominalmente mais que o VAF.

**Interpretação:** o setor público municipal constitui um circuito relevante de entrada e redistribuição de recursos com dinâmica parcialmente distinta da produção territorial.

**Hipótese ainda não testada:** esse circuito pode reduzir a exposição de determinados mercados locais às oscilações de curto prazo do VAF, dependendo de quem recebe a despesa e de quanto do valor recircula no município.

## 8. Próximas análises necessárias

1. Recuperar histórico por credor 2019–2025 em fonte oficial TCE-RS/SIAPC ou equivalente.
2. Separar CNPJ e CPF preservando CPF apenas em agregado.
3. Reconciliar a classificação territorial de CNPJs com o snapshot oficial da RFB antes de promover indicadores de presença local.
4. Construir, por ano, a sequência:
   `despesa paga → CNPJ/CPF → rubrica → função → geografia cadastral do CNPJ → sensibilidades`.
5. Comparar a estabilidade dos circuitos público, agropecuário, comercial e de serviços sem presumir causalidade entre eles.

## 9. Indicadores de acompanhamento

- transferências correntes brutas / receita corrente bruta;
- crescimento nominal e, quando definido índice de deflação, crescimento real de receita e despesa;
- despesa paga por função;
- despesa paga a CNPJ versus CPF;
- núcleo de compras/contratações por tipo de aquisição;
- participação de credores com presença local, após reconciliação RFB;
- sensibilidade dos resultados à retirada de grandes entidades institucionais;
- VAF e IPM mantidos como indicadores fiscais/produtivos conceitualmente separados.

## 10. Regra editorial

Esta nota é material analítico de apoio. **Não altera o Caderno-Base v028, que permanece read-only**, nem promove automaticamente deltas para os cadernos.
