# Nota analítica — Radar do Mercado — cesta-piloto de arroz — jul/2024 a ago/2026

## 1. Objeto e finalidade

Esta nota registra a primeira série mensal contínua materializada a partir dos arquivos oficiais de **Composição de Mercado** do Radar do Mercado da Receita Estadual/SEFAZ-RS.

A finalidade desta etapa é dupla:

1. validar a continuidade técnica e metodológica do schema mensal;
2. testar, com uma cesta explícita de sete NCMs de arroz, a evolução dos fluxos `INT`, `OUF` e `EXT` e da `Part.RS`.

A cesta é **piloto metodológico**. Ela não representa automaticamente todo o setor arrozeiro, não mede demanda de São Borja e não deve ser usada como market size municipal.

## 2. Fonte, período, unidade e abrangência

- Fonte observada: Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos.
- Arquivos: `Composicao_de_Mercado_MM_AAAA.csv`.
- Período: julho/2024 a agosto/2026.
- Competências esperadas: 26.
- Competências baixadas: 26.
- Competências auditadas: 26.
- Competências com os sete NCMs-piloto: 26.
- Abrangência: Rio Grande do Sul.
- Unidade: valores nominais publicados nos CSVs oficiais.
- Natureza de `INT`, `OUF`, `EXT`: dado observado na fonte.
- Natureza de `Part.RS`: dado calculado pelo SBMI.
- Promoção canônica automática: nenhuma.

## 3. Auditoria de schema

As 26 competências possuem o mesmo conjunto de campos observado:

`anomes | cod_ncm | ncm_descr | emit_uf | tipo_operacao | vlr_nominal | corte_sigilo`

Mapeamento reproduzido em todas as competências:

- NCM = `cod_ncm`;
- período = `anomes`;
- origem/operação = `tipo_operacao`;
- valor = `vlr_nominal`.

Resultado: **não foi observada mudança de schema entre jul/2024 e ago/2026** nos arquivos materializados.

## 4. Fórmulas

Para cada NCM:

`Demanda_RS = INT + OUF + EXT`

`Part.RS = INT / (INT + OUF + EXT)`

Para a cesta-piloto agregada no mês:

`Part.RS_piloto = ΣINT / Σ(INT + OUF + EXT)`

A agregação ponderada é um **cálculo SBMI sobre os sete NCMs**. Não é indicador oficial publicado com esse rótulo.

## 5. Resultados da cesta-piloto

### 5.1 Síntese por intervalo

| Intervalo | Meses | INT (R$) | OUF (R$) | EXT (R$) | Demanda agregada piloto (R$) | Part.RS ponderada |
|---|---:|---:|---:|---:|---:|---:|
| jul–dez/2024 | 6 | 1.206.344.305 | 97.354.363 | 798.444.748 | 2.102.143.416 | 57,39% |
| 2025 | 12 | 1.804.812.628 | 122.319.786 | 571.637.011 | 2.498.769.425 | 72,23% |
| jan–ago/2026 | 8 | 1.033.017.496 | 71.357.280 | 333.548.856 | 1.437.923.632 | 71,84% |

Os intervalos possuem comprimentos diferentes. A linha de 2026 é parcial e não deve ser comparada diretamente ao total anual de 2025.

### 5.2 Comparação homogênea jan–ago

| Variável | jan–ago/2025 | jan–ago/2026 | Variação nominal |
|---|---:|---:|---:|
| INT | R$ 1.330.050.839 | R$ 1.033.017.496 | -22,33% |
| OUF | R$ 86.879.754 | R$ 71.357.280 | -17,87% |
| EXT | R$ 443.443.442 | R$ 333.548.856 | -24,78% |
| Demanda agregada piloto | R$ 1.860.374.035 | R$ 1.437.923.632 | -22,71% |
| Part.RS ponderada | 71,49% | 71,84% | +0,35 p.p. |

**Dado calculado:** no recorte homogêneo jan–ago, o valor nominal agregado da cesta-piloto caiu 22,71% em 2026 frente a 2025, enquanto a participação interna ponderada permaneceu praticamente estável, com aumento de aproximadamente 0,35 ponto percentual.

