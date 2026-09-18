# Cesta Nutricional Familiar — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Auditar a Cesta Nutricional Familiar como fonte complementar para análise de custo alimentar, perfis familiares e capacidade potencial de consumo, preservando a granularidade regional publicada e sem alterar os cadernos ou bases canônicas do SBMI.

## Fontes oficiais

- Receita Dados: https://receitadados.sefaz.rs.gov.br/desenvolve-rs/cesta-nutricional-familiar/
- PUCRS DataSocial: https://www.pucrs.br/datasocial/cesta-nutricional-familiar/
- NT CIET 02/2026 — Preço da Cesta de Alimentos (PCA-RE): https://receitadoc.sefaz.rs.gov.br/media/axphdecc/nt02_26-pre%C3%A7os-da-cesta-de-alimentos-v20260203.pdf

## Achados observados — etapa 3A

### Produção institucional

O projeto é uma parceria entre:
- Secretaria da Fazenda/Receita Estadual do RS;
- PUCRS DataSocial;
- Grupo de Pesquisa em Comportamento Alimentar da PUCRS.

A Receita Estadual fornece a base de preços e confecciona o painel interativo; a PUCRS DataSocial realiza análises dos movimentos de preços; o GPCA/PUCRS responde pela composição técnica da cesta e análises nutricionais.

### Fonte de preços

Os preços são monitorados por NFC-e, abrangendo o mercado formalizado.

### Personalização

O painel permite simular o custo da cesta segundo:
- composição familiar;
- hábito alimentar regular ou vegetariano;
- faixa etária;
- região geográfica por COREDE.

### Relatórios mensais

Na página pública da PUCRS DataSocial estão listados relatórios de:
- junho/2026;
- julho/2026;
- agosto/2026;
- setembro/2026.

A página informa como cesta de referência do relatório uma família formada por:
- 2 adultos;
- alimentação regular;
- 1 criança de 4 a 10 anos.

Essa composição é referência editorial do relatório e não deve ser confundida com a única configuração disponível no painel.

### Relação com o PCA-RE

A NT CIET 02/2026 define o PCA-RE como o valor médio mensal dispendido por uma pessoa residente na área geográfica considerada (RS ou COREDE) para a aquisição de produtos alimentícios.

O PCA-RE:
- deriva dos preços processados no Preços Dinâmicos;
- usa consumo per capita como ponderador;
- é calculado para RS e 28 COREDES;
- possui publicação diária e mensal nos painéis e mensal nos boletins.

### Geografia

A NT CIET 02/2026 confirma:
- São Borja pertence ao COREDE Fronteira Oeste;
- os preços agregados públicos são disponibilizados por COREDE e RS.

Regra SBMI:
- usar `COREDE Fronteira Oeste — região de referência de São Borja`;
- nunca converter a cesta regional em custo municipal observado;
- qualquer cruzamento com renda municipal será classificado como **indicador calculado pelo SBMI**, com limitação territorial explícita.

## Aplicações mercadológicas potenciais

- custo alimentar por perfil familiar;
- pressão do custo de alimentação sobre renda disponível;
- comparação entre perfis de famílias;
- vulnerabilidade de consumo;
- disponibilidade potencial para consumo discricionário;
- leitura transversal para bens essenciais e alimentação fora do lar.

## Cálculos possíveis no SBMI

Exemplo conceitual:

`comprometimento_alimentar = custo_cesta_regional / renda_referencia * 100`

Esse cálculo será classificado como **calculado**, não observado, e só será produzido após definição compatível da renda de referência.

## Limitações

- geografia publicada é COREDE, não município;
- cesta nutricional é um modelo customizado de consumo, não gasto efetivo observado de uma família específica;
- renda municipal e custo regional possuem abrangências geográficas distintas;
- não inferir causalidade entre aumento de preços e retração de outros mercados sem evidência adicional.

## Próxima subetapa — 3B

Extrair, quando possível de forma reproduzível:
- custo da cesta de referência para Fronteira Oeste e RS;
- variação mensal;
- componentes com maior contribuição para variação;
- diferenças por composição familiar selecionada.

Toda observação deve registrar período, configuração familiar, hábito alimentar, geografia, valor, unidade e fonte.
