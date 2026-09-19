# Checkpoint — São Borja — Inteligência Mercadológica — etapa multissetorial e fechamento de rotas oficiais — 18/09/2026

## 1. Regras de preservação

- Branch exclusiva de trabalho: `explore/receita-estadual-rs-market-intel-v1`.
- Não alterar bases ou cadernos canônicos sem autorização explícita.
- Caderno-Base usado somente para leitura: `v028`, Drive ID `17Sk5Hu_CQ-hKJYTNEfYSN4F97MiuZrfrU9o_VxEg0Rc`.
- Documento-mestre da auditoria: `1cQ_y3H0drdPBEv8TfKjTfze5sEux77YpiNG89zous4U`.
- Matriz exploratória: `1_y29fNqP8i_FyM4gWJIo7fy_Ef9dcuLZbHHV4IZy9jU`.
- PR #41 deve permanecer aberto, draft e sem merge.
- Toda evidência desta etapa permanece **exploratória / não canônica** até promoção explícita.

## 2. Arquitetura analítica corrente

A análise opera em três níveis:

1. `território/circuitos`;
2. `setores/cadeias`;
3. `produtos/NCMs`.

O arroz permanece somente como primeiro teste técnico em algumas rotas de produto. Não é mais o centro da análise.

## 3. Estado da branch no fechamento

Head imediatamente anterior a este checkpoint:

`f073e5d78e28b1749bb4be8a28cb73c5401988b7`

Commit: `data: extract Comex municipal 2026 for São Borja`.

Desde a criação do workflow SINAC/SIMEI, a branch avançou automaticamente com rotas Cadastur, SINAC/SIMEI e Comex Stat. Houve concorrência entre pushes de workflows; isso gerou rejeições por non-fast-forward em alguns jobs, mas os resultados de consulta ficaram preservados em logs/artifacts.

## 4. Rotas oficiais — estado atualizado

### 4.1 SINAC / SIMEI — Receita Federal

**Fonte primária:** Estatísticas do Simples Nacional.

**Posição de referência:** 12/09/2026.

Última execução reprodutível do workflow:
- run: `35407048863`;
- consulta municipal: HTTP 200;
- filtro: RS → São Borja;
- valor SINAC / optantes do Simples: **7.176**;
- valor SIMEI / optantes: **4.883**;
- soma por CNAE SINAC: **7.176**;
- soma por CNAE SIMEI: **4.883**;
- conciliação total × CNAE: **PASS** para ambos.

Natureza:
- valores exibidos pela consulta oficial: **DADO OBSERVADO**;
- somas por CNAE e reconciliação: **DADO CALCULADO**.

Controle:
- o antigo cross-check secundário de 3.829 MEI **não deve ser usado como substituto**;
- 4.883 optantes SIMEI em 12/09/2026 não deve ser comparado diretamente com o snapshot secundário 2026-08 sem alinhar data, conceito e universo;
- 7.176 optantes SINAC não é sinônimo de 7.306 estabelecimentos ativos RFB/CNPJ 2026-08.

Problema operacional residual:
- o job conseguiu gerar `sao_borja_totals.csv` e `sao_borja_cnae.csv`, mas o push final foi rejeitado por non-fast-forward porque a branch recebeu commits concorrentes;
- artifact preservado por 30 dias: ID `10573251037`;
- primeira ação na retomada: persistir esse artifact/resultado completo na branch e sincronizar documento-mestre e matriz exploratória.

### 4.2 Cadastur — 2º trimestre de 2026

Workflow de auditoria de todas as categorias:
- run disparado a partir de `751dfbed761ea86bc6ad6aa45194fe16c9c33320`;
- resultado persistido no commit `bfb948f21e92750914e236916d1e9339d5e7f4ff`;
- 15 conjuntos/pacotes descobertos;
- 13 recursos identificados para 2T2026;
- 5 categorias com registros de São Borja;
- 21 linhas municipais no conjunto das categorias;
- 0 falhas de download/processamento.

Categorias com registros:
- Meios de Hospedagem: **2**;
- Agências de Turismo: **7**;
- Guia de Turismo: **6**;
- Transportadora Turística: **5**;
- Organizador de Eventos: **1**.

Resultados anteriores preservados:
- Meios de Hospedagem Regular/Operação: 2;
- 90 UHs;
- 180 leitos;
- Agências: 7 registros, sendo 6 Regular/Operação e 1 Em Implantação.

Controle:
- as 21 linhas **não representam necessariamente 21 empresas únicas**;
- categorias possuem regras de obrigatoriedade/cobertura distintas;
- Cadastur não mede demanda, ocupação, gasto, pernoite ou market share;
- não comparar diretamente com RFB/CNAE como taxa de cobertura.

### 4.3 ANP — vendas municipais e revendedores

Rota municipal permanece fechada de forma exploratória.

Vendas 2024 em São Borja:
- Gasolina C: **15.929.410 L**;
- Etanol hidratado: **592.100 L**;
- Óleo diesel: **49.501.472 L**;
- GLP P13: **1.124.934 kg**;
- GLP OUTROS: **210.685 kg**.

