# Caderno-Base Territorial — regra de consistência

Este diretório acompanha a construção do Caderno-Base Territorial de São Borja.

## Regra operacional

Toda etapa que altere dados, indicadores, método, interpretação ou diagnóstico do Caderno-Base deve atualizar no mesmo ciclo, quando aplicável:

1. os derivados auditáveis em `.data/exports/` e sua promoção à pasta `_sao_borja/exports/` no Google Drive;
2. os manifestos, metadados, validações e hashes das saídas;
3. a narrativa analítica correspondente em `docs/caderno_base/`;
4. a versão corrente da planilha de controle do Caderno-Base no Drive, criando nova versão quando a mudança representar novo estágio substantivo;
5. a descrição do PR/branch de trabalho, preservando explicitamente o que é observado, calculado, estimado, hipótese, interpretação e recomendação.

Versões anteriores do caderno e derivados consolidados não devem ser sobrescritos quando forem necessários para auditoria histórica; nesses casos, cria-se nova versão e a anterior passa a ser marcada como histórica.

## Versão corrente neste estágio

- Caderno de controle corrente: `caderno_base_territorial_v007_fiscalidade_ipm_20260907` (Drive ID `1x83_dMuDQ9ks0mdNnv6mdw_Sopt7-KjIFWrD1rlouz8`).
- Versão histórica imediatamente anterior: `caderno_base_territorial_v006_emprego_remuneracao_20260907` (Drive ID `1A5C15qT1sAbEVnYctvGx91yokoiDOUgSDaC6UQrL8jg`).
- Controle cadastral: RFB Dados Abertos CNPJ, competência 2026-08.
- Emprego e remuneração: RAIS 2025, compatibilizada com RFB 2026-08 por células CNAE × natureza jurídica.
- Execução remuneratória canônica: `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`.
- Pasta dos derivados remuneratórios promovidos: Drive ID `12TDHgZ6_M63f98RMRUckTqcEA5FCRp_x`.
- Auditoria da execução remuneratória: 7/7 controles `PASS`, 0 vínculos `unmatched` e reconciliação integral das três métricas.
- Estado dos sete CSVs remuneratórios canônicos: **7/7 promovidos ao Drive** em 2026-09-07.
- Manifesto final da promoção remuneratória: `docs/caderno_base/territorial_wage_drive_promotion_manifest.md`.

## Fiscalidade territorial — estado atual

O primeiro bloco fiscal da v007, referente ao **IPM definitivo**, está canonizado. O bloco de **VAF** permanece em auditoria.

### IPM definitivo — série canônica

- Fonte: Receita Estadual/RS — IPM Definitivos — arquivos `DAIM545X`.
- Geografia: São Borja/RS.
- Anos de distribuição: **2003–2026**.
- Execução canônica: `ipm-definitive-sao-borja-2003-2026-v001`.
- Cobertura: **24/24 anos** e exatamente um registro de São Borja em cada arquivo.
- Validação: **7/7 controles PASS**.
- Benchmarks reproduzidos: 2025 = **0,527880**; 2026 = **0,533647**.
- Variação calculada 2026/2025: **+1,092483%** (aprox. +1,09%).
- Pasta dos cinco derivados promovidos ao Drive: ID `1YTbi1SKuaJndJ8E-GhYwqHgcN1crnjJu`.
- Promoção: **5/5 arquivos**, nomes e tamanhos pós-upload conferidos.
- Manifesto: `docs/caderno_base/ipm_definitive_drive_promotion_manifest.md`.

A v007 contém agora as abas `IPM_historico` e `Manifesto_IPM`, além de `Fiscalidade_IPM`. O status corrente é **IPM DEFINITIVO CANONIZADO — VAF ainda em auditoria**.

A regra de extração histórica é deliberadamente conservadora: usa apenas o último campo de seis casas da linha única de São Borja no `DAIM545X`. Os componentes intermediários não são interpretados porque a estrutura do arquivo muda entre os anos.

### Limitações fiscais preservadas

**IPM ≠ VAF ≠ VAB ≠ arrecadação municipal.** O IPM é um índice de repartição do ICMS; o VAF é uma grandeza fiscal utilizada em sua apuração; o VAB pertence às Contas Regionais/PIB; e transferências efetivas são fluxos financeiros. A variação do IPM não representa, por si só, a mesma variação percentual do valor monetário recebido pelo município.

A série do índice final é histórica e oficial, mas os pesos e critérios legais do IPM mudam ao longo do tempo. Portanto, não se deve atribuir uma oscilação anual a um conjunto fixo de determinantes sem decomposição metodológica específica de cada período.

O IPM 2027 permanece provisório nesta etapa e não integra a série definitiva.

## Próxima etapa fiscal

A construção da série histórica definitiva do IPM, anteriormente listada como próximo passo, está **CONCLUÍDA**.

A etapa corrente é a auditoria da fonte oficial de **Valor Adicionado dos Municípios / VAF**, com três objetivos antes de qualquer canonização:

1. identificar período, unidade, status e semântica dos campos disponibilizados pela Receita Estadual/RS;
2. verificar se os derivados fiscais já existentes no projeto contêm VAF ou se tratam apenas de SICONFI/transferências, evitando duplicidade e mistura conceitual;
3. somente após essa auditoria decidir a estrutura de uma série histórica canônica de VAF e sua posterior reconciliação com a quota-parte monetária do ICMS.

Documento metodológico principal: `docs/caderno_base/fiscalidade_vaf_ipm_audit.md`.

A configuração de escrita controlada e as alternativas operacionais estão em `docs/drive_write_connection.md`; a execução e os controles metodológicos da remuneração estão em `docs/caderno_base/territorial_wage_drive_execution.md`.

A atualização do caderno deve acompanhar a atualização dos dados; nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
