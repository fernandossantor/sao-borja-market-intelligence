# Auditoria do inventário POM de empresas — 18/09/2026

**Status:** exploratório — não canônico  
**Fonte:** planilha “Empresas de Varejo de São Borja” no Drive do projeto  
**Finalidade:** avaliar a qualidade do inventário antes de utilizá-lo em diagnósticos setoriais.

## 1. Resultado geral

A planilha contém quatro blocos com níveis de completude muito diferentes:

- bens essenciais: 54 linhas, todas nomeadas;
- saúde/higiene/cuidados pessoais: 41 linhas, todas nomeadas;
- bens não essenciais: 120 linhas, todas nomeadas;
- serviços/alimentação fora do lar: 80 linhas, mas apenas 3 empresas nomeadas e **77 placeholders**.

Consequência:

**o número 80 não pode ser tratado como número de operadores de serviços/alimentação.**

Para esse mercado, o SBMI deve continuar usando RFB, RAIS e o POM específico.

## 2. Saúde, higiene e cuidados — oferta varejista finalmente delimitada, mas ainda não “ativa”

O inventário contém 41 linhas nomeadas.

Agrupamento textual SBMI:
- farmácia/drogaria: 22 linhas;
- óticas: 9;
- produtos médicos/ortopédicos: 1;
- perfumaria: 5;
- cosméticos: 4.

### Auditoria de CNPJ

- 39 linhas têm CNPJ extraível do texto;
- 37 CNPJs extraíveis são únicos;
- foram detectados 2 pares de duplicidade de CNPJ;
- 2 linhas não fornecem CNPJ extraível pelo parser;
- uma linha de cosméticos informa explicitamente que o CNPJ encontrado foi baixado em julho de 2025.

Farmácia/drogaria:
- 22 linhas;
- 20 CNPJs únicos extraíveis;
- 2 duplicidades de CNPJ.

### Interpretação permitida

O inventário prova que o projeto já possui uma **base nominal detalhada** para a oferta de saúde/higiene.

Ele não prova que existam exatamente 41 estabelecimentos ativos no presente.

Para fechar a estrutura competitiva, é necessário:
1. deduplicar por CNPJ/unidade;
2. consultar situação cadastral atual;
3. classificar matriz local/externa;
4. separar rede/independente apenas por critério documental;
5. manter cosméticos/perfumaria/ótica separados do varejo farmacêutico.

## 3. Bens não essenciais

O inventário contém 120 linhas nomeadas.

Auditoria:
- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos extraíveis;
- 16 linhas sem CNPJ extraível;
- uma duplicidade de CNPJ detectada;
- ao menos duas linhas trazem nota explícita de CNPJ baixado.

Agrupamentos exploratórios por texto:
- moda/calçados: 61 linhas;
- pet/agro: 22;
- joias/ótica/relojoaria: 11;
- eletro/eletrônicos/mobile: 8;
- presentes/utilidades/departamento: 7;
- papelaria: 3;
- demais grupos menores.

Esses agrupamentos são **analíticos do SBMI**, não categorias oficiais.

### Implicação

O inventário já é suficientemente rico para orientar uma próxima auditoria por submercado, sobretudo:
- moda/calçados;
- pet/agro;
- eletroeletrônicos;
- joias/ótica;
- móveis/casa.

Mas o número bruto de 120 não deve ser promovido como estoque empresarial ativo.

## 4. Bens essenciais

Há 54 linhas nomeadas.

A camada específica de bens essenciais já passou por auditoria documental mais forte:
- 52 CNPJs documentais validados;
- 2 pendências já registradas.

Portanto, a simples taxa de CNPJ extraível desta planilha não substitui a base específica já auditada.

## 5. Serviços/alimentação — bloqueio

A seção possui:
- 80 linhas;
- 3 empresas nomeadas;
- 77 placeholders.

Regra:
**não usar a planilha para contagem, market mapping ou inferência de oferta neste mercado.**

Fontes adequadas:
- RFB/CNPJ 2026-08;
- RAIS;
- POM 2026;
- Cadastur, quando aplicável;
- pesquisa/inventário futuro especificamente construído para o setor.

## 6. Consequência para os diagnósticos POM

### Saúde/higiene

O status muda de “estrutura varejista totalmente desconhecida” para:

**inventário nominal disponível, porém estoque ativo e controle territorial ainda não auditados.**

### Bens não essenciais

A análise pode ser desagregada por submercado usando o inventário como mapa de investigação, sem tratá-lo como censo vigente.

### Alimentação/serviços

O inventário geral é inadequado; manter fontes administrativas.

Arquivo estruturado:
`inventario_pom_varejo_auditoria_20260918_v001.csv`.
