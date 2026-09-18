# ANP + Cadastur — observações municipais recuperadas — São Borja — 18/09/2026

**Status:** exploratório — não canônico  
**Geografia:** São Borja/RS  
**Fontes:** ANP Dados Abertos / API Revendedores; Ministério do Turismo — Cadastur Dados Abertos.

## 1. Avanço efetivo

A limitação anterior de acesso foi superada por execução no GitHub Actions do branch exploratório.

Foram materializados:
- três arquivos municipais ANP de vendas anuais com registros de São Borja;
- resposta da API ANP de revendedores em operação;
- arquivos Cadastur 2T2026 de meios de hospedagem e agências de turismo.

Os arquivos filtrados e os resumos foram preservados em:

`docs/data_sources/secondary_official_sources_runtime/`.

Os arquivos brutos integrais permanecem no artefato da execução do workflow, com hashes SHA-256 registrados.

## 2. ANP — vendas municipais

### 2024

DADOS OBSERVADOS:

- Gasolina C: **15.929.410 litros**;
- Etanol hidratado: **592.100 litros**;
- Óleo diesel: **49.501.472 litros**.

### 2023

- Gasolina C: 10.356.700 litros;
- Etanol: 359.000 litros;
- Diesel: 32.426.894 litros.

### Variações calculadas 2023→2024

Fórmula:

`((valor_2024 / valor_2023) - 1) × 100`

Resultados:

- Gasolina C: **+53,81%**;
- Etanol: **+64,93%**;
- Diesel: **+52,66%**.

### Interpretação

Os três combustíveis líquidos apresentam aumento forte no volume municipal registrado entre 2023 e 2024.

Isso é um **fato descritivo da série ANP**.

Não é possível atribuir a variação, isoladamente, a:
- tráfego da Ponte Internacional;
- turistas argentinos;
- transporte de cargas;
- safra agrícola;
- mudança de empresas/revendedores;
- alteração de padrões de abastecimento.

A simultaneidade das altas torna o indicador relevante para investigação de mobilidade e atividade, mas **não demonstra causalidade**.

## 3. Auditoria temporal ANP

Os arquivos filtrados de gasolina C, etanol e diesel retornaram 29 linhas cada, porém 27 anos distintos.

As linhas de 1990 e 1991 aparecem duplicadas de forma idêntica no recorte extraído.

Decisão:
- os dados 2023 e 2024 não são afetados;
- qualquer série histórica integral deve remover apenas **duplicatas exatas**, registrando a operação;
- não agregar as duplicatas, pois isso duplicaria artificialmente os volumes.

A série também salta de 1991 para 2000 no arquivo retornado para São Borja. Essa ausência deve ser preservada como ausência de observação no recorte, não preenchida.

## 4. ANP — revendedores em operação

A API oficial retornou HTTP 200 e **10 registros** para São Borja/RS.

Distribuição por campo `distribuidora`:

- VIBRA: 3;
- Bandeira Branca: 3;
- IPIRANGA: 2;
- SANTA LUCIA: 1;
- RAIZEN: 1.

Natureza:
- 10 = dado observado do retorno;
- distribuição = cálculo por contagem dos registros.

### Controle

A distribuição por bandeira/distribuidora é participação no **número de revendedores retornados**, não market share de combustíveis.

A API também expõe produtos, tancagem, bicos e, em parte dos registros, georreferenciamento. Esses campos devem ser auditados separadamente antes de derivar indicadores de capacidade.

## 5. Cadastur — Meios de Hospedagem

O arquivo oficial do 2º trimestre de 2026 retornou **2 registros de São Borja**.

Ambos têm:
- Situação Cadastral = Regular;
- Situação da Atividade = Operação.

Dados observados dos registros:

Registro A:
- 70 unidades habitacionais;
- 156 leitos.

Registro B:
- 20 unidades habitacionais;
- 24 leitos.

Cálculos:

`70 + 20 = 90 UHs`

`156 + 24 = 180 leitos`

Portanto, a capacidade formal cadastrada nesses dois registros soma:
- **90 unidades habitacionais**;
- **180 leitos**.

### Limitação crítica

Não interpretar 2 como total de toda a oferta de alojamento existente em São Borja.

Cadastur e RFB/CNPJ possuem universos e regras diferentes.

O dado mede os meios presentes no arquivo oficial Cadastur consultado no 2T2026.

## 6. Cadastur — Agências de Turismo

Foram localizados **7 registros** no arquivo oficial 2T2026.

Situação:
- 6 = Regular / Operação;
- 1 = Em Implantação.

O registro em implantação foi aberto em 07/05/2026 segundo o próprio arquivo.

### Interpretação

São Borja possui base formal cadastrada de intermediação turística, mas:
- número de agências não mede fluxo turístico;
- não mede receita;
- não mede quantidade de clientes;
- não demonstra captura de visitantes da fronteira.

## 7. Implicações mercadológicas

### Mobilidade

A ANP adiciona uma série municipal objetiva que pode servir como **indicador complementar** de intensidade de abastecimento.

Ela não resolve a origem do consumidor.

### Hospitalidade

O Cadastur adiciona:
- capacidade formal cadastrada de hospedagem;
- estrutura de agências.

Isso melhora a caracterização da **capacidade de captura**, mas continua faltando a variável de demanda:
- ocupação;
- origem;
- permanência;
- ticket;
- pernoites.

## 8. Estado da agenda de dados

Frentes parcialmente fechadas:

- ANP vendas municipais: **VALORES 2024 RECUPERADOS**;
- ANP revendedores: **CADASTRO CORRENTE RECUPERADO**;
- Cadastur hospedagem: **2T2026 RECUPERADO**;
- Cadastur agências: **2T2026 RECUPERADO**.

Ainda pendentes:
- GLP — schema específico P13/OUTROS em auditoria;
- demais categorias Cadastur;
- SINAC/SIMEI municipal;
- Comex municipal;
- BET municipal.

Nenhum caderno ou base canônica foi alterado.
