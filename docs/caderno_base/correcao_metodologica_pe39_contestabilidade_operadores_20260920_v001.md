# PE 39/2026 — correção metodológica e matriz territorial de operadores — v001

**Data:** 20/09/2026  
**Status:** correção metodológica / camada exploratória  
**Unidade analítica:** `objeto/grupo de produto × oferta local × participação em licitações × escala × habilitação × preço/frete/logística`

## 1. Motivo da correção

As análises anteriores do PE39 usaram a Iluminar como o caso documental mais completo disponível para testar mecanismos de oferta local, experiência B2G e acesso upstream.

Essa escolha foi útil como **teste de mecanismo**, mas não deve converter a empresa em unidade analítica principal nem permitir que a maior disponibilidade documental produza viés de disponibilidade.

A partir desta versão, a leitura territorial é explicitamente **operador-neutra**.

## 2. Reclassificação das evidências anteriores

### 42.78 / oferta local

A evidência acumulada permite rejeitar apenas a formulação extrema:

> “não existe oferta local observável da família de materiais elétricos/condutores”.

Ela **não permite** afirmar:
- que a cesta do PE39 seja localmente contestável;
- que exista equivalência técnica aos nove clusters;
- que a escala requerida esteja disponível;
- que os operadores locais tenham habilitação, estoque, capital de giro ou preço competitivo.

### 42.79 / experiência B2G

A experiência documentada da Iluminar permanece válida como **caso observacional individual**:
- fornecimento público municipal em materiais elétricos;
- pagamento compatível;
- participação histórica em pregão eletrônico.

Ela não é uma medida da experiência B2G do conjunto dos operadores locais.

### 42.81 / catálogo upstream Cigame

Os matches T01, T07 e T09, somando R$150.633,00 ou 28,25% do valor estimado dos condutores prioritários, permanecem válidos somente como **cobertura documental do catálogo de um fornecedor upstream observado em uma relação histórica específica**.

Esse percentual não pode ser reinterpretado como:
- participação local potencial;
- cobertura da oferta de São Borja;
- estoque local;
- capacidade de escala;
- acesso de todos os operadores à Cigame;
- competitividade de preço.

## 3. Universo territorial de operadores a testar

### Operadores presentes no inventário corrente

1. Iluminar Materiais Elétricos e Ferragens;
2. Mercado JL;
3. Comercial Loss;
4. Steelpet;
5. Agropecuária Vieira;
6. Agropecuária Centauro.

### Leads históricos ainda a reconciliar

7. Guasso Ferragens;
8. Comercial Passo;
9. Marta Ferragem;
10. Casa do Led / Ferragem Bueno.

A inclusão no universo de teste não implica compatibilidade técnica, capacidade ou habilitação.

## 4. Gate único e simétrico

Todos os operadores devem passar pela mesma sequência:

`produto equivalente → escala/estoque → prazo/logística → habilitação → preço entregue → participação`

Regras:

1. **Produto equivalente** é o primeiro gate substantivo. CNAE, ferragens genéricas ou presença em inventário não bastam.
2. **Escala/estoque** só é testada depois de equivalência técnica documental.
3. **Prazo/logística** deve considerar o prazo do instrumento oficial e a reposição efetiva do operador.
4. **Habilitação** é requisito próprio e não pode ser inferido de experiência B2G anterior.
5. **Preço entregue** deve incorporar frete/logística e comparar apenas objetos tecnicamente equivalentes.
6. **Participação** deve ser observada no processo; ausência de resultado publicado não autoriza inferência de ausência de participação.

## 5. Matriz de estados permitidos

Para evitar assimetria documental, cada célula deve assumir um dos estados:

- `OBSERVED`: evidência documental direta;
- `POTENTIAL_CADASTRAL`: compatibilidade apenas cadastral;
- `NOT_DEMONSTRATED`: busca realizada sem demonstração suficiente;
- `NOT_TESTED`: gate ainda não testado;
- `PENDING_OFFICIAL_TR`: depende do edital/TR oficial;
- `HISTORICAL_LEAD`: operador citado historicamente, situação corrente não reconciliada;
- `BLOCKED_MISMATCH`: incompatibilidade técnica documentada;
- `INDETERMINATE`: evidência insuficiente para classificação.

`NOT_DEMONSTRATED` nunca significa ausência.

## 6. Implicação para os nove clusters

Até a reconciliação do edital/TR oficial:

- T01–T09 continuam sendo **especificações de trabalho derivadas de espelho secundário**;
- T04 e T05 permanecem bloqueados nos matches Cigame já identificados por mismatch de tensão/construção;
- T06 permanece dependente da arquitetura oficial;
- T03 e T08 permanecem parciais;
- T01, T07 e T09 têm match upstream forte, mas nenhum operador local recebe por isso o status de produto equivalente.

O split 75%/25% dos itens 35/36 permanece apenas hipótese de cota principal/reservada.

## 7. Diagnóstico territorial corrigido

**Dado observado:** há evidência de presença local de operadores relacionados a materiais elétricos/ferragens e, em pelo menos um caso, de família de condutores, cadeia upstream e experiência B2G.

**Interpretação:** isso demonstra que a hipótese de ausência absoluta de oferta local é excessiva.

**O que não é possível concluir:** não há base suficiente para medir contestabilidade territorial efetiva do PE39, porque equivalência técnica, escala, prazo, habilitação, preço entregue e participação continuam incompletos.

**Próximo gargalo:** edital/TR oficial + matriz simétrica por operador e cluster.

## 8. Efeito sobre os cadernos

Esta correção deve entrar no `Delta_cadernos` como revisão de interpretação:

- substituir qualquer formulação centrada em empresa por leitura de mecanismo territorial;
- preservar casos empresariais apenas como evidência documental;
- não transformar cobertura upstream de um caso em atributo do mercado local;
- manter separados oferta observada, oferta potencial cadastral, equivalência, escala, experiência B2G, participação, preço e habilitação.

O Caderno-Base v028 permanece intacto.

## 9. Próxima ação dirigida

1. materializar/reconciliar edital e TR oficial do PE39;
2. confirmar as nove especificações e o desenho dos itens 35/36;
3. aplicar o gate de produto equivalente a todos os operadores candidatos;
4. avançar aos gates posteriores somente nas combinações operador × cluster aprovadas;
5. registrar cada conclusão madura no delta editorial;
6. somente depois sintetizar contestabilidade por cluster e para a cesta.

## 10. Governança

- branch: `explore/receita-estadual-rs-market-intel-v1`;
- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- análises anteriores não são apagadas: são preservadas como trilha de auditoria e reclassificadas por esta correção.
