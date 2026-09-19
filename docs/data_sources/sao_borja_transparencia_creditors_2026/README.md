# Portal da Transparência de São Borja — credores — 2026

Camada exploratória, não canônica.

Fonte oficial municipal: Portal da Transparência PMSB.
Endpoint reproduzido da própria interface: POST /despesas/getCredores.

Período: 01/01/2026 até a data de atualização indicada pelo portal.

Por minimização de dados pessoais, o CSV detalhado preserva somente credores
com CNPJ. Credores CPF/outros são mantidos apenas em totais agregados no JSON.

Os valores por credor ainda NÃO representam automaticamente compras públicas
elegíveis: podem incluir outras classes de despesa. Também NÃO existe, nesta
etapa, classificação local/externa. Isso exige seleção de elegibilidade e
enriquecimento cadastral RFB.
