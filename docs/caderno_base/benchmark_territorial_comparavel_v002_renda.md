# Benchmark territorial comparável v002 — renda domiciliar

## Objetivo

Comparar São Borja com municípios regionais de escala próxima e referências funcionais de fronteira usando **rendimento domiciliar per capita do Censo 2022**, extraído de forma homogênea do IBGE/SIDRA.

## Universo e fonte

- Fonte: IBGE/SIDRA, tabelas 10295 e 10296.
- Período: Censo 2022.
- Comparáveis por escala: São Gabriel, Alegrete e Santiago.
- Referências funcionais: Sant'Ana do Livramento e Uruguaiana.
- Workflow: `benchmark-income-sidra`.
- Run: `34532327447` — success.
- Artifact: `10173989022`.
- SHA-256 do artifact: `ed70913dedc2ac395c4b0f0ae6313520701afae12a1e94b8ac6582a39644f3df`.

## Resultados

| Município | Média R$/pc/mês | Mediana R$/pc/mês | ≤2 SM pc |
|---|---:|---:|---:|
| São Gabriel | 1.526,68 | 1.051,00 | 85,28% |
| **São Borja** | **1.568,58** | **1.100,00** | **85,79%** |
| Alegrete | 1.653,21 | 1.183,33 | 82,64% |
| Santiago | 2.097,02 | 1.342,40 | 74,14% |
| Sant'Ana do Livramento | 1.600,16 | 1.084,80 | 83,27% |
| Uruguaiana | 1.566,17 | 1.073,14 | 84,84% |

As faixas agregadas são **cálculos do SBMI** a partir das classes oficiais da tabela 10296 e não constituem classes sociais oficiais.

## Leitura

Entre os três comparáveis por escala, São Borja possui a maior participação até 2 SM per capita, mas está muito próxima de São Gabriel. A mediana é superior à de São Gabriel e inferior às de Alegrete e Santiago.

O contraste com o PIB per capita é importante:
- Alegrete: PIB pc 2023 apenas 0,24% acima de São Borja, mediana domiciliar 7,58% maior;
- Santiago: PIB pc 10,99% menor, mediana domiciliar 22,04% maior;
- São Gabriel: PIB pc 7,34% maior, mediana domiciliar 4,45% menor.

**Interpretação:** PIB per capita não representa adequadamente, sozinho, a capacidade econômica dos domicílios.

## Limitações

Rendimento domiciliar não equivale a renda disponível, consumo ou faturamento. As classes são de moradores. São Gabriel possui uma célula suprimida na faixa acima de 15 a 20 SM, por isso o agregado >5 SM não foi calculado.

## Drive

Derivados: pasta `15TbX7JhfDMzWso1Ub8Y6ruK9z7A8AQ7_`.

Documento nativo: `1VY8W00myQ59Qs6wJR1xA5yoPAHObQMxmjwqm6Hs0LR8`.
