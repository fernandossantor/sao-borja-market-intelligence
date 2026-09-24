# Revalidação de CNPJs — bens não essenciais — lote 03 — redes e reconciliações — 23/09/2026

## 1. Governança

Continuação da revalidação dos 103 CNPJs únicos do inventário de bens não essenciais.

Mantidos:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhuma atualização de oferta ativa, concentração, número final de operadores ou proporção multiunidade.

## 2. Escopo

O lote aborda cinco CNPJs do universo original:

- Lins Ferrão — `87.345.021/0122-14`;
- Lojas Três Passos — `98.102.650/0023-58`;
- RM2S — `58.434.608/0010-03`;
- Lojas P & S — `90.072.059/0009-35`;
- Brasil Free Shop — `32.195.385/0006-90`.

Também foram registrados quatro CNPJs que não integravam os 103 originais:

- Lins Ferrão — `87.345.021/0033-04`;
- RM2S — `58.434.608/0015-00`;
- Brasil Free Shop — `32.195.385/0011-58`;
- Monaco Freeshop / Brasil Free Shop — `32.195.385/0012-39`, que preenche a linha 177 antes sem CNPJ.

Com os cinco CNPJs originais auditados neste lote, a cobertura do universo original chega a **22/103 = 21,36%**. Trata-se apenas de cobertura da auditoria.

## 3. Lins Ferrão — Pompéia/Gang

### 3.1 CNPJ 87.345.021/0122-14

O CNPJ do inventário está ativo e vinculado à Rua Cândido Falcão, 1057.

O problema é a **marca**: o inventário o associa a “Lojas Pompéia”, enquanto diretórios operacionais atuais associam **Gang** ao mesmo endereço. O antigo CNPJ da Gang Comércio do Vestuário no ponto, `88.712.955/0059-39`, aparece baixado.

Isso cria uma hipótese plausível de migração jurídica da operação Gang para outro CNPJ da raiz Lins Ferrão, mas a associação exata **não foi comprovada por fonte de primeira parte**.

**Decisão:** manter `87.345.021/0122-14` como CNPJ ativo da raiz, retirar provisoriamente a certeza de que ele representa Pompéia e registrar a marca corrente como pendente de reconciliação.

### 3.2 CNPJ 87.345.021/0033-04

Foi localizado outro CNPJ ativo da mesma raiz em São Borja, na Rua General Marques, 1196.

Diretórios atuais associam **Lojas Pompéia** exatamente a esse endereço.

**Interpretação:** `87.345.021/0033-04` é candidato forte a CNPJ correto da operação Pompéia que o inventário pretendia representar.

**Decisão:** adicionar ao controle e tratar como candidato à correção da linha 103, sem promoção canônica antes de vínculo marca↔CNPJ de primeira parte ou confirmação equivalente.

## 4. Monjuá / Lojas Três Passos

CNPJ `98.102.650/0023-58`.

A revalidação mostra:

- situação ativa;
- endereço Rua General Marques, 1076;
- fantasia cadastral **Tecidos Três Passos**;
- a marca Monjuá mantém presença operacional atual em São Borja, inclusive com recrutamento recente para gerente de loja;
- diretórios situam Monjuá no mesmo endereço.

**Interpretação:** não se trata de CNPJ necessariamente incorreto, mas de diferença entre **marca operacional** e **fantasia cadastral formal**.

**Decisão:** manter o CNPJ e, no sucessor, separar explicitamente os campos “marca operacional: Monjuá” e “fantasia cadastral: Tecidos Três Passos”.

## 5. RM2S / MAXX Outlet

### 5.1 CNPJ do inventário — 58.434.608/0010-03

O CNPJ está ativo, foi aberto em 21/01/2026 e está em Rua General Osório, 2251.

A associação com a marca MAXX Outlet não foi revalidada externamente nesta rodada.

**Decisão:** manter o CNPJ, mas preservar a marca com flag de confirmação pendente.

### 5.2 CNPJ adicional — 58.434.608/0015-00

Foi identificado um segundo CNPJ ativo da mesma raiz em São Borja:

