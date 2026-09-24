# Bens não essenciais — matriz deduplicada de CNPJs adicionais, substitutos e candidatos — 24/09/2026

## 1. Objeto

Esta matriz executa a **Etapa B** do checkpoint de continuidade, após a conclusão da primeira varredura das linhas originalmente sem CNPJ.

Foram consolidados todos os CNPJs presentes na trilha `BNE_validacao` que **não pertenciam ao universo original dos 103 CNPJs únicos**.

Resultado: **26 CNPJs únicos externos ao universo original**.

## 2. Classificação calculada

- `ADICIONAL_RAIZ`: 11;
- `IDENTIFICADO_LINHA_SEM_CNPJ`: 5;
- `CANDIDATO_FORTE_LINHA_SEM_CNPJ`: 2;
- `CANDIDATO_CORRECAO_ASSOCIACAO_MARCA`: 1;
- `CANDIDATO_HISTORICO_FORTE`: 1;
- `CANDIDATO_MODERADO_LINHA_SEM_CNPJ`: 1;
- `CORRECAO_DUPLICIDADE`: 1;
- `HISTORICO_MARCA_BAIXADO`: 1;
- `HOMONIMO_ALTERNATIVO`: 1;
- `SUBSTITUTO_CNPJ_ORIGINAL`: 1;
- `SUCESSOR_CANDIDATO`: 1;

A classe é uma **classificação calculada do SBMI**, derivada do histórico de auditoria. Não substitui os dados observados nas fontes.

## 3. Regras de elegibilidade

A matriz não incorpora automaticamente nenhum CNPJ à oferta ativa.

- `IDENTIFICADO_LINHA_SEM_CNPJ`: pode ser candidato à incorporação no universo reconciliado, preservando as reconciliações residuais.
- `CORRECAO_DUPLICIDADE` e `SUBSTITUTO_CNPJ_ORIGINAL`: exigem confirmação final antes de substituir/retificar o registro original.
- `ADICIONAL_RAIZ`: exige validar a função física da unidade e evitar transformar CNPJ em loja automaticamente.
- candidatos fortes/moderados: permanecem fora do denominador até vínculo direto marca↔CNPJ.
- CNPJ histórico baixado: serve à trilha temporal, não à oferta corrente.
- homônimo/alternativo: exige resolver se há sucessão, coexistência ou apenas colisão de marca.

## 4. Resultado estrutural da Etapa B

A auditoria agora distingue explicitamente:

- correções documentais;
- substituições;
- ampliação de raízes já presentes;
- preenchimento de linhas originalmente sem CNPJ;
- candidatos ainda não promovíveis;
- registros históricos.

Isso evita dois erros metodológicos: **somar todo CNPJ novo como nova loja** e **substituir silenciosamente o inventário original**.

## 5. Próxima etapa — Etapa C

Construir o **universo candidato reconciliado**, ainda não canônico, combinando:

1. os 103 CNPJs originais e suas decisões de fechamento;
2. os CNPJs desta matriz que forem elegíveis;
3. as linhas sem CNPJ que continuarem operacionalmente relevantes;
4. exclusões provisórias justificadas;
5. pendências mantidas explicitamente fora do denominador definitivo.

O universo candidato deve preservar uma coluna de `regra_inclusao` e outra de `pendencia`.

## 6. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Nenhuma métrica estrutural foi recalculada nesta etapa.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_cnpjs_adicionais_substitutos_candidatos_20260924_v001.csv`
