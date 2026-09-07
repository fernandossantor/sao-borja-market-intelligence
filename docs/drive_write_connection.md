# Conexão de escrita controlada com o Google Drive

## Motivo

O projeto mantém `sbmi-drive` como remote rclone **somente leitura**. Esse remote não deve ser ampliado para escrita.

A conta de serviço `sbmi-drive-reader@sao-borja-market-intelligence.iam.gserviceaccount.com` também permanece adequada para leitura e auditoria, mas não deve ser usada para criar arquivos em `Meu Drive`: contas de serviço não possuem cota de armazenamento própria para assumir a propriedade de novos arquivos em `Meu Drive`.

Por isso, promoções autorizadas de derivados auditados utilizam um segundo remote rclone, autenticado por OAuth em nome do usuário humano proprietário do Drive.

## Remote de escrita

Nome lógico:

```text
sbmi-drive-write
```

Pasta raiz do projeto:

```text
_sao_borja
```

ID da raiz:

```text
1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V
```

## Configuração única

No Codespace:

```bash
rclone config
```

Criar um novo remote com:

1. nome `sbmi-drive-write`;
2. tipo `drive`;
3. `client_id` e `client_secret`: deixar vazios, salvo configuração própria já existente;
4. escopo: acesso completo ao Drive (`drive`), necessário para listar, criar e verificar os derivados;
5. `root_folder_id`: `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`;
6. service account file: vazio;
7. autenticar no navegador com a conta humana proprietária do projeto;
8. não configurar Shared Drive;
9. confirmar e salvar.

O `root_folder_id` restringe o caminho operacional do remote à raiz `_sao_borja`, embora a autorização OAuth concedida pelo Google seja do usuário autenticado. O remote deve ser utilizado apenas por rotinas de promoção explicitamente autorizadas.

## Separação de responsabilidades

- `sbmi-drive`: leitura e snapshots; permanece `drive.readonly`;
- `SBMI_GDRIVE_SA_B64`: leitura programática e inventários via conta de serviço;
- `sbmi-drive-write`: escrita excepcional e controlada de derivados já auditados.

## Promoção remuneratória

Depois de configurar o remote de escrita:

```bash
python -m sbmi.territorial_wage_promote_drive_cli
```

A CLI valida tamanho e SHA-256 dos sete arquivos locais antes de qualquer escrita. Em seguida:

- se um arquivo remoto com o mesmo nome já existir, baixa uma cópia temporária e exige igualdade de tamanho e SHA-256;
- se não existir, envia o arquivo e baixa uma cópia temporária para validar novamente tamanho e SHA-256;
- se houver nomes duplicados ou conteúdo divergente, interrompe a promoção;
- não usa `sync`, não exclui arquivos e não altera dados brutos.
