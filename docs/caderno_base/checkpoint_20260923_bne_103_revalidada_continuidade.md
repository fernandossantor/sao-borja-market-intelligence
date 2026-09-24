# CHECKPOINT — São Borja — Inteligência Mercadológica
## Bens não essenciais — primeira passagem dos 103 CNPJs concluída
**Data:** 23/09/2026

## 1. Governança e estado do trabalho

- Branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- PR #41 deve permanecer **aberto, draft e sem merge**.
- O Caderno-Base Territorial **v028 permanece read-only**.
- Não recalcular ainda oferta ativa, número final de operadores, concentração, proporção multiunidade ou qualquer indicador concorrencial derivado.
- Este checkpoint substitui, como ponto de retomada operacional, o checkpoint anterior `docs/caderno_base/checkpoint_20260923_continuidade_bne_revalidacao.md`, mas não apaga nem invalida a trilha anterior.

## 2. Universo original de bens não essenciais

Inventário documental de referência:

- 120 linhas;
- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes documentais;
- 16 linhas originalmente sem CNPJ extraível.

A primeira passagem de revalidação dos **103 CNPJs únicos originais foi concluída**.

### Cobertura

- CNPJs originais examinados: **103/103 = 100,00%**.
- CNPJs originais com alguma evidência independente recuperada: **102/103 = 99,03%**.
- Único CNPJ original examinado sem evidência externa suficiente:
  - Pimentas Boutique Sensual — `28.597.654/0001-63`.

Esses percentuais medem **cobertura de auditoria**, não oferta ativa.

## 3. Matriz de fechamento dos 103 CNPJs

Artefatos consolidados:

- `docs/data_sources/bens_nao_essenciais_revalidacao_fechamento_103_20260923_v001.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_revalidacao_fechamento_103_20260923_v001.md`
- Drive — aba `BNE_fechamento_103`.

Classificação calculada a partir dos status provisórios:

- `ATIVO_COMPATIVEL`: 47;
- `ATIVO_COM_RECONCILIACAO`: 37;
- `BAIXADO`: 3;
- `BAIXADO_COM_RECONCILIACAO`: 3;
- `STATUS_CADASTRAL_PENDENTE`: 5;
- `INAPTO`: 1;
- `INAPTO_COM_MARCA_OPERACIONAL_POSSIVEL`: 1;
- `CONFLITO_CADASTRAL`: 1;
- `ATIVO_FORA_ESCOPO_VAREJISTA`: 1;
- `ATIVO_COM_RECONCILIACAO_ESTRUTURAL`: 1;
- `SEM_EVIDENCIA_INDEPENDENTE`: 1;
- `ATIVA_POR_LISTAGEM_SETORIAL_STATUS_INDIVIDUAL_PENDENTE`: 1;
- `PRESENCA_COMPATIVEL_METADADO_JURIDICO_PENDENTE`: 1.

Bloqueio estrutural calculado:

- **30 CNPJs** com `bloqueio_estrutural = SIM`;
- **73 CNPJs** com `bloqueio_estrutural = NÃO`.

A classificação de fechamento é uma camada técnica calculada do SBMI. Ela não substitui os dados observados nem autoriza, sozinha, inclusão/exclusão na oferta ativa.

## 4. Principais reconciliações encontradas na revalidação

A auditoria revelou problemas que não existiam na leitura inicial do inventário:

1. **CNPJ baixado, mas marca possivelmente ainda operacional**;
2. **CNPJ inapto, mas marca aparentemente ativa**;
3. **conflito cadastral ativa × baixada**;
4. **marca operacional diferente da fantasia cadastral**;
5. **razão social histórica diferente da razão social corrente**;
6. **endereço cadastral diferente do ponto comercial divulgado**;
7. **raízes multiunidade subcobertas**;
8. **co-localização de CNPJs da mesma raiz**;
9. **colisão de nome fantasia entre empresas juridicamente distintas**;
10. **classificação POM diferente do CNAE principal**;
11. **registro cadastral ativo fora do escopo varejista**;
12. **linhas originalmente sem CNPJ que passaram a ter CNPJ identificado**.

