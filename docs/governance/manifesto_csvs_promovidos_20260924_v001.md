# Manifesto de CSVs promovidos — pacote de publicação SBMI
**Data:** 24/09/2026  
**Projeto:** São Borja — Inteligência Mercadológica  
**Escopo:** somente CSVs que sustentam diretamente a publicação corrente ou controles técnicos promovidos.

## 1. Regra de promoção

Um CSV só entra neste manifesto quando cumpre pelo menos uma das funções abaixo:

1. **PROMOVIDO_PUBLICACAO** — base corrente usada diretamente em report, factsheet, storyboard, painel ou síntese;
2. **PROMOVIDO_AUDITORIA** — controle técnico necessário para sustentar uma conclusão publicada, mas inadequado como headline.

Arquivos de triagem, lotes intermediários, probes, filas históricas, versões substituídas e derivados exploratórios permanecem no repositório para rastreabilidade, mas **não integram o conjunto promovido de publicação**.

A promoção não altera a natureza do dado. Em particular:
- storefront ≠ CNPJ ≠ raiz econômica ≠ market share;
- registro CNES ≠ censo mercadológico;
- optante SINAC/SIMEI ≠ empresa ativa ou ponto físico;
- índice de concentração em unidades ≠ HHI de market share;
- REGIC ≠ gasto.

## 2. CSVs promovidos

| Domínio | Arquivo | Status | Papel | SHA Git | Uso principal | Limitação central |
|---|---|---|---|---|---|---|
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v003.csv | PROMOVIDO_PUBLICACAO | Base estrutural canônica | 9d3b1542b0ce6f977613bba6596fe862365953af | 122 storefronts base / 121 sensibilidade | Não é censo oficial; 120→122 não é crescimento |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_taxonomia_harmonizada_20260924_v001.csv | PROMOVIDO_PUBLICACAO | Taxonomia canônica | 793b252637a99108a8cd3b7df77692aff96dbd70 | Estrutura por grupo — moda, pet, joalheria, eletro etc. | Categoria analítica SBMI; não nomenclatura CNAE oficial |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_operadores_raizes_20260924_v001.csv | PROMOVIDO_PUBLICACAO | Estrutura de operadores | e1731b337c2f91a94300e3078e40cc79a726f69e | 109 operator_keys; consolidação por raiz quando suportada | Raiz econômica não é market share |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_raizes_multiunidade_20260924_v001.csv | PROMOVIDO_PUBLICACAO | Subconjunto multiunidade | 547db96b641da38de3765ee181bffca253ca52fe | 8 raízes / 21 storefronts | Participação em unidades ≠ concentração econômica |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.csv | PROMOVIDO_PUBLICACAO | Estrutura por grupo | 4a6122a590cea0cd91da64d243909ae73874d7c9 | Diagnóstico por submercado | Não é participação de vendas |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_integracao_oferta_demanda_20260924_v001.csv | PROMOVIDO_PUBLICACAO | Crosswalk oferta × demanda | ca8014c46797b2e4d0c9d6d92f8727b3197383be | POM/REGIC; 64/122 = 52,46% de cobertura temática direta usada | REGIC ≠ gasto; não estender aos demais grupos |
| Bens Não Essenciais | docs/data_sources/bens_nao_essenciais_concentracao_unidades_20260924_v001.csv | PROMOVIDO_AUDITORIA | Controle descritivo de unidades | a32725a65cfaae47705c17e5d29b960a1b605acb | Auditoria da dispersão de unidades por operator_key | NÃO é HHI de market share; não usar limiares antitruste |
| Saúde/Higiene | docs/data_sources/farmacias_cnes_pom_crosswalk_20260922_v001.csv | PROMOVIDO_PUBLICACAO | Base CNES/crosswalk corrente | e4aba6935483e17e8a62a9326897bd01348c4ba1 | 23 registros/CNPJs, 7 raízes, arquitetura multiunidade | CNES ≠ situação RFB/market share; Agafarma sinaliza possível subcobertura |
| Serviços | docs/data_sources/sinac_simei_services_structure_20260920_v001.csv | PROMOVIDO_PUBLICACAO | Estrutura formal do recorte POM/CNAE | 146985d5ca8e901d929efdc0a8408499e911ea1b | 947 SINAC / 728 SIMEI por submercado | Optante ≠ empresa ativa, ponto físico, faturamento ou market share |

## 3. Domínios sem CSV final promovido nesta edição

### Bens essenciais

O benchmark de demanda, a base corrente 54/52 e as missões de compra estão canonizados no Caderno-Base Territorial v029, na planilha técnica v029 e no Caderno Setorial de Bens Essenciais v002.

O arquivo bens_essenciais_network_roots_20260920_v001.csv permanece útil como controle anterior de estrutura por raiz, mas **não é promovido como base final de publicação** porque não representa sozinho o universo corrente 54/52 nem sustenta o benchmark monetário.

### Alimentação fora do lar / PNAE

O conjunto corrente publicado combina RFB CNAE 56, POM n=153, pagamentos CNPJ auditados do PNAE e contratos de agricultura/agroindústria familiar. Esses universos estão preservados na planilha técnica setorial e no Caderno-Base v029. Nenhum CSV top-level único foi promovido como substituto desse conjunto porque contrato, pagamento, cadastro e survey são unidades conceitualmente distintas.

## 4. Famílias explicitamente não promovidas como publicação corrente

Permanecem apenas como histórico/auditoria, salvo nova decisão documentada:
- lotes bens_nao_essenciais_revalidacao_*;
- filas bens_nao_essenciais_fila_reconciliacao_final_*;
- universos candidatos bens_nao_essenciais_universo_candidato_reconciliado_*;
- saude_higiene_network_roots_20260920_v001.csv, anterior à camada CNES corrente;
- sinac_simei_pom_market_summary_20260920_v001.csv, porque agrega macro-recortes que não substituem as estruturas finais específicas de cada caderno;
- analise_multissetorial_territorial_20260918_v001.csv e arquiteturas_competitivas_pom_20260918_v001.csv, preservados como análises intermediárias anteriores à integração v029.

## 5. Camada técnica correspondente

Planilha v029: 1CHn1JZ-IcDxG3V9M5y0PKvN5lTkcvlVcov_vVw3je3c

Aba: Manifesto_CSVs_v029

O manifesto registra, por arquivo: domínio; caminho; versão/data; status de promoção; papel; fonte/conceito; período; geografia; unidade; SHA Git; tamanho; limitação; uso corrente.

## 6. Governança

- Caderno-Base v028 permanece read-only;
- Caderno-Base v029 é a base corrente de integração;
- arquivos exploratórios não são apagados, apenas não promovidos;
- PR #41 permanece aberto, draft e sem merge;
- nenhum arquivo deve ser elevado a canônico/publicável sem rastreabilidade conceitual e decisão documentada.