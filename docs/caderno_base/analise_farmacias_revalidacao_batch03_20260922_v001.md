# Farmácias/drogarias — revalidação de atividade — batch 03 — v001

**Data:** 22/09/2026  
**Geografia:** São Borja/RS  
**Objeto:** terceiro bloco de 5 CNPJs do recorte de 20 farmácias/drogarias do inventário POM  
**Fonte institucional prioritária:** CNES/DATASUS  
**Status:** revalidação operacional fortalecida; situação cadastral RFB continua separada e pendente.

## 1. Mudança metodológica relevante

Neste batch foi localizada uma rota institucional mais adequada para o objetivo de **revalidar presença operacional**: o Cadastro Nacional de Estabelecimentos de Saúde — CNES/DATASUS.

O CNES permite observar o CNPJ associado ao estabelecimento, código CNES, endereço, tipo de estabelecimento e, em diversos casos, data de atualização e horário informado.

Isso melhora a revalidação de atividade, mas não elimina a distinção metodológica:

- **CNES corrente** = evidência institucional de registro do estabelecimento de saúde;
- **RFB/CNPJ** = situação cadastral empresarial oficial;
- uma camada não deve ser apresentada como se fosse a outra.

## 2. Resultados

### 2.1 MB Farmácias — 93.641.710/0010-72

CNES 0249068.

O CNES registra o CNPJ 93.641.710/0010-72 como **MB Farmácia**, Rua Cândido Falcão, 1187, São Borja, estabelecimento do tipo farmácia, com horários de funcionamento informados.

- última atualização CNES: **23/08/2026**;
- atualização local: 26/05/2026.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026`.

### 2.2 MB Farmácias — 93.641.710/0038-73

CNES 4394232.

A listagem corrente do CNES associa o CNPJ à **MB Farmácias Filial 36**, São Borja.

O cadastro básico corrente localiza a unidade em **Rua Borges do Canto, 468 — Tiro**.

O inventário havia reproduzido o mesmo CNPJ em duas linhas/endereço:

- Borges do Canto, 589;
- Borges do Canto, 468.

**Dado observado:** o registro CNES corrente sustenta o endereço nº 468.

**Decisão:** tratar o nº 589 como endereço histórico/stale no inventário até evidência contrária. Isso não cria uma segunda unidade para o mesmo CNPJ.

**Classificação:** `REGISTRO_CNES_CORRENTE_COM_CORRECAO_ENDERECO`.

### 2.3 MB Farmácias — 93.641.710/0041-79

CNES 4660277.

O CNES registra o estabelecimento na Rua Vereador Eurico Batista da Silva, 890, Paraboi, com horários informados.

- última atualização CNES: **02/08/2026**;
- atualização local: 26/05/2026.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026`.

### 2.4 MB Farmácias — 93.641.710/0064-65

CNES 4028104.

O CNES registra o estabelecimento na Rua Venâncio Aires, 2060, São Borja, com horários informados.

- última atualização CNES: **24/07/2026**;
- atualização local: 26/05/2026.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026`.

### 2.5 Panvel — 92.665.611/0059-93

CNES 2923599.

O CNES registra **Panvel Farmácias Filial 072**, CNPJ 92.665.611/0059-93, Rua General Osório, 2160.

- última atualização CNES: **02/09/2026**;
- atualização local: 06/03/2024;
- horários de funcionamento informados.

**Classificação:** `REGISTRO_CNES_ATUALIZADO_2026`.

## 3. Síntese do batch 03

Dos 5 CNPJs:

- 5 aparecem no CNES/DATASUS corrente;
- 4 possuem página individual com atualização explicitamente registrada em 2026;
- 1 possui listagem/cadastro corrente e resolve uma duplicidade de endereço do inventário;
- 0 foram excluídos do recorte.

Este batch fornece evidência institucional significativamente mais forte para a **presença operacional** do que os agregadores cadastrais utilizados como fallback nos primeiros batches.

## 4. Acumulado dos batches 01–03

Cobertura auditada do inventário:

- 15 de 20 CNPJs = **75%**.

Entretanto, a descoberta da rota CNES exige uma rechecagem transversal dos batches 01 e 02, pois vários daqueles CNPJs também aparecem na listagem institucional corrente do CNES.

Portanto, o consolidado final deve ser calculado somente após o batch 04 e a comparação sistemática dos 20 CNPJs com a listagem CNES.

## 5. Alerta de completude

Durante a leitura da listagem CNES de São Borja surgiram CNPJs de redes já conhecidas que **não pertencem ao recorte de 20 CNPJs únicos** usado na métrica anterior.

Esse sinal deve ser auditado separadamente antes de interpretar 20 como universo ativo das farmácias/drogarias de São Borja.

Não incorporar unidades adicionais ao denominador sem:

1. confirmar CNPJ;
2. confirmar tipo de estabelecimento;
3. confirmar São Borja;
4. verificar se são realmente unidades distintas e não mera atualização/migração cadastral.

## 6. Próximo batch

Restam os 5 CNPJs:

- 92.665.611/0467-54 — Panvel;
- 61.585.865/2878-50 — Droga Raia;
- 94.963.576/0015-01 — Farmácia Fronteira;
- 94.963.576/0013-31 — Farmácia Fronteira;
- 26.710.619/0001-83 — Agafarma.

## 7. Artefato estruturado

- `docs/data_sources/farmacias_revalidacao_batch03_20260922_v001.csv`.

## 8. Status editorial

**CONTROLE / READINESS. NÃO CRIAR DELTA AINDA.**

O batch melhora a revalidação operacional, mas também revelou possível lacuna de completude do inventário. Fechar o universo antes de promover métrica de rede.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
