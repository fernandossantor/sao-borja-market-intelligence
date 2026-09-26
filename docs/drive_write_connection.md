# Conexão de escrita controlada com o Google Drive

## Motivo

O projeto mantém `sbmi-drive` como remote rclone **somente leitura**. Esse remote não deve ser ampliado para escrita.

A conta de serviço `sbmi-drive-reader@sao-borja-market-intelligence.iam.gserviceaccount.com` permanece adequada para leitura e auditoria, mas não deve ser usada para criar arquivos em `Meu Drive`: mesmo com papel `writer` na pasta, a criação de novos objetos pode falhar porque contas de serviço não possuem cota própria para assumir a propriedade dos arquivos em `Meu Drive`.

Por isso, promoções autorizadas de derivados auditados podem utilizar um segundo remote rclone autenticado por OAuth em nome do usuário humano proprietário do Drive. Como alternativa operacional para pequenos lotes de derivados, os arquivos podem ser transferidos ao operador autorizado e promovidos pelo conector Google Drive, preservando a mesma validação de tamanho e SHA-256 antes da escrita.

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
- `sbmi-drive-write`: escrita excepcional e controlada de derivados já auditados, autenticada pelo usuário humano;
- handoff controlado + conector Google Drive: alternativa para lotes pequenos já integralmente auditados.

## Promoção remuneratória

A CLI `sbmi.territorial_wage_promote_drive_cli` permanece disponível para ambientes em que `sbmi-drive-write` esteja configurado. Ela valida tamanho e SHA-256 dos sete arquivos locais antes da escrita, reutiliza arquivos remotos idênticos e interrompe colisões divergentes.

## Alternativa para pequenos lotes

Quando o lote for pequeno e já estiver totalmente auditado, como os sete CSVs da execução remuneratória, pode-se empacotar os derivados no Codespace, transferir o pacote ao operador autorizado e fazer a promoção via conector Google Drive. Nessa alternativa:

- o pacote deve ser reaberto antes da escrita;
- os nomes e a quantidade devem coincidir com o manifesto;
- tamanho e SHA-256 devem ser recalculados localmente antes do upload;
- os arquivos devem ser enviados sem conversão;
- a pasta de destino deve ser relistada após a promoção;
- deve-se registrar qualquer limitação do conector para verificação pós-upload.

## Execução remuneratória de 2026-09-07

A promoção final da execução `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236` utilizou essa alternativa de handoff controlado após a autenticação OAuth por rclone se mostrar desnecessariamente onerosa para um lote de apenas sete CSVs já auditados.

O ZIP de handoff tinha 22.223 bytes e SHA-256 `a4fc57af8c7bf3f81d8d160eed9fbc954826d9d1fa55dd0af8320c779eeeff43`. Os sete arquivos internos reproduziram seus hashes canônicos antes da escrita. Após a promoção via conector Google Drive, a pasta continha exatamente sete CSVs com os tamanhos esperados.

O conector utilizado não expõe `sha256Checksum` no retorno normalizado; portanto, a etapa pós-upload confirmou quantidade, nomes, pasta-pai e tamanhos, mas não realizou uma segunda recomputação criptográfica sobre bytes baixados do Drive. O manifesto final está em `docs/caderno_base/territorial_wage_drive_promotion_manifest.md`.
