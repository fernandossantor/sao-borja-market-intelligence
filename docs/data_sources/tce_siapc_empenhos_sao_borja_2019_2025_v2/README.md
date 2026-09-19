# TCE-RS/SIAPC — despesa orçamentária por empenhos — São Borja — 2019–2025 — v2

**Fonte observada:** Tribunal de Contas do Estado do Rio Grande do Sul — Dados Abertos SIAPC — conjunto anual consolidado “Despesa orçamentária por empenhos”.
**Órgão filtrado:** PM DE SÃO BORJA, código TCE-RS 58000.
**Período:** 2019–2025.
**Unidade:** R$ correntes/nominais.
**Rota oficial:** arquivos anuais consolidados `empenhos/<ano>.csv.7z` (fallback ZIP), processados em streaming e filtrados por órgão.

O TCE-RS descreve essa base como contendo empenhos do exercício, liquidações e pagamentos, inclusive liquidações/pagamentos relacionados a empenhos de exercícios anteriores. Os dados são oriundos do SIAPC e, segundo o próprio TCE-RS, não foram analisados pelo Tribunal, sendo de responsabilidade das entidades remetentes.

A camada persistida NÃO contém linhas de credores pessoa física, nomes de credores ou CPFs. Para CNPJ, persiste apenas agregado anual por documento empresarial válido, necessário para análises territoriais futuras.

CPF/CNPJ são classificados somente quando os dígitos verificadores validam após restauração de zeros à esquerda. Documentos inválidos, sintéticos, ausentes ou ambíguos permanecem em agregado separado.

A comparação com SICONFI/DCA é controle conceitual, não teste de igualdade. A base de empenhos do TCE inclui operações relacionadas a empenhos de exercícios anteriores; o DCA possui escopo contábil próprio. Diferenças devem ser explicadas antes de qualquer fusão.

**Não interpretar credor como fornecedor mercantil**, nem todo pagamento a CNPJ como compra/contratação.
