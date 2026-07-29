# São Borja — Inteligência Mercadológica

## Ponto de situação em 29 de julho de 2026

Este documento registra o estado do projeto imediatamente após o merge do PR
#17. Ele complementa, sem substituir, o ponto de situação de 24 de julho e os
documentos metodológicos de cada módulo.

Referência confirmada no GitHub:

```text
branch: main
commit: 9da2e41e8a1685816e813d66e3f8685fe7d2b334
último PR incorporado: #17
```

## 1. Evidências observadas

### 1.1 Repositório

- PR #15, auditoria semântica fiscal, incorporado à `main`;
- PR #16, auditoria semântica RAIS, incorporado à `main`;
- PR #17, auditoria de linhagem RAIS, incorporado à `main`;
- teste `quality/test` do PR #17 concluído com sucesso antes do merge;
- arquivos históricos e artefatos em `.data` permanecem fora do Git.

### 1.2 Demografia censitária

A execução `demography-census-rebuild-20260729-001426` reconstruiu, em novos
destinos, os produtos de composição domiciliar e território. Os produtos
históricos foram preservados.

Foram documentadas cinco células históricas com perda de separador decimal:

- três em `porcentagem_de_domicilios`;
- duas em medidas decimais do produto de território.

Os outros 15 pares censitários examinados foram equivalentes sob a
canonicalização documentada.

### 1.3 Captura e auditoria de linhagem RAIS

Uma captura local, somente leitura, preservou 21 arquivos de `raw/rais`:

```text
.data/snapshots/sources/rais/rais-raw-20260729-043100/
```

A captura totaliza 11.134.154 bytes. Todos os 21 arquivos foram verificados
localmente por tamanho e SHA-256; 18 também possuíam SHA-256 esperado informado
pela fonte consultada. A ausência desse metadado nos outros três arquivos não
foi preenchida por inferência.

Duas execuções reais da auditoria foram preservadas:

```text
.data/audit/base_territorial/rais_lineage/rais-lineage-20260729-045220/
.data/audit/base_territorial/rais_lineage/rais-lineage-20260729-045503/
```

Resultados observados e calculados:

- 21 arquivos brutos e 112 arquivos processados inventariados;
- 86 pares candidatos;
- 17 pares classificados como `CONTENT_EQUIVALENT`;
- 69 pares classificados como `VALUE_DIFFERENCE`;
- nenhuma diferença estrutural entre os pares candidatos avaliados;
- 41 unidades brutas sem candidato nominal;
- 27.550 células classificadas como perda de separador decimal;
- 1.074 células classificadas como perda de valor bruto;
- 49 outras diferenças;
- 2 arquivos XLS não avaliados por ausência do leitor específico;
- 26 arquivos processados sem par candidato;
- `promotion_allowed=0`.

O par `RAIS SB 2024.csv` e `RAIS SB 2024.parquet` apresentou equivalência de
conteúdo nas 18.923 linhas e 58 colunas examinadas, sob a canonicalização
documentada.

As cinco saídas analíticas das duas execuções foram `IDENTICAL`. O manifesto
final contém 107 entradas e cinco saídas, sem erro de tamanho ou hash.

## 2. Resultados calculados

- as diferenças RAIS impedem a promoção automática dos produtos históricos
  afetados;
- a repetição integral da auditoria RAIS produziu saídas analíticas idênticas;
- a reconstrução censitária preserva os produtos anteriores e materializa as
  correções em destinos novos;
- o estado incorporado à `main` reúne as auditorias semânticas fiscal e RAIS e
  a auditoria de linhagem RAIS.

## 3. Estimativas

Não há estimativa numérica adotada como resultado neste ponto de situação.
Associações baseadas em nomes de arquivos ou abas permanecem hipóteses de par,
não vínculos comprovados de linhagem.

## 4. Interpretações

- a RAIS contém diferenças materiais de transformação que exigem tratamento
  explícito antes de qualquer curadoria;
- equivalência de conteúdo do produto RAIS 2024 não comprova, isoladamente,
  autoridade, adequação conceitual ou comparabilidade temporal;
- a reconstrução censitária resolveu um erro técnico conhecido, mas ainda
  precisa ser integrada aos consumidores sem substituir históricos;
- a política para ocorrências repetidas do ICMS continua sendo uma decisão de
  curadoria, não uma deduplicação automática.

## 5. O que pode ser concluído

- o PR #17 foi incorporado à `main` no commit registrado acima;
- as auditorias RAIS são reproduzíveis no ambiente atual para as entradas
  preservadas;
- há evidência determinística de perdas de separador decimal e de valores em
  produtos processados históricos da RAIS;
- nenhum desses produtos deve ser promovido automaticamente;
- os arquivos brutos, processados, exportações e snapshots históricos
  examinados não foram sobrescritos ou removidos.

## 6. O que não pode ser concluído

- os nomes dos arquivos não comprovam linhagem;
- equivalência de conteúdo não comprova autoridade da fonte;
- não foi determinada a causa histórica de cada transformação RAIS;
- os dois arquivos XLS não avaliados não podem ser classificados quanto ao
  conteúdo;
- não está demonstrada a adequação metodológica ou comparabilidade de toda a
  série RAIS;
- ainda não foi definida a regra de curadoria das ocorrências repetidas do
  ICMS;
- este registro não valida substantivamente todos os indicadores do acervo.

## 7. Validações já executadas

Na etapa da auditoria de linhagem RAIS:

- quatro testes focais aprovados;
- `make verify` aprovado com 198 testes e Ruff;
- pipeline real executado duas vezes;
- manifestos, resumos, diferenças, problemas e pares inspecionados;
- nenhuma diferença entre as cinco saídas analíticas das duas execuções.

Este documento deve passar novamente por `make verify` antes de ser publicado
em sua branch documental.

## 8. Operações externas

- leitura seletiva de 21 arquivos RAIS para snapshot local, sem escrita no
  Google Drive;
- push das branches dos PRs #15, #16 e #17;
- merges dos PRs #15, #16 e #17;
- nenhuma escrita, movimentação, sincronização ou exclusão no Google Drive;
- nenhuma publicação no Supabase.

## 9. Próxima ação recomendada

Ao retomar:

1. revisar e incorporar o PR documental deste ponto de situação;
2. integrar os dois produtos censitários reconstruídos aos consumidores da
   Base Territorial, sem substituir os históricos;
3. definir a política de ocorrências repetidas do ICMS antes da curadoria;
4. elaborar um mapeamento explícito dos pares RAIS prioritários e reconstruir
   somente produtos com contrato conceitual e proveniência suficientes;
5. manter `promotion_allowed=0` enquanto diferenças relevantes permanecerem.

Antes de qualquer nova coleta externa, reconstrução ou promoção, reapresentar
escopo, volume, riscos, destinos e validações para autorização.

## 10. Procedimento de retomada

```bash
git fetch origin
git switch docs/project-status-20260729
git status --short --branch
```

Depois da eventual incorporação do registro:

```bash
git switch main
git pull --ff-only
make verify
```
