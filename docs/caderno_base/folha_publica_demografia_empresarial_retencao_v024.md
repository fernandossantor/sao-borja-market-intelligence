# Caderno-Base Territorial v024 — folha pública, demografia empresarial e retenção financeira

Data da atualização: 2026-09-12.

## Objetivo

A v024 aprofunda a leitura dos circuitos de renda de São Borja sem fundir produção, salários, benefícios e ativos financeiros em uma única grandeza. Esta camada incorpora: (a) folha pública federal civil diretamente territorializada; (b) folha ativa do Poder Executivo estadual; (c) primeiro snapshot oficial municipal do Mapa de Empresas; e (d) estado metodológico das fontes ESTBAN e SICOR/MDCR para a investigação de retenção financeira.

## Folha federal civil — observado, parcial

Fonte: Portal da Transparência/CGU — dados abertos de Servidores SIAPE, competência 2026-07.

Regra territorial: UORG de exercício/lotação auditada e reconciliada por unidade local. O subtotal preferencial foi deduplicado entre as regras verificadas.

| Unidade/regra | IDs únicos | Remuneração básica bruta (R$) |
|---|---:|---:|
| IFFar Campus São Borja — exercício local | 123 | 1.728.965,44 |
| Unipampa Campus São Borja — subunidades CAMPSB | 103 | 1.674.998,72 |
| MAPA/Vigiagro São Borja | 13 | 214.362,77 |
| INSS — APS São Borja | 7 | 80.712,43 |
| RFB — Inspetoria São Borja | 1 | 49.354,49 |
| **Subtotal civil federal verificado** | **247** | **3.748.393,85** |

Há 246 identificadores com registro de remuneração no subtotal. A natureza do dado é **observada**, agregada a partir de registros administrativos.

### Limitações federais

O subtotal não é exaustivo. A base de militares da CGU não oferece UORG/UF territorial suficiente para identificar as unidades militares de São Borja. PF/PRF apresentam campos territoriais/UORG sigilosos ou codificados, impedindo municipalização segura. Nenhum valor foi imputado por médias nacionais ou por simples presença institucional.

## Poder Executivo estadual — observado

Fonte: Portal da Transparência do Estado do Rio Grande do Sul — Dados Abertos — Pessoal do Poder Executivo (Gov-RS), competência 2026-07.

Filtro: `Municipio=SAO BORJA` e `Situacao=ATIVO`.

Resultado observado: **877 vínculos ativos**, **R$ 5.526.530,07 de remuneração bruta** e **R$ 4.291.259,62 de remuneração líquida**.

| Órgão | Vínculos ativos | Bruto (R$) |
|---|---:|---:|
| Secretaria da Educação | 663 | 3.410.016,55 |
| Secretaria de Sistemas Penal e Socioeducativo | 201 | 1.938.173,95 |
| UERGS | 8 | 147.442,40 |
| FGTAS | 3 | 15.473,53 |
| IRGA | 2 | 15.423,64 |

Dados calculados: Educação = **61,70%** do bruto; Penal/Socioeducativo = **35,07%**; juntas = **96,77%**.

Limitação: o arquivo cobre o Poder Executivo estadual. Judiciário, MPRS, Defensoria, TCE e Legislativo permanecem fora deste subtotal. O município da folha é localização administrativa e não comprova residência do trabalhador.

## Subtotal público não municipal diretamente auditado

Fórmula:

`subtotal = federal civil verificado + Executivo estadual ativo`

`R$ 3.748.393,85 + R$ 5.526.530,07 = R$ 9.274.923,92/mês`

Classificação: **dado calculado — ordem de grandeza, não total consolidado**.

Comparações apenas contextuais:

- `9.274.923,92 / 23.940.059,71 = 38,74%` da massa empresarial RAIS de dezembro de 2025;
- `9.274.923,92 / 24.535.168,54 = 37,80%` dos créditos INSS/SUIBE de julho de 2026.

