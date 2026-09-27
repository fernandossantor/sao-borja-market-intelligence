# Checkpoint — Pacote B — QA de consistência factual concluído — 27/09/2026

## 1. Escopo

Executar exclusivamente o QA de consistência factual entre:

- Caderno-Base Territorial v029;
- Factsheet Territorial v002;
- Storyboard Territorial v002;
- Caderno Geral — Report Empresarial v004;
- abas de controle da planilha v029.

Este pacote não executa revisão de fluidez, estilo, redundância ou diagramação. Esses itens ficam para o Pacote C.

## 2. Cadeia canônica confirmada

### Taxonomia Radar

- run: `36326001762`;
- 110 grupos de afinidade;
- 13.829 NCM8;
- grupo Químicos Orgânicos reconsultado após detecção de truncagem da janela de 10.000 linhas.

### Camada curated

- run: `36326283761`;
- 18 validações PASS.

### Camada analysis

- run: `36326631575`;
- 12 validações PASS.

Runs anteriores permanecem apenas para linhagem quando explicitamente marcados como históricos/superseded.

## 3. Correções efetuadas neste pacote

### Factsheet Territorial v002

Foi corrigida a identificação da camada analítica:

- antes: `public-market-series-analysis-v001`;
- depois: `public-market-series-analysis-v002`;
- run permanece corretamente `36326631575`.

Nenhum valor analítico foi alterado.

### Series_publicas_v029

Foi corrigido o rótulo da camada:

- antes: `public-market-series-analysis-v001`;
- depois: `public-market-series-analysis-v002`.

A próxima frente foi atualizada para o Pacote C — QA editorial final.

### Auditoria_series_v029

As linhas de controle de DFe, Cesta e período Radar ainda apontavam para a antiga curated `36279321664`.

Foram atualizadas para a curated canônica `36326283761`.

Os checks permanecem PASS e seus valores não mudaram.

### Rastreabilidade_v029

Foram explicitamente marcados como **SUPERSEDED / HISTÓRICO**:

- curated v001 — run `36279321664`;
- diagnóstico inicial Drive pré-correção;
- diagnóstico inicial GitHub pré-correção;
- analysis v001 — run `36280101723`;
- checkpoints de 26/09 já superados.

Os registros foram preservados para linhagem; não foram apagados.

## 4. Consistência dos sinais DFe

Comparação 01/01 a 14/09/2026 versus o mesmo período de 2025.

### CT-e

- quantidade: +15,47%;
- valor nominal: +29,11%;
- valor médio por documento: +11,81%.

### NF-e

- quantidade: +13,30%;
- valor nominal: +17,24%;
- valor médio por documento: +3,48%.

### NFC-e

- quantidade: +2,87%;
- valor nominal: -2,22%;
- valor médio por documento: -4,95%.

Os valores estão consistentes entre Caderno-Base, Factsheet, Caderno Geral, Resumo e Teses. O Storyboard usa síntese reduzida, sem valor contraditório.

Escala: São Borja/RS.

Limite preservado: DFe não mede quantidade física, consumo real, inflação ou market share.

## 5. Consistência da Cesta Alimentos

H1/2026 versus H1/2025:

- 80 produtos;
- mediana simples das variações: +2,46%;
- média simples: +2,28%;
- 44 produtos em alta;
- 36 produtos em queda.

Escala: COREDE Fronteira Oeste.

Limite preservado: a distribuição simples das variações não é índice de inflação e COREDE Fronteira Oeste não equivale ao município de São Borja.

## 6. Consistência do benchmark Radar/RS

Jan–ago/2026 versus jan–ago/2025, valor nominal publicado não suprimido:

- Bens Essenciais / CORE: -1,27%;
- Bens Não Essenciais / CORE: -2,97%;
- Saúde/Higiene/Cuidados Pessoais / CORE: +16,12%;
- Serviços / ADJACENT: +6,48%.

Escala: Rio Grande do Sul.

Limites preservados:

- Radar/RS não é trajetória municipal de São Borja;
- não representa market share municipal;
- Serviços/ADJACENT representa mercadorias complementares e não prestação de serviços.

## 7. Consistência taxonômica

Os artefatos ativos convergem para:

- taxonomia completa: 13.829 NCM8;
- 110 grupos;
- cobertura monetária da Composição: 99,999817%;
- residual publicado não suprimido: R$ 2.074.800;
- 98,676162% do residual publicado concentrado em códigos prefixados `00`;
- 6 NCM29 residuais;
- 13 linhas NCM29;
- todas sob sigilo;
- valor publicado não suprimido dos NCM29 residuais = R$ 0.

Controle preservado: R$ 0 publicado sob sigilo não significa zero econômico.

## 8. Estado dos documentos ativos

### Caderno-Base Territorial v029

Nenhuma referência ativa a run antigo ou cobertura taxonômica pré-correção foi localizada.

### Factsheet Territorial v002

Após a correção de versão da camada, não permanece referência ativa a `analysis-v001` ou run antigo.

### Storyboard Territorial v002

Fonte corrente: run `36326631575`; sem referência factual ativa a run superseded.

### Caderno Geral — Report Empresarial v004

A seção conjuntural usa os runs `36326283761` e `36326631575`, a taxonomia corrigida e as limitações territoriais corretas.

## 9. Resultado do QA factual

**PACOTE B: CONCLUÍDO / PASS.**

Não foi encontrada divergência numérica material entre os quatro artefatos editoriais ativos e as abas de controle após as correções acima.

As diferenças de nível de detalhe entre Factsheet, Storyboard, Caderno-Base e Caderno Geral são editoriais e não constituem inconsistência factual.

## 10. Ponto exato de retomada — Pacote C

Executar apenas QA editorial final:

1. fluidez;
2. precisão de redação;
3. redundâncias;
4. padronização de nomenclaturas;
5. clareza entre dado observado, calculado, interpretação e recomendação;
6. consistência de referências e limitações na forma editorial;
7. revisão final de Factsheet e Storyboard antes de congelamento.

Não reabrir as camadas de dados ou taxonomia sem nova evidência.

## 11. Governança

- bruto imutável;
- observado ≠ calculado ≠ interpretação;
- código bruto ≠ código normalizado;
- sigilo ≠ zero econômico;
- COREDE ≠ São Borja;
- RS ≠ São Borja;
- DFe ≠ consumo real;
- Cesta simples ≠ inflação;
- Radar ≠ market share municipal;
- runs superseded permanecem apenas para linhagem;
- PR #41 permanece **OPEN / DRAFT / UNMERGED**.
