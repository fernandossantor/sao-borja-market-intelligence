# RAIS 2024 — estrutura ocupacional, remuneração e interdependências — v028

**Data:** 13/09/2026  
**Geografia:** São Borja/RS  
**Status:** documentação metodológica e analítica da reexecução canônica.

## 1. Objetivo

Reexecutar, sem reutilizar resultados numéricos da chamada interrompida:

- escolaridade;
- grandes grupos CBO 2002;
- CNAE;
- remuneração nominal média e de dezembro;
- jornada contratada;
- perfis setoriais;
- teste de agroimportância × agrodependência;
- matriz de interdependências econômicas.

## 2. Fontes e hashes

| Arquivo | Drive | SHA-256 | Uso |
|---|---|---|---|
| `rais_consolidated.csv` | `1hUlMY-6OfvFmbkzx6TBwhmeMuESRx_Ki` | `028765779ad80d27ed54a6d125611e2a478ca72892fe66a23e272394087a5766` | fonte analítica principal |
| `rais_canonical.csv` | `1iyx20-j8l4v7bULSGFOUiQc3LsBPfUgm` | `fb93c45b4a6135e973bd289901ee252cfccfedfaa0cfc70556f635f21adc1421` | controle de linhagem |

O consolidado contém o bloco `RAIS SB 2024.csv` com CBO e indicador de vínculo abandonado. O canônico não preserva essas duas variáveis e, portanto, não define o universo principal desta investigação.

Fonte institucional: MTE, RAIS 2024 — segundo processamento, incluindo administração pública.

## 3. Universo e filtro

1. `_source_file == "RAIS SB 2024.csv"` → **18.923** linhas;
2. `Ind Vínculo Ativo 31/12 == 1` → **13.233**;
3. excluir `Ind Vínculo Abandonado == 1` → **108** registros, todos zerados em remuneração média e dezembro;
4. estoque primário → **13.125 vínculos**.

**Fórmula:**  
`estoque_primario = ativo_31_12 AND NOT abandonado`.

Vínculo não equivale a pessoa.

## 4. Remuneração e jornada

Os campos monetários foram convertidos do formato BRL para número.

- remuneração média nominal positiva: n=12.395; média R$ 3.177,10; mediana R$ 2.510,86;
- remuneração de dezembro positiva: n=12.156; média R$ 3.307,05; mediana R$ 2.605,60;
- massa nominal de dezembro: R$ 40.200.501,32;
- até 2 SM: 56,57%;
- até 3 SM: 81,33%;
- >=40h: 90,44%;
- <30h: 4,91%;
- mediana da jornada: 44h.

As faixas em SM foram recalculadas como `remuneracao_dezembro_nominal / 1.412`. O campo de remuneração em SM da base não é usado como fonte primária nesta etapa porque o extrato contém ocorrências que exigiriam auditoria adicional de codificação.

## 5. Escolaridade

| Código | Categoria |
|---:|---|
| 1 | analfabeto |
| 2 | até 5º ano incompleto |
| 3 | 5º ano completo |
| 4 | 6º–9º incompleto |
| 5 | fundamental completo |
| 6 | médio incompleto |
| 7 | médio completo |
| 8 | superior incompleto |
| 9 | superior completo |
| 10 | mestrado |
| 11 | doutorado |

Resultados-chave:
- médio completo: **50,16%**;
- até médio completo: **74,94%**;
- superior completo ou mais: **20,79%**.

## 6. CBO 2002

Grande grupo = primeiro dígito do código CBO de seis dígitos, operacionalmente `floor(CBO/100000)`.

- GG4–GG9: **77,78%**;
- GG4+GG5: **45,97%**;
- GG5: **28,57%**.

A CBO define nível de competência como característica da ocupação e da complexidade das atividades; não é sinônimo de escolaridade individual.

## 7. CNAE e agregações analíticas

Divisão CNAE = dois primeiros dígitos da subclasse, com zeros à esquerda.

Agrupamentos usados:
- 01–03 agropecuária/floresta/pesca;
- 10 fabricação de alimentos;
- 11–33 indústria não alimentar/extrativa;
- 35–39 utilidades;
- 41–43 construção;
- 45 comércio/reparação de veículos;
- 46 atacado;
- 47 varejo;
- 49–53 transporte/armazenagem/correio;
- 55 alojamento;
- 56 alimentação fora do lar;
- 58–63 informação/comunicação;
- 64–66 financeiro;
- 68 imobiliário;
- 69–75 profissionais/científicos/técnicos;
- 77–82 administração/apoio;
- 84 administração pública;
- 85 educação;
- 86–88 saúde/assistência;
- 90–93 artes/cultura/recreação;
- 94–96 outros serviços.

