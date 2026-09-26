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

## 3. Auditoria dos fatores IPCA

Foram combinadas as tabelas SIDRA:

- **1419** — IPCA por geral/grupo/subgrupo/item/subitem até dezembro/2019;
- **7060** — mesma arquitetura a partir de janeiro/2020;
- variável **63** — variação mensal (%);
- classificação **315** — geral, grupo, subgrupo, item e subitem.

Para compatibilidade com o modelo já preservado de alimentação, o período acumulado é **2018-01 a 2026-06**, 102 meses.

O fator calculado pelo novo pipeline para `Alimentação e bebidas` foi **1,781565142282**. O fator já canônico do projeto é **1,781742384675**.

Diferença relativa:

`(1,781565142282 / 1,781742384675 - 1) × 100 = -0,00995%`.

**Interpretação:** a reprodução por composição das variações mensais publicadas praticamente fecha com o fator canônico. A diferença residual é compatível com acumulação de taxas mensais publicadas com arredondamento. O fator canônico de Bens Essenciais é preservado.

## 4. Crosswalk POF → IPCA

| Módulo POF/SBMI | POF R$/família/mês | IPCA usado | Código SIDRA c315 | Fator jan/2018–jun/2026 | Compatibilidade |
|---|---:|---|---:|---:|---|
| Alimentação no domicílio | 487,00 | Alimentação e bebidas | 7170 | 1,781742384675* | proxy de grupo já canônica |
| Alimentação fora do domicílio | 249,69 | Alimentação fora do domicílio | 7433 | 1,590068184251 | alta |
| Higiene e Cuidados Pessoais | 139,87 | Higiene pessoal | 7698 | 1,521859557648 | média-alta; nomenclatura POF é mais ampla |
| Remédios | 171,83 | Produtos farmacêuticos | 7662 | 1,497233067692 | alta |
| Mobiliários e artigos do lar | 85,18 | Móveis e utensílios | 7487 | 1,424601780273 | média-alta; conceitos próximos, não idênticos |
| Eletrodomésticos | 74,66 | Eletrodomésticos e equipamentos | 7522 | 1,356992683697 | alta |
| Vestuário | 183,53 | Vestuário | 7558 | 1,473133343800 | alta no nível agregado |
| Serviços pessoais | 47,28 | Serviços pessoais | 7714 | 1,440282974794 | alta para esse submercado |

`* fator preservado no modelo canônico; o pipeline reproduziu 1,781565142282.`

## 5. Resultados modelados

| Setor | Módulo | Baseline mensal — preços POF | Fator | Demanda mensal — preços aprox. jun/2026 | Demanda anual — preços aprox. jun/2026 | Status |
|---|---|---:|---:|---:|---:|---|
| Bens Essenciais | Alimentação no domicílio | R$ 10.977.373,90 | 1,781742384675 | R$ 19.558.852,34 | **R$ 234.706.228,14** | canônico |
| Alimentação Fora do Lar | Alimentação fora do domicílio | R$ 5.628.214,56 | 1,590068184251 | R$ 8.949.244,90 | **R$ 107.390.938,78** | promover como benchmark modelado |
| Saúde/Higiene | Higiene e Cuidados Pessoais | R$ 3.152.782,93 | 1,521859557648 | R$ 4.798.092,84 | **R$ 57.577.114,03** | módulo |
| Saúde/Higiene | Remédios | R$ 3.873.187,18 | 1,497233067692 | R$ 5.799.063,92 | **R$ 69.588.767,08** | módulo |
| Bens Não Essenciais | Mobiliários e artigos do lar | R$ 1.920.026,10 | 1,424601780273 | R$ 2.735.272,59 | **R$ 32.823.271,13** | módulo |
| Bens Não Essenciais | Eletrodomésticos | R$ 1.682.896,79 | 1,356992683697 | R$ 2.283.678,63 | **R$ 27.404.143,52** | módulo |
| Bens Não Essenciais | Vestuário | R$ 4.136.914,64 | 1,473133343800 | R$ 6.094.226,90 | **R$ 73.130.722,82** | módulo |
| Serviços | Serviços pessoais | R$ 1.065.729,44 | 1,440282974794 | R$ 1.534.951,97 | **R$ 18.419.423,64** | submercado apenas |

## 6. Agregações permitidas e proibidas

