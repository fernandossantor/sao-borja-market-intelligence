# CHECKPOINT — São Borja — Inteligência Mercadológica
## Bens não essenciais — pós-integração oferta, operadores e Caderno Setorial v002
**Data:** 24/09/2026

## 1. Governança

- Branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- PR #41: **deve permanecer aberto, draft e sem merge** até autorização explícita.
- Caderno-Base Territorial v028: **read-only**; não foi alterado nesta etapa.
- O Caderno Setorial BNE v001 foi preservado.
- A atualização editorial ocorreu em uma cópia v002.
- Nenhum resultado exploratório foi promovido automaticamente a indicador canônico.

## 2. Estado dos bloqueios BNE

Fila reconciliada v008:

- P0: **0**;
- P1: **0**;
- P2: 33;
- P3: 36;
- P4: 71;
- total: **140 registros de controle**.

### 7 Povos Kids

- cenário-base: incluída;
- sensibilidade conservadora: excluída;
- pendência: confirmação cadastral oficial direta.

A diferença entre os cenários permanece limitada a essa unidade.

## 3. Oferta física reconciliada

### Cenário-base

- 122 storefronts.

### Sensibilidade conservadora

- 121 storefronts.

### Composição do cenário-base

- 120 linhas originais do inventário;
- 115 mantidas no cenário-base;
- 5 excluídas;
- 7 storefronts adicionais comprovados.

Fórmula:

`115 + 7 = 122 storefronts`

Regra crítica:

**120 → 122 não representa crescimento temporal.**

A diferença decorre de reconciliação, exclusões, correções e identificação de unidades adicionais.

## 4. Taxonomia harmonizada

Distribuição calculada no cenário-base:

- `MODA_CALCADOS_ACESSORIOS`: 57 — 46,72%;
- `PET_VETERINARIA_AGRO`: 20 — 16,39%;
- `JOALHERIA_OPTICA_RELOJOARIA`: 12 — 9,84%;
- `CASA_UTILIDADES_PRESENTES_DECORACAO`: 7 — 5,74%;
- `ELETRODOMESTICOS_AUDIO_VIDEO`: 7 — 5,74%;
- `MISTO_MULTISSEGMENTO`: 5 — 4,10%;
- `LOJA_FRANCA_DUTY_FREE`: 3 — 2,46%;
- `ARMARINHO_TECIDOS`: 2 — 1,64%;
- `DEPARTAMENTOS_MAGAZINES`: 2 — 1,64%;
- `FERRAGENS_MATERIAIS_ELETRICOS`: 2 — 1,64%;
- `PAPELARIA`: 2 — 1,64%;
- `ACESSORIOS_DISPOSITIVOS_MOVEIS`: 1 — 0,82%;
- `ARTIGOS_MILITARES`: 1 — 0,82%;
- `MOVEIS`: 1 — 0,82%.

A taxonomia é **analítica**, não classificação oficial CNAE.

## 5. Consolidação por operadores e raízes

Regra corrente:

1. quando existe CNPJ de referência reconciliado e raiz de oito dígitos:
   `operator_key = RAIZ_<raiz>`;
2. quando a identidade jurídica corrente permanece pendente:
   `operator_key = OPERACAO_<storefront_id>`;
3. não atribuir vínculo econômico sem evidência;
4. não converter automaticamente CNPJ em storefront ou vice-versa.

### Resultado do cenário-base

- 122 storefronts;
- 109 `operator_keys`;
- 8 raízes/chaves com mais de um storefront;
- 21 storefronts nessas raízes;
- 17,21% das unidades em raízes multi-storefront;
- 101 `operator_keys` com apenas um storefront.

### Raízes multiunidade

- Grupo Grazziotin: 6 storefronts — 4,92%;
- Brasil Free Shop: 3 — 2,46%;
- Lojas Becker: 2 — 1,64%;
- Cia dos Bichos: 2 — 1,64%;
- Rogéria Tatiane Machado Loureiro: 2 — 1,64%;
- Lins Ferrão: 2 — 1,64%;
- José Altamir Silveira da Rosa Ltda: 2 — 1,64%;
- Lojas Quero-Quero: 2 — 1,64%.

### Correção Lins Ferrão

Preservar explicitamente:

- `87.345.021/0122-14` = **Gang**;
- `87.345.021/0033-04` = **Lojas Pompéia**.

São dois storefronts distintos sob a mesma raiz.

## 6. Concentração em participação de unidades

Métrica descritiva:

`HHI_unidades = Σ (100 × unidades_i / total)^2`

Resultados:

- cenário-base: **114,22**;
- sensibilidade conservadora: **115,43**.

Duas maiores raízes:

`(6 + 3) / 122 × 100 = 7,38%`

