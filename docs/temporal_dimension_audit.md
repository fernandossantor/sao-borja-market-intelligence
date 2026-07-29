# Integração SIDRA e diagnóstico temporal

O builder `canonical_territorial_model_extended` preserva o builder canônico
histórico e acrescenta somente os valores numéricos observados da captura
SIDRA. Marcadores ausentes ou suprimidos permanecem na fonte curada e são
registrados como exclusões; nunca são transformados em zero.

O diagnóstico `temporal_dimension_audit` mede a presença de fatos canônicos
entre 1996 e 2026 para as dez dimensões já existentes. Ele não cria dimensões e
não interpreta ausência canônica como prova de ausência em fontes brutas.

Comandos:

```bash
python -m sbmi.canonical_territorial_model_extended_cli
python -m sbmi.temporal_dimension_audit_cli
```
