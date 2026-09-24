# Revalidação de CNPJs — bens não essenciais — lote 14 — papelaria e fechamento da varredura setorial — 23/09/2026

## 1. Escopo e governança

Este lote trata:

- dois CNPJs do universo original: Graffite/Gaffiti Papelaria e Consermaq;
- uma linha originalmente sem CNPJ extraível: Mais Top Papelaria.

Mantêm-se integralmente:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhum recálculo de oferta ativa, número final de operadores, concentração ou proporção multiunidade.

Após os dois CNPJs originais deste lote:

- examinados: **100/103 = 97,09%**;
- com evidência independente de revalidação/reconciliação: **99/103 = 96,12%**.

Mais Top não entra nesses denominadores porque a linha 215 originalmente estava entre as linhas sem CNPJ extraível.

## 2. Graffite/Gaffiti Papelaria — 92.691.104/0001-08

A base CNPJ Go, que declara utilizar os dados abertos da Receita Federal com atualização mensal, lista **Algacir José Bertuol — CNPJ 92.691.104/0001-08** como empresa ativa no CNAE de comércio varejista de artigos de papelaria em São Borja.

A identidade operacional recebe triangulação institucional:

- a Câmara Municipal de São Borja contratou o mesmo CNPJ em junho/2024 para fornecimento de material de consumo e, em julho/2024, manteve credenciamento para serviços reprográficos e encadernações;
- a própria Câmara usa a denominação **Graffite Papelaria**;
- o Portal da Transparência do Sesc-RS registra pagamento de nota fiscal a Algacir José Bertuol, mesmo CNPJ, em 28/10/2025.

**Dado observado:** há evidência cadastral de atividade e evidência institucional recente de operação.

**Reconciliação necessária:** o inventário grafava “Gaffiti Papelaria”, enquanto a fonte institucional municipal usa “Graffite Papelaria”.

**Decisão provisória:** manter o CNPJ, preservar ambas as grafias na trilha de auditoria e confirmar a marca operacional corrente por primeira parte antes de corrigir definitivamente o sucessor.

## 3. Consermaq — 89.271.464/0001-46

Fonte cadastral recente apresenta:

- situação ativa;
- matriz;
- razão social **W. Gomes de Oliveira Ltda**;
- Avenida Presidente Vargas, 1906;
- CNAE principal de papelaria;
- amplo conjunto de CNAEs secundários.

Há documentação oficial e fiscal histórica para o mesmo CNPJ:

- Câmara Municipal de São Borja, em 2024, usa **G. de Oliveira e Cia Ltda — Consermaq**;
- NF-e de 2022 registra **Consermaq / G. de Oliveira e Cia Ltda**, no mesmo CNPJ, mas em endereço anterior.

**Interpretação:** o inventário, ao usar W. Gomes de Oliveira Ltda, está alinhado ao cadastro mais recente; as fontes anteriores revelam mudança ou variação temporal da razão social e do endereço.

**Decisão provisória:** manter o CNPJ e a razão social corrente, preservando “G. de Oliveira e Cia Ltda” como denominação histórica e “Consermaq” como marca operacional histórica/documentada.

## 4. Mais Top Papelaria — 24.495.873/0001-80

A linha 215 do inventário não tinha CNPJ extraível.

A revalidação encontrou:

- CNPJ `24.495.873/0001-80`;
- razão social Juliana Andrade Moreira;
- fantasia Mais Top Papelaria;
- situação ativa;
- matriz;
- abertura em 31/03/2016;
- CNAE principal de comércio varejista de artigos de papelaria;
- endereço cadastral: Rua Coronel Lago, 2328, apto 02, sala 01.

Diretório operacional atual utiliza o mesmo CNPJ e marca, mas apresenta endereço comercial na Avenida Presidente Vargas, 2109, sala A e razão social com uma variação nominal.

**Dado observado:** o CNPJ da linha sem número foi identificado com grau suficiente para entrar na camada de reconciliação.

**Decisão provisória:** preencher `24.495.873/0001-80` na linha 215 do sucessor, preservando separadamente endereço cadastral e endereço operacional até confirmação.

## 5. Resultado metodológico

### Dados observados

- Graffite/Gaffiti e Consermaq possuem CNPJs originais revalidados;
- Mais Top recebeu CNPJ antes ausente;
- Graffite possui evidência de operação institucional em 2024 e pagamento fiscal/institucional em 2025;
- Consermaq apresenta mudança temporal de razão social/endereço;
- Mais Top apresenta divergência entre endereço cadastral e operacional.

### Dados calculados

- CNPJs originais examinados: `100 / 103 × 100 = 97,09%`;
- CNPJs originais com evidência independente: `99 / 103 × 100 = 96,12%`.

### Interpretação

A varredura por subcategorias está praticamente completa, mas o recálculo estrutural continua bloqueado até identificar exatamente os **três CNPJs originais ainda não examinados** e consolidar as reconciliações já abertas.

## 6. Próxima ação

Executar auditoria automática de cobertura entre:

- os 103 CNPJs únicos do inventário original; e
- todos os CNPJs originais registrados na aba `BNE_validacao`.

O objetivo é identificar, sem inferência manual, os três CNPJs ainda ausentes da revalidação. Só então concluir a primeira passagem dos 103.

Após 103/103 examinados, preparar uma matriz de fechamento por status — sem ainda recalcular oferta ativa — distinguindo:

- ativo compatível;
- ativo com reconciliação;
- baixado;
- inapto;
- conflito cadastral;
- status corrente pendente;
- fora do escopo varejista;
- CNPJ substituto/adicional;
- linha originalmente sem CNPJ recuperada.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_revalidacao_lote14_papelaria_fechamento_20260923_v001.csv`
