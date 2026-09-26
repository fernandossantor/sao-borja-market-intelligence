# Diagnóstico inicial das séries públicas normalizadas — v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica (SBMI)  
**Camada de dados:** `public-market-series-curated-v001`  
**Run canônico:** `36279321664`  
**Commit:** `3b7187d5453a4250699befbb9061ec39b33cdd61`  
**Artifact:** `10918776468`  
**Digest do artifact:** `sha256:2e1bb9d99c6dbc3bb55b1da604f5297c8b2de547a39c39f3ba53735a357f9aed`  
**SHA-256 do pacote interno:** `6f321b4b27deb2410e9be49c22d9f3429fdaaa20e8ed6f5edaaa3d153ded7275`

## 1. Objetivo e delimitação

Este diagnóstico é a primeira leitura analítica após a normalização das séries públicas da Receita Estadual/RS. Ele **não** estima market share municipal. Mantém separadas três escalas:

- São Borja/RS: DFe por modelo e data;
- COREDE Fronteira Oeste: preços unitários da Cesta Alimentos;
- Rio Grande do Sul: Radar do Mercado e DFe por CNAE.

Valores monetários desta etapa são **nominais**, salvo indicação em contrário. Nenhuma correlação é interpretada como causalidade.

## 2. Auditoria adicional descoberta durante a normalização

### 2.1 Mudança de formato numérico do Radar em 2026

Os arquivos do Radar de 2024 e 2025 apresentam os campos monetários como inteiros sem separador de milhares. Em 2026, a apresentação muda: exemplos observados incluem `129.639` e `3.020.306`. Nesses arquivos o ponto é **separador de milhares**, não decimal.

A primeira versão da camada curated leu esses pontos como decimais. A inconsistência foi identificada porque o total mensal publicado da Composição de Mercado caía artificialmente da ordem de dezenas de bilhões para poucos milhões.

A rotina foi corrigida para:

[
valor normalizado_{2026} = remover pontos de milhares(valor fonte)
]

Os brutos não foram alterados. As tabelas de cobertura agora registram `source_values_dot_thousands_rows` e `source_numeric_rule`.

Após a correção, por exemplo, o valor publicado não suprimido da Composição de Mercado em julho/2026 é **R$ 45,995 bilhões**, coerente em ordem de grandeza com a série anterior. Este valor é estadual e parcial quanto ao sigilo; não é faturamento de São Borja.

### 2.2 Cobertura da taxonomia NCM

A taxonomia canônica possui 11.765 NCM8 e 110 grupos. Ainda assim, há NCMs presentes nas séries correntes que não aparecem no catálogo:

- Composição de Mercado: 2.200 NCM8 não classificados; cobertura de linhas = **96,20%**;
- Exportações: 126 NCM8 não classificados; cobertura de linhas = **99,62%**;
- Portfólio: 1.333 de 1.349 NCM8 cobertos = **98,81%**.

Em valor publicado, a lacuna é bem menor:

- Composição: grupos classificados cobrem **99,50%** do valor nominal publicado não suprimido no período;
- Exportações: grupos classificados cobrem **99,43%** do valor FOB publicado no período.

**Interpretação:** os benchmarks por grupo podem ser usados provisoriamente como contexto estadual com alta cobertura de valor, mas os NCMs ausentes permanecem inventariados e não são imputados automaticamente.

## 3. Sinal fiscal local — DFe de São Borja

Fonte: Receita Estadual/RS.  
Geografia: São Borja/RS, código 4318002.  
Período: 2018-01-01 a 2026-09-14.  
Unidades: quantidade de DFe e valor total nominal associado ao modelo.

Os modelos são mantidos separados porque CT-e, NF-e e NFC-e representam documentos diferentes e não formam, por simples soma, um denominador de market share.

### 3.1 Fechamento 2025 contra 2024

| Modelo | Quantidade 2025/2024 | Valor nominal 2025/2024 | Valor médio por DFe |
|---|---:|---:|---:|
| CT-e | +6,37% | +15,14% | +8,25% |
| NF-e | +13,43% | -13,13% | -23,41% |
| NFC-e | +8,36% | +13,99% | +5,19% |

