# Migração estrutural do Google Drive — 2026-09-05

## Objeto

Registrar a reorganização controlada da pasta Google Drive `_sao_borja/new_files`,
sem alterar conteúdo, nome, ID ou bytes dos itens migrados.

A migração foi autorizada pelo responsável pelo projeto em 2026-09-05, após
inspeção da árvore atual e elaboração prévia do mapa de migração.

## Escopo e limites

A migração ficou restrita à pasta `new_files`, ID
`14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`, cujo pai foi confirmado como
`_sao_borja`, ID `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.

Não foram movidos ou alterados os ramos históricos `raw`, `processed`,
`warehouse`, `exports` e `governance` da raiz `_sao_borja`.

Nenhum item foi excluído, sobrescrito ou renomeado. As operações de migração
alteraram somente o parent no Google Drive e preservaram os IDs dos itens.

## Princípio funcional

A árvore de `new_files` separa cinco naturezas:

1. `01_fontes_e_coletas`: entradas e fontes, organizadas preferencialmente por
   domínio e provedor/origem;
2. `02_execucoes_tecnicas`: execuções identificadas por run ID, inclusive
   `raw`, `staging`, `audit`, manifestos e artefatos intermediários;
3. `03_bases_sistematizadas`: bases consolidadas e validadas destinadas à
   consulta e análise;
4. `04_apresentacoes`: produtos de síntese e apresentação;
5. `05_integracao_bi`: produtos específicos para integração com BI.

A taxonomia temática é criada apenas quando existe conteúdo concreto, evitando
diretórios vazios antecipados.

## Pastas criadas

| Caminho relativo em `new_files` | ID Drive |
| --- | --- |
| `01_fontes_e_coletas/demografia` | `1zi8wR9opH7uosIyqz-wayZQCDRQqvQa2` |
| `01_fontes_e_coletas/demografia/eventos_vitais` | `1cDVdiXPvsEPdeTFcfqwQ6DeF4eFWDSSM` |
| `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil` | `1hPVQ4vSsHeUkoz8QstgKF1K6mxDFyv4w` |
| `02_execucoes_tecnicas/economia` | `1h5yb5QVRMDQnBocBcUS_FiHTwY5sVvYi` |
| `02_execucoes_tecnicas/economia/v005-economic-go-xlsx-20260815-001` | `1pNi0cVgU3vC4VmR4sO2w-LPoRdE0yOd3` |
| `02_execucoes_tecnicas/financas_publicas` | `16IXTuC3H4EM9UdIuMfQQRPCBDmUe9Gvq` |
| `03_bases_sistematizadas/demografia` | `1NB_mgY38oLwaAmh5KwYoasyBjhAJTY_C` |
| `03_bases_sistematizadas/transversal` | `1Tu1DNLnQ-E2_wravty96ARonwd3J0TiK` |
| `04_apresentacoes/fotografia_cenario` | `1fmaqHqcs-KN83UUjgKZ63Ey8p_Xj1CNF` |

## Movimentos executados

| ID Drive preservado | Item | Parent anterior | Parent atual | Classificação |
| --- | --- | --- | --- | --- |
| `1rWJZY2ZaB6PpULOgGorObK_qRnJwLGr8` | `São Borja — PIB IBGE — 2026-08-15 — economic-go-001.xlsx` | `01_fontes_e_coletas/economia` (`13nbc6JpBpNjoF2mLs4kzh9fg3pHI9k5O`) | `02_execucoes_tecnicas/economia/v005-economic-go-xlsx-20260815-001` (`1pNi0cVgU3vC4VmR4sO2w-LPoRdE0yOd3`) | produto técnico, `EXPECTED_CHANGE` de caminho |
| `1RoOhiAJwMyw9y3GrnYNeCMOzqGj9mI4g` | `state-rs-expense-2026-01-04-20260730-003514` | `01_fontes_e_coletas/financas_publicas` (`1R_fBdL13atSd2I6HZ_EMrtrv99ZwQtlT`) | `02_execucoes_tecnicas/financas_publicas` (`16IXTuC3H4EM9UdIuMfQQRPCBDmUe9Gvq`) | execução técnica |
| `10eUtyJIGWJkzitvpJKLJ1keThUm0yc88` | `state-rs-public-funds-20260729-235709` | `01_fontes_e_coletas/financas_publicas` | `02_execucoes_tecnicas/financas_publicas` | execução técnica |
| `1Om-20OXb2pNDpBTTww1WxebUuSTqiWLv` | `state-rs-catalog-discovery-20260729-231506` | `01_fontes_e_coletas/financas_publicas` | `02_execucoes_tecnicas/financas_publicas` | execução técnica; contém metadados, validação e manifesto de upload |
| `1CZaNYqXtQ4Lz41dSbrblgV_q57RK9ui_` | `eventos_vitais` | `03_bases_sistematizadas` (`1AYQUhk16QzJhUI5qOSqGTqJcD6qNeO3p`) | `03_bases_sistematizadas/demografia` (`1NB_mgY38oLwaAmh5KwYoasyBjhAJTY_C`) | contêiner temático de bases sistematizadas |
| `196XhNcXmP17YH8Yq0EECb4GsHg11wP70` | `tabela2609.xlsx` | `03_bases_sistematizadas/demografia/eventos_vitais/nascimentos_obitos` (`1a4FhtEn49fp7RxnWiYPoNlbDtsO9ymzN`) | `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil` (`1hPVQ4vSsHeUkoz8QstgKF1K6mxDFyv4w`) | fonte IBGE — Registro Civil |
| `1WkxPmRxKdlxwWC1_mxrBwJPPjeIOYNNy` | `tabela2612.xlsx` | mesmo parent anterior | mesmo parent atual de fontes IBGE | fonte IBGE — Registro Civil |
| `1I_8Rig9TtfZHo8janCpRjz0WNcANu1o_` | `tabela2654.xlsx` | mesmo parent anterior | mesmo parent atual de fontes IBGE | fonte IBGE — Registro Civil |
| `1GmYJEeeXQYw6Aw0RsWwluwO14XY6V6D8` | `base_historica` | `03_bases_sistematizadas` | `03_bases_sistematizadas/transversal` (`1Tu1DNLnQ-E2_wravty96ARonwd3J0TiK`) | base sistematizada transversal |
| `1edRFS0Qjn-remMPBKD7-D7Z0SVLGHrJ1W-5kzra4YYw` | `São Borja — Fotografia do Cenário — 2026-08-12` | `03_bases_sistematizadas/apoio` (`1nfAPzfJeU6-0BoIO9VqfWHmXkodabZr6`) | `04_apresentacoes/fotografia_cenario` (`1fmaqHqcs-KN83UUjgKZ63Ey8p_Xj1CNF`) | síntese descritiva de apresentação |

## Decisão de parcimônia para eventos vitais

O mapa preliminar previa mover individualmente as duas bases sistematizadas de
eventos vitais. Na execução, foi adotada uma solução mais conservadora: mover o
contêiner `eventos_vitais` inteiro para o novo domínio `demografia` e retirar
dele apenas as três fontes brutas IBGE.

Assim, permaneceram no mesmo parent imediato `nascimentos_obitos`, ID
`1a4FhtEn49fp7RxnWiYPoNlbDtsO9ymzN`, mas passaram a estar sob o caminho
semântico correto:

- `São Borja — Eventos Vitais e População — 1996–2024 — 003`, ID
  `1F9ucOO4g20z0kqQSqCdZY72i5APVQYcPzLSr_248POo`;
- `sao_borja_nascimentos_obitos_saldo_1996_2026.xlsx`, ID
  `17Kosn8CIf7FU1FWCG-l8qHBhh3uk_gMj`.

Essa alternativa reduziu o número de mudanças de parent e preservou melhor a
estrutura interna já existente.

## Estrutura pós-migração validada

Foi verificado que:

- `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil` contém
  exatamente as três tabelas IBGE 2609, 2612 e 2654, com os mesmos IDs;
- `02_execucoes_tecnicas/economia/v005-economic-go-xlsx-20260815-001` contém o
  produto `economic-go-001.xlsx`, com o mesmo ID;
- `02_execucoes_tecnicas/financas_publicas` contém as três execuções estaduais
  previstas, com os mesmos IDs;
- `03_bases_sistematizadas/demografia/eventos_vitais/nascimentos_obitos`
  contém as duas bases sistematizadas de eventos vitais e não contém mais as
  três fontes IBGE;
- `03_bases_sistematizadas/transversal` contém `base_historica`;
- `04_apresentacoes/fotografia_cenario` contém a Fotografia do Cenário;
- `01_fontes_e_coletas/economia` preserva as fontes `pib_sao_borja_2002_2023.csv`
  e `sidra_manifest_pib_sao_borja_20260731.json`;
- `01_fontes_e_coletas/financas_publicas` ficou vazio e foi preservado como
  área de entrada futura, sem exclusão;
- `03_bases_sistematizadas/apoio` ficou vazio e foi preservado, sem exclusão.

## Compatibilidade do código

A função `source_from_path` foi ajustada para preservar os caminhos históricos
`raw/new_files/Federal`, `Estadual` e `Municipal`, mas não tratar
`01_fontes_e_coletas`, `02_execucoes_tecnicas`, `03_bases_sistematizadas`,
`04_apresentacoes` ou `05_integracao_bi` como nomes de fonte.

Na árvore funcional:

- somente `01_fontes_e_coletas` pode declarar uma origem de fonte;
- `Federal`, `Estadual` e `Municipal` continuam reconhecidos quando aparecem em
  subpastas de fontes;
- provedores explícitos, como `ibge_registro_civil`, podem ser identificados
  pela pasta imediatamente anterior ao arquivo;
- execuções técnicas, bases sistematizadas, apresentações e integrações BI não
  são interpretadas como fontes do staging fiscal histórico.

O staging fiscal também passou a ignorar explicitamente perfis fora de seus
contratos históricos, sem relaxar a exigência de contrato para uma fonte
Federal, Estadual ou Municipal reconhecida.

## Validação do repositório

As alterações foram feitas na branch `chore/drive-migration-20260905`, sem
escrita direta em `main`, e submetidas ao PR #40.

O workflow `quality` do GitHub Actions, que executa Ruff em `src/sbmi` e `tests`
e a suíte completa de `pytest`, concluiu com `success` antes da movimentação
física do Drive.

## Natureza da mudança

A migração não alterou valores, séries, metodologias, nomes ou conteúdos dos
datasets. Trata-se de mudança de organização e proveniência de caminho.

Classificação: `EXPECTED_CHANGE`.

Não foram observadas diferenças analíticas produzidas por esta operação.
