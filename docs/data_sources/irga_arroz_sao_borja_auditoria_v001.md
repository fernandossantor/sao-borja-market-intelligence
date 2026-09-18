# IRGA — cadeia do arroz em São Borja — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — fonte complementar oficial  
**Branch:** explore/receita-estadual-rs-market-intel-v1

## Objetivo

Documentar a fonte oficial de produção física de arroz usada no piloto do Radar do Mercado para São Borja.

O IRGA será usado como fonte de **capacidade produtiva primária municipal**, não como substituto dos indicadores fiscais do Radar.

## Fonte 1 — Produtividades Municipais Safra 2023/2024

Órgão: Instituto Rio Grandense do Arroz — IRGA.

Arquivo oficial:
https://admin.irga.rs.gov.br/upload/arquivos/202407/19142636-produtividades-municipais-safra-2023-24.pdf

Geografia: município de São Borja.

Unidades:
- hectares;
- kg/ha;
- toneladas.

Valores de São Borja:
- área semeada: 31.166 ha;
- área perdida: 2.014 ha;
- área colhida: 29.152 ha;
- produtividade: 8.129 kg/ha;
- produção: 236.977 t.

O documento também registra o total do NATE São Borja:
- 31.636 ha semeados;
- 2.014 ha perdidos;
- 29.622 ha colhidos;
- 8.128 kg/ha;
- 240.765 t.

**Controle:** não confundir total do NATE com município de São Borja. O NATE agrega também Itacurubi nessa tabela.

## Fonte 2 — Encerramento da safra 2024/2025

Órgãos: IRGA / Secretaria da Agricultura, Pecuária, Produção Sustentável e Irrigação do RS.

Publicação: 13/06/2025.

URL:
https://www.agricultura.rs.gov.br/encerrada-a-colheita-do-arroz-no-rio-grande-do-sul

Valor para São Borja:
- produção: 306.703,95 t.

Posições:
- 8º maior produtor do Rio Grande do Sul;
- 4º maior produtor da Fronteira Oeste, atrás de Uruguaiana, Itaqui e Alegrete.

A notícia informa que os dados detalhados de área, produtividade e perdas da safra 2024/2025 ainda estavam sendo finalizados para o relatório final. Assim, nesta auditoria a produção/ranking são tratados como observados; não se inventam área ou produtividade municipal para essa safra.

## Cálculo SBMI

Variação de produção:

((306.703,95 / 236.977) - 1) × 100 = 29,42%

Classificação:
**DADO CALCULADO**.

Período:
safra 2023/2024 → safra 2024/2025.

Limitação:
a variação de produção não identifica isoladamente efeitos de área, produtividade, clima, preço, crédito ou decisões de plantio.

## Comparação com IBGE/PAM

A camada canônica v028 registra para o arroz em 2024, via IBGE/SIDRA PAM 5457:
- área colhida: 29.152 ha;
- produtividade: 8.129 kg/ha;
- produção: 236.977 t.

Esses valores coincidem com a safra 2023/2024 publicada pelo IRGA para São Borja, oferecendo uma validação cruzada útil da base física.

A PAM acrescenta valor bruto da produção e preço implícito derivado, mas:
- valor bruto da produção ≠ VAB;
- preço implícito derivado ≠ cotação de mercado.

## Uso no piloto do Radar

Camada IRGA/IBGE:
**capacidade produtiva física municipal**.

Camada RAIS/RFB:
**capacidade agroindustrial e emprego local**.

Camada Radar:
**demanda, origem da oferta, concorrência, dependência externa e mercados no RS**.

A integração correta é:

capacidade municipal observada + estrutura agroindustrial local + oportunidade/fluxo estadual do Radar

e não:

produção municipal = demanda municipal.

## Limitações

- safra e ano-calendário podem usar referências temporais diferentes;
- produção física não mede faturamento, valor adicionado ou market share;
- ranking produtivo não mede competitividade completa;
- dados do Radar permanecem necessários para avaliar mercado, fluxos e concorrência.
