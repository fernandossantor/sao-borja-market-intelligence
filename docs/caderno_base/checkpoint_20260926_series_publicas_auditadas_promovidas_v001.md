# Checkpoint — séries públicas auditadas e promovidas — v001

**Data:** 2026-09-26  
**Branch:** `feature/cnpj-territorial-control-v1`  
**PR:** #41 — manter **OPEN / DRAFT / UNMERGED**

## Estado concluído

O download iniciado no checkpoint `checkpoint_20260926_inicio_download_series_publicas_v001.md` foi auditado integralmente.

O run originalmente indicado, `36276217961`, concluiu com sucesso técnico, mas seu derivado DFe CNAE apresentou erro de parsing de datas ISO. Ele foi rejeitado como fonte canônica.

A rotina foi corrigida e reexecutada. O pacote canônico passa a ser:

- run: `36277254947`;
- commit: `88528db86652607379a5f7f76003d97552e90fbf`;
- artifact: `10917538784`;
- digest: `sha256:c2c202561d00d516b56a6fb760c9adbbbcd68d1619d6f68928b0b3d8e11430d1`;
- warnings de parsing no job final: 0.

## Google Drive

Promoção realizada em:

- pasta: `exports/public-market-series-v001-20260926`;
- folder ID: `1jDfPKy6IpnHsBf82XWcifhZtQT7kd602`;
- arquivo: `SBMI_public_market_series_v001_GitHubActions_audited_20260926.zip`;
- file ID: `1a_lJ_3IGSDocYWAxNnsPYU5KYyFcxcIg`.

A planilha corrente `caderno_base_territorial_v029_integracao_setorial_v002_20260924` foi atualizada na aba `Rastreabilidade_v029`.

## Cobertura auditada

- Radar Composição de Mercado/RS: 2024-07 a 2026-08;
- Radar Exportações NCM/RS: 2024-07 a 2026-08;
- Radar Portfólio NCM/Setor: snapshot corrente;
- Cesta Alimentos/COREDE Fronteira Oeste: 2021-01 a 2026-06;
- DFe São Borja: 2018-01 a 2026-09-14;
- DFe CNAE/RS: 2018-01 a 2026-09.

## Controles que devem permanecer ativos

- `corte_sigilo=1` no Radar não é zero econômico;
- valores estaduais não são atribuídos a São Borja;
- valores do COREDE Fronteira Oeste não são rotulados como municipais;
- DFe CNAE estadual não pode ser rateado por população, emprego, CNPJ ou outro fator ad hoc;
- DFe municipal não fornece market share por produto;
- arquivos brutos permanecem imutáveis; normalizações devem gerar derivados separados.

## Próxima frente recomendada

Construir a camada **curated/normalized** das séries recém-promovidas, mantendo três escalas distintas:

1. São Borja — DFe municipal;
2. COREDE Fronteira Oeste — preços da cesta;
3. Rio Grande do Sul — Radar e DFe CNAE.

Prioridades técnicas imediatas:

- normalizar `ano_mes` do Radar sem editar o bruto;
- converter campos monetários/quantitativos com regra explícita de separador;
- produzir inventário mensal de cobertura e sigilo;
- preparar tabelas de benchmark estadual/regional para os cadernos;
- só depois testar relações entre sazonalidade fiscal local e benchmarks externos.

Relatório detalhado: `docs/caderno_base/auditoria_series_publicas_download_v001_20260926.md`.

**Nenhum merge do PR #41 está autorizado por este checkpoint.**
