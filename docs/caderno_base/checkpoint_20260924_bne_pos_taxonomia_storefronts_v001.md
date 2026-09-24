# CHECKPOINT — São Borja — Inteligência Mercadológica
## Bens não essenciais — P0/P1 fechados, storefronts e taxonomia harmonizada
**Data:** 24/09/2026

## 1. Governança

- Branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- PR #41: **aberto, draft e sem merge**.
- Caderno-Base Territorial: **v028 read-only**.
- Nenhum resultado exploratório abaixo foi promovido ao Caderno-Base.
- Storefront não equivale a CNPJ, raiz econômica, faturamento ou market share.

## 2. Nota de continuidade

A retomada solicitada apontava para:
`docs/caderno_base/checkpoint_20260924_bne_pos_lote19_p0_v002.md`.

Ao auditar a branch e a planilha do Drive antes de escrever, foi constatado que a trilha já havia avançado além desse checkpoint. Para não repetir auditorias concluídas, a continuidade foi feita a partir do estado efetivamente mais recente.

## 3. Fechamento P0 já existente na branch

### Lote 20
- Loja Portal: CNPJ `17.705.834/0001-03`, P0 resolvido.
- Elegância Moda e Acessórios: CNPJ `11.496.172/0001-14`, P0 resolvido.
- 7 Povos Kids: conflito preservado.
- Marlin Fashion: CNPJ histórico/inapto, presença operacional ainda separada da regularidade.
- Bicho Mimado: presença operacional mantida, identidade jurídica corrente pendente.

### Lote 21
Separação metodológica entre:
- presença operacional/mercadológica;
- situação/identidade jurídica.

Marlin, Mundi, Ciranda, Bicho Mimado, Pet House e Ponto dos Pets deixaram de bloquear o cenário-base por presença operacional suficientemente demonstrada, com pendências jurídicas rebaixadas.

### Lote 22
Pimentas Boutique Sensual, CHICMI, Loja do Ramada e Akazzo foram excluídas do cenário-base exploratório por ausência de evidência atual suficiente, preservadas como histórico/sensibilidade.

### Lote 23
7 Povos Kids foi incluída no cenário-base exploratório com sensibilidade conservadora sem a unidade.

**Estado após lote 23: P0 = 0.**

## 4. Fechamento P1 já existente na branch

Os lotes P1 23–25 resolveram os bloqueios que ainda podiam alterar diretamente o número de storefronts.

Destaques:
- correção da duplicidade Quero-Quero;
- quatro storefronts Grazziotin adicionais confirmados;
- Brasil Free Shop `/0011-58` confirmado como storefront adicional;
- Requinte/José Altamir `/0002-56` confirmado como storefront distinto, marca de fachada pendente;
- Lins Ferrão desdobrado em Gang `/0122-14` e Pompéia `/0033-04`;
- sucessões/continuidade operacional tratadas sem afirmar sucessão jurídica formal;
- operações com presença atual e CNPJ pendente deixaram de bloquear o denominador.

Fila corrente v008:
- P0: **0**;
- P1: **0**;
- P2: **33**;
- P3: **36**;
- P4: **71**;
- total: **140 registros de controle**.

## 5. Storefronts reconciliados

Artefato:
`docs/caderno_base/analise_bens_nao_essenciais_storefronts_reconciliados_20260924_v001.md`

Cálculo:
- 120 linhas originais;
- 115 mantidas no cenário-base;
- 5 excluídas do cenário-base;
- 7 storefronts adicionais comprovados.

Fórmula:
`storefronts_base = 115 + 7 = 122`.

Sensibilidade conservadora:
`122 - 1 (7 Povos Kids) = 121`.

Faixa exploratória corrente:
**121–122 storefronts**.

Não interpretar a diferença em relação às 120 linhas originais como crescimento temporal.

## 6. Bloco novo concluído nesta retomada — classificação dos adicionais

Artefatos:
- `docs/data_sources/bens_nao_essenciais_classificacao_storefronts_adicionais_20260924_v001.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_classificacao_storefronts_adicionais_20260924_v001.md`.

