# RFB CNAE × natureza × controle territorial — snapshot de referência

**Finalidade:** referência compacta para execução reprodutível em CI da estimativa RAIS × RFB. Este arquivo não substitui a fonte mestre nem os microdados brutos.

- Arquivo lógico: `rfb_cnae_nature_territorial_cells_v001.csv`
- Fonte mestre do derivado: Google Drive do projeto, `_sao_borja/exports/`
- Drive file ID: `10Frn6bcdixiMiXNQpe_5ycKjDHOrmyCd`
- Derivação original: pipeline auditado `cnpj-territorial-control-202608-manual-v002`
- Fonte primária a montante: Receita Federal — Dados Abertos CNPJ
- Competência RFB: `2026-08`
- Abrangência: estabelecimentos ativos em São Borja/RS
- Linhas de dados: `982`
- Bytes CSV: `30429`
- SHA-256 CSV: `73d53f372abda611f448970a5ea5a362f4183aee09e14b4c355c74ff7b585497`
- Soma dos estabelecimentos nas células: `7306`
- Entidades Empresariais: `6906`
- Entidades Empresariais vinculadas a matriz externa: `284`

A representação versionada no GitHub é `rfb_cnae_nature_territorial_cells_2026-08_v001.csv.gz.b64`, criada apenas para permitir que GitHub Actions utilize o derivado quando os hosts da Receita Federal não são acessíveis a partir dos runners hospedados. Ao executar, a workflow deve decodificar Base64, descompactar Gzip e exigir o SHA-256 do CSV acima antes de qualquer cálculo.

**Natureza:** derivado calculado de microdados oficiais por pipeline auditado; não é estatística municipal publicada diretamente pela RFB.
