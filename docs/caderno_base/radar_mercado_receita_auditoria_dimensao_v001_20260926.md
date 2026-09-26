# Radar do Mercado da Receita Estadual — auditoria para dimensão de mercado — v001

**Data:** 2026-09-26  
**Fonte:** Receita Estadual do Rio Grande do Sul — DESENVOLVE-RS — Radar do Mercado  
**Objeto:** avaliar se o painel público fornece faturamento/mercado em nível municipal ou outra granularidade útil aos cinco cadernos do SBMI.  
**Status:** auditoria de esquema público concluída.

## 1. Resultado principal

O Radar do Mercado é uma fonte **muito rica em produto/NCM, atividade econômica, origem/destino geográfico em nível estadual/UF/país e composição do mercado**, mas a auditoria do modelo público **não encontrou dimensão município nem COREDE**.

Assim, o Radar:
- não fornece diretamente faturamento de São Borja;
- não desbloqueia market share empresarial municipal;
- não deve ser usado para desagregar o envelope DFe de São Borja por aplicação de participações estaduais.

Seu maior valor imediato para o SBMI é:
1. **taxonomia de produtos/NCM e categorias**;
2. análise de dependência do RS em relação a outras UFs/exterior;
3. benchmark estadual de composição e oportunidades;
4. apoio à definição dos NCMs a solicitar em uma extração municipal agregada.

## 2. Evidência observada no modelo semântico

O Power BI público expõe, entre outras, as entidades:

### `f_visao3`
Campos:
- `emit_atividade`;
- `emit_classe`;
- `emit_setor`;
- `anomes`;
- `Data`;
- `tipo_operacao`;
- `cod_ncm`;
- `ncm_descr`;
- `vlr_ncm`;
- `nemit`;
- `ndest`;
- `corte_sigilo`;
- `vlr_ncm_sigilo`.

### `f_visao4`
Inclui:
- atividade/classe/setor;
- NCM;
- período;
- tipo de operação;
- valor;
- número de emitentes/destinatários;
- controle de sigilo.

### Dimensão de NCM — `d_ncms`
Campos:
- `ncm8`;
- `ncm4`;
- `grupo_afinidade_final`;
- `codxdescr_ncm8`.

### Camadas geográficas
Entidades específicas contêm:
- UF de destino;
- UF de emissão;
- código de país;
- bloco econômico.

Não foram observadas propriedades de:
- município;
- código IBGE municipal;
- COREDE.

## 3. O que o painel chama de “market share”

O modelo contém medidas e entidades com nomes como:

- `Barra SVG Mkt_Share NCM`;
- `Valor Total Entradas Mkt_Share NCM`;
- `Barra SVG Mkt_Share Setores`;
- `Valor Total Entradas Mkt_Share Setores`;
- `f_mkt_share_ncm_ufs_paises`;
- `f_mkt_share_setores_ufs_paises`;
- `f_mkt_share_ncm`;
- `f_mkt_share_setores`.

**Controle conceitual:** a presença da expressão “market share” no painel **não autoriza interpretar essas medidas como participação de empresas**.

As entidades observadas estruturam o mercado por:
- atividade/setor;
- NCM;
- UF;
- país/bloco;
- tipo de operação;
- período;
- valor.

Não foi observado identificador de empresa como dimensão de participação individual. Portanto, para o SBMI, essas medidas devem ser tratadas como **composição/participação geográfica ou setorial do mercado do RS**, até que a fórmula de cada medida seja auditada.

Elas não constituem numerador empresarial para market share em São Borja.

## 4. Conteúdo visível do painel

Na execução auditada, o painel informava mês de referência **agosto/2026** e apresentava, entre outros elementos:

- “Valor Financeiro de Aquisições de Fora do RS”;
- categorias/NCM;
- “Grau de Dependência”;
- valores de aquisição;
- categorias como Medicamentos, Eletrodomésticos, Instrumentos Médicos, Cereais e Grãos, entre outras.

Isso reforça que o objetivo do Radar é analisar estrutura de mercado, dependência, fornecedores, consumidores, concorrentes e oportunidades em perspectiva estadual.

