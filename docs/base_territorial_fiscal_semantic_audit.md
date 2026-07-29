# Auditoria semântica fiscal

## Objetivo

Auditar os seis contratos fiscais existentes em `staging` antes de qualquer
promoção para `curated`. A etapa compara transferências federais com produtos
históricos e registra bloqueios conceituais sem alterar entradas.

## Evidências observadas

- seis Parquets de staging, totalizando 8.413 linhas;
- Parquets fiscais históricos preservados no snapshot de produtos derivados;
- datas e valores presentes nas tabelas;
- fases `Empenhado`, `Liquidado` e `Pago` nas transferências estaduais;
- sinalizações de repetição na base estadual de repasses municipais.

## Resultados calculados

A comparação federal exige igualdade das doze colunas de negócio. Somente duas
normalizações são aplicadas à chave de comparação:

- meses históricos como `fev/20` são representados como `2020-02-01`;
- valores monetários são quantizados com `Decimal` para duas casas decimais.

Essas normalizações não alteram os arquivos. O resultado registra sobreposição
por ano e arquivo, linhas exclusivas de cada conjunto e duplicidades históricas.

Os 10 grupos estaduais sinalizados contêm 29 ocorrências de IPVA e 19
ocorrências excedentes sob igualdade estrita dos campos observados. Como não há
chave transacional, a política é `PRESERVE_OCCURRENCES_BLOCK_AGGREGATION`:

- preservar todas as ocorrências e linhas de origem;
- não deduplicar nem somar silenciosamente;
- bloquear agregações não qualificadas;
- admitir somente análises de sensibilidade explicitamente rotuladas.

## Bloqueios

- federal: autoridade e atualização da fonte ainda não comprovadas;
- o contrato `estadual_icms` também contém rubricas não ICMS, como IPVA, e seu
  nome precisa ser revisto antes da curadoria;
- repetições estaduais são preservadas e permanecem bloqueadas para agregação;
- transferências estaduais: fases da despesa não podem ser somadas entre si;
- tabelas municipais: período de referência e unidade não estão comprovados;
- nomes de arquivos não são aceitos como classificação substantiva.

Nenhum desses contratos é promovido para `curated` nesta etapa.

## Produtos

Cada execução cria um destino exclusivo com:

- `dataset_contract_review.csv`;
- `federal_overlap_by_year.csv`;
- `federal_overlap_by_source.csv`;
- `historical_duplicate_groups.csv`;
- `state_repetition_decisions.csv`;
- `semantic_issues.csv`;
- `fiscal_semantic_summary.csv`;
- `fiscal_semantic_manifest.csv`.

A escrita usa diretório parcial, promoção atômica e recusa sobrescrita.

## Limitações

- igualdade de conteúdo não comprova autoridade ou linhagem;
- linhas exclusivas não são automaticamente atualizações de fonte;
- valores não são declarados como reais correntes sem evidência da fonte;
- não há correção monetária ou comparação causal;
- nenhum arquivo histórico é substituído ou removido.

## Execução

```bash
make audit-base-territorial-fiscal-semantics
```
