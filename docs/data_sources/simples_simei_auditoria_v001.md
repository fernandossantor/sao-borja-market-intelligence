# Simples Nacional e SIMEI — auditoria de rota oficial — v001

**Status:** exploratório — não canônico  
**Data:** 18/09/2026  
**Geografia-alvo:** São Borja/RS

## 1. Problema

A matriz Fecomércio identifica como lacunas prioritárias:
- MEI;
- optantes do Simples Nacional;
- emprego segundo regime tributário do empregador.

A preferência metodológica do SBMI é reproduzir esses indicadores por fonte primária.

## 2. Rota oficial confirmada

O portal oficial **Estatísticas do Simples Nacional** está ativo em 2026.

Na consulta corrente, a página informa:
- ANO 2026;
- posição consolidada até **12/09/2026**.

Estatísticas SINAC disponíveis:
- Optantes por UF e Município;
- Optantes por CNAE, UF e Município;
- pedidos de opção;
- eventos de inclusão;
- eventos de exclusão.

Estatísticas SIMEI disponíveis:
- optantes por UF e Município;
- optantes por CNAE, UF e Município;
- total geral de MEI;
- enquadramento/desenquadramento.

Fonte:
https://www8.receita.fazenda.gov.br/SimplesNacional/Aplicacoes/ATBHE/estatisticasSinac.app/Default.aspx

## 3. Estado da extração

A interface exige seleção de UF/município em formulário.

No ambiente de auditoria atual:
- a existência da consulta municipal foi confirmada;
- a data de consolidação foi confirmada;
- o formulário não foi submetido de forma reproduzível para São Borja.

Consequência:
**nenhum valor SINAC/SIMEI municipal foi promovido ou aceito a partir dessa página nesta etapa.**

## 4. Dados Abertos CNPJ

A Receita Federal mantém o CNPJ em Dados Abertos e também um Painel de MEIs.

A estrutura pública dos dados CNPJ inclui historicamente um arquivo `Simples.zip`, com informações de opção pelo Simples/SIMEI, mas a competência 2026-08 ainda precisa ser obtida/reproduzida diretamente no ambiente do projeto antes de qualquer cálculo.

## 5. Cross-check existente

Cross-check secundário já registrado para agosto/2026:
- estabelecimentos ativos: 7.306;
- MEI ativos: 3.829;
- participação MEI: 52,41%.

O total de estabelecimentos ativos coincide exatamente com a base RFB v028:
`7.306 - 7.306 = 0`.

Mesmo assim:
- MEI permanece **não aceito**;
- Simples permanece **não aceito**;
- a concordância do estoque não valida campos adicionais.

## 6. RAIS e Simples

A RAIS 2024 de São Borja contém o campo bruto:
`Ind Estabelecimento Participante SIMPLES - Código`.

Contagens observadas:
- código 0: 10.087 vínculos;
- código 1: 3.038 vínculos.

O dicionário específico do microdado 0/1 não foi localizado.

Regra:
**não interpretar 0/1 como optante/não optante sem documentação oficial específica do arquivo.**

## 7. Plano de fechamento

Prioridade 1:
obter a estatística municipal oficial SINAC/SIMEI para São Borja, com data de consolidação.

Prioridade 2:
obter/processar `Simples.zip` da mesma competência dos CNPJs 2026-08, permitindo reprodução direta e eventual corte por estabelecimento/CNAE.

Prioridade 3:
somente depois avaliar o cruzamento regime tributário × emprego RAIS.

## 8. Critério de aceitação

O indicador só poderá mudar de lacuna para coberto quando houver:
- fonte oficial;
- competência;
- definição;
- denominador;
- código de reprodução ou tabela oficial;
- conciliação mínima com o estoque cadastral.

Até lá, a matriz deve permanecer:
- MEI: rota primária identificada, valor pendente;
- Simples: rota primária identificada, valor pendente.

## Retomada operacional — 18/09/2026

A rota oficial foi revalidada diretamente nas páginas de Estatísticas do Simples Nacional.

### Snapshots confirmados

SINAC — Optantes por UF e Município:
- ano: 2026;
- posição consolidada até **12/09/2026**.

SINAC — Optantes por CNAE, UF e município:
- ano: 2026;
- posição consolidada até **12/09/2026**.

SIMEI — Optantes por UF e Município:
- ano: 2026;
- posição consolidada até **12/09/2026**.

SIMEI — Eventos de enquadramento/desenquadramento:
- ano: 2026;
- posição consolidada exibida na página consultada: **18/09/2026**.

### Controle temporal

As páginas não possuem necessariamente o mesmo snapshot.

Regra:
**não combinar estoque de optantes em 12/09/2026 com eventos consolidados em 18/09/2026 como se fossem uma única fotografia temporal sem explicitar as datas.**

### Estado de São Borja

A granularidade municipal e a opção de consulta por CNAE estão confirmadas.

O formulário ainda não foi submetido de forma reproduzível para São Borja no ambiente atual.

Portanto:
- valor oficial de optantes do Simples em São Borja: PENDENTE;
- valor oficial de MEI/SIMEI em São Borja: PENDENTE;
- valor por CNAE: PENDENTE;
- cross-check secundário de 3.829 MEI permanece **não aceito**.

A lacuna continua operacional, não conceitual.
