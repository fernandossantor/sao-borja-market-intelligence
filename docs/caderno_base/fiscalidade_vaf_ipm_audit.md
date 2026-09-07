# Fiscalidade territorial — IPM definitivo canonizado e auditoria de VAF

## Objetivo e delimitação

Esta etapa desenvolve a dimensão de **fiscalidade territorializada** do Caderno-Base de São Borja. O primeiro bloco — a série histórica do Índice de Participação dos Municípios (IPM) definitivo — foi concluído e canonizado. O bloco seguinte é a auditoria do **Valor Adicionado Fiscal (VAF)** e, posteriormente, sua reconciliação metodológica com a quota-parte monetária do ICMS efetivamente transferida ao município.

Abrangência geográfica: São Borja/RS.  
Fontes prioritárias: Receita Estadual / SEFAZ-RS e, para as finanças municipais já existentes no projeto, Tesouro Nacional / SICONFI.  
Data de atualização desta etapa: 2026-09-07.

A série de IPM definitivo está consolidada para os anos de distribuição **2003–2026**. O VAF, porém, ainda permanece em auditoria e não deve ser tratado como indicador canônico até que fonte, período, unidade, semântica dos campos e comparabilidade temporal estejam documentados.

## Conceitos que não devem ser confundidos

### IPM — Índice de Participação dos Municípios

O IPM é utilizado na repartição municipal do ICMS no Rio Grande do Sul. O índice determina a participação relativa do município no montante estadual distribuído segundo as regras vigentes. A variação do IPM, isoladamente, **não equivale à variação monetária da transferência de ICMS**, pois o valor efetivamente transferido depende também da arrecadação estadual e das regras de distribuição aplicáveis.

### VAF — Valor Adicionado Fiscal

O VAF é uma grandeza fiscal utilizada na apuração do IPM. Ele não deve ser tratado como sinônimo do IPM e tampouco como valor diretamente transferido ao município.

### VAB — Valor Adicionado Bruto

O VAB integra as Contas Regionais / PIB dos Municípios. É uma medida de produção econômica e possui conceito, fonte e metodologia distintos do VAF. **VAF e VAB não são diretamente intercambiáveis.**

### Receita e transferências municipais

Receita própria municipal, transferências correntes, quota-parte do ICMS, convênios e demais ingressos fiscais são fluxos orçamentários/financeiros distintos. O projeto já possui rotinas SICONFI para algumas dessas categorias, mas elas não devem ser somadas ou comparadas diretamente ao VAF/IPM sem alinhamento de conceito, estágio contábil e período.

## Fontes oficiais registradas

1. Receita Estadual — IPM / Índice de Participação dos Municípios  
   https://atendimento.receita.rs.gov.br/ipm-indice-de-participacao-dos-municipios

2. Receita Estadual — IPM Definitivos  
   https://atendimento.receita.rs.gov.br/ipm-definitivos

3. Receita Estadual — Consulta Valor Adicionado dos Municípios  
   https://www.sefaz.rs.gov.br/AIM/VAL-HIS.aspx

4. Receita Estadual — Manual AIM  
   https://atendimento.receita.rs.gov.br/manual-aim

5. Estado do Rio Grande do Sul — publicação dos índices provisórios de 2027, de 03/09/2026  
   https://estado.rs.gov.br/indices-provisorios-de-participacao-dos-municipios-no-icms-para-2027-estao-disponiveis-para-consulta

6. Estado do Rio Grande do Sul — comparação definitiva IPM 2026 × 2025  
   https://estado.rs.gov.br/upload/arquivos/202512/2025-12-17-variacoes-ipm-2026-x-2025-definitivo.pdf

## Série canônica de IPM definitivo — 2003–2026

### Fonte, unidade e período

- Fonte: Receita Estadual/RS — página **IPM Definitivos** e respectivos arquivos oficiais de importação `DAIM545X`.
- Geografia: São Borja/RS.
- Período: anos de distribuição 2003 a 2026.
- Unidade: índice de participação municipal, valor adimensional publicado com seis casas decimais.
- Natureza do IPM: **observado em fonte oficial definitiva**.
- Natureza da variação anual: **calculado**.

