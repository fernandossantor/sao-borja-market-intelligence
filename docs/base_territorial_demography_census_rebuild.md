# Reconstrução dos produtos censitários em quarentena

A rotina `make rebuild-base-territorial-demography-census-products` reconstrói
somente composição domiciliar e território a partir dos XLSX originais já
preservados localmente. Não consulta serviços externos e não modifica os
Parquets históricos.

O fluxo publica novos produtos em `staging`, valida geografia, período, esquema,
linhas e decimais, promove cópias validadas para `curated` e registra comparação
e manifesto em `audit`. Todos os destinos usam identificador próprio e recusam
sobrescrita.

As cinco diferenças esperadas são classificadas como `EXPECTED_CHANGE`, com
justificativa `TRANSFORMATION_ERROR_CORRECTION_DECIMAL_SCALE`. Os outros 15
produtos censitários permanecem fora da reconstrução porque já são equivalentes
às entradas após canonicalização.
