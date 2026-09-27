# Checkpoint — Pacote A — auditoria do residual prefixo 00 concluída — 27/09/2026

## 1. Escopo deste pacote

Fechar exclusivamente a auditoria do residual taxonômico prefixado `00` do Radar do Mercado após a correção da taxonomia completa. Este checkpoint não executa o QA factual/editorial dos documentos; isso fica para o Pacote B.

## 2. Estado de governança

- repositório: `fernandossantor/sao-borja-market-intelligence`;
- branch: `feature/cnpj-territorial-control-v1`;
- PR #41: **OPEN / DRAFT / UNMERGED**;
- commit imediatamente anterior: `041331b0518060c798911375e48475282c208313`;
- regra: não mesclar sem autorização explícita.

## 3. Evidência auditada

Fonte: Receita Estadual/RS — Radar do Mercado — Composição de Mercado.

Período: julho/2024 a agosto/2026.

Geografia: Rio Grande do Sul.

Camada curated canônica: run `36326283761`.

Camada analysis canônica: run `36326631575`.

Resultados do residual prefixado `00`:

- 47 NCM8 normalizados;
- 235 linhas brutas correspondentes;
- 203 linhas sob corte de sigilo;
- taxa de linhas sob sigilo: 86,382979%;
- valor publicado não suprimido: R$ 2.047.333;
- participação no valor residual total da Composição: 98,676162%.

## 4. Estrutura do código bruto

A auditoria retornou aos 26 arquivos brutos e comparou `cod_ncm` da fonte com o NCM8 normalizado.

Foram observadas duas classes principais:

- códigos brutos de 2 dígitos: 142 linhas, 24 códigos distintos, R$ 2.045.661 publicados;
- códigos brutos de 8 dígitos iniciados por `00`: 93 linhas, 24 códigos distintos, R$ 1.672 publicados.

O código bruto `00`, normalizado como `00000000`, concentra:

- 80 linhas;
- 50 linhas sob sigilo;
- R$ 2.041.248 publicados;
- 99,702784% do valor publicado do prefixo `00`.

## 5. Decisão metodológica

**Não classificar** os códigos prefixados `00` em grupos SBMI.

Tratamento corrente:

- exceção de qualidade/codificação da fonte;
- manter fora dos benchmarks setoriais classificados;
- preservar na base de controle;
- não imputar NCM econômico por inferência;
- monitorar apenas se o residual crescer materialmente.

A cobertura monetária corrigida da Composição permanece em **99,999817%** do valor publicado não suprimido.

## 6. Controle de sigilo

Quarenta e quatro dos 47 NCM8 normalizados do prefixo `00` aparecem somente sob sigilo e possuem R$ 0 de valor publicado agregado.

**R$ 0 publicado sob sigilo não significa zero econômico.**

## 7. Efeito da normalização

Foi observado um caso em que os códigos brutos `01` e `00000001` convergem para o mesmo NCM8 normalizado `00000001`.

Não há impacto monetário corrente porque os registros envolvidos estão sob sigilo, mas a auditoria recomenda que uma futura revisão da camada curated preserve simultaneamente:

- `cod_ncm_fonte`;
- `ncm8_normalizado`;
- comprimento do código bruto;
- flag de aderência à dimensão taxonômica.

Essa melhoria é backlog técnico e **não bloqueia** o fechamento da v029.

## 8. Artefatos

Google Drive:
- documento metodológico: `1Z4nhQQpJlOwBlc238GcAi41ANKo_W6irH6oTFrUQAXw`.

Caderno-Base:
- planilha: `1CHn1JZ-IcDxG3V9M5y0PKvN5lTkcvlVcov_vVw3je3c`;
- aba `Taxonomia_Radar_v029`, sheetId `1498802222`;
- aba `Auditoria_series_v029`, com check `prefix00_quality_audit = PASS`;
- `Rastreabilidade_v029` já registra a auditoria e o documento metodológico.

GitHub:
- `docs/caderno_base/auditoria_residual_prefixo00_v001_20260927.md`;
- `docs/caderno_base/dados/radar_prefixo00_raw_code_audit_v001.csv`;
- commit `041331b0518060c798911375e48475282c208313`.

## 9. Status do Pacote A

**CONCLUÍDO / PASS.**

A frente taxonômica não bloqueia mais o fechamento da v029.

## 10. Ponto exato de retomada — Pacote B

Executar **QA de consistência factual** entre:

1. Caderno-Base Territorial v029;
2. Factsheet Territorial v002;
3. Storyboard Territorial v002;
4. Caderno Geral — Report Empresarial v004;
5. abas de controle da v029.

Objetivo do Pacote B:

- localizar referências a runs antigos ou artefatos superseded;
- substituir apenas o que ficou obsoleto após a correção da taxonomia;
- confirmar que os números correntes DFe/Cesta/Radar são idênticos entre artefatos;
- confirmar que geografia, período, unidade, fonte e limitações estão coerentes.

Não executar QA estilístico/fluidez no mesmo pacote.

## 11. Regras permanentes

- bruto imutável;
- observado ≠ calculado ≠ interpretação;
- código bruto ≠ código normalizado;
- sigilo ≠ zero econômico;
- residual não recebe imputação automática;
- COREDE ≠ São Borja;
- RS ≠ São Borja;
- DFe ≠ consumo real;
- Cesta simples ≠ inflação;
- Radar ≠ market share municipal;
- PR #41 permanece **OPEN / DRAFT / UNMERGED**.