### Saúde/Higiene — cesta-núcleo

Soma dos dois módulos monetários selecionados:

`R$ 57.577.114,03 + R$ 69.588.767,08 = R$ 127.165.881,11/ano`.

Natureza: **ESTIMATIVA MODELADA DE CESTA-NÚCLEO RESIDENTE**.

Não é o market size total do caderno. Pode não abranger integralmente suplementos e outras categorias; deliberadamente não inclui planos e serviços médicos/dentários.

### Bens Não Essenciais — cesta de três módulos

`R$ 32.823.271,13 + R$ 27.404.143,52 + R$ 73.130.722,82 = R$ 133.358.137,47/ano`.

Natureza: **ESTIMATIVA MODELADA DE TRÊS MÓDULOS**.

Não é o market size total de bens não essenciais. O caderno inclui outras categorias, entre elas pet/vet/agro, decoração/utilidades e outras frentes sem crosswalk completo.

### Serviços

Não somar `Serviços pessoais` a outras categorias sem perímetro explícito. A POF não cobre o universo heterogêneo do caderno como uma única categoria.

## 7. Revisão da estimativa de Alimentação Fora do Lar

A etapa anterior havia produzido, apenas como sensibilidade provisória, **R$ 120.336.341,08/ano** aplicando o fator geral `Alimentação e bebidas`.

Esse valor é **substituído** no modelo corrente por **R$ 107.390.938,78/ano**, porque agora existe fator IPCA específico para `Alimentação fora do domicílio`.

Diferença entre as duas modelagens:

`R$ 107.390.938,78 / R$ 120.336.341,08 - 1 = -10,7577%`.

Isso não representa queda de mercado. É **efeito metodológico da adoção de um índice de preços mais aderente ao módulo**.

## 8. Limitações comuns

- padrão de consumo é estadual, não municipal;
- população é 2025, enquanto a POF é 2017-2018;
- atualização de preços usa IPCA Brasil, não preço observado de São Borja;
- fatores são compostos a partir de variações mensais publicadas;
- alguns crosswalks POF↔IPCA são aproximações semânticas;
- não há ajuste por renda municipal por incompatibilidade conceitual entre classes POF e renda domiciliar per capita do Censo;
- não entram diretamente visitantes, população flutuante, compras de residentes fora do município, e-commerce externo ou compras na Argentina;
- demanda residente não informa quanto o comércio local captura.

## 9. O que muda na matriz de viabilidade

- **Alimentação Fora do Lar:** passa de `DR obtível` para **DR modelada disponível**.
- **Saúde/Higiene:** passa de `DR obtível` para **dois módulos de DR modelados**, com cesta-núcleo calculável.
- **Bens Não Essenciais:** passa de `DR obtível por módulos` para **três módulos modelados disponíveis**.
- **Serviços:** passa a ter **submercado modelado de serviços pessoais**, sem autorização para generalizar ao setor.
- **Market share:** permanece **não defensável** nos cinco mercados, pois falta faturamento observado setorial/local compatível.

## 10. Rastreabilidade

Workflow:
`.github/workflows/ipca-market-dimension-factor-discovery-v1.yml`

Execução final:
- run: `36259139094`;
- job: `108451478087`;
- commit do workflow: `b124ffe83277d5ec9a4c71953cbcdd6d722d455f`.

Artifact:
- ID: `10911821781`;
- digest: `sha256:3976d3c0944382a58b9ca9fe6d0d375b1851ed2e8aaf8fd1b417d8dfd7bbd221`.

Google Drive:
- `SBMI_IPCA_fatores_dimensao_mercado_v001.zip`;
- ID: `1X0_YBnZkN4B81FSO8acHgaWXUBEVvRjK`.

Fontes POF e DFe permanecem rastreadas nos documentos correspondentes.

## 11. Próxima decisão empírica

A prioridade deixa de ser ampliar estimativas por consumo e passa a ser obter **faturamento observado territorial-setorial**.

Ordem:

1. testar/solicitar `São Borja × CNAE × modelo DFe × mês × valor`;
2. testar/solicitar `São Borja × NCM × modelo DFe × mês × valor` para varejos de mix amplo;
3. obter NFS-e agregada por item de serviço para Serviços;
4. somente com denominador e numerador monetários compatíveis avançar para market share.
