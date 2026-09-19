# Reconciliação RFB 2026-08 — universo total × Entidades Empresariais — 2026-09-19

## 1. Problema

A validação exploratória das classificações territoriais de CNPJ havia sido registrada como divergente porque se comparava o espelho 2026-08 com uma decomposição atribuída à base canônica:

- 7.306 ativos;
- 6.906 supostamente “matrizes locais”;
- 116 supostamente “filiais de matriz local”;
- 284 supostamente “filiais de matriz externa”.

Essa decomposição está incorreta porque mistura **universos distintos**.

## 2. Fonte canônica recuperada

Fonte primária da base: **Receita Federal — Dados Abertos CNPJ**.

Fonte de controle preservada no projeto:
- Google Sheet histórico: `caderno_base_territorial_v005_controle_cadastral_cnpj_20260906`;
- competência: 2026-08;
- geografia: São Borja/RS;
- unidade: estabelecimento/CNPJ ativo, situação cadastral 02;
- execução canônica: `cnpj-territorial-control-202608-manual-v002`;
- commit validado registrado: `ab85c6895d34d78b041fd4949e2d867eb511a827`;
- 21 ZIPs oficiais da mesma competência;
- auditorias registradas: `AUDIT_OK`, `NATUREZA_AUDIT_OK`, `V001_V002_EQUIVALENCE_OK`;
- manifestos v001 e v002 idênticos.

## 3. Dados observados/calculados na base canônica v005

### Universo total de CNPJs ativos

| Classe territorial | Estabelecimentos |
|---|---:|
| MATRIZ_LOCAL | 6.881 |
| FILIAL_DE_MATRIZ_LOCAL | 102 |
| FILIAL_DE_MATRIZ_EXTERNA | 323 |
| **Total** | **7.306** |

Reconciliação:

`6.881 + 102 + 323 = 7.306`

Participação de filiais de matriz externa no universo total:

`323 / 7.306 × 100 = 4,42%`

### Subconjunto “Entidades Empresariais”

A mesma base canônica registra separadamente:

- Entidades Empresariais: **6.906 estabelecimentos**;
- Entidades Empresariais de matriz externa: **284 estabelecimentos**;
- participação externa no subconjunto: **4,11%**.

Portanto, **6.906 não é o número de MATRIZ_LOCAL** e **284 não é o número total de FILIAL_DE_MATRIZ_EXTERNA**. Ambos pertencem a um recorte institucional específico.

## 4. Origem do falso conflito

A tripla `6.906 / 116 / 284` não é uma decomposição oficial das três classes territoriais.

O valor 116 corresponde aritmeticamente a:

`7.306 - 6.906 - 284 = 116`

Esse residual combina:

- total de todos os CNPJs ativos;
- subtotal de Entidades Empresariais;
- subset externo dentro de Entidades Empresariais.

Como os conjuntos não são mutuamente exclusivos dessa forma, o residual não possui interpretação válida como “filial de matriz local”.

## 5. Comparação com o espelho 2026-08

A extração exploratória via espelho havia produzido:

| Classe | Canônico oficial v005 | Espelho | Diferença |
|---|---:|---:|---:|
| Total ativo | 7.306 | 7.306 | 0 |
| MATRIZ_LOCAL | 6.881 | 6.881 | 0 |
| FILIAL_DE_MATRIZ_LOCAL | 102 | 102 | 0 |
| FILIAL_DE_MATRIZ_EXTERNA | 323 | 323 | 0 |

**Resultado:** a divergência estrutural agregada está **resolvida**. O espelho reproduz exatamente os quatro totais do universo completo da execução canônica oficial 2026-08.

## 6. O que esta reconciliação autoriza

**Autoriza:**
- encerrar a hipótese de divergência agregada de matriz/filial;
- usar a decomposição 6.881 / 102 / 323 como referência canônica para o universo total de 7.306 ativos;
- manter 6.906 / 284 apenas como recorte “Entidades Empresariais”;
- atualizar controles e documentação para remover o falso erro estrutural.

**Não autoriza automaticamente:**
- afirmar igualdade linha a linha entre espelho e os 7.306 registros oficiais sem comparação dos CNPJs;
- dispensar hash/proveniência do arquivo utilizado quando um derivado depender de classificação individual;
- promover os indicadores de footprint dos credores públicos sem controlar o join de cada CNPJ;
- interpretar matriz externa como vazamento monetário.

## 7. Implicação para compras públicas

Os indicadores exploratórios de geografia dos credores deixam de estar bloqueados por uma **suposta divergência agregada** da RFB.

A pendência remanescente para promoção é mais estreita:

1. demonstrar correspondência dos CNPJs do universo de credores/core entre o espelho usado e a execução canônica oficial, ou recuperar o derivado oficial linha a linha;
2. registrar hash/proveniência da fonte efetivamente usada no join;
3. preservar a distinção entre presença cadastral local e retenção econômica.

Até esse controle linha a linha, os percentuais de footprint permanecem **exploratórios**, mas o motivo já não é divergência dos totais matriz/filial.

## 8. Regra editorial

Não alterar retroativamente o Caderno-Base v028. Corrigir a interpretação nos controles exploratórios, nos próximos deltas e nas versões futuras.

A base oficial canônica v005 permanece a referência para 2026-08.
