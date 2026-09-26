# Séries públicas Receita Estadual / Radar / Cesta de Alimentos — inventário de aquisição v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica  
**Objetivo:** registrar a aquisição automatizada das séries públicas identificadas manualmente, sua cobertura temporal, estrutura e limites de uso.

## 1. Padrões de URL auditados

### Radar do Mercado — Composição de Mercado

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Composicao_de_Mercado_MM_AAAA.csv`

### Radar do Mercado — Exportações por NCM

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Exportacoes_NCM_MM_AAAA.csv`

### Radar do Mercado — Portfólio NCM × Setor

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Portfolio_NCMs_Setor.csv`

### Receita Dados — DFe Totais Município

`https://receitadados.sefaz.rs.gov.br/Arquivos/DFe_Totais_Municipio_AAAA.zip`

### Receita Dados — DFe Totais CNAE Classe

`https://receitadados.sefaz.rs.gov.br/Arquivos/DFe_Totais_CNAE_Classe_AAAA.zip`

### Cesta de Alimentos — dados mensais por COREDE

`https://arquivosradar.sefaz.rs.gov.br/CestaAlimentos/Mensal_Todas/public_dados_mensais_AAAA.csv`

## 2. Cobertura encontrada

A rotina testou os anos 2018–2026 e, para as séries mensais do Radar, todos os meses de janeiro a dezembro.

| Série | Cobertura pública localizada | Arquivos válidos |
|---|---|---:|
| Radar — Composição de Mercado | jul/2024 a ago/2026 | 26 |
| Radar — Exportações NCM | jul/2024 a ago/2026 | 26 |
| Radar — Portfólio NCM × Setor | arquivo estático | 1 |
| DFe Totais Município | 2018–2026 | 9 |
| DFe Totais CNAE Classe | 2018–2026 | 9 |
| Cesta de Alimentos mensal | 2021–2026 | 6 |

Total de arquivos públicos válidos preservados: **77**.

As URLs inexistentes/futuras foram registradas no manifesto e não foram salvas como dados.

## 3. Auditoria estrutural inicial

### 3.1 Radar — Composição de Mercado

Estrutura estável observada nos 26 arquivos:

`anomes | cod_ncm | ncm_descr | emit_uf | tipo_operacao | vlr_nominal | corte_sigilo`

Tipos de operação observados:
- `INT`;
- `OUF`;
- `EXT`.

Exemplo de cobertura:
- jul/2024: 60.678 linhas; 8.931 NCM distintos;
- ago/2026: 64.948 linhas; 8.959 NCM distintos.

Há incidência elevada de `corte_sigilo = 1` — aproximadamente metade das células em meses auditados. Valores zerados por corte de sigilo **não devem ser interpretados como ausência econômica**.

**Uso potencial:** composição de abastecimento do mercado gaúcho por produto/NCM e origem — interno RS, outras UFs, exterior.

**Limite:** não contém município; não é faturamento de São Borja.

### 3.2 Radar — Exportações por NCM

Estrutura estável:

`anomes | cod_ncm | cod_pais | vlr_fob`

Cobertura:
- jul/2024 a ago/2026;
- 26 arquivos mensais.

Exemplo:
- jul/2024: 16.212 linhas; 2.431 NCM; 177 países/códigos de destino;
- ago/2026: 16.632 linhas; 2.405 NCM; 182 países/códigos.

**Uso potencial:** orientação exportadora e mercados externos dos produtos/setores do RS, cruzável com os módulos dos cadernos.

**Limite:** dado estadual/externo; não atribuir exportações a São Borja sem dimensão territorial compatível.

### 3.3 Portfólio NCM × Setor

Estrutura:

`emit_atividade | emit_classe | emit_setor | cod_ncm | ncm_descr`

Auditoria inicial:
- 1.900 linhas;
- 1.349 NCM distintos;
- 18 classes;
- 49 setores;
- `emit_atividade` observado: INDÚSTRIA.

**Uso potencial:** taxonomia setorial complementar para NCM, especialmente em análise de produção/oferta e composição de mercado.

**Limite:** não substitui o crosswalk SBMI orientado ao consumo e aos cinco cadernos; um NCM pode requerer decisão analítica diferente conforme a pergunta.

### 3.4 DFe Totais Município

Estrutura em todos os anos:

`modelo_dfe | dt_emissao | cod_municipio | nome_municipio | qtde_dfe | vlr_total_dfe`

Cobertura:
- 2018–2025: anos fechados;
- 2026: 01/01/2026 a 14/09/2026.

A série pública agora permite estender o envelope fiscal municipal de São Borja para **2018–2026**.

### 3.5 DFe Totais CNAE Classe

Estrutura:

`modelo_dfe | dt_emissao | cod_cnae_classe | nome_cnae_classe | qtde_dfe | vlr_total_dfe`

Cobertura:
- 2018–2025: anos fechados;
- 2026: até 14/09/2026.

