# SINAC/SIMEI — reprodução municipal São Borja

**Fonte observada:** Receita Federal — Portal Estatísticas do Simples Nacional (SINAC/SIMEI).  
**Abrangência geográfica:** São Borja/RS, seleção municipal oficial (código interno 8863).  
**Posição de consolidação preservada:** 12/09/2026.  
**Unidade:** número de optantes/ocorrências por CNAE, conforme a consulta oficial.

## Resultado corrente reproduzido

- SINAC total observado: **7.176**.
- SIMEI total observado: **4.883**.
- SINAC por CNAE: **427 linhas**, soma calculada = **7.176**.
- SIMEI por CNAE: **233 linhas**, soma calculada = **4.883**.
- Reconciliação total × soma CNAE: **exata nos dois regimes**.

A paginação completa da consulta por CNAE está persistida em
`sao_borja_cnae.csv`; os totais e controles estão em
`sao_borja_totals.csv` e `summary.json`.

## Natureza dos dados e regras

Os valores da página oficial são **dados observados**. As somas das linhas CNAE
e os testes de igualdade com o total são **cálculos de validação**.

A posição de consolidação exibida pela própria página deve ser preservada. Não
usar cross-check secundário como substituto da fonte primária e somente aceitar
resultado quando São Borja estiver explicitamente presente na saída ou quando o
controle da consulta comprovar o município selecionado.

## Limitações e comparabilidade

SINAC/SIMEI medem optantes nos respectivos regimes e **não equivalem ao universo
de estabelecimentos ativos da base CNPJ da RFB**. Portanto, 7.176 SINAC, 4.883
SIMEI e 7.306 estabelecimentos ativos RFB não devem ser comparados como se fossem
contagens do mesmo conceito. Qualquer reconciliação entre essas bases exige
alinhamento de competência/data, unidade estatística e regra cadastral.

O fechamento aqui é da **posição corrente 12/09/2026 — total e decomposição CNAE**.
Uma série histórica só deve ser construída se a rota oficial permitir reprodução
temporal consistente.
