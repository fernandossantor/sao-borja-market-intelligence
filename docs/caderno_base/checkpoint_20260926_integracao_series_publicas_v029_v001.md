# Checkpoint — integração das séries públicas na v029 — 26/09/2026

## 1. Estado de governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`.
- Branch de trabalho: `feature/cnpj-territorial-control-v1`.
- Head antes deste checkpoint: `c78d0a7fb1a4426b56a40bbc8c44342042fcd4bd`.
- PR #41: **OPEN / DRAFT / UNMERGED**.
- Base do PR: `main`.
- Regra: **não mesclar o PR #41 sem autorização explícita**.

## 2. Pacote público original auditado

Run canônico de download: `36277254947`.

- Conclusão: SUCCESS.
- Commit de origem: `88528db86652607379a5f7f76003d97552e90fbf`.
- Artifact original: `sbmi-public-market-series-v1`.
- Drive — pasta: `1jDfPKy6IpnHsBf82XWcifhZtQT7kd602`.
- Drive — pacote: `1a_lJ_3IGSDocYWAxNnsPYU5KYyFcxcIg`.
- Documento metodológico inicial: `1C5zrHI1YBpo9BDhChm6euPjoMt1XwgvmokZyDY1iFiM`.

O run anterior `36276217961` continua apenas como evidência de proveniência e foi rejeitado como canônico porque o parser DFe/CNAE invertia dia/mês em datas ISO.

## 3. Camada curated/normalized

Run canônico: `36279321664`.

- Conclusão: SUCCESS.
- Commit: `3b7187d5453a4250699befbb9061ec39b33cdd61`.
- Artifact: `10918776468`.
- Artifact digest: `sha256:2e1bb9d99c6dbc3bb55b1da604f5297c8b2de547a39c39f3ba53735a357f9aed`.
- Pacote interno SHA-256: `6f321b4b27deb2410e9be49c22d9f3429fdaaa20e8ed6f5edaaa3d153ded7275`.
- Drive — pasta: `1GwgMVh7xR2tjvIc88o0aqxaIBGLHTdzO`.
- Drive — pacote: `1cgXbasRdPJy005ePYrHiXxLdkHCq0qjg`.

Validações principais: 17 PASS.

Correção importante incorporada: em 2026 o Radar apresenta valores como `129.639` e `3.020.306`; o ponto é separador de milhares. A camada normalizada remove esse separador em 2026 sem alterar os arquivos brutos.

Escalas preservadas:

1. São Borja/RS — DFe municipal.
2. COREDE Fronteira Oeste — Cesta Alimentos.
3. Rio Grande do Sul — Radar + DFe/CNAE.

Nenhuma delas é convertida automaticamente em market share municipal.

## 4. Camada analítica reprodutível

Run canônico: `36280101723`.

- Workflow: `public-market-series-analysis-v1`.
- Conclusão: SUCCESS.
- Commit: `c78d0a7fb1a4426b56a40bbc8c44342042fcd4bd`.
- Artifact: `10918593126`.
- Artifact digest: `sha256:a32f762dc32df2ac2a527a2c09ae925bb15d9263d9bfd61f217203bae7055136`.
- Pacote interno SHA-256: `4197322fceebca6078b376052499ec34053eb2fab77521ddde0b03ab7e89da6e`.
- Drive — pasta: `1SWeGUxQSRXXFYhv5jM9qPsLPiBjE4O4O`.
- Drive — pacote: `1dDvH2zQZVRXt9kd6gBuZ1Y10TFC6cYqB`.

Validações da camada analítica: 8 PASS.

O workflow geral `quality`, run `36280101712`, ficou FAILURE porque o job independente `rfb-cnpj-territorial-control` sofreu falha de rede externa; o job `test` concluiu SUCCESS. A falha agregada não invalida a camada analítica.

Arquivos principais da camada analítica:

- `dfe_sao_borja_painel_mensal_2024_2026.csv`;
- `dfe_sao_borja_ytd_comparavel.csv`;
- `cesta_fronteira_oeste_yoy_produto_mensal.csv`;
- `cesta_fronteira_oeste_yoy_distribuicao_mensal.csv`;
- `cesta_fronteira_oeste_h1_2026_vs_2025.csv`;
- `radar_rs_benchmark_setor_status_mensal.csv`;
- `radar_taxonomia_gap_prefixo2.csv`.

## 5. Diagnóstico já documentado

GitHub:

- `docs/caderno_base/diagnostico_series_publicas_v001_20260926.md`;
- tabelas de sustentação em `docs/caderno_base/dados/`.

