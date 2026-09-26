# Instrumento futuro de DNR — varejo e alimentação fora do lar — v001

**Data:** 2026-09-26  
**Status:** desenho metodológico; **não operacional nesta etapa**  
**Geografia:** São Borja/RS  
**Objetivo:** preparar coleta primária mínima para monetizar demanda não residente caso adquirência/CRM não estejam disponíveis.

## 1. Pergunta

Quanto do valor efetivamente gasto em fornecedores de São Borja é realizado por não residentes, em quais categorias/canais e por quais motivos de presença no município?

## 2. Unidade de observação

A unidade preferencial é a **transação/ocasião de compra**, associada a uma pessoa respondente.

Não usar:
- loja como unidade de inferência;
- fluxo de veículos como transações;
- número de visitantes × gasto presumido.

## 3. Variáveis mínimas

### Território
- município de residência habitual;
- UF;
- país;
- quando Argentina, localidade/província se informada voluntariamente.

### Transação
- valor efetivamente pago naquela ocasião;
- categoria/módulo SBMI;
- canal: presencial, retirada, delivery;
- data e faixa de horário;
- forma de pagamento em categoria ampla, se analiticamente necessária.

### Motivo de presença
Taxonomia de pesquisa a validar em pré-teste:
- trabalho;
- estudo;
- saúde;
- compras;
- visita familiar/social;
- turismo/lazer;
- trânsito/passagem;
- outro.

Essas categorias são **hipóteses instrumentais do SBMI**, não classificação oficial.

### Frequência e permanência
- frequência de presença em São Borja;
- pernoite sim/não;
- número de noites, quando aplicável;
- outras compras/serviços realizados na mesma visita, por categoria ampla.

## 4. Módulos

### Varejo
Perguntar:
- categoria comprada;
- valor;
- se a compra foi planejada antes da chegada;
- se houve comparação com outro município/e-commerce/Argentina.

### Alimentação Fora do Lar
Perguntar:
- valor da conta individual ou parcela atribuível ao respondente;
- tipo de ocasião — refeição, lanche, encontro, trabalho, viagem;
- canal;
- se o consumo foi motivado pela presença em São Borja ou era destino principal.

## 5. Desenho de campo

Se ativado, o campo deve cobrir:
- diferentes formatos de estabelecimento;
- dias úteis e fins de semana;
- diferentes faixas horárias;
- áreas centrais e pontos ligados a fluxos de entrada/saída;
- períodos ordinários e, separadamente, eventos.

A alocação amostral não deve ser proporcional apenas ao número de lojas.

O universo de inferência deve ser explicitado antes do cálculo amostral, por exemplo:
**transações presenciais elegíveis no período e pontos cobertos**, não “população municipal”.

## 6. Indicadores

### Gasto não residente observado na amostra

`DNR_amostra = Σ valor_transação de respondentes não residentes`.

### Participação externa da amostra

`PE_amostra = DNR_amostra / Σ valor_transação de todos respondentes × 100`.

Sem desenho probabilístico e ponderação adequada, esse percentual permanece **descritivo da amostra/campo**.

### Ticket por origem

`ticket_medio_origem = Σ valor / número de transações`.

Só comparar grupos com cobertura de pontos/horários suficiente.

## 7. Expansão para mercado

Nenhuma expansão municipal será autorizada apenas com a amostra de intercept.

Para estimar DNR total seria necessário um fator de expansão defensável, baseado em:
- universo de transações/receitas conhecido;
- adquirência/POS agregado;
- ou desenho probabilístico com probabilidades de seleção mensuráveis.

Sem isso, publicar:
- valores e percentuais da amostra;
- perfis e ocasiões;
- diferenças entre estratos;
- nunca “R$ total gasto por visitantes em São Borja”.

## 8. Relação com fontes secundárias

REGIC:
- delimita área de influência;
- ajuda a selecionar municípios de origem;
- não pondera gasto.

NFS-e:
- pode substituir parte da coleta em Serviços se município do destinatário tiver cobertura adequada.

CRM/POS:
- preferível à intercept quando contiver origem e valor agregáveis.

Adquirência:
- rota potencial mais robusta para varejo/AFL caso exista produto agregado por município do estabelecimento × origem do portador.

## 9. Privacidade

Não coletar CPF, documento, nome completo ou dados financeiros identificáveis.

Município de residência é suficiente para a pergunta territorial.

## 10. Status

Instrumento preservado para futura ativação.

Nesta etapa:
- nenhuma DNR monetária municipal foi estimada;
- nenhum tamanho de amostra é definido;
- nenhum campo é iniciado sem decisão posterior.
