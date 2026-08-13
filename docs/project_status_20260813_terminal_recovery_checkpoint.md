# Checkpoint de recuperação do terminal — 2026-08-13

## Objetivo

Este checkpoint registra o estado local comprovado após duas reconstruções do
terminal, para que a continuação não dependa do histórico da conversa. Nenhuma
operação externa foi realizada nesta retomada.

## Evidências observadas

- O repositório está na branch `feature/new-files-temporal-coverage`, alinhada
  com `origin/feature/new-files-temporal-coverage` no último estado examinado.
- O último commit da branch é `b3b4f76`, de 2026-07-31, com a mensagem
  `Add authenticated Transparencia API client checkpoint`.
- O diretório de trabalho contém 3 arquivos rastreados modificados e 37
  arquivos novos não rastreados.
- Não houve commit, push, criação ou atualização de pull request, nem merge.
- `.data`, `.ruff_cache` e `*.egg-info` permanecem ignorados pelo Git.
- A revisão por padrões não encontrou credenciais reais no conjunto pendente;
  as ocorrências de `test-key` pertencem aos testes da API da Transparência.
- Não foram encontrados diretórios residuais com sufixo `.partial` em `.data`.

## Resultados calculados

`make verify` foi executado após a reconstrução do terminal e registrou:

- `sbmi doctor` com `status=ok`;
- 274 testes aprovados;
- Ruff aprovado sem achados.

Cinco pipelines exclusivamente locais foram executados com novos
identificadores:

| Produto | Nova execução | Resultado |
| --- | --- | --- |
| Empresas e emprego | `business-employment-series-20260813-193959` | 30 linhas |
| Educação | `education-series-20260813-194000` | 67 linhas |
| Finanças públicas locais | `public-finance-series-20260813-194200` | 20 linhas, 15 indicadores, 2019–2025 |
| DCA/SICONFI curado | `siconfi-dca-series-20260813-194200` | 268 linhas, 18 contas, 110 combinações ausentes |
| Canônico territorial paralelo | `canonical-series-20260813-194003` | 3.041 fatos e 145 indicadores |

Os quatro produtos temáticos foram comparados por SHA-256 com as execuções
anteriores registradas no checkpoint de séries e classificados como
`IDENTICAL`. Os seis artefatos do canônico territorial também apresentaram
SHA-256 idêntico à execução `canonical-series-20260813-003301`:

- `canonical_manifest.csv`;
- `dim_indicator.parquet`;
- `dim_territory.parquet`;
- `fact_territorial_indicator.parquet`;
- `source_reconciliation.csv`;
- `validation_summary.csv`.

O canônico reconciliou 1.920 fatos históricos preservados e 1.121 fatos
promovidos. Foram registradas 58 exclusões por ausência ou supressão, zero
chaves duplicadas, zero nulos obrigatórios e zero arquivos históricos
modificados. Todos os indicadores examinados estavam com status `PASS`.

## Estimativas

Nenhuma estimativa, imputação ou inferência numérica foi produzida nesta
retomada.

## Interpretações

- A reconstrução do terminal não alterou a reprodutibilidade dos cinco
  pipelines locais examinados.
- A igualdade de SHA-256 comprova igualdade binária dos produtos comparados,
  mas não amplia a autoridade ou a comparabilidade conceitual das fontes.
- Os pipelines externos e a planilha Google Sheets `v004` não foram
  revalidados nesta retomada.

## Inconsistência documental pendente

O arquivo `docs/project_status_20260813_series_checkpoint.md` contém uma frase
desatualizada em `O que não pode ser concluído`, afirmando que não houve
integração ao modelo territorial canônico. O próprio checkpoint documenta que
a integração paralela e aditiva foi concluída.

A correção planejada é substituir essa afirmação por:

> Não foi realizada comparação conceitual de equivalência entre famílias. A
> integração ao modelo territorial foi apenas paralela e aditiva, sem promover
> ou substituir os produtos canônicos históricos.

