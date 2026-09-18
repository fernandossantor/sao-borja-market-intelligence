# Agenda de dados decisórios e KPIs de monitoramento — 18/09/2026

**Status:** exploratório — não canônico

## 1. Objetivo

A etapa atual já possui volume suficiente de diagnóstico para evitar a armadilha de continuar acumulando fontes sem ganho decisório.

Foram separados dois produtos:
1. **agenda de dados decisórios** — quais lacunas ainda impedem conclusões mercadológicas;
2. **KPIs de monitoramento** — o que empresas, entidades ou futuras pesquisas podem medir sem inventar market share.

## 2. Lacunas que atravessam vários mercados

### Destino monetário do gasto

É a lacuna de maior alcance.

O projeto conhece:
- renda;
- estrutura de oferta;
- missões/jornadas;
- centralidade histórica;
- fluxo fronteiriço;
- presença digital.

Mas ainda não conhece, de forma monetária comparável:
- quanto fica em São Borja;
- quanto vai a outro município;
- quanto vai a e-commerce;
- quanto vai à Argentina;
- quanto é gasto por visitantes em São Borja.

Essa variável **não pode ser reconstruída por proxy**.

### Origem do cliente e captura de fluxo

Há forte evidência de circulação, mas pouca evidência de conversão econômica.

Fontes secundárias podem reduzir incerteza:
- Cadastur;
- ANP;
- eventos;
- tráfego;
- comércio exterior.

Nenhuma substitui ticket/gasto por origem.

### Radar

A metodologia está resolvida. O bloqueio é operacional: obter os CSVs reais.

Assim que os bytes forem obtidos, o pipeline genérico permitirá analisar várias cestas, não apenas arroz.

### Simples/SIMEI

A rota oficial está identificada; falta a extração municipal reproduzível.

Essa lacuna é mais “técnica” que “conceitual” e deve ser fechada antes de recorrer ao cross-check secundário.

## 3. Separação: secundário versus primário

### Ainda solucionável com dados secundários/administrativos
- Radar CSVs;
- SINAC/SIMEI;
- validação cadastral dos inventários POM;
- BET municipal;
- Comex Stat municipal;
- Cadastur;
- ANP;
- parte dos contratos públicos/B2B.

### Requer dado primário ou empresarial
- destino monetário do gasto;
- origem do cliente com ticket;
- market share;
- compras B2B privadas;
- conversão digital;
- ticket por missão;
- margem/lucro/reinvestimento;
- satisfação/recompra quando não houver CRM.

## 4. Critério para parar a coleta secundária

A coleta de uma dimensão deve ser considerada suficiente quando:
- fonte e conceito estiverem auditados;
- período e geografia forem adequados;
- valor puder ser reproduzido;
- a informação mudar uma decisão ou reduzir uma lacuna explicitamente registrada.

Se não atender a essas condições, não deve ser adicionada apenas para “enriquecer” o acervo.

## 5. KPIs sem pseudo-market-share

A proposta de monitoramento privilegia métricas observáveis dentro dos mercados:

Bens essenciais:
- ruptura;
- fila;
- divergência de preço;
- ticket por missão.

Saúde/higiene:
- unidades ativas por submercado;
- estrutura multiunidade;
- SLA digital;
- conversão pesquisa→compra.

Bens não essenciais:
- atualização digital;
- disponibilidade imediata;
- conversão digital→loja;
- prazo de troca.

Serviços:
- primeira resposta;
- lead→contrato;
- no-show;
- avaliações.

Alimentação:
- ticket por origem;
- ocupação;
- delivery;
- recompra.

Transversal:
- origem do cliente;
- retenção monetária do gasto — somente quando houver pesquisa/dado transacional adequado.

## 6. Ordem operacional recomendada

Sem atribuir score, a sequência mais eficiente é:

1. fechar fontes secundárias que já possuem rota oficial e alta alavancagem: Radar, SINAC/SIMEI, Comex, BET municipal, Cadastur/ANP;
2. validar oferta ativa nos inventários que já existem, especialmente saúde e não essenciais;
3. iniciar desenho de coleta primária/empresarial para destino do gasto, origem do cliente e B2B;
4. implantar KPIs operacionais com parceiros voluntários antes de tentar estimar market share.

Arquivos:
- `agenda_dados_decisorios_20260918_v001.csv`;
- `kpis_monitoramento_pom_20260918_v001.csv`.

## 7. Atualização operacional — ANP, Cadastur e ANTT

Após a definição da agenda, três rotas tiveram avanço material.

### ANP

São Borja foi extraído para:
- gasolina C, etanol, diesel e GLP — 2023 e 2024;
- cadastro corrente de revendedores — 18/09/2026.

A lacuna “mobilidade por combustíveis” deixa de ser ausência de valor municipal.

Novo estado:
**VALORES MUNICIPAIS RECUPERADOS; INTERPRETAÇÃO CAUSAL BLOQUEADA.**

### Cadastur

Para o 2T2026 foram recuperados:
- 2 meios de hospedagem Regular/Operação;
- 90 UHs;
- 180 leitos;
- 7 agências de turismo localizadas;
- 6 Regular/Operação;
- 1 Em Implantação.

Novo estado:
**HOSPEDAGEM/AGÊNCIAS RECUPERADAS; DEMAIS CATEGORIAS E DEMANDA PENDENTES.**

### ANTT

O Anuário TRC 2025 acrescenta série específica do ponto de fronteira de São Borja:
- 2023: 859.348 t exportadas;
- 2024: 800.435 t;
- 2025: 979.151 t.

A participação de São Borja no total das seis fronteiras da tabela sobe de 14,50% em 2023 para 16,22% em 2025.

### Consequência para a agenda

A fronteira passa a ter:
- fluxo físico exportador;
- abastecimento municipal;
- oferta turística formal;
- estrutura empresarial local.

O principal bloqueio permanece:
**origem do cliente + permanência + gasto/ticket.**

A comparação 2023→2024 também mostrou que exportações pela fronteira caíram 7%, enquanto gasolina, diesel e etanol vendidos no município cresceram fortemente.

Portanto, vendas de combustível **não devem ser usadas como proxy direto do fluxo exportador fronteiriço**.
