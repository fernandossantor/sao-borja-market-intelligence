# Checkpoint — 2026-09-07

## Projeto

São Borja — Inteligência Mercadológica

## Estado operacional ao encerrar o dia

- Branch de trabalho: `feature/cnpj-territorial-control-v1`.
- PR #41: **OPEN + DRAFT + NÃO MERGEAR** sem autorização explícita.
- Caderno-Base corrente no Drive: `caderno_base_territorial_v008_diagnostico_integrado_20260907`.
- Drive ID do Caderno-Base: `1NJp_tmQ36NE8YDA2JhmyqjsnB1a7V9ivtAFJW7YLhcU`.
- Documento narrativo corrente no Drive: `Caderno-Base — diagnóstico analítico integrado v002 — 20260907`.
- Drive ID do documento narrativo: `19QW1QJ7CUYHV8Gx9wkbivpfxNK8Phl6mNb5mUdXd8L0`.
- Regra estrutural preservada: Drive = fontes/derivados compartilhados; GitHub/Codespace = processamento, documentação e controle de versão.

## Mudança de estágio consolidada

A fase de auditoria recorrente das bases já estabilizadas foi encerrada. Auditorias concluídas passam a funcionar como controles de integridade e só devem ser reabertas por:

1. nova competência;
2. mudança metodológica;
3. falha de integridade;
4. lacuna analítica específica ainda não coberta.

O foco corrente é **análise territorial integrada**, com construção simultânea de dados, interpretação e narrativa do Caderno-Base.

## Controle empresarial — RFB 2026-08

Dados consolidados:

- 7.306 estabelecimentos ativos;
- 6.881 matrizes locais;
- 102 filiais de matriz local;
- 323 filiais de matriz externa;
- 6.906 Entidades Empresariais;
- 284 Entidades Empresariais de matriz externa;
- participação externa empresarial: **4,1124%**.

A classificação usa os campos oficiais da RFB e não usa `/0001` como heurística de matriz.

## Emprego e remuneração — RAIS 2025 × RFB 2026-08

Dados/estimativas consolidados:

- 8.595 vínculos empresariais;
- 8.581 vínculos com match exato CNAE subclasse × natureza jurídica;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na soma das remunerações médias nominais: **29,0903%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**;
- remuneração média implícita estimada em estruturas externas: **R$ 3.251,91/vínculo**;
- remuneração média implícita estimada em estruturas locais: **R$ 2.664,93/vínculo**;
- diferencial implícito externa/local: **+22,03%**;
- razão peso laboral externo / peso cadastral externo: **6,1183**.

Limitação permanente: emprego/remuneração por controle territorial são estimados por células CNAE × natureza jurídica porque a RAIS pública utilizada não preserva o CNPJ identificador do estabelecimento.

## IPM definitivo

Fonte: Receita Estadual/RS — arquivos `DAIM545X`.

Série canônica:

- cobertura: **2003–2026**, 24/24 anos;
- validação: **7/7 PASS**;
- mínimo: 2017 = **0,468285**;
- máximo: 2023 = **0,573154**;
- 2025 = **0,527880**;
- 2026 = **0,533647**;
- variação 2026/2025 = **+1,092483%**.

A série é cíclica: 12 altas e 11 quedas anuais. IPM 2027 permanece provisório e fora da série definitiva.

## VAF — série oficial publicada em REAL

A coleta municipal está fechada para o intervalo em REAL.

Fonte: Receita Estadual/SEFAZ-RS — `Valor Adicionado Municípios`.

Estado canônico:

- cobertura contínua: **1994–2025, 32/32 rótulos anuais**;
- unidade: R$ nominais/correntes;
- município: São Borja, prefixo 117;
- terminologia temporal preservada como `ano_rotulo_fonte`;
- o formulário denomina o intervalo como **Anos de Apuração**;
- não relabelar automaticamente como `ano_dado`.

Pontos recentes:

- 2023: R$ 2.449.438.258,50;
- 2024: **R$ 2.907.302.928,34** — maior valor nominal da série;
- 2025: **R$ 2.325.966.620,93**;
- variação nominal 2025/2024: **-19,9957%**.

