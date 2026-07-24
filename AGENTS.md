# AGENTS.md

## Projeto

Este repositório mantém o código e a documentação do projeto
**São Borja — Inteligência Mercadológica**.

O projeto integra análises econômicas, fiscais, demográficas, sociais,
setoriais, concorrenciais, educacionais, midiáticas e comportamentais, com
foco em São Borja/RS, sua região de influência e mercados comparáveis.

Este arquivo estabelece regras obrigatórias para agentes e rotinas
automatizadas que trabalhem no repositório.

## Modo de trabalho supervisionado

O trabalho deve ser conduzido de forma orientada, incremental e verificável.

Para cada etapa:

1. ler o estado atual do repositório e dos artefatos relevantes em `.data`;
2. apresentar separadamente:
   - o que foi observado;
   - o que foi calculado;
   - o que foi estimado;
   - o que foi interpretado;
   - o que é recomendado;
3. informar explicitamente o que pode e o que não pode ser concluído;
4. indicar a próxima ação recomendada;
5. não avançar para a etapa seguinte antes de explicar o resultado da etapa atual.

Antes de modificar arquivos, apresentar:

- objetivo da alteração;
- arquivos que serão modificados ou criados;
- impacto esperado;
- riscos;
- testes e pipeline real que serão executados.

Exigem autorização explícita do responsável pelo projeto antes da execução:

- alterações relevantes de arquitetura;
- reconstrução ou substituição de dados;
- downloads de grande volume;
- acesso a serviços externos;
- escrita em sistemas externos;
- commits;
- push;
- abertura ou atualização material de pull request;
- merge de pull request.

Leituras locais, inspeções de `.data`, diagnósticos e testes não destrutivos
podem ser executados diretamente quando estiverem dentro do escopo solicitado.

Não entregar apenas comandos para o responsável executar quando a ação puder
ser realizada diretamente e com segurança no Codespace.

## Arquitetura de dados

Preservar o fluxo lógico:

```text
raw → staging → curated → exports
```

Responsabilidade das camadas:

1. `raw`: fontes originais imutáveis;
2. `staging`: padronização mínima, temporária e rastreável;
3. `curated`: tabelas consolidadas, documentadas e validadas;
4. `exports`: produtos destinados a relatórios, dashboards e difusão.

Nenhuma etapa pode ignorar uma camada necessária ou promover dados para a
camada seguinte sem validação proporcional ao risco.

## Arquitetura de responsabilidade

- **Google Drive:** fonte mestre de arquivos originais, dados curados,
  manifestos completos e exportações existentes;
- **GitHub:** código, configurações sem segredos, testes, documentação e
  manifestos leves;
- **GitHub Codespaces:** ambiente principal de desenvolvimento, execução,
  auditoria e validação;
- **DuckDB:** mecanismo analítico local e reconstruível, nunca fonte mestre;
- **Supabase:** reservado para futura camada de publicação e consulta.

## Governança obrigatória

1. Nunca alterar, sobrescrever, mover ou excluir arquivos brutos ou históricos,
   inclusive nas camadas `raw`, `processed` e `exports`.
2. Nunca escrever no Google Drive.
3. Nunca sobrescrever snapshots existentes.
4. Novas execuções devem usar identificadores próprios ou falhar de forma
   segura quando o destino já existir.
5. Preservar a proveniência e os hashes disponíveis em todas as transformações.
6. Não substituir resultados existentes quando houver diferença não explicada
   em relação à execução anterior.
7. Não trabalhar diretamente na branch `main`.
8. Usar branch por tarefa e pull request.
9. Não fazer merge de pull request sem autorização explícita do responsável
   pelo projeto.
10. Preservar os builders históricos em `src/modeling/` durante a
    estabilização. Qualquer migração deve ser incremental, documentada e
    validada.
11. Nunca inserir no Git:
    - bases extensas;
    - credenciais ou tokens;
    - arquivos `.env`;
    - bancos DuckDB ativos;
    - snapshots locais;
    - resultados temporários;
    - artefatos reconstruíveis de `.data`.
