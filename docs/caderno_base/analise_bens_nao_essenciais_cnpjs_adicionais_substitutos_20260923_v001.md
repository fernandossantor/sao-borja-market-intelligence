# Bens não essenciais — CNPJs adicionais, substitutos e recuperados — 23/09/2026

## 1. Objeto

Esta matriz consolida os CNPJs encontrados durante a revalidação que **não pertenciam ao conjunto original dos 103 CNPJs únicos**.

Ela serve para impedir dois erros:

1. somar automaticamente CNPJs novos ao universo antes de reconciliar sua função;
2. perder correções relevantes de duplicidade, substituição e linhas originalmente sem CNPJ.

## 2. Resultado observado

Foram identificados **17 CNPJs únicos adicionais/substitutos/recuperados**.

Distribuição calculada por tipo:

- `CANDIDATO_CORRECAO_MARCA_CNPJ`: 1;
- `CNPJ_ADICIONAL_MESMA_RAIZ`: 11;
- `CNPJ_HOMONIMO_CONTROLE_SEPARADO`: 1;
- `CNPJ_RECUPERADO_LINHA_ORIGINAL_SEM_CNPJ`: 2;
- `CNPJ_SUBSTITUTO_CANDIDATO`: 1;
- `CORRECAO_DUPLICIDADE_CNPJ_DISTINTO`: 1;

Essas classes são **calculadas pelo SBMI** para controle de auditoria. Não são categorias oficiais da Receita Federal.

## 3. Tipos de caso

### Correção de duplicidade
A duplicidade Quero-Quero do inventário revelou outro CNPJ real da mesma raiz em São Borja.

### Substituição de CNPJ
Americanas apresenta CNPJ documental antigo baixado e CNPJ sucessor candidato no mesmo ponto.

### Correção marca ↔ CNPJ
Lins Ferrão/Pompéia exige reconciliar qual CNPJ corresponde à marca observada.

### CNPJs recuperados de linhas originalmente sem número
Monaco Freeshop e Mais Top Papelaria receberam CNPJs robustamente identificados.

### CNPJ homônimo de controle separado
Veterinária São Francisco possui outro CNPJ atual associado ao mesmo nome comercial; não há autorização metodológica para tratá-lo como substituto sem prova de sucessão.

### CNPJs adicionais da mesma raiz
As demais descobertas revelam raízes subcobertas no inventário, mas um CNPJ adicional não deve ser transformado automaticamente em nova loja física.

## 4. Regra de uso

Todos os 17 registros permanecem com:

`elegibilidade_provisoria = NAO_INCLUIR_NO_DENOMINADOR_ATE_RECONCILIACAO`.

Isso não significa que sejam inválidos. Significa apenas que sua incorporação ao universo reconciliado depende de verificar:

- função física/operacional;
- substituição versus coexistência;
- marca correspondente;
- eventual duplicidade;
- pertencimento ao escopo mercadológico;
- situação cadastral suficiente.

## 5. Próxima etapa

Cruzar esta matriz com as 16 linhas originalmente sem CNPJ extraível e, depois, montar um universo candidato reconciliado. O recálculo de oferta ativa continua bloqueado até essa reconciliação.

## 6. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Esta matriz é controle técnico de auditoria.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_cnpjs_adicionais_substitutos_20260923_v001.csv`
