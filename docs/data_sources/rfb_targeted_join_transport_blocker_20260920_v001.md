# Join RFB dirigido — operadores de bens essenciais — bloqueio de transporte — v001

**Data:** 20/09/2026  
**Competência RFB alvo:** 2026-08  
**Workflow:** `bens-essenciais-operadores-rfb-join`  
**Run ID:** `34909510407`  
**Status:** bloqueado por transporte da fonte oficial; nenhuma saída analítica produzida.

## 1. Objetivo do workflow

Cruzar os CNPJs documentais dos operadores de bens essenciais com os arquivos oficiais da Receita Federal para recuperar, sem heurística de `/0001`:

- situação cadastral;
- identificador oficial matriz/filial;
- município da unidade;
- município da matriz;
- classificação territorial.

A rotina usa os arquivos oficiais:

- `Municipios.zip`;
- `Estabelecimentos0.zip` a `Estabelecimentos9.zip`.

## 2. Primeira execução

A execução original falhou na etapa de download/varredura dos arquivos oficiais.

O problema identificado foi de transporte na rota pública DAV/Nextcloud da RFB.

Nenhuma matriz final do join foi gerada.

## 3. Reexecução em 20/09/2026

Apenas os jobs falhos do run foram reexecutados.

Novo job:

- job ID `106152699544`;
- conclusão: **failure**;
- etapas de checkout, Python, instalação e preparação dos CNPJs: sucesso;
- etapa `Download municipalities and scan official establishment files sequentially`: falha;
- etapas de construção da matriz e upload: não executadas.

## 4. Erro observado

O download de `Municipios.zip` não chegou a iniciar transferência de bytes.

O `curl` executou oito retentativas com:

`Recv failure: Connection reset by peer`

e encerrou com:

`Process completed with exit code 56`.

Portanto, a falha ocorre antes da leitura dos estabelecimentos e não é evidência de:

- CNPJ ausente na RFB;
- situação cadastral irregular;
- erro no parser;
- inconsistência nos 52 CNPJs documentais;
- inexistência de matriz.

## 5. Decisão operacional

**NÃO repetir imediatamente a mesma execução no mesmo runner/rota.**

A repetição já demonstrou o mesmo bloqueio de transporte.

Reabrir por uma destas rotas:

1. ambiente/rede diferente com acesso ao host oficial;
2. transporte previamente baixado dos mesmos arquivos oficiais, preservando SHA-256;
3. nova rota oficial da RFB, se publicada;
4. execução do pipeline completo quando os bytes oficiais estiverem disponíveis.

## 6. Estado analítico enquanto o join não fecha

Para bens essenciais, permanecem válidos:

- 54 operadores/linhas;
- 52 CNPJs documentais validados;
- 50 raízes CNPJ únicas;
- 2 raízes multiunidade;
- 7,69% das unidades documentadas em raízes multiunidade.

Ainda não promover, para os cinco CNPJs resolvidos documentalmente em 09/09/2026, afirmações novas sobre:

- situação cadastral RFB 2026-08;
- matriz/filial;
- município oficial da matriz;
- classe territorial.

## 7. Governança

- bloqueio de transporte ≠ ausência de dado;
- não substituir RFB oficial por agregador secundário para concluir o join;
- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch de análise: `explore/receita-estadual-rs-market-intel-v1`.
