# Arquitetura do projeto

## Objetivo

Estabilizar e profissionalizar o pipeline sem descartar os dados, resultados e builders já existentes.

## Componentes

### Google Drive

Armazena os arquivos originais, os dados curados, os manifestos completos e as exportações destinadas a análise e difusão.

### GitHub

É a única fonte oficial para código, configurações sem segredos, testes, documentação e histórico de alterações.

### GitHub Codespaces

É o ambiente principal de desenvolvimento, execução, validação e auditoria. O ambiente é reconstruído a partir de `.devcontainer/devcontainer.json` e `pyproject.toml`.

### DuckDB

É usado como mecanismo analítico local e reconstruível a partir de arquivos Parquet. Arquivos `.duckdb` não são tratados como fonte mestre nem versionados no Git.

### Supabase

Fica reservado para uma etapa futura de publicação, consulta, autenticação e APIs. Não integra a fase atual de estabilização.

## Camadas lógicas

```text
raw      -> original imutável
staging  -> padronização mínima e temporária
curated  -> tabelas consolidadas e validadas
exports  -> arquivos para relatórios, dashboards e difusão
```

## Fluxo de trabalho

```text
Google Drive/raw
      |
      v
Codespace/.data/raw
      |
      v
staging -> validação -> curated
      |
      +-> manifestos e relatórios de auditoria
      |
      v
Google Drive/exports e Google Drive/curated
```

## Compatibilidade com o legado

Os builders em `src/modeling/` permanecem preservados durante a estabilização. Eles contêm caminhos absolutos do Colab e serão migrados gradualmente, depois que a nova camada comum de caminhos, inventário e validação estiver testada.

O notebook `Analise_SB.ipynb` é documentação histórica. Não deve ser executado integralmente como pipeline operacional.

## Princípio de substituição

Nenhum resultado existente deve ser substituído até que uma nova execução seja comparada com a anterior e todas as diferenças estejam classificadas e explicadas.
