# Manifesto de promoção ao Drive — remuneração territorial

## Execução

Execução canônica: `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`.

Pasta de destino no Google Drive: `territorial-wage-rais2025-rfb2026-08-drive-20260907-200236`, ID `12TDHgZ6_M63f98RMRUckTqcEA5FCRp_x`.

Data da promoção: 2026-09-07.

## Método de promoção

Após duas tentativas de escrita direta pela conta de serviço falharem com `403 Forbidden`, os sete derivados foram empacotados no Codespace e transferidos como um handoff controlado. O ZIP recebido continha exatamente os sete arquivos esperados e, antes de qualquer escrita no Drive, cada arquivo foi novamente conferido quanto a nome, tamanho e SHA-256 contra a auditoria canônica.

ZIP de handoff: 22.223 bytes; SHA-256 `a4fc57af8c7bf3f81d8d160eed9fbc954826d9d1fa55dd0af8320c779eeeff43`.

Os arquivos foram promovidos como CSVs brutos, sem conversão para Google Sheets. A pasta foi listada após a promoção e contém exatamente os sete nomes esperados, com os mesmos tamanhos em bytes da auditoria local.

Limitação de verificação: o conector Google Drive utilizado para a promoção não expõe o campo `sha256Checksum` no retorno normalizado. Portanto, o SHA-256 registrado abaixo é o hash dos bytes auditados imediatamente antes do upload; a verificação pós-upload disponível nesta etapa confirmou nome, quantidade, pasta-pai e tamanho em bytes, mas não realizou uma segunda recomputação criptográfica sobre bytes baixados do Drive.

## Arquivos promovidos

| Arquivo | Bytes | SHA-256 auditado antes do upload | Drive file ID |
|---|---:|---|---|
| `run_metadata.csv` | 1.062 | `88e00fc30380a7ae0ea12bd97882677d9cd45ad25a04dc05ee77497ecae448f7` | `12_w-dFhOarOT1cKPIHs1Xppn6oML88Bl` |
| `source_manifest.csv` | 616 | `334a77029b14e3a0f51be34adda280f62ec2e253440244fc8026ec9137729839` | `1PxFmNNRIDWwAxHbDPyg08H8oKB3pY0av` |
| `territorial_wage_by_division.csv` | 10.450 | `c6d8fe91d95324da28ad35a77d08317309ecc3c358b6f070e21a86a9ef3e667a` | `15bivaaf_fgD_zh9GMGrPL8Vtcq6aTOdC` |
| `territorial_wage_cells.csv` | 55.816 | `0c2a6bb20e2a3abcca9840536639a3f2b516802d8c0cf2fffe6e83d1e109144f` | `19WoXfENy0cihi5MeMcz0kWqCqj_BQ5Tx` |
| `territorial_wage_coverage.csv` | 680 | `337b5e080d93b76f9dc67357c03c915ed1cb44524f72aa08d5c5ecd92b44c812` | `1J_DEWZqRrUI9UpF5z9PaW3zZ7rugeG9D` |
| `territorial_wage_summary.csv` | 1.490 | `1c72ebfa313548050eb9d6684ea1e02ee5b05208e9a08634729d27d748ac5f1e` | `1K5h5wVnJMWx5X39M9QBXN0T4pkRjrP9g` |
| `validation.csv` | 306 | `3379431961f8fc030bf85c1d6ffaaf74624b37074661f7a2406b6d33e8eede7d` | `1GGOFgIWajrANx6s5n_0CovopzIKz2Eca` |

## Estado final

- arquivos esperados: 7;
- arquivos presentes no destino: 7;
- nomes divergentes: 0;
- tamanhos divergentes: 0;
- promoção parcial: não;
- status operacional: **CONCLUÍDO**.

A aba `Manifesto_remuneracao` do `caderno_base_territorial_v006_emprego_remuneracao_20260907` registra os mesmos IDs, tamanhos, hashes auditados e o método de handoff.