# Fechamento técnico — TCE-RS/SIAPC — histórico de empenhos/credores — São Borja — 2019–2025

## 1. Objeto

Fechar metodologicamente a tentativa de extração automática, a partir do GitHub Actions, dos arquivos oficiais do TCE-RS/SIAPC para **Despesa orçamentária por empenhos**, órgão **PM DE SÃO BORJA — código 58000**, exercícios **2019–2025**.

Este fechamento **não afirma ausência de dados**. Ele documenta uma limitação de transporte entre o ambiente de execução do projeto e o host oficial `dados.tce.rs.gov.br`.

## 2. Fonte e rota oficial

Fonte: Tribunal de Contas do Estado do Rio Grande do Sul — Dados Abertos SIAPC.

Conjunto: Despesa orçamentária por empenhos.

Abrangência pretendida: Prefeitura Municipal de São Borja/RS, código TCE-RS 58000.

Período: 2019–2025.

Rotas oficiais testadas:

- por órgão: `/dados/municipal/empenhos/<ano>/58000.csv.7z`;
- por órgão: `/dados/municipal/empenhos/<ano>/58000.csv.zip`;
- consolidada anual: `/dados/municipal/empenhos/<ano>.csv.7z`;
- consolidada anual: `/dados/municipal/empenhos/<ano>.csv.zip`;
- catálogo CKAN: `/api/3/action/package_search`.

Foram testados HTTP e HTTPS quando aplicável.

## 3. Evidência observada

### 3.1 Extração anual consolidada

Run GitHub Actions: `35468774673`.

O run terminou tecnicamente como `success`, porém **não produziu nenhum ano válido**. O manifesto persistido registra:

- 2019: FAILED;
- 2020: FAILED;
- 2021: FAILED;
- 2022: FAILED;
- 2023: FAILED;
- 2024: FAILED;
- 2025: FAILED.

O arquivo `yearly_payment_aggregate.csv` registra `NO_SUMMARY` para os sete anos.

Portanto, o status `success` do run não deve ser confundido com sucesso de extração. O workflow foi corrigido posteriormente para tratar ausência de qualquer ano como falha lógica.

### 3.2 Extração paralela por órgão

Run: `35472497128`.

Foram executados sete jobs independentes, um para cada exercício de 2019 a 2025.

Resultado: **7/7 falharam no download**.

Foram tentados:

- HTTPS + 7Z;
- HTTPS + ZIP;
- HTTP + 7Z;
- HTTP + ZIP.

Os logs registram repetidamente `curl (28)` por timeout de conexão, tanto na porta 443 quanto na porta 80.

### 3.3 Descoberta CKAN

As consultas ao catálogo oficial também retornaram `ConnectTimeout` ao host `dados.tce.rs.gov.br`, sem obtenção de metadados de recursos no ambiente GitHub Actions.

### 3.4 Prova de conectividade controlada

Workflow: `.github/workflows/tce-siapc-connectivity-probe.yml`.

Run final: `35474280735`.

Teste forçando IPv4 sobre:

- home HTTPS;
- home HTTP;
- CKAN HTTPS;
- CKAN HTTP;
- arquivo por órgão 2025 em 7Z HTTPS/HTTP;
- arquivo por órgão 2025 em ZIP HTTPS/HTTP.

Resultado em todos os oito testes:

- `http_code = 000`;
- `size_download = 0`;
- `exit_code = 28`;
- nenhum `remote_ip` estabelecido.

Isso caracteriza **falha de conexão/transporte antes da resposta HTTP**, e não erro 404/403 do recurso.

## 4. Conclusão técnica

**DADO OBSERVADO:** o host oficial do TCE-RS não é alcançável de forma funcional pelo GitHub Actions usado neste projeto, tanto em HTTP quanto HTTPS, inclusive forçando IPv4.

**INTERPRETAÇÃO:** a rota SIAPC está bloqueada operacionalmente neste ambiente. Não há evidência de que os arquivos 2019–2025 estejam ausentes; a documentação pública do TCE-RS registra o conjunto e o padrão de rotas.

**DECISÃO METODOLÓGICA:** encerrar novas tentativas redundantes pelo mesmo transporte GitHub Actions. A extração SIAPC 2019–2025 fica classificada como:

> **FONTE OFICIAL IDENTIFICADA E METODOLOGIA PRONTA; AQUISIÇÃO DOS BYTES BLOQUEADA POR TRANSPORTE DO HOST NO AMBIENTE CORRENTE.**

## 5. Consequências para a análise

Não há valores históricos SIAPC 2019–2025 aprovados nesta camada.

Em especial, **não** foram obtidos:

- totais anuais de pagamento por SIAPC;
- quantidade anual de CNPJs credores pelo SIAPC;
- agregados anuais por CNPJ;
- geografia histórica dos credores.

A série fiscal agregada 2019–2025 continua sustentada pelo SICONFI/DCA já auditado.

O histórico de credores deve avançar por **rota administrativa oficial alternativa**, mantendo o SIAPC como fonte pendente de aquisição em outro ambiente.

## 6. Próxima rota operacional

O Portal da Transparência de São Borja apresentou uma rota histórica distinta, `Ordem Cronológica`, com:

- Prefeitura Municipal de São Borja como instituição;
- exercícios publicados de 2018 a 2026;
- endpoint `/ordem_cronologica/getElementos`;
- campos CPF/CNPJ, credor, valor, pagamento, descrição, número de contrato e documento fiscal;
- listas publicadas: Recursos Vinculados, Pequeno Valor e Dispensa.

Essa rota deve ser auditada como **fonte própria**, sem pressupor equivalência de universo com SIAPC ou com a despesa paga do SICONFI.

Primeiro controle obrigatório: medir cobertura anual da Ordem Cronológica contra a despesa paga do SICONFI e explicar o escopo jurídico/administrativo antes de qualquer uso como histórico de credores.

## 7. Governança

- Caderno-Base v028: read-only.
- PR #41: deve permanecer aberto, draft e sem merge.
- Nenhum resultado vazio desta tentativa SIAPC deve ser promovido como dado.