Número aproximado de linhas anuais:
- 2018: 234.823;
- 2019: 241.359;
- 2020: 242.885;
- 2021: 246.327;
- 2022: 249.075;
- 2023: 250.436;
- 2024: 249.937;
- 2025: 257.325;
- 2026 parcial: 191.078.

**Uso potencial:** benchmark estadual por classe CNAE, modelo DFe e dia, com série comparável longa.

**Limite central:** permanece sem município no mesmo arquivo.

### 3.6 Cesta de Alimentos — mensal por COREDE

Estrutura:

`Data | Corede | NMProduto | VlrUnidade`

Cobertura auditada:
- 2021–2025: 12 meses completos;
- 2026: jan–jun.

Cada ano fechado contém:
- 29 COREDE;
- 80 produtos;
- 12 meses;
- 27.840 linhas;
- nenhum valor ausente na estrutura lida.

2026 contém:
- 29 COREDE;
- 80 produtos;
- 6 meses;
- 13.920 linhas.

Os conjuntos de COREDE e de produtos permaneceram idênticos entre 2021 e 2026 na auditoria inicial.

**Uso potencial prioritário:** série regional de preços da Fronteira Oeste e construção de índice experimental/benchmark de preços de alimentos, com ponderação metodológica adequada.

**Limite:** COREDE não é São Borja; não denominar automaticamente o resultado como inflação municipal.

## 4. Pacotes preservados no Google Drive

### Cesta de Alimentos 2021–2026

Arquivo:
`SBMI_CestaAlimentos_mensal_2021_2026_v001.zip`

Drive ID:
`12w7dwLgW0Iuy6-t8SJ8KSU2hhbNRHgN-`

### Manifesto da aquisição

Arquivo:
`SBMI_series_publicas_manifest_v001.zip`

Drive ID:
`1jygX-oEQfcJnY-uf_XgWxOUDBXO2cp3M`

### Radar — Exportações NCM

Arquivo:
`SBMI_Radar_Exportacoes_NCM_2024-07_2026-08_v001.zip`

Drive ID:
`1YJfM_s9Jm2Q_RHTra-QW8r6p3bT2_pO3`

### DFe CNAE Classe 2018–2022

Arquivo:
`SBMI_DFe_CNAE_Classe_2018_2022_v001.zip`

Drive ID:
`11oaRJ3nMapL5LV7KnP2i53QfBBz6NtQ5`

### Radar — Composição de Mercado

Arquivo:
`SBMI_Radar_Composicao_Mercado_2024-07_2026-08_v001.zip`

Drive ID:
`1SgPMsAB2eWFiqd0vsjCGezCJeijPb3ET`

### DFe Município 2018–2026

Arquivo:
`SBMI_DFe_Municipio_2018_2026_v001.zip`

Drive ID:
`1DuirpWKYP4Pwu8qxyEU_B6le0MXnfD-j`

### DFe CNAE Classe 2023–2026

Arquivo:
`SBMI_DFe_CNAE_Classe_2023_2026_v001.zip`

Drive ID:
`1-NVys5ENQAw8bTrbv58Suvcjdcjujuv_`

## 5. Rastreabilidade técnica

Workflow corrente:
`.github/workflows/download-public-series-bulk-v1.yml`

Run:
`36275562165`

Commit:
`2d3c7decd30141cceb81064513dc51b71bdc46a1`

Artifacts:
- metadata: `10917176356`;
- cesta: `10917176369`;
- Radar exportações: `10917101603`;
- Radar composição: `10916627416`;
- DFe município: `10916617398`;
- DFe CNAE 2018–2022: `10916797132`;
- DFe CNAE 2023–2026: `10916542556`.

A aquisição foi feita por download direto das URLs públicas. Os arquivos originais foram preservados sem transformação de valores.

## 6. Prioridade analítica após a aquisição

1. **DFe Município 2018–2022:** estender imediatamente a série histórica de São Borja já existente para 2018–2026.
2. **Cesta 2021–2026:** construir painel de preços da Fronteira Oeste, testar continuidade e comparar com IPCA.
3. **Radar Composição 2024–2026:** cruzar os NCM prioritários dos cadernos e medir composição INT/OUF/EXT nas células não suprimidas.
4. **Radar Exportações 2024–2026:** produzir benchmark de exposição exportadora dos mesmos grupos/NCM.
5. **Portfólio NCM × Setor:** usar como taxonomia de oferta/produção, preservando separação em relação ao crosswalk de consumo do SBMI.
6. **DFe CNAE Classe 2018–2026:** construir benchmarks estaduais históricos por classe para comparação com a futura extração municipal-setorial.

## 7. Decisão

Essas séries passam a integrar o acervo auditável do projeto.

Elas ampliam significativamente:
- a profundidade temporal do envelope fiscal municipal;
- os benchmarks por classe CNAE;
- a análise regional de preços;
- a taxonomia e a composição do mercado gaúcho por NCM;
- a análise de exportações.

Elas **não resolvem**, por si só, a lacuna principal de market share:
`São Borja × setor/NCM × valor`.

Essa interseção continua dependente de fonte adicional ou extração agregada oficial.
