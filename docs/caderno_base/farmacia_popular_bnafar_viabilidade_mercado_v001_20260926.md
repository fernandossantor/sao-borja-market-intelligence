# Farmácia Popular / BNAFAR — auditoria de viabilidade para dimensão de mercado — v001

**Data:** 2026-09-26  
**Mercado:** Saúde, Higiene e Cuidados Pessoais  
**Geografia-alvo:** São Borja/RS  
**Finalidade:** avaliar se bases públicas federais permitem obter uma camada monetária observada de dispensações de medicamentos no município.  
**Status:** auditoria concluída para disponibilidade pública; **não há, na publicação aberta localizada, série monetária municipal defensável para market size ou market share**.

## 1. Pergunta analítica

É possível utilizar Farmácia Popular/BNAFAR para observar, em São Borja:

- quantidade de dispensações;
- valor monetário dispensado/reembolsado;
- estabelecimento;
- produto/medicamento;
- período;

de modo a construir um submercado observado de medicamentos?

## 2. BNAFAR — o que a base contém institucionalmente

O Ministério da Saúde informa que a Base Nacional de Dados de Ações e Serviços da Assistência Farmacêutica (BNAFAR) consolida posições de estoque, movimentações e dispensações de medicamentos e insumos de municípios, estados e Distrito Federal.

A documentação institucional também informa que medicamentos disponibilizados pelo Programa Farmácia Popular integram a BNAFAR e que os eventos do programa são incorporados diretamente pelo Ministério da Saúde.

Fontes oficiais:
- https://www.gov.br/saude/pt-br/composicao/sectics/daf/bnafar
- https://www.gov.br/saude/pt-br/composicao/sectics/daf/bnafar/faq/faq/o-que-e-a-base
- https://www.gov.br/saude/pt-br/composicao/sectics/daf/bnafar/faq/faq/como-enviar-os-dados-a

## 3. O que está aberto publicamente em setembro de 2026

No Portal de Dados Abertos do SUS, o grupo público de Assistência Farmacêutica retorna um conjunto identificado como:

`BNAFAR - Posição de Estoque`.

Metadados observados:
- granularidade geográfica: município;
- atualização declarada: quinzenal;
- situação informada na página: “Posição de estoque - BNAFAR - Em manutenção”;
- recursos CSV/JSON referentes à posição de estoque.

Fonte:
https://dadosabertos.saude.gov.br/dataset/bnafar-posicao-de-estoque

**Uso correto:** caracterização de estoque/disponibilidade administrativa, após auditoria do arquivo.

**Uso incorreto:** faturamento, gasto das famílias, dispensação monetária ou market share.

Estoque é uma variável de posição, não um fluxo de vendas ou dispensações.

## 4. DBPOPFARMA no Plano de Dados Abertos do Ministério da Saúde

O Plano de Dados Abertos 2024-2026 inventaria:

`Conjunto de Dados de Dispensações – Sistema Autorizador do Programa Farmácia Popular do Brasil (DBPOPFARMA)`.

No inventário do PDA, a base é classificada como:
- possível de abertura: **Sim**;
- disponível em dados.gov.br no inventário: **Não**;
- periodicidade: **em tempo real**;
- possui conteúdo sigiloso: **Sim**.

O mesmo documento inclui DBPOPFARMA no cronograma de abertura com frequência mensal e meta originalmente indicada para julho/2024.

Fonte oficial:
https://www.gov.br/saude/pt-br/acesso-a-informacao/dados-abertos/pda/plano-de-dados-abertos-ms-2024-2026.pdf

**Observação importante:** o fato de existir meta de abertura no PDA não prova que a base tenha sido efetivamente publicada com os campos de que o SBMI necessita. Na consulta corrente ao Portal de Dados Abertos do SUS, não foi localizado conjunto público de dispensações DBPOPFARMA equivalente; o conjunto público encontrado no tema Assistência Farmacêutica é o de posição de estoque da BNAFAR.

## 5. Conteúdo monetário — não comprovado

A documentação pública localizada confirma a existência de registros de dispensação, mas **não comprova que uma eventual publicação agregada do DBPOPFARMA exponha valor monetário de venda, ressarcimento ou pagamento por autorização**.

Portanto, nesta etapa não se assume que:

`dispensação = faturamento`

nem que:

`quantidade dispensada × preço de referência = faturamento empresarial`.

Para uso monetário, seria necessário obter diretamente uma variável administrativa de valor, com definição explícita, por exemplo:
- valor autorizado;
- valor pago/reembolsado pelo programa;
- valor de referência;
- copagamento, quando aplicável;
- valor total da operação.

É necessário também identificar qual desses conceitos existe e qual responde à pergunta de mercado.

## 6. Conclusão para o SBMI

### Dados observados

- a BNAFAR institucionalmente contempla dispensações;
- Farmácia Popular alimenta a arquitetura da BNAFAR;
- existe conjunto público de **posição de estoque** com granularidade municipal;
- DBPOPFARMA consta no PDA federal como base de dispensações possível de abertura, não disponível em dados.gov.br no inventário e contendo informação sigilosa.

### O que não é possível concluir

Com as fontes públicas localizadas, não é possível calcular para São Borja:
- faturamento do Farmácia Popular;
- valor total de medicamentos dispensados pelo programa;
- participação do Farmácia Popular no varejo farmacêutico;
- faturamento de farmácias individuais;
- market share de redes ou estabelecimentos.

### Grau de confiança

- existência e escopo institucional da BNAFAR: **ALTA**;
- disponibilidade pública de posição de estoque municipal: **ALTA**;
- disponibilidade pública corrente de dispensações DBPOPFARMA: **BAIXA/NÃO LOCALIZADA**;
- possibilidade de dimensão monetária com a publicação corrente: **NÃO DEFENSÁVEL**.

## 7. Rota de obtenção recomendada

Solicitar ao Ministério da Saúde/DAF, apenas em formato agregado e com aplicação das regras de sigilo:

`ano-mês | município da dispensação | código/descrição do produto | quantidade de autorizações/dispensações | quantidade dispensada | valor autorizado/reembolsado/pago (se existente) | número de estabelecimentos participantes`.

Para São Borja:
- município: São Borja/RS;
- código IBGE: 4318002;
- período recomendado: 2023-01 até a última competência fechada disponível em 2026.

A solicitação deve pedir explicitamente a **definição de cada variável monetária** e informar que não são necessários CPF, beneficiário, prescrição, CNPJ individual ou qualquer microdado sigiloso.

## 8. Uso futuro

Se o Ministério fornecer valor agregado por produto/município/período:
- classificar como **faturamento/dispensação administrativa observada do submercado Farmácia Popular**, conforme definição da variável;
- não generalizar ao varejo farmacêutico total;
- comparar com DR de Remédios apenas com ressalva de perímetro: a POF mede gasto das famílias e o programa mede uma modalidade específica de fornecimento/financiamento.

Se apenas quantidade de dispensações for fornecida:
- usar como intensidade/volume do submercado;
- não converter em faturamento sem preço/valor administrativo compatível.

## 9. Impacto na matriz de dimensão de mercado

Alterar a fonte `Farmácia Popular / BNAFAR / DBPOPFARMA` de **A AUDITAR** para:

**AUDITADA — PUBLICAÇÃO ABERTA INSUFICIENTE PARA DIMENSÃO MONETÁRIA; EXTRAÇÃO AGREGADA A SOLICITAR.**

O benchmark de demanda residente de Remédios do POF/IPCA permanece uma estimativa de demanda, não deve ser substituído ou “validado” por estoque BNAFAR.
