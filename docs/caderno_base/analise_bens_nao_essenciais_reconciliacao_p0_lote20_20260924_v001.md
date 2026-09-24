# Bens não essenciais — reconciliação final P0 — lote 20 — 24/09/2026

## 1. Objeto

Segundo lote de resolução da fila P0. O foco foi resolver duas linhas originalmente sem CNPJ e revalidar três bloqueios que ainda não podem ser encerrados.

Governança preservada: branch `explore/receita-estadual-rs-market-intel-v1`, PR #41 aberto/draft/sem merge e Caderno-Base v028 read-only.

## 2. Loja Portal — linha 132

Foi localizada ficha cadastral recente para:

- fantasia: PORTAL;
- razão social: Picon & Oliveira Ltda;
- CNPJ: `17.705.834/0001-03`;
- situação: ativa;
- CNAE principal: comércio varejista de vestuário;
- endereço: Rua General Marques, 1236, São Borja.

A marca Loja Portal já aparecia em diretório operacional nesse mesmo endereço.

**Correção de auditoria:** a hipótese anterior de Nayef Abdo Hijazi derivava apenas de co-localização e setor. Ela deve ser descartada como identidade jurídica da Loja Portal porque a ficha PORTAL fornece vínculo direto entre fantasia, CNPJ e endereço.

**Decisão provisória:** P0 resolvido. Adicionar `17.705.834/0001-03` como CNPJ identificado de linha originalmente sem número.

## 3. Elegância Moda e Acessórios — linha 134

Lista cadastral setorial de empresas ativas de vestuário em São Borja, atualizada em 21/08/2026, registra exatamente:

- fantasia: Elegancia Modas E Acessorios.;
- CNPJ: `11.496.172/0001-14`;
- município: São Borja;
- situação no conjunto: ativa.

Não foi recuperada, nesta rodada, ficha individual com endereço e razão social detalhados.

**Decisão provisória:** P0 resolvido quanto à identidade CNPJ e situação ativa. Endereço/razão detalhados permanecem como pendência não bloqueante de metadado.

## 4. 7 Povos Kids — linha 122

Fichas específicas recentes e uma lista setorial atualizada em agosto/2026 apresentam o CNPJ `62.201.625/0001-79` como ativo, com fantasia 7 Povos Kids e endereço na Avenida Presidente Vargas, 1970.

Persiste, contudo, uma listagem genérica recente que apresenta o mesmo CNPJ como baixado.

**Decisão:** manter P0. A evidência favorável à situação ativa ficou mais forte, mas o conflito não será resolvido por maioria de republicadores. É necessária fonte oficial atual inequívoca.

## 5. Loja Marlin Fashion — linha 100

Duas fontes recentes convergem para:

- CNPJ `18.556.994/0001-92`;
- situação **inapta**;
- Econodata: inaptidão desde 19/05/2026, motivo 63 — omissão de declarações;
- endereço cadastral: Rua General Osório, 2186.

Existem republicadores/diretórios que ainda exibem situação ativa, mas a evidência recente e mais detalhada converge para inaptidão.

**Decisão:** não tratar o CNPJ como ativo cadastral. P0 permanece aberto porque inaptidão não prova fechamento do ponto físico e não foi localizado novo CNPJ da marca.

## 6. Bicho Mimado — linha 188

O CNPJ original `22.663.567/0001-80` continua inadequado para contagem como ativo cadastral.

Por outro lado, diretórios operacionais revisados recentemente mantêm Pet Shop Bicho Mimado na Rua Inhandoi, 141, em São Borja.

Foi encontrado na web outro CNPJ associado a uma empresa homônima Bicho Mimado, mas não houve vínculo documental ou geográfico suficiente com a operação de São Borja; o resultado foi descartado.

**Decisão:** manter P0 como presença operacional confirmada / identidade jurídica corrente pendente.

## 7. Resultado do lote

- P0 resolvidos: Loja Portal e Elegância Moda e Acessórios.
- P0 mantidos: 7 Povos Kids, Marlin Fashion e Bicho Mimado.
- A fila P0 cai de 13 para 11 registros de controle após a atualização das matrizes.

## 8. Fontes principais

- Cirtrox — ficha PORTAL, CNPJ 17.705.834/0001-03, atualização 21/08/2026.
- Cirtrox — lista de empresas ativas de vestuário em São Borja, incluindo Elegancia Modas E Acessorios. 11.496.172/0001-14.
- CNPJ.biz e Cirtrox — 7 Povos Kids.
- Econodata e Serasa Experian — Loja Marlin Fashion.
- TutorCanino e OndePet — presença operacional recente do Bicho Mimado.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_reconciliacao_p0_lote20_20260924_v001.csv`