## Bloqueio do ambiente

As tentativas de usar o mecanismo obrigatório `apply_patch` falharam antes da
leitura do arquivo, com erro do helper de sandbox relacionado a `bwrap`. O
diagnóstico observou que o kernel permite namespaces, mas o executável `bwrap`
não está disponível no `PATH`. Não foi usado `sed`, Python, redirecionamento ou
outro mecanismo alternativo para contornar a restrição de edição.

## O que pode ser concluído

- O ambiente Python, a suíte de testes e o lint estão funcionais.
- Os cinco pipelines locais são reproduzíveis para as entradas preservadas.
- Não foi observada diferença `UNEXPLAINED`.
- Nenhum arquivo bruto, snapshot ou produto histórico foi modificado,
  removido, renomeado ou sobrescrito nesta retomada.

## O que não pode ser concluído

- A disponibilidade atual dos endpoints externos não foi verificada.
- As capturas externas não foram reexecutadas.
- A planilha `v004` no Google Drive não foi revalidada.
- O conjunto pendente ainda não passou por revisão em pull request.

## Próxima ação recomendada

1. restaurar o funcionamento do `apply_patch` no ambiente;
2. aplicar a correção documental delimitada no checkpoint de séries;
3. executar `git diff --check` e `make verify`;
4. revisar o diff final e o inventário dos 40 arquivos pendentes;
5. solicitar autorização explícita antes de commit, push ou abertura de pull
   request.

## Estado de operações externas e Git

Nesta retomada não houve acesso a serviços externos, escrita no Google Drive,
download, commit, push, pull request ou merge. Os novos artefatos foram criados
somente em `.data`, com identificadores próprios, e os produtos históricos
foram preservados.

---

## Continuação da recuperação — revisão dos achados e do diff

Esta seção registra a continuação executada no mesmo Codespace em 2026-08-13.
O diretório foi novamente confirmado como
`/workspaces/sao-borja-market-intelligence`. O mecanismo `apply_patch`
funcionou neste modo, sem iniciar a camada anteriormente bloqueada por `bwrap`.

### Evidências observadas

- A promoção sequencial de múltiplas camadas removia somente diretórios
  `.partial` após uma falha; destinos finais já promovidos podiam permanecer.
- A curadoria DCA/SICONFI consumia os arquivos indicados no manifesto sem
  recalcular tamanho e SHA-256.
- A captura DCA/SICONFI não validava `Content-Type` nem URL final.
- O pipeline de PIB/VAB validava o host final, mas não exigia HTTPS nem o tipo
  de conteúdo esperado para cada fonte.
- Seis CLIs sem parser de argumentos podiam executar o pipeline ao receber
  `--help`; quatro deles envolvem captura externa.
- A revisão por padrões não encontrou credenciais reais no conjunto pendente.
- Não foram encontrados diretórios residuais com sufixo `.partial` em `.data`.

### Resultados calculados

- Os 14 JSONs dos dois snapshots DCA locais foram recalculados por SHA-256 e
  coincidiram com os respectivos manifestos.
- Foram adicionados controles de rollback às sete publicações multicamada:
  SIDRA histórico, demografia censitária, PIB/VAB, empresas e emprego,
  educação, finanças públicas locais e série DCA/SICONFI.
- A curadoria DCA passou a validar confinamento do caminho, existência,
  tamanho e SHA-256 antes de ler cada JSON.
- A captura DCA passou a validar resposta não vazia, `Content-Type` JSON,
  HTTPS, host oficial e caminho final do endpoint.
- O pipeline PIB/VAB passou a validar HTTPS e os tipos JSON e ZIP conforme a
  fonte, registrando o `Content-Type` no manifesto.
- Os seis CLIs passaram a interpretar argumentos antes de qualquer leitura,
  escrita ou acesso HTTP; um teste parametrizado comprova que `--help` não
  chama os builders.
