# Inventário de fontes complementares

Esta rotina captura somente as quatro páginas indicadas para São Borja:

- Panorama do Censo 2022;
- Panorama municipal do IBGE Cidades;
- perfil territorial do Observatório Sebrae.
- explorador de dados do IPS Brasil.

O HTML original é preservado com URL, data de obtenção, tamanho e SHA-256. As
URLs públicas incorporadas ao perfil do Sebrae são extraídas, filtradas pelo
município `4318002`, deduplicadas e classificadas, mas não são executadas.

Cada consulta candidata registra:

- agregador;
- fonte primária declarada;
- cubo;
- dimensão existente;
- sobreposição com produtos locais;
- decisão recomendada;
- estado obrigatório `PREPARED_NOT_EXECUTED`.

Os panoramas do IBGE são fontes primárias oficiais. Suas consultas específicas
permanecem como `QUERY_DISCOVERY_PENDING`, porque os parâmetros não devem ser
inferidos apenas a partir da interface.

O IPS Brasil é registrado como índice composto publicado e como
`PARTIAL_OVERLAP` em relação ao módulo IPS já curado. A advertência da fonte de
que as edições 2024, 2025 e 2026 não são estritamente comparáveis deve ser
preservada em qualquer captura ou transformação futura.

Execução:

```bash
python -m sbmi.complementary_source_inventory_cli
```
