# Checkpoint — conversão territorial, contas públicas e mapa mestre de variáveis — 19/09/2026

**Projeto:** São Borja — Inteligência Mercadológica  
**Data:** 19/09/2026  
**Branch de trabalho:** `explore/receita-estadual-rs-market-intel-v1`  
**PR #41:** deve permanecer **aberto, draft e sem merge**.  
**Caderno-Base:** v028, **read-only**, sem promoção automática.  
**Documento mestre de auditoria:** `1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`  
**Matriz exploratória:** `1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`

---

## 1. Regra central de continuidade

O projeto está organizado pelo modelo:

**entrada exógena / produção territorial → cadeia produtiva → VAB → apropriação primária → renda residente → gasto local → recirculação empresarial → saída/vazamento → resultados territoriais.**

Nenhuma etapa pode ser tratada como equivalente à outra.

Controles permanentes:

- VAB não é faturamento;
- transferências públicas não são VAB nem renda domiciliar;
- consumo intermediário já foi deduzido do VAB;
- remuneração/VAB não é taxa de retenção;
- fornecedor externo não equivale a 100% de vazamento;
- fornecedor local não equivale a 100% de retenção;
- presença digital não equivale a maturidade/conversão;
- estabelecimento externo/matriz externa não é market share;
- fluxo físico de fronteira não é gasto local;
- correlação entre retenção, renda e migração não prova causalidade.

---

## 2. Estado atual da tese territorial

A hipótese geral evoluiu de uma ideia genérica de “vazamento” para um diagnóstico em etapas:

> São Borja apresenta geração relevante de valor e entradas externas de recursos, mas os diferentes circuitos econômicos possuem capacidades muito distintas de transformar esses fluxos em remuneração de residentes, compras locais, recirculação empresarial e reinvestimento. A questão territorial prioritária é a **conversão e retenção seletiva** do valor, não a ausência de geração.

O terciário privado não “apenas circula”: em 2021 gerou VAB observado de **R$ 928,203 milhões**, superior ao agro (**R$ 795,875 milhões**). A administração pública gerou VAB de **R$ 351,229 milhões**.

A tese permanece **parcialmente sustentada**. Não existe uma taxa única observada de retenção municipal.

---

## 3. Contas públicas — novo recorte temporal obrigatório

A partir deste checkpoint, contas públicas devem ser tratadas em dois planos temporais.

### 3.1. Plano fiscal agregado — 2019–2026

Recorte preferencial: **2019–2025 anos fechados + 2026 parcial/execução corrente**.

Variáveis obrigatórias:

- receita corrente;
- transferências correntes;
- FPM;
- ICMS quota-parte;
- Fundeb;
- IPVA;
- ITR;
- outras transferências relevantes;
- despesa empenhada;
- despesa liquidada;
- despesa paga;
- composição funcional;
- pessoal/previdência;
- juros e dívida;
- investimentos;
- aquisição de bens/serviços/obras.

Fonte principal para séries fechadas:
- SICONFI/FINBRA/DCA/RREO quando conceitualmente comparável;
- Portal da Transparência PMSB e TCE-RS/SIAPC como camadas de execução;
- LDO/LOA apenas como projeção/orçamento, nunca confundidas com realizado.

Já observado:
- transferências correntes realizadas municipais 2019–2025;
- 2025 = **R$ 295,355 milhões**;
- participação média aproximada das transferências na receita corrente 2019–2025 = **74,64%**.

### 3.2. Pagamentos por credor / compras — série desejada 2019–2026

Foi criado workflow:
`.github/workflows/sao-borja-public-accounts-timeseries-discovery.yml`.

Run inicial:
- 2026: rota funcionou;
- 2019–2025: a interface atual retornou erro de JSON no endpoint de credores;
- isso **não significa ausência de dados**;
- a rota histórica precisa ser investigada por parâmetros/arquivos alternativos.

