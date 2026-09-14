# Demanda potencial de bens essenciais — São Borja/RS — v005

Atualização: 2026-09-08.

## 1. Objeto

Estimar a ordem de grandeza da demanda potencial residente para o **núcleo alimentar comprado para consumo no domicílio** em São Borja/RS.

O resultado **não** representa a totalidade dos bens essenciais, não inclui higiene e cuidados pessoais, não mede faturamento observado e não equivale ao mercado efetivamente capturado pelos estabelecimentos locais.

## 2. Fontes e abrangência

- **Demografia:** IBGE — Censo 2022, 59.676 pessoas; IBGE — Estimativas da População 2025, 61.311 pessoas em 01/07/2025.
- **Consumo:** IBGE — Pesquisa de Orçamentos Familiares 2017-2018 — Primeiros resultados — tabelas por Unidade da Federação.
- **Benchmark principal:** Rio Grande do Sul, tabela `1.3.23.3`.
- **Atualização monetária:** IPCA nacional — grupo Alimentação e bebidas, até junho de 2026.
- **Geografia do resultado:** São Borja/RS.
- **Unidade principal:** R$/mês e R$/ano, preços aproximados de junho de 2026.

## 3. Dados observados — POF Rio Grande do Sul

Tabela `1.3.23.3`: *Despesa monetária e não monetária média mensal familiar, com alimentação, por classes de rendimento total e variação patrimonial mensal familiar — Rio Grande do Sul — 2017-2018*.

Total estadual observado:

- famílias: **4.155.820**;
- tamanho médio da família: **2,72 pessoas**;
- alimentação total: **R$ 736,69/família/mês**;
- alimentação no domicílio: **R$ 487,00/família/mês**;
- alimentação fora do domicílio: **R$ 249,69/família/mês**.

## 4. Cálculos do benchmark estadual

Conversão per capita:

`R$ 487,00 / 2,72 = R$ 179,04412/pessoa/mês`.

Fator de atualização de preços preservado no modelo:

`1,781742384675`.

Gasto per capita benchmark atualizado:

`R$ 179,04412 × 1,781742384675 = aproximadamente R$ 319,01/pessoa/mês`.

O fator usa o IPCA nacional do grupo Alimentação e bebidas. É uma **proxy de atualização monetária**, não um índice de preços de São Borja e não é restrito exclusivamente à alimentação no domicílio.

## 5. Estimativa modelada principal

População oficial estimada para 2025: **61.311 pessoas**.

Mercado mensal benchmark:

`61.311 × R$ 319,010493 = R$ 19.558.852,34/mês`.

Mercado anual benchmark:

`R$ 19.558.852,34 × 12 = R$ 234.706.228,14/ano`.

**Natureza:** ESTIMATIVA MODELADA.

O valor de **R$ 234,706 milhões/ano** deve ser interpretado como ordem de grandeza da demanda potencial residente do núcleo alimentar no domicílio. Não é faturamento observado, renda disponível ou mercado capturado.

## 6. Mudança da v004 para a v005

A v004 usava **Região Sul** como benchmark principal. A v005 usa **Rio Grande do Sul**, por maior aderência geográfica, mantendo Sul e Brasil como comparadores.

Cenário 2025, mesma população e nível de preços:

- Rio Grande do Sul: **R$ 234.706.228,14/ano**;
- Região Sul: **R$ 223.342.012,82/ano**;
- Brasil: **R$ 193.255.019,83/ano**.

Diferença RS versus Sul:

`(234.706.228,14 / 223.342.012,82 - 1) × 100 = +5,08826%`.

**Interpretação:** +5,09% é efeito da troca da referência geográfica. **Não é crescimento observado do mercado.**

## 7. Classes de rendimento — POF RS

Valores observados de alimentação no domicílio por família/mês:

| Classe de rendimento total e variação patrimonial familiar | Famílias | Tam. médio | No domicílio | Per capita calculado | % do gasto alimentar no domicílio |
|---|---:|---:|---:|---:|---:|
| Até R$ 1.908, inclusive sem rendimento | 546.135 | 2,06 | R$ 248,57 | R$ 120,67 | 78,94% |
| Mais de R$ 1.908 a R$ 2.862 | 643.114 | 2,44 | R$ 339,91 | R$ 139,31 | 78,37% |
| Mais de R$ 2.862 a R$ 5.724 | 1.433.219 | 2,80 | R$ 440,32 | R$ 157,26 | 69,81% |
| Mais de R$ 5.724 a R$ 9.540 | 874.122 | 2,98 | R$ 534,63 | R$ 179,41 | 61,99% |
| Mais de R$ 9.540 a R$ 14.310 | 343.491 | 3,08 | R$ 760,46 | R$ 246,90 | 62,64% |
| Mais de R$ 14.310 a R$ 23.850 | 205.262 | 2,98 | R$ 835,10 | R$ 280,23 | 55,71% |
| Mais de R$ 23.850 | 110.477 | 2,79 | R$ 1.253,49 | R$ 449,28 | 60,74% |