## 5. Relevância para os cinco cadernos

### Bens Essenciais
Pode apoiar:
- seleção de NCMs/categorias alimentares;
- dependência do RS;
- contexto de fornecedores.

Não substitui:
- DR de São Borja;
- faturamento municipal;
- preço local;
- market share municipal.

### Saúde/Higiene
É particularmente útil para construir taxonomia de:
- medicamentos;
- produtos farmacêuticos;
- instrumentos/produtos relacionados;
- outras categorias mapeáveis por NCM.

Pode ajudar a definir o conjunto de NCMs a solicitar à Receita Estadual para São Borja.

### Bens Não Essenciais
Há categorias como eletrodomésticos e outros grupos de afinidade. O Radar pode ajudar a fechar o crosswalk **NCM → módulo de mercado**, sem atribuir os valores estaduais ao município.

### Serviços
Utilidade menor, pois o eixo principal do Radar é mercadorias/NCM. Para Serviços, NFS-e municipal continua prioritária.

### Alimentação Fora do Lar
A atividade econômica do emitente pode aparecer, mas NCM não representa adequadamente toda a experiência de serviço de alimentação. A divisão CNAE 56 na camada DFe regional é mais diretamente útil como benchmark fiscal do que o Radar por produto.

## 6. Descoberta metodológica relevante

O Radar demonstra que a própria Receita Estadual mantém, em sua arquitetura analítica, uma camada que relaciona:

`atividade/classe/setor do emitente × NCM × período × tipo de operação × valor`.

Isso fortalece tecnicamente a solicitação do SBMI por uma extração **agregada** que associe território municipal a CNAE/NCM, porque a taxonomia produto-atividade já é usada institucionalmente em outro produto público da Receita.

Isso **não prova** que o município esteja presente no mesmo banco ou que a Receita possa divulgar essa interseção. É apenas evidência de que atividade e NCM são dimensões existentes na arquitetura analítica pública.

## 7. Limite territorial

A auditoria textual e de esquema encontrou:
- ocorrências extensas de NCM, setor, atividade, produto, vendas/mercado;
- dimensões UF e país;
- **zero propriedades municipais identificadas no modelo central auditado**;
- **zero propriedades COREDE identificadas**.

Portanto, não usar o Radar para produzir:
- `São Borja × NCM × valor`;
- `São Borja × setor × valor`;
- market share de empresa local.

## 8. Integração recomendada ao SBMI

Classificar o Radar como:

**BENCHMARK ESTADUAL / FONTE DE TAXONOMIA DE PRODUTO E ESTRUTURA DE MERCADO**.

Uso prioritário:
- construir crosswalk `NCM → módulos dos cadernos`;
- identificar categorias de maior relevância para pedido de dados;
- analisar dependência/fornecimento estadual quando essa dimensão for pertinente ao diagnóstico.

Não classificar como:
- faturamento observado de São Borja;
- demanda residente;
- mercado capturado municipal;
- market share empresarial.

## 9. Rastreabilidade

Workflow:
`.github/workflows/receita-radar-mercado-schema-discovery-v1.yml`

Execução:
- run: `36263753330`;
- job: `108464360510`;
- artifact: `10912374240`;
- digest: `sha256:e98ed4ca5dc65988bc1ae7dee19a32e9b96585e9d31bb422aff77a97940aeb1f`.

Google Drive:
- `SBMI_Receita_Radar_Mercado_schema_v001.zip`;
- ID: `1GzoYYHsNEh4ZbjirbSVpmPPkvBq4Frw6`.

Fonte pública:
https://receitadados.sefaz.rs.gov.br/desenvolve-rs/radar-do-mercado-da-receita-estadual/

## 10. Próximo uso concreto

O próximo passo defensável não é extrair um “market share de São Borja” do Radar.

É usar a dimensão `d_ncms` e as categorias do painel para construir um **crosswalk NCM dos quatro mercados de mercadorias** e incorporá-lo à especificação de pedido `São Borja × NCM × valor` à Receita Estadual.