Google Drive:

- documento `Diagnóstico inicial — séries públicas normalizadas — 20260926`;
- ID `1P3o71iNxsWIo7vlftYTfoQyxVn1Zx6XPPi6LthP-npA`.

Fatos/calculados já registrados:

- DFe São Borja — 01/01 a 14/09/2026 vs mesmo período de 2025:
  - CT-e: quantidade +15,47%; valor nominal +29,11%; valor médio +11,81%;
  - NF-e: quantidade +13,30%; valor nominal +17,24%; valor médio +3,48%;
  - NFC-e: quantidade +2,87%; valor nominal -2,22%; valor médio -4,95%.
- Cesta — COREDE Fronteira Oeste, H1/2026 vs H1/2025:
  - 80 produtos;
  - mediana das variações +2,46%;
  - média simples +2,28%;
  - 44 produtos em alta e 36 em queda;
  - estes números **não constituem índice de inflação**.
- Radar RS — jan–ago/2026 vs jan–ago/2025, valor nominal publicado não suprimido:
  - Bens Essenciais / CORE: -1,27%;
  - Bens Não Essenciais / CORE: -2,97%;
  - Saúde/Higiene/Cuidados Pessoais / CORE: +16,12%;
  - Serviços / ADJACENT: +6,48%.
- Cobertura taxonômica monetária da Composição: 99,50%.
- A lacuna monetária da Composição está 99,96% concentrada no prefixo NCM 29; não houve imputação automática.

## 6. Caderno-Base v029 — estado das abas

Planilha: `caderno_base_territorial_v029_integracao_setorial_v002_20260924`.

ID: `1CHn1JZ-IcDxG3V9M5y0PKvN5lTkcvlVcov_vVw3je3c`.

Foram criadas **e já estão preenchidas**:

### `Series_publicas_v029`

- sheetId: `2011733761`;
- preenchida até a linha 57;
- contém DFe São Borja, Cesta Fronteira Oeste, benchmark Radar/RS, controles de cobertura/sigilo e diagnóstico provisório.

### `Auditoria_series_v029`

- sheetId: `1354348657`;
- preenchida até a linha 25;
- contém oito checks PASS, linhagem, regras de comparabilidade e lista dos arquivos analíticos preservados.

**Nota sobre o timeout:** após a mensagem `ChatGPT stream recovery polling timed out`, foi feita verificação direta. As duas abas não ficaram vazias: o preenchimento havia sido concluído antes da perda do stream. Não refazer a criação nem sobrescrever essas abas sem auditoria prévia.

## 7. Rastreabilidade v029

A aba `Rastreabilidade_v029` já registra:

- pacote público auditado;
- nota metodológica;
- camada curated;
- diagnóstico no Drive;
- diagnóstico e tabelas no GitHub.

Ao retomar, registrar também explicitamente:

- o pacote da camada analítica `1dDvH2zQZVRXt9kd6gBuZ1Y10TFC6cYqB`;
- este checkpoint;
- a integração das abas `Series_publicas_v029` e `Auditoria_series_v029`.

## 8. Ponto exato para retomada

**Não recomeçar download, normalização ou camada analítica.**

Retomar pela integração editorial/analítica da v029:

1. auditar visual e semanticamente as abas `Series_publicas_v029` e `Auditoria_series_v029`;
2. incorporar os achados consolidados em `Resumo_v029`, `Teses_transversais_v029`, `Factsheets_v029`, `Storyboards_v029` e `QA_argumentativo_v029`, sem misturar escalas territoriais;
3. substituir a linha “Próxima análise” da aba `Series_publicas_v029` por tarefas ainda realmente pendentes, porque o painel mensal DFe, as variações da Cesta e o benchmark mensal Radar já foram produzidos na camada analítica;
4. abrir a auditoria específica dos NCM8 ausentes, começando pelo prefixo NCM 29 e priorizando valor publicado;
5. somente depois avaliar novas hipóteses explicativas e relações entre DFe local, preços regionais e benchmarks estaduais, sem inferir causalidade.

## 9. Regras que permanecem obrigatórias

- bruto imutável;
- observado ≠ calculado ≠ interpretação;
- valores Radar sob sigilo são censurados, não zeros econômicos;
- COREDE ≠ São Borja;
- RS ≠ São Borja;
- CT-e, NF-e e NFC-e não são somados para formar market share;
- variações simples de preços não são inflação;
- NCM ausente não recebe classificação por inferência automática;
- PR #41 permanece OPEN / DRAFT / UNMERGED.
