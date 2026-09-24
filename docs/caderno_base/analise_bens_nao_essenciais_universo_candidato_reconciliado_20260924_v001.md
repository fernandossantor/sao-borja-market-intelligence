# Bens não essenciais — universo candidato reconciliado v001 — 24/09/2026

## 1. Objeto

Esta tabela executa a **Etapa C** prevista no checkpoint: construir um universo candidato reconciliado, **ainda não canônico e sem recálculo de indicadores**.

A tabela reúne três camadas:

- 103 CNPJs originais já auditados;
- 26 CNPJs externos aos 103, identificados como adicionais, substitutos, correções ou candidatos;
- 6 linhas que continuam sem qualquer CNPJ identificado/candidato suficiente.

Total de registros de controle: **135**.

Esse total **não é número de operadores, lojas ou CNPJs ativos do mercado**.

## 2. Composição por origem

- `CNPJ_EXTERNO_AOS_103`: 26;
- `CNPJ_ORIGINAL_103`: 103;
- `LINHA_SEM_CNPJ_NAO_RESOLVIDA`: 6;

## 3. Regra de inclusão

Cada registro recebe uma `regra_inclusao` calculada para orientar o próximo passo. As principais regras são:

- `INCLUIR_CANDIDATO_BASE`: 47;
- `INCLUIR_COM_PENDENCIA`: 37;
- `PENDENTE_FUNCAO_FISICA_DA_UNIDADE`: 11;
- `INCLUIR_CANDIDATO_ADICIONAL`: 5;
- `PENDENTE_STATUS_ATUAL`: 5;
- `EXCLUIR_CNPJ_ATUAL_PRESERVAR_HISTORICO`: 3;
- `PENDENTE_SUBSTITUICAO_OU_CONTINUIDADE_DE_MARCA`: 3;
- `NAO_INCLUIR_CANDIDATO_ATUAL_SEM_EVIDENCIA`: 3;
- `PENDENTE_VINCULO_DIRETO_MARCA_CNPJ`: 2;
- `INCLUIR_COMO_OPERADOR_SEM_CNPJ_PENDENTE`: 2;
- `HISTORICO_FORTE_CNPJ_CORRENTE_PENDENTE`: 1;
- `HISTORICO_NAO_INCLUIR_COMO_ATIVO`: 1;
- `PENDENTE_PROVA_IDENTIDADE_JURIDICA`: 1;
- `SUBSTITUIR_CNPJ_ORIGINAL_APOS_CONFIRMACAO_FINAL`: 1;
- `PENDENTE_RESOLVER_HOMONIMIA_OU_SUCESSAO`: 1;
- `PENDENTE_COMPROVAR_SUCESSAO_DA_MARCA`: 1;
- `PENDENTE_VINCULO_EXPLICITO_MARCA_CNPJ`: 1;
- `RETIFICAR_INVENTARIO_APOS_CONFIRMACAO_FINAL`: 1;
- `NAO_INCLUIR_COMO_ATIVO_ENQUANTO_INAPTO`: 1;
- `PENDENTE_EVIDENCIA_INDEPENDENTE`: 1;
- `PENDENTE_RESOLVER_STATUS_CADASTRAL`: 1;
- `EXCLUIR_PROVISORIAMENTE_DO_ESCOPO_BNE`: 1;
- `INCLUIR_COM_PENDENCIA_ESTRUTURAL`: 1;
- `PENDENTE_CNPJ_ATUAL_DA_MARCA`: 1;
- `INCLUIR_COM_PENDENCIA_DE_STATUS_INDIVIDUAL`: 1;
- `INCLUIR_COM_PENDENCIA_JURIDICA`: 1;
- `HISTORICO_SEM_IDENTIDADE_JURIDICA_ATUAL`: 1;

Essas regras são **decisões técnicas provisórias**, não dados observados.

## 4. Princípios usados

- CNPJ ativo compatível pode entrar no universo candidato, mas ainda não define sozinho um ponto de venda.
- CNPJ adicional de uma raiz não é somado automaticamente como nova loja.
- CNPJ baixado não integra oferta cadastral ativa, mas a marca pode exigir busca de sucessor.
- CNPJ inapto não é tratado como ativo cadastral.
- linha sem CNPJ pode permanecer como operador operacional pendente quando há evidência atual forte, sem inventar identidade jurídica.
- registros históricos sem evidência corrente não entram como oferta atual.
- substituições e correções de duplicidade permanecem bloqueadas até confirmação final.

## 5. O que a tabela permite fazer agora

A próxima análise pode trabalhar apenas sobre registros com regras que autorizam presença no **universo candidato**, sem usar ainda um denominador definitivo.

Antes de qualquer indicador estrutural final, devem ser resolvidos os registros de pendência alta capazes de alterar:

- inclusão/exclusão;
- identidade jurídica;
- número de unidades;
- relação matriz/filial;
- sucessão de CNPJ;
- pertencimento setorial.

## 6. Decisão sobre recálculo

**Ainda não iniciar o recálculo canônico.**

A cobertura documental está alta e as etapas A–C estão estruturadas, mas persistem pendências estruturais relevantes. O próximo passo recomendado é gerar uma **fila priorizada de reconciliação final**, separando:

1. pendências que podem alterar o denominador;
2. pendências meramente editoriais;
3. confirmações RFB desejáveis, mas que não mudam a decisão provisória.

Somente o primeiro grupo deve bloquear o primeiro recálculo exploratório.

## 7. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Este universo candidato é exploratório e não substitui o inventário original.

## 8. Artefato

`docs/data_sources/bens_nao_essenciais_universo_candidato_reconciliado_20260924_v001.csv`