Resultado:
- 7/7 storefronts adicionais classificados;
- Tottal Casa & Lazer → `CASA_UTILIDADES_LAZER`;
- Por Menos /0121 → `MODA_VESTUARIO_ACESSORIOS`;
- Tech Box → `OPTICA`;
- Pormenos /0451 → `MODA_VESTUARIO_ACESSORIOS`;
- Brasil Free Shop /0011 → `LOJA_FRANCA_VAREJO_MISTO`;
- José Altamir /0002 → `MODA_VESTUARIO_ACESSORIOS`;
- Pompéia /0033 → `MODA_VESTUARIO_ACESSORIOS`.

A classificação não altera o denominador.

## 7. Bloco novo concluído — taxonomia harmonizada

Artefatos:
- `docs/data_sources/bens_nao_essenciais_taxonomia_harmonizada_20260924_v001.csv`;
- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v002.csv`;
- `docs/data_sources/bens_nao_essenciais_subcategorias_exploratorias_20260924_v001.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_taxonomia_subcategorias_20260924_v001.md`.

A taxonomia preserva os rótulos originais e adiciona um `grupo_analitico_harmonizado`.

Casos explicitamente multissegmento foram mantidos em `MISTO_MULTISSEGMENTO` para evitar uma primazia arbitrária.

### Distribuição calculada — cenário-base de 122 storefronts

- MODA_CALCADOS_ACESSORIOS: 57 — 46,72%;
- PET_VETERINARIA_AGRO: 20 — 16,39%;
- JOALHERIA_OPTICA_RELOJOARIA: 12 — 9,84%;
- CASA_UTILIDADES_PRESENTES_DECORACAO: 7 — 5,74%;
- ELETRODOMESTICOS_AUDIO_VIDEO: 7 — 5,74%;
- MISTO_MULTISSEGMENTO: 5 — 4,10%;
- LOJA_FRANCA_DUTY_FREE: 3 — 2,46%;
- ARMARINHO_TECIDOS: 2 — 1,64%;
- DEPARTAMENTOS_MAGAZINES: 2 — 1,64%;
- FERRAGENS_MATERIAIS_ELETRICOS: 2 — 1,64%;
- PAPELARIA: 2 — 1,64%;
- ACESSORIOS_DISPOSITIVOS_MOVEIS: 1 — 0,82%;
- ARTIGOS_MILITARES: 1 — 0,82%;
- MOVEIS: 1 — 0,82%.

A sensibilidade conservadora altera apenas MODA_CALCADOS_ACESSORIOS: 57 → 56, porque retira 7 Povos Kids.

## 8. Drive sincronizado

Planilha:
`Matriz de fontes exploratórias — Receita Estadual + Fecomércio — v001 — 20260917`

ID:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Novas abas verificadas:
- `BNE_classif_add_v001`;
- `BNE_taxonomia_v001`;
- `BNE_storefronts_v002`;
- `BNE_subcategorias_v001`.

## 9. Limitações ativas

- distribuição por grupo mede unidades, não receita ou market share;
- CNPJ/raiz não é automaticamente storefront;
- há operações com identidade jurídica corrente ainda P2;
- a taxonomia harmonizada é analítica, não classificação oficial CNAE;
- lojas multissegmento não devem ser forçadas para uma única categoria quando a evidência não permite;
- não há série histórica homogênea de storefronts para inferir crescimento/declínio temporal.

## 10. Próximo passo exato

Consolidar os 122 storefronts por operador/raiz econômica, com cuidado especial para:

- Grazziotin;
- Brasil Free Shop;
- Quero-Quero;
- Becker;
- Lins Ferrão — corrigindo a leitura de `/0122-14` como Gang e `/0033-04` como Pompéia;
- José Altamir/Requinte;
- Rogéria Tatiane Machado Loureiro — Lolita/Volúpia;
- Companhia dos Bichos.

Depois calcular apenas **concentração em participação de unidades**, explicitamente distinta de market share de faturamento.

O próximo bloco deve preservar operadores sem CNPJ/raiz corrente como chaves sintéticas individuais, sem atribuir vínculo econômico não demonstrado.