O resultado mais relevante é a divergência da NF-e em 2025: houve mais documentos, mas menor valor nominal agregado e menor valor médio por documento. Isso é um **fato descritivo**, não evidência suficiente de queda da economia local: podem existir mudanças de composição, emissão, natureza das operações ou outras alterações não identificadas pela série agregada.

### 3.2 Comparação homóloga de 2026

Para evitar comparar um ano parcial com anos completos, foi calculado o período **1º de janeiro a 14 de setembro** em 2025 e 2026.

Fórmulas:

[
variação (%) = left(rac{x_{2026}}{x_{2025}}-1ight)	imes100
]

[
valor médio por DFe = rac{valor total DFe}{quantidade DFe}
]

Resultados:

| Modelo | Qtde. 2026 vs 2025 | Valor nominal | Valor médio/DFe |
|---|---:|---:|---:|
| CT-e | +15,47% | +29,11% | +11,81% |
| NF-e | +13,30% | +17,24% | +3,48% |
| NFC-e | +2,87% | -2,22% | -4,95% |

**Interpretação:** até 14/09/2026, a NFC-e registra mais documentos do que no mesmo período de 2025, mas valor nominal agregado e valor médio por documento menores. Este é um sinal potencialmente relevante para o consumo transacional local, porém ainda não permite concluir redução real de consumo, porque a série não controla inflação, composição da cesta, perfil dos emissores ou mudanças de registro.

## 4. Preços regionais — Cesta Alimentos

Fonte: Receita Estadual/RS — Cesta Alimentos.  
Geografia: COREDE Fronteira Oeste.  
Período comparado: média de janeiro a junho de 2025 contra média de janeiro a junho de 2026.  
Universo: 80 produtos com cobertura completa.

Para cada produto:

[
Delta_i = left(rac{overline{P}_{i,2026H1}}{overline{P}_{i,2025H1}}-1ight)	imes100
]

Depois é examinada a distribuição das 80 variações. **Não são somados preços entre produtos de unidades diferentes e não se cria um índice de inflação sem pesos de cesta.**

Resultados calculados:

- mediana das variações por produto: **+2,46%**;
- média simples das variações: **+2,28%**;
- primeiro quartil: **-5,87%**;
- terceiro quartil: **+8,80%**;
- 44 produtos tiveram média H1 maior em 2026;
- 36 tiveram média H1 menor.

A dispersão é muito elevada. Entre as maiores altas aparecem moranga (+62,89%), cenoura (+54,96%), chuchu (+47,69%), beterraba (+41,40%) e batata-doce (+38,69%). Entre as maiores quedas aparecem alho (-34,38%), azeite de oliva (-34,09%), laranja (-33,17%), arroz branco (-29,48%) e coxa de frango (-26,19%).

**Interpretação:** o comportamento regional dos alimentos é heterogêneo; a média/mediana simples não deve ser apresentada como inflação da cesta. A utilidade mercadológica está na identificação de pressão relativa por item e na combinação futura com pesos de consumo.

## 5. Benchmark estadual do Radar

Fonte: Receita Estadual/RS — Radar do Mercado, Composição de Mercado.  
Geografia: Rio Grande do Sul.  
Comparação: janeiro-agosto/2026 contra janeiro-agosto/2025.  
Unidade: valor nominal **publicado e não suprimido** das células mapeadas para a taxonomia SBMI.

Por status de aderência ao escopo:

| Setor SBMI | Status | Jan-ago/2025 | Jan-ago/2026 | Variação nominal |
|---|---|---:|---:|---:|
| Bens Essenciais | CORE | R$ 56,10 bi | R$ 55,39 bi | -1,27% |
| Bens Essenciais | ADJACENT | R$ 9,01 bi | R$ 9,77 bi | +8,50% |
| Bens Não Essenciais | CORE | R$ 28,01 bi | R$ 27,17 bi | -2,97% |
| Bens Não Essenciais | EXPANDED | R$ 10,82 bi | R$ 11,16 bi | +3,18% |
| Saúde/Higiene/Cuidados Pessoais | CORE | R$ 14,76 bi | R$ 17,13 bi | +16,12% |
| Saúde/Higiene/Cuidados Pessoais | EXPANDED | R$ 3,79 bi | R$ 4,13 bi | +9,05% |
| Serviços | ADJACENT | R$ 16,81 bi | R$ 17,90 bi | +6,48% |