Esses fenômenos precisam permanecer separados. Não converter CNPJ em loja física, raiz em rede comercial ou presença cadastral em market share.

## 5. CNPJs adicionais, substitutos ou identificados durante a auditoria

Foram encontrados **17 CNPJs únicos que não faziam parte dos 103 originais**, por substituição, subcobertura de raiz ou preenchimento de linha sem CNPJ:

1. `96.418.264/0028-59` — Lojas Quero-Quero — correção candidata da duplicidade do inventário;
2. `00.776.574/1709-06` — Americanas — substituto candidato do CNPJ documental baixado;
3. `92.012.467/0094-79` — Tottal Casa & Lazer / Grazziotin;
4. `92.012.467/0121-86` — Por Menos / Grazziotin;
5. `92.012.467/0265-60` — Tech Box / Grazziotin;
6. `92.012.467/0451-90` — Pormenos / Grazziotin;
7. `87.345.021/0033-04` — Lins Ferrão — candidato forte para a operação Pompéia;
8. `58.434.608/0015-00` — RM2S — marca operacional ainda não identificada;
9. `32.195.385/0011-58` — Brasil Free Shop;
10. `32.195.385/0012-39` — Monaco Freeshop — preenche a linha 177 originalmente sem CNPJ;
11. `96.418.264/0533-30` — Lojas Quero-Quero — terceiro CNPJ da raiz identificado em São Borja;
12. `93.202.695/0002-56` — José Altamir Silveira da Rosa Ltda — raiz Requinte;
13. `05.823.159/0001-20` — G P Junior Moda Íntima — raiz M.H.;
14. `03.243.241/0001-50` — operação homônima Veterinária São Francisco — manter separada até reconciliação;
15. `59.205.031/0001-21` — matriz da raiz João e Maria Pet;
16. `92.293.703/0011-45` — Barraca Missões — segunda filial identificada em São Borja;
17. `24.495.873/0001-80` — Mais Top Papelaria — preenche a linha 215 originalmente sem CNPJ.

**Regra:** nenhum desses CNPJs deve ser incorporado automaticamente ao denominador canônico antes da reconciliação de função, unidade física, marca e situação cadastral.

## 6. Linhas originalmente sem CNPJ

O inventário tinha **16 linhas sem CNPJ extraível**.

Duas já receberam identificação documental suficientemente robusta:

- linha 177 — Monaco Freeshop → `32.195.385/0012-39`;
- linha 215 — Mais Top Papelaria → `24.495.873/0001-80`.

Restam **14 linhas** sem CNPJ documental resolvido:

1. linha 121 — Magazine Bandeirante;
2. linha 123 — 7 Povos Confecções e Calçados São Borja;
3. linha 125 — Loja CHICMI;
4. linha 126 — Loja do Ramada;
5. linha 130 — Ka Lopes Fitness;
6. linha 132 — Loja Portal;
7. linha 134 — Elegância Moda e Acessórios;
8. linha 141 — Carol Modas;
9. linha 150 — Casa A Favorita / Casa Favoritasb Ltda — o número `05534303578` do inventário não é CNPJ de 14 dígitos e não deve ser completado/inferido;
10. linha 154 — Akazzo;
11. linha 160 — Amei Presentes Criativos;
12. linha 161 — Bella Cestas & Presentes;
13. linha 189 — Pet House;
14. linha 213 — Marco Relojoeiro.

Ausência de CNPJ recuperado não autoriza concluir informalidade, inatividade ou inexistência.

## 7. Lotes já produzidos

A revalidação foi documentada em lotes pequenos e auditáveis:

