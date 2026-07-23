# Captura seletiva de `raw/new_files`

## Objetivo

A captura seletiva copia somente os arquivos da caixa de entrada `raw/new_files` para o armazenamento local do Codespace.

A operação usa a Google Drive API com escopo `drive.readonly`. Nenhum arquivo é criado, movido, renomeado, excluído ou alterado no Drive.

## Pré-condições

- segredos `SBMI_GDRIVE_SA_B64` e `SBMI_DRIVE_ROOT_FOLDER_ID` disponíveis;
- inventário em `.data/manifests/google_drive_inventory.csv`;
- auditoria de metadados executada;
- volume total conhecido e inferior ao limite configurado.

## Execução

```bash
make gdrive-snapshot-inbox
```

O limite padrão é 10.000.000 bytes. O volume observado da caixa em 23 de julho de 2026 foi de 590.693 bytes.

Para informar um identificador estável:

```bash
python -m sbmi.inbox_snapshot_cli --snapshot-id new-files-20260723
```

## Destino

A captura é criada em:

```text
.data/snapshots/new_files/<snapshot_id>/
```

Os caminhos relativos do Drive são preservados, por exemplo:

```text
raw/new_files/Federal/arquivo.xlsx
raw/new_files/Estadual/arquivo.xlsx
raw/new_files/Municipal/arquivo.xlsx
```

## Validação

Para cada arquivo, a rotina verifica:

- tamanho baixado contra `size_bytes` informado pela API;
- SHA-256 local contra `sha256Checksum` informado pela API;
- ausência de destino preexistente;
- ausência de travessia de diretórios no caminho relativo.

A captura só é publicada com o nome definitivo depois que todos os arquivos passam nas verificações. Em caso de erro, o diretório parcial é removido.

O arquivo `snapshot_manifest.csv` registra tamanho esperado, tamanho obtido, checksum esperado, checksum local e status de verificação.

## Limitações

- identidade binária não elimina a necessidade de auditoria conceitual;
- a captura permanece local ao Codespace e fora do Git;
- a etapa seguinte deve examinar folhas, cabeçalhos, dimensões, períodos, unidades, abrangência geográfica e possíveis sobreposições entre as bases.
