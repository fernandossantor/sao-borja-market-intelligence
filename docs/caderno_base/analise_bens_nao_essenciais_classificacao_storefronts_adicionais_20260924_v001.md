# Bens não essenciais — classificação mercadológica dos storefronts adicionais — 24/09/2026

## 1. Objeto

Auditar a classificação mercadológica dos **sete storefronts adicionais** já incorporados ao primeiro cenário exploratório de oferta de bens não essenciais em São Borja.

Este bloco **não altera o denominador** de 121–122 storefronts já calculado. Seu objetivo é remover a pendência de classificação dos adicionais antes de qualquer contagem por subcategoria.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhuma métrica canônica promovida.

## 2. Regra metodológica

A classificação foi feita em três níveis de evidência, nesta ordem:

1. descrição de primeira parte da própria rede, quando disponível;
2. CNAE principal corrente da unidade jurídica;
3. diretório operacional/cadastral recente para confirmar a aderência da unidade.

A classificação é **analítica**, não uma redefinição da CNAE e não implica exclusividade de mix. Lojas multissegmento permanecem explicitamente tratadas como tal.

## 3. Resultado

### Tottal Casa & Lazer — 92.012.467/0094-79

**Dado observado:** o Grupo Grazziotin descreve a Tottal como especializada em utilidades para o lar, com bazar, cama/mesa/banho, camping, decoração, eletroportáteis e utensílios de cozinha.

**Decisão analítica:** `CASA_UTILIDADES_LAZER`.

**Limite:** o mix é amplo; a categoria resume a proposta principal e não reduz a loja a um único tipo de produto.

### Por Menos — 92.012.467/0121-86

**Dado observado:** CNAE principal 4781-4/00, comércio varejista de artigos do vestuário e acessórios.

**Decisão analítica:** `MODA_VESTUARIO_ACESSORIOS`.

### Tech Box — 92.012.467/0265-60

**Dado observado:** CNAE principal 4774-1/00, comércio varejista de artigos de óptica.

**Decisão analítica:** `OPTICA`.

**Limite:** a classificação segue a atividade principal cadastral e não o nome comercial, que poderia sugerir outro segmento.

### Pormenos — 92.012.467/0451-90

**Dado observado:** CNAE principal 4781-4/00, comércio varejista de artigos do vestuário e acessórios.

**Decisão analítica:** `MODA_VESTUARIO_ACESSORIOS`.

### Brasil Free Shop — 32.195.385/0011-58

**Dado observado:** a Receita Estadual/RS inclui o CNPJ na lista oficial de lojas francas de fronteira terrestre em São Borja. A atividade principal é loja franca/duty free e a unidade possui múltiplas atividades varejistas secundárias.

**Decisão analítica:** `LOJA_FRANCA_VAREJO_MISTO`.

**Limite:** não é metodologicamente adequado forçar a unidade a uma única categoria de produto.

### José Altamir Silveira da Rosa Ltda — 93.202.695/0002-56

**Dado observado:** unidade ativa em São Borja, CNAE principal 4781-4/00, comércio varejista de artigos do vestuário e acessórios.

**Decisão analítica:** `MODA_VESTUARIO_ACESSORIOS`.

**Limite:** a marca/fachada da unidade permanece pendente. A classificação refere-se à atividade econômica do estabelecimento jurídico, não a uma marca presumida.

### Lojas Pompéia / Lins Ferrão — 87.345.021/0033-04

**Dado observado:** diretório operacional recente associa o CNPJ e o endereço Rua General Marques, 1196, a roupas e acessórios; a razão social é Lins Ferrão Artigos do Vestuário Ltda.

**Decisão analítica:** `MODA_VESTUARIO_ACESSORIOS`.

**Limite:** a categoria primária não pretende excluir calçados ou outros itens do mix.

## 4. Síntese calculada

Dos sete adicionais:

- 4 são classificados em `MODA_VESTUARIO_ACESSORIOS`;
- 1 em `CASA_UTILIDADES_LAZER`;
- 1 em `OPTICA`;
- 1 em `LOJA_FRANCA_VAREJO_MISTO`.

Total reconciliado: **7/7**.

## 5. Consequência metodológica

A pendência de classificação dos storefronts adicionais está encerrada para o primeiro cenário exploratório.

O próximo passo não deve ser uma contagem automática por rótulo textual do inventário, porque as 120 linhas originais usam nomenclaturas heterogêneas, grafias distintas e categorias mistas. Antes da agregação, é necessário criar uma **taxonomia harmonizada e auditável** para as linhas originais, preservando os casos multissegmento.

## 6. Fontes

- Grupo Grazziotin — Tottal Casa & Lazer: https://www.grupograzziotin.com.br/nossos-negocios/tottal/
- Cirtrox — Por Menos, CNPJ 92.012.467/0121-86: https://www.cirtrox.com.br/consulta-empresas/empresa/92012467012186-por-menos
- Cirtrox — Tech Box, CNPJ 92.012.467/0265-60: https://www.cirtrox.com.br/consulta-empresas/empresa/92012467026560-tech-box
- Solutudo — Pormenos, CNPJ 92.012.467/0451-90: https://www.solutudo.com.br/empresas/rs/s-borja/roupas-e-acessorios/grazziotin-s-a-9418715
- Receita Estadual/RS — Lista de Lojas Francas de Fronteira Terrestre: https://atendimento.receita.rs.gov.br/lojas-francas-de-fronteira-terrestre
- Econodata — José Altamir Silveira da Rosa Ltda, CNPJ 93.202.695/0002-56: https://www.econodata.com.br/consulta-empresa/93202695000256-jose-altamir-silveira-da-rosa-ltda
- Solutudo — Lins Ferrão Artigos do Vestuário Ltda, CNPJ 87.345.021/0033-04: https://www.solutudo.com.br/empresas/rs/s-borja/roupas-e-acessorios/lins-ferrao-artigos-do-vestuario-ltda-9418535

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_classificacao_storefronts_adicionais_20260924_v001.csv`
