# Perfil estrutural da captura `raw/new_files`

## Objetivo

Descrever a estrutura dos arquivos capturados localmente antes de qualquer consolidação, transformação ou movimentação no Google Drive.

A rotina trabalha sobre a captura imutável em:

```text
.data/snapshots/new_files/<snapshot_id>/raw/new_files/
```

Nenhum conteúdo é escrito, movido, renomeado ou excluído no Drive.

## Formatos processados

- `.xlsx` e `.xlsm`, por meio do `openpyxl` em modo somente leitura;
- `.csv`, `.tsv` e `.txt` delimitado;
- outros formatos são registrados como `UNSUPPORTED_FORMAT`, sem interromper a auditoria.

## Saídas locais

Por padrão, a captura mais recente é usada e os relatórios são gravados em:

```text
.data/audit/new_files/content_profile/<snapshot_id>/
```

Arquivos gerados:

- `file_profile.csv`: formato, tamanho, quantidade de planilhas e status por arquivo;
- `sheet_profile.csv`: dimensões observadas, estado da planilha, candidato a cabeçalho, anos observados e assinatura estrutural;
- `column_profile.csv`: cabeçalhos, contagens por tipo aparente, valores não vazios, cardinalidade observada e intervalos de anos;
- `exact_schema_groups.csv`: planilhas com a mesma sequência normalizada de cabeçalhos.

## Natureza dos indicadores

### Dados observados

- tamanho local do arquivo;
- quantidade de planilhas;
- estado visível ou oculto;
- quantidade de linhas e células não vazias;
- cabeçalhos encontrados na linha candidata;
- contagens de tipos aparentes;
- anos encontrados nos valores;
- igualdade de assinatura estrutural.

### Estimativas

- linha candidata a cabeçalho;
- confiança da detecção do cabeçalho;
- tipo predominante estimado de cada coluna.

A linha candidata é escolhida por heurística entre as primeiras 25 linhas, considerando quantidade de células preenchidas, proporção de texto e unicidade dos rótulos. A estimativa não substitui inspeção metodológica.

## Limitações

- dimensões declaradas por uma planilha podem ser maiores que as dimensões efetivamente preenchidas devido à formatação residual;
- tipos em arquivos delimitados são inferidos a partir do texto e podem confundir códigos numéricos com medidas;
- anos são detectados por datas ou sequências de quatro dígitos entre 1800 e 2199;
- assinatura estrutural idêntica indica cabeçalhos normalizados iguais e na mesma ordem, não conteúdo equivalente;
- sobreposição parcial de variáveis, períodos ou territórios exige etapa posterior;
- fórmulas são contadas, mas não executadas;
- relatórios detalhados permanecem fora do Git.

## Execução

```bash
make profile-inbox-snapshot
```

Para indicar uma captura específica:

```bash
python -m sbmi.inbox_profile_cli \
  --snapshot-path .data/snapshots/new_files/new-files-20260723
```
