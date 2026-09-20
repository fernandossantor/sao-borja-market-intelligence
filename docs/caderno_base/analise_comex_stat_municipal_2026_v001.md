# Comex Stat municipal — comércio exterior domiciliado em São Borja — jan–ago/2026 — v001

**Fonte:** MDIC/SECEX — API oficial Comex Stat, módulo municipal `/cities`  
**Período:** janeiro a agosto de 2026  
**Geografia:** São Borja/RS — código IBGE 4318002  
**Unidades:** US$ FOB e kg  
**Status:** dado municipal oficial reproduzido; candidato à incorporação no sucessor do Caderno-Base.

## 1. Controle conceitual

O módulo municipal do Comex Stat identifica o **domicílio fiscal da empresa declarante**.

Portanto:

- exportação domiciliada em São Borja **não prova origem física municipal da mercadoria**;
- importação domiciliada em São Borja **não prova destino final municipal da mercadoria**;
- o saldo não mede renda líquida retida no território;
- não usar os dados como proxy direto de produção, consumo ou market share local.

Esse controle é central para toda interpretação.

## 2. Totais jan–ago/2026

Dados observados na API:

### Exportações
- **US$ 9.848.096 FOB**;
- **32.151.627 kg**.

### Importações
- **US$ 6.514.628 FOB**;
- **17.497.000 kg**.

### Saldo calculado do módulo municipal

`US$ 9.848.096 - US$ 6.514.628 = US$ 3.333.468`.

Saldo físico:

`32.151.627 - 17.497.000 = 14.654.627 kg`.

Esses saldos são do recorte por domicílio fiscal, não “ganho líquido” de São Borja.

## 3. Estrutura das exportações

A extração retornou quatro SH4 exportadores no período:

- SH4 1201 — soja;
- SH4 1005 — milho;
- SH4 1006 — arroz;
- SH4 1001 — trigo.

Valores FOB agregados:

- soja: **US$ 4.072.934 = 41,36%**;
- milho: **US$ 4.786.899 = 48,61%**;
- arroz: **US$ 952.735 = 9,67%**;
- trigo: **US$ 35.528 = 0,36%**.

As quatro rubricas somam 100% do valor exportado observado na resposta municipal do período.

### Interpretação

O comércio exterior domiciliado em São Borja no período é fortemente concentrado em commodities agropecuárias.

Isso é compatível com a estrutura produtiva/agroindustrial documentada no Caderno-Base, mas não prova que toda mercadoria tenha sido produzida no município.

## 4. Arroz — exportações

SH4 1006:

- Estados Unidos: **US$ 899.977 / 1.152.477 kg**;
- Nicarágua: **US$ 38.775 / 77.400 kg**;
- Cuba: **US$ 13.983 / 51.600 kg**.

Total calculado:
- **US$ 952.735 FOB**;
- **1.281.477 kg**.

O arroz representa:

`952.735 / 9.848.096 × 100 = 9,67%`

das exportações FOB domiciliadas no período.

## 5. Arroz — importações

SH4 1006:

- Uruguai: **US$ 6.033.956 / 15.942.000 kg**;
- Argentina: **US$ 280.420 / 584.000 kg**;
- Paraguai: **US$ 103.120 / 708.000 kg**.

Total:
- **US$ 6.417.496 FOB**;
- **17.234.000 kg**.

Participação do arroz nas importações:

`6.417.496 / 6.514.628 × 100 = 98,51%`.

Em massa:

`17.234.000 / 17.497.000 × 100 = 98,50%`.

### Uruguai dentro das importações de arroz

Valor:

`6.033.956 / 6.417.496 × 100 = 94,02%`.

Massa:

`15.942.000 / 17.234.000 × 100 = 92,50%`.

**Dado calculado:** as importações domiciliadas de arroz são fortemente concentradas no Uruguai.

## 6. O aparente paradoxo do arroz

São Borja possui:
- produção primária material;
- beneficiamento local fortemente documentado;
- exportações domiciliadas de arroz;
- e, simultaneamente, importações domiciliadas de arroz muito superiores às exportações do mesmo SH4 no período.

Saldo do SH4 1006:

