# Séries demográficas censitárias

O pipeline `sbmi.demography_census_series_cli` captura valores oficiais do SIDRA para São Borja e publica novas camadas `raw`, `staging`, `curated`, `exports` e `audit`.

- tabela 200: sexo e grupos quinquenais de idade, 1991, 2000 e 2010;
- tabela 202: sexo e situação do domicílio, 1991, 2000 e 2010;
- tabela 9606: cor ou raça e sexo, 2010 e 2022;
- variáveis absolutas (`Pessoas`) e percentuais (`%`).

A tabela 200 é declarada pelo IBGE como produto da amostra e não deve ser equiparada automaticamente ao universo de 2022. A ausência de raça em 1991 e 2000 nesta seleção permanece vazia, sem interpolação.
