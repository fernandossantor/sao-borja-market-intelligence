# Auditoria Receita Estadual RS — integração exploratória SBMI

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico

## Objetivo

Avaliar, sem alterar qualquer base, planilha, caderno ou documento consolidado do São Borja — Inteligência Mercadológica, quais produtos públicos da Receita Estadual do Rio Grande do Sul podem acrescentar informação territorial e mercadológica ao projeto.

Nenhum dado desta auditoria deve ser tratado como canônico antes de validação metodológica, extração reproduzível e decisão explícita de promoção.

## Regra de preservação

- Não modificar o Caderno-Base vigente nem os quatro cadernos setoriais.
- Não substituir dados já canonizados.
- Não alterar o PR #41 nem sua condição de aberto/draft.
- Trabalhar em camada paralela de auditoria.
- Qualquer dado novo permanece como `exploratório` até auditoria e promoção.
- Registrar fonte, período, unidade, abrangência geográfica e limitações.

## Ambiente

Branch exploratória:

`explore/receita-estadual-rs-market-intel-v1`

Base: `6f3d94b620a1e9368a187eff343bf8572e45d1b5`, head do PR #41 em 2026-09-17.

Estado confirmado do PR #41 em 2026-09-17:

- `state = open`
- `draft = true`
- `merged = false`

## Fontes em auditoria

### Boletim Econômico-Tributário

Fonte oficial:  
https://receitadoc.sefaz.rs.gov.br/boletins/

A Receita Estadual informa que o BET fornece panorama da atividade econômica estadual, incluindo nível de atividade e demografia de estabelecimentos por setor, categoria e **COREDE/municípios**, além da arrecadação.

**Granularidade potencial**
- Município: sim
- COREDE: sim
- RS: sim

**Prioridade:** primeira fonte a ser testada para extração direta de São Borja.

### Preços Dinâmicos da Receita Estadual

Fonte oficial:  
https://receitadados.sefaz.rs.gov.br/desenvolve-rs/precos-dinamicos-da-re/

Divulga preços pagos em transações formalizadas e séries temporais em Power BI.

**Granularidade pública relevante**
- Município: não confirmada como publicada
- COREDE: sim
- RS: sim

**Aplicação potencial:** pressão de preços, sazonalidade e ambiente econômico do consumo.

### Cesta Nutricional Familiar

Fonte oficial:  
https://receitadados.sefaz.rs.gov.br/desenvolve-rs/cesta-nutricional-familiar/

O painel permite simular custo da cesta por composição familiar, hábito alimentar, faixa etária e região geográfica em COREDEs.

**Granularidade**
- Município: não
- COREDE: sim

**Aplicação potencial:** custo alimentar, comprometimento potencial da renda e capacidade de consumo discricionário.

### Radar do Mercado da Receita Estadual

Fonte oficial:  
https://receitadados.sefaz.rs.gov.br/desenvolve-rs/radar-do-mercado-da-receita-estadual/

Produto público do Desenvolve-RS em Power BI.

**Granularidade**
- Município: existe em parte do modelo/visualizações, ainda a auditar indicador por indicador
- COREDE: a confirmar por indicador
- RS: sim

**Aplicação potencial:** demanda por NCM, produção interna, entradas interestaduais, importações, fornecedores, concorrência e lacunas produtivas.

## Hierarquia territorial

1. São Borja — usar sempre que a fonte publicar município.
2. COREDE Fronteira Oeste — usar quando a menor granularidade pública for regional.
3. Rio Grande do Sul — benchmark estadual.

**Regra:** nunca converter dado de COREDE em dado municipal.

## Ordem de trabalho

1. **BET** — indicadores extraíveis para São Borja, períodos e série reproduzível.
2. **Preços Dinâmicos** — produtos, periodicidade, histórico e Fronteira Oeste.
3. **Cesta Nutricional** — perfis, periodicidade e Fronteira Oeste.
4. **Radar** — auditoria página por página: indicador → período → unidade → granularidade → filtros → extração.

## Próxima tarefa operacional

> Extrair e auditar os indicadores do Boletim Econômico-Tributário que sejam diretamente selecionáveis para o município de São Borja.