A categoria Serviços no Radar contém **mercadorias complementares** relacionadas, como peças/pneumáticos, e não mede prestação de serviços. O denominador de serviços continua dependendo de NFS-e/CFS-e ou fonte equivalente.

Além disso, mais de metade das linhas da Composição sofre corte de sigilo. O valor não suprimido é um **piso observável**, não o total integral do mercado estadual.

## 6. Diagnóstico provisório

### Fatos observados/calculados

1. O sinal NFC-e local de 2026 até 14 de setembro combina **+2,87% em documentos** com **-2,22% em valor nominal** frente ao mesmo período de 2025.
2. A Cesta regional não apresenta movimento uniforme: 44 de 80 produtos sobem e 36 caem na comparação H1, com mediana de +2,46%.
3. No benchmark estadual publicado, o núcleo de Saúde/Higiene cresce nominalmente com intensidade (+16,12%), enquanto os núcleos de Bens Essenciais (-1,27%) e Bens Não Essenciais (-2,97%) ficam abaixo de 2025.
4. As lacunas da taxonomia são numerosas em NCM8, mas pequenas em valor publicado: cerca de 0,50% na Composição e 0,57% nas Exportações.

### Interpretação

Os novos dados tornam possível sair de uma leitura exclusivamente estrutural para uma leitura de **movimento recente**, mas ainda sem medir participação de mercado municipal.

A divergência entre quantidade e valor da NFC-e merece prioridade analítica porque é um sinal diretamente municipal e contemporâneo. A próxima investigação deve separar:

- inflação/preços;
- quantidade de transações;
- valor médio;
- sazonalidade;
- eventual mudança de composição entre tipos de operação e setores.

### O que ainda não é possível concluir

Não é possível afirmar, com estas séries:

- que o consumo real de São Borja caiu em 2026;
- que o mercado de Bens Essenciais local acompanha a queda nominal observável do RS;
- que o crescimento estadual de Saúde/Higiene ocorreu em São Borja;
- market share de qualquer operador local;
- inflação municipal.

Para isso faltam, principalmente, decomposição municipal de DFe por NCM/CNAE e/ou série local de preços com metodologia própria.

## 7. Próxima etapa recomendada

Prioridade 1: construir o painel mensal 2024-2026 do DFe de São Borja, por modelo, com índices base 100 e comparações homólogas, preservando 2026 como período parcial.

Prioridade 2: construir indicadores de preço por produto da Cesta regional e cruzar apenas **variações relativas**, nunca níveis de preços entre produtos.

Prioridade 3: usar o Radar como benchmark estadual por módulos CORE/EXPANDED/ADJACENT, sempre exibindo cobertura taxonômica e sigilo ao lado do valor.

Prioridade 4: abrir auditoria específica dos 2.200 NCMs ausentes da taxonomia, começando pelos de maior valor publicado, sem atribuir grupo por inferência não validada.

## 8. Tabelas de sustentação

- `docs/caderno_base/dados/dfe_sao_borja_anual_2018_2025_v001.csv`;
- `docs/caderno_base/dados/dfe_sao_borja_ytd_2025_2026_v001.csv`;
- `docs/caderno_base/dados/cesta_fronteira_oeste_h1_2026_vs_2025_v001.csv`;
- `docs/caderno_base/dados/radar_rs_benchmark_setorial_jan_ago_2026_vs_2025_v001.csv`.

## 9. QA e governança

O workflow específico `public-market-series-curated-v1` concluiu com sucesso no run `36279321664`; todas as 17 validações internas ficaram em PASS.

No workflow geral `quality`, run `36279321683`, o job `test` concluiu com sucesso. O workflow agregado ficou vermelho porque o job independente `rfb-cnpj-territorial-control` sofreu falha de rede na aquisição externa da Receita Federal; essa falha não é atribuída à camada curated.

O **PR #41 permanece aberto, draft e sem merge**.