Esses agrupamentos são **analíticos**, não uma nomenclatura oficial concorrente. CNAE descreve o empregador, não a ocupação do trabalhador.

## 8. Resultados setoriais prioritários

| Setor | Vínculos | Share | Mediana dez. |
|---|---:|---:|---:|
| Varejo | 2.824 | 21,52% | R$ 2.132,59 |
| Administração pública | 2.262 | 17,23% | R$ 3.592,57 |
| Agro 01–03 | 1.635 | 12,46% | R$ 2.824,91 |
| Alimentos 10 | 993 | 7,57% | R$ 2.922,49 |
| Transporte/armazenagem | 873 | 6,65% | R$ 2.858,81 |
| Administração/apoio | 738 | 5,62% | R$ 2.045,61 |
| Saúde/assistência | 721 | 5,49% | R$ 2.857,76 |
| Atacado | 474 | 3,61% | R$ 3.189,42 |
| Alimentação fora do lar | 339 | 2,58% | R$ 1.994,43 |

## 9. Núcleo agro direto ampliado

Convenção conservadora: CNAE 01–03 + divisão 10.

- emprego: **20,02%**;
- massa de dezembro: **19,96%**;
- fora do núcleo: **79,98%** dos vínculos.

**Controle:** fora do núcleo não significa independente do agro. Transporte, atacado, varejo, finanças e serviços podem ter exposição indireta.

## 10. Composição salarial

**INTERPRETAÇÃO SUSTENTADA:** a composição ocupacional/setorial é parte importante da remuneração típica relativamente comprimida, dada a concentração em varejo, serviços/vendas, apoio e foodservice.

**NÃO RESPONDIDO:** eventual penalidade salarial dentro da mesma ocupação em São Borja. Isso exige benchmark RAIS 2024 por CBO, jornada e escolaridade.

O CEMPRE 2022 é apenas controle contextual e não indica desvantagem média excepcional de São Borja nos pares de escala usados.

## 11. Teste de agrodependência

Evidências combinadas, não aditivas:
- agro = 33,87% do VAB 2021;
- agro = 12,41% do emprego formal 2021;
- comércio + serviços = 69,45% do emprego 2021;
- agro 01–03 = 12,46% do emprego RAIS 2024;
- núcleo 01–03+10 = 20,02% do emprego 2024;
- 2019–2021: agro +118,85% real-proxy, comércio/demais serviços -9,11%, indústria -2,80%, público -6,78%;
- beneficiamento de arroz: 953 vínculos e R$ 3,491 mi de massa de dezembro/2025;
- ESTBAN rural agrícola: 47,64%–55,55% das operações de crédito selecionadas.

**Diagnóstico:** agroimportância alta = sustentada. Agrodependência global = não demonstrada.

## 12. Matriz de interdependências

Tipologia:
1. geradores de valor;
2. geradores de emprego/renda;
3. transmissores de ciclos;
4. estabilizadores candidatos da demanda;
5. dependentes de outros circuitos;
6. conectores externos.

A tipologia é analítica, não oficial e não mutuamente exclusiva. Não há multiplicadores locais.

## 13. Relação com os cadernos POM

- essenciais: demanda recorrente e preço/custo-benefício devem ser lidos em conjunto com renda mensal;
- saúde/higiene: separar medicamentos/higiene básica de cosméticos/suplementos;
- não essenciais: maior exposição a renda disponível, crédito e adiamento;
- alimentação/serviços: combinar demanda residente com potenciais fluxos externos da ponte/instituições.

RAIS não permite inferir participação do orçamento ou causalidade de consumo. POF é benchmark nacional; POM é evidência qualitativa/contextual local.

## 14. Retificações da execução interrompida

- vínculos abandonados excluídos: **108**, não 139;
- até 2 SM em dezembro: **56,57%**, não 57,03%;
- até 3 SM em dezembro: **81,33%**, não 81,42%.

## 15. Governança

A v028 permanece corrente. A v029 anterior é fonte auxiliar e não substitui a v028. PR #41 permanece **aberto, draft e sem merge**.
