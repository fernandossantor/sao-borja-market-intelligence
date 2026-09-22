# Farmácias/drogarias — revalidação de atividade — batch 01 — v001

**Data:** 22/09/2026  
**Geografia:** São Borja/RS  
**Objeto:** primeiro bloco de 5 CNPJs do recorte de 20 farmácias/drogarias do inventário POM  
**Status:** controle de atividade; validação cadastral oficial RFB ainda pendente.

## 1. Objetivo

Revalidar, em blocos pequenos e auditáveis, se os CNPJs do inventário de farmácias/drogarias permanecem associados a unidades com sinais recentes de operação em São Borja.

A investigação separa três camadas:

1. **evidência institucional/regulatória recente** — fonte pública ou institucional que confirme a presença operacional da unidade;
2. **evidência cadastral secundária corrente** — agregadores que reproduzem situação cadastral atribuída à Receita Federal;
3. **situação RFB oficial** — permanece PENDENTE enquanto o projeto não obtiver os bytes/consulta oficial reproduzível.

Não converter a camada 2 em “validação RFB”.

## 2. Universo deste batch

Cinco CNPJs:

- 20.507.692/0001-76 — Farmácia Maria do Carmo;
- 88.212.113/0049-46 — São João Farmácias — General Osório, 2179;
- 88.212.113/0387-60 — São João Farmácias — Francisco Miranda, 944;
- 88.212.113/0598-48 — São João Farmácias — General Marques, 440;
- 88.212.113/0247-00 — São João Farmácias — General Marques, 1226.

## 3. Resultados observados

### 3.1 Farmácia Maria do Carmo — 20.507.692/0001-76

**Evidência institucional:** o Guia de Boas-Vindas da Unipampa 2025 lista “Farmácia Maria do Carmo”, Rua General Marques, 728, com o mesmo telefone do inventário.

**Evidência cadastral secundária:** consulta pública ao CNPJ.biz em 2026 informa situação “Ativa”, matriz, no mesmo endereço.

**Classificação provisória:** `ATIVIDADE_PLAUSIVEL_COM_EVIDENCIA_RECENTE`.

**Limite:** o guia institucional não traz o CNPJ. A situação cadastral corrente ainda não foi reproduzida diretamente na RFB.

### 3.2 São João — 88.212.113/0049-46

**Evidência regulatória oficial:** Diário Oficial do Município de São Borja publicado em 29/09/2025 registra decisão sanitária para Comércio de Medicamentos Brair Ltda, CNPJ 88.212.113/0049-46, Rua General Osório, 2179. A autuação ocorreu em 11/09/2024 e a decisão em 06/12/2024.

**Evidência cadastral secundária:** Adv Dinâmico, consultado em 2026, informa situação “Ativa”, filial, no mesmo endereço.

**Classificação provisória:** `ATIVIDADE_PLAUSIVEL_COM_EVIDENCIA_REGULATORIA_RECENTE`.

**Limite:** o ato municipal prova atividade no período do processo, não a situação cadastral RFB em setembro/2026.

### 3.3 São João — 88.212.113/0387-60

**Evidência institucional:** o Guia de Boas-Vindas da Unipampa 2025 lista Farmácia São João na Rua Francisco Miranda, 944, mesmo endereço do inventário.

**Evidência cadastral secundária:** RaizLegal e CNPJCheck, consultados em 2026, informam CNPJ ativo, filial, no mesmo endereço.

**Classificação provisória:** `ATIVIDADE_PLAUSIVEL_COM_EVIDENCIA_RECENTE`.

**Limite:** a fonte institucional confirma a unidade/endereço, não o CNPJ. RFB oficial segue pendente.

### 3.4 São João — 88.212.113/0598-48

**Evidência cadastral secundária:** Econodata, atualizada em setembro/2026, informa situação “Ativa”, filial, Rua General Marques, 440.

Foi localizada evidência sanitária municipal histórica de 2018 para o mesmo CNPJ/endereço, mas ela é insuficiente para classificar atividade corrente.

**Classificação provisória:** `ATIVA_APENAS_EM_FONTE_CADASTRAL_SECUNDARIA`.

### 3.5 São João — 88.212.113/0247-00

**Evidência cadastral secundária:** Econodata, atualizada em setembro/2026, informa situação “Ativa”, filial, Rua General Marques, 1226.

A evidência oficial localizada no projeto para esse CNPJ é antiga e não sustenta, isoladamente, atividade corrente.

**Classificação provisória:** `ATIVA_APENAS_EM_FONTE_CADASTRAL_SECUNDARIA`.

## 4. Síntese do batch

Dos 5 CNPJs:

- 3 possuem **evidência institucional/regulatória relativamente recente** associada ao mesmo estabelecimento/endereço;
- 5 aparecem como **ativos em fontes cadastrais secundárias correntes**;
- 0 possuem, nesta etapa, **validação cadastral oficial RFB reproduzida diretamente pelo projeto**.

Portanto, **não promover “5/5 ativos na RFB”**.

A leitura permitida é mais restrita: o primeiro batch não produziu evidência de encerramento dessas unidades e apresentou sinais recentes de operação/cadastro, porém o gate de situação cadastral oficial permanece aberto.

## 5. Implicação para a métrica de rede

A estrutura já calculada para farmácias/drogarias continua sendo:

- 20 CNPJs únicos;
- 7 raízes;
- 17/20 unidades em raízes multi = 85%;
- maior raiz: 7 unidades = 35%.

**Este batch não altera ainda o denominador 20.**

Ele apenas inicia a revalidação da atividade. Qualquer CNPJ que futuramente seja confirmado como baixado exigirá recalcular o recorte ativo e todas as métricas derivadas.

## 6. Fontes

Institucionais/oficiais:

- Unipampa — Guia de Boas-Vindas a São Borja 2025;
- Prefeitura de São Borja — Diário Oficial, 29/09/2025, decisão sanitária do CNPJ 88.212.113/0049-46.

Secundárias de controle:

- CNPJ.biz;
- Adv Dinâmico;
- RaizLegal;
- CNPJCheck;
- Econodata.

As fontes secundárias são usadas somente como **sinal cadastral provisório** e não substituem o dado oficial da Receita Federal.

## 7. Próximo batch

Prosseguir com os cinco CNPJs seguintes do recorte:

- 88.212.113/0241-14;
- 88.212.113/1200-08;
- 88.212.113/0124-50;
- 93.641.710/0033-69;
- 93.641.710/0031-05.

## 8. Artefato estruturado

- `docs/data_sources/farmacias_revalidacao_batch01_20260922_v001.csv`.

## 9. Status editorial

**CONTROLE / READINESS. NÃO CRIAR NOVO DELTA AINDA.**

Promover somente quando a revalidação atingir cobertura suficiente do universo de 20 CNPJs, com distinção explícita entre atividade observada e situação cadastral oficial.

## 10. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
