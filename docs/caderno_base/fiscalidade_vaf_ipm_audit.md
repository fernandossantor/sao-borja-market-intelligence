# Fiscalidade territorial — IPM definitivo canonizado e auditoria de VAF

## Objetivo e delimitação

Esta etapa desenvolve a dimensão de **fiscalidade territorializada** do Caderno-Base de São Borja. O primeiro bloco — a série histórica do Índice de Participação dos Municípios (IPM) definitivo — foi concluído e canonizado. O bloco seguinte é a auditoria do **Valor Adicionado Fiscal (VAF)** e, posteriormente, sua reconciliação metodológica com a quota-parte monetária do ICMS efetivamente transferida ao município.

Abrangência geográfica: São Borja/RS.  
Fontes prioritárias: Receita Estadual / SEFAZ-RS e, para as finanças municipais já existentes no projeto, Tesouro Nacional / SICONFI.  
Data de atualização desta etapa: 2026-09-07.

A série de IPM definitivo está consolidada para os anos de distribuição **2003–2026**. O VAF permanece em auditoria: a arquitetura da fonte, a semântica temporal e os conceitos centrais já foram documentados, mas nenhuma série monetária oficial foi ainda canonizada.

## Conceitos que não devem ser confundidos

### IPM — Índice de Participação dos Municípios

O IPM é utilizado na repartição municipal do ICMS no Rio Grande do Sul. O índice determina a participação relativa do município no montante estadual distribuído segundo as regras vigentes. A variação do IPM, isoladamente, **não equivale à variação monetária da transferência de ICMS**, pois o valor efetivamente transferido depende também da arrecadação estadual e das regras de distribuição aplicáveis.

### Valor adicionado anual e critério VAF do IPM

O Manual AIM atual permite distinguir duas grandezas que não devem ser fundidas em uma única coluna denominada genericamente `vaf`:

1. **valor adicionado anual do município**, grandeza monetária apurada por ano civil a partir do movimento econômico no âmbito do ICMS;
2. **índice de valor adicionado utilizado como critério do IPM**, construído a partir dos índices dos dois anos civis imediatamente anteriores ao ano de apuração.

Para empresas da categoria Geral, o valor adicionado corresponde, em termos gerais, ao valor das saídas e prestações menos as entradas, com as regras fiscais de apropriação aplicáveis. Nas hipóteses de tributação simplificada previstas na legislação, considera-se 32% da receita bruta.

O Manual AIM registra ainda que a totalização da diferença entre saídas/prestações e entradas deve ser efetuada **por município e por ano civil**. Em seguida, informa que o VAF considerado no IPM corresponde à **média dos índices apurados nos dois anos civis imediatamente anteriores ao ano da apuração**.

Por essa razão, a futura base canônica deverá preservar, no mínimo:

- `ano_dado`: ano civil do movimento econômico-fiscal;
- `valor_adicionado_anual_rs`: valor monetário anual, quando a fonte oficial o publicar de forma inequívoca;
- `indice_valor_adicionado`: participação/índice relativo, quando disponibilizado;
- `ano_apuracao_ipm`: ano em que o IPM é calculado;
- `ano_distribuicao_ipm`: ano seguinte, em que o índice definitivo é utilizado no rateio.

Não será feita conversão entre valor monetário e índice relativo sem denominador estadual oficial e regra explicitamente documentada.

### VAB — Valor Adicionado Bruto

O VAB integra as Contas Regionais / PIB dos Municípios. É uma medida de produção econômica e possui conceito, fonte e metodologia distintos do VAF. **VAF e VAB não são diretamente intercambiáveis.**

### Receita e transferências municipais

Receita própria municipal, transferências correntes, quota-parte do ICMS, convênios e demais ingressos fiscais são fluxos orçamentários/financeiros distintos. O projeto já possui rotinas SICONFI para algumas dessas categorias, mas elas não devem ser somadas ou comparadas diretamente ao VAF/IPM sem alinhamento de conceito, estágio contábil e período.

A auditoria dos derivados `fiscal_*` existentes no Drive confirmou que eles reúnem transferências federais constitucionais, royalties e transferências programáticas — FPM, FUNDEB, ITR, saúde, educação e outras — e **não contêm VAF**. Esses derivados permanecem úteis para a análise de dependência fiscal, mas não são fonte nem proxy do valor adicionado fiscal.

## Fontes oficiais registradas

1. Receita Estadual — IPM / Índice de Participação dos Municípios  
   https://atendimento.receita.rs.gov.br/ipm-indice-de-participacao-dos-municipios

2. Receita Estadual — IPM Definitivos  
   https://atendimento.receita.rs.gov.br/ipm-definitivos

