# São Borja — Inteligência Mercadológica

## Ponto de retomada dos recursos públicos em 30 de julho de 2026

Este documento registra o estado exato da frente de recursos públicos estaduais
e federais ao encerrar o trabalho de 30 de julho de 2026. Ele complementa os
pontos de situação anteriores e não substitui os documentos metodológicos dos
módulos.

Referência no momento de preparação:

```text
branch: feature/state-rs-expense-head-inventory
base incorporada: main em 9b12f09ffae151c6e78853d043d87a60cae323fd
PR desta etapa: #36
último PR estadual já incorporado: #35
```

O PR #36 deve estar incorporado e a `main` atualizada antes da próxima ação
descrita ao final.

## Evidências observadas

### Repositório e governança

- o PR #35 incorporou snapshot, perfil e staging do piloto estadual;
- o PR #36 contém o inventário `HEAD` e o pipeline mensal de despesas;
- dados extensos e artefatos reconstruíveis permanecem fora do Git;
- snapshots e execuções anteriores foram preservados;
- não houve escrita no Supabase;
- escritas no Google Drive ocorreram somente dentro da pasta autorizada
  `new_files`.

### Fontes estaduais

O catálogo CKAN da CAGE/RS contém 173 ZIPs mensais de despesas entre janeiro de
2012 e maio de 2026. Todos responderam HTTP 200 a `HEAD`, declararam
`application/zip` e informaram `Content-Length`.

O volume compactado declarado é 2.301.073.839 bytes. A parcela de 2012 a 2025
totaliza 2.234.688.540 bytes. O catálogo possui oito divergências entre o nome
do mês e o período codificado na URL:

- 2020: três;
- 2021: uma;
- 2022: uma;
- 2023: três.

Essas divergências são anomalias de metadados. Elas não comprovam, sem inspeção
interna, erro ou duplicidade de conteúdo.

Convênios de despesa possuem correspondências de São Borja entre 2003 e 2026.
Parcerias possuem correspondências entre 2017 e 2025 no snapshot examinado.
O recurso denominado `agreements_layout` contém dados tabulares e foi
classificado como `PARTIAL_OVERLAP` em relação a `agreements_expense`; ele
permanece em quarentena e não pode ser somado à base atual.

### Lote mensal estadual de 2026

O lote final de janeiro a abril de 2026 é:

```text
run_id: state-rs-expense-2026-01-04-20260730-003514
bytes compactados: 51.899.110
linhas examinadas: 1.331.658
correspondências de São Borja: 839
linhas estruturalmente irregulares: 5.237
codificação observada e aplicada: cp1252
```

Os quatro ZIPs possuem tamanho igual ao contrato derivado do inventário
`HEAD`, hash SHA-256 registrado, um CSV seguro cada e período interno
compatível. Nenhum CNPJ, favorecido, beneficiário, histórico, objeto, banco ou
agência foi persistido.

Todas as 839 linhas territorializadas estão classificadas como fase
`Liquidação`. As somas observadas, sem interpretação como receita municipal,
são:

| Mês | Linhas | Valor |
|---|---:|---:|
| janeiro | 130 | R$ 1.115.737,42 |
| fevereiro | 201 | R$ 1.326.404,84 |
| março | 293 | R$ 2.757.881,46 |
| abril | 215 | R$ 2.854.840,16 |
| total | 839 | R$ 8.054.863,88 |

Maio de 2026 foi capturado no piloto anterior:

```text
arquivo: state_expense_2026_05.zip
bytes: 14.486.189
linhas examinadas: 359.748
correspondências de São Borja: 208
linhas estruturalmente irregulares: 1.343
```

O staging de maio foi produzido antes da correção de codificação para
`cp1252`. Seus valores e seleção permanecem evidência útil, mas o produto deve
ser reprocessado pelo pipeline mensal corrigido antes de ser combinado com
janeiro–abril.

### Fontes federais

A descoberta preservada examinou cinco famílias:

1. painel da localidade;
2. transferências;
3. benefícios a residentes;
4. convênios;
5. programas ou gastos aplicados na localidade.

