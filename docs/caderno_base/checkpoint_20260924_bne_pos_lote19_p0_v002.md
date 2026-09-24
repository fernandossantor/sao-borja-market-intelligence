# CHECKPOINT — São Borja — Inteligência Mercadológica
## Bens não essenciais — pós-lote 19 / fila P0 v002
**Data:** 24/09/2026

## 1. Governança

- Branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- PR #41: **aberto, draft e sem merge**.
- Caderno-Base Territorial: **v028 read-only**.
- Não recalcular ainda oferta ativa canônica, operadores, raízes ou concentração.
- Este checkpoint substitui como ponto de retomada o checkpoint anterior `checkpoint_20260923_bne_103_revalidada_continuidade.md`, preservando toda a trilha anterior.

## 2. Estado consolidado já concluído

### Universo original
- 120 linhas de inventário;
- 103 CNPJs únicos originais;
- 103/103 examinados = 100,00%;
- 102/103 com alguma evidência independente recuperada = 99,03%;
- único original sem evidência independente suficiente: Pimentas Boutique Sensual — `28.597.654/0001-63`.

### Linhas originalmente sem CNPJ
A primeira varredura das 14 linhas pendentes foi concluída nos lotes 16–18.

CNPJs identificados com grau forte:
- Magazine Bandeirante → `87.583.456/0001-00`;
- Carol Modas → `88.721.220/0001-55`;
- Casa A Favorita → `89.224.869/0001-23`.

Candidatos fortes/históricos:
- 7 Povos Confecções → `97.093.694/0001-90`;
- Ka Lopes Fitness → `15.009.711/0001-02` histórico;
- Amei Presentes Criativos → histórico `30.650.368/0001-66`, sucessor candidato `66.405.682/0001-20`;
- Marco Relojoeiro → `87.236.758/0001-01`.

Outros:
- Loja Portal → Nayef Abdo Hijazi como candidato de razão social, sem CNPJ recuperado;
- Bella Cestas → `48.341.505/0001-46` candidato moderado;
- Pet House → presença operacional atual sem identidade jurídica;
- CHICMI, Elegância Moda e Acessórios, Akazzo → sem identificação jurídica suficiente;
- Loja do Ramada → presença histórica, identidade jurídica pendente.

### Matriz externa v002
Artefato:
`docs/data_sources/bens_nao_essenciais_cnpjs_adicionais_substitutos_candidatos_20260924_v002.csv`

Contém **31 CNPJs externos aos 103 originais**.

### Universo candidato v002
Artefato:
`docs/data_sources/bens_nao_essenciais_universo_candidato_reconciliado_20260924_v002.csv`

Composição:
- 103 CNPJs originais;
- 31 CNPJs externos;
- 6 linhas sem CNPJ suficientemente identificado;
- total: **140 registros de controle**.

**Importante:** 140 não representa lojas, operadores ou oferta ativa.

## 3. Fila priorizada v002

Artefato:
`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v002.csv`

Distribuição atual:
- P0: **13**;
- P1: **21**;
- P2: **12**;
- P3: **37**;
- P4: **57**.

P0 = bloqueio direto de inclusão/exclusão ou atividade corrente.
P1 = bloqueio de identidade, sucessão ou número de unidades.
P2–P4 não devem bloquear o primeiro recálculo exploratório se não alterarem o denominador.

## 4. Lote 19 — P0 já resolvidos ou rebaixados

Artefatos:
- `docs/data_sources/bens_nao_essenciais_reconciliacao_p0_lote19_20260924_v001.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_reconciliacao_p0_lote19_20260924_v001.md`

### Resolvidos
- MB Lojas: CNPJ histórico `93.641.710/0003-43` sai do cenário corrente; operador atual `43.839.616/0001-63`.
- Loja It Girls: CNPJ histórico `32.894.094/0001-86` sai; operador atual `35.686.566/0001-01`.
- Top 20: CNPJ histórico `34.542.287/0001-01` sai; operador atual `37.106.058/0001-24`.
- Americanas: original `33.014.556/1900-33` sai; operação corrente `00.776.574/1709-06`.
- Cia do Uniforme: `41.726.814/0001-95` passa a ativo compatível para cenário-base exploratório.
- Menta Pimenta: `18.627.385/0001-87` passa a ativo compatível para cenário-base exploratório.
- Loja Maçônica Luz Invisível: exclusão provisória do universo BNE comercial por natureza associativa/CNAE não varejista.

