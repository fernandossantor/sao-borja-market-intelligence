# RFB CNPJ 2026-08 — reconciliação do controle estrutural de São Borja

## 1. Problema auditado

A validação exploratória mais recente registrava uma aparente divergência entre a base canônica e o espelho RFB para os **7.306 estabelecimentos ativos** de São Borja/RS.

O vetor que vinha sendo tratado como "canônico esperado" era:

- 6.906 matrizes locais;
- 116 filiais de matriz local;
- 284 filiais de matriz externa.

O espelho reproduzia:

- 6.881 matrizes locais;
- 102 filiais de matriz local;
- 323 filiais de matriz externa.

O total era idêntico: 7.306.

## 2. Auditoria da linhagem canônica anterior

O checkpoint de 07/09/2026, produzido quando o controle territorial RFB 2026-08 já havia sido consolidado, registra explicitamente:

- **7.306 estabelecimentos ativos**;
- **6.881 matrizes locais**;
- **102 filiais de matriz local**;
- **323 filiais de matriz externa**;
- **6.906 Entidades Empresariais**;
- **284 Entidades Empresariais de matriz externa**.

A nota `docs/caderno_base/matriz_controle_setorial_v001.md` confirma, para o universo geral de estabelecimentos, **323 filiais externas**.

Portanto, o vetor estrutural efetivamente canônico do universo geral de estabelecimentos é:

`7.306 = 6.881 + 102 + 323`.


### Evidência canônica adicional recuperada no Drive

A planilha histórica `caderno_base_territorial_v005_controle_cadastral_cnpj_20260906` registra a execução canônica `cnpj-territorial-control-202608-manual-v002`, competência 2026-08, fonte primária Receita Federal — Dados Abertos CNPJ, e o mesmo vetor estrutural 7.306 / 6.881 / 102 / 323.

A aba de validação dessa versão informa:

- v001 = 7.306 linhas e v002 = 7.306 linhas;
- zero CNPJs exclusivos entre v001 e v002;
- classes territoriais idênticas;
- matriz/filial idêntico;
- zero células diferentes nas 22 colunas comuns;
- agregados CNAE e porte idênticos;
- manifestos dos **21 insumos oficiais** idênticos;
- validação v002 sem FAIL;
- status `V001_V002_EQUIVALENCE_OK`.

A aba Metadados registra ainda o commit validado `ab85c6895d34d78b041fd4949e2d867eb511a827` e explicita que os 21 ZIPs oficiais pertencem à mesma competência. Isso torna a linhagem do vetor canônico mais forte do que uma simples referência a checkpoint: trata-se de resultado já produzido sobre a fonte oficial e submetido a equivalência v001 × v002.

## 3. Diagnóstico da divergência

### Dado observado

O espelho reproduz exatamente o vetor estrutural que já estava registrado na linhagem canônica em 07/09/2026:

| Categoria | Canônico 07/09 | Espelho | Diferença |
|---|---:|---:|---:|
| Total ativos | 7.306 | 7.306 | 0 |
| Matriz local | 6.881 | 6.881 | 0 |
| Filial de matriz local | 102 | 102 | 0 |
| Filial de matriz externa | 323 | 323 | 0 |

### Erro identificado

O vetor 6.906 / 116 / 284 não representa a decomposição matriz/filial do universo geral de 7.306 estabelecimentos.

Os valores **6.906** e **284** pertencem a outro recorte: o universo analítico de **Entidades Empresariais** e o seu subconjunto de matriz externa. Eles foram indevidamente reutilizados como se fossem, respectivamente, contagem de matrizes locais e filiais de matriz externa do universo geral.

O valor **116** não aparece como contagem canônica de filial de matriz local no checkpoint de 07/09; no vetor incorreto ele funciona como residual necessário para fechar 7.306.

## 4. Consequência metodológica

A "divergência estrutural RFB" registrada em 19/09/2026 não é sustentada pela própria linhagem do projeto.

O que ocorreu foi uma **mistura de denominadores e universos analíticos**:

- universo geral de estabelecimentos ativos: 7.306;
- decomposição territorial correta: 6.881 / 102 / 323;
- universo de Entidades Empresariais: 6.906;
- Entidades Empresariais de matriz externa: 284.

Essas métricas podem coexistir, mas não podem ser rearranjadas em uma única decomposição.

## 5. Estado após a correção

**Controle estrutural RFB 2026-08: RECONCILIADO.**

O workflow `.github/workflows/rfb-official-vs-mirror-control-validation-2026-08.yml` foi corrigido para usar como referência estrutural:

- TOTAL_ATIVOS = 7.306;
- MATRIZ_LOCAL = 6.881;
- FILIAL_DE_MATRIZ_LOCAL = 102;
- FILIAL_DE_MATRIZ_EXTERNA = 323;
- FILIAL_MATRIZ_NAO_LOCALIZADA = 0;
- INDETERMINADO = 0.

## 6. Limitação remanescente

A correção resolve o **controle estrutural** e a falsa divergência de categorias.

Permanece separadamente uma limitação de **revalidação de transporte no ambiente atual**: nas execuções recentes, o host oficial da RFB apresentou reset/time-out e não permitiu repetir agora a comparação byte a byte com SHA-256. Isso não apaga a proveniência histórica já registrada na execução canônica v002, baseada em 21 ZIPs oficiais da mesma competência com manifestos equivalentes entre v001 e v002.

Assim:

- a estrutura matriz/filial do espelho está reconciliada com a linhagem canônica;
- não se deve mais afirmar que o espelho diverge estruturalmente;
- a ausência de revalidação dos hashes oficiais atuais deve ser registrada como limitação de transporte, não como falha do indicador estrutural;
- qualquer promoção editorial de indicadores de fornecedores deve manter a distinção entre **reconciliação estrutural** e **revalidação byte a byte da fonte oficial**.

## 7. Regra para os Cadernos

Não alterar silenciosamente versões históricas.

O Caderno-Base v028 permanece **read-only**.

A correção deve entrar primeiro no mapa mestre, agenda de dados e documentação metodológica. Uma eventual promoção ao texto narrativo deve ser deliberada em versão posterior.