**Interpretação limitada à POF estadual:** classes inferiores apresentam menor gasto alimentar absoluto, mas parcela maior do gasto alimentar é realizada no domicílio.

Isso não autoriza atribuir automaticamente o mesmo padrão a São Borja.

## 8. Controle metodológico da renda

A v005 **não calibra o benchmark pela renda municipal**.

Motivo: as classes da POF são definidas por **rendimento total e variação patrimonial mensal familiar**. A distribuição municipal consolidada no Censo 2022 utiliza principalmente **rendimento domiciliar per capita**. Os conceitos e denominadores não são diretamente equivalentes.

Assim, a informação local de que **85,79220%** dos moradores do universo da tabela SIDRA 10296 estão sem rendimento ou em faixas de até 2 salários mínimos per capita pode orientar hipóteses, mas não é usada como multiplicador nem como chave de distribuição pelas classes da POF.

## 9. Integração oferta × demanda

O varejo (CNAE 47) permanece o principal nó externo em peso absoluto:

- presença cadastral externa: **6,63%**;
- emprego externo estimado: **37,46%**;
- remuneração de dezembro externa estimada: **38,16%**;
- participação do varejo no total externo de remuneração de dezembro: **36,41%**.

O novo benchmark dimensiona a demanda alimentar residente, mas **não permite** repartir R$ 234,7 milhões entre firmas locais e redes externas, medir retenção territorial ou inferir “vazamento” monetário.

A próxima pergunta analítica é: **como essa demanda potencial se distribui entre formatos, empresas, canais e territórios?**

## 10. Limitações e dados faltantes

- POF não municipal;
- população 2025 é estimativa oficial;
- IPCA usado é nacional e inclui alimentação fora do domicílio;
- conversão per capita não modela economias de escala intradomiciliares;
- não há calibração de renda local conceitualmente compatível;
- não entram atração de consumidores externos ou população flutuante;
- faltam destino geográfico das compras, Argentina/outros municípios, comércio eletrônico, vendas ou proxy de capacidade/porte dos operadores, preços locais, fornecedores e pesquisa primária de gasto.

## 11. Rastreabilidade

Workflow: `pof-rs-food-source-discovery`.

- run: `34293228168`;
- artifact: `10082136959`;
- pacote oficial: `tabelas_unidades_da_federacao_xls_20191108.zip`;
- tamanho: **1.409.382 bytes**;
- SHA-256 pacote: `7be3b0c5852d02ee886cf59265d0301278ff36d3d53445cab63ba7a25b525048`;
- arquivo RS: `43RS.xls.xlsx`;
- tamanho: **58.216 bytes**;
- SHA-256 43RS: `a32c3201cc201d669c65d3f46f50033bdad2e810d603a41d3731ffe64976d975`.

Google Drive:

- fonte oficial preservada em `raw/consumer`: ID `1BJiRJn8KoTYQBqlKcThFy7oCQqsv41PK`;
- derivado POF RS: `pof_rs_alimentacao_classes_2017_2018_v001_20260908`, ID `11xTjsR4AkTALlySBBomX4N20REIvG95ucKF3gjyRsfA`;
- modelo v005: `demanda_potencial_bens_essenciais_sao_borja_v005_20260908`, ID `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- documento nativo: `Demanda potencial de bens essenciais — São Borja — v005 — 20260908`, ID `19hu0twj8N1xt66zHaHW0xJbMC9pTdvyhchJYbVm2Qbg`;
- Caderno-Base v010: ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.

## 12. Uso recomendado

Usar **R$ 234,706 milhões/ano** como benchmark modelado de ordem de grandeza do núcleo alimentar no domicílio, nunca como tamanho observado do mercado. O próximo avanço de maior valor é investigar destino e retenção do gasto e construir proxy de capacidade competitiva da oferta.