As cinco páginas do Portal da Transparência retornaram HTTP 405 com verificação
humana na execução `public-funds-discovery-20260729-230456`. Nenhuma amostra de
dados, valor ou registro pessoal foi capturada; todas permanecem
`NOT_INTEGRATED`.

O endereço oficial de download em massa informado para continuação é:

```text
https://portaldatransparencia.gov.br/download-de-dados
```

A alternativa é a API oficial:

```text
https://api.portaldatransparencia.gov.br/api-de-dados/
```

O uso da API depende de chave. O fluxo preferencial pendente é testar e
inventariar primeiro os downloads públicos que não exijam credencial.

Bases fiscais federais históricas já existentes no projeto não comprovam,
isoladamente, equivalência, autoridade ou ausência de sobreposição com as
novas extrações do Portal da Transparência. Qualquer incorporação nova precisa
de reconciliação explícita.

## Resultados calculados

- a série mensal estadual catalogada cobre 2012–2026 e não cobre 1996–2011;
- convênios estaduais ampliam parte da visão até 2003, sem preencher
  1996–2002;
- janeiro–abril e maio de 2026 somam 1.047 correspondências nominais válidas,
  mas ainda pertencem a execuções e metodologias que precisam ser
  reconciliadas;
- as linhas irregulares conhecidas nos cinco meses somam 6.580;
- o inventário mensal estadual restante, excluindo maio já capturado,
  representa 2.286.587.650 bytes compactados;
- nenhuma linha estadual ou federal foi promovida para `curated`;
- não existe ainda total anual validado de recursos que entraram em São Borja.

## Estimativas

Não há estimativa financeira adotada como resultado.

O volume descompactado dos lotes históricos permanece desconhecido. A razão de
expansão observada em maio de 2026 indica que pode ser muitas vezes superior ao
volume dos ZIPs, mas não deve ser aplicada automaticamente aos anos antigos.

## Interpretações

- despesa estadual territorializada representa gasto associado ao município,
  não necessariamente transferência, pagamento ou receita municipal;
- liquidação não comprova pagamento;
- valor celebrado, concedido, liberado, liquidado e pago são estágios
  financeiros distintos;
- benefícios a residentes não são repasses à Prefeitura;
- ocorrência nominal de São Borja não comprova impacto econômico local;
- as famílias `TRANSFER`, `CITIZEN_BENEFIT`, `AGREEMENT` e
  `DIRECT_EXPENDITURE_OR_PROGRAM` devem permanecer separadas;
- a existência de arquivos desde 2012 não produz, por si só, uma série
  temporal comparável.

## O que pode ser concluído

- os recursos estaduais mensais foram dimensionados sem baixar todos os corpos;
- janeiro–abril de 2026 possuem raw, staging, auditoria, hashes e cópia no
  Drive;
- maio de 2026 possui raw e auditoria preservados, mas requer reprocessamento
  textual;
- convênios, parcerias e despesas estaduais não foram combinados;
- a base ambígua de convênios permanece bloqueada;
- as fontes federais foram identificadas, mas os dados federais novos ainda
  não foram baixados;
- arquivos históricos não foram substituídos ou removidos.

## O que não pode ser concluído

- o total anual recebido pelo município;
- o total anual aplicado no território por todas as esferas;
- a cobertura estadual de 1996–2002;
- a cobertura federal efetiva entre 1996 e 2026;
- que linhas irregulares não contenham outras ocorrências de São Borja;
- que os oito metadados estaduais divergentes possuam conteúdo incorreto;
- que bases federais existentes e futuras sejam complementares ou duplicadas;
- que valores de fases financeiras diferentes possam ser somados.

## Artefatos de retomada

Inventário estadual final:

```text
.data/audit/base_territorial/state_rs_expense_head_inventory/
  state-rs-expense-head-inventory-20260730-002132/
```

Lote estadual final:

