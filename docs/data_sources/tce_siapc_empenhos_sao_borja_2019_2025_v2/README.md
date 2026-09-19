# TCE-RS/SIAPC — tentativa de extração consolidada — São Borja — 2019–2025 — v2

> **STATUS: EXTRAÇÃO NÃO MATERIALIZADA. NÃO USAR COMO SÉRIE HISTÓRICA DE CREDORES.**

**Fonte pretendida:** Tribunal de Contas do Estado do Rio Grande do Sul — Dados Abertos SIAPC — conjunto anual consolidado “Despesa orçamentária por empenhos”.

**Órgão-alvo:** PM DE SÃO BORJA, código TCE-RS 58000.

**Período pretendido:** 2019–2025.

O workflow que produziu esta pasta terminou com estado GitHub `success`, porém isso ocorreu porque a rotina permitia continuar mesmo quando os downloads falhavam. Os arquivos desta pasta demonstram que **nenhum dado anual foi efetivamente obtido**:

- `source_manifest.tsv`: 2019–2025 = `FAILED`, bytes = 0;
- `yearly_payment_aggregate.csv`: todos os anos = `NO_SUMMARY`;
- `schema_inventory.csv`: vazio;
- `cnpj_payments_2019_2025.csv`: somente cabeçalho.

Portanto, esta pasta é **evidência diagnóstica de uma tentativa malsucedida**, e não um produto de dados.

A auditoria de rede posterior confirmou que `dados.tce.rs.gov.br` resolve por DNS, mas as conexões TCP a partir do GitHub Actions expiram tanto na porta 443 quanto na porta 80. Ver:

- `docs/data_sources/tce_host_network_diagnostic/network.txt`;
- `docs/data_sources/tce_siapc_empenhos_transport_closure_2019_2025.md`.

A fonte oficial não foi considerada ausente. O impedimento identificado é de transporte/acessibilidade no ambiente de execução.

A metodologia de reabertura foi preparada em:

`.github/workflows/tce-siapc-empenhos-per-organ-parallel-2019-2025.yml`.

Não persistir ou inferir números históricos de credores a partir desta pasta.
