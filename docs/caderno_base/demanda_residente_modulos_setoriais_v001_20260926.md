# Demanda residente modelada — módulos setoriais POF/IPCA — v001

**Data:** 2026-09-26  
**Geografia do resultado:** São Borja/RS  
**População usada:** 61.311 pessoas — Estimativas da População 2025/IBGE  
**Consumo-base:** POF 2017-2018 — Rio Grande do Sul  
**Tamanho médio familiar:** 2,72 pessoas — POF/RS  
**Atualização de preços:** IPCA Brasil, variações mensais oficiais, janeiro/2018 a junho/2026  
**Natureza dos resultados:** ESTIMATIVAS MODELADAS DE DEMANDA RESIDENTE.

## 1. Objetivo

Avançar da matriz metodológica para uma primeira dimensão monetária comparável entre módulos dos cinco cadernos, preservando a diferença entre:

- demanda residente;
- faturamento empresarial;
- mercado capturado;
- faturamento observado;
- market share.

Os resultados deste documento estimam **gasto potencial dos residentes**, e não vendas realizadas em São Borja.

## 2. Fórmula geral

Para cada módulo:

`baseline mensal a preços POF = população São Borja 2025 × (despesa média familiar mensal POF/RS ÷ 2,72)`

`demanda mensal atualizada = baseline mensal × fator IPCA específico`

`demanda anual atualizada = demanda mensal atualizada × 12`

A população 2025 é usada como escala demográfica atual. O padrão de gasto permanece derivado do Rio Grande do Sul na POF 2017-2018.

A divisão por `2,72` é uma territorialização per capita do padrão estadual. Não afirma que o tamanho médio domiciliar de São Borja em 2025 seja exatamente 2,72.

## 3. Auditoria dos fatores IPCA

Foram combinadas as tabelas SIDRA:

- **1419** — IPCA por geral/grupo/subgrupo/item/subitem até dezembro/2019;
- **7060** — mesma arquitetura a partir de janeiro/2020;
- variável **63** — variação mensal (%);
- classificação **315** — geral, grupo, subgrupo, item e subitem.

Para compatibilidade com o modelo já preservado de alimentação, o período acumulado é **2018-01 a 2026-06**, 102 meses.

O fator calculado pelo pipeline para `Alimentação e bebidas` foi **1,781565142282**. O fator já canônico do projeto é **1,781742384675**.

Diferença relativa:

`(1,781565142282 / 1,781742384675 - 1) × 100 = -0,00995%`.

**Interpretação:** a reprodução por composição das variações mensais publicadas praticamente fecha com o fator canônico. O fator canônico de Bens Essenciais é preservado.

## 4. Crosswalk POF → IPCA

| Módulo POF/SBMI | POF R$/família/mês | IPCA usado | Código SIDRA c315 | Fator jan/2018–jun/2026 | Compatibilidade |
|---|---:|---|---:|---:|---|
| Alimentação no domicílio | 487,00 | Alimentação e bebidas | 7170 | 1,781742384675* | proxy de grupo já canônica |
| Alimentação fora do domicílio | 249,69 | 1201.Alimentação fora do domicílio | 7433 | 1,590068184251 | alta |
| Higiene e Cuidados Pessoais | 139,87 | 6301.Higiene pessoal | 7698 | 1,521859557648 | média-alta; nomenclatura POF é mais ampla |
| Remédios | 171,83 | 6101.Produtos farmacêuticos | 7662 | 1,497233067692 | alta |
| Mobiliários e artigos do lar | 85,18 | 31.Móveis e utensílios | 7487 | 1,424601780273 | média; conceitos próximos, não idênticos |
| Eletrodomésticos | 74,66 | 3201.Eletrodomésticos e equipamentos | 7522 | 1,356992683697 | alta |
| Vestuário | 183,53 | 4.Vestuário | 7558 | 1,473133343800 | alta no nível agregado |
| Serviços pessoais | 47,28 | 7101.Serviços pessoais | 7714 | 1,440282974794 | alta para esse submercado |

`* fator preservado no modelo canônico; o pipeline reproduziu 1,781565142282.`

A seleção usa o nível mais específico quando o SIDRA publica simultaneamente um agregado e um detalhamento, como `12` versus `1201`, `61` versus `6101` e `71` versus `7101`.

## 5. Resultados modelados

| Setor | Módulo | Baseline mensal — preços POF | Fator | Demanda mensal — preços aprox. jun/2026 | Demanda anual — preços aprox. jun/2026 | Grau atual |
|---|---|---:|---:|---:|---:|---|
| Bens Essenciais | Alimentação no domicílio | R$ 10.977.373,90 | 1,781742384675 | R$ 19.558.852,34 | **R$ 234.706.228,14** | MÉDIA-ALTA |
| Alimentação Fora do Lar | Alimentação fora do domicílio | R$ 5.628.214,56 | 1,590068184251 | R$ 8.949.244,90 | **R$ 107.390.938,78** | MÉDIA-ALTA |
| Saúde/Higiene | Higiene e Cuidados Pessoais | R$ 3.152.782,93 | 1,521859557648 | R$ 4.798.092,84 | **R$ 57.577.114,03** | MÉDIA |
| Saúde/Higiene | Remédios | R$ 3.873.187,18 | 1,497233067692 | R$ 5.799.063,92 | **R$ 69.588.767,08** | MÉDIA-ALTA |
| Bens Não Essenciais | Mobiliários e artigos do lar | R$ 1.920.026,10 | 1,424601780273 | R$ 2.735.272,59 | **R$ 32.823.271,13** | MÉDIA |
| Bens Não Essenciais | Eletrodomésticos | R$ 1.682.896,79 | 1,356992683697 | R$ 2.283.678,63 | **R$ 27.404.143,52** | MÉDIA-ALTA |
| Bens Não Essenciais | Vestuário | R$ 4.136.914,64 | 1,473133343800 | R$ 6.094.226,90 | **R$ 73.130.722,82** | MÉDIA-ALTA |
| Serviços | Serviços pessoais | R$ 1.065.729,44 | 1,440282974794 | R$ 1.534.951,97 | **R$ 18.419.423,64** | MÉDIA para o submercado |

