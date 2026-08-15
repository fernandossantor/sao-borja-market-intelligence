# Checkpoint da decisão de escopo da planilha v005 — 2026-08-15

## Objetivo

Classificar blocos da proposta local da planilha v005 como `GO`,
`QUARANTINE` ou `BLOCKED`, mantendo separadas a prontidão técnica, a
autorização de escrita externa, a proveniência e a validade temporal.

Esta etapa produziu somente uma decisão local. Não criou planilha, não
promoveu dados, não acessou o Google Drive e não alterou a v004, snapshots,
arquivos brutos ou produtos históricos.

## Evidências observadas

- O pacote integrado `spreadsheet-v005-integrated-package-20260814-001`
  registra 413 séries, 319 indicadores únicos e 3.630 observações numéricas.
- O pacote dos fatos canônicos ausentes contém 46 fatos e três registros de
  fonte, todos com hashes locais reconciliados.
- Quarenta fatos econômicos usam a API SIDRA/IBGE e três usam um arquivo
  histórico do PIB municipal publicado pelo IBGE. Os registros contêm URL,
  horário de obtenção e hashes do original e da entrada imediata.
- Três fatos de composição domiciliar declaram IBGE/Censo 2022, mas o
  manifesto registra `EVIDENCE_NOT_AVAILABLE` para URL, URL final e horário de
  obtenção do XLSX original.
- A prontidão não canônica contém 115 séries e 589 valores numéricos:
  - 9 séries demográficas;
  - 11 séries empresariais;
  - 95 séries de finanças públicas, das quais 91 possuem valores e 4 estão
    vazias.
- As 115 séries têm decisão anterior `BLOCK_PROMOTION`; 111 possuem linhagem
  local verificada, mas ainda não foram modeladas conceitualmente.
- A revisão temporal corrigida registra 81 valores de ano abreviado no arquivo
  fiscal `Legais, Voluntárias e Específicas Primária Saúde 2020 - 2026.csv`.
  Todos estão como `AMBIGUOUS_DATE` e `PENDING_TEMPORAL_VALIDATION`.
- A exceção de escrita vigente inclui fontes IBGE/SIDRA, Censo 2022 e
  Sebrae/Datawheel, mas não inclui genericamente dados fiscais nem autoriza um
  pacote consolidado de escopo misto.

## Resultados calculados

Foram registrados oito blocos de decisão:

| Decisão | Blocos | Conteúdo principal |
| --- | ---: | --- |
| `GO` | 2 | 43 fatos econômicos IBGE/SIDRA |
| `QUARANTINE` | 4 | 3 fatos domiciliares, 20 séries não modeladas e 81 datas ambíguas |
| `BLOCKED` | 2 | 95 séries fiscais e o pacote integral da v005 |

Os 43 fatos `GO` são candidatos apenas a um futuro plano reduzido e
controlado. A decisão não executa nem autoriza automaticamente uma escrita;
qualquer operação externa ainda exige preflight, destino validado e
autorização específica para a etapa.

As 115 séries e os 589 valores não canônicos foram integralmente
contabilizados. Nenhum valor foi descartado ou promovido.

## Critérios de decisão

### `GO`

Usado quando o bloco possui pacote local validado, fonte dentro da exceção
vigente, proveniência mínima comprovada e nenhuma pendência temporal conhecida
que impeça planejar uma publicação reduzida.

### `QUARANTINE`

Usado quando a família de fonte pode estar dentro da exceção, mas permanece
uma lacuna de proveniência, modelagem conceitual ou interpretação temporal.

### `BLOCKED`

Usado quando o bloco está fora do escopo externo autorizado, mistura famílias
com decisões diferentes ou depende de expansão de governança além de
remediações técnicas.

## Matriz de decisão

1. PIB corrente, 40 fatos: `GO`.
2. PIB histórico 1999–2001, 3 fatos: `GO`, preservando a separação
   metodológica.
3. Composição domiciliar, 3 fatos: `QUARANTINE` por lacuna de URL e horário da
   captura original.
4. Demografia não canônica, 9 séries: `QUARANTINE` por modelagem conceitual
   pendente.
5. Empresas/DataSebrae, 11 séries: `QUARANTINE` por modelagem explícita da
   extração datada pendente.
6. Finanças públicas não canônicas, 95 séries e 569 valores: `BLOCKED` por
   modelagem pendente e escopo externo não autorizado.
7. Datas fiscais abreviadas, 81 valores: `QUARANTINE`; nenhum século foi
   inferido.
8. Pacote integral v005, 413 séries: `BLOCKED` por escopo misto e dependência
   dos blocos em quarentena ou bloqueados.

