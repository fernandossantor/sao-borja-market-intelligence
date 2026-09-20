# Farmácia Básica — contestabilidade B2G documental — São Borja — 2026 — v002

## 1. Escopo desta versão

Esta versão complementa a v001 e não a substitui. O objetivo é transformar a frente Farmácia Básica em um teste documental de **contestabilidade B2G**, sem ampliar coleta de forma indiscriminada e sem tratar ausência de pagamento local como "vazamento".

Unidade analítica:

`item de medicamento → participantes/propostas → vencedor/segundo colocado → requisitos → preço/escala/logística → geografia do fornecedor`.

## 2. Evidência observada já consolidada

Na ação **Farmácia Básica e Demandas Judiciais**, rubrica **Material, Bem ou Serviço para Distribuição Gratuita**, no período 01/01/2026–19/09/2026:

- valor pago: **R$ 964.631,84**;
- credores sem footprint ativo local: **30**;
- credores com presença local: **0**;
- participação cadastral externa na primeira rodada: **100%**.

O inventário setorial auditado registra **20 CNPJs únicos de farmácias/drogarias**, organizados em **7 raízes CNPJ**, com **85% das unidades catalogadas vinculadas a raízes multiunidade**.

Esses dois conjuntos não são diretamente equivalentes. O primeiro mede credores pagos pelo Município na rubrica analisada; o segundo descreve oferta varejista local catalogada. A coexistência de varejo local e pagamento B2G externo é o problema a explicar, não uma prova de capacidade substitutiva.

## 3. Desenho oficial do processo 34/2026

A publicação oficial do Município de São Borja informa para o **Pregão Eletrônico 34/2026/DCL/SMPOP**:

- objeto: registro de preços para aquisição de medicamentos destinados aos usuários do SUS;
- destino: Farmácias Básicas, Unidades de Saúde e SAMU;
- critério: **menor preço por item**;
- modo de disputa: **aberto**;
- sessão: **16/06/2026 às 8h30**;
- plataforma: Portal de Compras Públicas.

Fonte oficial municipal:
https://saoborja.rs.gov.br/index.php/licitacoes-e-contratos/item/6765-pregao-eletronico-34-2026-dcl-smpop

O aviso também foi publicado no Diário Oficial dos Municípios do Estado do Rio Grande do Sul em 02/06/2026.

### Implicação metodológica

Como a disputa é por item, a hipótese de que a ausência de fornecedor local decorra simplesmente de um lote global indivisível **não é suficiente** para explicar o resultado. Permanecem abertas hipóteses de preço, atacado, escala, capital de giro, mix, habilitação, logística, política de redes e custo de participação.

Nenhuma dessas hipóteses é promovida como causa nesta versão.

## 4. Rota pública estruturada para auditoria

O Manual de Integração do PNCP documenta rotas públicas de consulta que permitem reconstruir a contratação em camadas:

1. contratação:
   `/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}`;
2. itens:
   `/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens`;
3. resultado por item:
   `/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/itens/{numeroItem}/resultados`;
4. histórico:
   `/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/historico`;
5. atas de registro de preços:
   `/v1/orgaos/{cnpj}/compras/{ano}/{sequencial}/atas`;
6. contratos/empenhos associados:
   `/v1/orgaos/{cnpj}/contratos/contratacao/{ano}/{sequencial}`.

Fonte técnica oficial:
Manual de Integração do PNCP, versão corrente consultada em 20/09/2026.

## 5. Identificador PNCP — controle de evidência

Indexadores públicos que reproduzem metadados do PNCP associam o Pregão 34/2026 ao controle:

`88489786000101-1-000109/2026`

e ao valor estimado de **R$ 1.671.770,00**.

Esses dois campos permanecem classificados nesta versão como **metadados indexados por fonte secundária, ainda não promovidos a dado canônico**, porque a consulta direta do registro oficial do PNCP não foi concluída no ambiente desta rodada.

Consequentemente:

- CNPJ do órgão: `88489786000101`;
- ano candidato: `2026`;
- sequencial candidato: `109`.

Esses parâmetros podem ser usados para a próxima tentativa de extração, mas devem ser reconfirmados no PNCP antes de alimentar cálculo ou tabela canônica.

