# Comex Stat municipal — São Borja — 2026

Camada exploratória, não canônica.

Fonte primária: MDIC/SECEX, API oficial do Comex Stat, endpoint /cities.

Recorte: São Borja/RS; janeiro-agosto/2026; filtro municipal pelo código IBGE 4318002; detalhamento por país e SH4.

Controle conceitual obrigatório: CO_MUN e SG_UF_MUN representam o domicílio
fiscal da empresa declarante. Não representam a origem física da mercadoria.

Saídas preservam direção (EXP/IMP), ano, mês, SH4, país, quilograma líquido
e US$ FOB. O SH4 1006 (arroz) é mantido apenas como primeiro teste técnico;
a arquitetura é multissetorial.