### Regra de extração

A auditoria dos 24 arquivos definitivos mostrou que o número e a estrutura dos campos intermediários do `DAIM545X` mudam ao longo do tempo. Por isso, a rotina canônica:

1. localiza a linha de São Borja em cada arquivo;
2. exige exatamente um registro municipal por ano;
3. extrai **somente o último campo**, que permanece estável no padrão decimal de seis casas;
4. não atribui significado aos campos intermediários sem o leiaute oficial específico do respectivo período.

Essa decisão evita reconstruir retrospectivamente componentes com nomenclatura ou posição variável.

### Execução canônica

Execução: `ipm-definitive-sao-borja-2003-2026-v001`.

Workflow: `ipm-definitive-layout-audit`, run `34165290782`, job final `101875804910`.

A primeira tentativa dessa execução foi interrompida por timeout do servidor oficial no arquivo de 2003. O job foi reexecutado sem alteração metodológica e concluiu com sucesso, baixando os 24 arquivos oficiais.

Validações finais:

| Controle | Resultado | Status |
|---|---:|---|
| linhas da série | 24 | PASS |
| anos únicos | 24 | PASS |
| intervalo completo | 2003–2026 | PASS |
| um único registro de São Borja por ano | 24/24 | PASS |
| IPM positivo | 24/24 | PASS |
| benchmark 2025 | 0,527880 | PASS |
| benchmark 2026 | 0,533647 | PASS |

Resultado da auditoria: **7/7 controles PASS**.

### Série observada e variação calculada

| Ano de distribuição | IPM definitivo | Variação anual calculada |
|---:|---:|---:|
| 2003 | 0,513428 | — |
| 2004 | 0,495566 | -3,4790% |
| 2005 | 0,527544 | +6,4528% |
| 2006 | 0,552260 | +4,6851% |
| 2007 | 0,534556 | -3,2057% |
| 2008 | 0,506586 | -5,2324% |
| 2009 | 0,497940 | -1,7067% |
| 2010 | 0,514494 | +3,3245% |
| 2011 | 0,520548 | +1,1767% |
| 2012 | 0,514997 | -1,0664% |
| 2013 | 0,501506 | -2,6196% |
| 2014 | 0,486621 | -2,9681% |
| 2015 | 0,487373 | +0,1545% |
| 2016 | 0,481651 | -1,1740% |
| 2017 | 0,468285 | -2,7750% |
| 2018 | 0,481831 | +2,8927% |
| 2019 | 0,511653 | +6,1893% |
| 2020 | 0,519229 | +1,4807% |
| 2021 | 0,520352 | +0,2163% |
| 2022 | 0,553953 | +6,4574% |
| 2023 | 0,573154 | +3,4662% |
| 2024 | 0,543201 | -5,2260% |
| 2025 | 0,527880 | -2,8205% |
| 2026 | 0,533647 | +1,0925% |

Fórmula da variação anual:

\[
\Delta IPM_t = \left(\frac{IPM_t}{IPM_{t-1}} - 1\right) \times 100
\]

Os valores anuais do IPM são **observados**. As variações são **calculadas**.

### Comparabilidade temporal

A série é comparável como trajetória do **índice final oficialmente publicado**. Entretanto, pesos, critérios legais e componentes de cálculo do IPM mudam ao longo do tempo. Portanto, a mudança de um ano para outro não pode ser atribuída automaticamente a um mesmo conjunto invariável de fatores.

## Promoção ao Google Drive

Pasta dos derivados: `ipm-definitive-sao-borja-2003-2026-v001`, Drive ID `1YTbi1SKuaJndJ8E-GhYwqHgcN1crnjJu`.

Foram promovidos cinco CSVs sem conversão:

