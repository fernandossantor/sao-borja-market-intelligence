# Checkpoint — retomada da inclusão de novos dados territoriais — 20/09/2026

## 1. Objetivo

Retomar a frente de inclusão de dados territoriais e mercadológicos que já estava em andamento antes do aprofundamento em compras públicas/B2G.

A frente não foi perdida. Os artefatos permaneceram na branch exploratória e voltaram a ser promovidos, por deltas, para o sucessor do Caderno-Base.

## 2. Governança

- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- Caderno-Base v028: **read-only**;
- PR #41: permanece **aberto, draft e sem merge**;
- nenhuma alteração em `main`.

## 3. Blocos retomados e promovidos por delta

### 3.1 SINAC/SIMEI — estrutura empresarial

Fonte: Receita Federal — Estatísticas do Simples Nacional.  
Posição: 12/09/2026.  
Geografia: São Borja/RS.

Fechamento:
- SINAC = 7.176;
- SIMEI = 4.883;
- razão SIMEI/SINAC = 68,05%;
- decomposição CNAE reconcilia exatamente com totais.

Principais divisões SINAC:
- comércio varejista 27,08%;
- serviços especializados para construção 9,78%;
- transporte terrestre 8,35%;
- alimentação 6,94%;
- comércio/reparação de veículos 6,83%;
- serviços pessoais 6,23%.

Status: **PROMOVER AO SUCESSOR DO CADERNO-BASE**.

Artefatos novos:
- `docs/data_sources/sinac_simei_division_summary_20260920_v001.csv`;
- `docs/caderno_base/analise_sinac_simei_estrutura_empresarial_20260920_v002.md`.

Drive:
- Delta_cadernos linha 49;
- documento-mestre seção 42.90.

### 3.2 ANP + Cadastur — mobilidade e turismo

ANP:
- gasolina C: 10.356.700 L (2023) → 15.929.410 L (2024), +53,81%;
- etanol: 359.000 → 592.100 L, +64,93%;
- diesel: 32.426.894 → 49.501.472 L, +52,66%;
- GLP total analítico: 1.676.685 → 1.335.619 kg, -20,34%;
- 10 revendedores em operação em 18/09/2026.

Cadastur 2T2026:
- 2 meios de hospedagem / 90 UHs / 180 leitos;
- 7 agências, 6 em operação;
- 6 guias regulares;
- 5 transportadoras, 4 em operação, 12 veículos declarados;
- 1 organizadora de eventos em operação.

Status: **PROMOVER AO SUCESSOR DO CADERNO-BASE**; contexto para Serviços e Alimentação Fora do Lar.

Artefatos novos:
- `docs/data_sources/cadastur_sao_borja_summary_20260920_v002.csv`;
- `docs/caderno_base/analise_anp_cadastur_mobilidade_turismo_20260920_v002.md`.

Drive:
- Delta_cadernos linha 50;
- documento-mestre seção 42.91.

### 3.3 Comex Stat municipal — jan–ago/2026

Fonte: MDIC/SECEX API oficial /cities.

Totais:
- exportações = US$ 9.848.096 FOB / 32.151.627 kg;
- importações = US$ 6.514.628 FOB / 17.497.000 kg;
- saldo FOB calculado = US$ 3.333.468.

Exportações:
- milho 48,61%;
- soja 41,36%;
- arroz 9,67%;
- trigo 0,36%.

Importações:
- arroz = US$ 6.417.496 = 98,51%;
- Uruguai = 94,02% do valor importado de arroz.

Controle:
município = domicílio fiscal do declarante, não origem/destino físico.

Status: **PROMOVER AO SUCESSOR DO CADERNO-BASE**; arroz apenas como contexto de cadeia em Bens Essenciais.

Artefatos novos:
- `docs/data_sources/comex_sao_borja_2026_summary_v001.csv`;
- `docs/caderno_base/analise_comex_stat_municipal_2026_v001.md`.

Drive:
- Delta_cadernos linha 51;
- documento-mestre seção 42.92.

### 3.4 ANTT — fluxo físico da fronteira

Fonte: ANTT — Anuário TRC 2025.

São Borja:
- 2023 = 859.348 t;
- 2024 = 800.435 t;
- 2025 = 979.151 t;
- 2024→2025 = +22%.

Participação entre as seis fronteiras da tabela:
- 2023 = 14,50%;
- 2024 = 14,78%;
- 2025 = 16,22%.

Em 2025:
- 3º maior volume entre os seis pontos apresentados;
- os três pontos gaúchos somam 58,37% do conjunto.

Controle:
ANTT mede fluxo físico pelo ponto; Comex municipal mede domicílio fiscal.

Status: **PROMOVER AO SUCESSOR DO CADERNO-BASE**; contexto de fluxo para Serviços.

Artefato novo:
- `docs/caderno_base/analise_antt_fronteira_fluxo_exportador_20260920_v002.md`.

Drive:
- Delta_cadernos linha 52;
- documento-mestre seção 42.93.

## 4. BET municipal

A varredura das 28 edições numéricas recuperadas do BET encontrou:
- downloads OK = 28;
- ocorrências textuais explícitas de “São Borja” = 0.

Isso **não significa atividade zero**.

Conclusão corrente:
- BET municipal continua **bloqueado para inclusão quantitativa**;
- não interpolar COREDE Fronteira Oeste para São Borja;
- manter BET como benchmark regional/estadual até rota municipal verificável.

## 5. Próxima ordem de inclusão

1. construir crosswalk auditável `CNAE → quatro mercados do projeto` sobre SINAC/SIMEI;
2. integrar Radar do Mercado histórico como benchmark estadual, preservando a distinção municipal/estadual;
3. promover Preços Dinâmicos e Cesta Nutricional apenas como benchmark COREDE/RS;
4. integrar estrutura de rede POM já materializada:
   - essenciais pulverizado;
   - farmácias multiunidade;
   - não essenciais pulverizado;
5. depois consolidar os deltas maduros em uma versão sucessora da v028.

## 6. Regra de promoção

Dado municipal oficial e reconciliado:
**PROMOVER**.

Benchmark regional/estadual:
**PROMOVER COMO CONTEXTO**, com geografia explícita.

Dado exploratório sem fechamento de fonte/geografia:
**NÃO PROMOVER**.

Inferência causal:
**BLOQUEADA** sem desenho específico.

## 7. Estado do documento-mestre

Última seção após esta retomada:
**42.93 — ANTT — corredor fronteiriço e escala física do fluxo exportador**.