Não interpretar essa variação como crescimento/contração real sem deflação documentada.

## Reconciliação Sebrae × SEFAZ

- Sebrae 2009–2019 ↔ SEFAZ 2007–2017;
- **11/11 correspondências consecutivas exatas** após arredondamento para R$ milhões com duas casas;
- deslocamento regular de dois anos.

A correspondência esclarece a defasagem do relatório secundário, mas não autoriza renomear a dimensão temporal da fonte oficial.

## VAF × IPM — análise exploratória

Alinhamento descritivo `VAF t → IPM t+2`:

- 23 transições comparáveis entre VAF 2002–2024 e IPM 2004–2026;
- **15/23** com o mesmo sinal;
- **8/23** divergentes;
- em **todas as 8 divergências**, o VAF municipal nominal cresceu enquanto o IPM caiu.

Interpretação permitida: crescimento nominal do VAF municipal, isoladamente, não é suficiente para explicar o movimento do IPM. A análise é exploratória e não causal.

## Matriz de controle territorial por setor — v001

Artefatos:

- aba `Matriz_controle_setorial` no Caderno-Base v008;
- `matriz_controle_setorial_sao_borja_v001.csv` promovido ao Drive;
- `docs/caderno_base/matriz_controle_setorial_v001.md` no repositório.

Cobertura atual: **10 divisões CNAE** com sobreposição comparável entre cadastro e emprego/remuneração.

Destaques:

- Varejo (47): 6,63% cadastral externa; 37,46% emprego externo est.; 38,16% remuneração externa est.; 36,41% de toda a remuneração externa estimada. Principal nó externo em peso absoluto.
- Finanças (64): 32,50% cadastral; 96,73% emprego externo est.; 98,70% remuneração externa est. Dependência funcional externa muito elevada nas métricas disponíveis.
- Energia/utilidades (35): 75,00% cadastral; 96,20% emprego externo est.; 100,00% remuneração externa est. Setor de rede, com pequena base absoluta.
- Transporte terrestre (49): 4,15% cadastral versus 29,95% do emprego e 42,76% da remuneração estimados como externos. Exemplo de diferença entre presença cadastral e peso funcional.
- Serviços de apoio empresarial (82): 3,20% cadastral versus 37,40% do emprego e 42,96% da remuneração estimados como externos.
- Serviços pessoais (96): alta intensidade relativa externa, mas apenas 27 vínculos; não confundir percentual alto com relevância absoluta.

A classificação `base local / presença externa complementar / dependência funcional externa / setor estratégico de rede` é analítica e preliminar, não nomenclatura oficial.

## Próxima ação ao retomar

Não voltar à auditoria geral das bases já estabilizadas.

Prioridade de trabalho:

1. **Integrar estrutura empresarial com população, renda, emprego e mercado consumidor** para começar a medir capacidade de compra e estrutura da demanda local.
2. Ampliar a matriz setorial somente quando houver sobreposição comparável e ganho analítico claro.
3. Transformar a matriz de controle territorial em uma tipologia setorial utilizável no Caderno-Base e nos quatro cadernos setoriais.
4. Na fiscalidade, buscar apenas grandezas novas e explicativas: denominador/índice estadual compatível do VAF, decomposição dos critérios do IPM e quota-parte monetária efetivamente transferida de ICMS.
5. Preservar a construção simultânea de **dados + narrativa explicativa + interpretação + diagnóstico**.

## Pergunta-guia para o próximo ciclo

**O que a combinação entre estrutura empresarial, emprego, remuneração, população, renda e consumo revela sobre o funcionamento efetivo do mercado de São Borja e sobre sua dependência/integração com redes externas?**

## Regras que não devem ser alteradas

- diferenciar dado observado, calculado, estimado, hipótese, interpretação e recomendação;
- não fundir universos distintos em índice único sem justificativa metodológica;
- IPM ≠ VAF ≠ VAB ≠ arrecadação/transferência;
- não inferir retenção de renda, remessa de lucros ou vazamento monetário com os dados atuais;
- preservar versões históricas do Caderno-Base;
- manter PR #41 **draft e sem merge** até autorização explícita.