2026 parcial, 01/01 a 18/09:
- 1.930 credores;
- 740 CNPJs;
- 1.190 CPFs;
- pago total = **R$ 275.649.734,78**;
- pago a CNPJ = **R$ 132.146.080,70**;
- pago a CPF = **R$ 143.503.654,08**.

Regra de continuidade:
- buscar série histórica no Portal/TCE/SIAPC;
- se a geografia histórica do fornecedor for calculada, usar snapshot cadastral compatível com cada exercício ou explicitar a limitação;
- 2026 nunca deve ser comparado como ano cheio.

---

## 4. Compras/contratações públicas — 2026

### 4.1. Reconciliação

669 CNPJs com pagamento positivo foram reextraídos no nível do empenho.

Controle:
- 669/669 processados;
- 33 rubricas;
- total CNPJ por credor = **R$ 132.146.080,70**;
- soma por empenho = **R$ 132.146.080,70**;
- diferença = **R$ 0,00**.

### 4.2. CORE_PROCUREMENT

Núcleo conservador de rubricas compatíveis com compra/contratação:

**R$ 72.039.491,18**.

Representa:
- 54,52% do pago a CNPJ;
- 26,13% do pago total.

Não é universo jurídico perfeito de licitação/contrato.

### 4.3. Exposição territorial — provisória

Com geografia cadastral RFB 2026-08 transportada por espelho:

- LOCAL_EXACT_ACTIVE = **R$ 43.751.499,71 = 60,73%**;
- ROOT_WITH_LOCAL_ACTIVE_FOOTPRINT = **R$ 10.184.036,91 = 14,14%**;
- presença local ampliada = **74,87%**;
- externo sem footprint local = **25,13%**.

Sensibilidade sem Fundação Ivan Goulart:
- presença local ampliada = **58,57%**;
- externo sem footprint = **41,43%**.

### 4.4. Heterogeneidade por tipo de aquisição

- serviços PJ genéricos: presença local ampliada **91,22%**;
- serviços PJ genéricos sem Fundação Ivan Goulart: **80,27%**;
- bens + materiais + equipamentos: presença local **25,90%**, externa **74,09%**;
- obras e instalações: presença local **91,75%**;
- TIC: externa **66,37%**;
- consultoria: externa **89,74%**;
- passagens/locomoção: externa **85,87%**;
- TIC + consultoria + passagens: externa **70,24%**.

### 4.5. Função orçamentária

- Saúde = R$ 39,520 mi, 54,86% do core; presença local ampliada 81,20%;
- Urbanismo = R$ 12,309 mi; presença local 83,41%;
- Educação = R$ 7,704 mi; presença local 67,36%;
- Administração = R$ 6,234 mi; aproximadamente 50/50;
- Assistência Social = R$ 2,439 mi; externa 53,49%;
- Transporte = R$ 0,982 mi; externa 87,91%.

### 4.6. Fundação Ivan Goulart

- total pago = R$ 30.769.932,49;
- core = R$ 28.342.657,23;
- 39,34% do core municipal;
- 71,72% do core de Saúde;
- 100% dos pagamentos na função Saúde;
- 99,75% ligados à assistência de média/alta complexidade.

Não tratar como fornecedor mercantil ordinário.

### 4.7. Geografia dos credores externos

Dos **R$ 18,103 milhões** sem footprint local:

- 60,87% sediados em outros municípios do RS;
- 39,13% em outras UFs.

Principais polos cadastrais:
- Porto Alegre;
- Curitiba;
- Brasília;
- Pinhalzinho/SC;
- Santo Antônio das Missões.

A competição por fornecimento é principalmente **intermunicipal dentro do RS**.

---

## 5. ALERTA CRÍTICO — validação do espelho RFB falhou estruturalmente

Workflow de validação do espelho RFB 2026-08:
`rfb-mirror-sao-borja-control-validation-2026-08`.

Resultado:

Total de estabelecimentos ativos:
- canônico esperado = **7.306**;
- espelho observado = **7.306**;
- reconciliação total = **exata**.

Porém, estrutura matriz/filial NÃO reconciliou:

| Categoria | Canônico | Espelho | Diferença |
|---|---:|---:|---:|
| Matriz local | 6.906 | 6.881 | -25 |
| Filial de matriz local | 116 | 102 | -14 |
| Filial de matriz externa | 284 | 323 | +39 |
| Não localizada | 0 | 0 | 0 |

Portanto:

- o espelho NÃO pode ser tratado como reprodução estrutural exata da base canônica;
- os indicadores de footprint de fornecedor público continuam **exploratórios**;
- antes de promoção, diagnosticar se a divergência decorre de:
  - snapshot de 09/08 versus competência canônica;
  - alteração cadastral intramês;
  - diferença no algoritmo de matriz/filial;
  - diferença de bytes entre espelho e fonte oficial;
- buscar hash/bytes oficiais ou reexecutar pela mesma fonte/base usada na canonização.

**Não promover ao Caderno enquanto esse controle não for resolvido.**

---

## 6. Mapa mestre de todas as variáveis ativas

A matriz exploratória ganhou a aba:
**`Mapa_variaveis_ativas`**.

Ela passa a ser o inventário obrigatório de continuidade. Nenhum eixo abaixo deve ser descartado silenciosamente.

### 6.1. Demografia
- população histórica;
- estimativas intercensitárias;
- urbanização;
- domicílios ocupados;
- moradores por domicílio;
- saldo migratório residual;
- perfil/destino/motivo da migração — ainda aberto.

### 6.2. Renda
- renda domiciliar média e mediana;
- distribuição por faixas;
- base de renda alta/nichos;
- conversão contextual PIB pc → renda residente;
- comparação territorial com São Gabriel, Alegrete, Santiago, Santana do Livramento e Uruguaiana.

### 6.3. Trabalho
- emprego formal por setor;
- massa de remuneração;
- mediana salarial;
- setor público;
- varejo;
- agro;
- agroindústria;
- alimentação;
- transporte;
- serviços administrativos;
- comparação salarial por CBO/jornada/escolaridade — ainda aberta.

### 6.4. Entradas externas de renda
- INSS;
- Novo Bolsa Família;
- folha pública federal/estadual/outros órgãos;
- transferências federativas;
- gasto de visitantes — ainda não observado monetariamente;
- exportações por domicílio fiscal.

### 6.5. Produção e VAB
- PIB total;
- VAB total;
- VAB agro;
- VAB terciário privado;
- VAB administração pública;
- estrutura de geração por circuito;
- atualização do PIB municipal quando publicada.

### 6.6. Apropriação do valor
- remunerações/VAB;
- EOB/rendimento misto;
- propriedade/residência dos recebedores;
- lucros/dividendos;
- renda da terra;
- juros;
- reinvestimento;
- destino patrimonial — vários ainda bloqueados.

### 6.7. Agro e cadeia produtiva
- custo do arroz Conab 2025/26;
- insumos;
- defensivos;
- fertilizantes;
- sementes;
- mecanização;
- irrigação;
- transporte;
- armazenagem;
- juros;
- depreciação/capital;
- conteúdo externo via MIP-RS;
- beneficiamento de arroz;
- manutenção de máquinas;
- origem municipal dos fornecedores B2B — aberta;
- outras culturas relevantes — ampliar.

### 6.8. Crédito e finanças
- SICOR;
- crédito rural;
- ESTBAN;
- crédito total;
- depósitos;
- poupança;
- depósitos a prazo;
- estrutura bancária;
- retenção financeira;
- não usar queda de depósitos como “fuga de capital”.