- Os testes direcionados dos três achados registraram 18 aprovações; o teste
  dos contratos de CLI registrou 6 aprovações.
- A validação final `make verify` registrou `sbmi doctor` com `status=ok`, 287
  testes aprovados e Ruff aprovado.
- `git diff --check` foi aprovado.

Quatro pipelines locais foram executados com novos identificadores e seus
produtos curados foram classificados como `IDENTICAL` por SHA-256 em relação
às execuções anteriores:

| Produto | Execução de revisão | Linhas | SHA-256 do produto curado |
| --- | --- | ---: | --- |
| Empresas e emprego | `business-employment-series-20260813-225704` | 30 | `21521e16e94fc2c3e73f918defd4d0e388ba7f4ba1495113962d607e6620d0d2` |
| Educação | `education-series-20260813-225705` | 67 | `54906c87ff84e2d0db2d825669e1d1532aba1357e9401dfd0ac392f33f0ac0b6` |
| Finanças públicas locais | `public-finance-series-20260813-review-001` | 20 | `7da821fcabb6bb1fbb6dfab81f404338ff125ef61a39bff8e7b668dda21145ee` |
| DCA/SICONFI curado | `siconfi-dca-series-20260813-review-001` | 268 | `09f3fd44ce09bb77b3a9d6c843a1c7d642d7c10e4576c574cb585efc134046c7` |

A DCA manteve 18 contas, sete exercícios, zero duplicidades e 110
combinações ausentes registradas como `MISSING`, sem imputação por zero.

### Estimativas

Nenhuma estimativa, imputação ou inferência numérica foi produzida.

### Interpretações

- Os três achados revisados eram procedentes e agora possuem controles
  preventivos e testes automatizados.
- Os snapshots DCA locais examinados não apresentam evidência de corrupção.
- A igualdade de SHA-256 comprova igualdade binária dos produtos comparados,
  sem comprovar equivalência conceitual ou autoridade adicional.
- O comportamento anterior de `--help` constituía risco operacional, pois uma
  inspeção da interface podia criar artefatos ou acessar rede.

### O que pode ser concluído

- Os três achados solicitados foram corrigidos e validados localmente.
- Os quatro pipelines locais permanecem reproduzíveis para as entradas
  preservadas.
- Não foi observada diferença `UNEXPLAINED`.
- O conjunto pendente não apresenta segredo evidente, falha de teste, erro de
  lint, erro de whitespace ou resíduo parcial.
- Nenhum arquivo bruto, snapshot ou produto histórico foi alterado,
  sobrescrito, movido, renomeado ou removido.

### O que não pode ser concluído

- A disponibilidade atual dos endpoints externos não foi verificada.
- Os controles HTTP novos foram exercitados por testes, mas não por nova
  captura externa nesta continuação.
- A planilha `v004` no Google Drive não foi revalidada.
- O conjunto pendente ainda não passou por revisão formal em pull request.

### Arquivos e artefatos

Foram modificados nesta continuação os módulos e testes relacionados ao
rollback multicamada, integridade DCA, validação HTTP e contratos de CLI. Foi
criado `tests/test_series_cli_contract.py`. A documentação do canônico passou
a distinguir hashes calculados de validação contra manifestos upstream, e a
documentação DCA passou a registrar os novos controles.

Os quatro novos produtos locais foram criados somente em `.data`, sob os IDs
listados acima. As execuções anteriores permaneceram preservadas.

### Operações externas e estado Git

Não houve acesso a serviços externos, escrita no Google Drive, download,
commit, push, criação ou atualização de pull request, nem merge nesta
continuação. O trabalho permanece na branch
`feature/new-files-temporal-coverage`.

### Próxima ação recomendada

Realizar revisão humana do conjunto pendente e decidir se ele deve ser dividido
em mais de um commit ou pull request. Commit, push e operações de pull request
continuam condicionados a autorização explícita do responsável pelo projeto.
