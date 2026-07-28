# Captura oficial de valores SIDRA — São Borja

A rotina `make snapshot-base-territorial-demography-census-sidra-values` captura respostas novas e imutáveis das tabelas 4714 e 9879 para o município 4318002 e período 2022. Preserva JSON, URL, HTTP, tamanho e SHA-256; valida tipo de conteúdo, esquema mínimo, geografia, período, quantidade esperada de linhas e limites de tamanho; não altera dados históricos. Identificadores de execução devem ser nomes simples, e colisões no snapshot ou na auditoria são recusadas antes da publicação.

## Valores observados em 2026-07-24

A tabela 4714 retornou população 59676 pessoas, área 3616.690 km² e densidade 16.50 hab./km². A tabela 9879 retornou: Unipessoal 4815 domicílios e 21.31%; Nuclear 13820 e 61.17%; Estendida 3518 e 15.57%; Composta 438 e 1.94%.

Esses valores confirmam correspondência numérica com valores brutos previamente observados quando estes existem, mas não estabelecem a origem dos arquivos históricos. A diferença por fator 100 nos artefatos processados é compatível com perda de separador decimal; a etapa não autoriza correção, reconstrução ou substituição de resultados.
