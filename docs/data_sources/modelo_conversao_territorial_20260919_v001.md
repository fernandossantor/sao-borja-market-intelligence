# Modelo territorial de geração, apropriação, recirculação e vazamento — São Borja — v001

**Status:** exploratório — não canônico.  
**Data:** 19/09/2026.  
**Objeto:** organizar a hipótese de conversão territorial do valor em uma sequência contábil e mercadológica auditável.  
**Abrangência:** município de São Borja, com benchmarks do Rio Grande do Sul e de Uruguaiana explicitamente separados dos dados municipais.

## 1. Problema analítico

A questão central não é apenas quanto São Borja produz, recebe ou vende, mas **quanto dos fluxos gerados ou recebidos se converte em renda de residentes, compras locais, remuneração do trabalho, reinvestimento e recirculação antes de sair do território**.

O modelo evita três simplificações incorretas:

1. “o agro gera valor e esse valor sai”;
2. “o comércio apenas circula e não gera valor”;
3. “todo recurso público recebido permanece no município”.

Os dados correntes mostram que os circuitos têm estruturas distintas e que geração, apropriação e retenção são etapas diferentes.

## 2. Sequência do modelo

**Entrada externa / produção territorial → cadeia produtiva → VAB → apropriação primária → renda residente → gasto local → recirculação empresarial → vazamento → resultados territoriais.**

Cada seta representa uma transformação que deve ser medida separadamente.

### Etapa 0 — entradas externas

Fluxos federativos, folhas de órgãos externos ao município, benefícios previdenciários e assistenciais, exportações por domicílio fiscal e gasto de visitantes podem introduzir recursos no território.

As bases existentes demonstram escala material desses canais, mas **não devem ser somadas mecanicamente**, porque possuem períodos, conceitos e universos diferentes.

### Etapa 1 — geração de valor

Em 2021, valores observados de VAB municipal:
- agropecuária: **R$ 795,875 milhões**;
- comércio e demais serviços privados, excluída administração pública: **R$ 928,203 milhões**;
- administração pública: **R$ 351,229 milhões**.

Portanto, o terciário privado é simultaneamente grande gerador de valor agregado e principal circuito cotidiano de emprego/transação.

### Etapa 2 — cadeia produtiva

O benchmark Conab 2025/26 de Uruguaiana identifica **55,94% do custo total** do arroz em um núcleo formado por insumos industriais, mecanização, transporte/armazenagem e juros, cuja retenção depende fortemente da localização de fornecedores/prestadores/capital.

O cruzamento MIP-RS 2019 × Conab indica **10,01% do custo total** como conteúdo proveniente de fora do próprio RS apenas nas linhas mapeadas. Isto é um **piso parcial de exposição extraterritorial**, não uma taxa municipal.

### Etapa 3 — apropriação primária do VAB

Benchmark TRU-RS 2019:
- agro: remunerações/VAB **12,75%**;
- terciário privado amplo: **40,48%**;
- produção pública: **89,53%**.

A estrutura mostra que VAB semelhante pode produzir efeitos muito distintos sobre a renda laboral. No agro, grande parte do valor aparece como excedente operacional/rendimento misto; seu destino territorial permanece desconhecido.

### Etapa 4 — renda residente

Censo 2022:
- mediana do rendimento domiciliar per capita: **R$ 1.100/mês**;
- média: **R$ 1.568,58/mês**;
- 85,79% do universo sem rendimento ou até 2 salários mínimos per capita;
- 2,78% acima de 5 salários mínimos per capita.

A renda residente é o elo que conecta produção/transferências à capacidade efetiva de demanda local, mas não equivale ao PIB nem ao VAB.

### Etapa 5 — gasto local

É a maior lacuna atual. Não há medida municipal confiável de:
- gasto em estabelecimentos de São Borja;
- gasto em outros municípios;
- gasto na Argentina;
- gasto em e-commerce/marketplaces externos.