## 6. Matriz mínima para medir contestabilidade

A auditoria documental do processo deve gerar uma linha por item × participante, contendo no mínimo:

| Campo | Uso analítico |
|---|---|
| numero_item | chave do medicamento |
| descricao_item | identificação do produto/apresentação |
| quantidade_estimada | escala potencial |
| valor_unitario_estimado | referência pré-disputa |
| cnpj_participante | identificação do ofertante |
| municipio_uf_participante | geografia |
| proposta_inicial | ponto de entrada |
| proposta_final | preço após disputa |
| classificacao_final | posição |
| vencedor | indicador |
| segundo_colocado | referência competitiva |
| diferenca_pct_vencedor_segundo | intensidade de preço |
| situacao_item | homologado/deserto/fracassado |
| motivo_desclassificacao | barreira observada |
| prazo_entrega | exigência logística |
| habilitacao_especifica | barreira documental/sanitária |
| local_no_inventario | cruzamento com oferta local |
| raiz_cnpj_local | controle de redes/multiunidade |

Fórmula para itens com vencedor e segundo colocado válidos:

`gap_preco_pct = (preco_segundo - preco_vencedor) / preco_vencedor × 100`.

O gap é descritivo. Não prova que um fornecedor local conseguiria praticar o mesmo preço.

## 7. Testes documentais prioritários

### T1 — participação local

Pergunta: algum dos CNPJs/raízes do inventário local apresentou proposta?

Resultado possível:
- sim → medir em quais itens e posições;
- não → registrar ausência de participação, sem inferir motivo.

### T2 — competitividade de preço

Pergunta: quando houver participante local, qual a distância entre sua melhor proposta e o vencedor?

Medida:
- diferença absoluta;
- diferença percentual;
- distribuição por item.

### T3 — habilitação/desclassificação

Pergunta: fornecedores locais foram eliminados por requisito documental, sanitário, técnico ou operacional?

Somente decisões/atas explícitas podem sustentar esta conclusão.

### T4 — escala e mix

Pergunta: os itens disputados pertencem ao mix varejista corrente ou exigem apresentações/volumes pouco compatíveis com a operação local?

A classificação deve ser feita item a item; não pode ser inferida apenas pela denominação "medicamentos".

### T5 — logística

Pergunta: prazo, frequência e condições de entrega criam requisito material de estoque/distribuição?

Depende do edital/termo de referência e deve ser comparado com capacidade observável dos participantes.

## 8. Regra de decisão

A contestabilidade local só será classificada quando houver evidência suficiente em pelo menos quatro dimensões:

`oferta local + participação efetiva + preço + requisito de escala/habilitação/logística`.

Categorias provisórias:

- **contestabilidade observada**: fornecedor local participa e é competitivo em pelo menos parte dos itens;
- **contestabilidade limitada observada**: há participação local, mas barreira explícita de preço/requisito/escala aparece nos documentos;
- **não participação observada**: nenhum operador local participa, sem causa inferida;
- **não mensurável**: documentação de participantes/propostas insuficiente.

## 9. O que não concluir

Com a evidência atual, não é possível afirmar:

- que as farmácias locais não têm capacidade de fornecer ao Município;
- que elas não participam de licitações;
- que o preço local é necessariamente maior;
- que a compra externa representa vazamento econômico integral;
- que o valor estimado do pregão é market size capturável;
- que os 30 credores pagos correspondem aos participantes ou vencedores do PE 34/2026.

## 10. Próxima ação

Prioridade imediata: recuperar de forma reproduzível os **itens, resultados, atas e documentos de classificação/habilitação** do PE 34/2026, preferencialmente pelo PNCP/Portal de Compras Públicas.

A pesquisa primária fica fora do caminho crítico nesta fase. Entrevistas com operadores somente devem ser consideradas posteriormente, se a auditoria documental deixar uma hipótese causal relevante sem resposta e houver decisão explícita de abrir pesquisa primária.

## 11. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- esta análise pertence à branch `explore/receita-estadual-rs-market-intel-v1`;
- a v001 permanece preservada;
- metadados de fonte secundária não são promovidos sem reconfirmação oficial.
