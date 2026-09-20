# Análise de retenção seletiva das compras públicas — São Borja — 2026 parcial — v002

**Status:** análise exploratória controlada; não promoção automática ao Caderno-Base.  
**Período dos pagamentos:** 01/01/2026 a 18/09/2026.  
**Geografia:** São Borja/RS.  
**Fonte de pagamentos:** Portal da Transparência da Prefeitura Municipal de São Borja.  
**Fonte cadastral:** Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08.  
**Unidade:** R$ pagos e percentuais calculados.

## 1. Correção de estado da fonte RFB

O controle estrutural RFB 2026-08 está **reconciliado**:

- 7.306 estabelecimentos ativos;
- 6.881 matrizes locais;
- 102 filiais de matriz local;
- 323 filiais de matriz externa.

A divergência anterior com 6.906/284 decorreu da mistura com o universo separado de Entidades Empresariais.

Permanece uma limitação distinta: os arquivos usados no enriquecimento dos credores foram transportados por espelho da mesma competência devido a indisponibilidade do host oficial naquela execução. A estrutura do snapshot está reconciliada com a linhagem canônica, mas o subconjunto de credores ainda deve ter sua proveniência/linhagem validada CNPJ a CNPJ antes de promoção editorial definitiva.

## 2. Universo analítico

CORE_PROCUREMENT: **R$ 72.039.491,18** pagos em rubricas compatíveis com aquisição/contratação.

Primeira ordem cadastral:

- presença local ampliada: **74.87%**;
- credores sem footprint ativo local: **25.13%**.

Esses percentuais não são taxas finais de retenção/vazamento.

## 3. O agregado é sensível a grandes arranjos institucionais

A Fundação Ivan Goulart concentra R$ 28,343 milhões do core.

Sensibilidade sem a Fundação:

- presença local ampliada: **58.57%**;
- externo sem footprint: **41.43%**.

**Interpretação:** o agregado integral superestima a generalidade da ancoragem local se for lido sem separar grandes serviços institucionais.

## 4. O principal resultado é a heterogeneidade por tipo de gasto

### Serviços PJ genéricos

- total: **R$ 51.041 milhões**;
- presença local ampliada: **91.22%**;
- externo sem footprint: **8.78%**.

Mesmo sem a Fundação, o bloco de serviços genéricos continua majoritariamente ancorado localmente no teste já calculado.

### Bens, materiais e equipamentos

- total: **R$ 16.763 milhões**;
- presença local ampliada: **25.90%**;
- externo sem footprint: **74.09%**;
- valor externo sem footprint: **R$ 12.420 milhões**.

Este é o maior bloco com evidência de contestabilidade extralocal nas aquisições de bens.

### Núcleo sem serviços PJ genéricos

- denominador: **R$ 20.999 milhões**;
- presença local ampliada: **35.12%**;
- externo sem footprint: **64.88%**.

A diferença mostra que “compras públicas” não devem ser tratadas como mercado territorial homogêneo.

## 5. Ranking por rubrica — valor pago a credores sem footprint local

| Rubrica | Total (R$ mi) | Externo sem footprint (R$ mi) | Externo (%) | Prioridade analítica |
|---|---:|---:|---:|---|
| MATERIAL DE CONSUMO | 9.327 | 5.965 | 63.95% | ALTA |
| MATERIAL, BEM OU SERVIÇO PARA DIST. GRATUITA | 4.139 | 3.620 | 87.47% | ALTA |
| OUTROS SERVIÇOS DE TERCEIROS - PESSOA JURÍDICA | 49.725 | 3.163 | 6.36% | ALTA |
| EQUIPAMENTOS E MATERIAL PERMANENTE | 3.297 | 2.835 | 86.00% | ALTA |
| OUTROS SERVIÇOS DE TERCEIROS PESSOA JURÍDICA | 1.316 | 1.316 | 100.00% | MEDIA_ALTA |
| SERVIÇOS DE TECNOLOGIA DA INFORMAÇÃO E COMUNICAÇÃO | 1.137 | 0.754 | 66.37% | MEDIA_ALTA |
| OBRAS E INSTALAÇÕES | 2.857 | 0.236 | 8.25% | MEDIA |
| SERVIÇOS DE CONSULTORIA | 0.156 | 0.140 | 89.74% | MEDIA |
| PASSAGENS E DESPESAS COM LOCOMOÇÃO | 0.086 | 0.074 | 85.87% | BAIXA |