12. Nunca registrar credenciais em código, documentação, commits, saídas de
    comandos ou logs.

## Hierarquia das evidências

As seguintes relações devem permanecer explicitamente separadas:

1. correspondência nominal não comprova equivalência de conteúdo;
2. equivalência de conteúdo não comprova autoridade da fonte;
3. autoridade da fonte não comprova origem ou linhagem do arquivo local;
4. autoridade e linhagem não comprovam validade conceitual;
5. validade conceitual não comprova comparabilidade temporal ou territorial;
6. correlação não comprova causalidade.

Não usar nomes de arquivos, nomes de colunas, URLs parametrizadas ou
similaridade estrutural como prova suficiente de conteúdo, autoridade,
linhagem ou adequação metodológica.

Não combinar bases que utilizem conceitos, populações de referência, unidades,
geografias, períodos ou métodos distintos sem documentar a diferença e
justificar a compatibilidade.

## Evidências e linguagem analítica

Toda documentação, relatório e saída analítica deve distinguir:

### Observado

Informação diretamente presente na fonte, arquivo, resposta oficial, metadado
ou execução examinada.

### Calculado

Resultado produzido por regra determinística documentada a partir de
evidências observadas.

### Estimado

Resultado dependente de aproximação, inferência, heurística, modelo ou
informação incompleta.

### Interpretado

Leitura analítica fundamentada nas evidências, sem ser apresentada como fato
observado.

### Recomendado

Próxima ação ou decisão proposta, separada dos resultados observados e
calculados.

Hipóteses devem ser identificadas explicitamente como hipóteses.

Nunca inventar:

- números;
- fontes;
- indicadores;
- categorias;
- períodos;
- unidades;
- abrangências geográficas;
- nomenclaturas oficiais;
- classificações oficiais;
- resultados;
- vínculos de proveniência;
- conclusões metodológicas.

Quando uma informação não puder ser comprovada, registrar a ausência de
evidência em vez de preenchê-la por suposição.

## Metadados e proveniência

Cada dataset ou captura deve registrar, quando aplicável:

- identificador estável;
- instituição ou fonte declarada;
- URL de origem;
- data e hora de obtenção;
- período de referência;
- abrangência geográfica;
- unidade;
- natureza do resultado;
- esquema esperado;
- chave ou combinação de chaves;
- tamanho em bytes;
- hash SHA-256 do arquivo original;
- caminho ou identificador da captura;
- transformações aplicadas;
- status de auditoria;
- limitações conhecidas.

Transformações devem permitir rastrear cada produto até sua entrada imediata e,
quando possível, até a fonte original.

## Snapshots e saídas atômicas

Snapshots e produtos de pipeline devem:

1. ser escritos inicialmente em diretório temporário ou parcial;
2. ser validados antes da publicação;
3. ser promovidos ao destino final por operação atômica;
4. recusar sobrescrita por padrão;
5. remover resíduos parciais após falha, quando isso puder ser feito com
   segurança;
6. registrar manifesto com arquivos, URLs, tamanhos e hashes;
7. preservar a captura original sem normalização destrutiva.

Opções como `--replace` não devem ser usadas sem autorização explícita quando
puderem substituir uma execução existente.

## Qualidade e validação

Antes de concluir uma alteração:

1. executar:

   ```bash
   make verify
   ```

2. executar o pipeline real diretamente associado à alteração;
3. examinar as saídas geradas, especialmente os CSVs de manifesto, resumo,
   validação, diferenças e decisões;
4. verificar, conforme aplicável:
   - colunas obrigatórias;
   - tipos;
   - unidades;
   - valores ausentes;
   - duplicidades de chave;
   - cobertura temporal;
   - cobertura geográfica;
   - quantidade de arquivos;
   - quantidade de tabelas;
   - quantidade de linhas;
   - totais e medidas de reconciliação;
   - hashes;
   - proveniência;
   - limitações;
5. comparar a execução atual com a execução anterior;
6. registrar e classificar todas as diferenças;
7. adicionar teste automatizado para cada falha real encontrada;
8. repetir testes e pipeline após a correção;
9. examinar novamente as saídas finais.

