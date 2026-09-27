# Checkpoint — taxonomia Radar corrigida e integração editorial concluída — 27/09/2026

## 1. Governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`.
- Branch: `feature/cnpj-territorial-control-v1`.
- PR #41: **OPEN / DRAFT / UNMERGED**.
- Não mesclar sem autorização explícita.

## 2. Correção metodológica concluída

Foi identificado que a taxonomia Radar anterior estava truncada porque a consulta inicial atingia 10.000 linhas e terminava dentro do grupo **Químicos Orgânicos**. O grupo aparecia parcialmente e, por isso, não era reconsultado pelo procedimento original.

A correção passou a reconsultar o grupo de fronteira e os grupos ausentes.

### Cadeia canônica

**Taxonomia Radar**
- run `36326001762`;
- commit `62b25805429a2d1e0fe9617065cf4fcaa12d95b0`;
- artifact `10934195965`;
- Drive `1Ss4MxTH9GRAi4hovgnc9rQDCMA1omJFt`;
- 110 grupos;
- 13.829 NCM8;
- Químicos Orgânicos = 2.302 NCM8.

**Curated**
- run `36326283761`;
- commit `ee48bfc853f7889497073a7d7124d8d752b3244d`;
- artifact `10934196451`;
- Drive `18c1OJLqCeSE-_oCULlicl95XhB9FFevp`;
- 18 validações PASS.

**Analysis**
- run `36326631575`;
- commit `88895cd2cb12fd3e5bea84313fb3e80625736049`;
- artifact `10934028190`;
- Drive `1t01q-cVFiInJaGouvHADIndnzeoQdLrq`;
- 12 validações PASS;
- pacote interno SHA-256 `a59f1b26cb19292967edee89496a36997b6265e5e70bfc98974c389823ed27a6`.

## 3. Cobertura corrente

Radar Composição:
- cobertura de linhas: **99,838592%**;
- cobertura monetária do valor publicado não suprimido: **99,999817%**;
- NCM8 residuais: 1.074;
- valor publicado residual: **R$ 2.074.800**.

Radar Exportações:
- cobertura de linhas: **100%**;
- NCM8 residuais: **0**.

Portfólio:
- cobertura por NCM8: **99,925871%**.

## 4. Revisão do NCM 29

A antiga concentração monetária no NCM 29 era efeito da truncagem da taxonomia.

Após a correção:
- 6 NCM8 do prefixo 29 permanecem residuais;
- 13 linhas;
- todas sob sigilo;
- R$ 0 publicado não suprimido.

Portanto, **não existe mais uma frente monetária NCM 29 a auditar**. Os seis códigos são preservados como censurados, sem imputação.

O residual monetário corrente é dominado pelo prefixo **00**:
- 47 NCM8;
- R$ 2.047.333;
- 98,676162% do valor residual.

## 5. Artefato intermediário superado

Run `36325331369` e sua análise de priorização monetária NCM29 são **SUPERSEDED**.

Preservados apenas para linhagem:
- artifact `10933798441`;
- Drive folder `1t65LxedlixIBYbm7RT6f1O4aua3R-zlR`;
- Drive doc `1PjEaIQFeaUqLbYPLNG65O85LQuwiRNf0nmkzxAarG6s`.

## 6. Drive

Novos artefatos promovidos:
- taxonomia corrigida: pasta `17AiZZIcJXhnSaurO123qTMU3-HTAzJnt`, arquivo `1Ss4MxTH9GRAi4hovgnc9rQDCMA1omJFt`;
- curated corrigida: pasta `1lACc6dtbT83p4ltNc4sjT7ptikFWcl0K`, arquivo `18c1OJLqCeSE-_oCULlicl95XhB9FFevp`;
- analysis corrigida: pasta `1ZyTj5Yh8jco7ghkEOPHQm4Kovhe8b27X`, arquivo `1t01q-cVFiInJaGouvHADIndnzeoQdLrq`;
- nota metodológica: `1ck41F-bKY5rzMNN6NKeGoZdR3Gd4A5HtC3n71LqsCug`.

## 7. Caderno-Base v029

Planilha:
`1CHn1JZ-IcDxG3V9M5y0PKvN5lTkcvlVcov_vVw3je3c`.

Estado:
- `Series_publicas_v029`: corrigida;
- `Auditoria_series_v029`: corrigida e ampliada;
- `Resumo_v029`: corrigido;
- `Teses_transversais_v029`: T12 corrigida;
- `Factsheets_v029`: factsheet territorial corrente;
- `Storyboards_v029`: storyboard territorial corrente;
- `QA_argumentativo_v029`: Caderno Geral atualizado;
- nova aba `Taxonomia_Radar_v029`, sheetId `1498802222`, com linhagem, cobertura, residual e artefato superseded;
- `Rastreabilidade_v029`: atualizada com a cadeia corrigida.

## 8. Documentos editoriais

**Caderno-Base Territorial v029**
- Drive ID `1Fj6MgIPDetaN8PPUeJ7k8zsH5L6jeHoClmb3ZST9oD4`;
- Eixo 7 usa a taxonomia corrigida e o residual prefixo 00.

**Factsheet Territorial v002**
- Drive ID `1JkNJxm38J-RMPP94QCW_mqGeE_bZCeIBOpZplM0KK_0`;
- controle taxonômico corrigido.

**Storyboard Territorial v002**
- Drive ID `1eR73tUv_OkjfOSYBYAtL03h1QRmRqSdkvCtoEcj9J7U`;
- 9 quadros; escalas São Borja / COREDE / RS separadas.

**Caderno Geral — Report Empresarial v004**
- Drive ID `13yqwDHKJuEag4I0l7XaUZ_oDIg5lh0UvQsmJWc3H2Co`;
- seção 13 recebeu camada conjuntural DFe/Cesta/Radar;
- adicionada **TESE 9 — Sinais conjunturais públicos exigem leitura multiescalar**;
- 143.460 caracteres no fechamento desta etapa.

## 9. CI

Workflow `quality`, run `36326631502`:
- job `test`: **SUCCESS**;
- job `rfb-cnpj-territorial-control`: **FAILURE** na etapa de download oficial RFB;
- a falha agregada não invalida a correção da taxonomia nem as camadas curated/analysis, que possuem workflows específicos SUCCESS.

## 10. Ponto exato de retomada

Não reabrir:
- parser DFe;
- normalização Radar 2026;
- taxonomia Químicos Orgânicos;
- auditoria monetária NCM29.

Retomar por:

1. auditoria de qualidade dos códigos prefixados 00;
2. QA editorial final do Caderno-Base, Factsheet, Storyboard e Caderno Geral;
3. decidir congelamento/publicação da v029;
4. somente depois explorar novas hipóteses multiescalares ou buscar decomposição municipal adicional em fonte administrativa compatível.

## 11. Regras permanentes

- bruto imutável;
- observado ≠ calculado ≠ interpretação;
- sigilo ≠ zero econômico;
- COREDE ≠ São Borja;
- RS ≠ São Borja;
- DFe ≠ consumo real;
- Cesta simples ≠ inflação;
- Radar ≠ market share municipal;
- residual taxonômico não recebe imputação automática;
- PR #41 permanece **OPEN / DRAFT / UNMERGED**.