- abertura: 19/06/2026;
- endereço: Rua General Marques, 1112.

A marca operacional correspondente não foi identificada.

**Interpretação:** a raiz RM2S está subcoberta no inventário.

**Decisão:** adicionar ao controle, sem presumir que se trate de uma segunda MAXX Outlet.

## 6. Lojas P & S

CNPJ `90.072.059/0009-35`.

Fonte cadastral atualizada em agosto/2026 apresenta:

- situação ativa;
- filial;
- Rua Cândido Falcão, 1155, loja 101;
- fantasia Lojas P & S.

**Decisão:** manter provisoriamente. A confirmação oficial RFB direta permanece pendente.

## 7. Brasil Free Shop / Monaco — evidência oficial forte

A lista oficial da Receita Estadual do Rio Grande do Sul para **Lojas Francas de Fronteira Terrestre** apresenta três CNPJs da raiz `32.195.385` em São Borja:

- `32.195.385/0006-90`;
- `32.195.385/0011-58`;
- `32.195.385/0012-39`.

Essa evidência tem natureza diferente das fontes cadastrais secundárias: é uma lista oficial estadual de estabelecimentos de loja franca.

### 7.1 32.195.385/0006-90

Já estava no inventário. Fontes cadastrais recentes o apresentam ativo na Rua Coronel Aparício Mariense da Silva, 2918.

**Decisão:** manter.

### 7.2 32.195.385/0011-58

Não estava no inventário.

- ativo em fonte cadastral recente;
- abertura em 09/06/2025;
- Rua Vereador Eurico Batista da Silva, 925, Paraboi;
- consta na lista oficial estadual de lojas francas de São Borja.

**Decisão:** adicionar ao controle como candidato forte à incorporação no sucessor.

### 7.3 32.195.385/0012-39 — Monaco Freeshop

A linha 177 do inventário registrava Monaco Freeshop sem CNPJ.

A revalidação identificou:

- CNPJ `32.195.385/0012-39`;
- fantasia cadastral Monaco Freeshop;
- situação ativa em fonte cadastral recente;
- Rua General Marques, 541, Anexo B;
- presença na lista oficial estadual de lojas francas de São Borja.

**Decisão:** preencher o CNPJ da linha Monaco no sucessor, preservando a trilha de que a identificação ocorreu nesta revalidação.

## 8. Resultados metodológicos

### Dados observados

- cinco CNPJs do universo original foram revalidados;
- quatro CNPJs adicionais foram identificados;
- Monaco passou de linha sem CNPJ para linha com CNPJ identificado;
- Lins Ferrão apresentou provável erro de associação entre marca e CNPJ no inventário;
- Monjuá apresentou diferença entre marca operacional e fantasia cadastral;
- as raízes Lins Ferrão, RM2S e Brasil Free Shop estão subcobertas no inventário.

### Dados calculados

Cobertura do universo original:

`22 / 103 × 100 = 21,36%`.

Esse indicador mede somente o avanço da auditoria.

### Interpretações

- raiz CNPJ e quantidade de estabelecimentos cadastrais não devem ser transformadas diretamente em quantidade de lojas físicas;
- a lista oficial de lojas francas é evidência forte de existência/autorização dos três CNPJs Brasil Free Shop no município, mas não mede faturamento, fluxo ou relevância concorrencial;
- mudanças de marca e reorganizações societárias exigem camada temporal de reconciliação.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_revalidacao_lote03_redes_reconciliacoes_20260923_v001.csv`

## 10. Próxima ação imediata

Registrar uma **corrigenda do lote 01** para a Lojas Quero-Quero: durante a expansão da pesquisa foi localizado um terceiro CNPJ ativo da raiz em São Borja, `96.418.264/0533-30`, em Rua Homero Pereira Coimbra, 54. A descoberta não invalida os dois CNPJs documentados no lote 01, mas mostra que aquele lote ficou incompleto quanto à raiz.

Depois da corrigenda, seguir a revalidação por subcategoria, sem recalcular ainda os indicadores estruturais.
