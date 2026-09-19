# PMSB — exposição territorial de primeira ordem das compras/contratações — 2026

Camada exploratória, não canônica.

Une:
1. pagamentos por credor/rubrica do Portal da Transparência PMSB;
2. núcleo de rubricas compatíveis com aquisição/contratação;
3. geografia cadastral RFB 2026-08.

A nomenclatura deliberadamente evita “taxa de vazamento”.

LOCAL_EXACT_ACTIVE = CNPJ credor ativo em São Borja no snapshot RFB.
LOCAL_EXACT_NONACTIVE_SNAPSHOT = CNPJ registrado em São Borja, porém não ativo no snapshot;
fica separado por incompatibilidade temporal potencial com pagamentos anteriores.
ROOT_WITH_LOCAL_ACTIVE_FOOTPRINT = CNPJ credor não é local, mas a raiz possui estabelecimento ativo local.
EXTERNAL_EXACT_ACTIVE_NO_LOCAL_FOOTPRINT = CNPJ ativo fora e raiz sem estabelecimento ativo local.
EXTERNAL_EXACT_NONACTIVE_NO_LOCAL_FOOTPRINT = registro exato fora não ativo no snapshot e sem footprint ativo local.
RFB_NOT_FOUND = sem match; não inferir.

Como a RFB oficial estava indisponível para o runner, os bytes deste enriquecimento
foram transportados por espelho do snapshot agosto/2026. Resultados permanecem
exploratórios até reconciliação por hash ou reexecução oficial.
