# Farmácias/drogarias — revalidação de atividade — batch 02 — v001

**Data:** 22/09/2026  
**Geografia:** São Borja/RS  
**Objeto:** segundo bloco de 5 CNPJs do recorte de 20 farmácias/drogarias do inventário POM  
**Status:** controle de atividade; validação cadastral oficial RFB ainda pendente.

## 1. CNPJs auditados

- 88.212.113/0241-14 — São João Farmácias — Av. Presidente Vargas, 1883;
- 88.212.113/1200-08 — São João Farmácias — Rua Cândido Falcão, 1125;
- 88.212.113/0124-50 — São João Farmácias — Rua Vereador Euríco Batista da Silva, 1015;
- 93.641.710/0033-69 — MB Farmácias — Avenida Francisco Miranda, 947;
- 93.641.710/0031-05 — MB Farmácias — Rua General Marques, 1050.

## 2. Resultados

### 2.1 São João — 88.212.113/0241-14

Econodata, atualizada em setembro/2026, informa situação cadastral **Ativa**, condição de filial e endereço em São Borja coincidente com o inventário.

**Classificação provisória:** `ATIVA_APENAS_EM_FONTE_CADASTRAL_SECUNDARIA`.

Não foi localizada, neste batch, evidência institucional recente suficientemente específica para o estabelecimento.

### 2.2 São João — 88.212.113/1200-08

O Guia de Boas-Vindas da Unipampa 2025 lista “Farmácia São João 24h” na Rua Cândido Falcão, 1125, mesmo endereço do inventário.

Econodata, atualizada em setembro/2026, informa situação **Ativa**, filial, no mesmo endereço.

**Classificação provisória:** `ATIVIDADE_PLAUSIVEL_COM_EVIDENCIA_RECENTE`.

O guia institucional não identifica o CNPJ; portanto a ligação CNPJ↔situação cadastral corrente permanece dependente de fonte secundária até reprodução RFB.

### 2.3 São João — 88.212.113/0124-50

SintegraBrasil, consultado em setembro/2026, lista a filial 88.212.113/0124-50 em São Borja como **Ativa**.

**Classificação provisória:** `ATIVA_APENAS_EM_FONTE_CADASTRAL_SECUNDARIA`.

A página consultada agrega dados cadastrais e não substitui o registro oficial RFB reproduzido pelo projeto.

### 2.4 MB Farmácias — 93.641.710/0033-69

O Guia de Boas-Vindas da Unipampa 2025 lista “MB Farmácia — Filial 31” na Avenida Francisco Miranda, 947, mesmo endereço do inventário.

GuiaPJ informa dados cadastrais atribuídos à Receita Federal com referência agosto/2026, situação **Ativa**, filial, CNPJ 93.641.710/0033-69 no mesmo endereço.

**Classificação provisória:** `ATIVIDADE_PLAUSIVEL_COM_EVIDENCIA_RECENTE`.

Apesar de a fonte secundária declarar origem RFB e competência agosto/2026, ela continua sendo uma camada intermediária. O projeto ainda não reproduziu diretamente o registro oficial.

### 2.5 MB Farmácias — 93.641.710/0031-05

Econodata, atualizada em agosto/2026, informa situação **Ativa**, filial, Rua General Marques, 1050, São Borja.

**Classificação provisória:** `ATIVA_APENAS_EM_FONTE_CADASTRAL_SECUNDARIA`.

## 3. Síntese do batch 02

Dos 5 CNPJs:

- 2 possuem evidência operacional institucional recente associada ao mesmo endereço;
- 5 aparecem como ativos em fontes cadastrais secundárias correntes;
- 0 possuem validação oficial RFB diretamente reproduzida pelo projeto.

## 4. Acumulado dos batches 01 + 02

Cobertura auditada até aqui:

- 10 de 20 CNPJs únicos = **50%** do recorte de farmácias/drogarias;
- 5 dos 10 possuem evidência institucional/regulatória recente no mesmo estabelecimento/endereço;
- 10 dos 10 aparecem ativos em fontes cadastrais secundárias correntes;
- 0 de 10 possuem validação oficial RFB diretamente reproduzida.

**Interpretação permitida:** os dez primeiros registros não apresentaram sinal de encerramento nas fontes consultadas e todos possuem evidência cadastral secundária corrente de atividade.

**Interpretação proibida:** “100% das farmácias estão oficialmente ativas na RFB”. O gate oficial continua aberto.

## 5. Efeito sobre a estrutura de rede

Nenhum CNPJ foi excluído neste estágio. Assim, **não recalcular ainda**:

- 20 CNPJs únicos;
- 7 raízes;
- 17/20 unidades em raízes multi = 85%;
- maior raiz = 7 unidades = 35%.

Essas métricas permanecem como estrutura do inventário até a conclusão da revalidação dos 20 CNPJs.

## 6. Próximo batch

Prosseguir com:

- 93.641.710/0010-72;
- 93.641.710/0038-73;
- 93.641.710/0041-79;
- 93.641.710/0064-65;
- 92.665.611/0059-93.

## 7. Artefato estruturado

- `docs/data_sources/farmacias_revalidacao_batch02_20260922_v001.csv`.

## 8. Status editorial

**CONTROLE / READINESS. NÃO CRIAR DELTA AINDA.**

Cobertura de 50% ainda não autoriza fechar a situação ativa do universo de 20 unidades nem promover métrica recalculada.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
