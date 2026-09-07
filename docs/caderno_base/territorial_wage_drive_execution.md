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

## Execução no worktree correto

```bash
cd /workspaces/sbmi-cnpj-run
git fetch origin feature/cnpj-territorial-control-v1
git merge --ff-only origin/feature/cnpj-territorial-control-v1
python -m sbmi.territorial_wage_drive_cli
```

Se as cópias locais da RAIS e do derivado RFB já estiverem validadas, a rotina as reutiliza e não transfere novamente o conteúdo do Drive.

## Saídas

Cada execução cria uma pasta nova em `.data/exports/base_territorial/territorial_wage_estimation/` contendo:

- `territorial_wage_cells.csv`;
- `territorial_wage_coverage.csv`;
- `territorial_wage_by_division.csv`;
- `territorial_wage_summary.csv`;
- `validation.csv`;
- `source_manifest.csv`;
- `run_metadata.csv`.

O manifesto registra os IDs das fontes mestre do Drive, tamanhos e SHA-256 das entradas e do recorte municipal.

## Benchmarks de auditoria

Antes de promover qualquer resultado à narrativa do Caderno-Base, a execução deve reproduzir aproximadamente:

- 8.595 vínculos empresariais;
- 25,1606% do emprego estimado associado a matriz externa;
- 29,0903% da soma da remuneração média nominal estimada associada a matriz externa;
- 29,6897% da remuneração de dezembro informada estimada associada a matriz externa.

Essas participações são **estimativas**, não observações empresa a empresa, e não medem remessa de lucros, compras fora do município ou vazamento monetário.
