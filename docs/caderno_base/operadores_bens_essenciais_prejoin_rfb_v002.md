# Operadores de bens essenciais — pré-join RFB v002

Atualização: 2026-09-09. Abrangência: São Borja/RS.

## Objetivo

Fechar a preparação documental dos CNPJs do universo corrente de 54 linhas de bens essenciais antes do cruzamento exato com os Dados Abertos CNPJ da Receita Federal do Brasil, mantendo a classificação territorial **pendente da fonte oficial**.

## Estado da preparação

- 54 linhas correntes classificadas como bens essenciais;
- **52 CNPJs documentais prontos** para join exato;
- prontidão: `52 / 54 × 100 = 96,2963%`;
- **0 duplicidades documentais pendentes**;
- **2 linhas sem CNPJ documental confiável**;
- 52 `MATCH_POM` e 2 `ONLY_CURRENT` na reconciliação interna.

Natureza: **calculado a partir da matriz documental**. A prontidão não é cobertura do mercado, censo de estabelecimentos ativos ou classificação local/externa.

## Resoluções documentais incorporadas

Cinco casos que estavam pendentes na versão anterior foram resolvidos documentalmente:

- Supermercado Baklizi — CNPJ `00.610.350/0017-37`, com evidência em licença de operação da Prefeitura de São Borja; o CNPJ anteriormente duplicado com Nicolini foi corrigido;
- Supermercado Nicoline — CNPJ `89.835.672/0036-50`, preservado para a unidade de São Borja após resolução da duplicidade documental;
- Mercado Precioso — CNPJ `55.330.974/0001-25`, identificado em documentação pública de rede credenciada;
- Mercado Santa Lúcia — CNPJ `07.934.366/0001-87`, identificado em relação pública estadual de credenciados da FGTAS/RS;
- Minimercado D'Gringa — CNPJ `51.634.027/0001-77`, identificado em relação pública estadual de credenciados da FGTAS/RS.

Essas identificações são **resoluções documentais**. Situação cadastral, CNAE oficial, matriz/filial, município da matriz e controle territorial somente são consolidados após o join com a RFB 2026-08.

## Pendências restantes

Sem CNPJ documental suficientemente validado:

- `Bedi Padaria e Confeitaria (Mercearia)` — cadastro interno registra endereço R. Frei Miguelino, 245, São Borja/RS e Instagram `@bedimercearia`, mas ainda sem CNPJ confiável;
- `Sabor mineiro da Lu Delícias caseiras` — cadastro interno registra R. Campos Sáles, Itachere, São Borja/RS e Instagram `@sabor_mineiro_da_lu`, mas ainda sem CNPJ confiável.

Não inferir CNPJ por similaridade nominal, telefone, endereço ou resultado comercial sem validação suficiente.

## Controle territorial

Os campos `controle_local_externo` e `municipio_matriz` permanecem `PENDENTE_RFB_OFICIAL` para os 52 CNPJs preparados.

A classificação deverá usar:

1. CNPJ completo exato no arquivo oficial de estabelecimentos;
2. `identificador_matriz_filial` da RFB;
3. registro oficial da matriz da mesma raiz CNPJ;
4. município e UF do registro oficial da matriz.

**Proibido:** usar terminação `/0001` como heurística de matriz, ou substituir os campos oficiais por endereço, telefone, nome empresarial ou narrativa documental.

## Rastreabilidade

Matriz detalhada v002 no Drive:

`matriz_operadores_bens_essenciais_prejoin_rfb_v002_20260909.xlsx`

Drive ID: `12IKd7-zipN29iAYa16HNcoBT6PFa8k2S`.

Caderno-Base corrente: `caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908`, Drive ID `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.

A aba `Operadores_prejoin_RFB` e o `Diagnostico_integrado` foram atualizados para 52/54 CNPJs prontos e 2 pendências.

## Próximo passo

Executar scan direcionado dos arquivos oficiais `Estabelecimentos0..9.zip` + `Municipios.zip` da RFB, competência 2026-08, para os 52 CNPJs. O scan deve localizar o CNPJ exato e a matriz oficial da mesma raiz, evitando o download desnecessário dos arquivos `Empresas*.zip`.