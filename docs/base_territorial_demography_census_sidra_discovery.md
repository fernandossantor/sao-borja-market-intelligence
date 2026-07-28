# Descoberta oficial de metadados no SIDRA

## Escopo

A rotina captura somente páginas e descritores oficiais, preserva hashes e não executa a rota `/values`. O endpoint operacional documentado é `https://apisidra.ibge.gov.br`; `https://api.sidra.ibge.gov.br` não passou na validação TLS em 2026-07-24.

## Tabelas candidatas

- 4714: variáveis 93 (população, pessoas), 6318 (área, km², 3 casas) e 614 (densidade, hab./km², 2 casas).
- 9879: variável 800 (domicílios) e derivada 1000800 (percentual, 5 casas armazenadas e 2 apresentadas).

Na tabela 9879, a classificação 460 usa 12076 Unipessoal, 12077 Nuclear, 12078 Estendida e 12079 Composta. Para isolar os totais dessas espécies, o plano fixa os totais das classificações 68/9902, 11561/100679, 12237/104570 e 11562/72593.

## Planos de consulta

O arquivo `sidra_query_plan.csv` contém duas URLs para São Borja (`4318002`), período 2022. O estado obrigatório é `PREPARED_NOT_EXECUTED`; a descoberta rejeita `/values` em qualquer captura. Preparar uma URL é recomendação técnica e não constitui observação, download ou validação conceitual.

## Limitações

Correspondência nominal e estrutural não prova origem nem equivalência com os arquivos históricos. Não se pode concluir ainda que o percentual histórico veio da variável 1000800, que os filtros eram os mesmos, ou que dividir resultados históricos por 100 seja uma correção autorizada. O endpoint oficial `/ajax/tabela/descricao` é usado pela interface SIDRA, mas não é apresentado como parte da API REST pública estável.

Execute `make discover-base-territorial-demography-census-sidra-metadata`. Snapshots e auditorias são novos, atômicos e nunca sobrescritos.
