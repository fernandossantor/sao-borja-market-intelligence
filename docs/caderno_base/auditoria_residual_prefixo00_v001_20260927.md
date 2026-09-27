# Auditoria de qualidade do residual prefixo 00 — Radar — 27/09/2026

## 1. Objeto

Auditar os códigos da série **Radar do Mercado — Composição de Mercado** que permanecem fora da taxonomia corrigida e cujo NCM8 normalizado começa por `00`.

A finalidade é distinguir uma lacuna econômica/taxonômica de uma exceção de qualidade/codificação da fonte.

## 2. Fonte, período, unidade e abrangência

- fonte primária: Receita Estadual/RS — Radar do Mercado — Composição de Mercado;
- período: julho/2024 a agosto/2026;
- arquivos brutos: 26 CSVs mensais;
- geografia: Rio Grande do Sul;
- unidade monetária: valor nominal publicado na fonte;
- camada curated de referência: run `36326283761`;
- camada analítica de referência: run `36326631575`.

A auditoria retornou aos arquivos brutos para preservar `cod_ncm` antes da normalização por preenchimento com zeros à esquerda.

## 3. Resultado geral

**Dados observados/calculados:**

- 47 NCM8 normalizados com prefixo `00`;
- 235 linhas brutas correspondentes;
- 203 linhas sob `corte_sigilo=1`;
- taxa de linhas sob sigilo: **86,382979%**;
- valor publicado não suprimido: **R$ 2.047.333**;
- participação no valor residual total da Composição: **98,676162%**.

O residual total publicado fora da taxonomia corrigida é R$ 2.074.800. Como a cobertura monetária da taxonomia é 99,999817%, o residual do prefixo `00` representa parcela imaterial do valor publicado total, embora domine o resíduo ainda não classificado.

## 4. Estrutura do código original

Os 235 registros se dividem em duas classes de formato bruto:

### Códigos originais com 2 dígitos

- 142 linhas;
- 24 códigos brutos distintos;
- 111 linhas sob sigilo;
- R$ 2.045.661 publicados.

### Códigos originais com 8 dígitos já iniciados por 00

- 93 linhas;
- 24 códigos brutos distintos;
- 92 linhas sob sigilo;
- R$ 1.672 publicados.

Assim, praticamente todo o valor publicado do prefixo `00` vem de códigos originalmente curtos, e não de NCM8 reconhecidos na dimensão taxonômica completa do Radar.

## 5. Concentração do valor publicado

Somente três códigos normalizados possuem valor publicado não suprimido maior que zero.

| Código bruto | NCM8 normalizado | Linhas | Linhas sob sigilo | Valor publicado | % do prefixo 00 |
|---|---:|---:|---:|---:|---:|
| 00 | 00000000 | 80 | 50 | R$ 2.041.248 | 99,702784% |
| 99 | 00000099 | 11 | 10 | R$ 4.413 | 0,215549% |
| 00061046 | 00061046 | 10 | 9 | R$ 1.672 | 0,081667% |

Os outros 44 códigos normalizados possuem valor publicado agregado igual a zero e todas as suas 134 linhas estão sob corte de sigilo.

**Controle:** valor publicado igual a zero sob sigilo é censura e não prova ausência de operação econômica.

## 6. Código bruto 00

O código bruto `00` é o principal responsável pelo residual monetário:

- 80 linhas no período;
- 50 sob sigilo;
- R$ 2.041.248 publicados.

Do valor publicado:
- R$ 2.040.671 estão em `emit_uf=RS` e `tipo_operacao=INT`;
- R$ 577 estão em `emit_uf=SC` e `tipo_operacao=OUF`;
- demais combinações aparecem integralmente sob sigilo ou sem valor publicado.

A fonte não fornece informação suficiente, neste recorte, para reconstruir qual NCM econômico deveria substituir o código `00`.

## 7. Efeito da normalização

A normalização SBMI retém dígitos e completa o código para oito posições com zeros à esquerda.

Isso é adequado quando o problema é apenas a perda de zeros à esquerda, mas pode aproximar formatos diferentes em registros anômalos.

Foi observado um caso explícito:

- código bruto `01`;
- código bruto `00000001`;

ambos convergem para o NCM8 normalizado `00000001`.

Todos os registros desse caso estão sob sigilo e não possuem valor publicado não suprimido, portanto não há impacto monetário atual. Mesmo assim, a ocorrência justifica preservar o código bruto em futuras camadas curated.

## 8. Interpretação

A evidência sustenta tratar o prefixo `00` como **exceção de qualidade/codificação da fonte**, e não como conjunto econômico ainda aguardando classificação setorial.

Fundamentos:

1. a dimensão taxonômica completa do Radar não contém esses códigos;
2. a maior parte do valor publicado vem de códigos brutos com apenas dois dígitos;
3. o código bruto `00` sozinho concentra 99,702784% do valor publicado do prefixo;
4. 44 dos 47 códigos normalizados só aparecem sob sigilo;
5. não há base documental para imputar esses registros a grupos de afinidade existentes.

## 9. Decisão de governança

**Recomendação baseada em evidência:**

- não classificar os códigos prefixados `00` em grupos SBMI;
- manter o valor fora dos benchmarks setoriais classificados;
- registrar o residual como **exceção de qualidade da fonte / NCM não classificável**;
- preservar os registros na base de controle;
- monitorar se o valor residual aumenta materialmente em novas atualizações.

A cobertura monetária de 99,999817% é suficiente para o uso analítico dos benchmarks publicados, desde que o residual permaneça documentado.

## 10. Melhoria de pipeline

Em uma futura revisão da camada curated, preservar simultaneamente:

- `cod_ncm_fonte`;
- `ncm8_normalizado`;
- comprimento do código bruto em dígitos;
- flag de aderência à dimensão taxonômica.

Essa melhoria aumenta a auditabilidade sem exigir reclassificação econômica do residual e não bloqueia o fechamento da v029.

## 11. O que não é possível concluir

Os dados disponíveis não permitem determinar:

- a categoria econômica real do código bruto `00`;
- a qual NCM8 os registros deveriam pertencer;
- se os códigos curtos são placeholders, erros de preenchimento, categorias técnicas internas ou outro tratamento da fonte;
- o valor econômico integral dos registros sob sigilo.

Essas lacunas não devem ser preenchidas por inferência.

## 12. Artefatos

- documentação Drive: `1Z4nhQQpJlOwBlc238GcAi41ANKo_W6irH6oTFrUQAXw`;
- tabela auditável: `docs/caderno_base/dados/radar_prefixo00_raw_code_audit_v001.csv`;
- Caderno-Base: aba `Taxonomia_Radar_v029`, sheetId `1498802222`.

## 13. Próxima etapa

A frente taxonômica deixa de bloquear o fechamento da v029.

Próximo passo:
1. executar QA editorial final;
2. verificar consistência entre Caderno-Base, Factsheet, Storyboard e Caderno Geral;
3. decidir congelamento/publicação da v029.

## 14. Governança

- bruto imutável;
- código bruto e código normalizado não são sinônimos;
- sigilo ≠ zero econômico;
- residual não recebe imputação automática;
- Radar/RS ≠ São Borja;
- PR #41 permanece **OPEN / DRAFT / UNMERGED**.
