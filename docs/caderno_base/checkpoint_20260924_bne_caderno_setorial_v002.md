# CHECKPOINT — São Borja — Inteligência Mercadológica
## Bens não essenciais — oferta reconciliada, operadores e Caderno Setorial v002
**Data:** 24/09/2026

## 1. Governança

- Branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- PR #41: deve permanecer **aberto, draft e sem merge**.
- Caderno-Base Territorial v028: **read-only**; não foi editado nesta etapa.
- O Caderno Setorial BNE v001 foi preservado e uma cópia v002 foi criada para atualização.
- Nenhuma participação em unidades deve ser interpretada como market share.

## 2. Estado dos bloqueios BNE

Fila reconciliada v008:
- P0: **0**;
- P1: **0**;
- P2: 33;
- P3: 36;
- P4: 71;
- total: 140 registros de controle.

7 Povos Kids:
- cenário-base: incluída;
- sensibilidade conservadora: excluída;
- pendência: confirmação cadastral oficial direta.

## 3. Oferta física reconciliada

Cenário-base:
- 122 storefronts.

Sensibilidade conservadora:
- 121 storefronts.

Composição do cenário-base:
- 115 linhas originais mantidas;
- 5 linhas originais excluídas;
- 7 storefronts adicionais comprovados.

A diferença 120 → 122 **não representa crescimento temporal**.

## 4. Taxonomia harmonizada

Distribuição do cenário-base:
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

Taxonomia = classificação analítica, não CNAE oficial.

## 5. Consolidação por operadores/raízes

Regra:
- CNPJ de referência + raiz reconciliada → `RAIZ_<8 dígitos>`;
- identidade jurídica corrente pendente → chave sintética individual `OPERACAO_<storefront_id>`.

Cenário-base:
- 122 storefronts;
- 109 operator_keys;
- 8 raízes/chaves com mais de um storefront;
- 21 storefronts nessas raízes;
- 17,21% das unidades em raízes multi-storefront;
- 101 operator_keys com apenas um storefront.

Raízes multiunidade:
- Grupo Grazziotin: 6 storefronts — 4,92%;
- Brasil Free Shop: 3 — 2,46%;
- Lojas Becker: 2 — 1,64%;
- Cia dos Bichos: 2 — 1,64%;
- Rogéria Tatiane Machado Loureiro: 2 — 1,64%;
- Lins Ferrão: 2 — 1,64%;
- José Altamir Silveira da Rosa Ltda: 2 — 1,64%;
- Lojas Quero-Quero: 2 — 1,64%.

Correção Lins Ferrão:
- `87.345.021/0122-14` = Gang;
- `87.345.021/0033-04` = Lojas Pompéia.

## 6. Concentração em unidades

Métrica descritiva:
`HHI_unidades = Σ(100 × unidades_i / total)^2`.

Resultados:
- cenário-base: 114,22;
- sensibilidade: 115,43.

**Limite:** HHI de unidades não é HHI de market share e não deve ser comparado mecanicamente com limiares antitruste.

Duas maiores raízes em unidades:
- 9/122 = 7,38%.

## 7. Estrutura por grupo

### Moda
- 57 storefronts;
- 51 operator_keys;
- 4 raízes multiunidade no grupo;
- 10 unidades nessas raízes;
- 17,54% das unidades em raízes multiunidade;
- maior raiz: Grazziotin, 4 unidades = 7,02%.

### Pet/veterinária/agro
- 20 storefronts;
- 19 operator_keys;
- 1 raiz multiunidade;
- 2 unidades nessa raiz = 10,00%.

### Eletrodomésticos/áudio/vídeo
- 7 storefronts;
- 5 operator_keys;
- 2 raízes multiunidade;
- 4 unidades nessas raízes = 57,14%.

### Loja franca/duty free
- 3 storefronts;
- 1 operator_key;
- 100% das unidades sob a mesma raiz Brasil Free Shop.

## 8. Integração oferta × demanda

Fontes:
- POM 2026 — n=10 qualitativo;
- REGIC 2018 Q1/Q2;
- Caderno Setorial BNE v001.

Resultado metodológico:
- MODA_CALCADOS_ACESSORIOS ↔ REGIC Q1: correspondência direta;
- ELETRODOMESTICOS_AUDIO_VIDEO ↔ REGIC Q2: correspondência direta;
- MOVEIS ↔ REGIC Q2: correspondência direta;
- CASA_UTILIDADES_PRESENTES_DECORACAO ↔ Q2: apenas parcial.

