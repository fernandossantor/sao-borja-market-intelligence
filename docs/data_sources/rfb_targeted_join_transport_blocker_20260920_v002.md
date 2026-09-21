# Join RFB dirigido — operadores de bens essenciais — bloqueio de transporte — v002

**Data de controle:** 20/09/2026  
**Competência RFB alvo:** 2026-08  
**Geografia analítica:** São Borja/RS  
**Workflow:** `bens-essenciais-operadores-rfb-join`  
**Status:** bloqueado no transporte da fonte oficial em runner hospedado pelo GitHub; nenhuma saída cadastral analítica produzida.

## 1. Objeto

Validar os 52 CNPJs documentalmente reconciliados do inventário corrente de bens essenciais contra os arquivos oficiais da Receita Federal, recuperando por CNPJ completo situação cadastral, identificador matriz/filial, município do estabelecimento, estabelecimento matriz da mesma raiz, município da matriz e classificação territorial.

O método planejado não usa o sufixo `/0001` como heurística de matriz.

## 2. Dados observados — tentativas

O bloqueio anterior já havia sido reproduzido no run `34909510407` e na reexecução do job `106152699544`: o primeiro arquivo, `Municipios.zip`, permaneceu em zero bytes e o transporte terminou com `curl: (56) Recv failure: Connection reset by peer`.

### Run 35547624975

Commit: `bb38ff98566bd9df336d5090ab343c0289eec368`.

Foi testada uma rota estática no domínio oficial. Checkout, instalação e preparação dos 52 alvos concluíram com sucesso, mas `Municipios.zip` permaneceu em zero bytes após oito retentativas. O join e o upload não foram executados.

### Run 35547812277

Commit: `985b91c44768465c17286f776c5b4730deb6ddad`.

Foi testada a raiz DAV do compartilhamento público corrente. As etapas locais concluíram com sucesso, mas o primeiro arquivo novamente permaneceu em zero bytes e encerrou com o mesmo erro de transporte.

### Run 35547962441

Commit: `ebe262c9f4828f3fc03bcabef58d6113c77fe318`.

Foi testada a variante WebDAV do compartilhamento público com autenticação própria de compartilhamento público e cabeçalho de requisição apropriado. Checkout, Python, instalação e preparação do scanner concluíram com sucesso. O download de `Municipios.zip` permaneceu em zero bytes, houve oito retentativas e o processo terminou com `curl: (56) Recv failure: Connection reset by peer`. Construção da matriz e upload foram pulados.

## 3. Interpretação técnica

As variantes alteraram o modo de endereçamento e, no último teste, também o modo de acesso ao compartilhamento. Todas falharam antes da recepção do primeiro byte do primeiro arquivo.

**Interpretação:** a evidência acumulada é compatível com bloqueio de transporte/conectividade entre o runner hospedado pelo GitHub e o host de arquivos da RFB, e não com falha do parser ou ausência dos CNPJs pesquisados.

Essa interpretação é operacional e não prova indisponibilidade universal da fonte em outras redes ou ambientes.

## 4. O que não pode ser concluído

As falhas não autorizam concluir que:

- qualquer dos 52 CNPJs esteja ausente da base RFB 2026-08;
- algum estabelecimento esteja baixado ou irregular;
- os cinco CNPJs reconciliados em 09/09 estejam incorretos;
- uma raiz tenha matriz local ou externa;
- os arquivos oficiais estejam indisponíveis para outros clientes ou redes.

## 5. Decisão

**Não repetir, neste momento, a mesma estratégia em runner hospedado pelo GitHub.**

Rotas admissíveis: executar o scanner em rede/ambiente diferente; usar os mesmos arquivos oficiais previamente adquiridos com origem e SHA-256 preservados; ou retomar por nova rota oficial após teste de transporte fora do workflow analítico.

O join linha a linha permanece aberto e não deve ser substituído por agregadores secundários para classificar situação cadastral ou matriz.

## 6. Estado analítico preservado

Continuam válidos apenas como estrutura do inventário documental:

- 54 operadores/linhas;
- 52 CNPJs documentais validados;
- 52 CNPJs únicos;
- 50 raízes;
- 2 raízes multiunidade;
- 4 unidades em raízes multi;
- 7,69% das unidades documentadas em raízes multi.

Bedi Padaria e Confeitaria e Sabor mineiro da Lu Delícias caseiras permanecem fora do denominador por falta de CNPJ documental suficientemente confiável.

## 7. Pendências específicas

Os cinco registros corrigidos/identificados documentalmente em 09/09/2026 continuam aguardando confirmação oficial RFB 2026-08 de situação e território:

- Supermercado Baklizi — 00.610.350/0017-37;
- Supermercado Nicolini — 89.835.672/0036-50;
- Mercado Precioso — 55.330.974/0001-25;
- Mercado Santa Lúcia — 07.934.366/0001-87;
- Minimercado D'Gringa — 51.634.027/0001-77.

## 8. Readiness editorial

**Controle técnico, não novo delta.**

O bloqueio não modifica a leitura de pulverização por raiz já promovida e não acrescenta evidência territorial sobre matriz/filial. Portanto, não gera nova linha em `Delta_cadernos`.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- não criar sucessora da v028 por este controle.
