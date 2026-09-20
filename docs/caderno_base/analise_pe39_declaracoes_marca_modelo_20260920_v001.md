# PE39/2026 — declarações de modelo/marca: participante local × vencedores — v001

**Data:** 20/09/2026  
**Escopo:** 18 itens prioritários / 9 clusters técnicos  
**Fonte:** Ata Final oficial do PE39/2026 — tabelas de propostas iniciais e classificação final  
**Unidade de análise:** `item × papel no resultado (LOCAL/WINNER) × declaração de Modelo + Marca/Fabricante`

## 1. Regra metodológica

A Ata Final apresenta as colunas `Modelo` e `Marca/Fabricante`, mas a extração textual do PDF não preserva uma fronteira estável entre elas.

Por isso, o projeto **não separa artificialmente** os dois campos.

O arquivo-base preserva:
- `declaracao_modelo_marca_raw`;
- valor unitário inicial;
- valor total inicial;
- status e posição final;
- valor final.

O campo bruto é evidência do que foi declarado na proposta, não verificação independente do fabricante, do produto efetivamente entregue ou do fornecedor upstream.

## 2. Completude

Foram reconciliadas:

- **18 declarações do participante local** — uma para cada item prioritário;
- **17 declarações dos arrematantes** — todos os itens aceitos;
- total: **35 linhas**;
- item 7 sem linha de vencedor porque fracassou.

A validação utiliza a mesma Ata Final cuja hash SHA-256 já foi canonizada no bloco oficial do PE39.

## 3. Concentração da declaração local

Em **15 das 18 propostas locais**, o campo bruto de Modelo + Marca/Fabricante contém a expressão **CORFIO**.

Fórmula:

`15 / 18 × 100 = 83,33%`.

As três exceções são:

- T05 / item 35 — `ELETROMAX ELETROMAX`;
- T05 / item 36 — `DEPECIL DECEPIL`;
- T06 / item 49 — `TRAMONTINA TRAMONTINA`.

Nos demais clusters T01, T02, T03, T04, T07, T08 e T09, a proposta local registra CORFIO em todos os itens.

### Significado permitido

**Dado observado:** a proposta do operador local é fortemente concentrada, no campo declarado, em uma mesma referência de marca/fabricante.

### O que não significa

Não é possível concluir:
- que a empresa compre diretamente da CORFIO;
- qual distribuidor/atacadista utiliza;
- que a marca determine o preço;
- que o produto declarado tenha sido tecnicamente validado em profundidade nas linhas não vencedoras;
- que CORFIO seja estruturalmente mais cara ou menos competitiva.

## 4. Declarações dos vencedores

Nas **17 linhas vencedoras**, nenhuma declaração bruta contém `CORFIO`.

Os campos vencedores observados são heterogêneos:

- **T02** — `CONTROLLER CONTROLLER`;
- **T03** — `SCREEN VISION SCREEN VISION`, `PLAY GO PLAY GO` e `CABO ENERGY`;
- **T04** — `ultraflex/sccable ultraflex/blucabos`;
- **T05** — `Cabo PP 4x10mm CONDUFAST` nas parcelas principal e reservada;
- **T06** — `PLUZIE PLUZIE`;
- **T07** — `AMPEX AMPEX` em dois itens e `19007 VIBRA` no terceiro;
- **T08** — `AMPEX AMPEX` nos três itens;
- **T09** — `MASTERPLUS/FCCABOSMASTERPLUS/FCCABOS`, `Cabo Flexível 25mm DeltaFlex` e, no item 86, o campo pouco informativo `39/2026 39/2026`.

A heterogeneidade dos vencedores indica que não há, no subconjunto analisado, uma única referência declarada de fabricante/modelo dominando todas as famílias técnicas.

## 5. O mesmo fornecedor vencedor pode operar com múltiplas referências

O maior vencedor em número de linhas, João Batista Sanches Silva e Cia Ltda., venceu 7 itens e apresentou referências declaradas diferentes conforme o cluster:

- T03: SCREEN VISION e PLAY GO;
- T07/T08: AMPEX.

**Interpretação:** amplitude competitiva não depende necessariamente de uma única marca declarada. Pelo menos um operador vencedor utiliza um portfólio multirreferência no certame.

Não é possível concluir, a partir disso, se há compra direta do fabricante, distribuição atacadista, estoque próprio ou triangulação comercial.

