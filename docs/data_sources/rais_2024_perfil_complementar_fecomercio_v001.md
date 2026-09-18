# RAIS 2024 — perfil complementar inspirado nas lacunas do Observatório Fecomércio

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Verificar quais indicadores identificados no Observatório do Comércio Fecomércio-RS/IFEP-RS podem ser reproduzidos diretamente a partir da fonte primária **MTE/RAIS 2024** já existente no SBMI.

Não se pretende reproduzir a metodologia proprietária do IFEP-RS quando ela não está documentada. O objetivo é reduzir dependência de uma fonte secundária quando o mesmo conceito puder ser calculado de modo auditável.

## Arquivos auditados

### Microdados consolidados

Drive ID:
`1hUlMY-6OfvFmbkzx6TBwhmeMuESRx_Ki`

Arquivo:
`rais_consolidated.csv`

A parcela de microdados RAIS 2024 possui 18.923 linhas com `_source_file = RAIS SB 2024.csv`.

### Pipeline do projeto

`src/rais_engine.py`

Achado:
o pipeline:
1. carrega o arquivo;
2. aplica filtro territorial;
3. elimina colunas totalmente vazias;
4. adiciona metadados de fonte;
5. concatena e exporta.

**Não há recodificação de sexo, idade, tempo de emprego ou indicador do Simples nessa etapa.**

`src/domains/rais/semantic/rais_canonicalizer.py` mapeia:
- `Sexo - Código → gender`;
- `Idade → age`;
- `Tempo Emprego → tenure`;
- remuneração e jornada.

O indicador do Simples não está incluído no mapeamento canônico histórico.

## Universo reproduzido

Filtro utilizado pela v028:

`Ind Vínculo Ativo 31/12 - Código = 1`

e

`Ind Vínculo Abandonado - Código != 1`

Resultado:
**13.125 vínculos**.

Esse total reproduz exatamente o universo primário documentado na v028.

Unidade:
**vínculo formal**, não pessoa única.

## Sexo

O layout oficial da RAIS documenta:
- código 1 = Masculino;
- código 2 = Feminino.

No universo primário:
- homens: **7.665 vínculos — 58,40%**;
- mulheres: **5.460 vínculos — 41,60%**.

Fórmula:
`participação = vínculos da categoria / 13.125 × 100`.

## Idade

Todos os 13.125 vínculos possuem valor utilizável no campo `Idade`.

- média: **39,60 anos**;
- mediana: **38 anos**.

Faixas analíticas criadas pelo SBMI, portanto não oficiais:
- até 24: **12,42%**;
- 25–34: **27,06%**;
- 35–44: **25,78%**;
- 45–54: **19,82%**;
- 55+: **14,93%**.

## Tempo de emprego

O layout local `RAIS_vinculos_layout.xls` descreve `Tempo Emprego` como tempo de emprego do trabalhador e explicita que, quando acumulado, representa a soma dos **meses**.

Todos os 13.125 vínculos possuem valor utilizável.

- média: **61,92 meses**;
- mediana: **28 meses**.

Faixas SBMI:
- até 12 meses: **30,27%**;
- 13–36 meses: **26,86%**;
- 37–60 meses: **13,17%**;
- 61–120 meses: **13,21%**;
- mais de 120 meses: **16,49%**.

Essas distribuições descrevem **antiguidade dos vínculos ativos em 31/12**, não rotatividade.

## Remuneração por sexo

Foi calculada apenas para remunerações nominais médias anuais positivas.

### Média

Homens:
- n = 7.176;
- média = **R$ 3.334,00**.

Mulheres:
- n = 5.219;
- média = **R$ 2.961,37**.

Diferença bruta:
`(2.961,37 / 3.334,00 - 1) × 100 = -11,18%`.

### Mediana

Homens:
**R$ 2.689,55**.

Mulheres:
**R$ 2.241,81**.

Diferença bruta:
`(2.241,81 / 2.689,55 - 1) × 100 = -16,65%`.

### Regra de interpretação

Essas diferenças são **descritivas e não ajustadas**.

Não permitem concluir discriminação salarial, porque não controlam:
- ocupação;
- setor;
- jornada;
- escolaridade;
- idade;
- tempo no emprego;
- tipo de vínculo;
- composição público/privado.

A utilidade imediata é identificar uma diferença a ser decomposta, não explicar sua causa.

## Indicador Simples — BLOQUEADO PARA INTERPRETAÇÃO

O arquivo RAIS 2024 contém:
- código bruto 0: **10.087 vínculos**;
- código bruto 1: **3.038 vínculos**.

Entretanto, o layout oficial de geração da declaração RAIS disponível publicamente documenta:
- 1 = optante;
- 2 = não optante.

O microdado utilizado no SBMI apresenta 0/1.

Como o `rais_engine.py` não recodifica esse campo, a diferença não foi criada pelo pipeline de consolidação. Pode decorrer do formato de disseminação dos microdados, mas o dicionário específico dessa codificação ainda não foi localizado de forma suficientemente verificável.

**Decisão metodológica:** não converter 0/1 em optante/não optante e não calcular participação do emprego em empresas do Simples até resolver a codificação.

## Relação com o Observatório Fecomércio

Passam de lacuna para **reproduzíveis diretamente pela RAIS**:
- participação por sexo;
- idade;
- tempo de vínculo;
- remuneração por sexo;
- faixas de jornada — já presentes na v028.

Continuam dependentes de auditoria adicional:
- emprego × Simples;
- rotatividade do trabalho na fórmula IFEP;
- tempo médio de atividade das empresas;
- concentração territorial;
- vendas;
- receitas;
- despesas;
- MEI.

## Fontes

MTE/RAIS 2024 — microdados existentes no acervo SBMI.

Layout oficial RAIS:
https://www.rais.gov.br/sitio/rais_ftp/LayoutRAIS2022.pdf

Layout local de microdados:
Drive ID `1h9kzXuBF_JKpmX4s2Q-ODvjZ-tEmoQ3J` — `RAIS_vinculos_layout.xls`.

Código de processamento do próprio projeto:
- `src/rais_engine.py`;
- `src/domains/rais/semantic/rais_canonicalizer.py`.

## Limitações

- RAIS mede vínculos formais, não indivíduos únicos;
- o recorte é dezembro/2024 para perfil de vínculos ativos;
- múltiplos vínculos podem representar a mesma pessoa;
- diferenças de remuneração são brutas;
- faixas de idade e tempo criadas nesta auditoria são categorias analíticas SBMI, não categorias oficiais;
- nenhum indicador desta camada foi promovido ao Caderno-Base.
