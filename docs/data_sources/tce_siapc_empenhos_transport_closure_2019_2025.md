# TCE-RS/SIAPC — fechamento técnico da rota de empenhos por credor — São Borja — 2019–2025

## 1. Objeto

Registrar o estado final da tentativa de materialização da série histórica de empenhos/liquidações/pagamentos por credor da **PM DE SÃO BORJA (código TCE-RS 58000)** no conjunto oficial **“Despesa orçamentária por empenhos”** do Tribunal de Contas do Estado do Rio Grande do Sul — SIAPC.

Este fechamento distingue três coisas que não podem ser confundidas:

1. **existência/documentação da fonte oficial**;
2. **metodologia de extração e tratamento**;
3. **materialização efetiva dos arquivos no ambiente de execução do SBMI**.

## 2. Fonte e rota oficial

**Fonte:** Tribunal de Contas do Estado do Rio Grande do Sul — Dados Abertos SIAPC.

**Produto:** Despesa orçamentária por empenhos.

**Órgão:** PM DE SÃO BORJA — código TCE-RS 58000.

**Período pretendido:** 2019–2025.

**Unidade monetária pretendida:** R$ correntes/nominais de cada exercício.

A documentação oficial informa rotas anuais consolidadas e rotas por órgão no padrão:

`/dados/municipal/empenhos/<ano>/<codigo-do-orgao>.<formato>`

com `csv.7z` e `csv.zip`.

As rotas específicas de São Borja foram registradas em:

`docs/data_sources/tce_siapc_official_per_organ_routes_2019_2025.md`.

## 3. Tentativas realizadas

### 3.1 Rota por órgão

Workflow:

`.github/workflows/tce-siapc-empenhos-sao-borja-2019-2025.yml`

Resultado persistido:

`docs/data_sources/tce_siapc_empenhos_sao_borja_2019_2025/`

Os sete anos ficaram sem arquivo extraído. Isso NÃO demonstra inexistência do dado; demonstra falha de transporte no ambiente utilizado.

### 3.2 Descoberta CKAN

Resultado:

`docs/data_sources/tce_siapc_empenhos_ckan_discovery_2019_2025/`

As consultas ao catálogo sofreram `ConnectTimeout`. Portanto, os registros `NO_CKAN_RESOURCE` dessa tentativa não devem ser interpretados como prova de ausência do recurso.

### 3.3 Arquivos anuais consolidados

Workflow:

`.github/workflows/tce-siapc-empenhos-consolidated-sao-borja-2019-2025.yml`

Run:

`35468774673`.

O GitHub marcou o workflow como **success**, mas esse sucesso é apenas do fluxo técnico: **nenhum dos sete arquivos anuais foi baixado**.

Evidências persistidas em:

`docs/data_sources/tce_siapc_empenhos_sao_borja_2019_2025_v2/`

- `source_manifest.tsv`: 2019–2025 = `FAILED`, bytes = 0;
- `yearly_payment_aggregate.csv`: 2019–2025 = `NO_SUMMARY`;
- `schema_inventory.csv`: sem schemas;
- `cnpj_payments_2019_2025.csv`: apenas cabeçalho.

**Decisão:** o run 35468774673 NÃO constitui extração SIAPC válida e não pode sustentar qualquer número histórico de credores.

## 4. Diagnóstico de rede

Workflow:

`.github/workflows/tce-host-network-diagnostic.yml`

Run:

`35472771620`.

Evidência persistida:

`docs/data_sources/tce_host_network_diagnostic/network.txt`.

### Resultado observado no GitHub Actions

DNS do host `dados.tce.rs.gov.br` resolveu para:

- `191.253.200.252`;
- `187.44.87.182`.

Não foi retornado endereço IPv6.

Testes TCP/HTTP:

- HTTPS raiz, IPv4, porta 443: **timeout de conexão nos dois IPs**;
- HTTPS rota por órgão, IPv4, porta 443: **timeout de conexão nos dois IPs**;
- HTTP rota por órgão, IPv4, porta 80: **timeout de conexão nos dois IPs**;
- IPv6: sem resolução utilizável.

Assim, a falha ocorre **antes de qualquer resposta HTTP**, autenticação, schema ou leitura do arquivo.

## 5. Diagnóstico

### Dado observado

A fonte e a rota oficial estão identificadas e documentadas.

### Dado observado

No ambiente GitHub Actions usado pelo projeto, o host de dados do TCE-RS não aceita conexão TCP nas portas testadas durante esta auditoria.

### Interpretação

O bloqueio é de **transporte/acessibilidade do host a partir do ambiente de execução**, não evidência de ausência dos dados SIAPC.

### O que NÃO é possível concluir

Não é possível, com os arquivos não materializados:

- calcular pagamentos históricos por credor;
- contar CNPJs/CPFs anuais de credores;
- calcular participação de pagamentos a CNPJ por ano;
- reconstruir geografia histórica de credores;
- comparar retenção territorial da primeira rodada do gasto público entre 2019 e 2025.

Nenhum valor deve ser imputado, estimado ou retroprojetado a partir de 2026.

## 6. Metodologia preparada para reabertura

A rotina mais robusta está em:

`.github/workflows/tce-siapc-empenhos-per-organ-parallel-2019-2025.yml`.

Ela prevê:

- um arquivo oficial por ano e órgão;
- processamento paralelo;
- soma por **tipo de operação**, evitando somar campos repetidos em eventos de natureza diferente;
- validação de CPF/CNPJ por dígitos verificadores;
- não persistência de nome, CPF ou linha de pessoa física;
- persistência apenas de agregados anuais e de CNPJ empresarial válido agregado por ano;
- comparação com SICONFI/DCA apenas como controle conceitual, não como teste de igualdade.

## 7. Condição objetiva para reabrir

A variável pode ser reaberta assim que os sete arquivos oficiais por órgão forem materializados a partir de uma rede que alcance o host do TCE-RS:

`2019/58000.csv.7z` até `2025/58000.csv.7z` — ou os equivalentes ZIP.

Não é necessária nova metodologia. O insumo faltante é o **arquivo bruto oficial acessível**.

Após obtenção:

1. registrar bytes e SHA-256;
2. auditar schema por ano;
3. executar agregação por tipo de operação;
4. validar documentos;
5. comparar os totais de pagamento ao SICONFI com nota conceitual;
6. somente então atualizar série de credores e análises territoriais.

## 8. Status final desta rodada

**STATUS: BLOQUEADO POR TRANSPORTE EXTERNO — FONTE E ROTA OFICIAL FECHADAS METODOLOGICAMENTE; ARQUIVOS 2019–2025 NÃO MATERIALIZADOS NO AMBIENTE.**

Este status fecha a investigação operacional desta rodada sem declarar ausência de dados e sem impedir reabertura futura.

A série fiscal agregada 2019–2025 permanece fechada pelo SICONFI/DCA. O histórico de credores não está fechado numericamente.

O Caderno-Base v028 permanece read-only.