- FOB: `US$ 952.735 - US$ 6.417.496 = -US$ 5.464.761`;
- massa: `1.281.477 - 17.234.000 = -15.952.523 kg`.

### Interpretação permitida

O resultado demonstra **integração comercial transfronteiriça relevante da cadeia do arroz por empresas fiscalmente domiciliadas em São Borja**.

Ele pode refletir:
- abastecimento de agroindústrias/comerciantes;
- complementaridade de origem;
- operações de trading;
- composição varietal ou industrial;
- arbitragem comercial;
- fluxos para posterior distribuição.

### Não concluir

Não é possível afirmar, apenas com o Comex Stat, que:
- São Borja “não produz arroz suficiente”;
- as importações são consumidas localmente;
- todo arroz importado é beneficiado em São Borja;
- existe substituição causal da produção local por produto estrangeiro;
- o saldo negativo do arroz representa vazamento econômico.

Para responder isso são necessários dados de empresa, produto/NCM 8 dígitos, destino físico, processamento e vendas.

## 7. Demais importações

Além do arroz, aparecem valores pequenos de:
- cebolas/alhos e outros aliáceos frescos — Argentina;
- cereais SH4 1008 — Estados Unidos;
- equipamento térmico SH4 8419 — Argentina;
- instrumentos/aparelhos médicos SH4 9018 — China.

Somadas, essas rubricas representam apenas cerca de **1,49%** do valor importado no período.

## 8. Geografia comercial

### Exportações

Principais destinos em valor:
- China — soja;
- Egito — milho;
- Estados Unidos — arroz;
- Malásia, Filipinas e Vietnã — milho.

### Importações

No total importado, o Uruguai responde por:

`US$ 6.033.956 / US$ 6.514.628 × 100 = 92,62%`.

Quase toda essa participação corresponde ao arroz.

### Interpretação

A fronteira econômica de São Borja não se limita à travessia física da ponte: empresas domiciliadas no município participam de fluxos comerciais internacionais amplos, com forte componente regional do Mercosul nas importações e mercados extrarregionais nas exportações.

A frase descreve o domicílio fiscal do comércio exterior, não a rota física de cada carga.

## 9. Relação com Radar do Mercado

Os dois bancos respondem perguntas distintas.

### Radar da Receita Estadual
- abrangência RS;
- composição de mercado;
- INT, OUF e EXT;
- estrutura estadual de abastecimento por NCM.

### Comex Stat municipal
- domicílio fiscal da empresa;
- exportações/importações internacionais;
- país;
- SH4;
- FOB e kg.

Portanto:

`Radar EXT ≠ importação Comex de São Borja`.

Os dados podem ser combinados analiticamente, mas não somados ou comparados como se medissem o mesmo universo.

## 10. Implicação editorial

### Caderno-Base

Promover:
- totais municipais jan–ago/2026;
- estrutura agro das exportações;
- concentração das importações em arroz;
- controle de domicílio fiscal;
- geografia internacional.

### Comércio de bens essenciais

O arroz pode entrar como **contexto da cadeia de abastecimento**, não como medida do mercado varejista local.

### Diagnóstico territorial

A combinação:
- produção local;
- beneficiamento;
- importação;
- exportação;
- fluxo fronteiriço;

mostra que o município exerce funções simultâneas de produção, processamento e intermediação comercial.

A intensidade relativa de cada função ainda precisa ser medida com dados de destino/processamento.

## 11. Artefatos

- `docs/data_sources/comex_municipal_sao_borja_2026/run_summary.json`;
- `docs/data_sources/comex_municipal_sao_borja_2026/comex_2026_sao_borja_totals_ytd.csv`;
- `docs/data_sources/comex_municipal_sao_borja_2026/comex_2026_sao_borja_sh4_pais_ytd.csv`;
- `docs/data_sources/comex_municipal_sao_borja_2026/comex_2026_sao_borja_sh4_pais_mes_aggregated.csv`;
- `docs/data_sources/comex_sao_borja_2026_summary_v001.csv`.

## 12. Governança

- v028 permanece **read-only**;
- promoção apenas ao sucessor;
- PR #41 permanece **aberto, draft e sem merge**.
