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
- blocos adicionais encontrados por palavras-chave ou revisão de conteúdo;
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

Os demais arquivos são inicialmente classificados por regras de palavras-chave. Casos não reconhecidos são submetidos a revisão antes de qualquer conclusão sobre lacunas.

## Calibração após revisão manual

A primeira execução real identificou 131 candidatos não classificados e 53 arquivos associados a mais de um bloco. A revisão mostrou três situações distintas:

1. produtos analíticos em inglês, especialmente arquivos econômicos e de mercado de trabalho;
2. cadastros processados de servidores, aposentados, pensionistas e militares;
3. arquivos técnicos de inventário, auditoria, catálogo e registro sem conteúdo substantivo próprio.

A calibração foi separada das regras heurísticas gerais em:

```text
src/sbmi/base_territorial_coverage_refinement.py
```

As primeiras regras explicitamente justificadas foram:

- `exports/economic_*`, `exports/sector_*`, `exports/private_vab_*`, `exports/public_vab_*`, `exports/public_sector_*`, `exports/public_structural_*` e `exports/structural_analysis*` → economia e estrutura produtiva;
- `exports/labor_market_*` e `exports/private_employment_*` → renda, emprego e trabalho, com relação secundária com economia;
- `processed/202601_aposentados_*`, `processed/202601_pensionistas_*`, `processed/202601_servidores_*`, `processed/202601_militares/*` e `processed/202601_reserva_reforma_militares/*` → renda, emprego e trabalho;
- `exports/census_*` → demografia;
- arquivos `exports/domain_*`, `exports/inventory.*`, `exports/semantic_*`, catálogos, perfis técnicos, mapas de domínio e registros de premissas → artefatos técnicos não contabilizados como cobertura analítica.

Essas regras não alteram os arquivos originais e não validam o conteúdo substantivo. Elas apenas corrigem falsos negativos e retiram falsos candidatos evidentes.

## Segunda revisão: fontes institucionais e PDFs

A segunda execução reduziu os candidatos não classificados de 131 para 43. Todos os 43 foram então revisados nominalmente e, quando necessário, pelo conteúdo disponível no Drive ou por inspeção visual dos PDFs.

### Dados institucionais

Os arquivos de pessoal público foram classificados no bloco **Renda, emprego e trabalho**, com relação secundária com economia:

- cadastros de servidores, aposentados, pensionistas, militares e reserva/reforma;
- registros de afastamentos;
- `serv_por_mun_exerc_202512`;
- Tabelas 1 e 2 da tabela IBGE 5881, sobre pessoal ocupado na administração direta e indireta segundo o vínculo empregatício.

Arquivos denominados `Observacoes` e `tabela5881_Notas` foram tratados como documentação de suporte e não como cobertura analítica independente.

### PDFs territoriais e contextuais

Foram classificados por revisão de conteúdo:

- Plano Estratégico de Desenvolvimento do COREDE Fronteira Oeste 2022-2030 → ambiente político e regulatório, com relações econômicas, infraestruturais e transversais;
- mapa do COREDE Fronteira Oeste → ambiente sociocultural e territorial;
- dissertações e dossiês sobre o patrimônio arqueológico, histórico e missioneiro de São Borja → ambiente sociocultural e territorial;
- apresentação municipal de agricultura e meio ambiente → economia e estrutura produtiva, com dimensões demográficas e territoriais;
- estudo nacional da FGV Social sobre classes econômicas → renda, emprego e trabalho, como referência contextual nacional;
- Perfil das Cidades Gaúchas de São Borja → transversal e multitemático;
- mapa do Plano Diretor → ambiente político e regulatório, com relação com infraestrutura e território;
- Plano Municipal de Saúde 2014-2017 → saúde e condições sociais, com natureza de planejamento público;
- relatório municipal multitemático de São Borja → transversal e multitemático;
- mapa do sistema viário motorizado → infraestrutura e conectividade;
- Perfil Socioeconômico do COREDE Fronteira Oeste de 2025 → transversal e multitemático.

O artigo `admin,+1.pdf`, dedicado à historiografia de Santa Catarina e sem objeto territorial pertinente a São Borja ou à sua região de influência, foi marcado como **fora do escopo territorial**.

