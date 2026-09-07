# Fiscalidade territorial — auditoria inicial de IPM e VAF

## Objetivo e delimitação

Esta etapa inicia a dimensão de **fiscalidade territorializada** do Caderno-Base de São Borja. O objetivo imediato é organizar fontes oficiais e conceitos antes de produzir qualquer indicador que possa ser interpretado como retorno fiscal, retenção territorial ou vazamento de valor.

Abrangência geográfica: São Borja/RS.  
Fontes prioritárias: Receita Estadual / SEFAZ-RS e, para as finanças municipais já existentes no projeto, Tesouro Nacional / SICONFI.  
Data desta auditoria inicial: 2026-09-07.

A etapa ainda **não constitui um pipeline canônico de VAF/IPM**. Ela registra benchmarks oficiais, mudanças de status provisório/definitivo, distinções metodológicas e lacunas que devem ser resolvidas antes da integração quantitativa com emprego, remuneração ou finanças municipais.

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

## Dados observados — São Borja

Os valores abaixo referem-se ao **ano de distribuição do IPM**, conforme identificação das publicações oficiais utilizadas.

| Indicador | Ano | Valor | Natureza | Situação |
|---|---:|---:|---|---|
| IPM definitivo | 2025 | 0,527880 | observado | canônico nesta auditoria |
| IPM provisório | 2026 | 0,528175 | observado provisório | superado pelo definitivo; preservar apenas para linhagem |
| IPM definitivo | 2026 | 0,533647 | observado | canônico nesta auditoria |
| IPM 2027 | 2027 | valor municipal ainda não incorporado | observado apenas quanto ao status | provisório, sujeito a impugnação |

### Dado calculado

Variação relativa do IPM definitivo de 2025 para 2026:

\[
\Delta IPM = \left(\frac{0{,}533647}{0{,}527880} - 1\right) \times 100
\]

Resultado:

**+1,092483%**, arredondado para **+1,09%**.

Natureza: **calculado a partir de dois índices oficiais definitivos**.  
Unidade: percentual de variação relativa do índice.  
Limitação: não representa aumento de 1,09% da arrecadação estadual nem da transferência monetária de ICMS recebida por São Borja.

## Mudanças registradas para o IPM provisório de 2027

A publicação estadual de 03/09/2026 informa mudanças de pesos em critérios do IPM 2027. Nesta auditoria foram registrados:

| Critério | Peso anterior | Peso informado para 2027 | Natureza |
|---|---:|---:|---|
| Programa de Reforma Tributária / PRE | 12,8% | 14,2% | observado em publicação oficial |
| População | 4,2% | 2,8% | observado em publicação oficial |
| Propriedades rurais | 4,8% | 4,7% | observado em publicação oficial |
| Programa de Integração Tributária / PIT | 0,7% | 0,8% | observado em publicação oficial |

A mesma publicação informa que os índices provisórios de 2027 utilizam dados relativos ao exercício de 2025 e estavam sujeitos a impugnação até 03/10/2026. Por isso, **nenhum valor provisório de 2027 deve ser incorporado à série definitiva antes do encerramento do processo e da publicação do índice definitivo**.

## Auditoria do acervo do projeto

A pasta de fontes `_sao_borja/new_files/01_fontes_e_coletas/financas_publicas` foi conferida nesta etapa e estava vazia. Portanto, não existe atualmente nesse diretório uma fonte mestre de VAF/IPM a ser reaproveitada.

O repositório já contém rotinas de finanças públicas municipais (`public_finance_series.py`) baseadas em SICONFI/Tesouro e rotinas de perfil de recursos públicos estaduais (`state_rs_public_funds_profile.py`). Essas rotinas tratam conceitos diferentes do IPM/VAF e **não foram modificadas nem reutilizadas como substituto** nesta auditoria.

## O que esta etapa permite concluir

**Fato observado:** o IPM definitivo de São Borja passou de 0,527880 em 2025 para 0,533647 em 2026.

**Dado calculado:** isso corresponde a aumento relativo de aproximadamente 1,09% no índice.

**Interpretação limitada:** a participação relativa de São Borja na regra estadual de distribuição do ICMS melhorou entre os dois índices definitivos. O dado, sozinho, não informa quanto dinheiro adicional entrou no orçamento municipal, quais componentes explicaram a mudança nem qual parcela do valor econômico gerado no município foi retida localmente.

## O que não é possível concluir ainda

Nesta fase não é possível afirmar, com base apenas nesses índices:

- o valor monetário adicional de ICMS efetivamente recebido por São Borja;
- o VAF definitivo de São Borja em cada exercício ou sua composição por atividade/contribuinte;
- quanto do VAF é gerado por estruturas empresariais de matriz local ou externa;
- relação causal entre presença de matrizes externas e evolução do IPM;
- taxa de retenção/vazamento econômico do município;
- equivalência entre VAF fiscal e VAB das Contas Regionais.

## Próximas etapas recomendadas

1. Construir uma **série histórica canônica apenas com IPM definitivos**, preservando ano de distribuição, ano-base/apuração quando disponível, fonte e status.
2. Obter da fonte oficial a **série histórica de Valor Adicionado de São Borja** e documentar a semântica de cada campo antes da integração.
3. Se houver detalhamento oficial suficiente, decompor os componentes do IPM e explicar mudanças entre anos sem misturar pesos de metodologias distintas.
4. Reconciliar o IPM com a **quota-parte monetária do ICMS efetivamente transferida** ao município, mantendo separados índice e fluxo financeiro.
5. Somente depois avaliar se há base metodológica para relacionar fiscalidade à estrutura de matriz/filial, emprego e remuneração.

## Controle do Caderno-Base

Esta auditoria motivou a criação de `caderno_base_territorial_v007_fiscalidade_ipm_20260907`, preservando a v006 como histórica. A v007 contém a aba `Fiscalidade_IPM` e registra explicitamente que o estágio fiscal ainda está em **auditoria inicial** e que a série detalhada de VAF/IPM ainda não foi canonizada.
