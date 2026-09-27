# Checkpoint — São Borja Inteligência Mercadológica — 2026-09-09

## 1. Finalidade

Registrar o estado exato do Caderno-Base Territorial ao encerramento da sessão de 9 de setembro de 2026, preservando decisões, dados consolidados, artefatos correntes, bloqueios metodológicos e o ponto preciso de retomada.

Abrangência: São Borja/RS.  
Branch de trabalho: `feature/cnpj-territorial-control-v1`.  
PR de integração: #41 — deve permanecer **aberto, draft e não mesclado** até autorização explícita.

Checkpoint nativo no Google Drive: `Checkpoint — São Borja Inteligência Mercadológica — 20260909`, Drive ID `1EUFIFoP_2F0uZSSgLn0hdXIW9HAzUGlQ7wsnk_i5kSc`.

## 2. Caderno-Base corrente

Caderno corrente no Google Drive:

`caderno_base_territorial_v011_oferta_demanda_bens_essenciais_20260908`

Drive ID: `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`.

A v011 preserva as versões anteriores e contém, entre outras, as abas `Oferta_demanda_controle`, `Qualidade_oferta` e `Operadores_prejoin_RFB`.

A v010 permanece histórica: Drive ID `1pTYhntxHJA24geADFVFiEOYoXvc8thtEYKP7901X9Ac`.

## 3. Estado analítico consolidado

### 3.1 Estrutura empresarial e trabalho

Dados já canônicos:

- RFB 2026-08 — 6.906 estabelecimentos empresariais no universo analítico;
- 284 estabelecimentos empresariais de matriz externa;
- participação cadastral externa empresarial: **4,1124%**;
- RAIS 2025 × RFB 2026-08 — 8.595 vínculos empresariais;
- participação externa estimada no emprego: **25,1606%**;
- participação externa estimada na remuneração de dezembro: **29,6897%**.

No varejo amplo — divisão CNAE 47:

- 1.720 estabelecimentos;
- 114 filiais de matriz externa;
- participação cadastral externa: **6,627907%**;
- participação externa estimada no emprego: **37,460891%**;
- participação externa estimada na remuneração de dezembro: **38,163647%**.

Essas proporções não medem market share, faturamento, retenção ou vazamento territorial.

### 3.2 Mercado residente

- população Censo 2022: **59.676 pessoas**;
- população estimada 2025: **61.311 pessoas**;
- rendimento domiciliar per capita médio — Censo 2022: **R$ 1.568,58/mês**;
- mediana: **R$ 1.100,00/mês**;
- universo compatível da distribuição: **59.038 moradores**;
- sem rendimento ou até 2 SM per capita: **50.650 moradores / 85,79220%**;
- INSS/SUIBE julho de 2026: **R$ 24.535.168,54** em 14.247 registros de benefícios/créditos;
- Novo Bolsa Família janeiro–julho de 2026: média mensal do fluxo de referência corrente **R$ 1.502.070,14**.

As massas monetárias de Censo, RAIS, INSS e Novo Bolsa Família não devem ser somadas diretamente.

### 3.3 Demanda modelada de bens essenciais

Modelo v005:

- fonte principal: IBGE POF 2017-2018 — Rio Grande do Sul — tabela 1.3.23.3;
- benchmark atualizado: aproximadamente R$ 319,01/pessoa/mês;
- demanda modelada mensal: **R$ 19.558.852,34**;
- demanda modelada anual: **R$ 234.706.228,14**.

Natureza: **estimativa modelada** de alimentação comprada para consumo no domicílio. Não é faturamento observado nem mercado capturado.

### 3.4 Oferta e estrutura competitiva

Censo da Oferta v002:

- 138 linhas brutas POM;
- 135 nomes únicos;
- 54 linhas correntes classificadas como bens essenciais;
- 52 reconciliadas com a base POM.

A base sustenta análise estrutural, mas não é censo exaustivo de lojas ativas.

Interpretação corrente: poucos operadores generalistas de maior escala coexistem com rede numerosa de proximidade/especializados. No varejo amplo, estruturas externas apresentam peso funcional muito superior ao seu peso cadastral.

## 4. Matriz de operadores — avanço de 9 de setembro

A preparação documental passou para:

- **54 linhas correntes**;
- **52 CNPJs documentais prontos**;
- prontidão: `52 / 54 × 100 = 96,2963%`;
- **0 duplicidades documentais pendentes**;
- **2 registros ainda sem CNPJ documental suficientemente confiável**;
- 52 `MATCH_POM` e 2 `ONLY_CURRENT`.

Derivado corrente: `matriz_operadores_bens_essenciais_prejoin_rfb_v002_20260909.xlsx`, Drive ID `12IKd7-zipN29iAYa16HNcoBT6PFa8k2S`.

Nota metodológica no GitHub: `docs/caderno_base/operadores_bens_essenciais_prejoin_rfb_v002.md`.

Nota nativa no Drive: `Operadores de bens essenciais — pré-join RFB v002 — 20260909`, Drive ID `1u8l0ll_TmR4PabMuNfAQvLlUFiyFcBjkLlV4G9BJyOg`.

Pendências documentais restantes:

1. `Bedi Padaria e Confeitaria (Mercearia)`;
2. `Sabor mineiro da Lu Delícias caseiras`.

Não inferir CNPJ por similaridade nominal, telefone, endereço ou resultado comercial sem validação suficiente.

