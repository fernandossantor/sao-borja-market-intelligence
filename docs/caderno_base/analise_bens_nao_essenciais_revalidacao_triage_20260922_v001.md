# Bens não essenciais — revalidação cadastral — triagem de anomalias — v001

**Data:** 22/09/2026  
**Geografia:** São Borja/RS  
**Universo de referência:** inventário POM/documental de bens não essenciais  
**Status:** início da revalidação; controle de qualidade, ainda sem nova métrica promovível.

## 1. Universo corrente do inventário

O artefato estrutural anterior contém:

- 120 linhas;
- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes CNPJ;
- 16 linhas sem CNPJ extraível;
- uma duplicidade explícita de CNPJ: Lojas Quero-Quero.

Esses números continuam descrevendo o inventário documental, não oferta ativa corrente.

## 2. Triagem inicial de alto risco

Antes de revalidar os 103 CNPJs em lotes, foram isolados registros em que o próprio inventário já continha sinal de inconsistência cadastral.

### 2.1 Excêntrica — 18.283.007/0001-23

O inventário registra a observação “CNPJ baixado, Instagram atualizado”.

Fonte cadastral secundária consultada em 22/09/2026 informa:

- situação: **BAIXADA**;
- data: **24/05/2022**;
- motivo: extinção por encerramento/liquidação voluntária.

**Classificação provisória:** `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`.

A presença digital não autoriza tratar este CNPJ como ativo. Se a marca continua operando, é necessário identificar eventual novo CNPJ.

### 2.2 Rilu Armarinhos e Presentes — 90.859.091/0001-08

O inventário registra “CNPJ baixado, mas redes sociais ativas com ofertas”.

Fonte cadastral secundária consultada em 22/09/2026 informa:

- situação: **BAIXADA**;
- data: **09/05/2019**;
- motivo: extinção por encerramento/liquidação voluntária.

**Classificação provisória:** `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`.

Novamente, eventual continuidade comercial da marca precisa ser reconciliada com outro CNPJ antes de ser contada como unidade formal ativa.

### 2.3 Lojas Quero-Quero — 96.418.264/0357-81

O mesmo CNPJ aparece em duas linhas do inventário.

Duas fontes cadastrais secundárias correntes apresentam:

- situação: ativa;
- tipo: filial;
- município: São Borja;
- endereço: Rua Coronel Aparício Mariense, 2635.

**Classificação provisória:** `CNPJ_SECUNDARIO_ATIVO_DUPLICIDADE_DE_LINHA_CONFIRMADA`.

Até prova de outra unidade/CNPJ distinto, o denominador deve continuar tratando essas duas linhas como **um único CNPJ/unidade cadastral**.

## 3. Implicação metodológica

A triagem confirma que a revalidação dos 103 CNPJs é necessária antes de chamar o inventário de “oferta ativa”.

Também mostra dois tipos distintos de problema:

1. **CNPJ baixado com possível continuidade da marca** — exige descobrir eventual sucessor cadastral;
2. **duplicidade de linha** — exige deduplicação antes de qualquer contagem.

## 4. O que não pode ser concluído ainda

Ainda não é possível:

- recalcular o número de operadores ativos;
- recalcular a proporção de raízes multiunidade sobre oferta ativa;
- estimar encerramentos do mercado;
- inferir que marcas com CNPJ baixado deixaram de operar;
- promover nova métrica de estrutura concorrencial.

## 5. Fontes

Fontes do inventário:
- `docs/data_sources/bens_nao_essenciais_network_roots_20260920_v001.csv`.

Fontes cadastrais secundárias de triagem:
- CNPJ.biz — Excêntrica e Rilu;
- Econodata e Cirtrox — Lojas Quero-Quero.

Essas fontes são auxiliares e **não substituem a RFB oficial**.

## 6. Artefato

- `docs/data_sources/bens_nao_essenciais_revalidacao_triage_20260922_v001.csv`.

## 7. Próxima etapa

Revalidar os 103 CNPJs únicos em lotes pequenos, registrando para cada CNPJ:

- situação encontrada;
- data/competência da evidência;
- endereço;
- compatibilidade com o operador do inventário;
- fonte;
- natureza institucional/secondary;
- necessidade de reconciliação;
- decisão provisória de manter/excluir/substituir.

Priorizar, nesta ordem:

1. registros com sinal de baixa/inconsistência;
2. grandes redes/filiais;
3. raízes multiunidade;
4. demais CNPJs por subcategoria.

## 8. Status editorial

**CONTROLE DE REVALIDAÇÃO — NÃO GERAR DELTA AINDA.**

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
