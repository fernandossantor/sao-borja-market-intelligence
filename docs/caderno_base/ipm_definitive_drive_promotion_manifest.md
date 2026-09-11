# Manifesto de promoção ao Drive — IPM definitivo de São Borja

## Execução

Execução canônica: `ipm-definitive-sao-borja-2003-2026-v001`.

Fonte: Receita Estadual/RS — IPM Definitivos — arquivos `DAIM545X`, anos de distribuição 2003–2026.

Workflow auditada: `ipm-definitive-layout-audit`, run `34165290782`, job `101875804910`.

Artifact GitHub Actions: ID `10034030494`, nome `ipm-definitive-sao-borja-2003-2026-v001`, SHA-256 do ZIP `0e810bca54380212d8cb71f4c79c6383bcb90d9464e949f5799c44fbd74be39f`.

Pasta de destino no Google Drive: `ipm-definitive-sao-borja-2003-2026-v001`, ID `1YTbi1SKuaJndJ8E-GhYwqHgcN1crnjJu`.

Data da promoção: 2026-09-07.

## Método e validações

A rotina oficial baixou os 24 anexos definitivos publicados pela Receita Estadual/RS, de 2003 a 2026, localizou exatamente uma linha de São Borja em cada arquivo e extraiu somente o último campo de seis casas decimais do `DAIM545X`.

Os componentes intermediários do arquivo não foram interpretados porque o número e a estrutura de campos mudam entre os anos. A série canônica preserva apenas o IPM final publicado, o ano de distribuição, a variação anual calculada e a proveniência do arquivo oficial.

Validações da execução:

- 24 linhas para 24 anos;
- 24 anos únicos;
- intervalo completo 2003–2026;
- exatamente um match municipal por ano;
- todos os IPMs positivos;
- benchmark 2025 = `0,527880` — PASS;
- benchmark 2026 = `0,533647` — PASS.

Resultado: **7/7 controles PASS**.

## Arquivos promovidos

Os cinco CSVs foram promovidos sem conversão. A listagem pós-upload confirmou exatamente cinco arquivos, os cinco nomes esperados e os mesmos tamanhos em bytes observados antes da escrita.

| Arquivo | Bytes | SHA-256 auditado antes do upload | Drive file ID |
|---|---:|---|---|
| `sao_borja_ipm_definitive_2003_2026.csv` | 6.712 | `d3dcc40c2e3f9eb135ac32cde2e5a189e9db2b23aeb6cf5409b809d9794fc96c` | `1FA6YVJSKl1RMPZWyYpVHye7VCh6R9OGc` |
| `validation.csv` | 219 | `2eb0a8b497ea8fd2b52477fcf51804832723e8f5758f3b9caa2cde1e162ff6f5` | `1PgAOSTrEHdut8soXPSSiC2tUXFTQrT6v` |
| `source_manifest.csv` | 6.049 | `007d0cf881032dcd0205c19981359402507a1a1bc01c5ef4cb9bddda6bc3b85b` | `1_zSaXbX7bGrGTyUC_Pfo5fCUgu1uDR4E` |
| `run_metadata.csv` | 581 | `8d1d8c84b378f6d0d701ad82b61ff05dcac3cb3edace724d4d90f147ade9f8c7` | `1P2m0NwBr31MTlYwqBPuB_WHLZuA3Mrl0` |
| `ipm_definitive_layout_audit.csv` | 14.287 | `2f3fa595cbe3c227b09a13b3af75f743084b75166a2257d4fa845d541caf296c` | `1e8HXwjswIg3DDSKT937_G-soybqhfIDB` |

## Limitação da verificação pós-upload

O conector Google Drive utilizado não expõe `sha256Checksum` no retorno normalizado. Portanto, os SHA-256 acima correspondem aos bytes auditados imediatamente antes do upload. A verificação pós-upload confirma quantidade, nomes, pasta-pai e tamanhos, mas não constitui uma segunda recomputação criptográfica sobre bytes baixados do Drive.

## Caderno-Base

O `caderno_base_territorial_v007_fiscalidade_ipm_20260907` foi sincronizado no mesmo ciclo. Foram adicionadas as abas `IPM_historico` e `Manifesto_IPM`, e o status fiscal foi alterado de auditoria inicial de IPM para **IPM definitivo canonizado; VAF ainda em auditoria**.

Durante a primeira escrita da aba histórica, o locale `pt_BR` interpretou pontos decimais do `pasteData` como separadores de milhar. O problema foi detectado na leitura de verificação e corrigido antes do fechamento da etapa, regravando ano, IPM e variação como valores numéricos da API e aplicando formatação explícita. A leitura final reproduz os valores canônicos, inclusive `0,527880` em 2025 e `0,533647` em 2026.

## Estado final

- anos esperados: 24;
- anos presentes: 24;
- validações: 7/7 PASS;
- arquivos esperados no Drive: 5;
- arquivos presentes no Drive: 5;
- nomes divergentes: 0;
- tamanhos divergentes: 0;
- promoção parcial: não;
- status operacional: **CONCLUÍDO**.