A aprovação dos testes não substitui a inspeção do pipeline real e dos
artefatos produzidos.

O lint obrigatório estabilizado é o executado por `make verify`. Débitos do
código histórico fora de `src/sbmi` não devem ser corrigidos incidentalmente.

## Comparação de resultados

Classificações mínimas:

- `IDENTICAL`
- `EXPECTED_CHANGE`
- `SOURCE_UPDATE`
- `METHODOLOGY_CHANGE`
- `ERROR`
- `UNEXPLAINED`

Um resultado `UNEXPLAINED` impede a substituição ou promoção automática do
produto anterior.

Toda comparação deve registrar:

- execução anterior;
- execução atual;
- indicadores comparados;
- diferenças observadas;
- classificação;
- justificativa;
- decisão de preservação, quarentena ou promoção.

## Duplicidades e sobreposições

Classificações mínimas:

- `EXACT_DUPLICATE`
- `CONTENT_DUPLICATE`
- `PARTIAL_OVERLAP`
- `COMPLEMENTARY`
- `CONFLICT`
- `UNIQUE`

Igualdade de hash comprova igualdade binária do conteúdo observado, mas não
determina redundância conceitual, autoridade, qualidade ou possibilidade de
exclusão.

Nenhuma fonte bruta deve ser removida em decorrência de classificação de
duplicidade.

## Alterações de arquitetura e reconstruções

Mudanças estruturais relevantes exigem, antes da implementação:

1. justificativa documentada;
2. arquivos e camadas afetados;
3. impacto sobre dados e resultados existentes;
4. riscos;
5. estratégia de migração;
6. estratégia de reversão;
7. testes;
8. execução paralela ou comparação quando aplicável;
9. revisão em pull request;
10. aprovação explícita do responsável pelo projeto.

Reconstruções devem publicar novos produtos em novo destino. Produtos
históricos devem permanecer preservados até que todas as diferenças estejam
explicadas e a substituição seja autorizada.

## Relato obrigatório ao final de cada etapa

O diagnóstico deve apresentar separadamente:

### Evidências observadas

Arquivos, metadados, respostas, linhas, valores e resultados diretamente
examinados.

### Resultados calculados

Contagens, hashes, comparações e demais resultados determinísticos.

### Estimativas

Heurísticas, inferências e aproximações, incluindo suas limitações.

### Interpretações

Significado técnico ou analítico atribuído às evidências.

### O que pode ser concluído

Conclusões sustentadas pelas evidências disponíveis.

### O que não pode ser concluído

Afirmações ainda não sustentadas, dependências pendentes e limitações.

### Recomendações

Próxima ação proposta, riscos e necessidade de autorização.

Também devem ser informados:

- arquivos modificados ou criados;
- artefatos gerados;
- testes executados;
- pipeline real executado;
- resultados das validações;
- diferenças em relação à execução anterior;
- operações externas realizadas;
- confirmação de que arquivos históricos não foram modificados;
- estado de commit e pull request.

## Segurança e operações externas

- Usar GitHub Codespaces Secrets para credenciais necessárias.
- Configurar acesso ao Drive fora do repositório.
- Não executar escrita, sincronização, exclusão ou movimentação no Drive.
- Não acessar serviços externos sem apresentar objetivo, escopo, volume,
  riscos e obter autorização.
- Preferir endpoints oficiais, documentados e verificáveis.
- Aplicar limites de tamanho, timeout, domínios permitidos e validação de tipo
  de conteúdo.
- Não contornar controles de acesso, desafios automatizados ou proteções dos
  provedores.
- Não expor conteúdo sensível em mensagens, comandos, logs ou artefatos.

## Restrições de conclusão

Uma etapa não pode ser declarada concluída apenas porque:

- o comando terminou sem erro;
- os testes passaram;
- dois arquivos têm nomes semelhantes;
- dois produtos têm conteúdo equivalente;
- uma página pertence a domínio oficial;
- um valor parece plausível;
- um artefato histórico é legível.

A conclusão exige evidência proporcional ao que está sendo afirmado e registro
explícito das limitações remanescentes.