### Limite metodológico

Este HHI é apenas uma medida de dispersão dos storefronts por `operator_key`.

**Não é HHI de market share.**

Não comparar mecanicamente com limiares concorrenciais/antitruste.

## 7. Estrutura por grupo mercadológico

### Moda, calçados e acessórios

- 57 storefronts;
- 51 `operator_keys`;
- 4 raízes multiunidade dentro do grupo;
- 10 storefronts nessas raízes;
- 17,54% das unidades do grupo em raízes multiunidade;
- maior raiz: Grupo Grazziotin, 4 unidades — 7,02%.

### Pet, veterinária e agro

- 20 storefronts;
- 19 `operator_keys`;
- 1 raiz multiunidade;
- 2 unidades nessa raiz — 10,00%.

### Joalheria, óptica e relojoaria

- 12 storefronts;
- 12 `operator_keys`;
- nenhuma raiz multiunidade dentro do grupo.

### Eletrodomésticos, áudio e vídeo

- 7 storefronts;
- 5 `operator_keys`;
- 2 raízes multiunidade;
- 4 unidades nessas raízes;
- 57,14% das unidades do grupo em raízes multiunidade.

### Loja franca / duty free

- 3 storefronts;
- 1 `operator_key`;
- 100% das unidades documentadas da categoria sob a mesma raiz Brasil Free Shop.

Isso descreve estrutura em unidades, não captura monetária.

## 8. Integração oferta × demanda/comportamento

Fontes de demanda/comportamento:

- POM 2026 — 10 entrevistas semiestruturadas;
- REGIC 2018 — Q1 e Q2;
- Caderno Setorial BNE v001;
- planilha setorial v001.

### Regra de comparabilidade

POM:

- uso qualitativo;
- não generalizar percentuais à população;
- usar relatos como mecanismos/indícios.

REGIC:

- Q1 possui correspondência direta com moda/calçados;
- Q2 possui correspondência direta com eletrodomésticos/eletrônicos e móveis;
- casa/utilidades possui correspondência apenas parcial;
- não aplicar REGIC diretamente a pet, joalheria, papelaria, duty free ou nichos sem correspondência temática.

### Cobertura direta REGIC

Moda/calçados + eletrodomésticos/áudio-vídeo:

`57 + 7 = 64 storefronts`

`64 / 122 × 100 = 52,46%`

Portanto:

**52,46% dos storefronts do cenário-base pertencem aos dois grandes grupos com correspondência temática direta limpa aos recortes Q1/Q2 usados no caderno.**

Os 47,54% restantes não devem receber automaticamente a mesma leitura territorial.

## 9. Diagnóstico integrado corrente

### Moda

- maior bloco físico;
- oferta pulverizada;
- presença de algumas raízes multimarca;
- concorrência local + territorial + digital;
- POM sustenta preço/variedade online, busca digital, experimentação, imediatismo, troca e crediário.

### Eletrodomésticos

- poucos storefronts em termos absolutos;
- maior presença proporcional de redes multiunidade;
- aderência direta ao REGIC Q2;
- competição envolve redes, plataformas, crédito, disponibilidade e logística.

### Pet/agro

- segundo maior grupo em número de storefronts;
- elevada pulverização em operadores;
- cobertura local específica de demanda ainda insuficiente.

Principal lacuna:
frequência, gasto, recorrência, mix pet×agro, canal e sensibilidade a preço.

### Joalheria/óptica/relojoaria

- 12 storefronts;
- estrutura totalmente pulverizada em chaves de um ponto;
- demanda local específica não observada com detalhe suficiente.

### Duty free

- 3 storefronts;
- 1 raiz;
- forte concentração em unidades dentro do recorte;
- nenhuma base atual permite converter isso em market share ou gasto transfronteiriço.

## 10. Delta editorial concluído

Artefatos:

- `docs/data_sources/bens_nao_essenciais_delta_editorial_caderno_v001_20260924.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_delta_editorial_caderno_20260924_v001.md`.

Conclusão:

- nenhuma tese central do caderno v001 precisou ser retirada;
- a nova oferta exige maior precisão e estratificação;
- principais mudanças:
  - adicionar oferta reconciliada;
  - separar submercados;
  - restringir REGIC aos grupos comparáveis;
  - reforçar que unidades não equivalem a market share;
  - priorizar recomendações por grupo.

## 11. Caderno Setorial BNE v002

### Documento narrativo

Título:

**Caderno Setorial — Bens Não Essenciais — Diagnóstico v002 — oferta reconciliada — 20260924**

Drive ID:

`1gNCKoKPj2SECZf3ocNhiXorftSoQgfqDTAbo-_U0e9A`

O v001 original foi preservado.

