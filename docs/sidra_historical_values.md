# Captura histórica de valores agropecuários do SIDRA

O módulo `sbmi.sidra_historical_values_cli` executa somente as três consultas
agropecuárias previamente aprovadas para São Borja. Cada execução usa um
identificador novo e publica, sem sobrescrita, artefatos separados nas camadas
`raw`, `staging`, `curated`, `exports` e `audit`.

As respostas JSON originais são preservadas com URL, horário de obtenção,
tamanho e SHA-256. A tabela consolidada conserva o valor textual oficial e
acrescenta `numeric_value` apenas quando a conversão determinística é possível.
Marcadores oficiais como `-`, `...` e `X` permanecem registrados como
`MISSING_OR_SUPPRESSED`; não são estimados nem convertidos em zero.

Execução:

```bash
python -m sbmi.sidra_historical_values_cli
```

O plano de origem continua preservado. Uma cópia com estado `EXECUTED`, o
manifesto das respostas e o registro de validação são gravados na camada de
auditoria da nova execução.
