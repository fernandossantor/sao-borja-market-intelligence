# Snapshot piloto de recursos públicos estaduais

Baixa seis recursos oficiais do Dados RS: convênios de receita e despesa,
parcerias, seus layouts e uma competência mensal de despesas estaduais.

Os arquivos são preservados sem extração. O pipeline limita domínio, tamanho
por arquivo e tamanho total, calcula SHA-256, inventaria membros ZIP e recusa
sobrescrita. Nenhuma linha é filtrada ou promovida nesta etapa.

Execução: `python -m sbmi.state_rs_public_funds_snapshot_cli`.
