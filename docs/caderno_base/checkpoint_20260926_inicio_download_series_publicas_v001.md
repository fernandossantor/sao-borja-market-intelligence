# Checkpoint — início do download consolidado das séries públicas — v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica  
**Repositório:** `fernandossantor/sao-borja-market-intelligence`  
**Branch:** `feature/cnpj-territorial-control-v1`  
**PR:** #41 — deve permanecer **OPEN / DRAFT / UNMERGED**.

## 1. Motivo deste checkpoint

A conversa atingiu o limite de duração do chat no momento em que foi iniciada a coleta automatizada das novas séries públicas identificadas manualmente.

Este arquivo é o handoff para continuação em novo chat sem repetir a investigação anterior.

## 2. Novas rotas oficiais identificadas

### Radar do Mercado — composição de mercado

Padrão:

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Composicao_de_Mercado_MM_AAAA.csv`

Exemplo validado:

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Composicao_de_Mercado_08_2026.csv`

Uso:
- NCM8;
- origem interna RS / outras UFs / exterior;
- valor nominal;
- análise de estrutura de abastecimento;
- benchmark estadual, nunca faturamento municipal.

### Radar do Mercado — exportações por NCM

Padrão:

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Exportacoes_NCM_MM_AAAA.csv`

Exemplo:

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Exportacoes_NCM_08_2026.csv`

Uso:
- orientação externa/exportadora por NCM;
- complemento da composição de mercado;
- benchmark estadual.

### Radar do Mercado — portfólio NCM × setor

Arquivo estático:

`https://arquivosradar.sefaz.rs.gov.br/RadarMercadoGaucho/Dados_Abertos/Portfolio_NCMs_Setor.csv`

Uso:
- taxonomia NCM × setor;
- crosswalk setorial;
- checagem de classificação.

### DFe Totais Município

Padrão:

`https://receitadados.sefaz.rs.gov.br/Arquivos/DFe_Totais_Municipio_AAAA.zip`

Uso SBMI:
- preservar somente linhas de São Borja na versão curada;
- ampliar série municipal para anos anteriores, quando disponíveis;
- manter URL e SHA256 do arquivo-fonte no manifest.

### DFe Totais CNAE Classe

Padrão:

`https://receitadados.sefaz.rs.gov.br/Arquivos/DFe_Totais_CNAE_Classe_AAAA.zip`

Uso SBMI:
- benchmark estadual por classe CNAE;
- reduzir fonte diária para `mês × modelo DFe × classe CNAE × valor/quantidade`;
- não atribuir ao município.

### Cesta de Alimentos — dados mensais por COREDE

Padrão:

`https://arquivosradar.sefaz.rs.gov.br/CestaAlimentos/Mensal_Todas/public_dados_mensais_AAAA.csv`

Exemplo:

`https://arquivosradar.sefaz.rs.gov.br/CestaAlimentos/Mensal_Todas/public_dados_mensais_2026.csv`

Uso:
- preços mensais de 80 produtos por COREDE;
- Fronteira Oeste como benchmark territorial;
- possível índice regional calculado pelo SBMI;
- não chamar de inflação de São Borja sem dado municipal.

## 3. Workflow criado

Arquivo:

`.github/workflows/download-market-dimension-public-series-v1.yml`

Commit:

`037e2eb1249766aa20f04d8d4760cb3e15a542a7`

Função:

1. testar disponibilidade de 2018–2026;
2. para 2026, testar meses jan–set;
3. baixar:
   - Composição de Mercado;
   - Exportações NCM;
   - Portfolio_NCMs_Setor;
   - CestaAlimentos anual;
   - DFe Totais Município;
   - DFe Totais CNAE Classe;
4. preservar manifest com:
   - série;
   - período;
   - URL;
   - HTTP status;
   - bytes;
   - SHA256;
   - content-type;
5. para DFe Município:
   - manter na camada curada apenas São Borja — IBGE 4318002;
6. para DFe CNAE:
   - reduzir a fonte diária a série mensal por classe CNAE × modelo DFe;
7. empacotar resultados em:
   `SBMI_public_market_series_v001.zip`.

## 4. Execuções disparadas

Push run:
`36276217961`

Pull request run:
`36276219876`

No momento da criação deste checkpoint ambas estavam em estado **queued**.

## 5. Próximos passos exatos

No novo chat:

1. consultar o estado do run `36276217961`;
2. se concluído com sucesso:
   - abrir os logs entre `SBMI_PUBLIC_SERIES_BEGIN` e `SBMI_PUBLIC_SERIES_END`;
   - registrar quais anos/meses realmente existem para cada série;
   - baixar o artifact `sbmi-public-market-series-v1`;
   - promover cópia ao Google Drive;
   - atualizar `Rastreabilidade`;
3. auditar a série `Composicao_de_Mercado`:
   - cobertura temporal;
   - NCMs;
   - corte_sigilo;
   - INT / OUF / EXT;
4. auditar `Exportacoes_NCM`;
5. cruzar `Portfolio_NCMs_Setor` com a taxonomia NCM já canonizada;
6. ampliar a série DFe municipal de São Borja se houver anos anteriores a 2023;
7. construir benchmark histórico CNAE Classe;
8. auditar continuidade dos 80 produtos da CestaAlimentos e cobertura da Fronteira Oeste.

## 6. Controles metodológicos preservados

- Composição de Mercado e Exportações NCM são benchmarks estaduais;
- corte de sigilo não deve ser tratado como zero econômico;
- DFe CNAE estadual não deve ser rateado para São Borja;
- CestaAlimentos por COREDE não é preço municipal;
- nenhuma dessas séries, isoladamente, resolve market share;
- market share continua dependente de denominador municipal-setorial + numerador empresarial compatível.

## 7. Governança

PR #41 deve permanecer:
- OPEN;
- DRAFT;
- UNMERGED.

Não mesclar sem autorização explícita do usuário.
