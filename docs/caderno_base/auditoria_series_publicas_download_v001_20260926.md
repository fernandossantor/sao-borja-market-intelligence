# Auditoria e promoção das séries públicas de dimensão de mercado — v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica (SBMI)  
**Objeto:** séries públicas baixadas pelo workflow `download-market-dimension-public-series-v1`  
**Geografias presentes:** São Borja/RS; Rio Grande do Sul; COREDE Fronteira Oeste  
**Regra de governança:** nenhuma série estadual ou regional é convertida em market share municipal por rateio arbitrário.

## 1. Delimitação e decisão de auditoria

O checkpoint de partida foi `docs/caderno_base/checkpoint_20260926_inicio_download_series_publicas_v001.md`.

A execução inicialmente indicada, **run 36276217961**, foi verificada como concluída com sucesso técnico, no commit `037e2eb1249766aa20f04d8d4760cb3e15a542a7`, com artifact `10917522369` e digest `sha256:8b1c8f3b815cdae16d2654d2bbb3b0ebd86c7c2767a21fcf7553ba9bdb65032b`.

A auditoria, porém, identificou um erro metodológico na curadoria mensal da série DFe por CNAE: datas-fonte em padrão ISO `YYYY-MM-DD` estavam sendo submetidas a `dayfirst=True`, o que podia inverter mês e dia quando ambos eram numericamente válidos. O efeito observado foi a criação indevida de meses de 2026 posteriores ao período efetivamente disponível.

**Decisão:** o artifact do run 36276217961 é tecnicamente reproduzível, mas **não é canônico para análise** e não foi promovido ao Drive como pacote auditado.

## 2. Correção reprodutível

A rotina foi corrigida no próprio workflow, preservando o branch corrente e sem merge:

- `643cf8ef65753c32fa2fb621e335e273c7bc3814` — separação inicial de datas ISO;
- `c27ff22a3632ce2d51062024f0e5bef1e856b2a8` — reconhecimento de timestamp ISO antes do fallback;
- `88528db86652607379a5f7f76003d97552e90fbf` — correção final da expressão regular para `^\d{4}-\d{2}-\d{2}`.

A execução canônica após a correção é:

- run: **36277254947**;
- workflow: `download-market-dimension-public-series-v1`;
- commit: `88528db86652607379a5f7f76003d97552e90fbf`;
- conclusão: **success**;
- warnings de parsing de data no job final: **0**;
- artifact: **10917538784**;
- artifact digest: `sha256:c2c202561d00d516b56a6fb760c9adbbbcd68d1619d6f68928b0b3d8e11430d1`;
- pacote interno `SBMI_public_market_series_v001.zip`: `sha256:ba696b6087bc2fa8068fb3f760464ecb3b0f0c59b1ce1dde8df75c0f81712c86`.

## 3. Promoção ao Google Drive

Pasta de promoção:

- `exports/public-market-series-v001-20260926`;
- Drive folder ID: `1jDfPKy6IpnHsBf82XWcifhZtQT7kd602`.

Arquivo promovido:

- `SBMI_public_market_series_v001_GitHubActions_audited_20260926.zip`;
- Drive file ID: `1a_lJ_3IGSDocYWAxNnsPYU5KYyFcxcIg`;
- o arquivo corresponde ao artifact canônico do run 36277254947 e preserva o pacote interno produzido pelo workflow.

A aba `Rastreabilidade_v029` da planilha corrente `caderno_base_territorial_v029_integracao_setorial_v002_20260924` foi atualizada com o ID do pacote, run canônico, governança e períodos correntes.

## 4. Auditoria por série

