# Auditoria — correção da taxonomia Radar e reprocessamento das séries públicas — 27/09/2026

## 1. Objeto

Documentar a correção de completude da taxonomia NCM do Radar do Mercado, o reprocessamento das camadas `curated` e `analysis` e o impacto sobre a cobertura taxonômica e a antiga hipótese de concentração da lacuna no prefixo NCM 29.

## 2. Problema identificado

A consulta da dimensão NCM/grupo do Radar utilizava uma janela fixa de 10.000 linhas. A janela chegava exatamente ao limite e terminava dentro do grupo de afinidade **Químicos Orgânicos**.

O procedimento anterior completava os grupos totalmente ausentes da janela inicial, mas não reconsultava o grupo de fronteira quando ele aparecia parcialmente. Como consequência, a taxonomia canônica anterior ficou truncada dentro desse grupo.

O efeito analítico foi material: NCM8 pertencentes ao grupo truncado apareciam artificialmente como “não classificados”, concentrando o gap no prefixo 29.

## 3. Correção aplicada

O workflow `radar-mercado-ncm-taxonomy-complete-v1` passou a:

1. detectar quando a consulta inicial atinge o limite de 10.000 linhas;
2. identificar o grupo de fronteira;
3. reconsultar esse grupo independentemente, mesmo quando parcialmente presente;
4. reconsultar grupos totalmente ausentes;
5. deduplicar o conjunto final;
6. validar os 110 grupos de afinidade;
7. controlar explicitamente o grupo de fronteira **Químicos Orgânicos**.

### Run canônico da taxonomia corrigida

- run: `36326001762`;
- commit: `62b25805429a2d1e0fe9617065cf4fcaa12d95b0`;
- status: **SUCCESS**;
- artifact: `10934195965`;
- digest: `sha256:06bc6edbd6dba6229e1898dc2942a40ebaff34c53351daadeccc210a15f6e100`;
- Drive: `1Ss4MxTH9GRAi4hovgnc9rQDCMA1omJFt`.

Resultado:
- 110 grupos;
- 13.829 NCM8;
- 2.302 NCM8 em Químicos Orgânicos;
- nenhum grupo ausente ao final.

A taxonomia anterior continha 11.765 NCM8. A diferença de 2.064 NCM8 é correção de completude da extração, não criação de códigos pelo SBMI.

## 4. Camada curated reprocessada

Run canônico:
- run: `36326283761`;
- commit: `ee48bfc853f7889497073a7d7124d8d752b3244d`;
- status: **SUCCESS**;
- artifact: `10934196451`;
- digest: `sha256:4653e9cee7d0c6aece8b70a54490690213f3bc2a3e6792587c73492a6eaa90f4`;
- Drive: `18c1OJLqCeSE-_oCULlicl95XhB9FFevp`;
- validações: **18 PASS**.

Resultados de cobertura:
- Radar Composição: 1.589.761 linhas;
- linhas mapeadas: 99,838592%;
- NCM8 residuais na Composição: 1.074;
- Radar Exportações: 100,000000% das linhas mapeadas;
- NCM8 residuais em Exportações: 0;
- Portfólio: 1.348 de 1.349 NCM8 mapeados = 99,925871%.

## 5. Camada analysis reprocessada

Run canônico:
- run: `36326631575`;
- commit: `88895cd2cb12fd3e5bea84313fb3e80625736049`;
- status: **SUCCESS**;
- artifact: `10934028190`;
- digest: `sha256:53388b22d7f629ae7289cb2928f6379649fbc2f1960d6eb9669d658a3fb85783`;
- SHA-256 do pacote interno: `a59f1b26cb19292967edee89496a36997b6265e5e70bfc98974c389823ed27a6`;
- Drive: `1t01q-cVFiInJaGouvHADIndnzeoQdLrq`;
- validações: **12 PASS**.

### Cobertura monetária corrigida

A cobertura monetária da taxonomia sobre o valor publicado não suprimido da Composição é:

[
	ext{Cobertura} = rac{	ext{valor mapeado}}{	ext{valor publicado não suprimido}} 	imes 100
]

Resultado: **99,999817%**.

Residual publicado não suprimido fora da taxonomia: **R$ 2.074.800**.

## 6. Residual da Composição

O residual publicado está concentrado em códigos prefixados **00**:

- 47 NCM8;
- R$ 2.047.333;
- 98,676162% do valor residual não classificado.

Demais resíduos monetários relevantes:
- prefixo 61: R$ 15.717;
- prefixo 33: R$ 5.261;
- prefixo 09: R$ 4.800;
- prefixo 85: R$ 1.297;
- prefixo 62: R$ 392.

O prefixo 00 deve ser tratado como exceção de qualidade/codificação da fonte, não como mercado a ser imputado.

## 7. Revisão da hipótese NCM 29

A hipótese anterior de que o prefixo 29 concentrava praticamente todo o valor não classificado foi **refutada pela auditoria de completude**: o fenômeno era efeito da taxonomia truncada.

Após a correção:
- 6 NCM8 residuais do prefixo 29;
- 13 linhas;
- todas as linhas sob corte de sigilo;
- valor publicado não suprimido = R$ 0.

Os códigos residuais são:
- 29109026;
- 29120000;
- 29241000;
- 29252900;
- 29309000;
- 29369200.

**Controle:** valor publicado igual a zero sob sigilo NÃO significa ausência de atividade econômica. Esses códigos permanecem censurados e não são imputados automaticamente.

## 8. Impacto sobre os benchmarks setoriais

Os benchmarks jan–ago/2026 versus jan–ago/2025 permanecem:

- Bens Essenciais / CORE: -1,27%;
- Bens Não Essenciais / CORE: -2,97%;
- Saúde/Higiene/Cuidados Pessoais / CORE: +16,12%;
- Serviços / ADJACENT: +6,48%.

A correção melhora a cobertura e a confiabilidade da classificação, mas não altera a regra territorial: **Radar/RS é benchmark estadual e não deve ser tratado como trajetória municipal de São Borja**.

## 9. Artefatos superados

A análise intermediária baseada no run `36325331369` fica **SUPERSEDED**.

Não usar como diagnóstico corrente:
- artifact `10933798441`;
- pasta Drive `1t65LxedlixIBYbm7RT6f1O4aua3R-zlR`;
- documento Drive `1PjEaIQFeaUqLbYPLNG65O85LQuwiRNf0nmkzxAarG6s`.

Esses artefatos são preservados somente para linhagem.

## 10. Governança e próxima etapa

Regras:
- bruto imutável;
- taxonomia corrigida preserva a dimensão Radar;
- zero sob sigilo é censura, não zero econômico;
- residual não recebe imputação automática;
- RS ≠ São Borja;
- PR #41 permanece **OPEN / DRAFT / UNMERGED**.

Próxima frente: tratar os códigos prefixados 00 como qualidade de dados, executar QA editorial final dos artefatos v029 e somente depois decidir congelamento/publicação.