```text
.data/snapshots/web/state_rs_expense_monthly/
  state-rs-expense-2026-01-04-20260730-003514/
.data/staging/base_territorial/state_rs_expense_monthly/
  state-rs-expense-2026-01-04-20260730-003514/
.data/audit/base_territorial/state_rs_expense_monthly/
  state-rs-expense-2026-01-04-20260730-003514/
```

Drive do piloto estadual:

```text
https://drive.google.com/drive/folders/10eUtyJIGWJkzitvpJKLJ1keThUm0yc88
```

Drive do lote janeiro–abril:

```text
https://drive.google.com/drive/folders/1RoOhiAJwMyw9y3GrnYNeCMOzqGj9mI4g
```

## Validações executadas

- inventário real com 173 respostas `HEAD`;
- pipeline real de janeiro–abril executado;
- tamanhos, períodos, membros ZIP, hashes e saídas examinados;
- comparação entre execução UTF-8 e execução `cp1252`;
- cinco testes focais dos dois módulos;
- `make verify` com 251 testes e Ruff;
- CI do PR #36 aprovado antes da inclusão deste documento; o CI deve ser
  novamente aprovado após seu commit.

## Operações externas

- duas execuções do inventário `HEAD`, totalizando 346 requisições `HEAD`;
- dois downloads completos bem-sucedidos do lote de 51.899.110 bytes para
  comparação metodológica;
- uma tentativa intermediária encerrada por timeout antes do primeiro arquivo;
- uploads finais realizados somente em `new_files`;
- commit e push do PR #36;
- nenhuma publicação no Supabase.

## Pendências estaduais

Na retomada:

1. confirmar que o PR #36 foi incorporado e atualizar a `main`;
2. reprocessar maio de 2026 com `cp1252` pelo pipeline mensal;
3. publicar uma execução consolidada janeiro–maio sem sobrescrever stagings;
4. definir regra que separe liquidação de pagamento antes de qualquer total;
5. gerar plano determinístico de lotes de até 60 MB para os 168 arquivos de
   2012–2025;
6. começar com lotes sentinela de anos distintos para detectar mudanças de
   esquema antes do download integral;
7. validar internamente os oito recursos com divergência nome/período;
8. manter linhas malformadas em quarentena sem realinhamento heurístico;
9. reconciliar produtos novos com convênios, parcerias e dados fiscais já
   existentes;
10. somente depois promover produtos documentados para `curated`.

Downloads históricos estaduais continuam sendo operações de grande volume e
exigem nova autorização por lote.

## Pendências federais

Na retomada:

1. inventariar o catálogo `download-de-dados`, sem baixar bases extensas;
2. identificar arquivos, partições, períodos, tamanhos e documentação para:
   transferências, benefícios, convênios e gastos/programas;
3. verificar quais produtos permitem filtro municipal oficial pelo código
   `4318002`;
4. preferir download público sem chave; usar a API somente se necessário e
   com credencial configurada fora do repositório;
5. planejar lotes com limites explícitos antes de qualquer download;
6. preservar raw, URLs, datas, hashes e manifestos no Drive `new_files`;
7. persistir benefícios somente de forma agregada, sem CPF ou nome;
8. manter estágios financeiros e famílias separados;
9. reconciliar com bases federais locais existentes, classificando
   duplicidade, sobreposição e conflitos;
10. não calcular total anual consolidado enquanto diferenças conceituais e de
    cobertura permanecerem.

Qualquer acesso novo ao Portal, uso de API, download, escrita no Drive, commit,
push, PR ou merge posterior exige o escopo e a autorização correspondentes.

## Próxima ação exata

Ao retomar, executar:

```bash
git switch main
git pull --ff-only
git status --short --branch
make verify
```

Depois:

1. verificar o merge e CI do PR #36;
2. iniciar uma tarefa específica para reprocessar maio de 2026 com `cp1252` e
   consolidar janeiro–maio;
3. em paralelo lógico, mas sem download extensivo, inventariar o catálogo
   federal `download-de-dados`;
4. apresentar os dois diagnósticos antes de solicitar os próximos downloads.
