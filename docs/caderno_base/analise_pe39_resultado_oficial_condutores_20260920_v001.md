# PE39/2026 — resultado oficial, cota ME/EPP e contestabilidade local dos condutores — v001

**Data:** 20/09/2026  
**Fonte primária:** PNCP / documentos oficiais do PE39/2026, incluindo Edital e Anexos, Termo de Referência e Ata Final publicada em 25/08/2026  
**Processo:** Pregão Eletrônico 39/2026 — Processo 14698/2026 — controle PNCP 88489786000101-1-000136/2026  
**Objeto:** registro de preços para materiais elétricos destinados à iluminação pública e infraestrutura elétrica dos prédios públicos de São Borja  
**Valor total estimado:** R$ 1.074.671,14

## 1. Correção de fonte

A informação anterior de que o resultado do PE39 ainda não estava publicado, baseada em indexador secundário, está superada.

O PNCP possui, como documento oficial anexado ao processo:
- `Ata_Final_144426_250826.zip`, publicada em 25/08/2026;
- a Ata Final contém a relação de vencedores, propostas, classificação, desclassificações e chat do processo.

Há uma assimetria de publicação: no endpoint estruturado do PNCP, a compra ainda aparece com `existeResultado=false` e os endpoints de `/resultados` dos itens prioritários retornam 204; entretanto, o documento oficial anexado ao mesmo processo contém o resultado do certame.

**Implicação metodológica:** para pregões municipais no PNCP, ausência de resultado no endpoint estruturado ou em indexador secundário não pode ser tratada como ausência de resultado documental sem verificar os anexos oficiais do processo.

## 2. Reconciliação das nove especificações

As nove famílias técnicas anteriores foram confirmadas nos itens oficiais do PNCP/Ata:

- T01 — plastichumbo Cu 2x4,0 mm 450/750V — item 7;
- T02 — plastichumbo Cu 2x2,5 mm 450/750V — item 8;
- T03 — flexível 16 mm² 0,6/1kV ATOX — itens 18, 25 e 41;
- T04 — PP 2x2,5 mm 1kV — item 30;
- T05 — PP 4x10 mm 1kV — itens 35 e 36;
- T06 — multiplex 4x16 mm² 1kV alumínio — item 49;
- T07 — flexível Cu 6 mm² PVC 70°C — itens 78–80;
- T08 — flexível Cu 10 mm² PVC 70°C — itens 81–83;
- T09 — flexível Cu 25 mm² PVC 70°C — itens 84–86.

A condição `SECONDARY_MIRROR_PENDING_OFFICIAL_TR_RECONCILIATION` deixa de ser necessária para essas especificações.

## 3. Cota principal/reservada — hipótese confirmada

O edital oficial estabelece expressamente que o **item 35 do Termo de Referência** é dividido em:
- ampla concorrência;
- cota reservada de até 25% para ME/EPP.

O edital também informa que a numeração sofre alteração no Portal de Compras Públicas devido à divisão do quantitativo.

No Portal/Ata:
- item 35 = 2.115 m;
- item 36 = 705 m;
- total = 2.820 m;
- 2.115/2.820 = 75%;
- 705/2.820 = 25%.

O chat oficial identifica expressamente o item 36 como **cota reservada**. Portanto, a leitura 75%/25% deixa de ser hipótese e passa a ser evidência documental oficial.

## 4. Resultado dos 18 itens prioritários

Valor estimado conjunto: **R$ 533.194,40**.

Resultado:
- 17 itens com vencedor na Ata Final;
- item 7 fracassado;
- valor vencedor somado dos 17 itens: **R$ 376.591,40**;
- valor estimado dos 17 itens adjudicáveis: **R$ 506.986,40**;
- diferença frente à estimativa nesses 17 itens: **R$ 130.395,00**, ou **25,72% abaixo**;
- o item 7 fracassado representa R$ 26.208,00, equivalentes a 4,92% da cesta prioritária.

Os 17 itens foram distribuídos entre múltiplos vencedores, sem dependência de um único fornecedor.

## 5. Descoberta de participação local que o inventário anterior não capturava

A Ata Final registra participação da **Comercial de Tintas Santo Antonio Ltda., CNPJ 28.927.340/0001-81**, em **todos os 18 itens prioritários de condutores**.

Na base territorial RFB já reconciliada do projeto, esse CNPJ é `LOCAL_EXACT_ACTIVE`, com estabelecimento ativo em São Borja.

Isso altera o diagnóstico anterior:

**Dado observado**
- existe participação local efetiva no PE39 para toda a cesta prioritária de condutores;
- o operador local participou dos 18 itens;
- ficou classificado, sem vencer, em 15 itens;
- foi desclassificado nos itens 7, 36 e 41.

**Não significa**
- que toda a oferta local esteja representada;
- que os demais operadores locais tenham capacidade equivalente;
- que o operador possua estoque físico integral;
- que a existência de uma proposta prove execução posterior.

## 6. Motivos das três não-conversões locais fora do preço comparável

### Item 7 — T01

O item foi considerado **fracassado**.

A proposta local acabou desclassificada por **valor acima da referência**. O mesmo ocorreu com os demais proponentes remanescentes até esgotamento das propostas válidas.

Portanto, T01 é um caso de insuficiência competitiva do conjunto de ofertas frente ao preço máximo, não de ausência de oferta.

### Item 36 — T05 / cota reservada

A empresa local chegou a ser arrematante da cota reservada, mas foi posteriormente desclassificada **a pedido da própria empresa**.

O item terminou com D33D Comércio Ltda. a R$ 32,16/m.

