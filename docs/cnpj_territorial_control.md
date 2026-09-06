# Controle territorial de matriz/filial — CNPJ

## Objetivo

Construir uma base municipal auditável que responda, para cada estabelecimento ativo em São Borja/RS:

1. se o estabelecimento é matriz ou filial segundo o campo oficial da Receita Federal;
2. onde está localizada a matriz da mesma raiz CNPJ;
3. se o controle territorial é classificado como:
   - `MATRIZ_LOCAL`;
   - `FILIAL_DE_MATRIZ_LOCAL`;
   - `FILIAL_DE_MATRIZ_EXTERNA`;
   - `FILIAL_MATRIZ_NAO_LOCALIZADA`;
   - `INDETERMINADO`;
4. qual é o CNAE principal, divisão CNAE, porte cadastral e capital social da empresa.

A finalidade analítica é apoiar o módulo transversal de **retenção territorial, vazamento econômico e circulação da renda**. A localização da matriz é apenas uma dimensão da retenção; ela não mede lucro, faturamento, compras externas ou valor vazado.

## Fontes

Fonte primária: Receita Federal do Brasil — Dados Abertos CNPJ.

- Dados cadastrais e campo matriz/filial: <https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/convenios-e-transferencias/compartilhamento-de-bases-de-dados-2013-decreto-no-8-789-2016/leiaute-das-bases/dados-da-base-cnpj>
- Cadastro e dados abertos: <https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/dados-abertos/cadastros>
- Tabela de municípios TOM: <https://www.gov.br/receitafederal/dados/municipios.csv/view>

São Borja:

- código TOM: `8863`;
- código IBGE: `4318002`.

## Regra metodológica crítica

**Não usar a ordem do estabelecimento no CNPJ como sinônimo de matriz/filial.**

O pipeline lê o campo oficial `identificador_matriz_filial`. Depois, para cada raiz empresarial com estabelecimento em São Borja, localiza o estabelecimento identificado como matriz e lê seu município.

A classificação territorial resulta de duas informações diferentes:

- condição do estabelecimento local (`matriz` ou `filial`);
- município da matriz empresarial.

## Entradas

O pipeline espera os arquivos ZIP originais da mesma competência mensal:

- `Estabelecimentos*.zip` — todos os arquivos da competência;
- `Empresas*.zip` — todos os arquivos da competência;
- `Municipios.zip`.

Os arquivos nacionais são volumosos e **não devem ser adicionados ao Git**. Devem permanecer em `.data/raw` ou snapshot local equivalente, com proveniência registrada.

O download integral é uma operação de grande volume e deve respeitar a autorização prevista em `AGENTS.md`.

## Execução

Exemplo:

```bash
python -m sbmi.cnpj_territorial_control_cli \
  --establishments-dir .data/raw/rfb_cnpj/2026-08 \
  --companies-dir .data/raw/rfb_cnpj/2026-08 \
  --municipalities-zip .data/raw/rfb_cnpj/2026-08/Municipios.zip \
  --execution-id cnpj-territorial-control-202608
```

O CLI filtra por padrão:

- município TOM `8863`;
- situação cadastral ativa `02`;
- IBGE `4318002`.

## Fluxo de dados

```text
raw ZIPs RFB
   ↓
staging — estabelecimentos ativos de São Borja
   ↓
curated — estabelecimento + empresa + matriz + município da matriz
   ↓
exports — agregações por divisão CNAE e porte
   ↓
audit — manifesto SHA-256 + validações
```

## Saídas

### Curated

`cnpj_territorial_control.csv`

Inclui CNPJ completo, raiz, indicador oficial matriz/filial, razão social, nome fantasia, CNAE, porte, capital social, CNPJ da matriz, município/UF da matriz e classificação territorial.

### Exports

- `cnpj_territorial_control_by_division.csv`
- `cnpj_territorial_control_by_size.csv`

As proporções de matriz externa são **contagens cadastrais**. Não devem ser interpretadas como participação em faturamento, emprego ou valor adicionado.

### Audit

- `source_manifest.csv` — arquivo, tamanho, SHA-256 e fonte declarada;
- `validation.csv` — duplicidades, município, códigos matriz/filial e cobertura de localização das matrizes.

## Próxima integração

Depois da execução real, cruzar a base com:

1. RAIS — vínculos e massa salarial por estabelecimento/setor;
2. CEMPRE — unidades locais e pessoal ocupado para reconciliação de escala;
3. VAF/ICMS — quando houver desagregação compatível;
4. pesquisa de fornecedores — para estimar encadeamentos e vazamentos correntes.

A primeira proxy quantitativa de controle externo deve ponderar o cadastro por variáveis de escala econômica; a simples participação das filiais no número de CNPJs é insuficiente.