3. Receita Estadual — Consulta Valor Adicionado dos Municípios — wrapper atual  
   https://www.sefaz.rs.gov.br/AIM/VAL-HIS.aspx

4. Receita Estadual — formulário legado da consulta histórica de VAF  
   https://www.sefaz.rs.gov.br/ASP/SEF_ROOT/AIM/AIM-WEB-VAL-HIS_1.asp

5. Receita Estadual — Consultas e Arquivos Antigos - IPM  
   https://atendimento.receita.rs.gov.br/consultas-e-arquivos-antigos-ipm

6. Receita Estadual — Manual AIM  
   https://atendimento.receita.rs.gov.br/manual-aim

7. Estado do Rio Grande do Sul — publicação dos índices provisórios de 2027, de 03/09/2026  
   https://estado.rs.gov.br/indices-provisorios-de-participacao-dos-municipios-no-icms-para-2027-estao-disponiveis-para-consulta

8. Estado do Rio Grande do Sul — comparação definitiva IPM 2026 × 2025  
   https://estado.rs.gov.br/upload/arquivos/202512/2025-12-17-variacoes-ipm-2026-x-2025-definitivo.pdf

## Auditoria da fonte oficial de VAF

### Arquitetura observada

A consulta pública atual possui a seguinte cadeia oficial:

`Portal IPM da Receita Estadual → /AIM/VAL-HIS.aspx → iframe do formulário AIM-WEB-VAL-HIS_1.asp → POST para AIM-WEB-VAL-HIS_2.asp`.

A rotina `src/sbmi/vaf_source_audit.py` preserva essa arquitetura sem atribuir semântica a campos por posição. Apenas domínios oficiais da Receita Estadual/SEFAZ-RS são aceitos.

Em execução real bem-sucedida de disponibilidade (`vaf-source-audit`, run `34167993906`, job `101882749634`), as quatro rotas oficiais responderam HTTP 200. O formulário legado apresentou:

- método `POST`;
- action oficial `AIM-WEB-VAL-HIS_2.asp`;
- `anoini`: anos de apuração de **1992 a 2025**;
- `anofim`: anos de apuração de **1992 a 2025**;
- `letramun`: intervalos alfabéticos de municípios;
- intervalo que contém São Borja: **“São Martinho até Soledade”**, valor de formulário `SAO MARTINHSZZZZZZZZZZ`;
- comando de submissão `Action=Consultar`.

Esses campos são **observados na estrutura oficial do formulário**. A faixa 1992–2025 é cobertura disponível da interface de consulta por **ano de apuração**, não uma afirmação de que exista uma série monetária homogênea de VAF para todo esse período.

### Arquivos históricos oficiais identificados

A página oficial `Consultas e Arquivos Antigos - IPM` publica, entre outros materiais:

- **Valor Adicionado Municípios — 2009 a 2012**;
- **Valor Adicionado Municípios — 1989 a 1997**;
- leiautes do Sistema Próprio/AIM de 2003, 2004, 2005, 2006 e 2007;
- perfis econômico-tributários históricos e documentação GMB/AIM.

Esses arquivos constituem uma segunda rota oficial para reconstrução e validação histórica. Até esta etapa, os binários antigos de valor adicionado foram identificados no catálogo oficial, mas ainda não foram incorporados aos dados mestre do projeto: o host legado apresenta disponibilidade intermitente para download automatizado.

### Disponibilidade e limitações técnicas do endpoint legado

A disponibilidade do serviço é intermitente a partir do GitHub Actions. Depois da execução em que todas as rotas responderam HTTP 200, duas tentativas controladas da consulta mínima — ano de apuração 2025 e somente o intervalo municipal que contém São Borja — sofreram `ConnectTimeout` antes da recuperação do formulário e, portanto, **o POST não foi executado**.

Execução: run `34168189937`; jobs `101883303645` e reexecução `101883730618`.

O código da auditoria permaneceu estável quanto aos parâmetros da consulta. Na versão corrente, **8 testes passaram e o Ruff passou**. A falha é registrada como disponibilidade externa e não é convertida em dado ausente, zero ou estimativa.

### Semântica temporal confirmada pelo Manual AIM

O Manual AIM diferencia explicitamente os estágios temporais. O IPM apurado em determinado ano é utilizado na distribuição do ano seguinte, com dados econômico-fiscais de anos anteriores. O exemplo oficial indica:

- dados econômicos: 2016 e 2017 para o critério de valor adicionado;
- apuração do IPM: 2018;
- distribuição das quotas-partes: 2019.

Portanto, `ano_dado`, `ano_apuracao_ipm` e `ano_distribuicao_ipm` são dimensões distintas. Essa linhagem será obrigatória no pipeline de VAF.

## Benchmark secundário de VAF — não canônico

