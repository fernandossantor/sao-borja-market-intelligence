# Bens não essenciais — linhas sem CNPJ — lote 16 — 24/09/2026

## 1. Objeto

Início da Etapa A definida no checkpoint `checkpoint_20260923_bne_103_revalidada_continuidade.md`: revalidar as 14 linhas restantes do inventário de bens não essenciais que não possuíam CNPJ documental resolvido.

Este lote trata quatro linhas:

- 121 — Magazine Bandeirante;
- 123 — 7 Povos Confecções e Calçados São Borja;
- 125 — Loja CHICMI;
- 126 — Loja do Ramada.

O Caderno-Base v028 permanece read-only e o PR #41 permanece aberto, draft e sem merge.

## 2. Magazine Bandeirante — linha 121

Foi identificado o CNPJ **87.583.456/0001-00**.

### Dados observados

- publicação oficial do INPI vincula diretamente a marca **MB Magazine Bandeirante** ao CNPJ `87.583.456/0001-00`;
- fonte cadastral recente apresenta o mesmo CNPJ como **ativo**, no varejo de vestuário, em São Borja;
- há evidência histórica local da Magazine Bandeirante no município.

### Reconciliação necessária

Há divergência de endereço:

- marca histórica: Rua General Osório, 1373;
- cadastro recente recuperado: Rua General Osório, 2273.

A fonte cadastral recente também apresenta titularidade nominal diferente da publicação histórica do INPI.

### Decisão provisória

Classificar como **CNPJ identificado com grau forte**, preencher o número no sucessor do inventário com flag de reconciliação e preservar temporalmente endereços/titularidade.

Não transformar a identificação do CNPJ em prova automática de que a marca permanece atualmente no mesmo ponto histórico.

## 3. 7 Povos Confecções e Calçados — linha 123

Foi localizado o CNPJ candidato **97.093.694/0001-90**, de João Renato Prauchner.

### Dados observados

- o CNPJ aparece ativo no comércio varejista de vestuário;
- fontes históricas co-localizam **Loja 7 Povos** e João Renato Prauchner em Cândido Falcão, 1227/1233;
- a lista institucional SIMUSB atualizada em 22/04/2026 mantém **7 Povos Confecções**, mas em Rua General Marques, 978.

### Interpretação

A associação marca↔CNPJ é forte, porém ainda não conclusiva. O deslocamento espacial pode representar mudança do ponto comercial, mas não há documento recuperado nesta rodada ligando explicitamente a marca atual de General Marques 978 ao CNPJ `97.093.694/0001-90`.

### Decisão provisória

Manter `97.093.694/0001-90` como **candidato forte**, sem preencher canonicamente a linha 123 ainda.

Priorizar NF-e, inscrição estadual, alvará, fonte de primeira parte ou base oficial que una marca atual e CNPJ.

## 4. Loja CHICMI — linha 125

Buscas por:

- “Loja CHICMI”;
- “CHICMI São Borja”;
- variações de grafia;
- combinações com CNPJ/empresa;

não produziram fonte cadastral ou institucional suficientemente específica.

### Decisão provisória

Manter a linha sem CNPJ.

### Limite

Ausência de resultado indexado **não** permite concluir inexistência, informalidade, baixa ou fechamento.

## 5. Loja do Ramada — linha 126

A marca aparece em listagem comercial histórica de conveniados de São Borja, confirmando que não se trata de item inventado pelo inventário.

Não foi localizado, entretanto, CNPJ ou razão social com vínculo documental suficientemente confiável nesta rodada.

### Decisão provisória

Manter a linha sem CNPJ e classificar como **presença histórica confirmada, identificação jurídica pendente**.

## 6. Resultado do lote

Dos quatro registros:

- **1 CNPJ identificado com grau forte** — Magazine Bandeirante;
- **1 CNPJ candidato forte** — 7 Povos Confecções;
- **2 linhas permanecem sem CNPJ identificado** — CHICMI e Loja do Ramada.

Não há alteração no denominador da oferta ativa.

## 7. Próxima etapa

Continuar as linhas sem CNPJ em lote pequeno, prioritariamente:

- 130 — Ka Lopes Fitness;
- 132 — Loja Portal;
- 134 — Elegância Moda e Acessórios;
- 141 — Carol Modas.

Depois seguir para Casa A Favorita, Akazzo, Amei Presentes Criativos e Bella Cestas & Presentes.

## 8. Artefato auditável

`docs/data_sources/bens_nao_essenciais_sem_cnpj_lote16_20260924_v001.csv`
