# Séries demográficas históricas do SIDRA

O módulo `sbmi.demography_historical_values_cli` captura duas famílias oficiais
para São Borja/RS, código IBGE `4318002`:

- tabela 6579, variável 9324: população residente estimada;
- tabela 156, variáveis 2048, 134 e 619: domicílios particulares ocupados,
  pessoas residentes nesses domicílios e média de moradores.

As famílias permanecem conceitualmente separadas. Estimativas anuais não são
tratadas como equivalentes a população recenseada, contagens populacionais ou
moradores em domicílios particulares.

Cada execução usa identificador próprio, preserva as respostas JSON e publica
novos artefatos nas camadas `raw`, `staging`, `curated`, `exports` e
`audit`. O pipeline recusa sobrescrita, limita cada resposta a 250 kB e registra
URL, horário, tamanho, tipo de conteúdo e SHA-256.

Execução:

```bash
make snapshot-base-territorial-demography-historical-values
```

Os anos ausentes não são interpolados nem preenchidos com zero.