O Drive do projeto contém o relatório **Perfil das Cidades Gaúchas — São Borja**, Sebrae/RS, edição 2020. O documento informa explicitamente como fonte do VAF a **SEFAZ-RS — Receita Estadual/RS** e declara utilizar “o VAF que compõe o IPM do ano corrente”.

O relatório reproduz a seguinte série, em **milhões de reais**, que será mantida somente como benchmark independente para validação futura da fonte oficial:

| Ano rotulado no relatório | VAF reproduzido (R$ milhões) | Natureza no projeto |
|---:|---:|---|
| 2009 | 553,32 | observado em fonte secundária |
| 2010 | 655,36 | observado em fonte secundária |
| 2011 | 692,88 | observado em fonte secundária |
| 2012 | 742,77 | observado em fonte secundária |
| 2013 | 801,33 | observado em fonte secundária |
| 2014 | 854,64 | observado em fonte secundária |
| 2015 | 1.021,53 | observado em fonte secundária |
| 2016 | 994,83 | observado em fonte secundária |
| 2017 | 1.047,00 | observado em fonte secundária |
| 2018 | 1.211,63 | observado em fonte secundária |
| 2019 | 1.313,68 | observado em fonte secundária |

**Limitação:** a série acima não é promovida ao pipeline canônico. O próprio rótulo do relatório associa o valor ao VAF que compõe o IPM do ano corrente; por isso, o ano apresentado não deve ser reinterpretado automaticamente como ano civil do movimento econômico bruto sem reconciliação com a fonte oficial.

Um segundo relatório territorial armazenado no Drive confirma, de forma secundária, a lógica de média dos dois anos anteriores utilizada no critério VAF. Também não é usado como substituto do Manual AIM.

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

O `caderno_base_territorial_v007_fiscalidade_ipm_20260907` permanece como versão corrente. As abas `IPM_historico` e `Manifesto_IPM` registram a série e sua linhagem. A primeira escrita da aba histórica revelou uma particularidade do locale `pt_BR`; a inconsistência foi detectada e corrigida no mesmo ciclo.

O estado fiscal da v007 permanece: **IPM definitivo canonizado; VAF ainda em auditoria**.

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

**Dado observado oficial:** São Borja possui uma série definitiva de IPM de 2003 a 2026 reproduzida diretamente dos arquivos oficiais da Receita Estadual/RS.

**Dado calculado:** de 2025 para 2026 o IPM passou de 0,527880 para 0,533647, variação relativa de **+1,092483%**.

**Dado observado sobre a fonte VAF:** a consulta pública oferece anos de apuração 1992–2025; a Receita mantém também arquivos históricos explícitos de valor adicionado para 1989–1997 e 2009–2012.

**Interpretação metodológica:** a fonte oficial permite separar movimento econômico anual, apuração do IPM e distribuição. Essa distinção é obrigatória para que uma futura série de VAF não misture valor monetário anual com índice relativo de valor adicionado.

**Benchmark secundário:** existe uma reprodução Sebrae/RS 2009–2019, em milhões de reais, atribuída à SEFAZ-RS. Ela serve apenas para validação futura e não integra o conjunto canônico.

## O que ainda não é possível concluir

Mesmo com o IPM canonizado e a arquitetura do VAF auditada, ainda não é possível afirmar:

- uma série oficial canônica de `valor_adicionado_anual_rs` de São Borja;
- se todos os anos disponibilizados pela consulta histórica possuem exatamente a mesma unidade e estrutura de resultado;
- o valor monetário adicional de ICMS efetivamente recebido em decorrência de cada mudança do índice;
- a composição setorial/contribuinte do VAF histórico;
- quanto do VAF é gerado por estruturas empresariais de matriz local ou externa;
- relação causal entre presença de matrizes externas e evolução do IPM;
- taxa de retenção ou vazamento econômico do município;
- equivalência entre VAF fiscal e VAB das Contas Regionais.

## Próximas etapas

A etapa de construção da série histórica canônica de IPM definitivo está **CONCLUÍDA**. Para o VAF, a sequência passa a ser:

1. recuperar pelo menos um resultado oficial do formulário ou um dos arquivos históricos binários e documentar cabeçalhos, unidade e ano de referência;
2. reconciliar o resultado com o benchmark secundário 2009–2019 nos anos sobrepostos, sem usá-lo como fonte substituta;
3. separar no modelo `valor_adicionado_anual_rs` e `indice_valor_adicionado`, caso ambos estejam disponíveis;
4. construir a série histórica canônica apenas nos intervalos cuja comparabilidade seja demonstrada;
5. reconciliar IPM/VAF com a **quota-parte monetária do ICMS efetivamente transferida** ao município;
6. somente depois avaliar relações exploratórias com estrutura matriz/filial, emprego e remuneração.
