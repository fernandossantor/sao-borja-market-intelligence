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



### Observatório do Comércio — Fecomércio-RS / IFEP-RS

Fonte principal:  
https://observatorio.fecomercio-rs.org.br/page/home

**Natureza da fonte:** plataforma secundária/integradora produzida pelo Instituto Fecomércio-RS de Pesquisas (IFEP-RS), com indicadores próprios e integração de bases oficiais.

A documentação pública sobre o lançamento informa que o Observatório reúne dados sobre empresas/estabelecimentos, trabalho, receitas e despesas e permite análises segmentadas por região e atividade econômica. Também divulga indicadores próprios do IFEP-RS, entre eles rotatividade, concentração territorial e tempo de vida/atividade das empresas.

**Origem dos dados:** a própria plataforma possui área “Fonte dos dados”. Nesta auditoria, o mapa detalhado de origem deve ser transcrito e validado diretamente nessa área antes de qualquer promoção. Fontes confirmadas externamente para a plataforma incluem Receita Federal e Ministério do Trabalho. Não presumir que todos os indicadores derivam dessas duas fontes.

**Regra de uso no SBMI:**
- quando o indicador apenas reorganizar uma base primária já utilizada pelo SBMI, manter a fonte primária como referência canônica e usar o Observatório como interface de conferência/benchmark;
- quando o indicador for calculado pelo IFEP-RS, registrar explicitamente IFEP-RS como produtor do indicador e documentar fórmula/metodologia, se publicada;
- preservar granularidade territorial original;
- não substituir séries já auditadas sem comparação metodológica.

**Granularidade potencial:** regional e por atividade econômica confirmada; recorte municipal deve ser auditado dentro da própria plataforma antes de uso.

**Aplicações potenciais:** demografia empresarial, emprego, receitas/despesas, rotatividade, concentração territorial, sobrevivência/tempo médio de atividade e benchmarking setorial.

## Atualização da ordem de trabalho

O Observatório Fecomércio-RS/IFEP-RS entra como fonte transversal de validação e complementação, sem interromper a sequência já definida:

1. **BET** — concluir auditoria de indicadores municipais de São Borja;
2. **Preços Dinâmicos** — produtos, periodicidade, histórico e Fronteira Oeste;
3. **Cesta Nutricional** — perfis, periodicidade e Fronteira Oeste;
4. **Radar** — auditoria por indicador e granularidade;
5. **Observatório Fecomércio-RS/IFEP-RS** — auditar “Fonte dos dados”, granularidade municipal/regional e indicadores próprios; comparar com fontes primárias já canônicas.

## Atualização integrada — 18/09/2026 — PDFs recebidos

Foram recebidos e auditados cinco documentos oficiais:
- NT CIET 05/2026 — Radar de Mercado;
- BET agosto/2026;
- BET Comércio Exterior ed.07;
- Preços Dinâmicos ed.25 / agosto/2026;
- Volume de Vendas da Indústria ed.03 / 1º trimestre de 2026.

### Principais avanços

1. O método do Radar está fechado, inclusive fórmula de Part.RS, faixas de dependência, janela LTM, portfólio Top 90% e dicionário das seis bases CSV.
2. A Fronteira Oeste passa a ter observações correntes de agosto/2026 para estabelecimentos, vendas industriais, realizado vs previsto, PCA/ICA e comércio exterior.
3. O BET Comércio Exterior confirma granularidade por COREDE.
4. O boletim de Preços permite comparar Fronteira Oeste x RS e faixas de renda.
5. A edição 03 de vendas industriais confirma desempenho relativamente mais forte de alimentos no 1º trimestre de 2026.

### Artefatos novos

- `radar_nt_ciet_05_2026_dicionario_v001.csv`
- `precos_dinamicos_fronteira_oeste_agosto2026_v001.csv`
- `bet_ed29_fronteira_oeste_agosto2026_v001.csv`
- `bet_comex_ed07_fronteira_oeste_v001.csv`
- `volume_vendas_industria_rs_1t2026_selecionados_v001.csv`
- `receita_rs_sintese_exploratoria_20260918_v001.md`

### Próxima prioridade

A principal pendência operacional é baixar as bases CSV da página **Dados Abertos** do Radar e preencher os sete NCMs do piloto do arroz.

Nenhuma base ou caderno canônico foi alterado.
