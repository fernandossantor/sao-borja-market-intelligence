# Bens não essenciais — linhas sem CNPJ — lote 18 — conclusão da primeira varredura — 24/09/2026

## 1. Objeto

Este lote conclui a primeira varredura das **14 linhas que permaneciam sem CNPJ resolvido** no checkpoint de 23/09/2026.

São tratadas:

- linha 150 — Casa A Favorita;
- linha 154 — Akazzo;
- linha 160 — Amei Presentes Criativos;
- linha 161 — Bella Cestas & Presentes;
- linha 189 — Pet House;
- linha 213 — Marco Relojoeiro.

Mantêm-se integralmente as regras de governança:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhum recálculo de oferta ativa, número de operadores, raízes ou concentração.

## 2. Casa A Favorita — linha 150

Foi identificado com alto grau de confiança o CNPJ **89.224.869/0001-23**.

### Dados observados

Fontes cadastrais recentes apresentam:

- razão social: Casa Favoritasb Ltda;
- fantasia: Casa A Favorita;
- CNPJ: `89.224.869/0001-23`;
- situação: ativa;
- matriz;
- endereço: Rua General Osório, 2238;
- atividade principal: comércio varejista de vestuário;
- atividades secundárias: cama/mesa/banho, artigos esportivos e calçados;
- telefone cadastral: `55 3430-3578`.

O inventário trazia no campo de CNPJ a sequência `05534303578`.

### Interpretação

A sequência de 11 dígitos coincide com o telefone cadastral **(55) 3430-3578**. Portanto, o problema não é um CNPJ truncado a ser completado, mas provavelmente um **erro de campo** na fonte original.

### Decisão provisória

- preencher a linha 150 do sucessor com `89.224.869/0001-23`;
- registrar `05534303578` como dado originalmente classificado de forma incorreta;
- nunca reconstruir CNPJ a partir daquele número.

## 3. Akazzo — linha 154

Buscas dirigidas por:

- Akazzo;
- Akazzo + São Borja;
- Akazzo + calçados;
- Akazzo + CNPJ;

não produziram fonte local específica.

Os resultados recuperados para o nome Akazzo referem-se a empresas de outros estados e foram descartados por homonímia.

### Decisão provisória

Manter a linha sem CNPJ e sem candidato jurídico.

## 4. Amei Presentes Criativos — linha 160

Este caso apresenta uma provável transição de CNPJ, mas ainda não completamente demonstrada.

### Dados observados — CNPJ histórico

O marketplace Magalu identifica a loja parceira **Amei Presentes Criativos** como:

- CNPJ `30.650.368/0001-66`;
- titular Jenifer Bettim Marques Dias;
- endereço Avenida Júlio Trois, 1559, Passo.

A ficha cadastral desse CNPJ informa:

- situação **baixada** desde 03/11/2025;
- motivo: encerramento/liquidação voluntária.

### Dados observados — CNPJ novo

Foi localizado outro CNPJ da mesma titular:

- `66.405.682/0001-20`;
- Jenifer Bettim Marques Dias;
- situação ativa;
- abertura em 23/04/2026;
- mesmo endereço: Avenida Júlio Trois, 1559;
- atividades compatíveis com armarinho, vestuário, outros produtos, joalheria, cama/mesa/banho, alimentos e bebidas.

### Interpretação

A combinação:

- mesma titular;
- mesmo endereço;
- baixa do CNPJ anterior em novembro/2025;
- abertura do novo em abril/2026;

constitui evidência forte de **possível sucessão operacional**.

Não foi localizada, porém, fonte que vincule explicitamente a marca Amei Presentes Criativos ao novo CNPJ `66.405.682/0001-20`.

### Decisão provisória

- registrar `30.650.368/0001-66` como CNPJ histórico diretamente vinculado à marca;
- registrar `66.405.682/0001-20` como **sucessor candidato forte**;
- não preencher ainda um CNPJ corrente canônico para a linha 160.

## 5. Bella Cestas & Presentes — linha 161

A operação Bella Cestas & Presentes aparece atualmente em:

- Rua Coronel Aparício Mariense, 2671, sala 02;
- telefone 55 99657-5801.

No mesmo endereço e sala está cadastrado o CNPJ:

- `48.341.505/0001-46`;
- Michele Silveira Avila;
- situação ativa;
- atividade principal de estética;
- atividades secundárias de vestuário e cosméticos.

### Interpretação

A co-localização é exata, mas existem dois problemas:

