# Descoberta de fontes de recursos públicos

Esta rotina captura somente páginas públicas e metadados das fontes federais
e estaduais destinadas ao território de São Borja. Não baixa bases completas,
não captura registros pessoais e não promove valores.

As famílias permanecem separadas: transferências, benefícios a residentes,
convênios/acordos e gastos ou programas aplicados na localidade. A localização
do favorecido não comprova que o recurso foi recebido pela Prefeitura.

Saídas imutáveis:

- páginas originais em `.data/snapshots/web/public_funds_discovery/<run_id>`;
- `source_inventory.csv` e `validation.csv` em
  `.data/audit/base_territorial/public_funds_discovery/<run_id>`.

Execução: `python -m sbmi.public_funds_source_discovery_cli`.