**Prioridade analítica** é uma classificação SBMI baseada no valor externo observado; não significa que a demanda seja automaticamente substituível por fornecedores locais.

## 6. Geografia da parcela externa

Dos pagamentos a credores sem footprint ativo local, **60.87%** estão no próprio RS.

Principais UFs externas ao footprint local:

- RS: R$ 11.020 mi = 60.87% da parcela externa;
- SC: R$ 2.026 mi = 11.19% da parcela externa;
- PR: R$ 1.739 mi = 9.60% da parcela externa;
- DF: R$ 1.363 mi = 7.53% da parcela externa;
- SP: R$ 0.949 mi = 5.24% da parcela externa;

Principais municípios cadastrais externos:

- PORTO ALEGRE/RS: R$ 1.468 mi;
- CURITIBA/PR: R$ 1.393 mi;
- BRASILIA/DF: R$ 1.363 mi;
- PINHALZINHO/SC: R$ 1.223 mi;
- SANTO ANTONIO DAS MISSOES/RS: R$ 1.079 mi;
- PASSO FUNDO/RS: R$ 0.975 mi;
- NOVO CABRAIS/RS: R$ 0.838 mi;
- VENANCIO AIRES/RS: R$ 0.794 mi;
- SANTA MARIA/RS: R$ 0.763 mi;
- BARUERI/SP: R$ 0.702 mi;

### Interpretação

A competição pelo fornecimento público não é predominantemente “São Borja versus outros estados”. A maior parte do valor externo cadastrado permanece dentro do Rio Grande do Sul, indicando competição intermunicipal e redes regionais de fornecimento.

## 7. Implicações por mercado

### Bens essenciais

Material de consumo apresenta exposição externa relevante. Antes de recomendar substituição local, é necessário abrir itens de maior valor e verificar preço, escala, distribuição, habilitação e disponibilidade.

### Saúde/Higiene

O agregado de Saúde é fortemente ancorado pelo HIG, mas as aquisições de medicamentos, equipamentos e materiais podem permanecer externas. A estrutura é bifurcada: **prestação local de serviços versus cadeia externa de produtos**.

### Bens não essenciais

Equipamentos e material permanente apresentam exposição externa muito elevada, constituindo sinal B2G de demanda contestada por fornecedores extralocais. É necessário cruzar os itens com a oferta empresarial local antes de classificar isso como lacuna de mercado.

### Alimentação/Serviços

Serviços presenciais e obras mostram maior ancoragem local de primeira ordem. Serviços especializados — TIC, consultoria e passagens — mostram padrão mais externo, coerente com maior escala, especialização ou prestação remota.

## 8. Diagnóstico

**Dado observado/calculado:** a primeira rodada da despesa pública possui padrões territoriais radicalmente distintos conforme a natureza da aquisição.

**Interpretação:** o mecanismo territorial mais promissor para análise não é uma taxa agregada de “retenção”, mas uma matriz:

**tipo de compra × disponibilidade local × escala/habilitação × geografia do fornecedor × cadeia subsequente**.

**Hipótese a testar:** parte dos R$ 12.420 milhões externos em bens/materiais/equipamentos pode representar espaço contestável para empresas locais ou regionais com presença em São Borja. A proporção efetivamente contestável ainda não é conhecida.

## 9. Próxima investigação dirigida

Em vez de ampliar novas bases, o próximo passo de alto valor é abrir os **maiores itens/objetos** das rubricas com exposição externa alta e classificar cada um em:

1. oferta local existente;
2. oferta local potencial, mas sem escala/habilitação conhecida;
3. ausência plausível de oferta local;
4. aquisição estruturalmente externa/especializada.

Isso permitirá converter “exposição externa” em uma análise de **contestabilidade de mercado** sem confundi-la com vazamento econômico.
