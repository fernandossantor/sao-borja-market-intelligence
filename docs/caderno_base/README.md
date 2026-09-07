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
- Estado dos sete CSVs remuneratórios canônicos: **7/7 promovidos ao Drive** em 2026-09-07. O handoff ZIP foi revalidado antes do upload contra os sete nomes, tamanhos e SHA-256 canônicos; após a promoção, a pasta foi conferida com exatamente sete arquivos e tamanhos idênticos aos auditados.
- Manifesto final da promoção remuneratória: `docs/caderno_base/territorial_wage_drive_promotion_manifest.md`, com IDs individuais dos sete arquivos e limitação explícita de que o conector utilizado não expõe `sha256Checksum` para uma segunda recomputação criptográfica pós-upload.

## Etapa fiscal em andamento

A v007 inicia a dimensão **VAF/fiscalidade territorializada**, sem alterar os resultados consolidados de cadastro, emprego ou remuneração.

Benchmarks oficiais atualmente registrados para São Borja:

- IPM definitivo 2025: **0,527880** — dado observado, Receita Estadual/RS;
- IPM definitivo 2026: **0,533647** — dado observado, Receita Estadual/RS;
- variação relativa 2026/2025: **+1,092483%** (aprox. **+1,09%**) — dado calculado pela fórmula `(0,533647 / 0,527880 - 1) × 100`;
- IPM provisório 2026: **0,528175** — preservado apenas para linhagem, pois foi superado pelo índice definitivo de 2026;
- IPM 2027: publicação provisória identificada, ainda sujeita ao processo de impugnação; o valor municipal de São Borja não foi incorporado à série desta etapa.

A aba `Fiscalidade_IPM` da v007 registra também mudanças de pesos informadas para o IPM provisório 2027 e a distinção metodológica central: **IPM ≠ VAF ≠ VAB ≠ arrecadação municipal**.

O estágio fiscal permanece **AUDITORIA INICIAL**. Ainda não existe série histórica canônica de VAF, decomposição definitiva dos componentes nem reconciliação do IPM com a quota-parte monetária do ICMS. Esses dados não devem ser tratados como retenção/vazamento de valor antes da conclusão dessas etapas.

Documento metodológico: `docs/caderno_base/fiscalidade_vaf_ipm_audit.md`.

A configuração de escrita controlada e as alternativas operacionais estão em `docs/drive_write_connection.md`; a execução e os controles metodológicos da remuneração estão em `docs/caderno_base/territorial_wage_drive_execution.md`.

A atualização do caderno deve acompanhar a atualização dos dados; nenhum resultado novo deve permanecer apenas em código, terminal ou conversa sem registro nos artefatos e na narrativa do projeto.