### Produtos que não contam como cobertura independente

Foram excluídos da contagem analítica:

- `exports/dashboard_dataset.csv`, por ser produto integrado de apresentação e não fonte independente;
- `warehouse/sao_borja.duckdb`, por ser contêiner técnico de armazenamento;
- inventários, auditorias, catálogos, registros de premissas e documentação de datasets.

## Cobertura temática primária e secundária

Um arquivo pode ser multitemático. Para não perder essa informação, a síntese final distingue:

```text
primary_candidate_files
secondary_candidate_files
```

A classificação primária indica o objeto principal da fonte. As relações secundárias indicam temas efetivamente cobertos, mas que não constituem o foco central do documento.

Exemplo: um relatório municipal multitemático pode conter dados de educação sem ser uma fonte educacional dedicada. Nesse caso:

- o relatório conta como candidato secundário de educação;
- não é promovido a fonte primária de educação;
- o bloco recebe `SECONDARY_TOPIC_CANDIDATES_PRESENT` quando não há fonte dedicada mais madura.

Essa distinção evita dois erros:

1. declarar que não existe qualquer cobertura porque o tema aparece somente em fonte multitemática;
2. tratar uma menção secundária como equivalente a uma base específica, validada e dedicada ao tema.

A lógica está isolada em:

```text
src/sbmi/base_territorial_secondary_coverage.py
```

## Status de cobertura

O mapa pode atribuir:

```text
CURATED_VALIDATED_PRESENT
STAGING_VALIDATED_PRESENT
DERIVED_PRODUCTS_AUDITED_PRESENT
RAW_SOURCES_PRESENT
METADATA_CANDIDATES_PRESENT
SECONDARY_TOPIC_CANDIDATES_PRESENT
NO_CANDIDATE_IDENTIFIED
```

A ordem representa maturidade técnica, não qualidade substantiva.

### Interpretação

- `CURATED_VALIDATED_PRESENT`: há módulo curado e validado, mas a cobertura pode não ser exaustiva;
- `STAGING_VALIDATED_PRESENT`: estrutura e proveniência foram validadas, mas falta curadoria temática;
- `DERIVED_PRODUCTS_AUDITED_PRESENT`: produtos históricos existem e são legíveis, sem validação metodológica concluída;
- `RAW_SOURCES_PRESENT`: há fonte bruta primária candidata;
- `METADATA_CANDIDATES_PRESENT`: há candidato primário, ainda sustentado principalmente por metadados;
- `SECONDARY_TOPIC_CANDIDATES_PRESENT`: o tema aparece em fontes multitemáticas, mas nenhuma fonte primária dedicada foi identificada;
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

Resume arquivos, bytes, extensões e métodos de classificação por família e bloco primário.

### `coverage_evidence_register.csv`

Reúne contratos de staging, famílias históricas auditadas e módulos curados locais. Para cada evidência, registra período, unidade, abrangência, validação e limitação quando disponíveis.

### `coverage_block_summary.csv`

Consolida a maturidade técnica por bloco e separa candidatos primários e secundários. Também indica a próxima ação recomendada.

### `coverage_gap_register.csv`

Distingue lacunas de integração, curadoria, revisão metodológica, auditoria estrutural, falta de fonte dedicada e ausência de qualquer candidato identificado.

### `coverage_map_summary.csv`

Preserva indicadores gerais e a natureza observada ou calculada de cada medida.

## Limitações

- o mapa depende da atualização do inventário do Drive;
- um arquivo pode conter múltiplos temas, embora apenas um bloco seja primário;
- a classificação de famílias históricas usa caminhos e metadados, não revalida o conteúdo;
- referências nacionais ou regionais não substituem dados municipais;
- a classificação temática não prova atualidade, comparabilidade ou suficiência da fonte;
- uma relação temática secundária não substitui fonte dedicada;
- os módulos IDSC e IPS são detectados localmente e continuam sujeitos às limitações documentadas em seus próprios contratos;
- nenhuma ausência definitiva deve ser declarada somente com base neste mapa;
- nenhuma inferência causal é produzida.
