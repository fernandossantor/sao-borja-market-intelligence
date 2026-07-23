# Conexão somente leitura com o Google Drive

## Objetivo

Permitir que o Codespace leia a pasta `_sao_borja` para inventariar e auditar os dados sem alterar, mover ou excluir arquivos no Google Drive.

## Remote adotado

Nome lógico:

```text
sbmi-drive
```

Pasta raiz do projeto no Google Drive:

```text
_sao_borja
```

ID da pasta raiz:

```text
1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V
```

O remote deve usar o escopo `drive.readonly`. Dessa forma, o rclone poderá ler metadados e conteúdos, mas não escrever no Drive.

## Configuração inicial

No Codespace, instale o rclone quando necessário:

```bash
sudo apt-get update
sudo apt-get install -y rclone
```

Depois execute:

```bash
rclone config
```

Respostas principais:

1. criar novo remote;
2. nome: `sbmi-drive`;
3. tipo: `drive`;
4. `client_id`: deixar vazio;
5. `client_secret`: deixar vazio;
6. escopo: `drive.readonly`;
7. `root_folder_id`: `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`;
8. arquivo de service account: deixar vazio;
9. autenticar no navegador;
10. não configurar Shared Drive;
11. confirmar e salvar.

A numeração apresentada pelo rclone pode variar. Deve-se escolher pela descrição e não apenas pelo número.

## Segurança

- Nunca copiar o token OAuth, o conteúdo de `rclone.conf` ou qualquer credencial para o GitHub, para issues, pull requests ou chats.
- O arquivo de configuração fica fora do repositório, normalmente em `~/.config/rclone/rclone.conf`.
- Para ambientes reconstruídos, a credencial poderá posteriormente ser migrada para GitHub Codespaces Secrets.
- O remote desta etapa deve permanecer somente leitura.

## Validação sem download

Após configurar:

```bash
make drive-check
```

Esse comando lista apenas o primeiro nível de `raw` e não baixa os arquivos.

Depois calcule o volume:

```bash
make drive-size
```

Esse comando informa quantidade de objetos e bytes antes de qualquer captura local.

## Captura local

A captura só deve ser executada depois de revisar o volume:

```bash
make drive-snapshot
```

O conteúdo será copiado para uma pasta nova em:

```text
.data/snapshots/<data-hora-UTC>/raw
```

A rotina usa `rclone copy`, não `sync`. Portanto, não exclui arquivos de destino nem altera o Drive. Também recusa sobrescrever um snapshot local não vazio.

## Inventário e duplicidades exatas

Depois da captura, usar o caminho informado pelo comando:

```bash
python -m sbmi.cli inventory \
  --root .data/snapshots/<snapshot>/raw \
  --output manifests/drive_raw_inventory.csv

python -m sbmi.cli find-exact-duplicates \
  --inventory-csv manifests/drive_raw_inventory.csv \
  --output reports/generated/drive_exact_duplicates.csv
```

O inventário registra caminho relativo, nome, extensão, tamanho, data de modificação, SHA-256 e status inicial de auditoria.

## Limitação

Hash SHA-256 exige leitura integral do arquivo. Por isso a auditoria física completa ocorre sobre a captura local, não apenas por listagem remota.
