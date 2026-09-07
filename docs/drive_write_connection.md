# Conexão de escrita controlada com o Google Drive

## Motivo

O projeto mantém `sbmi-drive` como remote rclone **somente leitura**. Esse remote não deve ser ampliado para escrita.

A conta de serviço `sbmi-drive-reader@sao-borja-market-intelligence.iam.gserviceaccount.com` permanece adequada para leitura e auditoria, mas não deve ser usada para criar arquivos em `Meu Drive`: mesmo com papel `writer` na pasta, a criação de novos objetos pode falhar porque contas de serviço não possuem cota própria para assumir a propriedade dos arquivos em `Meu Drive`.

Por isso, promoções autorizadas de derivados auditados podem utilizar um segundo remote rclone autenticado por OAuth em nome do usuário humano proprietário do Drive. Como alternativa operacional para pequenos lotes de derivados, os arquivos podem ser transferidos ao operador autorizado e promovidos pelo conector Google Drive, preservando a mesma validação de tamanho e SHA-256.

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

## Pré-requisito: rclone instalado

O rclone não é garantido pela imagem padrão do Codespace. Antes de configurar o remote, verificar:

```bash
command -v rclone || true
```

Se não houver resultado:

```bash
sudo apt-get update
sudo apt-get install -y rclone
rclone version
```

Essa instalação altera apenas o ambiente efêmero do Codespace; não modifica o Google Drive nem os dados do projeto.

## Codespaces é ambiente headless

No Codespace, **não usar `Use auto config? = yes`**. Essa opção abre o callback OAuth em `127.0.0.1` dentro do ambiente remoto; o navegador do computador do usuário não consegue devolver o código para esse localhost do container e a autenticação termina com `No code returned by remote server`.

A configuração correta no Codespace é:

```bash
rclone config
```

Criar o remote com:

1. nome `sbmi-drive-write`;
2. tipo `drive`;
3. `client_id` e `client_secret`: vazios, salvo configuração própria já existente;
4. escopo: acesso completo ao Drive (`drive`);
5. service account file: vazio;
6. advanced config: não;
7. **Use auto config?: `n`**.

O rclone então exibirá um comando `rclone authorize "drive" ...` para ser executado em uma máquina local com navegador. Nessa máquina local, após a autorização Google, o rclone retornará um token JSON. Esse token deve ser copiado integralmente e colado no prompt `config_token>` do Codespace.

Depois de autenticado, configurar `root_folder_id` como `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`, não configurar Shared Drive e confirmar o remote.

Nunca registrar o token OAuth, `rclone.conf` ou credenciais no GitHub, nos documentos do projeto ou em chats.

## Separação de responsabilidades

- `sbmi-drive`: leitura e snapshots; permanece `drive.readonly`;
- `SBMI_GDRIVE_SA_B64`: leitura programática e inventários via conta de serviço;
- `sbmi-drive-write`: escrita excepcional e controlada de derivados já auditados, autenticada pelo usuário humano.

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

## Alternativa para pequenos lotes

Quando o lote for pequeno e já estiver totalmente auditado, como os sete CSVs da execução remuneratória, pode-se empacotar os derivados no Codespace, transferir o pacote ao operador autorizado e fazer a promoção via conector Google Drive. Nessa alternativa, devem ser preservados e novamente conferidos os mesmos nomes, tamanhos e SHA-256 registrados no manifesto canônico antes de marcar a promoção como concluída.
