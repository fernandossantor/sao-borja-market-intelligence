# Radar do Mercado — histórico mensal de Composição de Mercado — jul/2024 a ago/2026

**Fonte observada:** Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos.
**Abrangência:** Rio Grande do Sul; fluxos INT/OUF/EXT conforme a metodologia do Radar.
**Período solicitado:** julho/2024 a agosto/2026, 26 competências mensais.
**Unidade:** valores nominais publicados nos CSVs oficiais; o pipeline preserva o conteúdo fonte e calcula Part.RS = INT/(INT+OUF+EXT).
**Natureza:** arquivos mensais oficiais observados + cálculos SBMI reproduzíveis.

Esta rodada mantém a cesta-piloto de sete NCMs de arroz para testar continuidade temporal, schema e cálculo. O arquivo rice_pilot_monthly_summary.csv é uma agregação calculada da cesta-piloto, não um indicador oficial do setor arroz nem medida municipal.

Nenhuma linha é promovida automaticamente a base canônica. O histórico deve ser auditado quanto a completude, mudança de schema e coerência temporal antes de uso narrativo.

Limitações:
- indicador estadual ≠ demanda de São Borja;
- cesta de sete NCMs ≠ total de uma cadeia econômica;
- valores >30% de Part.RS ficam fora das faixas de dependência explicitadas pela NT e não recebem categoria oficial inventada;
- mudanças no catálogo/NCM ou no schema mensal devem ser tratadas explicitamente.
