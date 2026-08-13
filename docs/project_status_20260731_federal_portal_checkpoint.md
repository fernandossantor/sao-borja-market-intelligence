# Checkpoint — Portal da Transparência federal — 2026-07-31

## Escopo

Checkpoint da retomada da captura de dados federais para São Borja/RS
(código IBGE `4318002`). O checkpoint preserva descobertas, capturas locais,
limitações de acesso e a próxima ação. Nenhum produto foi promovido para
`curated`.

## Evidências observadas

- O cliente autenticado mínimo da API está em `src/sbmi/transparencia_api.py`.
- A chave `TRANSPARENCIA_API_KEY` está configurada fora do repositório.
- A rota `convenios` aceitou o filtro `codigoIBGE=4318002` em uma execução e
  retornou 15 registros por página.
- A captura local `federal-api-convenios-sao-borja-20260731-001` preserva as
  páginas 1–3, com 45 registros e 45 IDs únicos.
- Todos os 45 registros da captura possuem `municipioConvenente.codigoIBGE`
  igual a `4318002`.
- As páginas 4 e 5 também retornaram registros em uma validação posterior;
  portanto, a execução 001 não representa a consulta completa.
- As execuções 002 e 003 registraram timeout antes da primeira página e não
  possuem registros.
- O catálogo oficial informa que convênios têm atualização semanal e geram
  `Convenios` e `Convenios_OrdensBancarias`; transferências são mensais e
  recebimento de recursos por favorecido é diário.
- A página oficial de dados abertos e os panoramas anuais foram localizados:
  `https://portaldatransparencia.gov.br/download-de-dados` e
  `https://portaldatransparencia.gov.br/localidades/4318002-sao-borja`.
- Busca indexada das páginas oficiais exibiu, para 2021, transferências apenas
  ao município de `R$ 91.751.678,97` e benefícios de `R$ 59.680.348,75`.
- Busca indexada das páginas oficiais exibiu, para 2022, transferências apenas
  ao município de `R$ 110.946.125,67` e benefícios de `R$ 53.889.525,76`.

## Resultados calculados

- Diferença nominal das transferências municipais entre 2021 e 2022:
  `R$ 19.194.446,70`.
- Variação nominal calculada: aproximadamente `20,9%`.
- Esses cálculos não foram promovidos a produto, pois os panoramas anuais não
  puderam ser baixados diretamente nesta execução.

## Estimativas

Nenhuma estimativa financeira foi adotada.

## Interpretações e limitações

- Convênio, transferência, benefício e gasto direto são famílias distintas e
  não podem ser somados sem reconciliação conceitual.
- Os valores anuais de 2021 e 2022 são evidências observadas em páginas
  oficiais indexadas, mas ainda não constituem captura bruta local validada.
- A API apresentou timeouts intermitentes, enquanto as páginas do Portal
  apresentaram verificação humana/AWS WAF.
- Não foi possível obter competências, tamanhos e URLs finais do catálogo
  dinâmico.
- Não há série federal consolidada para 1996–2026.

## Artefatos preservados

```text
.data/snapshots/web/federal_api/convenios-sao-borja-20260731-001/
.data/snapshots/web/federal_api/convenios-sao-borja-20260731-002/
.data/snapshots/web/federal_api/convenios-sao-borja-20260731-003/
```

Os artefatos estão sob `.data/`, ignorado pelo Git. A execução 001 contém os
45 registros; 002 e 003 são tentativas com erro e zero registros.

## Validação executada

- `make verify`: 256 testes aprovados e Ruff aprovado.
- Manifestos, contagens, IDs, códigos municipais e ausência de arquivos
  parciais foram examinados.
- Nenhum arquivo histórico foi alterado.

## Operações externas

- Consultas de baixo volume à API oficial do Portal da Transparência.
- Consulta ao OpenAPI oficial e ao catálogo público.
- Busca de páginas oficiais indexadas para 2021, 2022 e convênios individuais.
- Nenhuma escrita no Google Drive.

## Estado de Git e retomada

- Branch: `feature/new-files-temporal-coverage`.
- HEAD local observado: `b3b4f76`.
- Branch limpa; nenhum commit, push ou PR foi criado nesta retomada.
- O commit de merge citado no checkpoint anterior (`a2896db`) não está
  presente no histórico local observado.

## Próxima ação recomendada

Retomar por uma sessão manual/interativa autorizada no Portal para obter uma
URL direta de download ou exportação dos panoramas anuais e do catálogo de
convênios. Criar nova execução própria, sem sobrescrever as anteriores, e
validar primeiro um lote pequeno antes de qualquer download extensivo ou
publicação externa.
