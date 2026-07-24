# Auditoria de proveniência das planilhas do Censo 2022

## Objetivo

Extrair evidências internas das 17 planilhas capturadas antes de atribuir autoridade institucional, validar conceitos ou reconstruir os dois produtos processados em quarentena.

A auditoria examina:

- metadados do documento XLSX;
- nomes, visibilidade e dimensões das abas;
- cabeçalhos e formatos numéricos;
- URLs e hyperlinks;
- comentários;
- rótulos de fonte, instituição, período, unidade e abrangência geográfica;
- consistência com o manifesto da captura.

Ela não consulta a internet e não atribui autoridade a qualquer domínio, autor ou instituição detectada.

## Entradas

```text
.data/audit/base_territorial/demography_lineage/<execução>/demography_lineage_register.csv
.data/snapshots/sources/demography_census/<captura>/source_manifest.csv
.data/snapshots/sources/demography_census/<captura>/raw/social/*.xlsx
```

A captura já foi validada por tamanho e SHA-256 quando disponível. Essa validação comprova integridade da cópia local em relação ao arquivo do Drive, não sua origem institucional.

## Evidências observadas

### Propriedades do documento

São registrados, quando presentes:

- criador;
- último modificador;
- datas de criação e modificação;
- título;
- assunto;
- descrição;
- palavras-chave;
- categoria;
- identificador;
- idioma;
- versão.

Essas propriedades podem ter sido preenchidas pelo software ou pelo último usuário que salvou o arquivo. Não comprovam autoria nem autoridade.

### Evidências em células e comentários

O módulo procura:

```text
CELL_URL
HYPERLINK_TARGET
SOURCE_LABEL
INSTITUTION_LABEL
PERIOD_LABEL
UNIT_LABEL
GEOGRAPHY_LABEL
CELL_COMMENT
```

A detecção é textual e serve para orientar a próxima verificação. Uma menção ao IBGE ou a um endereço eletrônico não comprova, isoladamente, que o arquivo foi publicado pelo órgão citado.

### Metadados de colunas

Para cada coluna são registrados:

- cabeçalho original e normalizado;
- quantidade de células não vazias;
- tipos semânticos observados;
- formatos numéricos do Excel;
- quantidade de células com estilo percentual;
- presença de fórmulas;
- pista de unidade derivada do cabeçalho.

As pistas de unidade são classificações internas, não metadados oficiais.

## Estados de proveniência

```text
EMBEDDED_PROVENANCE_EVIDENCE_DETECTED
DOCUMENT_METADATA_ONLY
NO_EMBEDDED_PROVENANCE_EVIDENCE
```

### Interpretação

- `EMBEDDED_PROVENANCE_EVIDENCE_DETECTED`: há URL, rótulo de fonte ou menção institucional que precisa ser verificada externamente;
- `DOCUMENT_METADATA_ONLY`: existem propriedades do arquivo, mas não evidência de fonte incorporada;
- `NO_EMBEDDED_PROVENANCE_EVIDENCE`: não foi localizada evidência interna suficiente.

O campo de autoridade permanece:

```text
PENDING_EXTERNAL_VERIFICATION
NOT_ESTABLISHED
```

Nenhum dataset recebe validação conceitual nesta etapa.

## Execução

```bash
make audit-base-territorial-demography-census-provenance
```

Para substituir a execução do mesmo dia:

```bash
python -m sbmi.demography_census_provenance_cli --replace
```

## Saídas

```text
.data/audit/base_territorial/demography_census_provenance/
└── demography-census-provenance-AAAAMMDD/
    ├── demography_census_workbook_provenance.csv
    ├── demography_census_sheet_register.csv
    ├── demography_census_column_metadata.csv
    ├── demography_census_provenance_evidence.csv
    └── demography_census_provenance_summary.csv
```

### Registro por planilha

Consolida manifesto, hashes, propriedades do documento, domínios detectados e status de proveniência.

### Registro de abas

Preserva dimensões, cabeçalhos, células não vazias, fórmulas, comentários, hyperlinks, intervalos mesclados e linhas ou colunas ocultas.

### Metadados de colunas

Permite revisar unidades e formatos antes da reconstrução dos produtos em quarentena.

### Evidências de proveniência

Preserva o texto detectado, posição, domínio, número de ocorrências e a limitação da inferência.

## Relação com as anomalias já identificadas

Os produtos de composição domiciliar e território permanecem em quarentena por erro sistemático de escala decimal. A auditoria de proveniência não os corrige.

A reconstrução somente será aberta depois de:

1. examinar as evidências internas;
2. verificar externamente a fonte e seus metadados;
3. definir a unidade e o conceito de cada coluna afetada;
4. construir novos produtos a partir das planilhas capturadas;
5. repetir a comparação de conteúdo.

## Limitações

- propriedades XLSX podem refletir o último software ou usuário que salvou o arquivo;
- URLs incorporadas podem estar desatualizadas ou não representar a origem real;
- rótulos textuais podem ter sido copiados de outra fonte;
- formatos do Excel não substituem definição oficial de unidade;
- o arquivo pode ter perdido metadados durante exportação ou edição;
- nenhuma consulta externa é realizada;
- nenhum arquivo bruto ou processado é modificado;
- nenhuma escrita é feita no Google Drive.
