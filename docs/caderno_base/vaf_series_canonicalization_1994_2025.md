# VAF de São Borja — série oficial publicada 1994–2025

## Objetivo e status

Esta nota encerra a etapa recorrente de auditoria da consulta pública de **Valor Adicionado Municípios** da Receita Estadual/SEFAZ-RS para o intervalo em que a própria página informa moeda **REAL**. A partir desta etapa, a série 1994–2025 pode ser usada como série canônica do **valor publicado pela fonte**, preservando literalmente sua dimensão temporal e sem relabelagem automática.

- Geografia: São Borja/RS.
- Prefixo publicado: 117.
- Fonte: Receita Estadual/SEFAZ-RS — `AIM-WEB-VAL-HIS_1.asp` / resultado `AIM-WEB-VAL-HIS_2.asp`.
- Cobertura: **1994–2025**, 32 rótulos anuais consecutivos.
- Unidade: **R$ correntes/nominais**, pois a página informa “Moeda a partir de 1994: REAL.”
- Natureza dos valores: **observado em fonte oficial**.
- Natureza das variações anuais: **calculado**.
- Terminologia temporal preservada: o formulário denomina o intervalo como **“Anos de Apuração”**. O projeto armazena `ano_rotulo_fonte` e não o converte automaticamente em `ano_dado`.

## Evidência e execuções

A consulta possui limite observado de oito anos por requisição. A série foi recuperada em blocos oficiais, mantendo HTML bruto e SHA-256:

| Bloco | HTTP | SHA-256 do HTML bruto |
|---|---:|---|
| 1994–2001 | 200 | `63179848519df8521699c1b543a7ddd8c2fd050d3397507ae593b1fd2da76ec5` |
| 2002–2008 | 200 | `7d182698324dea5e7155a8eb5e0b7cbb2bebd7bbb6181cee012c8ce9d43dbd0b` |
| 2009–2016 | 200 | `d2cbce2868ecdaf07e61937ebbd4ea44c2737dd61b10733656d73c18823bda2c` |
| 2017–2019 | 200 | `7ac63c358e2015f60c10ca0b594e19f4565000e2faca71f9bcbc408ffd886e39` |
| 2020–2025 | 200 | `ccdb5489ad67ac7bf0d950b07e826ce58f5f5b7410a5b6c5ddb0161fdbf82afd` |

Execuções principais:

- overlap histórico: workflow `vaf-source-audit`, run `34172172027`, attempt 2;
- fechamento dos intervalos faltantes: workflow `vaf-series-completion`, run `34173182403`;
- faixa municipal correta: valor técnico `S          SAO MARTINH`, rótulo oficial “Sagrada Família até São Martinho”.

Pacotes brutos foram preservados em `_sao_borja/raw/fiscal/vaf_sefaz_rs` no Google Drive. A série consolidada auditável foi promovida para `_sao_borja/exports/caderno-base-v008-diagnostico-integrado-v001/vaf_sao_borja_1994_2025_oficial_v001.csv`.

## Série observada e variação nominal calculada

| Rótulo da fonte | VAF publicado (R$) | Variação nominal anual |
|---:|---:|---:|
| 1994 | 37.591.078,56 | — |
| 1995 | 47.088.464,31 | +25,26% |
| 1996 | 188.740.427,55 | +300,82% |
| 1997 | 195.397.799,67 | +3,53% |
| 1998 | 220.951.545,77 | +13,08% |
| 1999 | 229.287.141,81 | +3,77% |
| 2000 | 258.529.832,55 | +12,75% |
| 2001 | 274.566.079,55 | +6,20% |
| 2002 | 317.920.102,38 | +15,79% |
| 2003 | 443.621.790,30 | +39,54% |
| 2004 | 496.430.335,02 | +11,90% |
| 2005 | 467.654.909,04 | -5,80% |
| 2006 | 467.155.296,35 | -0,11% |
| 2007 | 553.315.939,35 | +18,44% |
| 2008 | 655.362.679,07 | +18,44% |
| 2009 | 692.882.496,93 | +5,73% |
| 2010 | 742.771.982,74 | +7,20% |
| 2011 | 801.334.756,39 | +7,88% |
| 2012 | 854.643.152,23 | +6,65% |
| 2013 | 1.021.529.073,55 | +19,53% |
| 2014 | 994.834.483,43 | -2,61% |
| 2015 | 1.047.001.345,43 | +5,24% |
| 2016 | 1.211.634.280,43 | +15,72% |
| 2017 | 1.313.681.606,38 | +8,42% |
| 2018 | 1.390.390.033,25 | +5,84% |
| 2019 | 1.548.063.657,14 | +11,34% |
| 2020 | 1.844.857.219,33 | +19,17% |
| 2021 | 2.331.374.375,86 | +26,37% |
| 2022 | 2.353.300.619,62 | +0,94% |
| 2023 | 2.449.438.258,50 | +4,09% |
| 2024 | 2.907.302.928,34 | +18,69% |
| 2025 | 2.325.966.620,93 | **-20,00%** |

Fórmula das variações: `(VAF_t / VAF_t-1 - 1) × 100`.

## Reconciliação com o benchmark Sebrae/RS

O relatório Sebrae/RS 2020 reproduz VAF em milhões de reais e afirma usar “o VAF que compõe o IPM do ano corrente”. Com o fechamento dos rótulos 2007 e 2008, o benchmark foi reconciliado integralmente:

- Sebrae 2009 = 553,32 mi ↔ SEFAZ rótulo 2007 = 553,32 mi;
- Sebrae 2010 = 655,36 mi ↔ SEFAZ rótulo 2008 = 655,36 mi;
- …
- Sebrae 2019 = 1.313,68 mi ↔ SEFAZ rótulo 2017 = 1.313,68 mi.

Resultado: **11/11 correspondências consecutivas exatas** quando o valor oficial é arredondado para milhões com duas casas, sempre com deslocamento de dois anos. Trata-se de uma **correspondência observada**, útil para compreender a defasagem do relatório secundário; não autoriza substituir o rótulo temporal oficial da SEFAZ.

## Primeiras implicações analíticas

1. **Dado observado:** 2024 é o maior valor nominal da série, R$ 2,907 bilhões.
2. **Dado calculado:** 2025 recua **19,9957% nominalmente** frente a 2024.
3. **Interpretação:** a queda de 2025 merece acompanhamento fiscal, porém não pode ser convertida diretamente em previsão de queda do IPM, pois o IPM usa participação relativa, outros critérios e pesos legais variáveis.
4. **Limitação:** todo crescimento da série é nominal. Comparações de poder econômico real exigem deflação com índice e regra metodológica explicitamente escolhidos.
5. **Limitação:** para decompor o efeito do VAF no IPM, ainda falta o denominador estadual/índice relativo compatível por período e a reconstrução dos pesos legais vigentes.

## Regra operacional após o fechamento

A auditoria da fonte deixa de ser atividade recorrente. O pipeline deve ser reaberto apenas para: nova competência publicada, mudança de estrutura/metodologia da SEFAZ, falha de integridade/hashes ou necessidade específica de reconstrução dos anos em moedas anteriores a 1994. O esforço principal do Caderno-Base passa para análise, diagnóstico e integração dos indicadores já canonizados.
