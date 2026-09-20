# PE 39/2026 — materialização e reconciliação oficial — v001

**Data de consolidação:** 20/09/2026  
**Abrangência:** Município de São Borja/RS — Pregão Eletrônico nº 39/2026 — Processo nº 14698/2026  
**PNCP:** `88489786000101-1-000136/2026`  
**Objeto:** registro de preços para materiais elétricos destinados à manutenção da rede de iluminação pública e da infraestrutura elétrica dos prédios públicos.  
**Unidade analítica do projeto:** `objeto/grupo de produto × oferta local × participação × escala × habilitação × preço/frete/logística`.

## Fontes oficiais materializadas

Fonte primária: Portal Nacional de Contratações Públicas (PNCP).

Documentos observados no endpoint oficial de arquivos em 20/09/2026:

| seq. | documento | publicação PNCP | SHA-256 |
|---:|---|---|---|
| 1 | EDITAL_E_ANEXOS_PCE_39_2026.7z | 09/07/2026 11:23:10 | `8af6ab36c81f6c0380c77cc4b0c84a1142f8fe367346511c84d08c302ec5870a` |
| 2 | FASE_PREPARAT_RIA_PCE_39_2026.7z | 09/07/2026 11:23:12 | `9d850a2f9345d931f294a1de28a010fa6b5f3f03584ce5d8914e7a796315049d` |
| 3 | Ata_Final_144426_250826.zip | 25/08/2026 14:45:18 | `6412b0508682441618c3eefd248cdf4c5a1599dc48d8bed66a531d8a14db1cb9` |
| 4 | Ata_Parcial_144549_250826.zip | 25/08/2026 14:46:52 | `a35f92262884092f731e663590a1e44cee53c6deb98f35c0733cd2f3ba15ecfd` |

A Ata Final foi gerada eletronicamente em 25/08/2026 às 14:44:29, com 229 páginas e código verificador `176D2C9`. A Ata Parcial foi gerada às 14:45:54, com 224 páginas e código verificador `176D311`.

A materialização reproduzível foi executada pelo workflow:
`.github/workflows/pncp-pe39-priority-audit.yml`.

Execução validada:
- run: `35530814428`;
- conclusão: **success**;
- artifact: `pe39-priority-official`;
- artifact id: `10611316819`;
- digest: `sha256:47b35c745e35d15e588f2c4158fc1d7f4d2b4d2248468ea23e4498e0ec6b920b`.

Foi executada também auditoria dirigida da Ata Final:
- workflow: `.github/workflows/pncp-pe39-ata-final-audit.yml`;
- run: `35530968233`;
- conclusão: **success**;
- artifact: `pe39-ata-final-audit`;
- artifact id: `10610624747`;
- digest: `sha256:3dda6a7730ab8d2dd11425abbcc82c4254a5767cfdf2bc4b6a41d0391c459359`.

## Correção de estado documental

A formulação anterior — “resultado ainda não publicado segundo indexador secundário” — ficou **superada**.

**Dado observado:** o PNCP oficial disponibiliza Ata Final e Ata Parcial desde 25/08/2026.

**Limitação:** o registro estruturado do PNCP continua, na consulta realizada, com:
- `existeResultado = false`;
- `valorTotalHomologado = null`;
- endpoint estruturado `/resultados` dos 18 itens prioritários retornando HTTP 204.

Portanto, devem ser distinguidos:

1. **resultado documental da sessão/ata**, que existe e pode ser analisado;
2. **resultado estruturado/homologação no PNCP**, que ainda não está preenchido no endpoint consultado;
3. **contratação/ata de registro de preços/empenho/pagamento**, que são etapas posteriores e não podem ser inferidas da Ata Final.

## Especificações dos condutores

As descrições e quantidades dos 18 itens prioritários foram confirmadas por fonte oficial PNCP/Ata Final. Assim, os nove clusters técnicos deixam de depender apenas do espelho secundário para sua descrição básica.

O arquivo `priority_conductors_result.csv` preserva os 18 itens, valores estimados, status da Ata, vencedor documental, oferta final do operador local confirmado e observações.

## Desenho 75%/25% — T05

A hipótese anterior foi resolvida.

- item 35: 2.115 m, `Sem benefício`;
- item 36: 705 m, `Participação exclusiva para ME/EPP`;
- soma: 2.820 m;
- proporções: 75% e 25%.

A Ata Final denomina o item 36 como **cota reservada** e registra que, quando um fornecedor vence cota reservada e principal, aplica-se o menor valor às duas. Também registra a orientação do edital para considerar a divisão do quantitativo entre ampla concorrência e cota reservada.

**Conclusão observacional:** o par 35/36 corresponde ao desenho principal/reservado 75%/25%.

## Resultado dos 18 condutores prioritários

- 18 linhas analisadas;
- 17 aceitas na Ata Final;
- 1 fracassada: item 7;
- taxa por linhas: `17 / 18 = 94,44%`;
- valor estimado das 18 linhas: **R$ 533.194,40**;
- item fracassado: **R$ 26.208,00** estimados;
- valor de referência das 17 linhas aceitas:  
  `R$ 533.194,40 - R$ 26.208,00 = R$ 506.986,40`;
- soma dos valores documentais dos vencedores das 17 linhas aceitas: **R$ 376.591,40**;
- diferença frente à referência do mesmo subconjunto:  
  `R$ 506.986,40 - R$ 376.591,40 = R$ 130.395,00`;
