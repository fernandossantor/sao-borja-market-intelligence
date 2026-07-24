# Mapa de cobertura da Base Territorial Comum

## Objetivo

Identificar o que já existe no acervo do projeto antes de abrir novas coletas externas ou reconstruir produtos históricos.

O mapa reúne três tipos de evidência:

1. metadados do inventário recursivo do Google Drive;
2. resultados das auditorias e validações locais já concluídas;
3. presença de módulos curados da Base Territorial Comum no Codespace.

Ele não substitui a validação metodológica de cada fonte.

## Blocos analíticos

O mapa organiza os candidatos nos seguintes blocos internos:

- demografia;
- economia e estrutura produtiva;
- renda, emprego e trabalho;
- educação;
- infraestrutura e conectividade;
- finanças públicas e transferências governamentais;
- saúde e condições sociais;
- ambiente político e regulatório;
- ambiente sociocultural e territorial;
- indicadores transversais e multitemáticos.

Esses blocos são categorias analíticas internas e não nomenclaturas oficiais das fontes.

## Tratamento de `raw/new_files`

A pasta `raw/new_files` não é classificada como lacuna integral.

Ela já foi:

- inventariada;
- capturada seletivamente;
- auditada estruturalmente;
- transformada em seis datasets de staging;
- validada quanto a contratos, proveniência, tipos e reconciliação.

Os seis contratos são:

```text
federal_transferencias
estadual_icms
estadual_transferencias
municipal_despesas_instituicao
municipal_despesas_elemento
municipal_receita_elemento
```

Por isso, todos os arquivos sob `raw/new_files` recebem classificação explícita no bloco **Finanças públicas e transferências governamentais**. Palavras como saúde ou educação no nome de um programa não alteram o bloco primário da fonte, embora possam ser relevantes em análises secundárias posteriores.

A cobertura registrada é técnica. Ainda faltam:

- documentação conceitual das medidas;
- confirmação explícita das unidades monetárias;
- confirmação da abrangência geográfica de cada contrato;
- análise de comparabilidade entre fontes federais, estaduais e municipais;
- construção da camada curada temática;
- revisão das 29 linhas de ICMS já sinalizadas na fonte.

## Regras de classificação

### Dados observados

- caminhos e nomes de arquivos;
- extensões;
- tamanhos;
- hashes disponíveis;
- estágios do acervo: `raw`, `processed`, `warehouse` e `exports`;
- contratos de staging e resultados das validações;
- famílias históricas já auditadas;
- módulos locais já existentes.

### Dados calculados

- família de origem derivada do caminho;
- bloco analítico primário;
- blocos adicionais encontrados por palavras-chave;
- contagens de arquivos, famílias e bytes;
- status técnico de cobertura;
- classe de lacuna operacional.

### Estimativas e heurísticas

A classificação por palavras-chave é uma heurística de triagem. Ela não comprova:

- conteúdo substantivo do arquivo;
- adequação metodológica;
- atualidade;
- comparabilidade temporal ou territorial;
- completude do bloco.

O mapa registra o método e a base de classificação de cada arquivo para permitir revisão.

### Regras explícitas

- `raw/new_files/*` → finanças públicas e transferências;
- `raw/social/*` → saúde e condições sociais;
- `governance/*` → documentação não contabilizada como candidato analítico.

Os demais arquivos são classificados por regras de palavras-chave. Arquivos não reconhecidos permanecem como `nao_classificado` e devem ser revisados antes de concluir que há uma lacuna.

## Calibração após revisão manual

A primeira execução real identificou 131 candidatos não classificados e 53 arquivos associados a mais de um bloco. A revisão mostrou três situações distintas:

1. produtos analíticos em inglês, especialmente arquivos econômicos e de mercado de trabalho;
2. cadastros processados de servidores, aposentados, pensionistas e militares;
3. arquivos técnicos de inventário, auditoria, catálogo e registro sem conteúdo substantivo próprio.

A calibração foi separada das regras heurísticas gerais em:

```text
src/sbmi/base_territorial_coverage_refinement.py
```

As regras explicitamente justificadas são:

- `exports/economic_*`, `exports/sector_*`, `exports/private_vab_*`, `exports/public_vab_*`, `exports/public_sector_*`, `exports/public_structural_*` e `exports/structural_analysis*` → economia e estrutura produtiva;
- `exports/labor_market_*` e `exports/private_employment_*` → renda, emprego e trabalho, com relação secundária com economia;
- `processed/202601_aposentados_*`, `processed/202601_pensionistas_*`, `processed/202601_servidores_*`, `processed/202601_militares/*` e `processed/202601_reserva_reforma_militares/*` → renda, emprego e trabalho;
- `exports/census_*` → demografia;
- arquivos `exports/domain_*`, `exports/inventory.*`, `exports/semantic_*`, catálogos, perfis técnicos, mapas de domínio e registros de premissas → artefatos técnicos não contabilizados como cobertura analítica.

Essas regras não alteram os arquivos originais e não validam o conteúdo substantivo. Elas apenas corrigem falsos negativos e retiram falsos candidatos evidentes.

Permanecem deliberadamente sem regra automática:

- `raw/institucional/*`;
- `raw/pdfs/*`;
- `processed/institucional/*`;
- produtos de nome genérico, como `dashboard_dataset.csv`.

Esses grupos exigem revisão nominal e, quando necessário, inspeção de conteúdo antes de qualquer classificação.

## Status de cobertura

O mapa pode atribuir:

```text
CURATED_VALIDATED_PRESENT
STAGING_VALIDATED_PRESENT
DERIVED_PRODUCTS_AUDITED_PRESENT
RAW_SOURCES_PRESENT
METADATA_CANDIDATES_PRESENT
NO_CANDIDATE_IDENTIFIED
```

A ordem representa maturidade técnica, não qualidade substantiva.

### Interpretação

- `CURATED_VALIDATED_PRESENT`: há módulo curado e validado, mas a cobertura pode não ser exaustiva;
- `STAGING_VALIDATED_PRESENT`: estrutura e proveniência foram validadas, mas falta curadoria temática;
- `DERIVED_PRODUCTS_AUDITED_PRESENT`: produtos históricos existem e são legíveis, sem validação metodológica concluída;
- `RAW_SOURCES_PRESENT`: há fonte bruta candidata;
- `METADATA_CANDIDATES_PRESENT`: a evidência ainda é apenas classificatória;
- `NO_CANDIDATE_IDENTIFIED`: nenhuma ocorrência foi encontrada pelas regras atuais, sem provar ausência absoluta.

## Entradas padrão

```text
.data/manifests/google_drive_inventory.csv
.data/staging/new_files/<snapshot_id>/source_manifest.csv
.data/audit/new_files/staging_validation/<snapshot_id>/dataset_validation_summary.csv
.data/audit/derived_products/derived-products-20260723/derived_family_summary.csv
.data/curated/base_territorial/
```

O inventário deve ser atualizado quando houver mudanças relevantes no Drive, como inclusão ou movimentação de arquivos.

## Execução

```bash
make gdrive-inventory
make map-base-territorial-coverage
```

O segundo comando não baixa conteúdos históricos, não modifica arquivos brutos e não escreve no Google Drive.

## Saídas

```text
.data/audit/base_territorial/coverage_map/coverage-map-AAAAMMDD/
├── coverage_file_inventory.csv
├── coverage_source_family_summary.csv
├── coverage_evidence_register.csv
├── coverage_block_summary.csv
├── coverage_gap_register.csv
└── coverage_map_summary.csv
```

### `coverage_file_inventory.csv`

Registra um arquivo por linha, com estágio, família, bloco, método, base e confiança da classificação.

### `coverage_source_family_summary.csv`

Resume arquivos, bytes, extensões e métodos de classificação por família e bloco.

### `coverage_evidence_register.csv`

Reúne contratos de staging, famílias históricas auditadas e módulos curados locais. Para cada evidência, registra período, unidade, abrangência, validação e limitação quando disponíveis.

### `coverage_block_summary.csv`

Consolida a maturidade técnica por bloco e indica a próxima ação recomendada.

### `coverage_gap_register.csv`

Distingue lacunas de integração, curadoria, revisão metodológica, auditoria estrutural e ausência de candidato identificado pelas regras atuais.

### `coverage_map_summary.csv`

Preserva indicadores gerais e a natureza observada ou calculada de cada medida.

## Limitações

- o mapa depende da atualização do inventário do Drive;
- arquivos com nomes genéricos podem permanecer não classificados;
- um arquivo pode conter múltiplos temas, embora apenas um bloco seja primário;
- a classificação de famílias históricas usa caminhos e metadados, não revalida o conteúdo;
- os módulos IDSC e IPS são detectados localmente e continuam sujeitos às limitações documentadas em seus próprios contratos;
- nenhuma ausência definitiva deve ser declarada somente com base neste mapa;
- nenhuma inferência causal é produzida.
