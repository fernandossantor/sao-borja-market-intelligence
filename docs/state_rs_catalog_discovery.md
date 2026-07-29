# Descoberta do catálogo estadual

A rotina consulta apenas os endpoints públicos usados pela página de dados
abertos do Transparência RS. Registra a data declarada de atualização, o ID do
relatório e o host de incorporação.

O token efêmero retornado pelo painel não é gravado, impresso nem incluído em
artefatos. A rotina não consulta o modelo Power BI, não baixa CSVs, não captura
dados pessoais e não promove valores.

Execução: `python -m sbmi.state_rs_catalog_discovery_cli`.
