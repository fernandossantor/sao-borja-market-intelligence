# Análise dirigida — PE 39/2026 — resultado oficial e contestabilidade B2G territorial — v001

**Data:** 20/09/2026  
**Escopo:** materiais elétricos / 18 condutores prioritários / 9 clusters técnicos  
**Fonte primária:** PNCP + Ata Final oficial de 25/08/2026  
**Status:** evidência madura para correção factual; diagnóstico territorial ainda parcial até territorialização completa dos participantes.

## 1. O que mudou

A principal mudança desta etapa não é a descoberta de uma empresa, mas a mudança de estado do mecanismo analisado.

Antes, havia:
- oferta local observável;
- experiência B2G local em casos documentais;
- especificações reconstruídas por espelho secundário;
- participação no PE39 indeterminada.

Agora há:
- resultado documental oficial da sessão;
- especificações prioritárias confirmadas por fonte oficial;
- arquitetura principal/reservada 75%/25% confirmada no T05;
- **participação efetiva de operador local comprovada em todos os nove clusters**;
- resultados de preço e causas de desclassificação observáveis.

A unidade analítica permanece:
`objeto/grupo de produto × oferta local × participação × escala × habilitação × preço/frete/logística`.

## 2. Correção documental do PE39

O PNCP passou a disponibilizar em 25/08/2026:
- Ata Final;
- Ata Parcial.

Portanto, a expressão anterior “resultado ainda não publicado segundo indexador secundário” não deve ser promovida aos cadernos.

A correção adequada é:

> o resultado documental da sessão está publicado no PNCP oficial; porém o resultado estruturado/homologado continua não preenchido no endpoint consultado (`existeResultado=false`, `valorTotalHomologado=null`, endpoints de resultado dos itens prioritários com HTTP 204).

Essa diferença é metodologicamente importante porque impede confundir:
`ata da sessão → homologação → ARP/contrato → empenho → pagamento`.

## 3. Validação dos nove clusters

As 18 linhas prioritárias foram reconciliadas com o PNCP/Ata Final. As descrições básicas utilizadas na normalização T01–T09 permanecem válidas.

O desenho T05 foi resolvido:
- item 35: 2.115 m, sem benefício;
- item 36: 705 m, participação exclusiva ME/EPP;
- total: 2.820 m;
- repartição: 75% / 25%.

A Ata denomina o item 36 como **cota reservada** e registra a regra de equalização entre cota principal e reservada quando vencidas pelo mesmo fornecedor.

A antiga hipótese pode, portanto, ser substituída por **dado observado**.

## 4. Resultado do subconjunto prioritário

### Dados observados

- 18 linhas;
- 17 aceitas;
- item 7 fracassado;
- referência total das 18 linhas: R$ 533.194,40;
- referência das 17 linhas aceitas: R$ 506.986,40;
- valores documentais vencedores nas 17 aceitas: R$ 376.591,40.

### Dados calculados

Taxa de aceitação por linha:

`17 / 18 × 100 = 94,44%`.

Diferença entre referência e valores vencedores no mesmo subconjunto:

`R$ 506.986,40 - R$ 376.591,40 = R$ 130.395,00`.

Diferença relativa:

`R$ 130.395,00 / R$ 506.986,40 × 100 = 25,72%`.

### Interpretação

A competição documental produziu valores aceitos substancialmente abaixo das referências no subconjunto de condutores concluído.

### Limitação

Não denominar R$ 130.395,00 de “economia realizada”. O dado não é pagamento nem contrato executado e a estrutura do PNCP ainda não registra homologação.

## 5. Contestação local efetiva

A Ata Final revelou participação de **COMERCIAL DE TINTAS SANTO ANTONIO LTDA — CNPJ 28.927.340/0001-81**.

O controle territorial já existente no projeto classifica esse CNPJ como `LOCAL_EXACT_ACTIVE`, São Borja/RS.

A empresa apresentou proposta nas 18 linhas prioritárias, cobrindo os nove clusters.

Esse dado resolve uma parte importante do problema:

> a participação local no subconjunto prioritário não é mais hipótese; é observada.

Contudo, participação não equivale a vitória, capacidade integral de fornecimento ou competitividade.

### Resultado observado do operador local nas 18 linhas

- 18 participações;
- 15 classificações finais;
- 3 desclassificações;
- 0 vitórias finais no subconjunto.