## 5. Join oficial dos 52 CNPJs — estado técnico

Workflow: `.github/workflows/bens-essenciais-operadores-rfb-join.yml`.

Método previsto: usar 52 CNPJs completos documentalmente preparados; baixar `Municipios.zip` e `Estabelecimentos0..9.zip` da RFB, competência 2026-08; localizar cada CNPJ completo por correspondência exata; usar `identificador_matriz_filial` oficial; localizar a matriz oficial da mesma raiz; recuperar município/UF da matriz; classificar controle territorial.

A execução não usa terminação `/0001` como heurística de matriz.

### Resultado da execução de 9 de setembro

Run: **34417653207**.  
Estado final: **failure**.

A falha ocorreu no passo `Download municipalities and scan official establishment files sequentially`, antes da construção da matriz final e antes do upload do artifact.

Causa observada nos logs: o runner do GitHub Actions não conseguiu estabelecer conexão HTTPS com `dadosabertos.rfb.gov.br:443`. O `curl` atingiu timeout de conexão de 30 segundos e repetiu as tentativas previstas, sem receber bytes. A execução encerrou com `curl: (28) Failed to connect ... Timeout was reached` e exit code 28.

Natureza do bloqueio: **infraestrutura/acesso à fonte externa**, não erro conceitual do método de classificação territorial e não evidência de problema nos 52 CNPJs preparados.

Consequência: **nenhum resultado local/externo por operador foi produzido nesta sessão**. Não preencher manualmente os campos pendentes.

## 6. Ponto exato de retomada

A retomada deve começar pelo join oficial dos 52 CNPJs, mas **não repetir cegamente o mesmo download** enquanto o endpoint da RFB estiver inacessível ao runner.

Ordem recomendada:

1. testar disponibilidade do endpoint oficial da RFB;
2. verificar se existe no Drive ou no pipeline canônico uma cópia integral já preservada dos arquivos de estabelecimentos 2026-08 que possa ser usada sem alterar a fonte conceitual;
3. se não houver cópia preservada, tornar o downloader mais tolerante à indisponibilidade temporária ou executar a coleta por ambiente com acesso estável, preservando hashes e arquivos oficiais;
4. somente após a obtenção íntegra dos arquivos, rodar o scan direcionado e gerar a matriz oficial;
5. promover o resultado ao Drive;
6. atualizar Caderno, diagnóstico, nota metodológica, README e corpo do PR #41;
7. depois resolver, separadamente, os dois operadores ainda sem CNPJ documental validado.

## 7. Indicadores que permanecem bloqueados

Não calcular ainda:

- market share por operador ou formato;
- faturamento médio por divisão simples da demanda pelo número de lojas;
- saturação por simples contagem de estabelecimentos;
- participação das redes externas nos R$ 234,7 milhões aplicando percentuais da divisão 47;
- retenção ou vazamento territorial apenas pela localização da matriz;
- participação da demanda por operador sem dados de vendas ou proxy explicitamente validado.

## 8. Próximo estágio analítico depois do join

Quando a classificação oficial por operador estiver concluída, construir:

`operador × formato × CNPJ/unidade × situação cadastral × CNAE × matriz/filial × município da matriz × controle local/externo × proxy de porte × confiança da reconciliação`.

Só então avançar para a pergunta substantiva: **como a demanda residente é distribuída entre formatos, operadores, canais e territórios, e que evidências podem sustentar retenção local ou saída de gasto?**

Isso exigirá dados adicionais sobre destino do gasto, compras na Argentina/outros municípios, comércio eletrônico, participação de redes e fornecedores, ou pesquisa primária.

## 9. Artefatos-chave para retomada

- Caderno v011: Drive `1dwyqUrPKs3QfMe6p5YMvbKYlZXaiDkBztdNoucvc6nc`;
- matriz pré-join v002: Drive `12IKd7-zipN29iAYa16HNcoBT6PFa8k2S`;
- nota pré-join v002 no Drive: `1u8l0ll_TmR4PabMuNfAQvLlUFiyFcBjkLlV4G9BJyOg`;
- demanda v005: Drive `1KS9glx_tES10Ry8vAGO0uQFhemOWJlO911EvliwTTTo`;
- Censo da Oferta v002: Drive `14mOXvVHmwB195HA2_jxNgrIKtoZE28Y3`;
- proxy oferta/capacidade v007: Drive `1mit1gNiFS2T4c3ax9wnyCaERuhkci0Wg`;
- workflow do join: `.github/workflows/bens-essenciais-operadores-rfb-join.yml`;
- run com falha de conectividade: `34417653207`;
- checkpoint nativo no Drive: `1EUFIFoP_2F0uZSSgLn0hdXIW9HAzUGlQ7wsnk_i5kSc`;
- PR: #41.

## 10. Regras de preservação

- Google Drive continua sendo a fonte/preservação dos dados e derivados compartilhados;
- GitHub permanece como código, documentação, histórico e controle de versão;
- cada avanço substantivo deve gerar documentação explicativa para uso nos Cadernos;
- preservar versões históricas;
- não alterar valores canônicos silenciosamente;
- distinguir observado, calculado, estimado, hipótese, interpretação e recomendação;
- não tratar correlação como causalidade;
- PR #41 permanece **aberto, draft e sem merge** até autorização explícita.