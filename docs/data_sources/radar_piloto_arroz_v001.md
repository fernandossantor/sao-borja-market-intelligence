# Radar do Mercado — piloto Arroz / São Borja

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Criar o primeiro piloto controlado de cruzamento entre:

`oportunidade estadual por NCM → cadeia produtiva local → capacidade territorial → hipótese mercadológica`

sem converter demanda estadual em demanda municipal.

## Justificativa territorial

O Caderno Setorial de Bens Essenciais registra, com base em documentação municipal/Emater já incorporada ao projeto, forte presença histórica de **arroz** na base agropecuária de São Borja.

Essa evidência é suficiente para selecionar a cadeia como **piloto de auditoria**, mas não prova, por si só:
- capacidade industrial corrente;
- volume atual de beneficiamento;
- participação de São Borja na oferta estadual;
- viabilidade de expansão.

Esses pontos deverão ser verificados em bases canônicas do SBMI e, quando possível, no próprio Radar.

## Correspondência CNAE — fonte oficial CONCLA/IBGE

### Elo primário

**0111-3/01 — Cultivo de arroz**

A busca oficial da CONCLA associa a subclasse ao cultivo de arroz e ao beneficiamento quando atividade complementar ao cultivo.

### Elo industrial principal

**1061-9/01 — Beneficiamento de arroz**

A CONCLA/IBGE informa que compreende:
- arroz descascado;
- moído;
- branqueado;
- polido;
- parboilizado;
- convertido.

### Elo industrial derivado

**1061-9/02 — Fabricação de produtos do arroz**

Compreende, entre outros:
- farinha de arroz;
- flocos;
- outros produtos de arroz.

## Cesta piloto de NCM

Fonte de classificação: Sumário Executivo de Arroz do Ministério da Agricultura e Pecuária, referência 2026, e tabela NCM vigente/CLASSIF da Receita Federal.

### Arroz descascado

- `10062010` — arroz descascado (cargo/castanho), parboilizado;
- `10062020` — arroz descascado (cargo/castanho), não parboilizado.

### Arroz semibranqueado ou branqueado

- `10063011` — parboilizado, polido ou brunido;
- `10063019` — outros, parboilizados;
- `10063021` — não parboilizado, polido ou brunido;
- `10063029` — outros, não parboilizados.

### Subproduto

- `10064000` — arroz quebrado.

## Variáveis a buscar no Radar para cada NCM

1. demanda financeira no RS;
2. participação da produção interna do RS;
3. participação/valor de entradas de outras UFs;
4. participação/valor de importações;
5. classificação de dependência externa, se disponível;
6. variação temporal, se o painel permitir;
7. localização municipal da produção, se a versão atual mantiver esse visual;
8. principais mercados consumidores/destinos, quando disponível;
9. principais concorrentes, quando disponível.

## Variáveis locais a cruzar no SBMI

Para São Borja, usar apenas bases já auditadas ou que venham a ser auditadas:

- CNPJ/CNAE local;
- emprego formal;
- VAF/IPM, quando compatível;
- produção agropecuária oficial;
- localização de estabelecimentos industriais;
- evidência documental de operadores da cadeia.

## Estrutura analítica

Para cada NCM:

`demanda_RS → oferta_RS → OUF → importação → dependência → capacidade_local → hipótese`

Exemplo de interpretação permitida:

> “O produto X apresenta dependência externa relevante no mercado gaúcho. São Borja possui evidência de atividade produtiva relacionada à cadeia do arroz. Isso justifica investigar capacidade, escala, logística e acesso ao mercado estadual.”

Interpretação não permitida sem dado adicional:

> “São Borja possui mercado não atendido de R$ X.”

## Limitações

- a demanda do Radar é estadual;
- CNAE e NCM descrevem dimensões diferentes;
- presença de CNAE não mede capacidade instalada;
- produção agrícola não implica beneficiamento industrial local;
- dependência externa estadual não garante vantagem competitiva em São Borja;
- custos logísticos, escala, produtividade e contratos não estão automaticamente resolvidos pelo Radar.

## Próxima etapa

Preencher a matriz piloto com os valores do Radar quando a leitura confiável do Power BI for possível ou quando os mesmos indicadores aparecerem em documentação pública verificável.

Até lá, a tabela permanece como **esqueleto auditável**, sem preenchimento numérico especulativo.
