# São Borja — SICONFI/DCA — contas públicas 2019–2025

**Fonte:** Tesouro Nacional — SICONFI, API de Dados Abertos.
**Abrangência:** município de São Borja/RS, código IBGE 4318002.
**Período:** exercícios anuais de 2019 a 2025.
**Anexos coletados:** DCA Anexo I-C (receitas orçamentárias), I-D (despesas
por natureza) e I-E (despesas por função).

Esta camada preserva as linhas observadas e um dicionário temporal antes da
construção da série reconciliada. O arquivo `candidate_series_rows.csv` é
apenas uma triagem por palavras-chave; ele não redefine as contas oficiais.

2026 não é tratado como DCA anual fechada. A execução corrente permanece em
camada separada (Portal PMSB/RREO quando metodologicamente comparável).

Próximo passo: reconciliar contas e colunas por exercício e então calcular,
com fórmulas explícitas, receita corrente, transferências correntes,
FPM/ICMS/Fundeb/IPVA/ITR, empenhado/liquidado/pago, pessoal/previdência,
juros/dívida e investimentos.
