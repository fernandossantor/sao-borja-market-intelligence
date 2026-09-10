# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa substantiva deve, quando aplicável, sincronizar dados/derivados auditáveis no Google Drive, metadados e validações, narrativa em `docs/caderno_base/`, versão corrente do Caderno e descrição do PR.

Dado observado, cálculo, estimativa, hipótese, interpretação e recomendação permanecem separados. Versões anteriores são preservadas.

## Regra metodológica vigente — 2026-09-10

**auditoria suficiente → síntese analítica → lacunas decisórias → nova coleta apenas quando necessária.**

Auditorias marginais de bases já canonizadas não são caminho crítico. O join operador × CNPJ × RFB de bens essenciais permanece preservado como enriquecimento setorial **depriorizado**.

## Versão corrente

- Caderno: `caderno_base_territorial_v015_benchmark_estrutura_setorial_20260910` — Drive `17lktBasdTKFsnm0VIzBxnBcT3W3VVrN-Z_w_WwY-pZc`.
- Histórico imediato: v014 — Drive `1HXps9WjjO3p63TUrFYlCOaedA_kvyUVrcpa95ZCyIUY`.
- Diagnóstico: `docs/caderno_base/diagnostico_analitico_integrado_v012.md`.
- Diagnóstico nativo: Drive `1YCNcGDFeznW6NItibuaOJy0As89iZoP51uf1kujsxeA`.
- Benchmark escala/PIB: `benchmark_territorial_comparavel_v001.md`.
- Benchmark renda: `benchmark_territorial_comparavel_v002_renda.md`.
- Benchmark emprego/estrutura: `benchmark_territorial_emprego_estrutura_v001.md`.
- Checkpoint: `checkpoint_20260910.md`.

## Diagnóstico comparativo corrente

### Renda domiciliar — Censo 2022

Comparáveis por escala:
- São Gabriel: mediana R$ 1.051,00; até 2 SM pc 85,28%;
- **São Borja: mediana R$ 1.100,00; até 2 SM pc 85,79%**;
- Alegrete: mediana R$ 1.183,33; até 2 SM pc 82,64%;
- Santiago: mediana R$ 1.342,40; até 2 SM pc 74,14%.

São Borja não é outlier isolado, mas apresenta a maior concentração nas faixas até 2 SM entre os três comparáveis selecionados.

### PIB, trabalho e renda

PIB pc 2023 de Alegrete é apenas 0,24% maior que São Borja, porém sua mediana domiciliar é 7,58% maior.

Santiago possui PIB pc 10,99% menor e salário médio CEMPRE 0,18% menor que São Borja, mas mediana domiciliar 22,04% maior.

**Conclusão metodológica:** PIB per capita e salário médio das organizações não devem ser usados isoladamente como proxy de poder de compra.

### CEMPRE 2022

Salário médio mensal:
- São Borja R$ 2.708,09;
- Santiago R$ 2.703,19;
- São Gabriel R$ 2.646,27;
- Alegrete R$ 2.630,97.

Pessoal ocupado em unidades locais/1.000 residentes:
- São Borja 226,69;
- Santiago 220,67;
- Alegrete 209,82;
- São Gabriel 191,63.

Essa razão é contextual e **não é taxa de emprego**, pois mistura local de atividade e local de residência.

### Estrutura setorial

Participação no pessoal ocupado:
- comércio: São Borja 32,58%; Santiago 39,44%;
- transporte: São Borja 7,60%; Santiago 2,42%;
- construção: São Borja 7,25%; Santiago 3,13%;
- administração pública: São Borja 13,65%; Santiago 10,75%;
- educação + saúde*: São Borja 8,23%; Santiago 12,77%;
- J+K+M*: São Borja 5,29%; Santiago 8,32%.

\* Agregações analíticas, não categorias oficiais.

A estrutura é distinta, mas não se atribui causalidade à diferença de renda.

## Camadas territoriais já canonizadas

- RFB 2026-08: 6.906 estabelecimentos empresariais; 284 de matriz externa; 4,1124%.
- RAIS 2025 × RFB: emprego externo estimado 25,1606%; remuneração de dezembro externa estimada 29,6897%.
- Varejo G47: presença cadastral externa 6,6279%; emprego externo estimado 37,4609%; remuneração externa estimada 38,1636%.
- IPM definitivo 2026: 0,533647.
- VAF publicado 2025: R$ 2.325.966.620,93.
- Demanda modelada de bens essenciais: R$ 234.706.228,14/ano — **estimativa modelada**, não faturamento.

## Fronteira analítica

A questão de maior valor passa a ser a relação entre:
- local de residência;
- local de trabalho/estudo;
- centralidade regional;
- origem e destino do gasto.

A próxima prioridade é **mobilidade trabalho/estudo + centralidade regional → integração com POM → origem/destino do gasto**.

A configuração de escrita controlada permanece em `docs/drive_write_connection.md`. O PR #41 permanece **aberto, draft e sem merge** até autorização explícita.
