# Coleta de valores das quatro fontes complementares

Este pipeline aplica às quatro fontes autorizadas o mesmo procedimento de
governança usado na coleta histórica do SIDRA:

- Panorama do Censo 2022/IBGE;
- panorama municipal do IBGE Cidades;
- perfil territorial do Observatório Sebrae;
- explorador de dados do IPS Brasil.

Cada execução usa um identificador novo e publica, sem sobrescrita, artefatos
separados em `raw`, `staging`, `curated`, `exports` e `audit`. As respostas
originais permanecem imutáveis. O manifesto registra instituição, autoria
declarada, URL solicitada e final, data e hora de obtenção, período declarado,
município, tipo de conteúdo, tamanho, SHA-256, arquivo e natureza da evidência.

## Períodos

Somente valores com ano entre 1996 e 2026 são promovidos. A regra não preenche
anos ausentes:

- Censo 2022: períodos efetivamente devolvidos pelos indicadores acionados
  pelo panorama oficial;
- IBGE Cidades: períodos disponíveis em cada indicador panorâmico;
- Sebrae: períodos publicados por cada consulta incorporada ao perfil;
- IPS Brasil: edições 2024, 2025 e 2026.

As edições do IPS são mantidas separadas e recebem a advertência metodológica
já documentada: não são estritamente comparáveis entre si.

## Transformação

As respostas JSON do IBGE são normalizadas por indicador, localidade e período.
As respostas tabulares do Sebrae são preservadas por consulta, linha e campo.
Os CSVs nacionais do IPS são preservados integralmente no `raw`, mas somente a
linha com código IBGE `4318002` é promovida às camadas seguintes.

O pipeline não cria dimensões analíticas. Ele conserva as dimensões existentes
registradas no inventário; fontes multidimensionais permanecem marcadas como
transversais até a revisão semântica dos indicadores.

## Execução

```bash
python -m sbmi.complementary_source_values_cli
```

Limites padrão:

- 45 segundos por resposta;
- 5 MB por resposta;
- 20 MB para a execução completa.

A publicação ocorre por diretórios parciais promovidos atomicamente. Qualquer
colisão, domínio não autorizado, resposta vazia, geografia divergente,
duplicidade de chave ou ausência de uma das quatro fontes interrompe a
execução sem substituir produtos anteriores.
