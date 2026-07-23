# São Borja — Inteligência Mercadológica

Pipeline reprodutível de inteligência econômica e mercadológica de São Borja/RS.

## Objetivo

Organizar, auditar, processar e analisar dados territoriais, econômicos, fiscais, demográficos e sociais do município, preservando fontes, períodos, unidades, abrangência geográfica e limitações metodológicas.

## Arquitetura

- **Google Drive:** dados originais, dados curados e exportações;
- **GitHub:** código, configurações sem segredos, testes e documentação;
- **GitHub Codespaces:** ambiente principal de desenvolvimento e validação;
- **DuckDB:** mecanismo analítico local e reconstruível;
- **Supabase:** camada futura de publicação e consulta.

Os scripts históricos do Google Colab permanecem preservados em `src/modeling/` durante a estabilização.

## Ambiente

O repositório utiliza Python 3.12 e possui configuração para GitHub Codespaces.

```bash
make bootstrap
make verify
```

A verificação executa:

- diagnóstico dos caminhos locais;
- testes automatizados;
- lint do código estabilizado.

## Google Drive

O acesso inicial ao Drive usa uma conta de serviço com permissão de Visualizador apenas sobre a pasta do projeto. A credencial é fornecida ao Codespace por segredo criptografado e permanece em memória durante a execução.

Validação de acesso, sem download:

```bash
make gdrive-check
```

Inventário recursivo de metadados:

```bash
make gdrive-inventory
```

O inventário é salvo em:

```text
manifests/google_drive_inventory.csv
```

Consulte [`docs/google_drive_api.md`](docs/google_drive_api.md) para configuração e limitações.

## Estrutura nova

```text
.devcontainer/          ambiente Codespaces
.github/workflows/      integração contínua
config/                 exemplos de configuração
src/sbmi/               infraestrutura estabilizada
tests/                  testes automatizados
docs/                   arquitetura, governança e auditoria
manifests/              inventários leves de metadados
reports/generated/      relatórios gerados localmente
```

## Segurança

Dados, credenciais, arquivos Parquet, bancos DuckDB e artefatos temporários não devem ser versionados. O conteúdo de `raw` é imutável e nenhuma rotina de escrita no Drive faz parte desta etapa.

## Estado

A migração está em andamento na branch `stabilization/architecture-v1`. O pull request permanece em modo rascunho até a validação do inventário do Drive e da auditoria dos dados.