## 6. Agregações permitidas e proibidas

### Saúde/Higiene — cesta-núcleo

`R$ 57.577.114,03 + R$ 69.588.767,08 = R$ 127.165.881,11/ano`.

Natureza: **ESTIMATIVA MODELADA DE CESTA-NÚCLEO RESIDENTE**.

Não é o market size total do caderno. Pode não abranger integralmente suplementos e outras categorias; deliberadamente não inclui planos e serviços médicos/dentários.

### Bens Não Essenciais — cesta de três módulos

`R$ 32.823.271,13 + R$ 27.404.143,52 + R$ 73.130.722,82 = R$ 133.358.137,47/ano`.

Natureza: **ESTIMATIVA MODELADA DE TRÊS MÓDULOS**.

Não é o market size total de bens não essenciais. O caderno inclui outras categorias e arenas ainda sem crosswalk completo.

### Serviços

`R$ 18.419.423,64/ano` refere-se exclusivamente ao submercado **Serviços pessoais**. Não generalizar ao conjunto do caderno Serviços.

## 7. Revisão da estimativa de Alimentação Fora do Lar

A etapa anterior havia produzido, apenas como sensibilidade provisória, **R$ 120.336.341,08/ano** aplicando o fator geral `Alimentação e bebidas`.

Esse valor é **substituído** no modelo corrente por **R$ 107.390.938,78/ano**, porque existe fator IPCA específico para `1201.Alimentação fora do domicílio`.

Diferença entre as duas modelagens:

`R$ 107.390.938,78 / R$ 120.336.341,08 - 1 = -10,7577%`.

Isso não representa queda de mercado. É efeito metodológico da adoção de um índice de preços mais aderente ao módulo.

## 8. Comparabilidade com o envelope fiscal DFe

A demanda residente estimada e o envelope municipal de NFC-e respondem a perguntas diferentes:

- POF/IPCA: quanto os **residentes** tenderiam a demandar, independentemente do local/canal da compra;
- NFC-e municipal: quanto foi documentado em NFC-e por **emitentes localizados no município**, independentemente da residência do consumidor e do setor.

Consequentemente, não é válido calcular `DR_setorial / NFC-e_total_municipal` como taxa de captura, nem repartir o envelope de NFC-e por CNPJ, lojas, vínculos ou remuneração.

## 9. O que muda na matriz de viabilidade

- **Alimentação Fora do Lar:** passa de `DR obtível` para **DR modelada disponível**.
- **Saúde/Higiene:** passa de `DR obtível` para **dois módulos de DR modelados**, com cesta-núcleo calculável.
- **Bens Não Essenciais:** passa de `DR obtível por módulos` para **três módulos modelados disponíveis**.
- **Serviços:** passa a ter **submercado modelado de serviços pessoais**, sem autorização para generalizar ao setor.
- **Market share:** permanece **não defensável** nos cinco mercados.

## 10. Fontes, período, unidade e limitações

### POF
- Fonte: IBGE — POF 2017-2018 — tabelas por Unidade da Federação;
- geografia: Rio Grande do Sul;
- unidade: R$/família/mês;
- período: 2017-2018.

### IPCA
- Fonte: IBGE/SIDRA;
- tabelas: 1419 e 7060;
- variável: 63 — variação mensal;
- classificação: 315;
- geografia: Brasil;
- período encadeado: 2018-01 a 2026-06.

### Demografia
- Fonte: IBGE — estimativa populacional 2025;
- geografia: São Borja/RS;
- população: 61.311.

### Limitações principais
- POF não é municipal;
- fatores de preços são nacionais;
- alguns crosswalks são conceitualmente próximos, não idênticos;
- não há calibração pela distribuição de renda municipal por incompatibilidade conceitual já documentada;
- não entram demanda não residente, vazamento territorial ou comércio eletrônico de modo separado;
- não há, nesta etapa, faturamento empresarial observado por setor.

## 11. Rastreabilidade

Workflow:
`.github/workflows/ipca-market-dimension-factor-discovery-v1.yml`

Execução final auditada:
- run: `36262455280`;
- job: `108460749288`;
- commit do workflow: `813f95b379e6771f7437d207de6dc7a6381017a1`;
- artifact: `10912812570`;
- digest: `sha256:3650f0f1b59d1ee39267e19c84bdd660ff61556c79771d8beb88b60c4115d73a`.

Google Drive:
- `SBMI_IPCA_market_dimension_factors_v001.zip`;
- ID: `1kxAz3ajLl9UyTUlcN9iBlL16nFnQ9fJF`.

Crosswalk POF:
- workflow: `pof-rs-market-crosswalk-v1`;
- run: `36258547920`;
- artifact: `10911900788`;
- Drive: `SBMI_POF_RS_market_crosswalk_v001.zip`, ID `1OpNbR9_IAaXU-pdjsiLyvG8hOuXG1Asi`.

## 12. Próxima decisão empírica

A prioridade passa a ser obter **faturamento observado territorial-setorial**:

1. testar `São Borja × CNAE × modelo DFe × mês × valor`;
2. testar `São Borja × NCM × modelo DFe × mês × valor` para varejos de mix amplo;
3. obter NFS-e agregada por item de serviço para Serviços;
4. somente com denominador e numerador monetários compatíveis avançar para market share.