## Artefatos gerados

Execução nova, sem sobrescrita:

`spreadsheet-v005-scope-decision-20260815-001`

Diretório:

`.data/audit/base_territorial/spreadsheet_reconciliation/spreadsheet-v005-scope-decision-20260815-001`

Arquivos:

| Arquivo | SHA-256 |
| --- | --- |
| `scope_decisions.csv` | `14a6cc1d4d63ea865be6c1bdfc7d288d5cda8cec08dd779a13c94ac81f35744c` |
| `decision_summary.csv` | `2e53710819cf28db2eb08e707c143612e4d636ba1510d239c1bd5e8c29ff1411` |
| `source_manifest.csv` | `6ab126ce2a68f1d61e18ee2c59ce9f33db2181694b1b584eab292ee3185c75bc` |
| `validation.csv` | `cf42feef0cd7af890da084ef2b5d1aed6680d9cddddf11fc090c2a0ce31da3c9` |

O manifesto fixa oito entradas imediatas por caminho, tamanho e SHA-256.

## Validações executadas

O pipeline local criou os CSVs em diretório parcial, releu as entradas,
validou os totais e promoveu o diretório ao destino final por renomeação
atômica.

As 11 validações registradas em `validation.csv` passaram:

- oito blocos e somente três classes permitidas;
- 43 fatos econômicos em `GO`;
- três fatos domiciliares em quarentena;
- 115 séries e 589 valores não canônicos contabilizados;
- 81 datas ambíguas contabilizadas;
- pacote integral bloqueado;
- oito entradas presentes, com tamanhos e hashes coincidentes;
- zero escritas externas.

Não houve mudança de código e, por isso, não foram adicionados testes
direcionados. Ainda assim, a validação obrigatória `make verify` foi repetida:
`sbmi doctor` retornou `status=ok`, os 297 testes passaram e o Ruff não
registrou achados. O check remoto anterior `quality/test` também havia passado.

## Comparação com execuções anteriores

Não existe execução anterior da matriz de decisão para comparação binária.
Os totais de entrada reconciliam com os artefatos anteriores: 46 fatos, 115
séries, 589 valores e 81 ambiguidades. Nenhuma diferença foi classificada como
`UNEXPLAINED`.

A nova classificação é uma extensão interpretativa `EXPECTED_CHANGE` em
relação ao checklist anterior: o bloqueio integral foi decomposto em blocos
`GO`, `QUARANTINE` e `BLOCKED`, sem alterar os dados de origem.

## Estimativas

Nenhuma estimativa, imputação de século ou modelagem de valor foi realizada.

## Interpretações

- A evidência disponível sustenta planejar uma publicação reduzida dos 43
  fatos econômicos, mas não sustenta publicar o pacote integral.
- A instituição declarada como IBGE não elimina as lacunas de aquisição dos
  três fatos domiciliares.
- Linhagem local verificada não substitui modelagem conceitual.
- O nome do arquivo fiscal não comprova o século de cada data abreviada.

## O que pode ser concluído

- Os blocos da decisão estão delimitados e rastreáveis às entradas imediatas.
- Quarenta e três fatos econômicos podem avançar para planejamento de uma
  publicação reduzida, sujeito às validações e autorizações da operação.
- Os demais blocos devem permanecer preservados em quarentena ou bloqueados.
- A proposta integral da v005 não deve ser publicada no estado atual.

## O que não pode ser concluído

- Que `GO` equivalha a autorização automática de escrita no Drive.
- Que os três fatos domiciliares tenham proveniência de aquisição completa.
- Que as 20 séries demográficas e empresariais estejam conceitualmente prontas
  para promoção.
- Que as 95 séries fiscais estejam dentro da exceção vigente.
- Que o século correto das 81 datas abreviadas tenha sido comprovado.
- Que uma planilha v005 integral possa ser criada ou publicada.

## Operações externas e estado do Git

- Google Drive: não acessado.
- GitHub: não acessado nesta etapa.
- Outros serviços externos: não acessados.
- Arquivos históricos: não modificados.
- Branch: `feature/v005-scope-decision`.
- Commit: não realizado.
- Push: não realizado.
- Pull request: não criado.
- Merge: não realizado.

## Próxima ação recomendada

Preparar localmente um payload reduzido contendo somente os 43 fatos
econômicos `GO`, sem publicá-lo. A preparação deve derivar o payload existente,
recusar qualquer célula fora desses dois blocos, preservar os hashes das três
fontes e comparar o resultado com o pacote de 46 fatos. Somente após essa
validação deve ser apresentado objetivo, destino, volume e riscos para uma
eventual autorização de escrita externa.
