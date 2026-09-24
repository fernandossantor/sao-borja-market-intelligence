# Bens não essenciais — primeiro cenário exploratório de storefronts reconciliados — 24/09/2026

## 1. Objetivo

Converter a auditoria documental em uma primeira estimativa **exploratória** da oferta física/operacional de bens não essenciais em São Borja.

A unidade analítica aqui é **storefront/operação comercial**, não CNPJ.

## 2. Base documental

Inventário original:

- **120 linhas**;
- período de referência: 2026;
- 103 CNPJs únicos originais, além de linhas sem CNPJ.

Após a reconciliação:

- **115 das 120 linhas originais** permanecem no cenário-base;
- **5 linhas originais** ficam fora do cenário-base;
- **7 storefronts adicionais comprovados** foram incorporados porque não estavam representados por linhas próprias do inventário original.

### Linhas excluídas do cenário-base

- Pimentas Boutique Sensual — ausência de evidência atual independente;
- Loja CHICMI — ausência de evidência atual independente;
- Loja do Ramada — apenas evidência histórica;
- Akazzo — ausência de evidência local atual;
- Loja Maçônica Luz Invisível — CNPJ associativo sem atividade varejista identificada.

As exclusões por ausência de evidência atual são decisões de cenário, não afirmações de encerramento.

## 3. Storefronts adicionais

Foram adicionados **7 storefronts** não representados por linhas independentes no inventário:

- Tottal Casa & Lazer — Grazziotin;
- Por Menos — Grazziotin;
- Tech Box — Grazziotin;
- Pormenos — Grazziotin;
- Brasil Free Shop /0011-58;
- José Altamir Silveira da Rosa /0002-56 — marca de fachada pendente;
- Lojas Pompéia /0033-04.

A correção da Quero-Quero **não** acrescenta uma linha líquida: uma ocorrência duplicada do inventário foi reconciliada como a unidade distinta da Rua General Marques.

## 4. Dados calculados

### Cenário-base exploratório

Fórmula:

`storefronts_base = linhas_originais_incluidas + storefronts_adicionais`

`115 + 7 = 122 storefronts`.

### Cenário de sensibilidade conservadora

O cenário conservador mantém todas as decisões acima, mas exclui 7 Povos Kids até confirmação oficial direta:

`122 - 1 = 121 storefronts`.

Portanto, a faixa exploratória corrente é:

**121–122 storefronts**.

## 5. Interpretação

O inventário bruto tinha 120 linhas. A reconciliação produz uma faixa de **121 a 122 operações/storefronts** porque:

- cinco linhas deixam de compor o cenário-base;
- sete storefronts adicionais foram comprovados;
- 7 Povos Kids responde por uma diferença de uma unidade entre os cenários.

A variação líquida do cenário-base em relação às 120 linhas do inventário é:

`122 - 120 = +2`.

Esse resultado **não deve ser interpretado como crescimento temporal**. Ele decorre de auditoria, correções, substituições e descoberta de unidades omitidas.

## 6. Limitações

- storefront não equivale a empresa, CNPJ, raiz ou market share;
- algumas operações estão incluídas com identidade jurídica ainda P2;
- os sete adicionais precisam de classificação mercadológica harmonizada antes de análise por subcategoria;
- o resultado é municipal, São Borja/RS, e refere-se à melhor evidência reunida até 24/09/2026;
- não há série histórica comparável para inferir entrada líquida de estabelecimentos.

## 7. Próxima etapa

1. auditar a classificação mercadológica dos storefronts adicionais;
2. produzir contagem por subcategoria;
3. consolidar raízes/redes para distinguir storefronts de operadores econômicos;
4. somente depois calcular concentração e participação de redes em termos de **unidades**, deixando explícito que unidade não é faturamento nem market share.

## 8. Artefato

`docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v001.csv`