O v002 recebeu blocos novos em:

- estrutura empresarial/oferta;
- diagnóstico por grupo;
- limites metodológicos;
- free shops;
- papelarias;
- mercado pet/agro.

### Planilha técnica v002

Título:

`caderno_setorial_bens_nao_essenciais_v002_oferta_reconciliada_20260924`

Drive ID:

`1BiHO31FJTpt9jZUM5wIIKL78QOKG0QBeHcc6W4G0oTk`

Novas abas:

- `Oferta_reconciliada_20260924`;
- `Taxonomia_20260924`;
- `Operadores_20260924`;
- `Estrutura_grupos_20260924`;
- `Oferta_demanda_20260924`;
- `Delta_editorial_20260924`.

Também foram atualizados:

- `Sumario`;
- `Fontes_controle`.

## 12. Matriz exploratória no Drive

Planilha:

`Matriz de fontes exploratórias — Receita Estadual + Fecomércio — v001 — 20260917`

Drive ID:

`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Abas novas/atualizadas desta etapa:

- `BNE_classif_add_v001`;
- `BNE_taxonomia_v001`;
- `BNE_storefronts_v002`;
- `BNE_subcategorias_v001`;
- `BNE_storefronts_v003`;
- `BNE_operadores_v001`;
- `BNE_concentracao_v001`;
- `BNE_raizes_multi_v001`;
- `BNE_estrutura_grupos_v001`;
- `BNE_oferta_demanda_v001`;
- `BNE_delta_editorial_v001`.

## 13. Artefatos GitHub correntes

### Storefronts e taxonomia

- `docs/data_sources/bens_nao_essenciais_classificacao_storefronts_adicionais_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_taxonomia_harmonizada_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v002.csv`
- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v003.csv`
- `docs/data_sources/bens_nao_essenciais_subcategorias_exploratorias_20260924_v001.csv`

### Operadores e concentração

- `docs/data_sources/bens_nao_essenciais_operadores_raizes_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_concentracao_unidades_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_raizes_multiunidade_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.csv`

### Oferta × demanda e editorial

- `docs/data_sources/bens_nao_essenciais_integracao_oferta_demanda_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_delta_editorial_caderno_v001_20260924.csv`

### Documentação

- `docs/caderno_base/analise_bens_nao_essenciais_classificacao_storefronts_adicionais_20260924_v001.md`
- `docs/caderno_base/analise_bens_nao_essenciais_taxonomia_subcategorias_20260924_v001.md`
- `docs/caderno_base/analise_bens_nao_essenciais_operadores_concentracao_unidades_20260924_v001.md`
- `docs/caderno_base/analise_bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.md`
- `docs/caderno_base/analise_bens_nao_essenciais_integracao_oferta_demanda_20260924_v001.md`
- `docs/caderno_base/analise_bens_nao_essenciais_delta_editorial_caderno_20260924_v001.md`

## 14. Limitações ativas

Não é possível concluir com a base corrente:

- market share;
- faturamento por empresa/rede;
- gasto por categoria;
- gasto em e-commerce;
- gasto em outros municípios;
- gasto em free shops;
- retenção/vazamento monetário;
- ticket médio;
- elasticidade-preço;
- causalidade entre número de lojas e desempenho;
- crescimento temporal da oferta a partir de 120 → 122.

Também preservar:

- POM n=10 ≠ população;
- REGIC ≠ gasto;
- storefront ≠ CNPJ;
- CNPJ ≠ raiz econômica;
- raiz econômica ≠ market share;
- participação em unidades ≠ poder de mercado.

## 15. Próximo passo exato

Retomar pela **revisão editorial integral do Caderno Setorial BNE v002**, sem editar o Caderno-Base v028.

Ordem sugerida:

1. revisar o Resumo Executivo;
2. revisar seções 7, 17, 18 e 19 para substituir uma leitura homogênea de BNE por arquitetura de submercados;
3. atualizar o quadro de decisões empresariais por grupo;
4. incorporar os novos números à rastreabilidade;
5. conferir se toda nova métrica possui:
   - fonte;
   - período;
   - unidade;
   - abrangência;
   - natureza;
   - limitação;
6. conferir que nenhuma formulação sugira:
   - crescimento temporal;
   - market share;
   - causalidade;
   - representatividade populacional do POM;
7. somente após essa revisão decidir se o v002 pode ser promovido como versão setorial corrente.

## 16. Regra de retomada

Na próxima sessão, começar por:

**`docs/caderno_base/checkpoint_20260924_bne_pos_integracao_caderno_v002_v001.md`**

e seguir diretamente pela revisão editorial do Caderno Setorial BNE v002.

Não reabrir P0/P1 salvo aparecimento de nova evidência documental contraditória.
