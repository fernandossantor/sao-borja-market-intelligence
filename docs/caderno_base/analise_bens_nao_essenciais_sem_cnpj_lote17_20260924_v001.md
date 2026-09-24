# Bens não essenciais — linhas sem CNPJ — lote 17 — 24/09/2026

## 1. Objeto

Continuação da Etapa A do checkpoint `checkpoint_20260923_bne_103_revalidada_continuidade.md`.

Este lote trata quatro linhas originalmente sem CNPJ extraível:

- 130 — Ka Lopes Fitness;
- 132 — Loja Portal;
- 134 — Elegância Moda e Acessórios;
- 141 — Carol Modas.

O Caderno-Base v028 permanece read-only. O PR #41 permanece aberto, draft e sem merge. Nenhuma métrica estrutural é recalculada nesta etapa.

## 2. Ka Lopes Fitness — linha 130

Foi identificado o CNPJ histórico candidato **15.009.711/0001-02**, de Ana Karine Mello Lopes.

### Dados observados

Uma relação oficial histórica de emitentes NF-e da Receita Estadual/RS registrou:

- Ana Karine Mello Lopes;
- CNPJ `15.009.711/0001-02`;
- Avenida Presidente Vargas, 1938, sala B;
- telefone 3431-5212.

Esses dois últimos elementos coincidem com o endereço e o telefone historicamente divulgados para **Ka Lopes Fitness Colcci**.

O CNPJ permanece ativo em fonte cadastral recente.

A marca Ka Lopes Fitness, entretanto, aparece atualmente em diretório operacional na Rua Barão do Rio Branco, 2305, sala 102A, com outro telefone.

### Interpretação

O vínculo histórico marca↔CNPJ é muito forte.

O vínculo entre esse mesmo CNPJ e a **operação corrente** da Ka Lopes Fitness não está demonstrado.

### Decisão provisória

- registrar `15.009.711/0001-02` como **candidato histórico forte**;
- não preencher canonicamente a linha 130 ainda;
- buscar NF-e, inscrição estadual, alvará ou fonte de primeira parte da operação atual.

## 3. Loja Portal — linha 132

A Loja Portal permanece listada no varejo de roupas em:

- Rua General Marques, 1236;
- telefone 3431-7875;
- e-mail comercial próprio.

No mesmo endereço, diferentes diretórios empresariais registram **Nayef Abdo Hijazi** e “Nayef Abdo Hijazi Filial 2”, também no setor de roupas.

### Interpretação

Nayef Abdo Hijazi é um **candidato forte de pessoa jurídica/titular**, mas nesta rodada não foi recuperado:

- o CNPJ exato;
- vínculo explícito entre a marca Loja Portal e a pessoa jurídica.

### Decisão provisória

Manter a linha 132 sem CNPJ resolvido e registrar Nayef Abdo Hijazi apenas como candidato de razão social/titular.

## 4. Elegância Moda e Acessórios — linha 134

Buscas dirigidas pelo:

- nome exato;
- variações com e sem acento;
- combinações com São Borja;
- CNPJ;
- vestuário/moda;

não retornaram fonte cadastral ou institucional suficientemente específica.

### Decisão provisória

Manter a linha sem CNPJ.

### Limite

Ausência de resultado indexado não permite concluir inexistência, informalidade, baixa ou encerramento.

## 5. Carol Modas — linha 141

Foi identificado de forma robusta o CNPJ **88.721.220/0001-55**, de Carolina Oliveira Maciel.

### Dados observados

Fonte cadastral recente apresenta:

- situação ativa;
- abertura em 03/02/1983;
- comércio varejista de vestuário;
- Rua Cândido Falcão, 1247;
- telefone 3431-3216.

A marca **Carol Modas GG** aparece no mesmo endereço e telefone em diretório de moda.

Além disso, seller atual no Magalu utiliza:

- nome Carol_Modas_Saoborja;
- CNPJ `88.721.220/0001-55`;
- razão social Carolina Oliveira Maciel;
- Rua Cândido Falcão, 1247.

### Decisão provisória

Classificar como **CNPJ identificado com grau forte** e preencher `88.721.220/0001-55` na linha 141 do sucessor.

## 6. Resultado do lote

Dos quatro registros:

- **1 CNPJ identificado com grau forte** — Carol Modas;
- **1 CNPJ histórico candidato forte** — Ka Lopes Fitness;
- **1 candidato de razão social sem CNPJ recuperado** — Loja Portal / Nayef Abdo Hijazi;
- **1 linha ainda sem candidato confiável** — Elegância Moda e Acessórios.

Somando os lotes 16 e 17, foram tratadas **8 das 14 linhas pendentes** da Etapa A.

Resultados acumulados nessas oito:

- 2 CNPJs identificados com grau forte: Magazine Bandeirante e Carol Modas;
- 2 candidatos fortes: 7 Povos Confecções e Ka Lopes Fitness;
- 1 candidato de razão social sem CNPJ: Loja Portal;
- 3 linhas ainda sem identificação jurídica suficiente: CHICMI, Loja do Ramada e Elegância Moda e Acessórios.

Nenhum desses resultados altera ainda o denominador da oferta ativa.

## 7. Próxima etapa

Restam seis linhas da Etapa A:

- 150 — Casa A Favorita / Casa Favoritasb Ltda;
- 154 — Akazzo;
- 160 — Amei Presentes Criativos;
- 161 — Bella Cestas & Presentes;
- 189 — Pet House;
- 213 — Marco Relojoeiro.

A linha Casa A Favorita deve ser tratada com atenção porque o inventário contém `05534303578`, número que **não possui 14 dígitos** e não pode ser convertido em CNPJ por inferência.

## 8. Artefato auditável

`docs/data_sources/bens_nao_essenciais_sem_cnpj_lote17_20260924_v001.csv`
