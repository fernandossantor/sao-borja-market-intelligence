# Execução territorial de remuneração — RAIS 2025 × RFB 2026-08

## Objetivo

Executar a ponderação territorial de emprego e remuneração usando exclusivamente as cópias mestre já preservadas no Google Drive do projeto. Esta rotina não readquire microdados da RAIS ou da Receita Federal em fontes externas.

## Fontes operacionais

- RAIS Vínculos Sul 2025: `RAIS_VINC_PUB_SUL.7z`, Drive file ID `16NgcdvbvKLwlNoUmBpfXoeVXqGr5kOhn`, 704.888.712 bytes, SHA-256 `c537caaaa8318b04e6f4cbbc7e59b130988668b7ea58ce67a0ab2caebf2f5bd0`.
- RFB CNAE × natureza × controle territorial: `rfb_cnae_nature_territorial_cells_v001.csv`, Drive file ID `10Frn6bcdixiMiXNQpe_5ycKjDHOrmyCd`, 30.429 bytes, SHA-256 `73d53f372abda611f448970a5ea5a362f4183aee09e14b4c355c74ff7b585497`.

A origem estatística da RAIS continua sendo o MTE, ano-base 2025. A origem cadastral das células RFB continua sendo Dados Abertos CNPJ, competência 2026-08. O Drive é a fonte mestre operacional das cópias já auditadas pelo projeto.

## Regra de staging

O comando `sbmi.territorial_wage_drive_cli` usa a conta de serviço somente leitura já configurada no Codespace (`SBMI_GDRIVE_SA_B64`). Os arquivos são copiados do Drive para `.data/` somente quando a cópia local validada ainda não existe.

A promoção local ocorre apenas após conferir tamanho e SHA-256. Arquivos locais divergentes não são sobrescritos. Transferências incompletas permanecem como `.partial` para revisão.

## Recorte RAIS

O membro `RAIS_VINC_PUB_SUL.COMT` é processado em streaming. A rotina preserva as 62 colunas originais e seleciona `Município - Código = 431800`.

Controles esperados do recorte:

- 19.960 registros de São Borja;
- 62 colunas;
- universo empresarial comparável: 8.595 vínculos, após aplicar vínculo ativo em 31/12 = 1, vínculo abandonado = 0, tipo de estabelecimento = CNPJ e natureza jurídica grupo 2.

## Modelo

A remuneração e os vínculos observados pela RAIS são distribuídos entre matriz local, filial de matriz local e filial de matriz externa segundo as participações cadastrais da RFB dentro da hierarquia CNAE × natureza jurídica já auditada.

A medida remuneratória principal é a soma de `Vl Rem Média Nom` dos vínculos empresariais ativos e não abandonados. Ela não deve ser denominada massa salarial anual. A remuneração de dezembro informada é mantida como medida complementar.

A defasagem RAIS 2025 × RFB 2026-08 permanece limitação explícita.

## Execução canônica auditada

Execução: `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`.

A execução reutilizou a cópia local validada da RAIS e o recorte municipal já existente. O derivado RFB de 30.429 bytes foi staged a partir da cópia mestre do Drive. Não houve readquisição de microdados em fonte externa.

Resultados principais:

- 8.595 vínculos empresariais ativos não abandonados;
- 25,160555% do emprego estimado associado a matriz externa;
- 29,090298% da soma da remuneração média nominal estimada associada a matriz externa;
- 29,689702% da remuneração de dezembro informada estimada associada a matriz externa;
- 0 vínculos sem correspondência efetiva;
- todas as reconciliações de emprego e remuneração com diferença zero nos limites de validação.

Cobertura do match exato `CNAE subclasse × natureza jurídica`:

- 99,837115% dos vínculos;
- 99,790511% da remuneração de dezembro;
- 99,766278% da soma das remunerações médias nominais.

Os sete controles de `validation.csv` foram `PASS`.

## Saídas canônicas e hashes

A execução criou sete derivados em `.data/exports/base_territorial/territorial_wage_estimation/territorial-wage-rais2025-rfb2026-08-drive-20260907-200236/`:

