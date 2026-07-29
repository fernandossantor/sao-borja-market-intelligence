# Descoberta histórica de metadados SIDRA

## Objetivo

Identificar cobertura oficial potencial para São Borja entre 1996 e 2026 sem
criar dimensões, consultar valores ou promover dados. A rotina captura apenas
os descritores oficiais de dez tabelas previamente selecionadas.

## Dimensões existentes utilizadas

- `demografia`;
- `economia_estrutura_produtiva`;
- `renda_emprego_trabalho`;
- `ambiente_sociocultural_territorial`.

As demais dimensões do mapa territorial permanecem sem tabela confirmada nesta
etapa. Correspondência temática não é tratada como equivalência conceitual.

## Tabelas

| Tabela | Pesquisa | Dimensão associada | Disponibilidade observada em 2026-07-29 |
|---|---|---|---|
| 156 | Censo Demográfico | demografia; sociocultural | 1991, 2000, 2010 |
| 289 | PEVS — extração vegetal | economia | 1986 a 2025 |
| 291 | PEVS — silvicultura | economia | 1986 a 2025 |
| 3939 | PPM | economia | 1974 a 2025 |
| 5457 | PAM | economia | 1974 a 2025 |
| 5938 | PIB dos Municípios | economia | 2002 a 2023 |
| 6449 | CEMPRE | economia; trabalho | 2006 a 2021 |
| 6450 | CEMPRE | economia; trabalho | 2006 a 2021 |
| 6579 | Estimativas de População | demografia | 21 anos descontínuos de 2001 a 2025 |
| 9514 | Censo Demográfico | demografia; sociocultural | 2022 |

## Saídas

Snapshots imutáveis:

```text
.data/snapshots/web/sidra_historical_metadata/<snapshot_id>/
```

Auditoria:

```text
.data/audit/base_territorial/sidra_historical_discovery/<run_id>/
```

Os registros separam tabelas, períodos, variáveis, classificações, categorias,
limitações, planos de consulta e resumo. O manifesto registra URL, data de
obtenção, HTTP, tipo de conteúdo, tamanho e SHA-256. Os planos de consulta são
validados contra os descritores e publicados como `PREPARED_NOT_EXECUTED`.

O primeiro plano agropecuário contém:

- tabela 5457: 14 produtos e cinco variáveis, 1996 a 2025;
- tabela 3939: nove categorias atuais e uma variável, 1996 a 2025;
- tabela 291: sete categorias observadas localmente e somente quantidade
  produzida, 1996 a 2025.

A tabela 289 permanece no registro de metadados, mas fica fora do primeiro lote
porque extração vegetal não equivale ao produto local de silvicultura.

## Limitações

- nível municipal não comprova a existência de valores para São Borja;
- disponibilidade da tabela não comprova disponibilidade de toda categoria;
- não há dados de 2026 nas tabelas selecionadas;
- não há validação de comparabilidade temporal ou equivalência conceitual;
- as URLs `/values` são apenas planejadas e não são requisitadas;
- nenhum arquivo é escrito no Google Drive.

## Execução

```bash
make discover-base-territorial-sidra-historical-metadata
```
