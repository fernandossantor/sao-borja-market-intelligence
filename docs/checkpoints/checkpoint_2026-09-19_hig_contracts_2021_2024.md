# Checkpoint — HIG / Fundação Ivan Goulart — censo contratual 2021–2024

**Data:** 19/09/2026  
**Branch de trabalho:** `explore/receita-estadual-rs-market-intel-v1`  
**Governança:** PR #41 deve permanecer aberto, draft e sem merge. Caderno-Base v028 permanece read-only.

## Estado consolidado

O módulo oficial PMSB `/acordos` foi validado como fonte de estrutura contratual. O endpoint anual foi censado integralmente para os exercícios de 2021 a 2024, com leitura de 100% das páginas de detalhe retornadas e filtro pelo contratado `FUNDACAO IVAN GOULART`.

| Exercício | Linhas retornadas | Detalhes verificados | Falhas | Contratos HIG |
|---|---:|---:|---:|---:|
| 2021 | 102 | 102 | 0 | 6 |
| 2022 | 152 | 152 | 0 | 4 |
| 2023 | 178 | 178 | 0 | 2 |
| 2024 | 152 | 152 | 0 | 1 |

As contagens acima descrevem a camada contratual do módulo e **não** representam receitas, empenhos, liquidações ou pagamentos anuais.

## Contratos HIG identificados por exercício

### 2021
- Contrato 3/2021 — ID 453;
- Contrato 7/2021 — ID 460;
- Contrato 15/2021 — ID 469;
- Contrato 28/2021 — ID 483;
- Contrato 56/2021 — ID 511;
- Contrato 99/2021 — ID 558.

Crosswalks fechados:
- PRD Dispensa 11/2021 → Contrato 7/2021;
- PRD Dispensa 17/2021 → Contrato 15/2021;
- PRD Dispensa 24/2021 → Contrato 28/2021.

### 2022
- Contrato 7/2022 — ID 568 — sobreaviso médico SUS;
- Contrato 20/2022 — ID 581 — locação do antigo Hospital São Francisco;
- Contrato 117/2022 — ID 678 — tomografias e ressonâncias;
- Contrato 124/2022 — ID 685 — doença renal/hemodiálise.

Crosswalks fechados:
- Inexigibilidade 3/2022 → Contrato 7/2022;
- Dispensa 6/2022 → Contrato 20/2022;
- Inexigibilidade 20/2022 → Contrato 117/2022;
- Inexigibilidade 21/2022 → Contrato 124/2022.

Controle importante: o exercício 2022 demonstrou de forma inequívoca que o campo `Valor Total` do Portal é snapshot corrente e não série histórica. Há contratos historicamente monetários cujo detalhe atual mostra R$ 0,00.

### 2023
- Contrato 20/2023 — ID 768 — repasse federal — R$ 1.075.538,21;
- Contrato 146/2023 — ID 898 — mutirão de tomografias e ressonâncias — R$ 142.367,25.

Cadeias de identificadores:
- `licitacao_id 20318 → Inexigibilidade 13/2023 → processo 5562/2023 → Contrato 20/2023 → row.id 768`;
- `licitacao_id 20419 → Inexigibilidade 31/2023 → processo 16471/2023 → Contrato 146/2023 → row.id 898`.

O censo integral não revelou contratos HIG adicionais em 2023.

### 2024
- Contrato 105/2024 — ID 1068 — tomografias e ressonâncias sem contraste — R$ 122.212,00.

Crosswalk:
- `licitacao_id 20870 → Inexigibilidade 27/2024 → processo 20558/2024 → Contrato 105/2024 → row.id 1068`.

O censo integral não revelou contratos HIG adicionais em 2024.

## Regras metodológicas estabilizadas

1. `processo ≠ contrato ≠ aditivo ≠ empenho ≠ liquidação ≠ pagamento`.
2. `licitacao_id`, número da licitação, número do processo, número do contrato e `row.id` são identificadores distintos.
3. O campo `Valor Total` de `/acordos` é snapshot corrente e deve ser observado com data; não pode ser retroprojetado automaticamente.
4. Contrato/aditivo publicado não comprova pagamento.
5. Pagamentos via Prefeitura/FMS não comprovam origem municipal própria.
6. Contrato 20/2022 é fluxo de locação e não deve ser classificado automaticamente como financiamento assistencial SUS.
7. Não somar contratos-base, aditivos, portarias e mensalidades sem eliminação de sobreposição por competência.
8. A taxa de dependência financeira da Fundação continua **não calculável** sem DRE/balanço/receita operacional total e decomposição por origem.

## Artefatos principais

- `docs/data_sources/sao_borja_hig_contracts_census_2021/`
- `docs/data_sources/sao_borja_hig_contracts_census_2022/`
- `docs/data_sources/sao_borja_hig_contracts_census_2023/`
- `docs/data_sources/sao_borja_hig_contracts_census_2024/`
- `docs/data_sources/sao_borja_hig_contracts_history_2020_2025/hig_contracts_observed_2020_2025.csv`
- `docs/caderno_base/nota_analitica_fundacao_hospital_ivan_goulart_fontes_financiamento_2019_2026.md`
- Planilha exploratória Drive: abas `HIG_fontes_2019_2026`, `Agenda_dados`, `Delta_cadernos`, `Mapa_variaveis_ativas`.
- Documento-mestre de auditoria atualizado até a seção 42.52.

## Próximo bloco ao retomar

Executar o **censo integral de 2025** com o mesmo protocolo:

1. adaptar o workflow anual para 2025;
2. requisitar a grade integral com `rows=500`;
3. verificar 100% dos detalhes;
4. filtrar `FUNDACAO IVAN GOULART`;
5. cruzar com a série de Licitações;
6. separar identificadores técnicos e oficiais;
7. comparar valor histórico do instrumento com snapshot corrente;
8. registrar qualquer contrato HIG novo;
9. atualizar CSV histórico, nota analítica, planilha Drive e documento-mestre;
10. só depois produzir síntese longitudinal 2021–2025.

Hipóteses/itens já conhecidos que devem ser testados em 2025, sem presumir completude:
- aditivos do Contrato 99/2021, incluindo SERMulher;
- aditivos do Contrato 124/2022;
- aditivo do Contrato 20/2022;
- eventual instrumento novo de residência médica indicado na série de Licitações 2025.

## Estado de governança no fechamento

- PR #41: **aberto, draft, não mesclado**.
- Caderno-Base v028: **intocado/read-only**.
- Próximo passo autorizado apenas como continuação exploratória controlada.