- lote 01 — grandes redes e reconciliações;
- corrigenda lote 01 — Lojas Quero-Quero;
- lote 02 — raízes multiunidade;
- lote 03 — redes e reconciliações;
- lote 04 — vestuário inicial;
- lote 05 — vestuário e reconciliações;
- lote 06 — vestuário continuação;
- lote 07 — fechamento parcial de vestuário;
- lote 08 — calçados e especializados;
- lote 09 — utilidades/presentes e enquadramento setorial;
- lote 10 — ferragens, móveis e pets 01;
- lote 11 — pets 02;
- lote 12 — pets e agropecuárias;
- lote 13 — joalherias e ópticas;
- lote 14 — papelaria;
- lote 15 — fechamento dos três CNPJs faltantes e conclusão 103/103;
- matriz consolidada de fechamento dos 103.

Os CSVs estão em `docs/data_sources/` e as análises correspondentes em `docs/caderno_base/`.

## 8. Estado no Drive

Planilha exploratória:

- arquivo: `Matriz de fontes exploratórias — Receita Estadual + Fecomércio — v001 — 20260917`;
- spreadsheet ID: `1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`;
- aba `BNE_validacao`: trilha linha a linha dos lotes;
- aba `BNE_fechamento_103`: matriz consolidada dos 103 CNPJs originais.

A aba `BNE_validacao` contém registros dos CNPJs originais, CNPJs adicionais/substitutos e linhas sem CNPJ recuperadas.

## 9. O que NÃO deve ser feito na retomada

Até nova autorização metodológica, **não**:

- recalcular número final de operadores;
- recalcular oferta ativa;
- recalcular proporção de raízes multiunidade;
- recalcular concentração;
- usar número de CNPJs como número de lojas físicas;
- incorporar automaticamente os 17 CNPJs adicionais/substitutos;
- excluir automaticamente marcas cujo CNPJ original esteja baixado/inapto;
- alterar o Caderno-Base v028;
- mesclar o PR #41.

## 10. Próxima sequência exata

Retomar nesta ordem:

### Etapa A — linhas sem CNPJ

Investigar as **14 linhas restantes sem CNPJ**, em lotes pequenos, preservando três possíveis resultados:

- CNPJ identificado com evidência robusta;
- candidato insuficiente;
- sem identificação documental.

Não inventar CNPJ nem completar números truncados.

### Etapa B — matriz de CNPJs adicionais/substitutos

Criar uma matriz deduplicada dos **17 CNPJs adicionais/substitutos**, classificando cada um como:

- substituto de CNPJ original;
- correção de duplicidade;
- CNPJ adicional de raiz já presente;
- CNPJ de linha originalmente sem número;
- CNPJ homônimo/alternativo ainda não reconciliado.

Adicionar campos de:

- raiz;
- operador/marca;
- situação;
- função física conhecida;
- endereço;
- fonte;
- decisão provisória;
- elegibilidade para futura incorporação;
- bloqueio remanescente.

### Etapa C — universo candidato reconciliado

Somente depois de A e B, montar um **universo candidato reconciliado**, ainda não canônico, com:

- CNPJs originais elegíveis;
- substituições justificadas;
- adicionais elegíveis;
- exclusões provisórias justificadas;
- casos pendentes mantidos fora do denominador definitivo.

### Etapa D — decisão sobre recálculo

Avaliar se a cobertura e as reconciliações são suficientes para iniciar:

1. oferta ativa;
2. número de operadores;
3. estrutura de raízes;
4. concentração;
5. comparação entre subcategorias.

Nenhum desses indicadores deve ser recalculado antes da conclusão das etapas A–C.

## 11. Regra de documentação

Cada novo lote deve gerar:

- CSV auditável em `docs/data_sources/`;
- análise explicativa em `docs/caderno_base/`;
- registro correspondente no Drive;
- distinção explícita entre dado observado, dado calculado, interpretação e decisão provisória.

## 12. Ponto de retomada recomendado

**Começar diretamente pela Etapa A: revalidação das 14 linhas sem CNPJ restantes, em lotes pequenos e auditáveis.**

Não repetir a primeira passagem dos 103 CNPJs já concluída.
