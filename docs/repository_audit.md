# Auditoria inicial do repositório

Data da auditoria: 2026-07-23

## Escopo observado

O repositório contém builders modulares em `src/modeling/`, criados para execução no Google Colab e gravação direta no Google Drive.

Os módulos já identificados incluem:

- econômico;
- fiscal;
- social;
- IDSC.

O histórico de commits confirma que os últimos trabalhos realizados foram os builders do módulo social e do IDSC em 2 de junho de 2026.

## Achados

### 1. Caminhos absolutos do Colab

Os builders consultados utilizam caminhos como:

```text
/content/drive/MyDrive/Colab Notebooks/_sao_borja/raw/...
/content/drive/MyDrive/Colab Notebooks/_sao_borja/exports
```

Consequência: o código não é portável para Codespaces ou execução local sem alteração.

### 2. Dependências implícitas

Não havia configuração formal de ambiente no repositório. As bibliotecas eram instaladas ou disponibilizadas pelo ambiente do Colab.

Consequência: uma execução futura poderia usar versões diferentes e produzir comportamento incompatível.

### 3. Dependência entre arquivos exportados

Alguns builders leem resultados anteriores diretamente da pasta `exports`.

Consequência: a ordem de execução é relevante, mas ainda não está formalizada como grafo ou pipeline.

### 4. Sobrescrita de resultados

Os builders gravam os CSVs finais com nomes estáveis, substituindo o arquivo anterior.

Consequência: não há preservação automática da execução anterior nem comparação antes da substituição.

### 5. Auditoria limitada de origem

Os inventários existentes registram principalmente nome, extensão, linhas, colunas e status de leitura.

Consequência: ainda faltam hashes, identificador do Drive, fonte, período, unidade, abrangência e status de governança.

### 6. Ausência de testes e integração contínua

Não foram encontrados testes automatizados nem verificações de CI no estado inicial do repositório.

Consequência: mudanças de código podem alterar resultados sem detecção automática.

## Aspectos preservados

A arquitetura existente possui qualidades que serão mantidas:

- builders com responsabilidade relativamente delimitada;
- nomenclaturas consistentes por módulo;
- etapas de inventário, catálogo, mapa de domínio, painel, resumo, factsheet e storyboard;
- impressão de auditorias e resultados durante a execução;
- exportações em formatos simples e inspecionáveis;
- histórico de alterações preservado no GitHub.

## Estratégia de migração

1. preservar `src/modeling/` sem alterações funcionais iniciais;
2. introduzir ambiente reproduzível;
3. introduzir caminhos portáveis e configuração externa;
4. construir inventário com hashes;
5. auditar `raw/new_files`;
6. criar testes de caracterização dos resultados atuais;
7. migrar builders gradualmente;
8. reprocessar e comparar resultados antes de qualquer substituição.

## Limitação desta auditoria

Esta é uma auditoria estrutural inicial. A listagem completa de todos os arquivos e dependências será gerada no Codespace pelo inventário automatizado, após a conexão segura e somente leitura com o Google Drive.
