# São Borja — Inteligência Mercadológica

## Ponto de situação em 24 de julho de 2026

Este documento registra o estado técnico, metodológico e analítico do projeto no encerramento da estabilização inicial e da incorporação dos primeiros módulos sociais da Base Territorial Comum.

> Atualização operacional de 28 de julho de 2026: os arquivos existentes são
> tratados como originais por premissa declarada pelo responsável. O trabalho
> subsequente prioriza duplicidades, sobreposições, interpretação conceitual e
> validade das transformações. A decisão está registrada em
> `docs/audit_operating_premise_20260728.md` e não altera os resultados
> históricos documentados abaixo.

Referência do repositório no momento deste registro:

```text
branch: main
commit: ec5beeeb4f497b12133dd720217864d9cf575b93
```

## 1. Delimitação do projeto

O projeto organiza uma plataforma de inteligência mercadológica territorial para São Borja, sua região de influência e mercados comparáveis.

A estrutura editorial permanece dividida em:

1. **Base Territorial Comum de São Borja**, com informações macroambientais e territoriais transversais;
2. **Comércio varejista de bens essenciais**;
3. **Saúde, higiene e cuidados pessoais**;
4. **Bens não essenciais**;
5. **Serviços e alimentação fora do lar**.

A Base Territorial Comum não pertence a um setor específico. Ela deve sustentar os quatro cadernos setoriais com dados demográficos, econômicos, sociais, educacionais, fiscais, de infraestrutura e de contexto territorial.

## 2. Arquitetura vigente

- **GitHub:** código, configurações sem segredos, testes e documentação;
- **GitHub Codespaces:** ambiente principal de desenvolvimento, auditoria e processamento;
- **Google Drive:** fontes originais, produtos históricos e exportações;
- **Google Drive API v3:** acesso direto por conta de serviço com permissão de visualização;
- **DuckDB e arquivos locais em `.data`:** camada analítica reconstruível e não versionada;
- **Supabase:** previsto para uma fase posterior de publicação e consulta, ainda não implantado.

O Google Colab deixou de ser o ambiente ativo. O notebook histórico `Analise_SB.ipynb` permanece preservado como registro do desenvolvimento anterior.

## 3. Governança de dados adotada

Fluxo lógico:

```text
raw → staging → curated → exports
```

Regras principais:

- fontes brutas são imutáveis;
- o Drive é acessado em modo somente leitura pelas rotinas de auditoria;
- snapshots locais são seletivos e verificáveis por tamanho e SHA-256;
- `.data` não é versionado no GitHub;
- produtos derivados não são substituídos enquanto diferenças permanecerem sem explicação;
- duplicidades de arquivo e duplicidades de conteúdo são tratadas como classes distintas;
- alterações de reprocessamento devem ser classificadas como mudança esperada, atualização de fonte, mudança metodológica, erro ou diferença ainda não explicada.

## 4. Estabilização técnica concluída

### 4.1 Inventário do Google Drive

**Dados observados:**

- 1.127 entradas;
- 40 pastas;
- 1.087 arquivos;
- 2.042.029.593 bytes conhecidos;
- 4 arquivos sem SHA-256 disponível;
- 15 grupos de duplicidade binária exata, envolvendo 30 linhas do inventário.

Limitação: o inventário valida estrutura, metadados e integridade disponível, mas não representa validação substantiva de todos os indicadores históricos.

### 4.2 Auditoria de `raw/new_files`

**Dados observados:**

- 34 arquivos;
- 590.693 bytes;
- todos com SHA-256;
- 29 arquivos federais;
- 3 arquivos municipais;
- 2 arquivos estaduais.

Não foram encontradas duplicidades binárias exatas dentro da caixa de entrada ou em relação ao restante do acervo.

Uma duplicidade de conteúdo normalizado foi identificada entre:

```text
COFINANCIAMENTO DA PROTECAO SOCIAL BASICA.xlsx
COFINANCIAMENTO DA PROTECAO SOCIAL BASICA(1).xlsx
```

A cópia com sufixo foi excluída apenas dos produtos derivados. Os dois arquivos brutos permanecem preservados.

### 4.3 Staging construído e validado

Foram construídos seis datasets:

1. `federal_transferencias`;
2. `estadual_icms`;
3. `estadual_transferencias`;
4. `municipal_despesas_instituicao`;
5. `municipal_despesas_elemento`;
6. `municipal_receita_elemento`.

**Dados observados:**

- 8.413 linhas;
- 33 tabelas-fonte incluídas;
- uma fonte de 64 linhas excluída por duplicidade de conteúdo;
- validação concluída sem erros ou alertas estruturais.

No ICMS estadual foram mantidas 29 ocorrências sinalizadas, pertencentes a 10 grupos de linhas duplicadas, equivalentes a 19 ocorrências excedentes. Elas permanecem no staging até validação da fonte.

### 4.4 Produtos históricos auditados

Foram capturados seletivamente arquivos de `processed`, `warehouse` e `exports`.

**Dados observados:**

- 924 arquivos;
- 250.125.612 bytes;
- 920 arquivos válidos;
- 3 arquivos vazios;
- 1 arquivo auxiliar;
- 932 tabelas;
- 4.564.680 linhas;
- 17 famílias de dados;
- 14 grupos de duplicidade exata, envolvendo 28 registros do inventário.

A auditoria concluiu que não havia evidência de corrupção generalizada ou necessidade de reconstrução integral do acervo.

Documento de encerramento:

```text
docs/stabilization_audit_closure_20260724.md
```

## 5. Base Territorial Comum: módulos incorporados

