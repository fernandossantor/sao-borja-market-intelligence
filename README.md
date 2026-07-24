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

Os scripts históricos do Google Colab permanecem preservados em `src/modeling/` e serão revisados somente quando cada família temática for retomada.

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

O acesso ao Drive usa uma conta de serviço com permissão de Visualizador apenas sobre a pasta do projeto. A credencial é fornecida ao Codespace por segredo criptografado e permanece em memória durante a execução.

Validação de acesso, sem download:

```bash
make gdrive-check
```

Inventário recursivo de metadados:

```bash
make gdrive-inventory
```

O inventário local é salvo em:

```text
.data/manifests/google_drive_inventory.csv
```

Consulte [`docs/google_drive_api.md`](docs/google_drive_api.md) para configuração e limitações.

## Estrutura estabilizada

```text
.devcontainer/          ambiente Codespaces
.github/workflows/      integração contínua
config/                 exemplos de configuração
src/sbmi/               infraestrutura estabilizada
tests/                  testes automatizados
docs/                   arquitetura, governança e auditoria
manifests/               inventários leves de metadados
reports/generated/      relatórios gerados localmente
```

## Segurança

Dados, credenciais, arquivos Parquet, bancos DuckDB e artefatos temporários não devem ser versionados. O conteúdo de `raw` é imutável e as rotinas de auditoria usam o Google Drive em modo somente leitura.

## Estado

A auditoria de estabilização foi concluída em 24 de julho de 2026.

Resultados principais:

- inventário do acervo do Google Drive concluído;
- `raw/new_files` auditado e convertido em seis datasets de staging validados;
- produtos existentes em `processed`, `exports` e `warehouse` capturados e auditados sem reconstrução;
- 58 testes automatizados aprovados;
- nenhuma evidência de corrupção generalizada ou necessidade de reconstrução completa do acervo;
- riscos remanescentes localizados e documentados para revisão sob demanda.

Consulte [`docs/stabilization_audit_closure_20260724.md`](docs/stabilization_audit_closure_20260724.md) para o encerramento formal, as decisões de governança e as limitações.
