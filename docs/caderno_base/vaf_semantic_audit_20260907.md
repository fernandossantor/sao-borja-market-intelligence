# VAF — auditoria semântica da fonte oficial

## Objetivo e status

Este documento registra o estado corrente da auditoria da consulta pública **Valor Adicionado Municípios** da Receita Estadual/SEFAZ-RS para São Borja.

- Abrangência geográfica: São Borja/RS.
- Fonte primária: Receita Estadual/SEFAZ-RS.
- Data da auditoria: 2026-09-07.
- Natureza: auditoria de fonte, unidade, referência temporal e campos publicados.
- Status: a célula oficial de 2025 está semanticamente confirmada; a série histórica permanece em reconciliação e ainda não deve ser reinterpretada como série por ano civil do movimento econômico.

## Cadeia oficial da consulta

A arquitetura pública reproduzida é:

`Portal IPM → /AIM/VAL-HIS.aspx → iframe AIM-WEB-VAL-HIS_1.asp → POST AIM-WEB-VAL-HIS_2.asp`.

O formulário usa `POST` e os campos observados `anoini`, `anofim`, `letramun` e `Action`. A interface disponibiliza anos de **apuração** de 1992 a 2025.

## Correção do intervalo municipal

A auditoria do HTML do formulário mostrou duas faixas contíguas:

- `S          SAO MARTINH` — **Sagrada Família até São Martinho**;
- `SAO MARTINHSZZZZZZZZZZ` — **São Martinho até Soledade**.

São Borja pertence à primeira faixa. Portanto, `SAO_BORJA_RANGE_VALUE` foi corrigido para `S          SAO MARTINH`. O teste automatizado passa a exigir essa correspondência, evitando regressão para a faixa incorreta anteriormente utilizada.

## Resultado oficial observado — apuração 2025

Execução de referência:

- workflow: `vaf-source-audit`;
- run: `34171623022`;
- job: `101892869756`;
- testes: **10/10 PASS**;
- Ruff: **PASS**;
- SHA-256 do HTML bruto do POST: `9c213b01ffc3cb6544be29d7af6b6886b6824d6d8e9270d312d74747aa42c076`.

O HTML oficial publica no `<title>`:

`SEFAZ RS - Municipais / AIM (Índice de retorno ICMS) / Valor Adicionado Municípios`

A página exibe explicitamente:

- `Anos de Apuração: 2025 até 2025`;
- `Municípios: SAGRADA FAMILIA até SAO MARTINHO`;
- cabeçalhos visíveis: `MUNICÍPIO | PREFIXO | 2025`.

A linha de São Borja é:

| Município | Prefixo | 2025 |
|---|---:|---:|
| SAO BORJA | 117 | 2.325.966.620,93 |

A própria página informa:

- moeda em 1992: cruzeiro;
- moeda em 1993: cruzeiro real;
- moeda a partir de 1994: **real**.

### Classificação do dado

**Observado em fonte oficial:** para `ano_apuracao = 2025`, a consulta pública “Valor Adicionado Municípios” publica para São Borja, prefixo 117, o valor de **R$ 2.325.966.620,93**.

Esse registro confirma:

- grandeza publicada: Valor Adicionado Municípios;
- unidade: real;
- referência temporal do cabeçalho: ano de apuração 2025;
- município/prefixo: São Borja / 117.

## Limitação temporal obrigatória

O registro de 2025 **não deve ser relabelado como valor do movimento econômico do ano civil de 2025**. O Manual AIM distingue:

1. ano-base dos dados econômico-fiscais;
2. ano de apuração do IPM;
3. ano de distribuição seguinte.

Para o critério de valor adicionado, o Manual AIM informa a utilização dos índices dos dois anos civis imediatamente anteriores ao ano da apuração. Portanto, a futura base deve preservar as dimensões temporais separadamente.

No estágio de fonte, a estrutura recomendada é:

- `municipio`;
- `prefixo`;
- `ano_apuracao`;
- `valor_adicionado_publicado_rs`;
- `moeda`;
- `fonte_url`;
- `raw_sha256`;
- `natureza = observado_oficial`;
- `ano_dado = null` enquanto a correspondência não estiver explicitamente documentada.

Não será calculado índice de valor adicionado a partir do valor monetário sem denominador estadual oficial e regra metodológica publicada.

## Limite observado do endpoint

Uma consulta exploratória de 2009 a 2019 em um único POST retornou a mensagem oficial:

`Periodo excedeu 8 anos`

Assim, a auditoria histórica deve respeitar blocos de no máximo oito anos. A reconciliação com o benchmark secundário do Sebrae/RS foi dividida em 2009–2016 e 2017–2019.

## Fontes históricas e preservação

O portal atual referencia arquivos de **Valor Adicionado Municípios 1989–1997** e **2009–2012**, mas os caminhos XLS publicados retornaram HTTP 404 na auditoria.

Uma segunda rota oficial legada da SEFAZ-RS publicou `Valor adicionado mun(1989-1997)` apontando para `ASP/Download/AIM/tabvalor.exe`. Essa rota respondeu HTTP 200.

Arquivo preservado sem execução:

- nome de auditoria: `tabvalor_1989_1997_official_opaque.exe`;
- tamanho: 55.324 bytes;
- `Content-Type`: `application/octet-stream`;
- `Last-Modified`: 2000-08-16;
- SHA-256: `8356651c0949533bd1943e4dd0a2d21748a8346b7c9d153a591dba1bce4024c0`.

Inspeção estática de contêiner indica um autoextrator RAR antigo contendo `VALADI.XLS`. Isso não equivale à leitura do XLS e não autoriza inferir cabeçalhos, unidades ou valores internos.

## Google Drive

Pasta de preservação: `_sao_borja/raw/fiscal/vaf_sefaz_rs` — Drive ID `1mTeQluzZrq5yEPIVDzdAgabaCemBxqqb`.

Pacote da execução 2025: `vaf_source_audit_run_34171623022_semantic_confirmed_package.zip` — Drive ID `1mBXcL5-ATvNWpVpaWQdJc64-T0IA7aB9`.

Documento explicativo no Drive: `VAF_SEFAZ_RS_auditoria_semantica_20260907_v001` — Drive ID `1FyCYI1ts2Uk50-IM74bd-MTRtHLF4b8hWIvkfAg1CB4`.

## Próxima validação

A próxima etapa é confrontar diretamente os valores oficiais de São Borja para os anos de apuração 2009–2019 com o benchmark secundário do Sebrae/RS 2020. O benchmark continua **não canônico** até essa reconciliação.

A série somente será promovida quando cada registro preservar unidade, rótulo temporal, município/prefixo, valor, fonte e hash/linhagem do retorno oficial, sem confundir `ano_apuracao` com `ano_dado`.