Isto não permite atribuir a queda a volume físico, preço, produção ou consumo, porque os CSVs desta análise carregam valores nominais e esta nota não decompõe preço e quantidade.

### 5.3 Agosto: comparação interanual

| Variável | ago/2025 | ago/2026 | Variação |
|---|---:|---:|---:|
| INT | R$ 152.453.986 | R$ 135.978.913 | -10,81% |
| OUF | R$ 12.230.681 | R$ 9.979.870 | -18,40% |
| EXT | R$ 53.725.091 | R$ 65.227.155 | +21,41% |
| Demanda agregada piloto | R$ 218.409.758 | R$ 211.185.938 | -3,31% |
| Part.RS ponderada | 69,80% | 64,39% | -5,41 p.p. |

**Dado calculado:** em agosto/2026, o peso de `EXT` na cesta-piloto foi aproximadamente 30,89% do total mensal, contra 24,60% em agosto/2025; a `Part.RS` ponderada recuou 5,41 p.p.

**Interpretação:** o resultado sugere maior presença relativa de origem externa à produção interna do RS nesse recorte e nessa competência. Não autoriza inferir dependência estrutural de São Borja nem afirmar que houve substituição causal da produção gaúcha por importações.

## 6. Amplitude temporal do piloto

A `Part.RS` mensal ponderada da cesta variou de:

- mínimo observado: **42,22% em jul/2024**;
- máximo observado: **83,85% em dez/2025**;
- ago/2026: **64,39%**.

A amplitude mostra que uma fotografia mensal isolada pode ser pouco representativa da posição da cesta ao longo do tempo. Para uso analítico, a série deve acompanhar sazonalidade, preços, safra e possíveis mudanças de origem sem converter associação temporal em causalidade.

## 7. Faixas da Nota Técnica

A Nota Técnica CIET 05/2026 explicita as faixas:

- crítica: `Part.RS < 5%`;
- alta: `5% <= Part.RS < 15%`;
- média: `15% <= Part.RS < 30%`.

Valores acima de 30% são tratados pelo pipeline como `FORA_DAS_FAIXAS_NT`. Esse marcador é **controle interno**, não uma quarta categoria oficial.

A agregação mensal da cesta-piloto ficou acima de 30% em todas as competências, portanto não recebe categoria oficial de dependência pela classificação expressamente documentada na NT.

## 8. Diagnóstico mercadológico

**Dado observado:** há uma série oficial mensal contínua e tecnicamente homogênea de 26 competências para Composição de Mercado, jul/2024–ago/2026.

**Dado calculado:** no piloto de sete NCMs, a composição entre INT, OUF e EXT muda de forma relevante ao longo dos meses, mesmo quando a `Part.RS` agregada de intervalos mais longos parece relativamente estável.

**Interpretação:** para investigar cadeias relevantes a São Borja, o Radar é mais útil como indicador de **estrutura estadual de abastecimento e contestabilidade externa** do que como medida direta de demanda municipal.

**Recomendação baseada em evidência:** ampliar o pipeline para cestas de NCM explicitamente vinculadas às cadeias do projeto e observar série mensal, não apenas a competência corrente.

**Hipótese a testar:** itens/cadeias com baixa `Part.RS` estadual podem sinalizar espaços de fornecimento ou vulnerabilidade de suprimento relevantes para agentes locais, mas a oportunidade empresarial só existe se houver compatibilidade técnica, escala, preço, logística e demanda efetiva.

## 9. Próximas etapas

1. definir cestas de NCM por cadeia/mercado, com regra explícita de inclusão;
2. cruzar `Categorias_Produtos.csv` e `Portfolio_NCMs_Setor.csv` para documentar taxonomias;
3. gerar série mensal por NCM, cesta e setor;
4. identificar casos nas faixas crítica/alta/média da NT;
5. separar tendência, sazonalidade e choque mensal;
6. usar o Radar como benchmark estadual em conjunto com oferta produtiva e empresarial local, nunca como proxy de demanda de São Borja.

## 10. Regra editorial

Esta nota é evidência analítica exploratória e reproduzível. **Não altera o Caderno-Base v028, que permanece read-only**, e não promove automaticamente o piloto de arroz a indicador canônico do território.
