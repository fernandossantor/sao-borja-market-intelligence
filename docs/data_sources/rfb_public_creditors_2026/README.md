# RFB — enriquecimento territorial de credores CNPJ — PMSB 2026

Camada exploratória, não canônica.

Fonte substantiva: Receita Federal do Brasil — Dados Abertos CNPJ,
competência 2026-08, arquivos Estabelecimentos0..9 e Municípios.

Regra de transporte:
1. tentar o host oficial da RFB;
2. se houver timeout, usar o espelho Casa dos Dados do snapshot agosto/2026;
3. registrar a origem de transporte arquivo a arquivo.

Se o espelho for usado, a classificação não deve ser promovida ao canônico
antes de reconciliação de hash com o host oficial ou reexecução oficial.

Universo: CNPJs presentes na consulta de credores do Portal da Transparência
de São Borja para 01/01/2026 até a data corrente da extração.

Classificação:
- LOCAL_EXACT: o próprio CNPJ credor é estabelecimento ativo em São Borja;
- ROOT_WITH_LOCAL_FOOTPRINT: outra inscrição da raiz possui estabelecimento
  ativo em São Borja;
- EXTERNAL_NO_LOCAL_FOOTPRINT: CNPJ encontrado, sem estabelecimento ativo
  local na raiz;
- RFB_NOT_FOUND: não localizado na competência; manter indeterminado.

A classificação é cadastral e não substitui a classificação de elegibilidade
das rubricas de compra.
