# PE 39/2026 — oferta local e experiência B2G da Iluminar — v002

## 1. Objetivo

A v001 demonstrou que existe em São Borja ao menos um operador com oferta documental da família de condutores. Esta v002 testa dois gates adicionais:

1. **enquadramento empresarial/territorial em fonte governamental**;
2. **experiência observada de fornecimento ao setor público e participação em pregão eletrônico**.

O objetivo não é declarar a Iluminar competitiva no PE39. É reduzir a incerteza sobre se ela é apenas varejo B2C ou se possui histórico B2G observável.

## 2. Gate cadastral/territorial — evidência governamental

O Portal da Transparência do Governo Federal exibe para o CNPJ **09.674.510/0001-19**:

- razão social: Lopes & Gruendemann Comércio de Materiais Elétricos Ltda;
- nome fantasia: Iluminar Materiais Elétricos e Ferragens;
- condição: **MATRIZ**;
- município: **São Borja/RS**;
- CNAE: **47423 — Comércio varejista de material elétrico**;
- endereço: Rua Félix da Cunha, 246.

Fonte:
https://portaldatransparencia.gov.br/pessoa-juridica/09674510000119

### Consequência

Os gates `presença territorial`, `matriz local` e `compatibilidade de atividade principal com material elétrico` passam a ter suporte em fonte oficial federal.

### Controle

O projeto ainda deve fazer o relink com a **base canônica RFB 2026-08** antes de tratar essa validação como substituta do controle cadastral mensal do SBMI.

## 3. Experiência B2G municipal observada — 2025

A Prefeitura de São Borja publicou a **Dispensa de Licitação nº 85/2025**, com:

- contratada: Lopes e Gruendemann Comércio de Materiais Elétricos Ltda;
- CNPJ: 09.674.510/0001-19;
- objeto: aquisição de materiais elétricos para reforma da EMEFCM Duque de Caxias;
- valor: **R$ 30.485,60**.

Fonte municipal:
https://www.saoborja.rs.gov.br/index.php/vacinacao?start=994

O extrato de conta do FNDE/SIGEF registra, em **26/11/2025**, transferência enviada de **R$ 30.485,60** ao mesmo CNPJ.

Fonte:
https://www.fnde.gov.br/sigefweb/index.php/conta-corrente/extrato-conta-corrente-detalhamento/banco/001/agencia/0187/contacorrente/0000479357/cnpj/88489786000101/programa/CV/data/122017

### Interpretação

A coincidência de:
- CNPJ;
- valor;
- período;
- ente municipal/FNDE

é consistente com execução financeira da contratação publicada.

Assim, a empresa deixa de ser apenas **oferta local potencial** e passa a ter **experiência B2G municipal observada em materiais elétricos**.

### Limitação

A Dispensa 85/2025:
- não é pregão competitivo;
- não prova habilitação para PE39;
- não demonstra capacidade para os 18 itens prioritários;
- não mede escala comparável.

O valor de R$30.485,60 corresponde a apenas **5,72%** dos R$533.194,40 estimados nos 18 condutores prioritários. Essa razão é apenas comparação de magnitude; os objetos e mecanismos são diferentes.

## 4. Participação histórica em pregão eletrônico — 2022

O ranking oficial do **PE08/2022**, gerado pelo Portal de Compras Públicas e publicado pela Prefeitura, registra Lopes Gruendemann Comércio de Materiais Elétricos Ltda no **item 0006**, braço reto de 1m para iluminação pública.

Dados observados:
- quantidade do item: 310;
- valor de referência: R$32,40/un.;
- proposta da Iluminar: **R$32,00/un.**;
- menor proposta listada: **R$14,85/un.**.

Fonte:
https://www.saoborja.rs.gov.br/images/conteudo/Licitacoes/2022/Ranking_PE082022.pdf

### Cálculos descritivos

`gap_vs_menor = (32,00 - 14,85) / 14,85 × 100 = 115,49%`.