- diferença relativa:  
  `R$ 130.395,00 / R$ 506.986,40 = 25,72%`.

**Interpretação:** os valores aceitos na Ata ficaram 25,72% abaixo do valor estimado no subconjunto comparável de 17 linhas.

**Limitação:** não chamar essa diferença de “economia realizada”, pois Ata Final/aceitação não equivale, por si só, a homologação, contratação, empenho ou pagamento.

## Participação territorial observada

A leitura da Ata revelou um operador que não estava no primeiro inventário de candidatos:

**COMERCIAL DE TINTAS SANTO ANTONIO LTDA — CNPJ 28.927.340/0001-81.**

No controle territorial já existente do projeto (`core_vendor_territorial_2026.csv`), esse CNPJ está classificado como:
- `LOCAL_EXACT_ACTIVE`;
- município TOM 8863;
- São Borja/RS;
- 35 empenhos no núcleo municipal observado;
- R$ 336.976,46 pagos no núcleo 2026 acumulado do arquivo corrente.

Na Ata Final do PE39:
- o operador aparece nas **18/18 linhas prioritárias**;
- permaneceu classificado em 15;
- foi desclassificado em 3;
- não consta como vencedor final de nenhuma das 18.

Desclassificações observadas:
- item 7: valor acima da referência; o item inteiro fracassou;
- item 36: desclassificação a pedido da empresa;
- item 41: “Não apresentou o documento solicitado”.

### Comparação de preço — somente linhas em que permaneceu classificado

Para evitar misturar lances desclassificados com ofertas válidas finais, a comparação agregada usa apenas 15 linhas.

- soma dos valores finais locais: **R$ 732.334,40**;
- soma dos vencedores nas mesmas 15 linhas: **R$ 325.418,60**;
- diferença: **R$ 406.915,80**;
- diferença relativa ao valor dos vencedores:
  `R$ 406.915,80 / R$ 325.418,60 = 125,04%`.

**Interpretação:** nesse subconjunto observado, a oferta final do operador local ficou, em termos agregados ponderados, 125,04% acima dos vencedores.

**Não concluir:** que “o comércio local é 125% mais caro”. Trata-se de um operador, em 15 linhas específicas, em uma sessão específica. O indicador testa um mecanismo e não representa o universo local.

Os itens 36 e 41 reforçam outro mecanismo: preço baixo, isoladamente, não garante êxito quando há retirada/desclassificação ou falha documental.

## Correção do diagnóstico de contestabilidade

Formulação anterior:
> há oferta local da família e experiência B2G, mas participação efetiva permanece indeterminada.

Formulação corrigida:
> há **contestação B2G local efetivamente observada** nos nove clusters por pelo menos um operador comprovadamente localizado em São Borja, porque esse operador apresentou oferta nas 18 linhas prioritárias. Contudo, a contestabilidade competitiva foi insuficiente para gerar vitória final nesse conjunto: predominou desvantagem de preço nas linhas em que permaneceu classificado, além de duas desclassificações relevantes por retirada/documentação e um item fracassado por preço acima da referência.

Isso não transforma o operador em caso central. Ao contrário, o achado demonstra que o universo de operadores deve ser construído também **a partir dos participantes efetivos do certame**, e não apenas do inventário empresarial prévio.

## Próximo gate dirigido

1. territorializar os CNPJs de todos os participantes das 18 linhas prioritárias;
2. identificar quantos são locais, regionais e externos;
3. verificar se há outros operadores de São Borja além do já confirmado;
4. cruzar, para cada operador local efetivo, participação × classificação × preço × motivo de perda/desclassificação;
5. só depois retornar a estoque, escala, prazo e upstream dos operadores que de fato demonstraram aderência ao objeto;
6. acompanhar homologação/ARP/contratos/empenhos/pagamentos separadamente.

## Reconciliação do Edital e Termo de Referência

Uma auditoria posterior extraiu com sucesso os PDFs do pacote oficial do edital usando `p7zip`:

- workflow: `.github/workflows/pncp-pe39-edital-tr-audit.yml`;
- run: `35532386207`;
- conclusão: **success**.

O edital confirma expressamente:
- item 35 do Termo de Referência dividido entre ampla concorrência e cota reservada de até 25% para ME/EPP;
- alteração da numeração no Portal por causa dessa divisão;
- valor máximo total de R$ 1.074.671,14.

O Termo de Referência/contrato confirma:
- prazo de entrega de até 20 dias após confirmação do recebimento da nota de empenho/ordem de compra;
- entrega no DMPD, em São Borja/RS;
- preço contratual incluindo despesas diretas e indiretas, inclusive frete, seguro e demais custos necessários à execução.

Assim, a comparação de preços da Ata é mais adequadamente interpretada como comparação de **preço contratual entregue sob condições comuns**, sem revelar a decomposição interna de frete, margem ou custo de aquisição.

## Limitações

- a Ata Final documenta a sessão e o resultado nela registrado, mas não substitui homologação/contratação/pagamento;
- classificação processual de proposta não equivale automaticamente a validação técnica integral do produto, especialmente para licitantes não vencedores;
- a classificação territorial dos demais participantes ainda não está concluída;
- ausência dos dez candidatos anteriores na busca textual da Ata Final não deve ser convertida em ausência absoluta sem preservar a possibilidade de diferenças de razão social/CNPJ; para os seis CNPJs conhecidos, porém, a busca exata na Ata Final não encontrou ocorrência.