- `run_metadata.csv` — 1.062 bytes — SHA-256 `88e00fc30380a7ae0ea12bd97882677d9cd45ad25a04dc05ee77497ecae448f7`;
- `source_manifest.csv` — 616 bytes — SHA-256 `334a77029b14e3a0f51be34adda280f62ec2e253440244fc8026ec9137729839`;
- `territorial_wage_by_division.csv` — 10.450 bytes — SHA-256 `c6d8fe91d95324da28ad35a77d08317309ecc3c358b6f070e21a86a9ef3e667a`;
- `territorial_wage_cells.csv` — 55.816 bytes — SHA-256 `0c2a6bb20e2a3abcca9840536639a3f2b516802d8c0cf2fffe6e83d1e109144f`;
- `territorial_wage_coverage.csv` — 680 bytes — SHA-256 `337b5e080d93b76f9dc67357c03c915ed1cb44524f72aa08d5c5ecd92b44c812`;
- `territorial_wage_summary.csv` — 1.490 bytes — SHA-256 `1c72ebfa313548050eb9d6684ea1e02ee5b05208e9a08634729d27d748ac5f1e`;
- `validation.csv` — 306 bytes — SHA-256 `3379431961f8fc030bf85c1d6ffaaf74624b37074661f7a2406b6d33e8eede7d`.

O recorte municipal intermediário possui 5.275.011 bytes e SHA-256 `a4db6fb847eacab43e883d4daaaa9f0a16e23db07d4d2f117dd90231631e5c57`.

## Promoção ao Drive

A pasta de destino dos derivados canônicos foi criada em `_sao_borja/exports/`:

- folder ID `12TDHgZ6_M63f98RMRUckTqcEA5FCRp_x`;
- nome `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`.

### Diagnóstico das tentativas com conta de serviço

A primeira tentativa foi interrompida por `403 Forbidden` quando a conta de serviço ainda possuía papel `reader`. Após a permissão ser elevada manualmente para `writer`, a segunda tentativa retornou o mesmo `403`.

A auditoria posterior confirmou que a alteração de permissão foi efetiva: a conta `sbmi-drive-reader@sao-borja-market-intelligence.iam.gserviceaccount.com` aparece como `writer` na pasta. A pasta, porém, está em **Meu Drive** (`driveId` ausente/nulo), e não em um Shared Drive.

Esse segundo bloqueio não é mais uma falha de permissão de pasta. Contas de serviço não possuem cota de armazenamento própria para assumir a propriedade de novos arquivos em Meu Drive. Para criar arquivos nesse contexto, a escrita deve ocorrer em um Shared Drive ou por OAuth 2.0 em nome de um usuário humano.

A pasta foi conferida novamente e permanece vazia: **0 de 7 arquivos promovidos**. Não houve upload parcial.

### Backend de promoção adotado

A leitura do projeto continua separada e restrita:

- `SBMI_GDRIVE_SA_B64`: conta de serviço para leitura programática;
- `sbmi-drive`: remote rclone existente com escopo `drive.readonly`.

A promoção autorizada passa a usar um segundo remote rclone, `sbmi-drive-write`, autenticado por OAuth em nome do usuário humano proprietário do Drive e restrito operacionalmente pela raiz `_sao_borja`.

A CLI `sbmi.territorial_wage_promote_drive_cli` valida os sete arquivos locais por tamanho e SHA-256. Para cada arquivo remoto existente ou recém-enviado, baixa uma cópia temporária e recalcula o SHA-256. Nomes duplicados ou qualquer divergência interrompem a promoção. A rotina não usa `sync`, não apaga arquivos e não altera dados brutos.

A configuração única do remote de escrita está documentada em `docs/drive_write_connection.md`.

Execução, depois de configurar `sbmi-drive-write`:

```bash
cd /workspaces/sbmi-cnpj-run
git fetch origin feature/cnpj-territorial-control-v1
git merge --ff-only origin/feature/cnpj-territorial-control-v1
python -m sbmi.territorial_wage_promote_drive_cli
```

## Caderno-Base sincronizado

A versão de controle corrente foi criada no Drive como `caderno_base_territorial_v006_emprego_remuneracao_20260907`, preservando a v005 como histórico. A v006 reúne, em abas próprias, resumo, emprego/remuneração, cobertura de match, validação remuneratória, manifesto de fontes/saídas e análise setorial remuneratória.

## Interpretação e limitações

Os resultados de emprego e remuneração por controle territorial são **estimativas por células CNAE × natureza jurídica**, não observações por CNPJ. A diferença entre a remuneração média implícita das estruturas externas e locais é efeito agregado de composição das células e não demonstra prêmio salarial empresa a empresa.

As participações estimadas não medem remessa de lucros, compras fora do município, valor adicionado apropriado externamente nem vazamento monetário. A RAIS 2025 e a RFB 2026-08 também não representam o mesmo período.
