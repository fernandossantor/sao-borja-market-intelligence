# Revalidação de CNPJs — bens não essenciais — lote 15 — fechamento da primeira passagem dos 103 CNPJs — 23/09/2026

## 1. Objeto

Este lote fecha a primeira passagem dirigida pelos **103 CNPJs únicos originais** do inventário de bens não essenciais.

Uma auditoria automática de cobertura, realizada após o lote 14, comparou:

- os 103 CNPJs únicos extraídos do inventário original; e
- os CNPJs já registrados na aba `BNE_validacao`.

A comparação identificou exatamente três CNPJs originais ainda não examinados:

- `13.956.162/0001-40` — Mega City;
- `60.167.511/0001-24` — Luna Modas;
- `45.897.087/0001-80` — Su Store.

Este lote revalida os três.

## 2. Governança

Permanecem válidas as regras do checkpoint:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base Territorial v028 read-only;
- a conclusão de 103/103 examinados **não autoriza automaticamente** recalcular oferta ativa, concentração, número final de operadores ou proporção multiunidade;
- a próxima etapa é consolidar os status de reconciliação.

## 3. Mega City — 13.956.162/0001-40

Duas fontes recentes convergem para:

- situação ativa;
- matriz;
- fantasia Mega City;
- razão social Hiad Ahmad Al Jamal;
- Rua General Marques, 1168;
- abertura em 06/07/2011;
- CNAE principal de comércio varejista de vestuário;
- atividades secundárias de calçados, supermercado e cama/mesa/banho.

**Decisão provisória:** manter.

**Limite:** o conjunto de CNAEs secundários não autoriza atribuir participação relevante em todos esses mercados.

## 4. Luna Modas — 60.167.511/0001-24

Duas fontes atuais convergem para:

- situação ativa;
- matriz;
- fantasia Luna Modas;
- razão social Narieli Sarmento Picinin Ltda;
- Rua Félix da Cunha, 203;
- abertura em 31/03/2025;
- CNAE principal de vestuário;
- CNAE secundário de calçados.

**Decisão provisória:** manter.

## 5. Su Store — 45.897.087/0001-80

A matriz de São Borja está apresentada como:

- ativa;
- fantasia Su Store;
- razão social Leonardo de Souza Storch;
- Rua General Osório, 2270;
- abertura em 04/04/2022;
- CNAE principal de vestuário;
- atividade secundária de suvenires, bijuterias e artesanatos.

A mesma raiz possui filial ativa em Santiago, `45.897.087/0002-60`.

**Decisão provisória:** manter a matriz de São Borja.

**Limite:** a filial de Santiago está fora do recorte municipal e não pode ser somada à oferta local.

## 6. Fechamento da cobertura

Com este lote:

- **103/103 CNPJs originais foram examinados = 100,00% de cobertura de auditoria**;
- **102/103 possuem alguma evidência independente recuperada = 99,03%**;
- o único CNPJ original examinado sem evidência externa suficientemente confiável permanece `28.597.654/0001-63` — Pimentas Boutique Sensual.

Esses indicadores medem **cobertura de revalidação**, não oferta ativa.

## 7. O que ainda impede o recálculo estrutural

A cobertura completa não elimina os problemas de reconciliação. Permanecem, entre outros:

- CNPJs baixados com marcas possivelmente ainda operacionais;
- CNPJs inaptos com marcas aparentando continuidade;
- conflito cadastral ativa × baixada;
- marcas operacionais diferentes da fantasia cadastral;
- CNPJs adicionais de raízes já existentes;
- linhas originalmente sem CNPJ que agora receberam candidatos robustos;
- um registro ativo fora do escopo varejista;
- endereços cadastrais e operacionais divergentes;
- CNPJs ativos cuja função física ainda precisa ser distinguida de depósito, matriz administrativa ou loja.

## 8. Próxima etapa metodológica

A próxima etapa deve ser uma **matriz de fechamento de auditoria dos 103 CNPJs originais**, sem recalcular ainda a oferta.

Para cada CNPJ original, consolidar:

- status de auditoria;
- situação cadastral observada;
- necessidade de reconciliação;
- decisão provisória;
- existência de CNPJ substituto/adicional;
- status da marca;
- status do endereço;
- elegibilidade provisória para futura contagem de oferta;
- bloqueio que ainda impede decisão final.

Somente depois dessa matriz será possível decidir se a cobertura e a qualidade de reconciliação são suficientes para iniciar o recálculo.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_revalidacao_lote15_fechamento_103cnpjs_20260923_v001.csv`
