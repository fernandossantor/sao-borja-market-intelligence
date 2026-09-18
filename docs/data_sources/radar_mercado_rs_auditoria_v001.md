# Radar do Mercado da Receita Estadual — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Auditar o Radar do Mercado da Receita Estadual como fonte de inteligência mercadológica para estrutura de demanda, origem da oferta, fluxos comerciais, concorrência e oportunidades produtivas.

## Fontes

- Painel oficial: https://receitadados.sefaz.rs.gov.br/desenvolve-rs/radar-do-mercado-da-receita-estadual/
- Nota Técnica CIET 05/2026: link publicado no Receita.doc
- Material institucional sobre a versão ampliada lançada em 30/06/2026.

## Achados observados — etapa 4A

### Natureza

A versão ampliada de 2026 utiliza a base de NF-e para produzir indicadores econômicos estratégicos da indústria.

A divulgação institucional informa atualização mensal e utilização da totalidade das operações fiscais registradas no Estado.

### Dimensões confirmadas

O painel permite, conforme documentação institucional:
- visualizar perfil de vendas da indústria gaúcha;
- mapear origem dos produtos comprados no RS;
- identificar destino da produção gaúcha por UF e país;
- identificar mercados consumidores;
- identificar principais concorrentes;
- medir composição de mercado/market share por produto;
- distinguir origem entre produção local, compras de outras UFs e importações;
- mapear carências de atendimento da demanda pela produção local;
- classificar dependência externa;
- identificar oportunidades de expansão, substituição de importações e fortalecimento de cadeias.

### Unidade de produto

A documentação e exemplos publicados usam produtos/NCM como eixo analítico.

### Geografia

Foi confirmada evidência de dimensão municipal em visualizações derivadas do Radar, mas a granularidade não deve ser presumida para todos os indicadores.

Status atual:
- RS: confirmado;
- UF/país em fluxos: confirmado;
- município: presente em parte das visualizações/modelo;
- COREDE: ainda não confirmado para todos os indicadores.

### Regra SBMI

Não afirmar que um indicador é municipal apenas porque outro visual do Radar usa município.

A auditoria deverá registrar página por página:

`pagina | indicador | conceito | produto/NCM | periodo | unidade | geografia_disponivel | filtros | extraivel | limitacao`

## Aplicações prioritárias ao SBMI

1. **Lacunas de oferta**
   - demanda relevante no RS;
   - baixa produção interna;
   - dependência de outras UFs/importações.

2. **Cadeias relacionadas a São Borja**
   - cruzar produtos/NCM com setores/CNAEs locais;
   - avaliar se há produção local em mercados com dependência externa estadual;
   - identificar potenciais fornecedores e concorrentes.

3. **Benchmark territorial**
   - quando houver município, comparar São Borja com outros polos;
   - quando não houver município, manter o indicador estadual como contexto de mercado.

## Limitações

- o painel é orientado principalmente à indústria e fluxos de mercadorias;
- não representa diretamente demanda final das famílias;
- market share estadual não é market share municipal;
- produto/NCM e CNAE são classificações distintas e exigem mapeamento metodológico;
- oportunidade de mercado não equivale a viabilidade econômica de investimento.

## Próxima subetapa — 4B

Auditar o painel interativo página por página e construir uma matriz de granularidade e filtros antes de qualquer extração setorial.
