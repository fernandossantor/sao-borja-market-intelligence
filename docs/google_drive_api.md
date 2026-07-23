# Acesso ao Google Drive pela API

## Objetivo

A integração usa uma conta de serviço com permissão de **Visualizador** apenas sobre a pasta `_sao_borja`.

O inventário inicial consulta somente metadados pela Google Drive API v3. Nenhum arquivo é movido, excluído, renomeado ou sobrescrito.

## Segredos do Codespaces

O repositório utiliza duas variáveis protegidas:

- `SBMI_GDRIVE_SA_B64`: conteúdo Base64 do arquivo JSON da conta de serviço;
- `SBMI_DRIVE_ROOT_FOLDER_ID`: ID da pasta `_sao_borja`.

A credencial JSON não deve ser copiada para o repositório, para o terminal, para issues, pull requests ou documentação.

## Conversão local para Base64

No Windows PowerShell, substitua o caminho pelo arquivo JSON baixado:

```powershell
$arquivo = "C:\Users\SEU_USUARIO\Downloads\conta-de-servico.json"
[Convert]::ToBase64String([IO.File]::ReadAllBytes($arquivo)) | Set-Clipboard
```

O conteúdo Base64 ficará na área de transferência para ser inserido diretamente no campo do segredo no GitHub.

## Criação dos segredos

No repositório:

1. abrir `Settings`;
2. abrir `Secrets and variables`;
3. selecionar `Codespaces`;
4. criar o segredo `SBMI_GDRIVE_SA_B64` com o Base64;
5. criar o segredo `SBMI_DRIVE_ROOT_FOLDER_ID` com o ID da pasta raiz.

Depois de criar ou alterar segredos, o Codespace em execução deve ser parado e iniciado novamente para receber as novas variáveis.

## Validação

Após reiniciar o Codespace:

```bash
python - <<'PY'
import os
print("credential=available" if os.getenv("SBMI_GDRIVE_SA_B64") else "credential=missing")
print("root_id=available" if os.getenv("SBMI_DRIVE_ROOT_FOLDER_ID") else "root_id=missing")
PY
```

Esse comando verifica somente a existência das variáveis. Ele não imprime seus valores.

Atualizar e reinstalar o projeto:

```bash
git pull --ff-only
make bootstrap
make verify
```

Validar acesso à pasta raiz, sem baixar arquivos:

```bash
make gdrive-check
```

## Inventário de metadados

Depois que a validação retornar `status=ok`:

```bash
make gdrive-inventory
```

O comando cria:

```text
manifests/google_drive_inventory.csv
```

Campos principais:

- ID estável do arquivo no Drive;
- caminho relativo;
- nome e extensão;
- tipo MIME;
- identificação de pasta;
- tamanho informado;
- datas de criação e modificação;
- checksums MD5, SHA-1 e SHA-256, quando fornecidos pelo Drive;
- pasta-pai;
- status inicial de auditoria.

## Limitações

- arquivos dos Editores Google e atalhos podem não possuir tamanho ou checksum;
- o inventário registra metadados observados no momento da execução;
- a existência de checksum igual é evidência de duplicidade física, mas não resolve duplicidades conceituais ou sobreposição de períodos;
- a API não é usada para escrever no Drive nesta etapa;
- a captura dos conteúdos será uma etapa posterior e separada, após a auditoria do inventário.
