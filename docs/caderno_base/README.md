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

- Caderno de controle: `caderno_base_territorial_v006_emprego_remuneracao_20260907`.
- Controle cadastral: RFB Dados Abertos CNPJ, competência 2026-08.
- Emprego e remuneração: RAIS 2025, compatibilizada com RFB 2026-08 por células CNAE × natureza jurídica.
- Execução remuneratória canônica: `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`.

A atualização do caderno deve acompanhar a atualização dos dados; nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