| Série | Abrangência | Período observado | Volume auditado | Resultado | Limitação principal |
|---|---|---:|---:|---|---|
| Radar — Composição de Mercado | Rio Grande do Sul | 2024-07 a 2026-08 | 1.589.761 linhas; 11.500 NCM8 | Aprovada com controle de sigilo | Não é faturamento municipal; `corte_sigilo=1` gera valor nominal zero por supressão |
| Radar — Exportações NCM | Rio Grande do Sul | 2024-07 a 2026-08 | 426.550 linhas; 4.651 NCM8; 228 países | Aprovada com controle de granularidade | NCM×país não é chave única; não deduplicar mecanicamente |
| Radar — Portfólio NCM/Setor | Rio Grande do Sul | snapshot corrente | 1.900 linhas; 1.349 NCM8 | Aprovada como tabela auxiliar | Classificação industrial, não denominador universal de mercado |
| Cesta Alimentos | COREDE Fronteira Oeste | 2021-01 a 2026-06 | 153.120 linhas; 80 produtos por mês | Aprovada | COREDE ≠ município de São Borja |
| DFe — município | São Borja/RS | 2018-01 a 2026-09-14 | 9.536 linhas | Aprovada | Envelope fiscal por modelo/dia; não contém decomposição por NCM/CNAE municipal |
| DFe — CNAE classe | Rio Grande do Sul | 2018-01 a 2026-09 | 71.491 linhas | Aprovada após correção | Benchmark estadual; não pode ser rateado para São Borja |

## 5. Verificações de integridade

### 5.1 Manifesto e arquivos brutos preservados

O `meta/manifest.csv` contém **238 registros de tentativa/probe**. Entre os arquivos brutos efetivamente retidos no pacote para Radar e Cesta, **59 de 59** tiveram SHA-256 recalculado e coincidente com o manifesto.

Cobertura HTTP observada no download:

- Cesta Alimentos: 6 respostas 200 e 3 respostas 404;
- DFe município: 9 respostas 200;
- DFe CNAE: 9 respostas 200;
- Radar Composição: 26 respostas 200 e 79 respostas 404;
- Radar Exportações: 26 respostas 200 e 79 respostas 404;
- Radar Portfólio: 1 resposta 200.

Os ZIPs-fonte de DFe não são preservados como arquivos brutos dentro do artifact, embora seus hashes de origem estejam registrados no manifesto. A consistência das tabelas DFe curadas foi auditada separadamente.

### 5.2 Radar — Composição de Mercado

Foram auditados **26 arquivos mensais**. Não há duplicidades exatas nem duplicidades na chave candidata `cod_ncm × emit_uf × tipo_operacao`.

A variável `corte_sigilo` assume 0/1. Há **836.212 linhas suprimidas**, equivalentes a:

[
836.212 / 1.589.761 = 52,60\%
]

Todos os registros com `corte_sigilo=1` possuem `vlr_nominal=0`. Portanto, zero sob sigilo é **valor censurado**, e não evidência de ausência de atividade econômica.

Foi observada uma particularidade de formato da própria fonte em 2026: `anomes` aparece como `202.601`, `202.602`, ..., `202.608`. O mês deve ser normalizado a partir do nome do arquivo/período de referência, sem alterar o bruto preservado.

### 5.3 Radar — Exportações NCM

Foram auditados **26 arquivos mensais**, somando 426.550 linhas. Existem 250 linhas exatamente repetidas entre arquivos e 159.700 ocorrências repetidas na chave candidata `cod_ncm × cod_pais`.

Isso não autoriza exclusão automática: o grão público da fonte não é suficientemente documentado para tratar NCM×país como chave primária. Totais analíticos deverão ser agregados com regra explícita e testada, preservando a fonte mensal.

A mesma particularidade de `anomes` foi observada para 2026.

### 5.4 Radar — Portfólio NCM/Setor

A tabela possui 1.900 linhas, 1.349 NCM8 únicos, 18 classes emissoras e 49 setores. Não há duplicidades exatas, mas **371 NCMs** aparecem em mais de uma linha/setor, com até 8 associações por NCM.

Confrontada com a taxonomia canônica do Radar já preservada no projeto, a cobertura é:

[
1.333 / 1.349 = 98,81\%
]

Há 16 NCMs do Portfólio ausentes no catálogo canônico de grupos de afinidade. O Portfólio permanece, portanto, uma camada auxiliar de classificação industrial e não substitui a taxonomia NCM8 completa.