`dif_vs_referencia = (32,00 - 32,40) / 32,40 × 100 = -1,23%`.

Logo:
- a proposta local ficou **1,23% abaixo do valor de referência**;
- mas **115,49% acima da menor proposta listada**.

### Interpretação

Este é o primeiro exemplo documental direto no mecanismo estudado em que:

1. um fornecedor local efetivamente aparece em ranking de pregão eletrônico;
2. há ampla competição de fornecedores;
3. o preço local ficou próximo da referência administrativa;
4. ofertas concorrentes foram substancialmente menores.

Isso é compatível com a hipótese de **pressão de preço atacadista/inter-regional** em compras públicas.

### Controle decisivo

O item era um **braço metálico para iluminação pública**, não um condutor.

Portanto:
- não usar o gap de 115,49% como parâmetro de fios/cabos;
- não transportar preços de 2022 para 2026;
- não afirmar que a menor proposta listada foi necessariamente homologada sem documento final;
- não inferir que a empresa não seja competitiva em outros itens.

A evidência serve para demonstrar **participação histórica e mecanismo de pressão competitiva**, não o resultado do PE39.

## 5. Gate revisado

| Dimensão | Situação após v002 |
|---|---|
| Presença em São Borja | OFICIALMENTE OBSERVADA |
| Matriz local | OFICIALMENTE OBSERVADA no Portal da Transparência |
| CNAE material elétrico | OFICIALMENTE OBSERVADO |
| Família condutores | OBSERVADA no POM |
| Rede de abastecimento | OBSERVADA no POM |
| Fornecimento público de material elétrico | OBSERVADO — Dispensa 85/2025 |
| Pagamento público compatível | OBSERVADO — FNDE/SIGEF |
| Participação histórica em pregão eletrônico | OBSERVADA — PE08/2022 |
| Equivalência aos 18 condutores PE39 | PENDENTE |
| Escala/estoque para 48.540 m | PENDENTE |
| Prazo PE39 | PENDENTE |
| Habilitação PE39 | PENDENTE |
| Preço PE39 | PENDENTE |
| Participação PE39 | PENDENTE — resultado ainda não publicado segundo indexador secundário |

Classificação revisada:

**`LOCAL_OFFER_AND_B2G_EXPERIENCE_OBSERVED_CONTESTABILITY_OPEN`**

## 6. Diagnóstico

Duas explicações fortes deixam de ser adequadas:

- “o comércio local não trabalha com a família de produtos”;
- “o operador local não tem experiência alguma de fornecimento público”.

Ambas são contrariadas por evidência documental.

O problema analítico se estreita para:

> **equivalência técnica + escala/estoque + prazo + capital de giro + habilitação + preço competitivo.**

A evidência histórica de 2022 torna **preço** uma hipótese mais concreta, mas ainda não testada para condutores em 2026.

## 7. Próxima ação dirigida

A prioridade agora é mais estreita:

1. reconciliar o CNPJ com a base canônica RFB 2026-08;
2. obter edital/TR oficial do PE39 e fechar especificações dos 18 condutores;
3. testar catálogo/marca/certificação da Iluminar apenas nesses 18 itens;
4. testar quantidade disponível + lead time de reposição;
5. verificar requisitos de habilitação do PE39;
6. estimar preço entregue comparável somente quando houver especificação equivalente;
7. incorporar resultado do PE39 quando publicado.

Não é necessário abrir nova pesquisa genérica de “existência de fornecedores locais”.

## 8. Limitações

- Portal da Transparência não substitui o snapshot canônico RFB 2026-08;
- POM é de 2025;
- Dispensa 85/2025 demonstra execução pública, não competição em pregão;
- PE08/2022 demonstra participação histórica, mas em item diferente;
- comparação de magnitude R$30.485,60/R$533.194,40 não mede capacidade;
- nenhum resultado do PE39 foi inferido.

## 9. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
