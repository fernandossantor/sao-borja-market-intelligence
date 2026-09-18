# Radar-RS — benchmark setorial histórico — julho/2024

**Status:** exploratório — não canônico  
**Abrangência:** Rio Grande do Sul  
**Período:** julho/2024  
**Fonte secundária institucional:** TONETTO, Jorge Luís (org.). *Perspectivas para o desenvolvimento do Rio Grande do Sul: da competitividade às finanças*. Tabela 4.2. A tabela informa como fonte original: RADAR-RS — julho/2024.

## 1. Finalidade

Usar a matriz estadual histórica de origem de insumos e destino de produtos como **benchmark estrutural**, não como retrato atual de São Borja.

O dado é útil porque permite distinguir setores:
- abastecidos majoritariamente no próprio RS;
- dependentes de outras UFs/exterior;
- orientados ao mercado interno gaúcho;
- orientados a outras UFs/exterior.

## 2. Variáveis usadas

Da tabela 4.2 foram preservadas apenas as colunas cujo conceito é inequívoco no cabeçalho:
- origem dos insumos: INT / OUF / EXT;
- destino dos produtos: INT / OUF / EXT.

Não foram incorporados ao artefato os indicadores `RIPRS` e `VA`, porque suas definições não foram auditadas nesta etapa.

## 3. Cálculos SBMI

`origem_externa = OUF_origem + EXT_origem`

`destino_externo = OUF_destino + EXT_destino`

`diferença = destino_externo - origem_externa`

Quadrantes analíticos SBMI, com limiar de 50%:
- `A_INT_SOURCE_EXT_MARKET`: maioria dos insumos vem do RS e maioria das vendas vai para fora do RS;
- `B_EXT_SOURCE_INT_MARKET`: maioria dos insumos vem de fora e maioria das vendas fica no RS;
- `C_EXT_SOURCE_EXT_MARKET`: maioria dos insumos e maioria das vendas estão conectados a fora do RS;
- `D_INT_SOURCE_INT_MARKET`: maioria dos insumos e das vendas está no RS.

Esses quadrantes são **criação analítica do SBMI**, não classificação oficial da Receita.

## 4. Achados relevantes

### Agroindústria

- insumos INT: 79,30%;
- origem externa: 20,70%;
- destino externo: 63,06%;
- diferença destino externo - origem externa: +42,36 p.p.

Leitura: no benchmark estadual de 2024, agroindústria combinava forte abastecimento interno com forte orientação de vendas para fora do RS.

### Alimentos

- insumos INT: 48,34%;
- origem externa: 51,66%;
- destino externo: 49,82%.

Leitura: estrutura quase equilibrada nos dois lados, sem uma orientação tão extrema quanto agroindústria.

### Fertilizantes

- origem externa: 71,27%, dos quais 68,44% do exterior;
- destino interno RS: 60,19%.

Leitura: benchmark de cadeia fortemente dependente de insumos externos para atender majoritariamente o mercado gaúcho.

### Metalmecânico

- insumos INT: 50,71%;
- destino externo: 63,87%.

Leitura: setor estadual com orientação comercial externa relevante e base de insumos aproximadamente dividida.

### Móveis

- insumos INT: 60,61%;
- destino externo: 59,92%.

Leitura: estrutura compatível com encadeamento interno relativamente forte e vendas para fora do RS.

### Ração

- origem externa: 53,45%;
- destino interno: 57,46%.

Leitura: dependência moderada de insumos externos com orientação predominante ao mercado gaúcho.

## 5. Implicação para São Borja

O benchmark ajuda a formular perguntas, não respostas locais.

Exemplos:
- cadeias locais de agroindústria podem ser avaliadas quanto a fornecedores e destinos para verificar se reproduzem ou divergem do padrão estadual;
- fertilizantes/insumos agrícolas merecem análise como cadeia potencialmente dependente de suprimento externo;
- metalmecânico, manutenção, armazenagem e transporte podem ser analisados como serviços/indústrias de apoio às cadeias exportadoras;
- alimentos precisam ser decompostos por NCM/CNAE, porque o agregado estadual é muito heterogêneo.

## 6. Limitações

- julho/2024, não 2026;
- Rio Grande do Sul, não São Borja;
- tabela reproduzida em publicação institucional, com RADAR-RS como fonte original;
- não há causalidade implícita;
- os quadrantes usam limiar analítico arbitrário de 50%;
- diferenças entre origem e destino não são saldo comercial, valor agregado ou margem.

Arquivo estruturado:
`radar_benchmark_setorial_jul2024_v001.csv`.