Moda + eletro:
- 57 + 7 = 64 storefronts;
- 64/122 = **52,46%** do cenário-base em dois grandes grupos com correspondência REGIC direta limpa.

Não estender automaticamente REGIC aos 47,54% restantes.

Diagnóstico:
- moda: maior bloco físico + pulverização + concorrência digital/territorial;
- eletro: maior peso proporcional de redes;
- pet/agro: segundo maior bloco de oferta, mas demanda local específica pouco documentada;
- joalheria/óptica: oferta relevante e pulverizada, demanda local específica insuficiente;
- duty free: estrutura concentrada em uma raiz, sem informação de captura monetária.

## 9. Delta editorial

Artefatos:
- `docs/data_sources/bens_nao_essenciais_delta_editorial_caderno_v001_20260924.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_delta_editorial_caderno_20260924_v001.md`.

Conclusão:
- nenhuma tese central do caderno v001 precisa ser retirada;
- principais mudanças: adicionar oferta reconciliada, estratificar por grupo, restringir REGIC ao escopo diretamente comparável e reforçar que participação em unidades não é market share.

## 10. Caderno Setorial BNE v002

O v001 foi preservado.

Novo documento narrativo:
**Caderno Setorial — Bens Não Essenciais — Diagnóstico v002 — oferta reconciliada — 20260924**

Drive ID:
`1gNCKoKPj2SECZf3ocNhiXorftSoQgfqDTAbo-_U0e9A`

Nova planilha técnica:
`caderno_setorial_bens_nao_essenciais_v002_oferta_reconciliada_20260924`

Drive ID:
`1BiHO31FJTpt9jZUM5wIIKL78QOKG0QBeHcc6W4G0oTk`

O documento v002 recebeu blocos de atualização em:
- estrutura empresarial/oferta;
- diagnóstico por grupo;
- limites metodológicos;
- free shops;
- papelarias;
- pet/agro.

A planilha v002 recebeu:
- `Oferta_reconciliada_20260924`;
- `Taxonomia_20260924`;
- `Operadores_20260924`;
- `Estrutura_grupos_20260924`;
- `Oferta_demanda_20260924`;
- `Delta_editorial_20260924`.

O `Sumario` e `Fontes_controle` foram atualizados.

## 11. Artefatos GitHub novos desta etapa

- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v003.csv`
- `docs/data_sources/bens_nao_essenciais_operadores_raizes_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_concentracao_unidades_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_raizes_multiunidade_20260924_v001.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_operadores_concentracao_unidades_20260924_v001.md`
- `docs/data_sources/bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.md`
- `docs/data_sources/bens_nao_essenciais_integracao_oferta_demanda_20260924_v001.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_integracao_oferta_demanda_20260924_v001.md`
- `docs/data_sources/bens_nao_essenciais_delta_editorial_caderno_v001_20260924.csv`
- `docs/caderno_base/analise_bens_nao_essenciais_delta_editorial_caderno_20260924_v001.md`

## 12. Estado no Drive — matriz exploratória

ID:
`1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

Novas abas:
- `BNE_storefronts_v003`;
- `BNE_operadores_v001`;
- `BNE_concentracao_v001`;
- `BNE_raizes_multi_v001`;
- `BNE_estrutura_grupos_v001`;
- `BNE_oferta_demanda_v001`;
- `BNE_delta_editorial_v001`.

## 13. Próximo passo exato

Fazer uma **revisão editorial integral do Caderno Setorial BNE v002**, com foco em:

1. atualizar o Resumo Executivo para incorporar a oferta reconciliada sem sobrecarregar o texto;
2. substituir a ideia de um mercado BNE homogêneo por uma arquitetura de submercados;
3. ajustar o quadro de decisões empresariais por grupo;
4. verificar referências e rastreabilidade dos novos números;
5. manter explícitos os limites:
   - unidades ≠ market share;
   - POM n=10 ≠ percentuais populacionais;
   - REGIC Q1/Q2 ≠ gasto;
   - nenhuma inferência de crescimento 120 → 122;
6. somente depois avaliar se o v002 está pronto para ser promovido como nova versão setorial corrente.

Não editar o Caderno-Base v028 durante essa etapa.
