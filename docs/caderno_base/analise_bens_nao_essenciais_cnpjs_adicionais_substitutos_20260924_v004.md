# Bens não essenciais — CNPJs adicionais, substitutos e candidatos — v004 — 24/09/2026

## 1. Atualização

A v004 incorpora as decisões do lote 23 de reconciliação P1, sem criar novos CNPJs na matriz externa.

A matriz permanece com **33 CNPJs únicos externos aos 103 originais**, mas seis registros mudam de natureza porque sua função física foi decidida para o cenário-base exploratório.

## 2. Quero-Quero

### 96.418.264/0028-59

Passa de correção de duplicidade pendente para:

`STOREFRONT_DISTINTO_CORRECAO_DUPLICIDADE`.

A unidade da Rua General Marques, 694, possui CNPJ ativo e evidência operacional própria, distinta da unidade `/0357-81` da Rua Coronel Aparício Mariense, 2635.

**Decisão:** incorporar como storefront e corrigir a repetição documental do inventário.

### 96.418.264/0533-30

Passa de CNPJ adicional de raiz para:

`UNIDADE_JURIDICA_ATIVA_NAO_STOREFRONT_BASE`.

O CNPJ está ativo na Rua Homero Pereira Coimbra, 54, mas não foi encontrada evidência operacional suficiente de atendimento varejista ao público.

**Decisão:** preservar na camada jurídica e em sensibilidade, sem acrescentar storefront ao cenário-base.

## 3. Grazziotin

Quatro CNPJs adicionais passam para:

`STOREFRONT_DISTINTO_RAIZ`.

São eles:

- `92.012.467/0094-79` — Tottal Casa & Lazer — Eddie Freire Nunes, 1999;
- `92.012.467/0121-86` — Por Menos — Presidente Vargas, 1206;
- `92.012.467/0265-60` — Tech Box — General Marques, 1066;
- `92.012.467/0451-90` — Pormenos — Cândido Falcão, 940.

Todos possuem endereço próprio e evidência comercial atual compatível com storefront.

## 4. Efeito metodológico

A v004 reduz o conjunto de CNPJs adicionais cuja função física ainda bloqueia o denominador.

Ela também deixa explícito que:

- CNPJ adicional de raiz pode ser storefront;
- CNPJ adicional de raiz pode não entrar no storefront-base;
- nomes semelhantes da mesma raiz não autorizam deduplicação quando CNPJ e endereço são distintos.

## 5. Limitações

- a classificação de storefront é uma decisão técnica do SBMI baseada em convergência cadastral e operacional;
- não é nomenclatura oficial da Receita Federal;
- não mede faturamento, capacidade, fluxo ou participação de mercado;
- o CNPJ Quero-Quero `/0533-30` pode ser reclassificado se surgir evidência de atendimento ao público.

## 6. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- nenhum indicador canônico foi recalculado.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_cnpjs_adicionais_substitutos_candidatos_20260924_v004.csv`
