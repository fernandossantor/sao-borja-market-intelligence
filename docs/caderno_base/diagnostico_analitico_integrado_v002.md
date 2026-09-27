# Caderno-Base Territorial — diagnóstico analítico integrado v002

## Resumo executivo

Esta versão consolida a mudança de foco do projeto: **auditorias repetidas deixam de ser o eixo central e passam a funcionar como infraestrutura de confiança**, enquanto o trabalho principal avança para interpretação territorial integrada.

A evidência disponível aponta para quatro traços centrais de São Borja:

1. **forte predominância de comando empresarial local em quantidade**, mas presença de matrizes externas desproporcionalmente maior em emprego e remuneração;
2. **concentração do peso externo em poucos setores**, especialmente varejo, finanças, transportes, atacado, energia e logística;
3. **trajetória fiscal relativa cíclica**, com IPM em perda até 2017, recuperação até 2023 e recuo parcial posterior;
4. **VAF nominal com trajetória de forte expansão de longo prazo, mas queda expressiva no último rótulo disponível**, sem que isso possa ser convertido mecanicamente em previsão de IPM.

## 1. Objeto, fontes e limitações

Abrangência geográfica: São Borja/RS.

Fontes principais:

- RFB Dados Abertos CNPJ — competência 2026-08;
- RAIS — ano-base 2025;
- Receita Estadual/SEFAZ-RS — IPM definitivo, anos de distribuição 2003–2026;
- Receita Estadual/SEFAZ-RS — Valor Adicionado Municípios, rótulos oficiais 1994–2025 em REAL;
- Sebrae/RS 2020 — benchmark secundário usado exclusivamente para reconciliação temporal.

Limitações essenciais:

- RAIS 2025 e RFB 2026-08 não representam o mesmo período;
- a RAIS pública utilizada não preserva CNPJ identificador, de modo que o controle externo no emprego/remuneração é **estimado** por células CNAE × natureza jurídica;
- VAF publicado é nominal; não foi deflacionado;
- IPM é índice relativo e não equivale a VAF, VAB nem valor transferido de ICMS;
- pesos e componentes legais do IPM mudam no tempo;
- o alinhamento VAF → IPM com defasagem de dois anos é tratado como **correspondência empírica/exploratória**, não como equivalência semântica nem mecanismo causal.

## 2. Controle territorial das empresas

### Dados observados e calculados

- estabelecimentos empresariais: **6.906**;
- estabelecimentos de matriz externa: **284**;
- participação externa cadastral: **4,1124%**.

### Estimativas de emprego e remuneração

- vínculos empresariais: **8.595**;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na soma das remunerações médias nominais: **29,0903%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**.

### Cálculos integrados

**Intensidade laboral relativa das estruturas externas**

`25,1606 / 4,1124 = 6,1183`

O peso estimado das estruturas externas no emprego é cerca de **6,12 vezes** seu peso no número de estabelecimentos.

**Diferencial de remuneração média implícita**

- externa: **R$ 3.251,91/vínculo**;
- local: **R$ 2.664,93/vínculo**;
- diferencial calculado: `(3.251,91 / 2.664,93 - 1) × 100 = 22,03%`.

### Interpretação

São Borja não apresenta uma economia simplesmente “dominada por empresas externas”. Em quantidade, ocorre o oposto: o tecido empresarial é amplamente local. A questão territorialmente relevante é que **uma pequena parcela de estabelecimentos sob comando externo possui intensidade econômica muito superior em termos de vínculos e remuneração formal**.

Isso sugere uma estrutura dual:

- ampla base de firmas locais, potencialmente importante para capilaridade, empreendedorismo e circulação econômica cotidiana;
- conjunto menor de estruturas externas, mas com grande capacidade de empregar e remunerar.

Essa dualidade deve orientar análises futuras de consumo, concorrência, fornecedores e retenção de renda.

## 3. Onde o controle externo pesa mais

No cadastro geral de filiais externas, o varejo (CNAE 47) representa **35,29%** das 323 filiais externas identificadas. O denominador não é idêntico ao universo empresarial de 284 estabelecimentos usado no modelo RAIS × RFB, portanto as proporções cadastrais e trabalhistas não devem ser somadas diretamente.

Na remuneração de dezembro estimada como externa, a concentração setorial é elevada:

| Divisão CNAE | Participação no total externo estimado |
|---|---:|
| 47 — Comércio varejista | 36,41% |
| 64 — Atividades de serviços financeiros | 15,01% |
| 49 — Transporte terrestre | 11,45% |
| 46 — Comércio por atacado | 10,18% |
| 35 — Eletricidade, gás e outras utilidades | 4,52% |
| 52 — Armazenamento e atividades auxiliares dos transportes | 4,34% |

- Top 4: **73,05%**;
- Top 6: **81,91%**.

No varejo especificamente:

- vínculos externos estimados: **1.083,74**;
- participação externa estimada nos vínculos da divisão: **37,46%**;
- participação externa estimada na remuneração de dezembro da divisão: **38,16%**.

### Interpretação

O peso externo está concentrado em atividades que ligam o território a redes mais amplas de distribuição, finanças e infraestrutura. Isso cria uma primeira classificação funcional para análise mercadológica:

- **base local**: atividades com grande presença de empresas locais e menor dependência de redes externas;
- **presença externa complementar**: redes externas relevantes, mas sem dominar emprego/remuneração;
- **dependência funcional externa**: setores em que emprego, remuneração ou infraestrutura dependem fortemente de organizações de comando externo;
- **setores estratégicos de rede**: atividades como finanças, energia, transportes e logística cuja importância territorial ultrapassa a contagem de estabelecimentos.

Essa tipologia é uma **proposta analítica**, ainda não uma classificação oficial.

## 4. IPM: ciclos de participação relativa

Série oficial definitiva: 2003–2026.

Pontos de referência:

- 2003: **0,513428**;
- 2006: **0,552260**;
- 2017: **0,468285**, mínimo da série;
- 2023: **0,573154**, máximo da série;
- 2025: **0,527880**;
- 2026: **0,533647**.

Cálculos:

- 2006 → 2017: **-15,21%**;
- 2017 → 2023: **+22,39%**;
- 2023 → 2026: **-6,89%**;
- 2025 → 2026: **+1,09%**;
- 2003 → 2026: **+3,94%**.

A média simples de 2003–2026 é **0,515344**; o valor de 2026 está **3,55% acima** dela. Das 23 variações anuais, 12 são positivas e 11 negativas.

### Interpretação

O IPM de São Borja apresenta **ciclos**, não tendência linear. A recuperação de 2026 interrompe parcialmente a queda pós-2023, mas ainda não recompõe o pico. O comportamento relativo do município depende do desempenho próprio, do conjunto dos municípios e das regras legais vigentes.

## 5. VAF: série oficial fechada em REAL

A auditoria da fonte foi encerrada para o intervalo em REAL. A série oficial publicada cobre **32/32 rótulos anuais entre 1994 e 2025**.

Pontos recentes:

| Rótulo oficial | VAF publicado |
|---:|---:|
| 2019 | R$ 1.548.063.657,14 |
| 2020 | R$ 1.844.857.219,33 |
| 2021 | R$ 2.331.374.375,86 |
| 2022 | R$ 2.353.300.619,62 |
| 2023 | R$ 2.449.438.258,50 |
| 2024 | **R$ 2.907.302.928,34** |
| 2025 | **R$ 2.325.966.620,93** |

**Dado calculado:** `2025 / 2024 - 1 = -19,9957%`.

Assim, 2024 é o maior valor nominal da série e 2025 apresenta queda nominal de aproximadamente **20,0%**.

### Reconciliação temporal

O fechamento dos rótulos 2007 e 2008 permitiu confrontar todo o benchmark Sebrae 2009–2019. Resultado: **11/11 correspondências consecutivas exatas**, quando os valores oficiais são arredondados para milhões com duas casas, sempre com deslocamento de dois anos entre o rótulo SEFAZ e o ano apresentado pelo Sebrae.

Esse padrão fortalece a leitura de defasagem já sugerida pela documentação AIM, mas o projeto preserva `ano_rotulo_fonte` e não relabela automaticamente a série.

## 6. VAF e IPM: o que a comparação já permite concluir

Foi construído um alinhamento **exploratório** entre a variação nominal do VAF sob rótulo `t` e a variação do IPM em `t+2`, coerente com o padrão empírico identificado na reconciliação e com a cronologia AIM.

Entre 23 transições anuais comparáveis, de VAF 2002–2024 para IPM 2004–2026:

- **15/23** têm o mesmo sinal;
- **8/23** divergem;
- em **todas as oito divergências**, o VAF municipal nominal cresceu enquanto o IPM caiu.

### Interpretação

Esse resultado é analiticamente mais importante do que uma correlação simples. Ele demonstra empiricamente que **crescimento nominal do VAF de São Borja não é condição suficiente para crescimento do IPM**. Isso é coerente com o conceito do IPM: importa a participação relativa do município no contexto estadual, além dos demais componentes e dos pesos legais.

Portanto, a próxima investigação fiscal não deve repetir a coleta do VAF municipal. Deve buscar, quando disponível:

1. VAF/índice relativo estadual ou denominador compatível;
2. decomposição dos critérios do IPM por período;
3. valores efetivamente transferidos de ICMS;
4. comparação entre crescimento econômico local, posição relativa estadual e receita efetiva.

## 7. Diagnóstico territorial integrado

### Fatos

- empresas locais dominam numericamente a base empresarial;
- estruturas externas têm peso muito maior no emprego e remuneração do que no número de estabelecimentos;
- o peso externo está concentrado em poucos setores de rede;
- o IPM tem trajetória cíclica e atual recuperação parcial;
- o VAF nominal atingiu pico em 2024 e caiu cerca de 20% em 2025;
- VAF nominal e IPM nem sempre se movem na mesma direção.

### Interpretação

São Borja pode ser descrita, preliminarmente, como uma economia de **base empresarial local ampla, mas com pontos de dependência funcional externa relevantes**. A questão estratégica não é eliminar essa presença externa, que também sustenta emprego e renda, mas compreender quais funções econômicas permanecem sob comando local e quais dependem de redes externas.

Essa leitura abre uma agenda mais útil para os cadernos setoriais: identificar em cada mercado quem controla oferta, emprego, canais, compras, logística, crédito e decisões comerciais; e avaliar onde há espaço para fortalecimento de fornecedores e empresas locais.

### Hipóteses a testar

- varejo é o principal elo entre consumo local e redes empresariais externas;
- logística/transportes e finanças funcionam como infraestruturas de dependência territorial;
- maior remuneração nas estruturas externas pode decorrer parcialmente de composição setorial e porte, e não do controle externo em si;
- empresas locais podem ter alta capilaridade econômica mesmo quando possuem menor peso médio por estabelecimento.

## 8. Recomendações para a próxima fase

### Baseadas em evidências

1. **Encerrar auditorias recorrentes já resolvidas.** Reabrir somente por nova competência, mudança metodológica ou falha de integridade.
2. Construir uma **matriz setorial de controle territorial**, cruzando cadastro, emprego e remuneração externa/local.
3. Integrar a estrutura produtiva ao **mercado consumidor**, usando emprego, renda/remuneração, população e fluxos de consumo disponíveis.
4. Passar de indicadores isolados para **tipologias territoriais e setoriais** que possam orientar os quatro cadernos de mercado.
5. Na fiscalidade, priorizar denominador estadual, composição do IPM e transferência efetiva de ICMS, e não nova coleta do VAF municipal.

### Hipóteses que exigem dados adicionais

- retenção/vazamento de renda;
- compras locais versus externas;
- remessa de lucros;
- dependência de fornecedores externos;
- participação de redes externas no faturamento total do varejo;
- diferenciais salariais controlados por setor, porte e ocupação.

## 9. Indicadores de acompanhamento

- participação de matriz externa nos estabelecimentos empresariais;
- participação externa estimada no emprego e na remuneração;
- razão `peso laboral externo / peso cadastral externo`;
- concentração setorial externa — top 4/top 6;
- IPM definitivo e distância ao pico/média histórica;
- VAF nominal e, futuramente, VAF real após deflação documentada;
- discrepância de sinal VAF × IPM no alinhamento exploratório;
- quota-parte monetária efetivamente recebida de ICMS quando a série for integrada.

## 10. Artefatos que sustentam esta versão

- Caderno-Base v008: `caderno_base_territorial_v008_diagnostico_integrado_20260907`;
- série VAF: `vaf_sao_borja_1994_2025_oficial_v001.csv`;
- alinhamento exploratório: `vaf_ipm_alinhamento_exploratorio_v001.csv`;
- nota de canonização: `docs/caderno_base/vaf_series_canonicalization_1994_2025.md`;
- documentação anterior permanece preservada como histórico metodológico.