### 6.9. Contas públicas
- receitas correntes;
- transferências correntes;
- FPM;
- ICMS;
- Fundeb;
- IPVA;
- ITR;
- outras transferências;
- pessoal/previdência;
- dívida/juros;
- investimento;
- despesa empenhada;
- liquidada;
- paga;
- credores;
- compras/contratações;
- função/subfunção/programa/ação;
- geografia de fornecedores;
- objetos/itens;
- cadeia subsequente;
- série 2019–2026.

### 6.10. Fiscalidade
- IPM 2003–2026 — fechado;
- VAF — ainda em auditoria;
- não confundir VAF com transferências.

### 6.11. Estrutura empresarial
- RFB ativos;
- matriz/filial;
- raiz empresarial;
- grupos externos;
- footprint local;
- Simples/SINAC;
- SIMEI/MEI;
- CNAEs;
- validação temporal dos POMs.

### 6.12. Conjuntura
- BET municipal — rota ainda aberta;
- PCA/ICA regional;
- inflação/preços;
- eventual preço municipal estruturado;
- Radar Receita RS INT/OUF/EXT — dados ainda pendentes.

### 6.13. Comércio exterior e fronteira
- Comex municipal;
- exportações/importações;
- países;
- SH4/NCM;
- ANTT fluxo físico fronteiriço;
- diferença fluxo físico × captura local;
- logística/espera.

### 6.14. Mobilidade/combustíveis
- gasolina;
- etanol;
- diesel;
- GLP;
- revendedores;
- série temporal;
- relação com logística/fronteira sem inferência causal automática.

### 6.15. Turismo
- Cadastur;
- hospedagem;
- UHs;
- leitos;
- agências;
- guias;
- organizadores;
- transportadores turísticos;
- ocupação/pernoite — pendente;
- origem/ticket/gasto — pendente.

### 6.16. POM — Bens Essenciais
- universo 54;
- 52 CNPJs validados;
- 2 pendentes;
- matriz externa;
- emprego/remuneração de estabs externos;
- presença digital 72,22%;
- preços;
- ruptura;
- fila;
- ticket/missão;
- market share — não observado.

### 6.17. POM — Saúde/Higiene
- farmácias/drogarias;
- 20 CNPJs;
- 7 raízes;
- 85% unidades em raízes multiunidade;
- presença digital nominal 100%;
- maturidade;
- conversão;
- convênios;
- demanda institucional;
- compras públicas de saúde;
- market share — não observado.

### 6.18. POM — Bens Não Essenciais
- 103 CNPJs;
- 99 raízes;
- baixa multiunidade;
- presença digital 97,5%;
- nichos;
- renda discricionária;
- e-commerce;
- compra extralocal;
- TAM residente;
- captura regional;
- market share — não observado.

### 6.19. POM — Alimentação e Serviços
- CNAE 56;
- 409 estabelecimentos;
- 99,02% matriz local;
- turismo/experiência 542;
- 99,08% matriz local;
- inventário geral POM de serviços inválido para contagem — precisa reconstrução;
- ticket;
- origem;
- ocupação;
- delivery;
- no-show;
- lead→contrato;
- cadeia de insumos.

### 6.20. Digital
- presença;
- frequência de atualização;
- catálogo;
- preço;
- estoque;
- SLA;
- avaliações;
- resposta útil;
- integração;
- conversão digital→compra;
- conversão digital→loja.

### 6.21. Consumidor e demanda
- destino monetário do gasto;
- gasto local;
- outros municípios;
- Argentina;
- e-commerce;
- origem do cliente;
- residente;
- região;
- visitante;
- estudante;
- transportador;
- motivo;
- ocasião;
- permanência;
- ticket;
- missão de compra.

Essas são algumas das **maiores lacunas decisórias** e exigem pesquisa primária/dados empresariais.

### 6.22. Concorrência e captura
- market share;
- faturamento;
- concentração;
- redes;
- substitutos;
- compras centralizadas;
- matriz externa;
- escala;
- presença operacional;
- origem do fornecedor;
- não usar emprego/CNPJ como share.

