# Caderno Setorial — Comércio de Bens Essenciais — v001

## Estado

Planilha:
`caderno_setorial_bens_essenciais_v001_20260910`

Drive:
`13k3iYvb9kXNgDBWE2zZykHnO4u4idrXsYjo40-TXgUA`

Documento:
`1QSk2VU5eVGdP2H42fLaKCIJP5Nq4E0P54C768AGgKvY`

Pasta:
`13_rnLtVC4e7ga2lTTMuRAqETr7AkElln`

Status: **diagnóstico setorial v001 validado**.

## Demanda modelada

Fonte-base: IBGE/POF 2017–2018 — Rio Grande do Sul.

- alimentação no domicílio: R$ 487,00/família/mês;
- tamanho familiar médio: 2,72;
- per capita: R$ 179,0441176471/mês;
- fator de preços 2018–jun/2026: 1,781742384675;
- per capita atualizado: R$ 319,010493/mês;
- população 2025: 61.311.

Fórmula:

`61.311 × (487 / 2,72) × 1,781742384675 × 12`

Resultado:
**R$ 234.706.228,14/ano**.

Natureza:
**ESTIMATIVA MODELADA**.

Não é faturamento observado nem mercado capturado.

## Oferta

Inventário POM:
- 138 linhas brutas;
- 135 nomes únicos.

Base corrente:
- 54 linhas de bens essenciais;
- 52 reconciliadas documentalmente com POM;
- 52 com CNPJ documental;
- 2 sem CNPJ documental.

**Controle:** 52/54 mede prontidão/reconciliação interna, não cobertura de mercado.

A oferta é classificada como **estrutural, não censitária**.

## Join operador × RFB

**DEPRIORIZADO.**

A estrutura municipal RFB já é canônica.

Retomar somente se uma pergunta decisória exigir granularidade por operador.

O join não resolve:
- market share;
- destino do gasto;
- retenção monetária;
- faturamento.

## Estrutura ampla do varejo

Divisão 47:
- 1.720 estabelecimentos;
- participação cadastral externa: 6,63%;
- emprego externo estimado: 37,46%;
- remuneração de dezembro externa estimada: 38,16%.

Amplificação emprego/cadastro:
**5,65x**.

Leitura:
estruturas externas têm peso funcional maior que sua incidência cadastral.

Controle:
G47 inclui varejo alimentar e não alimentar.

## POM 2026

Fonte:
`Report Final POM - Comércio de Bens Essenciais.pdf`.

Método:
12 entrevistas em profundidade; coleta 24/06/2026.

### Abastecimento
Indícios:
- preço;
- promoções;
- variedade;
- comparação entre estabelecimentos;
- maior disposição a deslocamento por economia/variedade.

### Reposição
Indícios:
- proximidade;
- disponibilidade;
- rapidez;
- compras de perecíveis e itens recorrentes.

### Digital
Instagram, WhatsApp e aplicativos próprios aparecem como canais de acompanhamento de promoções e planejamento.

### Fricções
- filas;
- poucos caixas;
- divergência de preço;
- organização;
- atendimento.

Self-checkout aparece positivamente entre entrevistados.

## REGIC

Não há tema diretamente equivalente ao varejo alimentar cotidiano.

**Decisão:** REGIC não é usada como proxy de demanda ou centralidade deste mercado.

## Diagnóstico

O mercado deve ser lido por missão:

1. **abastecimento/estoque** — preço, promoção, variedade;
2. **reposição** — proximidade, disponibilidade, rapidez.

O benchmark monetário oferece escala potencial, mas não permite repartir a demanda entre formatos ou empresas.

## Bloqueios

Market share:
**NÃO DISPONÍVEL**.

Retenção:
**NÃO DISPONÍVEL**.

Saturação:
**NÃO DISPONÍVEL**.

Proibido:
- demanda ÷ número de lojas;
- 1 − participação cadastral externa;
- tratar 54 linhas como universo econômico.

## Próxima pesquisa

Medir:

`gasto × missão × formato × canal × território`

incluindo:
- supermercado;
- atacarejo;
- mercado/minimercado;
- padaria;
- açougue;
- fruteira;
- e-commerce;
- outro município;
- Argentina.


## Padrão editorial e de fontes — aplicado em 2026-09-10

Regra de governança:
`docs/governance/padrao_editorial_cadernos.md`.

Todo caderno deve conter:
- **Sumario**;
- **Siglas**;
- **Origem_dados**;
- **Referencias_originais**;
- e, nos cadernos setoriais, **Respostas_analiticas**.

Os documentos narrativos recebem igualmente:
- sumário textual;
- lista de siglas e códigos;
- nota conceitual das fontes;
- síntese de respostas analíticas;
- referências oficiais ao final.

A origem deve identificar a operação estatística ou cadastro, e não apenas o órgão. Exemplo: **PIB dos Municípios — IBGE**, conforme metodologia integrada ao SCN/SCR e SNA 2008, em vez de apenas “PIB — IBGE”.

No escopo atual, pesquisa primária é **não operacional**. Perguntas sem base compatível tornam-se limites explícitos.


### Leitura prioritária

A aba `Respostas_analiticas` organiza o caderno em:
`pergunta → resposta sustentada → natureza → evidência → implicação → limite`.

Essa camada deve orientar a redação final: primeiro responder o que a base permite; depois registrar os limites.


## Guia de uso empresarial

O documento organiza o mercado por duas missões:
- **abastecimento/estoque**;
- **reposição/conveniência**.

Grandes formatos podem competir por preço, promoção, variedade e checkout.

Vizinhança e especializados podem competir por proximidade, rapidez, disponibilidade e qualidade.

O benchmark de **R$ 234.706.228,14/ano** é ESTIMATIVA MODELADA de alimentação no domicílio e não faturamento observado.
