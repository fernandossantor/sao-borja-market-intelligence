# Bens não essenciais — universo candidato reconciliado v003 — 24/09/2026

## 1. Atualização

A v003 incorpora o lote 20.

Composição do universo de controle:

- 103 CNPJs originais;
- 33 CNPJs externos aos 103;
- 4 linhas ainda sem CNPJ suficientemente identificado.

Total: **140 registros de controle**.

O total permanece igual à v002 porque Loja Portal e Elegância saíram da camada de linhas sem CNPJ e passaram para a camada de CNPJs externos identificados.

## 2. Mudanças

### Loja Portal

A linha 132 deixa de ser registro sem CNPJ. Passa a ser representada por:

- CNPJ `17.705.834/0001-03`;
- fantasia PORTAL;
- Picon & Oliveira Ltda;
- situação ativa;
- Rua General Marques, 1236.

A hipótese anterior de Nayef Abdo Hijazi é descartada para essa linha.

### Elegância Moda e Acessórios

A linha 134 passa a ter o CNPJ `11.496.172/0001-14`, identificado em lista cadastral recente de empresas ativas de vestuário de São Borja.

Endereço e razão social detalhados continuam como pendências de metadado, sem bloquear a inclusão no cenário candidato.

## 3. Linhas ainda sem CNPJ

Restam quatro linhas sem identificação jurídica suficiente:

- 125 — Loja CHICMI;
- 126 — Loja do Ramada;
- 154 — Akazzo;
- 189 — Pet House.

Loja do Ramada possui apenas presença histórica; Pet House possui presença operacional atual; CHICMI e Akazzo não tiveram identidade jurídica recuperada.

## 4. Limites

A v003 ainda é exploratória. Não equivale a quantidade de lojas, operadores ou empresas ativas.

## 5. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- nenhum indicador estrutural foi recalculado.

## 6. Artefato

`docs/data_sources/bens_nao_essenciais_universo_candidato_reconciliado_20260924_v003.csv`