- o telefone cadastral da pessoa jurídica não coincide com o telefone da Bella Cestas;
- o cadastro não apresenta atividade evidente de cestas/presentes nem a marca Bella Cestas.

### Decisão provisória

Tratar `48.341.505/0001-46` apenas como **candidato moderado por co-localização**, sem preencher a linha 161.

## 6. Pet House — linha 189

A presença operacional atual é consistente:

- Pet House;
- Rua Joaquim Gonçalves Ledo, 354, Itachere;
- telefone 55 99947-3464;
- perfil Instagram `pethouse879`;
- atividade pet shop;
- listagens operacionais recentes em mais de uma fonte.

Nenhum CNPJ ou razão social suficientemente confiável foi recuperado a partir do nome, endereço, telefone ou identificador de rede social.

### Decisão provisória

Manter a linha sem CNPJ, mas classificar a operação como **presença operacional atual confirmada / identidade jurídica pendente**.

## 7. Marco Relojoeiro — linha 213

Foi localizado o CNPJ candidato **87.236.758/0001-01 — Telo e Telo Ltda**.

### Dados observados

Marco Relojoeiro aparece em diretório no endereço:

- Rua General Osório, 2215;
- telefone 55 3431-2598.

Telo e Telo Ltda:

- CNPJ `87.236.758/0001-01`;
- situação ativa;
- mesmo endereço: Rua General Osório, 2215;
- CNAE principal de óptica;
- atividades secundárias de relojoaria, joalheria, reparação de joias e reparação de relógios;
- sócios-administradores: Marco Telo e Roberto Mack Telo.

### Interpretação

A convergência entre:

- endereço;
- atividade de relojoaria/reparação;
- nome do sócio Marco Telo;

torna o CNPJ um **candidato forte** para Marco Relojoeiro.

Entretanto, o edifício abriga outras pessoas jurídicas e não foi encontrada fonte declarando explicitamente que “Marco Relojoeiro” é marca/fantasia da Telo e Telo Ltda.

### Decisão provisória

Manter `87.236.758/0001-01` como candidato forte e não preencher canonicamente a linha 213 ainda.

## 8. Fechamento da Etapa A

As 14 linhas restantes do checkpoint foram todas investigadas nos lotes 16–18.

### CNPJs identificados com grau forte

- Magazine Bandeirante → `87.583.456/0001-00`;
- Carol Modas → `88.721.220/0001-55`;
- Casa A Favorita → `89.224.869/0001-23`.

### Casos com CNPJ candidato forte ou histórico

- 7 Povos Confecções → `97.093.694/0001-90` — candidato forte;
- Ka Lopes Fitness → `15.009.711/0001-02` — candidato histórico forte;
- Amei Presentes Criativos → histórico `30.650.368/0001-66`, baixado; sucessor candidato `66.405.682/0001-20`;
- Marco Relojoeiro → `87.236.758/0001-01` — candidato forte.

### Candidato jurídico insuficiente

- Loja Portal → Nayef Abdo Hijazi como candidato de titular/razão, sem CNPJ recuperado;
- Bella Cestas & Presentes → `48.341.505/0001-46` como candidato moderado por co-localização.

### Sem CNPJ identificado, mas com presença comprovável

- Loja do Ramada — presença histórica;
- Pet House — presença operacional atual.

### Sem identificação jurídica suficiente

- Loja CHICMI;
- Elegância Moda e Acessórios;
- Akazzo.

## 9. O que este fechamento NÃO significa

A Etapa A está concluída como **varredura documental**, mas isso não significa que todas as 14 linhas tenham sido resolvidas.

Não alterar ainda:

- oferta ativa;
- número de operadores;
- concentração;
- estrutura de raízes.

## 10. Próxima etapa — Etapa B

Consolidar todos os CNPJs:

- adicionais;
- substitutos;
- identificados em linhas originalmente sem CNPJ;
- candidatos fortes;
- candidatos ainda não promovíveis;

em uma única matriz deduplicada, com classificação de origem e elegibilidade.

Essa matriz deverá distinguir, no mínimo:

1. substituto de CNPJ original;
2. correção de duplicidade;
3. CNPJ adicional de raiz já presente;
4. CNPJ identificado de linha originalmente sem número;
5. CNPJ histórico de marca;
6. sucessor candidato;
7. candidato forte;
8. candidato moderado;
9. CNPJ homônimo/alternativo ainda não reconciliado.

## 11. Artefato auditável

`docs/data_sources/bens_nao_essenciais_sem_cnpj_lote18_20260924_v001.csv`