Desclassificações:
- item 7 — valor acima da referência;
- item 36 — a pedido da empresa;
- item 41 — não apresentou documento solicitado.

## 6. Preço como gate competitivo

Nas 15 linhas em que o operador local permaneceu classificado:

- total final local: R$ 732.334,40;
- total dos vencedores nas mesmas linhas: R$ 325.418,60;
- diferença: R$ 406.915,80.

Fórmula:

`(732.334,40 - 325.418,60) / 325.418,60 × 100 = 125,04%`.

### Interpretação

No conjunto comparável, a proposta final local ficou 125,04% acima dos vencedores em termos ponderados.

Isso sustenta uma interpretação **mecânica**, não estrutural:

> a presença territorial e a participação efetiva não bastaram para converter a oferta local em vitória; na maior parte das linhas válidas observadas, o preço foi uma barreira competitiva importante.

### Exceções instrutivas

Os itens 36 e 41 mostram o mecanismo inverso.

Em ambos houve preço local muito baixo em algum momento, mas não conversão em resultado:
- item 36: retirada/desclassificação a pedido da empresa;
- item 41: falha documental.

Assim, a contestabilidade B2G depende de múltiplos gates, e não apenas de preço.

## 7. Correção do universo de operadores

O inventário prévio de operadores locais deve ser preservado, mas não pode definir sozinho o universo analítico.

O PE39 demonstra que o método correto é combinar:

`inventário territorial ex ante + participantes efetivos do certame ex post`.

Isso evita dois erros:
1. viés de disponibilidade, quando se privilegia a empresa sobre a qual há mais documentação;
2. viés de inventário, quando operadores reais do certame ficam fora porque não estavam na lista inicial.

A Comercial de Tintas Santo Antonio entra na matriz não como “novo caso central”, mas porque é **participante efetivo territorialmente confirmado**.

## 8. O que ainda não é possível concluir

Ainda não é possível medir:
- número total de participantes locais entre todos os licitantes do subconjunto;
- taxa local de vitória do PE39 como um todo;
- diferencial médio local versus externo do universo de concorrentes;
- capacidade de estoque e escala dos demais operadores locais;
- preço entregue com decomposição de frete;
- taxa de conversão entre participação, adjudicação/homologação, ARP, empenho e pagamento.

O fato de um operador local ter ofertado os nove clusters não prova que todos os demais operadores locais possam fazê-lo.

## 9. Implicação para os cadernos

### Correção factual

Substituir:
> resultado do PE39 ainda não publicado.

Por:
> Ata Final e Ata Parcial publicadas no PNCP em 25/08/2026; resultado estruturado/homologação ainda não preenchido na API consultada.

### Aprofundamento analítico

Substituir:
> participação local indeterminada.

Por:
> há participação local efetivamente observada nos nove clusters prioritários por pelo menos um operador confirmado de São Borja; essa participação não se converteu em vitória final nas 18 linhas analisadas.

### Diagnóstico

A leitura passa de **“oferta local existente, contestabilidade desconhecida”** para:

> **contestabilidade formal local demonstrada, mas conversão competitiva baixa no subconjunto observado**, com predominância de diferencial de preço e ocorrência de barreiras documentais/decisórias.

A formulação deve continuar provisória até a territorialização dos demais participantes.

## 10. Próximo bloco dirigido

Prioridade imediata:

`participante efetivo → CNPJ → município/UF → cluster/item → posição/preço → classificação/desclassificação`.

Somente depois disso retornar a:
`estoque/escala → prazo/logística → upstream → habilitação aprofundada`.

Isso mantém a análise centrada no mecanismo territorial e não em empresas individuais.

## 11. Artefatos de suporte

- `docs/data_sources/public_procurement_pe39_official_20260920_v001/README.md`;
- `docs/data_sources/public_procurement_pe39_official_20260920_v001/priority_conductors_result.csv`;
- `docs/caderno_base/correcao_metodologica_pe39_contestabilidade_operadores_20260920_v001.md`;
- workflows oficiais de auditoria PNCP registrados em `.github/workflows/`.

## 12. Governança

- branch: `explore/receita-estadual-rs-market-intel-v1`;
- Caderno-Base v028 permanece **read-only**;
- PR #41 permanece **aberto, draft e sem merge**;
- a presente nota é delta analítico e não altera retroativamente o v028.
