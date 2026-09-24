# Bens não essenciais — matriz de fechamento da revalidação dos 103 CNPJs — 23/09/2026

## 1. Objeto

Esta matriz consolida a primeira passagem de auditoria dos **103 CNPJs únicos originais** do inventário de bens não essenciais.

Ela não recalcula oferta ativa, concentração, número de operadores ou proporção multiunidade. Seu papel é separar os registros que podem seguir para futura consolidação daqueles que ainda exigem reconciliação estrutural.

## 2. Cobertura observada

- CNPJs originais: **103**.
- CNPJs examinados: **103/103 = 100,00%**.
- CNPJs com alguma evidência independente recuperada: **102/103 = 99,03%**.
- Único registro sem evidência independente suficiente: **28.597.654/0001-63 — Pimentas Boutique Sensual**.

## 3. Regra de classificação

A coluna `classe_fechamento` é uma classificação **calculada pelo SBMI** a partir do `status_provisorio` registrado nos lotes. Ela não substitui o dado observado de cada fonte.

Classes e contagens desta versão:

- `ATIVO_COMPATIVEL`: 47;
- `ATIVO_COM_RECONCILIACAO`: 37;
- `STATUS_CADASTRAL_PENDENTE`: 5;
- `BAIXADO`: 3;
- `BAIXADO_COM_RECONCILIACAO`: 3;
- `INAPTO`: 1;
- `SEM_EVIDENCIA_INDEPENDENTE`: 1;
- `CONFLITO_CADASTRAL`: 1;
- `ATIVO_FORA_ESCOPO_VAREJISTA`: 1;
- `ATIVO_COM_RECONCILIACAO_ESTRUTURAL`: 1;
- `INAPTO_COM_MARCA_OPERACIONAL_POSSIVEL`: 1;
- `ATIVA_POR_LISTAGEM_SETORIAL_STATUS_INDIVIDUAL_PENDENTE`: 1;
- `PRESENCA_COMPATIVEL_METADADO_JURIDICO_PENDENTE`: 1;

A coluna `bloqueio_estrutural` também é calculada. Ela marca como **SIM** situações que podem alterar inclusão, exclusão, identidade do operador ou quantidade de unidades/CNPJs no futuro recálculo, como:

- baixa ou inaptidão;
- conflito cadastral;
- status corrente não confirmado;
- duplicidade ou CNPJ substituto;
- raiz subcoberta/co-localizada;
- colisão/homonímia relevante;
- divergência setorial que afete pertencimento ao universo;
- registro fora do escopo varejista.

Nesta matriz:

- bloqueio estrutural = **SIM**: 30;
- bloqueio estrutural = **NÃO**: 73.

Essas contagens são de **status de auditoria**, não de oferta ativa.

## 4. Uso correto

A matriz permite agora:

1. localizar todos os bloqueios que precisam de tratamento antes do recálculo;
2. separar problemas meramente editoriais de problemas que alteram o denominador;
3. cruzar os CNPJs adicionais/substitutos descobertos nos lotes;
4. preparar um sucessor do inventário sem sobrescrever silenciosamente o histórico.

## 5. Próxima etapa

Antes de recalcular oferta ativa, produzir duas reconciliações específicas:

### 5.1 CNPJs adicionais/substitutos

Consolidar, sem duplicidade, todos os CNPJs encontrados durante a auditoria que não faziam parte dos 103 originais ou que substituem CNPJs baixados.

### 5.2 Linhas originalmente sem CNPJ

Revisar as 16 linhas sem CNPJ extraível, separando:

- CNPJ agora identificado com boa evidência;
- candidato ainda insuficiente;
- sem identificação documental.

Somente após essas duas camadas será possível montar um universo candidato reconciliado e decidir se o recálculo estrutural pode ser iniciado.

## 6. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Esta matriz é controle técnico de auditoria, não delta editorial autônomo.

## 7. Artefato tabular

`docs/data_sources/bens_nao_essenciais_revalidacao_fechamento_103_20260923_v001.csv`