### 6.23. Resultado territorial
- população;
- migração;
- emprego;
- renda;
- profundidade de nichos;
- densidade empresarial;
- retenção de jovens/profissionais;
- relação entre produção e mercado consumidor;
- causalidade permanece aberta.

---

## 7. Rotas abertas prioritárias

Ordem recomendada de continuidade:

1. **Contas públicas 2019–2026**
   - diagnosticar erro histórico do Portal;
   - montar série fiscal agregada SICONFI;
   - tentar série histórica de empenhado/liquidado/pago por credor;
   - só depois replicar geografia de fornecedores.

2. **Reconciliar RFB**
   - resolver divergência matriz/filial do espelho;
   - não promover compras públicas enquanto isso.

3. **VAF**
   - concluir série oficial.

4. **BET municipal**
   - obter valor/série reproduzível de São Borja.

5. **Radar Receita RS**
   - materializar CSVs reais e INT/OUF/EXT.

6. **SINAC/SIMEI**
   - recuperar decomposição CNAE completa do run reconciliado ou refazer paginação.

7. **Agro B2B**
   - medir origem dos fornecedores/compras.

8. **Destino do gasto / origem do cliente**
   - desenhar pesquisa primária transversal.

9. **Maturidade digital**
   - protocolo comum para os quatro POMs.

10. **Inventários POM**
   - fechar CNPJs pendentes;
   - revalidar ativos;
   - reconstruir serviços.

---

## 8. Artefatos novos desta fase

GitHub:
- `docs/data_sources/modelo_conversao_territorial_20260919_v001.md`
- `docs/data_sources/conab_rice_cost_exposure_2025_v001.md`
- `docs/data_sources/mip_rs_input_externality_benchmark_v001.md`
- `docs/data_sources/compras_publicas_hierarquia_evidencia_v001.md`
- `docs/data_sources/sao_borja_transparencia_creditors_2026/`
- `docs/data_sources/sao_borja_transparencia_cnpj_rubricas_2026/`
- `docs/data_sources/public_procurement_core_analytics_2026/`
- `docs/data_sources/rfb_public_creditors_2026/`
- `docs/data_sources/public_procurement_territorial_exposure_2026/`
- `docs/data_sources/public_procurement_external_geography_2026/`
- `docs/data_sources/public_procurement_function_territory_2026/`
- `docs/data_sources/fundacao_ivan_goulart_payment_profile_2026/`
- `docs/data_sources/public_procurement_market_opportunity_20260919_v001.md`
- `docs/data_sources/sao_borja_public_accounts_timeseries_2019_2026/`

Matriz exploratória:
- `Fluxo_recursos_territorial`
- `Conversao_renda_benchmark`
- `Cenarios_retencao`
- `MIP_benchmark_retencao`
- `MIP_externos_insumos`
- `Conab_exposicao_agro`
- `Tese_conversao_territorial`
- `Modelo_conversao_territorial`
- `Compras_publicas_2026`
- `Mapa_variaveis_ativas`
- `Agenda_dados`
- `KPIs_monitoramento`
- `Delta_cadernos`

---

## 9. Instrução para o próximo chat

Continuar **exatamente** deste checkpoint.

Não recomeçar auditorias já fechadas.

Primeiras tarefas:
1. ler este checkpoint;
2. ler `Mapa_variaveis_ativas`;
3. ler `Agenda_dados`, `KPIs_monitoramento`, `Delta_cadernos`;
4. verificar branch `explore/receita-estadual-rs-market-intel-v1`;
5. manter PR #41 draft/open/no merge;
6. manter Caderno-Base v028 read-only;
7. avançar primeiro em:
   - série de contas públicas 2019–2026;
   - reconciliação RFB;
   - VAF/BET/Radar/SINAC;
   - depois pesquisa primária e B2B.

Nenhuma variável do `Mapa_variaveis_ativas` deve ser descartada sem registro explícito de motivo, fonte e decisão metodológica.