Essas razões não são participações da renda municipal. Os fluxos possuem universos, períodos e conceitos distintos e não são aditivos.

## Interpretação — folha pública

A evidência fortalece a leitura da folha pública não municipal como **âncora material de circulação de renda**. Mesmo antes de incluir Forças Armadas, PF/PRF, outros órgãos federais não reconciliados e outros Poderes estaduais, o subtotal diretamente auditado já supera R$ 9,27 milhões mensais em remuneração bruta.

A hipótese de função **anticíclica** permanece não testada. Seria necessário construir série temporal e comparar sua estabilidade com ciclos do agro, emprego privado, VAF/IPM e demais indicadores, sem converter correlação em causalidade.

## Demografia empresarial — Mapa de Empresas

Fonte: MEMP/DREI — Mapa de Empresas — dados abertos, referência 31/05/2026.

Dados observados para São Borja:

- empresas abertas: **82**;
- empresas fechadas: **44**;
- empresas ativas: **6.950**.

Dados calculados pelo SBMI:

- saldo mensal = `82 - 44 = +38`;
- aberturas / estoque ativo final = `82 / 6.950 = 1,18%`;
- fechamentos / estoque ativo final = `44 / 6.950 = 0,63%`;
- rotatividade bruta proxy = `(82 + 44) / 6.950 = 1,81%`.

Os três percentuais são **proxies operacionais**, não taxas oficiais. Um mês não permite classificar a rotatividade de São Borja como alta ou baixa, nem medir mortalidade empresarial de coortes. A hipótese de “churn elevado” permanece **não verificada** até existir série e benchmark territorial compatível.

## Retenção financeira — ESTBAN e SICOR/MDCR

**ESTBAN/BCB** foi confirmado como fonte oficial para depósitos, crédito e outras posições bancárias municipais. Seu uso será contextual: observar a evolução da intermediação financeira de São Borja, sem atribuir automaticamente os saldos ao agro.

**SICOR/MDCR/BCB** teve o catálogo oficial auditado e contém recursos de contratos por município, além de recortes de custeio e investimento por município/produto. A extração municipal ainda não foi canonizada.

Controle metodológico: depósitos não identificam origem setorial; crédito rural é financiamento, não lucro; saldos bancários não identificam beneficiário econômico final; e associação temporal entre VAB agro e variáveis financeiras não comprova causalidade.

## Modelo integrado de circuitos de renda

A leitura corrente separa pelo menos seis circuitos: geração de valor agropecuário/agroindustrial; salários privados; salários públicos não municipais; previdência/assistência; renda empresarial/patrimonial; e crédito/intermediação financeira. Esses circuitos não devem ser somados mecanicamente e possuem mecanismos distintos de retenção territorial.

## Estado das hipóteses

- peso material da folha pública não municipal na circulação local: **fortemente sustentado, ainda com cobertura incompleta**;
- caráter anticíclico da folha pública: **plausível, não testado**;
- elevada rotatividade empresarial: **não verificada; primeiro snapshot oficial incorporado**;
- excedente agro majoritariamente aplicado fora do município: **não verificado**;
- ESTBAN/SICOR como caminho para aprofundar retenção financeira: **confirmado metodologicamente; extração municipal ainda pendente**.

## Rastreabilidade

Planilha Drive: `1Gp_Cj1b9JiJkGk0M9TBRYcRHTlvSsRs03k_3501KHkI`.

Documento narrativo Drive: `1Fe8WxLqvu_wN0VHpEGnSBkhje17VAapuB0boxZ6v2h4`.

Registro metodológico Drive: `1CTnvoyJLJqiFFbh8bbnTBAnrMXrtTVDOdr1C94vm_vc`.

Abas v024: `Folha_publica_auditada_v024`, `Demografia_empresarial_v024`, `Retencao_financeira_v024`, `Auditoria_v024`.

## Governança

O PR #41 deve permanecer **aberto, draft e sem merge** até autorização explícita do usuário.
