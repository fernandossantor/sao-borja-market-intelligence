# TJRS — consistência TLP × cargos providos — v027

**Data da auditoria:** 2026-09-12  
**Geografia:** São Borja/RS  
**Objetivo:** verificar a coerência entre a lotação real de servidores efetivos nas Tabelas de Lotação de Pessoal (TLP) do início de 2026 e o quantitativo oficial de cargos providos por comarca em junho/2026.

## 1. Conceitos

**Fonte normativa:** CNJ — Resolução nº 219/2016, Anexo VII.

- `LP`: lotação paradigma.
- `LR_EFET`: quantidade de servidores com provimento de cargo efetivo lotados na unidade ao final do ano-base.
- TLP 1: unidades judiciárias.
- TLP 2: demais unidades de apoio direto à atividade judicante.
- TLP 3: unidades de apoio indireto.

A TLP é semestral. A comparação abaixo é um **teste de consistência cross-period**, não uma identidade automática entre universos.

## 2. TLP 1 — unidades judiciárias de São Borja

**Fonte oficial:**  
`https://www.tjrs.jus.br/static/2026/03/2026-01-TLP1.pdf`

**Data no relatório:** 31/12/2025.

| Unidade | LP | LR_TOTAL | LR_EFET | LR_I | LR_SV |
|---|---:|---:|---:|---:|---:|
| 1ª Vara Cível | 4 | 4 | 3 | 0 | 1 |
| 1ª Vara Criminal | 3 | 4 | 3 | 0 | 1 |
| 2ª Vara Cível | 4 | 4 | 3 | 0 | 1 |
| 2ª Vara Criminal | 4 | 4 | 3 | 0 | 1 |
| CEJUSC | 1 | 1 | 1 | 0 | 0 |
| Vara do Juizado Especial Cível | 3 | 3 | 3 | 0 | 0 |
| **Total** | **19** | **20** | **16** | **0** | **4** |

**DADOS OBSERVADOS + CALCULADOS:** as seis unidades somam 16 servidores efetivos; a lotação real total soma 20 contra 19 posições de lotação paradigma.

**Limitação:** a diferença agregada de +1 em relação à soma da LP não demonstra folga operacional, excesso de pessoal ou adequação de capacidade; não considera carga processual corrente nem distribuição fina entre unidades.

## 3. TLP 2 — unidades de apoio direto

**Fonte oficial:**  
`https://www.tjrs.jus.br/static/2026/03/2026-01-TLP2.pdf`

**Data no relatório:** 01/01/2026.

| Unidade | LR_EFET |
|---|---:|
| Central de Atendimento ao Público (CAP) de São Borja | 4 |
| Central de Cumprimento Cartorário (CCC) de São Borja | 2 |
| Central de Mandados — Cartório da Direção do Foro de São Borja | 1 |
| Foro de São Borja | 9 |
| **Total** | **16** |

O PDF oficial é linearizado por blocos de coluna; os valores foram vinculados pela ordem unidade → `LR_EFET` dentro do mesmo bloco/página, com o código municipal como controle quando disponível.

## 4. TLP 3 — apoio indireto

**Fonte oficial:**  
`https://www.tjrs.jus.br/static/2026/03/2026-01-TLP3.pdf`

**Data:** 01/01/2026.

A busca documental por **São Borja** não encontrou ocorrência no TLP 3.

## 5. Soma estrutural

[
LR_EFET_{São Borja} = 16_{TLP1} + 16_{TLP2} = 32
]

**Natureza:** DADO CALCULADO.

Portanto, as TLPs registram **32 servidores efetivos lotados** nas unidades de São Borja identificadas no fechamento de 2025/início de 2026.

## 6. Controle com cargos providos — junho/2026

**Fonte:** TJRS — Quantitativo de Cargos Providos nas Comarcas.  
**Referência:** junho/2026.  
**Unidade:** cargos providos.

Resultado já auditado para São Borja:

**32 cargos providos**.

Teste:

[
Diferença = 32 - 32 = 0
]

[
Razão de consistência = 32/32 = 100%
]

**Classificação:** **COERÊNCIA CRUZADA FORTE**.

## 7. Interpretação

A igualdade entre o total `LR_EFET` das TLPs e os 32 cargos providos reforça a plausibilidade de um **núcleo efetivo local da ordem de 32 posições** no primeiro semestre de 2026.

A coincidência é compatível com a hipótese de que o relatório de cargos providos represente, em escala de comarca, o mesmo núcleo de cargos efetivos capturado por `LR_EFET`.

Essa hipótese **não é tratada como demonstrada**.

## 8. Limitações

A igualdade numérica não prova identidade porque:

- TLP 1: 31/12/2025;
- TLP 2 e TLP 3: 01/01/2026;
- cargos providos: junho/2026;
- movimentações podem ocorrer mantendo o mesmo total;
- o Anexo V inclui magistrados e demais agentes;
- a lotação total pode incluir servidores sem vínculo, cedidos/requisitados e funções comissionadas;
- 32 não deve ser usado como total de pessoas remuneradas pelo TJRS em São Borja.

## 9. Uso analítico

Quando a folha detalhada de julho/2026 for recuperada:

1. separar vínculos efetivos, magistrados e demais vínculos;
2. usar **32** como controle estrutural do núcleo efetivo;
3. investigar diferenças em vez de forçar reconciliação;
4. preservar as referências temporais distintas;
5. publicar apenas agregados.

## 10. Artefato Drive

Planilha v027: `1HjfbGo8qA2ZydfCrbouBVjlHDo8DRZs04H3cYr_FKMo`

Aba: `TJRS_TLP_consistencia_v027`

## 11. Governança

PR #41 deve permanecer **aberto, draft e sem merge**.

Branch: `feature/cnpj-territorial-control-v1`.

Nenhuma integração à `main` está autorizada.