### 5.1 IDSC-BR 2025

Fonte:

```text
raw/social/Base_de_Dados_IDSC-BR_2025.xlsx
```

**Dados observados:**

- 53.964.472 bytes;
- 5.570 linhas;
- 442 colunas;
- 17 pontuações de ODS para São Borja;
- 11 indicadores no factsheet municipal.

**Resultado calculado:**

- criação de resumo municipal e factsheet portáteis;
- comparação com os produtos históricos existentes;
- resultado `IDENTICAL` para os dois produtos, sem células divergentes.

As classes interpretativas do módulo são internas e não substituem classificações oficiais do IDSC-BR.

Documentação:

```text
docs/base_territorial_idsc.md
```

### 5.2 IPS Brasil: edições originalmente publicadas de 2024, 2025 e 2026

Fonte:

```text
https://ipsbrasil.org.br/explore/scorecard/4318002?year=<ANO>
```

O site utiliza Phoenix LiveView. As pontuações não estão presentes no HTML estático inicial e só aparecem após renderização em navegador. Por isso, o módulo usa Playwright com Chromium.

**Dados observados na execução real:**

- 3 scorecards renderizados;
- 370.086 bytes armazenados;
- 3 navegações do navegador;
- 48 pontuações agregadas;
- 16 registros por edição;
- resumo de 2026 com 16 registros;
- contrato estrutural de 1 índice geral, 3 dimensões e 12 componentes.

**Tratamento metodológico:**

- as edições originais são registradas separadamente;
- nenhuma variação temporal é calculada entre elas;
- os valores individuais dos indicadores não são inferidos de elementos visuais;
- a série harmonizada permanece fora deste módulo.

Documentação:

```text
docs/base_territorial_ips_published.md
```

## 6. Qualidade e estado do repositório

Na última execução completa validada:

- 80 testes automatizados aprovados;
- Ruff aprovado;
- GitHub Actions aprovado;
- branch do módulo IPS mesclada e removida;
- `main` atualizada no commit `ec5beee`.

Os artefatos do IPS permanecem localmente em:

```text
.data/snapshots/web/social_ips/ips-brasil-rendered-published-2024-2026/
.data/curated/base_territorial/social/ips/published_2024_2026/
```

Esses diretórios não estão no GitHub e devem ser reconstruídos ou preservados no ambiente de trabalho conforme a política de snapshots.

## 7. Pendências e limitações conhecidas

### 7.1 Dados e validação

- a estabilização não equivale à validação substantiva de todos os indicadores históricos;
- as 29 ocorrências duplicadas do ICMS estadual ainda exigem conferência da fonte;
- os quatro arquivos do inventário sem SHA-256 permanecem com verificação limitada;
- a existência de produtos derivados em `processed`, `warehouse` e `exports` não garante que suas metodologias tenham sido revisadas;
- não foi localizada no Drive uma base nominalmente identificada como IPS Brasil; buscas por `IPS` retornaram materiais da empresa Ipsos, não o Índice de Progresso Social.

### 7.2 Base Territorial Comum

Ainda é necessário revisar, consolidar ou construir os demais blocos transversais, entre eles:

- demografia;
- economia e estrutura produtiva;
- renda, emprego e trabalho;
- educação;
- infraestrutura e conectividade;
- finanças públicas;
- saúde e condições sociais;
- ambiente político, regulatório, sociocultural e territorial, quando pertinente.

A disponibilidade de dados já existentes no Drive deve ser auditada antes de qualquer nova coleta externa.

### 7.3 IPS Brasil

- construir, em módulo separado, a série harmonizada de 2024 a 2026 recalculada com os parâmetros de 2026;
- investigar o fluxo LiveView ou outra fonte oficial para essa série;
- não misturar a série harmonizada com as edições originalmente publicadas;
- não calcular tendência antes de confirmar a comparabilidade metodológica.

### 7.4 Produtos analíticos e publicação

- consolidar os módulos validados em tabelas curadas comuns;
- definir indicadores e visualizações do primeiro caderno;
- concluir a análise macroambiental da Base Territorial Comum;
- integrar os quatro estudos setoriais de 2026 aos respectivos cadernos;
- definir o modelo final de publicação e consulta;
- implantar Supabase somente depois da estabilização do modelo de dados e dos contratos de atualização.

## 8. Próxima etapa recomendada

Antes de abrir um novo módulo, realizar um mapa de cobertura da Base Territorial Comum:

1. listar as famílias de dados territoriais já existentes no Drive;
2. identificar fonte, período, unidade, abrangência e estágio de processamento;
3. separar fontes brutas de produtos derivados;
4. identificar lacunas reais;
5. escolher o próximo módulo com base em relevância analítica, qualidade da fonte e custo de integração.

Essa etapa reduz coleta duplicada, evita reconstruir produtos existentes e permite estabelecer uma sequência racional para a conclusão do primeiro caderno.

## 9. Procedimento de retomada

```bash
git switch main
git pull --ff-only
make verify
```

Para cada novo módulo:

1. criar uma branch temática;
2. desenvolver e testar;
3. validar com a fonte real;
4. documentar resultados e limitações;
5. abrir e mesclar um PR;
6. remover a branch após o merge;
7. atualizar este ponto de situação quando houver mudança relevante de fase.

## 10. Natureza deste documento

Este arquivo é uma memória operacional versionada. Ele registra o estado conhecido em 24 de julho de 2026 e não substitui:

- os manifests de dados;
- os documentos metodológicos de cada módulo;
- os relatórios analíticos finais;
- os snapshots locais;
- as fontes originais preservadas no Google Drive.