### Rebaixados de P0 para P1
- Excêntrica: presença atual da marca confirmada; CNPJ `46.083.011/0001-83` candidato forte, vínculo marca↔CNPJ ainda pendente.
- Rilu: operação atual Rilu Tecidos sob `00.664.113/0001-91`; equivalência com Rilu Armarinhos ainda pendente.

## 5. P0 remanescentes — ponto exato de retomada

Restam **13 P0**:

1. linha 100 — Loja Marlin Fashion — CNPJ `18.556.994/0001-92` — INAPTO;
2. linha 120 — Pimentas Boutique Sensual — `28.597.654/0001-63` — sem evidência independente;
3. linha 122 — 7 Povos Kids — `62.201.625/0001-79` — conflito ativa × baixada;
4. linha 125 — Loja CHICMI — sem CNPJ/evidência suficiente;
5. linha 126 — Loja do Ramada — presença apenas histórica;
6. linha 132 — Loja Portal — presença atual, identidade jurídica pendente;
7. linha 134 — Elegância Moda e Acessórios — sem identificação;
8. linha 144 — Mundi Calçados — `38.128.053/0001-65` — situação cadastral pendente;
9. linha 147 — Ciranda Boutique — `90.134.701/0001-06` — situação cadastral pendente;
10. linha 154 — Akazzo — sem identificação;
11. linha 188 — Bicho Mimado — `22.663.567/0001-80` — INAPTO, marca aparentemente operacional;
12. linha 189 — Pet House — presença atual, identidade jurídica pendente;
13. linha 190 — Ponto dos Pets — `34.338.660/0001-07` — situação cadastral corrente pendente.

## 6. Sinais adicionais já levantados para o próximo lote

- Marlin Fashion: fontes recentes convergem para INAPTA desde 19/05/2026 por omissão de declarações.
- Bicho Mimado: base derivada da RFB atualizada em 03/07/2026 continua classificando o CNPJ como INAPTO.
- 7 Povos Kids: fichas específicas recentes mostram ATIVA, mas existe listagem genérica conflitante como BAIXADA; não resolver por maioria de fontes.
- Ponto dos Pets: licença municipal 2022 e contrato municipal 2023 confirmam pessoa jurídica/endereço, mas não substituem status cadastral 2026.

## 7. Próxima sequência exata

Continuar P0 em pequenos lotes, nesta ordem sugerida:

### Lote 20
- Marlin Fashion;
- 7 Povos Kids;
- Mundi Calçados;
- Ciranda Boutique;
- Ponto dos Pets;
- Bicho Mimado.

Objetivo: resolver situação cadastral/atividade corrente.

### Lote 21
- Pimentas Boutique Sensual;
- CHICMI;
- Loja do Ramada;
- Loja Portal;
- Elegância Moda e Acessórios;
- Akazzo;
- Pet House.

Objetivo: decidir presença operacional e identidade jurídica suficiente para inclusão/exclusão provisória.

Depois:
- atualizar universo candidato para v003;
- atualizar fila para v003;
- somente quando P0 = 0, revisar P1 que podem alterar storefronts;
- então decidir se é possível iniciar primeiro recálculo exploratório com cenário-base + faixa de incerteza.

## 8. Regras metodológicas que permanecem válidas

- Não transformar CNPJ em loja física automaticamente.
- Não transformar raiz em market share.
- Não somar filiais externas ao mercado municipal.
- Não excluir marca apenas porque CNPJ histórico foi baixado.
- Não incluir candidato de marca/CNPJ sem vínculo documental suficiente.
- Não municipalizar dados de COREDE/região.
- Separar dado observado, cálculo, interpretação e decisão provisória.
- Toda escrita deve continuar em pequenos blocos verificáveis, com CSV + análise + Drive.

## 9. Estado no Drive

Planilha:
`Matriz de fontes exploratórias — Receita Estadual + Fecomércio — v001 — 20260917`

ID:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Abas relevantes:
- `BNE_validacao`;
- `BNE_fechamento_103`;
- `BNE_cnpjs_adic_subst`;
- `BNE_cnpjs_adic_v002`;
- `BNE_universo_candidato`;
- `BNE_universo_v002`;
- `BNE_fila_reconciliacao`;
- `BNE_fila_v002`.

## 10. Ponto de retomada

**Retomar diretamente pelos 13 P0 remanescentes, começando pelo lote 20. Não repetir auditorias anteriores e não recalcular ainda a oferta.**
