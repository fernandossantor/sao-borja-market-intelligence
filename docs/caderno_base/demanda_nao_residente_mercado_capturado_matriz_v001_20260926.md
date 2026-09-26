# Demanda não residente e mercado capturado — matriz de mensuração v001

**Data:** 2026-09-26  
**Geografia:** São Borja/RS  
**Objetivo:** definir como separar gasto residente, gasto não residente e mercado efetivamente capturado pelos fornecedores locais sem transformar fluxos de pessoas ou indicadores de centralidade em valores monetários.

## 1. Definições

**Demanda não residente (DNR):** gasto realizado junto a fornecedores de São Borja por pessoas ou organizações cuja base residencial/econômica relevante está fora do município.

**Mercado capturado (MC):**

`MC = gasto de residentes em fornecedores locais + gasto de não residentes em fornecedores locais`.

O mercado capturado não é igual a:
- população × gasto médio;
- faturamento empresarial territorial quando há vendas remotas para fora;
- número de visitantes;
- fluxo de veículos;
- índice de atração REGIC;
- quantidade de estabelecimentos.

## 2. Evidências territoriais já disponíveis

### REGIC 2018 — atração funcional

A Base Territorial já auditou as ligações temáticas da REGIC 2018.

São Borja aparece como destino temático para nove municípios:
- Maçambará;
- Santo Antônio das Missões;
- Itaqui;
- Garruchos;
- Itacurubi;
- São Luiz Gonzaga;
- Unistalda;
- Santiago;
- Uruguaiana.

Maiores participações gerais estimadas para São Borja:
- Maçambará: 27,33%;
- Santo Antônio das Missões: 12,04%;
- Itaqui: 10,41%;
- Garruchos: 9,33%;
- Itacurubi: 4,47%.

Há também centralidade temática em:
- vestuário/calçados;
- móveis/eletroeletrônicos;
- saúde de baixa/média complexidade;
- cultura;
- transporte coletivo.

**Classificação:** DADO/INDICADOR REGIC 2018 já auditado no projeto.

**Uso:** delimitar área de influência e municípios prioritários para investigar DNR.

**Proibição:** IA e PERC_LIG não são pessoas, visitas, vendas, faturamento ou market share.

### Censo 2022 — mobilidade de residentes

O Censo documenta deslocamentos dos residentes de São Borja para trabalho/estudo fora do município. Isso ajuda a entender exposição a outros mercados, mas não mede entrada de consumidores não residentes nem seus gastos em São Borja.

## 3. Fonte com maior potencial — NFS-e municipal

O layout atual da NFS-e/INFISC documenta:
- competência;
- local da prestação;
- destinatário;
- endereço nacional do destinatário;
- `cMun` — código IBGE do município do endereço do destinatário.

Se a Prefeitura fornecer agregado:

`competência × item de serviço × município do destinatário × valor`

poderemos calcular, para submercados de serviços:

`valor_endereço_externo / valor_total`.

Esse indicador deve ser denominado, inicialmente, **participação do valor faturado a destinatários com endereço externo**, e não “demanda não residente” sem auditoria.

Limitações:
- município do endereço do destinatário não prova residência usual;
- B2B registra sede/endereço empresarial;
- completude histórica pode variar;
- local da prestação precisa ser compatibilizado.

## 4. Bens comercializados via NFC-e

O DFe municipal observado não expõe origem do consumidor.

Assim, mesmo que seja obtido `São Borja × CNAE/NCM × NFC-e`, teremos mercado formal capturado no território por categoria, mas **não será possível separar residentes e não residentes apenas com a NFC-e agregada**.

Fontes adicionais defensáveis:

1. adquirência/cartões com município de residência/origem do portador em nível agregado;
2. CRM/programas de fidelidade com CEP/município do cliente e valor da transação, fornecidos voluntariamente e agregados;
3. pesquisa primária intercept em pontos de venda, registrando município de residência e valor efetivamente gasto;
4. dados de mobilidade geográfica agregada combinados com pesquisa de gasto — jamais movimento × gasto presumido sem calibração.

## 5. Matriz por setor

| Setor | Sinal de atração já disponível | Fonte monetária potencial para DNR | Situação atual |
|---|---|---|---|
| Bens Essenciais | REGIC geral e área de influência; estrutura territorial | adquirência; CRM/CEP + venda; pesquisa intercept | não monetizada |
| Saúde/Higiene | REGIC saúde baixa/média; rede regional de atendimento | NFS-e para serviços; adquirência/CRM para varejo farmacêutico | não monetizada |
| Bens Não Essenciais | REGIC vestuário/calçados e móveis/eletro | adquirência; CRM/CEP + venda; pesquisa intercept | não monetizada |
| Serviços | REGIC funcional + NFS-e com município do destinatário | **NFS-e agregada é rota prioritária** | potencial direto, ainda não obtido |
| Alimentação Fora do Lar | centralidade urbana/turística a investigar; mobilidade e eventos são apenas exposição | adquirência; pesquisa intercept/recibo; CRM/delivery com endereço agregado | não monetizada |

## 6. Indicadores a construir

Quando os dados permitirem:

### Valor local vendido a endereços externos
`VE = Σ vendas locais a clientes/endereço fora de São Borja`.

### Participação externa no faturamento capturado
`PE = VE / vendas locais totais`.

### Mercado capturado residente
`MCR = vendas locais totais - VE`, somente quando VE cobrir adequadamente o mesmo universo.

### Retenção da carteira residente
Se houver gasto total dos residentes e gasto dos residentes em fornecedores locais:

`retenção residente = gasto residente local / demanda residente total`.

### Vazamento da carteira residente
`vazamento = 1 - retenção residente`.

Esses indicadores exigem a mesma categoria, período e canal no numerador e denominador.

## 7. Pesquisa primária mínima para varejo/AFL

Caso dados transacionais por origem não sejam acessíveis, o desenho mínimo deve coletar, por transação:

- município de residência habitual;
- país, quando exterior;
- valor da compra/conta naquela ocasião;
- categoria/estabelecimento;
- canal — presencial, retirada, delivery;
- data/horário;
- motivo principal da presença em São Borja;
- frequência de visita.

A amostra não deve ser calculada sobre número de lojas. O universo de inferência precisa ser definido como transações/consumidores no período e os pontos de interceptação devem cobrir formatos e horários distintos.

## 8. Prioridade

1. obter NFS-e agregada com município do destinatário;
2. consultar adquirentes/operadoras sobre produto agregado por município do estabelecimento × município de origem do portador;
3. verificar possibilidade de CRM/CEP agregado com empresas parceiras;
4. somente na ausência dessas rotas desenhar pesquisa intercept para monetização da DNR.

## 9. Rastreabilidade

Base territorial relacionada:
- `benchmark_territorial_mobilidade_centralidade_v001.md`;
- `retencao_vazamento_draft.md`;
- `nfse_sao_borja_especificacao_dados_mercado_v001_20260926.md`.

A matriz é metodológica. Nenhum valor de demanda não residente foi estimado nesta versão.