- `sao_borja_ipm_definitive_2003_2026.csv`;
- `validation.csv`;
- `source_manifest.csv`;
- `run_metadata.csv`;
- `ipm_definitive_layout_audit.csv`.

A listagem pós-upload confirmou **5/5 arquivos**, nomes esperados e tamanhos idênticos aos auditados. O conector Drive não expõe `sha256Checksum`; por isso, a verificação criptográfica registrada refere-se aos bytes imediatamente anteriores ao upload e não a um novo download posterior.

Manifesto completo: `docs/caderno_base/ipm_definitive_drive_promotion_manifest.md`.

## Sincronização do Caderno-Base

O `caderno_base_territorial_v007_fiscalidade_ipm_20260907` permanece como versão corrente. Foram adicionadas as abas:

- `IPM_historico` — série definitiva 2003–2026 e hashes dos arquivos oficiais;
- `Manifesto_IPM` — arquivos promovidos, tamanhos, hashes pré-upload e IDs do Drive.

A primeira escrita da aba histórica revelou uma particularidade do locale `pt_BR`: strings com ponto decimal foram interpretadas pelo Google Sheets como milhares. A inconsistência foi detectada na leitura de verificação e corrigida no mesmo ciclo, regravando os campos como números da API e aplicando formatação explícita. A leitura final reproduziu corretamente os 24 índices e suas variações.

O estado fiscal da v007 passa a ser: **IPM definitivo canonizado; VAF ainda em auditoria**.

## IPM provisório de 2027

A publicação estadual de 03/09/2026 informa mudanças de pesos em critérios do IPM 2027. Nesta auditoria permanecem registrados:

| Critério | Peso anterior | Peso informado para 2027 | Natureza |
|---|---:|---:|---|
| Programa de Reforma Tributária / PRE | 12,8% | 14,2% | observado em publicação oficial |
| População | 4,2% | 2,8% | observado em publicação oficial |
| Propriedades rurais | 4,8% | 4,7% | observado em publicação oficial |
| Programa de Integração Tributária / PIT | 0,7% | 0,8% | observado em publicação oficial |

Os índices de 2027 permanecem provisórios nesta etapa e não são incorporados à série definitiva 2003–2026.

## O que a etapa concluída permite afirmar

**Dado observado:** São Borja possui uma série oficial definitiva de IPM de 2003 a 2026 reproduzida diretamente dos arquivos oficiais da Receita Estadual/RS.

**Dado calculado:** de 2025 para 2026 o IPM passou de 0,527880 para 0,533647, variação relativa de **+1,092483%**.

**Interpretação:** houve aumento da participação relativa de São Borja no índice estadual entre os dois anos definitivos. A série também mostra oscilações expressivas em diferentes períodos, mas a decomposição causal dessas mudanças exige os componentes e critérios válidos em cada ano.

## O que ainda não é possível concluir

Mesmo com o IPM canonizado, ainda não é possível afirmar:

- o valor monetário adicional de ICMS efetivamente recebido em decorrência de cada mudança do índice;
- o VAF definitivo de São Borja em cada exercício ou sua composição setorial/contribuinte;
- quanto do VAF é gerado por estruturas empresariais de matriz local ou externa;
- relação causal entre presença de matrizes externas e evolução do IPM;
- taxa de retenção ou vazamento econômico do município;
- equivalência entre VAF fiscal e VAB das Contas Regionais.

## Próximas etapas

A etapa anteriormente prevista de construção da série histórica canônica de IPM definitivo está **CONCLUÍDA**.

A sequência metodológica passa a ser:

1. auditar a fonte oficial de **Valor Adicionado dos Municípios** e documentar período, unidade, status e semântica dos campos;
2. construir a série histórica canônica de VAF somente após essa auditoria;
3. verificar eventual disponibilidade de componentes do IPM por ano, respeitando mudanças legais e metodológicas;
4. reconciliar IPM e VAF com a **quota-parte monetária do ICMS efetivamente transferida** ao município;
5. apenas depois avaliar relações exploratórias com estrutura matriz/filial, emprego e remuneração.
