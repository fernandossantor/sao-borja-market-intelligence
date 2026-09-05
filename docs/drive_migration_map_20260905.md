# Migração estrutural do Google Drive — 2026-09-05

## Objeto

Registrar a reorganização controlada da pasta Google Drive `_sao_borja/new_files`,
sem alterar conteúdo, nome, ID ou bytes dos itens migrados.

A migração foi autorizada pelo responsável pelo projeto em 2026-09-05, após
inspeção da árvore atual e elaboração prévia do mapa de migração.

## Limites do escopo

A migração se restringe à pasta `new_files`, ID
`14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`, cujo pai autorizado é `_sao_borja`, ID
`1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.

Não integram esta migração física:

- `raw` histórico;
- `processed` histórico;
- `warehouse` histórico;
- `exports` histórico;
- `governance`.

Nenhum item pode ser excluído, sobrescrito ou renomeado. A movimentação deve
preservar o ID de cada item no Google Drive.

## Princípio funcional

A árvore de `new_files` passa a separar cinco naturezas:

1. `01_fontes_e_coletas`: entradas e fontes, preferencialmente organizadas por
   domínio e provedor/origem;
2. `02_execucoes_tecnicas`: execuções identificadas por run ID, incluindo
   `raw`, `staging`, `audit`, manifestos e artefatos intermediários;
3. `03_bases_sistematizadas`: bases consolidadas e validadas destinadas à
   consulta e análise;
4. `04_apresentacoes`: produtos de síntese e apresentação;
5. `05_integracao_bi`: produtos específicos para integração com BI.

A taxonomia temática deve ser criada apenas quando houver conteúdo concreto,
evita-se antecipar diretórios vazios.

## Mapa autorizado

| ID Drive | Item | Natureza observada | Destino relativo em `new_files` | Decisão |
| --- | --- | --- | --- | --- |
| `1rWJZY2ZaB6PpULOgGorObK_qRnJwLGr8` | `São Borja — PIB IBGE — 2026-08-15 — economic-go-001.xlsx` | produto técnico preparado pela execução `v005-economic-go-xlsx-20260815-001`, não fonte bruta | `02_execucoes_tecnicas/economia/v005-economic-go-xlsx-20260815-001/` | MOVE |
| `1RoOhiAJwMyw9y3GrnYNeCMOzqGj9mI4g` | `state-rs-expense-2026-01-04-20260730-003514` | execução técnica com `raw`, `staging`, `audit` e inventário | `02_execucoes_tecnicas/financas_publicas/` | MOVE |
| `10eUtyJIGWJkzitvpJKLJ1keThUm0yc88` | `state-rs-public-funds-20260729-235709` | execução técnica com `raw`, `staging` e auditorias | `02_execucoes_tecnicas/financas_publicas/` | MOVE |
| `1Om-20OXb2pNDpBTTww1WxebUuSTqiWLv` | `state-rs-catalog-discovery-20260729-231506` | execução técnica; contém `state_rs_catalog_metadata.csv`, `validation.csv` e `drive_upload_manifest.csv` | `02_execucoes_tecnicas/financas_publicas/` | MOVE |
| `1GmYJEeeXQYw6Aw0RsWwluwO14XY6V6D8` | `base_historica` | base sistematizada transversal, com versões v001–v004 | `03_bases_sistematizadas/transversal/` | MOVE |
| `196XhNcXmP17YH8Yq0EECb4GsHg11wP70` | `tabela2609.xlsx` | fonte IBGE — Pesquisa Estatísticas do Registro Civil — nascidos vivos | `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil/` | MOVE |
| `1WkxPmRxKdlxwWC1_mxrBwJPPjeIOYNNy` | `tabela2612.xlsx` | fonte IBGE — Pesquisa Estatísticas do Registro Civil — nascidos vivos ocorridos no ano | `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil/` | MOVE |
| `1I_8Rig9TtfZHo8janCpRjz0WNcANu1o_` | `tabela2654.xlsx` | fonte IBGE — Pesquisa Estatísticas do Registro Civil — óbitos ocorridos no ano | `01_fontes_e_coletas/demografia/eventos_vitais/ibge_registro_civil/` | MOVE |
| `17Kosn8CIf7FU1FWCG-l8qHBhh3uk_gMj` | `sao_borja_nascimentos_obitos_saldo_1996_2026.xlsx` | base analítica sistematizada; integra SINASC/SIM, saldo natural, contrafactual e cenários migratórios | `03_bases_sistematizadas/demografia/eventos_vitais/` | MOVE |
| `1F9ucOO4g20z0kqQSqCdZY72i5APVQYcPzLSr_248POo` | `São Borja — Eventos Vitais e População — 1996–2024 — 003` | base sistematizada com série anual, validação e fontes | `03_bases_sistematizadas/demografia/eventos_vitais/` | MOVE |
| `1edRFS0Qjn-remMPBKD7-D7Z0SVLGHrJ1W-5kzra4YYw` | `São Borja — Fotografia do Cenário — 2026-08-12` | síntese descritiva transversal destinada à leitura/apresentação, com capa, resumo e abas temáticas | `04_apresentacoes/fotografia_cenario/` | MOVE |

## Itens preservados no local atual

Permanecem sem movimentação:

- `01_fontes_e_coletas/empresas`;
- `02_execucoes_tecnicas/complementacao_20260729` e suas execuções históricas;
- `04_apresentacoes/atual`;
- `04_apresentacoes/historico`;
- `05_integracao_bi/looker`.

## Compatibilidade do código

A função `source_from_path` deve preservar os caminhos históricos
`raw/new_files/Federal`, `Estadual` e `Municipal`, mas não pode tratar
`01_fontes_e_coletas`, `02_execucoes_tecnicas`, `03_bases_sistematizadas`,
`04_apresentacoes` ou `05_integracao_bi` como nomes de fonte.

Na árvore funcional:

- somente `01_fontes_e_coletas` pode declarar uma origem de fonte;
- `Federal`, `Estadual` e `Municipal` continuam reconhecidos quando aparecem em
  subpastas de fontes;
- provedores explícitos, como `ibge_registro_civil`, podem ser identificados
  pela pasta imediatamente anterior ao arquivo;
- execuções técnicas, bases sistematizadas, apresentações e integrações BI não
  devem ser interpretadas como fontes do staging fiscal histórico.

O staging fiscal deve ignorar explicitamente perfis fora de seus contratos
históricos, sem relaxar a exigência de contrato para uma fonte Federal,
Estadual ou Municipal reconhecida.

## Procedimento de execução

Antes de cada movimento:

1. confirmar o ID de `new_files` e seu pai `_sao_borja`;
2. confirmar o ID e o pai atual do item;
3. confirmar a existência do destino e ausência de colisão nominal;
4. registrar o par origem → destino;
5. executar somente mudança de parent, sem `file_uri` e sem alteração de nome;
6. reler os metadados do item e confirmar o novo pai;
7. confirmar que o ID permaneceu inalterado.

Se qualquer verificação falhar, interromper o movimento daquele item e não
compensar com exclusão ou sobrescrita.

## Estratégia de reversão

Como a operação altera apenas o parent do mesmo ID, a reversão consiste em
restaurar o parent imediatamente anterior registrado neste mapa/relato, sem
renomear ou recriar o item. A reversão também exige verificação prévia de
colisão e preservação do ID.

## Validação técnica

A alteração de código associada deve ser validada por:

- lint de `src/sbmi` e `tests`;
- suíte `pytest`;
- fluxo de qualidade equivalente a `make verify`;
- inspeção pós-migração dos IDs e pais no Drive.

A movimentação física não modifica os valores dos datasets e, portanto, não
constitui atualização de série, metodologia ou resultado analítico. Ela é uma
mudança de organização e proveniência de caminho, classificada como
`EXPECTED_CHANGE` quando os IDs e conteúdos permanecem preservados.