### 5.5 Cesta Alimentos — COREDE Fronteira Oeste

Os anos de 2021 a 2025 têm **27.840 linhas por ano** (= 29 COREDEs × 80 produtos × 12 meses). Em 2026 há **13.920 linhas** (= 29 × 80 × 6 meses).

Para `FRONTEIRA OESTE`, há exatamente 80 produtos em cada um dos **66 meses disponíveis**, sem duplicidade em `Data × Corede × NMProduto`, sem preços ausentes e sem preços não positivos.

O dado observado representa o COREDE Fronteira Oeste e **não deve ser rotulado como preço municipal de São Borja**.

### 5.6 DFe — São Borja

A série consolidada possui 9.536 linhas, exclusivamente para o código municipal **4318002 — São Borja**, nos modelos CT-e, NF-e e NFC-e.

2018–2025 têm cobertura anual completa. Em 2026, a série alcança **14/09/2026**. Não foram observados valores ausentes nos campos auditados, valores negativos ou duplicidades na chave `modelo_dfe × dt_emissao × cod_municipio`.

É uma medida fiscal observada de volume/valor por modelo e dia. Não oferece, sozinha, dimensão de mercado por categoria de produto.

### 5.7 DFe — CNAE classe / RS

Após a correção do parser, a série consolidada possui **71.491 linhas**. 2018–2025 cobrem janeiro a dezembro e 2026 contém apenas janeiro a setembro, coerentemente com a disponibilidade atual.

Linhas e CNAEs únicos por ano:

| Ano | Linhas | CNAEs únicos |
|---:|---:|---:|
| 2018 | 7.734 | 484 |
| 2019 | 7.935 | 486 |
| 2020 | 7.964 | 490 |
| 2021 | 8.098 | 485 |
| 2022 | 8.188 | 487 |
| 2023 | 8.233 | 487 |
| 2024 | 8.195 | 487 |
| 2025 | 8.459 | 496 |
| 2026 | 6.685 | 509 |

Não há datas inválidas, valores negativos, duplicidades exatas nem duplicidades na chave mensal `modelo_dfe × mês × CNAE`. Em 2026 existem 27 linhas classificadas pelo provedor como `Outros`; essa categoria deve ser preservada, e não convertida artificialmente em código CNAE.

A correção alterou apenas a alocação intra-anual dos meses: os totais anuais de quantidade permaneceram idênticos e as diferenças de valor ficaram restritas a arredondamento de ponto flutuante.

## 6. Classificação analítica

**Dados observados:** arquivos públicos, períodos, geografia, linhas, valores, códigos, indicadores de sigilo e metadados de download.

**Dados calculados:** contagens, cobertura, taxas de supressão, duplicidades e correspondência entre taxonomias.

**Interpretação:** Radar e DFe CNAE oferecem benchmarks estaduais; Cesta oferece referência regional; DFe municipal oferece envelope fiscal local. Nenhuma das três escalas deve ser confundida.

**Hipótese ainda não testada:** a combinação dessas séries poderá aumentar a precisão da leitura de dimensão de mercado e sazonalidade dos cadernos, desde que a integração preserve geografia, conceito e grão.

## 7. Regras para integração futura

1. Preservar os arquivos brutos e seus hashes.
2. Criar derivados normalizados separados, especialmente para `anomes` e números com separador de milhar.
3. Não substituir censura fiscal por zero econômico.
4. Não ratear DFe CNAE estadual para São Borja.
5. Não tratar Cesta COREDE como índice de preços municipal.
6. Usar DFe municipal como envelope observado por modelo/data, não como market share setorial.
7. Se for produzido um denominador municipal por produto/setor, exigir fonte agregada municipal compatível com NCM/CNAE ou método explicitamente identificado como estimativa.

## 8. Governança

O **PR #41 permanece aberto, draft e sem merge**. Esta auditoria não autoriza merge.

Artifacts anteriores à correção permanecem apenas como evidência de execução e não devem ser usados como fonte canônica. O pacote promovido ao Drive e registrado na `Rastreabilidade_v029` é o do run **36277254947**.
