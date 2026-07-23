# AGENTS.md

## Projeto

Este repositório mantém o código e a documentação do projeto **São Borja — Inteligência Mercadológica**.

O projeto integra análises econômicas, fiscais, demográficas, sociais, setoriais, concorrenciais, educacionais, midiáticas e comportamentais, com foco em São Borja/RS, sua região de influência e mercados comparáveis.

## Regras obrigatórias

1. Nunca alterar, sobrescrever ou excluir arquivos da camada `raw`.
2. Nunca inserir bases extensas, credenciais, tokens, arquivos `.env`, bancos DuckDB ativos ou resultados temporários no Git.
3. Não trabalhar diretamente na branch `main`. Usar branch por tarefa e pull request.
4. Não inventar números, fontes, indicadores, categorias, períodos, nomenclaturas oficiais ou resultados.
5. Distinguir explicitamente dados observados, dados calculados, estimativas, hipóteses, interpretações e recomendações.
6. Registrar fonte, período de referência, unidade, abrangência geográfica e limitações relevantes.
7. Não tratar correlação como causalidade.
8. Não combinar bases que usem conceitos distintos sem documentar a diferença metodológica.
9. Preservar os builders existentes em `src/modeling/` durante a estabilização. A migração deve ser incremental e validada.
10. Nenhum resultado existente pode ser substituído quando houver diferença não explicada em relação à execução anterior.

## Arquitetura de responsabilidade

- **Google Drive:** arquivos originais, dados curados, manifestos completos e exportações.
- **GitHub:** código, configurações sem segredos, testes, documentação e manifestos leves.
- **GitHub Codespaces:** ambiente principal de desenvolvimento, execução e validação.
- **DuckDB:** mecanismo analítico local e reconstruível; não é a fonte mestre dos dados.
- **Supabase:** reservado para uma futura camada de publicação e consulta.

## Convenções de dados

Camadas lógicas:

1. `raw`: original imutável;
2. `staging`: padronização mínima e temporária;
3. `curated`: tabelas consolidadas, documentadas e validadas;
4. `exports`: arquivos destinados a relatórios, dashboards e difusão.

Cada dataset deve possuir, quando aplicável:

- identificador estável;
- fonte e URL de origem;
- data de obtenção;
- período de referência;
- abrangência geográfica;
- unidade;
- esquema esperado;
- chave ou combinação de chaves;
- hash SHA-256 do arquivo original;
- status de auditoria;
- limitações conhecidas.

## Qualidade e validação

Antes de concluir uma tarefa:

- verificar colunas obrigatórias;
- verificar tipos e unidades;
- verificar valores ausentes;
- verificar duplicidades de chave;
- verificar cobertura temporal e geográfica;
- comparar totais e quantidade de linhas com a execução anterior;
- registrar diferenças e sua classificação;
- executar testes automatizados disponíveis.

Classificações mínimas para comparação de resultados:

- `IDENTICAL`
- `EXPECTED_CHANGE`
- `SOURCE_UPDATE`
- `METHODOLOGY_CHANGE`
- `ERROR`
- `UNEXPLAINED`

Classificações mínimas para possíveis duplicidades:

- `EXACT_DUPLICATE`
- `CONTENT_DUPLICATE`
- `PARTIAL_OVERLAP`
- `COMPLEMENTARY`
- `CONFLICT`
- `UNIQUE`

## Alterações de arquitetura

Mudanças estruturais relevantes exigem:

1. justificativa documentada;
2. impacto sobre dados e resultados existentes;
3. estratégia de migração;
4. testes;
5. revisão em pull request;
6. aprovação explícita do responsável pelo projeto.

## Segurança

- Nunca registrar credenciais no código, documentação, commits ou logs.
- Usar GitHub Codespaces Secrets para credenciais necessárias.
- Acesso ao Drive deve ser configurado fora do repositório.
- Qualquer rotina de escrita no Drive deve limitar-se a diretórios de saída previamente definidos.