O benchmark BCB de 28,1% do valor em cartão de crédito capturado pela internet no Brasil no 4T2025 apenas demonstra relevância do canal; não pode ser aplicado como share local.

### Etapa 6 — recirculação empresarial

Empresas locais podem transformar vendas em:
- salários;
- compras de fornecedores locais;
- serviços técnicos;
- aluguéis;
- tributos locais;
- investimento.

Há evidência de elos locais relevantes — por exemplo beneficiamento de arroz e manutenção de máquinas —, mas o volume monetário das compras B2B locais ainda não foi medido.

### Etapa 7 — vazamento

Os canais prioritários a medir são:
- fornecedores externos;
- compras centralizadas de redes;
- gasto digital/extralocal das famílias;
- juros e serviços financeiros;
- rendas de propriedade/lucros destinados a não residentes;
- investimentos realizados fora do município.

A medida correta deve ser específica por canal; uma “taxa única de vazamento municipal” ainda não é defensável.

### Etapa 8 — resultados territoriais

Entre 2010 e 2022, a população censitária caiu 1.995 pessoas. O saldo migratório residual estimado é negativo entre aproximadamente 4.780 e 5.001 pessoas.

Isto demonstra dificuldade de retenção populacional no período, **mas não demonstra que vazamento econômico tenha causado a migração**.

## 3. Indicadores decisórios

### Compras públicas

**Participação local da despesa paga = valor pago a credores locais / valor pago total elegível × 100.**

Classificação recomendada do CNPJ:
- LOCAL_EXACT: CNPJ credor corresponde a estabelecimento ativo em São Borja;
- ROOT_WITH_LOCAL_FOOTPRINT: CNPJ credor não é local, mas a raiz possui estabelecimento ativo em São Borja;
- EXTERNAL_NO_LOCAL_FOOTPRINT: raiz não aparece entre estabelecimentos ativos de São Borja;
- PF_OUTRO_INDETERMINADO: CPF, documento não CNPJ ou cadastro insuficiente.

Não combinar as categorias sem explicitar a regra. Para retenção jurídica/financeira, LOCAL_EXACT é a definição mais estrita. Para presença operacional, LOCAL_EXACT + ROOT_WITH_LOCAL_FOOTPRINT forma um indicador ampliado.

### Compras B2B privadas

**Participação local B2B = valor de compras de fornecedores de São Borja / valor total de compras amostradas × 100.**

Necessita dados empresariais ou pesquisa primária.

### Gasto das famílias

**Retenção de consumo = gasto destinado a vendedores estabelecidos em São Borja / gasto total da categoria × 100.**

Deve ser coletado por categoria e canal; não por percepção genérica.

## 4. Diagnóstico corrente

A evidência disponível sustenta uma formulação mais precisa:

> São Borja apresenta circuitos econômicos com capacidades muito diferentes de converter produção e transferências em renda laboral e recirculação local. O problema territorial prioritário não é ausência de geração de valor, mas a possível perda de conversão entre geração, apropriação, gasto e reinvestimento. Agro, terciário privado e setor público cumprem funções distintas nesse processo.

A tese é **parcialmente sustentada**. A taxa efetiva de retenção municipal continua não observada.

## 5. Prioridades de fechamento

1. despesa pública efetivamente paga por credor e classificação territorial;
2. origem geográfica de compras B2B do agro/agroindústria e cadeias âncora;
3. destino/canal do gasto das famílias;
4. residência/propriedade dos recebedores de excedente e renda da terra;
5. investimento local versus extralocal;
6. perfil e motivo da migração.

## 6. Decisão editorial

O modelo está pronto para orientar a redação do **Caderno Geral**, mas não deve ser promovido automaticamente ao Caderno-Base v028. O Caderno permanece read-only até autorização explícita.

Os quatro cadernos setoriais devem receber apenas deltas propostos, mantendo a distinção entre:
- evidência observada;
- benchmark;
- simulação;
- hipótese;
- recomendação.
