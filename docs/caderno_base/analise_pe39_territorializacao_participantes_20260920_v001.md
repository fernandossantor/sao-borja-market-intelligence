# PE39/2026 — territorialização dirigida dos participantes dos condutores — v001

**Data:** 20/09/2026  
**Escopo:** 18 itens prioritários de condutores / 9 clusters técnicos do PE39/2026  
**Abrangência geográfica:** São Borja/RS versus demais municípios/UFs  
**Fonte do universo de licitantes:** Ata Final oficial do PE39/2026  
**Fonte territorial substantiva:** Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08  
**Transporte da execução corrente:** espelho Casa dos Dados para todos os arquivos RFB, após indisponibilidade do host oficial na rotina automatizada  
**Status:** territorialização exploratória; não promover como classificação territorial definitiva até reconciliação oficial dos bytes RFB

## 1. Universo dirigido

A leitura das tabelas de propostas dos 18 itens prioritários identificou:

- **22 CNPJs únicos participantes**;
- **194 observações item × participante**;
- número de participantes por item entre **7 e 17**;
- média de **10,78 participantes por item**;
- mediana de **10 participantes por item**.

Cinco CNPJs aparecem nos 18 itens, incluindo o operador local já confirmado. Isso mostra que a participação integral da cesta não foi uma característica exclusiva de uma empresa.

## 2. Territorialização cadastral — execução corrente

A varredura RFB 2026-08 encontrou os 22 CNPJs exatos e todos com situação cadastral ativa (`02`).

Classificação obtida:

- **1 LOCAL_EXACT_ACTIVE** — São Borja/RS;
- **21 EXTERNAL_EXACT_ACTIVE_NO_LOCAL_FOOTPRINT**;
- **0 ROOT_WITH_LOCAL_ACTIVE_FOOTPRINT** entre os 21 CNPJs externos.

### Limitação de transporte

Os 11 arquivos utilizados (`Municipios.zip` + `Estabelecimentos0..9.zip`) foram obtidos, nesta execução, pelo espelho de transporte Casa dos Dados porque o host oficial da RFB não respondeu dentro dos limites operacionais.

A fonte substantiva permanece RFB 2026-08, mas esta territorialização deve permanecer **exploratória** até:
- reexecução integral pelo host oficial; ou
- reconciliação de hashes/bytes com a distribuição oficial.

A classificação do CNPJ local já possui confirmação independente no controle territorial do projeto e no Portal da Transparência federal, portanto a existência de **ao menos um participante local** não depende desta limitação.

## 3. Estrutura territorial preliminar dos 22 participantes

Na classificação exploratória:

- São Borja: 1/22 = **4,55%** dos CNPJs participantes;
- demais municípios do RS: 12/22 = **54,55%**;
- outras UFs: 9/22 = **40,91%**.

Entre os 21 CNPJs classificados como externos:
- 12 são do RS = **57,14%**;
- 9 são de outras UFs = **42,86%**.

Estados externos ao RS observados:
- SP;
- GO;
- MG;
- SC;
- RJ;
- MT;
- PR.

**Interpretação:** a contestação do PE39 não é apenas nacional/remota. A maior parte dos concorrentes externos ao município, na leitura preliminar, ainda está dentro do Rio Grande do Sul.

## 4. Intensidade da presença local no conjunto de propostas

O participante local confirmado aparece nos 18 itens.

Observações item × participante locais:

`18`.

Total de observações item × participante:

`194`.

Participação local nesse indicador de presença competitiva:

`18 / 194 × 100 = 9,28%`.

### Interpretação permitida

O indicador mede **presença em linhas disputadas**, não market share nem participação em valor.

Apesar de representar apenas 1 dos 22 CNPJs, o operador local participou de toda a cesta prioritária; portanto, o problema não é simples ausência de entrada no certame.

## 5. Resultado final e geografia — sensibilidade exploratória

A Ata Final possui 17 linhas com vencedor e uma fracassada.

O operador local confirmado não venceu nenhuma das 17 linhas.

A classificação RFB transportada por espelho atribui todos os CNPJs vencedores das 17 linhas ao grupo externo ao município. Como a territorialização dos demais participantes ainda depende de reconciliação oficial, a formulação segura para os cadernos permanece:

> há ao menos um participante local confirmado nas 18 linhas e nenhuma vitória desse operador; a hipótese de que todos os vencedores são externos é fortemente sustentada pela varredura cadastral corrente, mas deve aguardar reconciliação oficial da territorialização dos demais CNPJs antes de promoção factual.

## 6. Implicação para o mecanismo de contestabilidade

A sequência analítica fica mais precisa:

`entrada no certame → permanência/classificação → preço entregue → diligência/habilitação → vitória → contratação/ARP → empenho/pagamento`.

Para o operador local confirmado:
- entrada: observada em 18/18;
- permanência processual: 15/18;
- preço: principal barreira nas 15 linhas comparáveis;
- diligência/continuidade: duas falhas adicionais relevantes nos itens 36 e 41;
- vitória: 0/18.

Para o mercado territorial:
- não usar 1 operador como proxy;
- concluir a reconciliação oficial dos 21 demais CNPJs antes de medir taxa local de participantes/vencedores;
- depois comparar os operadores locais efetivos com rotas upstream, escala, frete e habilitação.

## 7. Tabela de participantes

Arquivo-base:
`docs/data_sources/public_procurement_pe39_participants_20260920_v001/priority_participants_rfb_202608.csv`.

Campos principais:
- CNPJ;
- nome do participante;
- número e lista de itens prioritários disputados;
- classe territorial;
- situação cadastral;
- UF;
- município TOM/nome;
- número de estabelecimentos ativos da mesma raiz em São Borja.

## 8. Fórmulas

Participação de CNPJs locais:

`1 / 22 × 100 = 4,55%`.

Participação dos demais municípios do RS:

`12 / 22 × 100 = 54,55%`.

Participação de outras UFs:

`9 / 22 × 100 = 40,91%`.

Presença local em observações item × participante:

`18 / 194 × 100 = 9,28%`.

## 9. Limitações

- localidade cadastral não mede origem física do produto;
- CNPJ local não prova estoque, capital, escala ou retenção econômica;
- CNPJ externo não implica vazamento integral;
- participação em item não significa proposta tecnicamente validada em profundidade;
- Ata Final não equivale a homologação, ARP, contratação ou pagamento;
- classificação 21 externos/1 local depende, para os 21 demais, da reconciliação do transporte RFB.

## 10. Próximo gate

1. reconciliar os 22 CNPJs contra fonte oficial RFB/Portal governamental;
2. somente depois calcular taxa territorial definitiva de participantes e vencedores;
3. para os participantes locais confirmados, cruzar item × marca/modelo × preço × fornecedor upstream;
4. testar escala/estoque, capital, frete e habilitação sem extrapolar de uma empresa para o mercado.

## 11. Governança

- branch: `explore/receita-estadual-rs-market-intel-v1`;
- Caderno-Base v028 permanece **read-only**;
- PR #41 permanece **aberto, draft e sem merge**.