Esse episódio não deve ser classificado como derrota por preço: trata-se de falha de conversão da participação em fornecimento.

### Item 41 — T03

A empresa local apresentou lance inferior ao valor final vencedor, mas foi desclassificada porque **não apresentou o documento solicitado**.

O vencedor final foi Instalart Materiais Elétricos Ltda.

Também aqui a barreira observada não é o preço final isoladamente; é cumprimento documental/diligência.

## 7. Competitividade de preço nas 15 linhas em que a proposta local permaneceu classificada

Nos 15 itens em que o operador local permaneceu classificado, mas não venceu:
- soma dos valores vencedores: **R$ 325.418,60**;
- soma das propostas locais finais: **R$ 732.334,40**;
- prêmio local ponderado: **+125,04%** sobre os vencedores;
- mediana do prêmio por item: **+92,79%**.

Por cluster, considerando apenas linhas locais classificadas:
- T02: +62,59%;
- T03: +46,16% nos itens 18 e 25; item 41 foi desclassificado documentalmente;
- T04: +109,88%;
- T05: +92,79% no item 35; item 36 foi retirado/desclassificado a pedido;
- T06: +48,95%;
- T07: +407,64%;
- T08: +301,31%;
- T09: +85,79%.

Esses percentuais descrevem **preços finais do certame para os mesmos itens e quantidades**, não margens empresariais nem preços de varejo.

## 8. Preço entregue e logística

O edital/TR torna os preços diretamente comparáveis em termos contratuais:
- prazo de entrega: **20 dias** após confirmação da nota de empenho/ordem de compra;
- local de entrega: Departamento Municipal de Patrimônio e Documentos, São Borja;
- o preço contratado inclui despesas diretas e indiretas, inclusive **frete, seguro e demais custos necessários ao cumprimento integral do objeto**.

Assim, para os itens em que a empresa local permaneceu classificada, o gap observado é um teste mais próximo de **preço entregue ao município** do que de preço nominal de balcão.

## 9. Efeito sobre a matriz territorial de operadores

A principal consequência não é substituir um caso empresarial por outro.

A Ata Final demonstra que o universo de operadores deve ser construído por duas entradas simultâneas:

1. **oferta local observada/cadastral** — inventários, RFB, POM e evidência de produto;
2. **participantes efetivos dos certames** — atas, propostas e resultados.

A Comercial de Tintas Santo Antonio não aparecia na matriz inicial de candidatos do PE39, mas o resultado oficial prova participação ampla. Portanto, qualquer matriz futura que use somente o inventário prévio é incompleta.

Para os seis operadores correntes anteriormente testados por CNPJ exato:
- Iluminar;
- Mercado JL;
- Comercial Loss;
- Steelpet;
- Agropecuária Vieira;
- Agropecuária Centauro;

a busca por nome/CNPJ na Ata Final não encontrou participação.

Para os quatro leads históricos sem CNPJ corrente reconciliado, ausência de match nominal continua insuficiente para concluir ausência.

## 10. Diagnóstico de contestabilidade B2G — estágio atual

**Oferta local observada:** SIM.  
**Participação local efetiva:** SIM, em 18/18 itens prioritários por ao menos um operador local identificado.  
**Equivalência/aceitação de proposta:** demonstrada em 15/18 linhas para esse operador, com três falhas específicas de conversão.  
**Escala declarada:** o operador ofertou os quantitativos integrais dos 18 itens, mas isso não prova estoque físico ou execução.  
**Prazo/logística:** proposta submetida sob prazo contratual de 20 dias e entrega em São Borja.  
**Habilitação:** não pode ser generalizada; ao menos um item revelou falha documental em diligência.  
**Preço entregue:** principal barreira observada nas 15 linhas classificadas, com prêmio ponderado de 125,04% sobre os vencedores.  
**Participação:** deixou de ser indeterminada para o processo analisado.

A leitura correta passa a ser:

> O PE39 demonstra que a oferta local pode entrar no certame e cobrir tecnicamente grande parte da cesta, mas a conversão em fornecimento foi limitada sobretudo pela competitividade de preço nas linhas classificadas e, em casos específicos, por falhas de documentação/continuidade da proposta.

Isso é muito diferente de “não há oferta local”.

## 11. Implicações para os cadernos

Atualizações necessárias no `Delta_cadernos`:
- corrigir “resultado PE39 não publicado” para “resultado documental oficial disponível no PNCP; endpoint estruturado ainda sem resultado”;
- promover o desenho 75/25 de hipótese para evidência;
- substituir “contestabilidade local aberta” por diagnóstico parcial observado;
- incluir a distinção entre:
  - participação;
  - classificação técnica/processual;
  - preço entregue;
  - diligência/habilitação;
  - conversão em vitória;
- registrar que o inventário local prévio não cobre necessariamente todos os participantes locais efetivos.

O Caderno-Base v028 permanece read-only.

## 12. Fontes e limitações

**Fontes primárias**
- PNCP — metadados do PE39/2026;
- Edital PCE 39/2026;
- Anexo III — Termo de Referência;
- Ata Final do Portal de Compras Públicas, gerada em 25/08/2026;
- base RFB territorial reconciliada do projeto para localização empresarial.

**Limitações**
- “vencedor”/“arrematante” da Ata Final não deve ser confundido automaticamente com pagamento executado;
- estoque, capital de giro e entrega física posterior ainda não foram observados;
- a comparação de preço é específica ao PE39/2026;
- um operador local não representa todo o mercado local;
- a ausência dos demais candidatos atuais na Ata Final é forte para os CNPJs exatos pesquisados, mas os leads históricos sem CNPJ permanecem indeterminados.