## 6. Relação com o diferencial de preço local

O bloco territorial anterior mostrou que, nas 15 linhas em que a proposta local permaneceu classificada, a mediana do diferencial frente ao vencedor foi **+92,79%**.

A nova evidência acrescenta que:
- o participante local registra CORFIO em **15/18** propostas;
- os vencedores registram outras referências em **17/17** linhas aceitas.

Isso cria uma **hipótese testável de cadeia de suprimento**:

> parte do diferencial de preço pode estar associada às marcas/rotas de abastecimento escolhidas e às condições comerciais de aquisição, e não apenas à localização geográfica do vendedor.

Essa hipótese **não está demonstrada**. Para testá-la, são necessários:
- fornecedor upstream efetivo;
- preço de aquisição;
- descontos comerciais;
- prazo;
- frete;
- crédito;
- lote mínimo;
- estoque;
- condições tributárias e comerciais.

## 7. Correção da leitura do catálogo Cigame

A relação histórica com a Cigame continua útil como uma rota documental de abastecimento possível, mas a proposta local do PE39 registra majoritariamente CORFIO.

Portanto:

- o match Cigame de 28,25% **não pode ser tratado como rota efetiva da proposta local**;
- mesmo quando a Cigame comercializa produto CORFIO em algum cluster, isso não prova que a proposta tenha sido formada por essa cadeia;
- o próximo teste deve partir das **referências efetivamente declaradas no certame**, e não de um fornecedor upstream escolhido ex ante.

Esse refinamento reduz o viés de disponibilidade que havia motivado a correção metodológica anterior.

## 8. Implicação por cluster

### T01 / T02

A proposta local declara CORFIO.  
T02 foi vencido por referência CONTROLLER.  
T01 fracassou.

### T03

Local: CORFIO nos três itens.  
Vencedores: SCREEN VISION, PLAY GO e ENERGY.

### T04

Local: CORFIO.  
Vencedor: referência Ultraflex/SCCable/Blucabos.

### T05

Local: ELETROMAX na parcela principal e DEPECIL/DECEPIL na reservada.  
Vencedor: CONDUFAST nas duas parcelas.

A cota reservada local foi desclassificada a pedido da empresa, portanto não usar o preço de R$ 3,90/m como comparação econômica válida.

### T06

Local: TRAMONTINA.  
Vencedor: PLUZIE.

### T07 / T08

Local: CORFIO em seis linhas.  
Vencedores: predominantemente AMPEX, com VIBRA em um item.

### T09

Local: CORFIO nas três linhas.  
Vencedores: MASTERPLUS/FCCABOS, DeltaFlex e um campo sem marca/modelo informativo suficiente no item 86.

## 9. Diagnóstico

**Dado observado:** a composição declarada da oferta local é muito mais concentrada em CORFIO do que a composição dos vencedores.

**Interpretação:** o próximo gargalo analítico deve migrar de “qual empresa local vende cabos?” para “qual arquitetura de abastecimento forma o preço das referências efetivamente ofertadas?”.

**Hipótese:** diferenças de rota de aquisição, volume, crédito e frete podem contribuir para o diferencial competitivo.

**Não concluir:** que a marca CORFIO seja causa do preço maior ou que trocar de marca resolveria a contestabilidade.

## 10. Próximo bloco dirigido

Prioridade:

1. mapear, em fonte oficial/institucional ou documental, os canais de distribuição das referências declaradas com maior recorrência;
2. começar por CORFIO, porque aparece em 15/18 propostas locais;
3. comparar com AMPEX, CONDUFAST, Controller e outras referências vencedoras apenas nos clusters em que são materialmente relevantes;
4. buscar evidência de distribuidores regionais, representantes, lead time e condições logísticas;
5. não inferir preço de aquisição sem documento;
6. manter fabricante/marca separado de distribuidor/fornecedor upstream.

## 11. Artefatos

- `docs/data_sources/public_procurement_pe39_product_declarations_20260920_v001/winner_local_product_declarations.csv`;
- `cluster_product_declarations.csv`;
- `summary.json`;
- `README.md`.

## 12. Governança

- branch: `explore/receita-estadual-rs-market-intel-v1`;
- Caderno-Base v028 permanece **read-only**;
- PR #41 permanece **aberto, draft e sem merge**.
