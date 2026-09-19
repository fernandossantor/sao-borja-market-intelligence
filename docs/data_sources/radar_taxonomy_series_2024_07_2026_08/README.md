# Radar do Mercado — composição por taxonomias oficiais — jul/2024 a ago/2026

**Fonte observada:** Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos.
**Composição temporal:** 26 competências mensais, jul/2024–ago/2026.
**Taxonomia aplicada:** snapshot corrente 2026-08 de Categorias_Produtos.csv e Portfolio_NCMs_Setor.csv.
**Unidade:** valores nominais publicados no Radar.
**Fórmula calculada:** Part.RS = INT / (INT + OUF + EXT).

Duas leituras são produzidas separadamente:
1. grupo_afinidade_final — classificação de Categorias_Produtos, com um grupo por NCM na tabela corrente; as agregações são aditivas entre grupos quando a cobertura do mês é completa;
2. emit_setor — Portfólio de NCMs por Setor, no qual um mesmo NCM pode integrar mais de um setor. Portanto, setores do Portfólio NÃO são aditivos entre si.

A classificação de dependência preserva apenas as faixas expressas na NT CIET 05/2026:
- CRITICA: Part.RS < 5%;
- ALTA: 5% <= Part.RS < 15%;
- MEDIA: 15% <= Part.RS < 30%;
- acima de 30%: FORA_DAS_FAIXAS_NT, marcador técnico do SBMI, não categoria oficial.

**Limitação temporal importante:** a taxonomia corrente 2026-08 é aplicada retrospectivamente às competências desde jul/2024. Isso permite uma série coerente sob uma classificação fixa, mas não prova que os rótulos/taxonomias publicados eram idênticos em cada competência histórica. A cobertura por NCM e valor é preservada em monthly_taxonomy_coverage.csv.

**Limitação territorial:** os indicadores são estaduais e não medem demanda, market share ou retenção monetária de São Borja.

Nenhuma linha é promovida automaticamente a base canônica.
