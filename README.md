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

A estabilização técnica inicial foi concluída em 24 de julho de 2026. A Base Territorial Comum já incorpora os módulos portáteis do IDSC-BR 2025 e das edições originalmente publicadas do IPS Brasil em 2024, 2025 e 2026.

Desde 28 de julho de 2026, os arquivos existentes são tratados como originais
por premissa declarada pelo responsável. A auditoria prioriza duplicidades,
sobreposições, interpretação conceitual e validade das transformações, sem
repetir investigação externa de origem na ausência de inconsistência concreta.

Última validação completa:

- 80 testes automatizados aprovados;
- Ruff aprovado;
- GitHub Actions aprovado;
- inventário e auditoria estrutural do acervo concluídos;
- seis datasets de staging construídos e validados;
- produtos históricos auditados sem reconstrução integral;
- nenhuma evidência de corrupção generalizada do acervo;
- riscos remanescentes localizados e documentados.

Consulte:

- [`docs/audit_operating_premise_20260728.md`](docs/audit_operating_premise_20260728.md) para a premissa operacional e o modo de auditoria enxuto;
- [`docs/project_status_20260724.md`](docs/project_status_20260724.md) para o ponto de situação, pendências e sequência recomendada;
- [`docs/stabilization_audit_closure_20260724.md`](docs/stabilization_audit_closure_20260724.md) para o encerramento formal da estabilização;
- [`docs/base_territorial_ips_published.md`](docs/base_territorial_ips_published.md) para o módulo IPS Brasil publicado.
