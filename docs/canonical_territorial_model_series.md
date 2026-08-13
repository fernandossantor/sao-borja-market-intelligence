# Extensão canônica das séries territoriais

## Objetivo

Acrescentar ao modelo canônico estendido sete famílias já curadas e validadas,
sem modificar os builders históricos ou substituir produtos existentes.

## Entradas e decisões

- demografia histórica SIDRA: promover somente valores numéricos;
- demografia censitária SIDRA: preservar categorias multidimensionais e excluir
  ausências/supressões;
- PIB e VAB: manter séries metodológicas, tipos de valor e variáveis separados;
- empresas e emprego: preservar unidades e não equiparar vínculos a pessoas;
- educação: preservar categorias e periodicidades de origem;
- finanças públicas locais: manter estágio não comprovado e limitações;
- DCA/SICONFI: manter conta, dimensão e medida, sem somar hierarquias.

O canônico estendido anterior é preservado integralmente como entrada imediata.
Cada família recebe um `source_dataset` próprio; finanças públicas locais e DCA
oficial não são reconciliadas como equivalentes.

## Segurança e validação

A execução escreve primeiro em diretório parcial, promove atomicamente e recusa
sobrescrita. Geografia, contratos, valores numéricos, chaves e campos obrigatórios
são validados. O manifesto registra tamanhos e hashes calculados das entradas e
saídas; ele não comprova equivalência com manifestos upstream. Valores ausentes ou
suprimidos são registrados na reconciliação e não são convertidos em zero.

## Execução

```bash
make build-canonical-territorial-model-series
```

O destino é `.data/curated/base_territorial/canonical_series`, sempre sob novo
identificador de execução.
