# São Borja — Inteligência Mercadológica

Pipeline reprodutível de inteligência econômica e mercadológica de São Borja/RS.

## Estado atual

O projeto está em fase de estabilização arquitetural. Os builders históricos permanecem em `src/modeling/` e continuam sendo a referência para os resultados já produzidos. A nova infraestrutura será incorporada gradualmente, com testes e comparação antes de qualquer substituição.

## Arquitetura

- **Google Drive:** dados originais, dados curados, manifestos completos e exportações;
- **GitHub:** código, configurações sem segredos, testes e documentação;
- **GitHub Codespaces:** ambiente principal de desenvolvimento e execução;
- **DuckDB:** mecanismo analítico local e reconstruível;
- **Supabase:** reservado para futura publicação e consulta.

Consulte:

- [`docs/architecture.md`](docs/architecture.md)
- [`docs/data_governance.md`](docs/data_governance.md)
- [`docs/repository_audit.md`](docs/repository_audit.md)
- [`AGENTS.md`](AGENTS.md)

## Ambiente de desenvolvimento

A branch de estabilização contém um ambiente Codespaces reproduzível em `.devcontainer/devcontainer.json`.

Depois de abrir o Codespace:

```bash
make doctor
make test
make lint
```

## Inventário local

Depois que os dados forem sincronizados para `.data/raw` em modo controlado:

```bash
sbmi inventory --root .data/raw --output manifests/local_inventory.csv
sbmi find-exact-duplicates \
  --inventory-csv manifests/local_inventory.csv \
  --output reports/generated/exact_duplicates.csv
```

O primeiro inventário calcula SHA-256 e identifica apenas duplicidades físicas exatas. Sobreposição estrutural e conceitual será tratada em etapas posteriores.

## Regras principais

- `raw` é imutável;
- dados extensos e credenciais não entram no Git;
- mudanças são feitas em branches e revisadas por pull request;
- diferenças entre resultados antigos e novos precisam ser explicadas;
- fontes, períodos, unidades, abrangência e limitações devem ser documentados.