Revendedores em operação em 18/09/2026:
- total: **10**;
- VIBRA: 3;
- Bandeira Branca: 3;
- IPIRANGA: 2;
- SANTA LUCIA: 1;
- RAIZEN: 1.

Controle:
- vendas de combustíveis são proxy complementar de abastecimento/mobilidade;
- não identificam residente, visitante, transportador ou turista;
- contagem por bandeira não é market share.

### 4.4 Comex Stat municipal — MDIC/SECEX

A limitação de download por CSV/host foi superada por uso da **API oficial do Comex Stat, endpoint /cities**.

Commit de persistência:
`f073e5d78e28b1749bb4be8a28cb73c5401988b7`.

Recorte:
- São Borja/RS;
- código municipal 4318002;
- janeiro a agosto de 2026;
- detalhe por mês, país e SH4;
- métricas: US$ FOB e kg líquido.

Linhas observadas na API:
- exportação: 18;
- importação: 15.

Agregados YTD calculados:
- exportações: **US$ 9.848.096 FOB** e **32.151.627 kg**;
- importações: **US$ 6.514.628 FOB** e **17.497.000 kg**.

Teste SH4 1006 — arroz:
- exportações: Estados Unidos, Nicarágua e Cuba;
- importações: Uruguai, Argentina e Paraguai.

Controle:
- o município do módulo municipal representa **domicílio fiscal da empresa declarante**;
- não representa origem física da mercadoria;
- SH4 não deve ser convertido automaticamente em NCM8;
- 2026 é ano parcial até agosto;
- totais YTD são cálculos sobre respostas oficiais, não valores canônicos.

### 4.5 Radar de Mercado — Dados Abertos

Workflow `radar-open-data-discovery` executado com sucesso técnico em 18/09/2026.

Resultado:
- página carregada;
- 22 respostas de rede selecionadas;
- clique em “Dados Abertos”: **False**;
- downloads capturados: **0**;
- elementos candidatos: **0**.

Conclusão:
- a rota continua **aberta**;
- o pipeline genérico `radar_open_data.py` e a CLI estão preparados;
- ainda faltam os CSVs reais;
- não preencher INT/OUF/EXT, Part.RS, dependência ou market share sem os bytes oficiais.

### 4.6 BET municipal

Estado inalterado:
- granularidade municipal confirmada;
- edições correntes identificadas;
- valores recentes específicos de São Borja ainda não materializados de forma reproduzível.

Regra:
- não inferir São Borja a partir da Fronteira Oeste;
- ausência em tabela exibida não equivale a zero.

## 5. Rotas agora fechadas ou substancialmente fechadas

Fechadas/substancialmente fechadas em camada exploratória:
- ANP — vendas municipais;
- ANP — revendedores;
- Cadastur — recursos 2T2026, incluindo auditoria multcategoria;
- Comex Stat municipal — API oficial jan–ago/2026;
- SINAC/SIMEI — consulta municipal e CNAE reproduzidas, faltando apenas persistir integralmente o último artifact na branch/matriz/Docs.

Ainda abertas:
- Radar Dados Abertos — obtenção dos CSVs reais;
- BET municipal corrente;
- persistência/sincronização final do resultado SINAC/SIMEI;
- eventual conciliação SINAC/SIMEI com CNPJ da mesma competência.

## 6. Grandes lacunas que permanecem não resolvíveis por proxy

Não transformar as rotas secundárias em substitutos para:
- destino monetário do gasto;
- origem do cliente associada ao ticket;
- market share;
- compras B2B privadas;
- conversão digital;
- lucros/reinvestimento local.

Para fechamento dessas perguntas são necessários dados primários e/ou empresariais.

## 7. Próxima ordem de trabalho recomendada

1. Persistir o artifact SINAC/SIMEI do run `35407048863` na branch sem perda por concorrência; registrar 7.176 / 4.883 e a decomposição completa por CNAE na matriz exploratória e no documento-mestre.
2. Atualizar `Simples_SIMEI`, `Rotas_secundarias` e `Agenda_dados` de “pendente” para “extraído/reproduzido”, mantendo natureza exploratória.
3. Integrar na matriz/documento-mestre o fechamento multcategoria do Cadastur.
4. Integrar o Comex Stat municipal via API como rota fechada, preservando domicílio fiscal e ano parcial.
5. Retomar Radar: inspecionar as 22 respostas de rede já preservadas e buscar a origem efetiva dos CSVs; depois executar o pipeline multissetorial.
6. Retomar BET municipal.
7. Somente após esses fechamentos decidir se alguma evidência deve ser promovida ao Caderno-Base ou aos cadernos setoriais.

## 8. Instrução de retomada

Retomar exclusivamente na branch `explore/receita-estadual-rs-market-intel-v1`.

Antes de qualquer nova alteração:
- conferir o head da branch;
- ler este checkpoint;
- ler o documento-mestre e a matriz exploratória;
- verificar se algum workflow concorrente avançou a branch;
- preservar o PR #41 aberto/draft/sem merge;
- não alterar bases/cadernos canônicos;
- classificar qualquer novo dado como exploratório até promoção explícita.
