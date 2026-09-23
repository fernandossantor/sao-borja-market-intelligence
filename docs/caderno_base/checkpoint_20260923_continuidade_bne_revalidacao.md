# Checkpoint — São Borja Inteligência Mercadológica — continuidade após limite da conversa — 23/09/2026

## 1. Governança

- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- PR #41: **aberto, draft e sem merge**;
- Caderno-Base v028: **read-only**;
- novas evidências maduras entram apenas como deltas para o sucessor;
- controles técnicos/auditorias não criam sucessora isoladamente;
- gravações devem seguir em blocos pequenos, com verificação após cada escrita;
- compras públicas/B2G seguem válidas, mas não monopolizam a agenda.

## 2. Estado consolidado herdado do checkpoint de 22/09/2026

### 2.1 Preços Dinâmicos — delta 42.109

A série PCA-RE Fronteira Oeste × Rio Grande do Sul está fechada para janeiro–agosto/2026, sem interpolação.

| Competência | FO (R$) | RS (R$) | Gap FO vs RS |
|---|---:|---:|---:|
| jan/2026 | 275,41 | 289,83 | -4,98% |
| fev/2026 | 273,97 | 288,33 | -4,98% |
| mar/2026 | 274,55 | 287,85 | -4,62% |
| abr/2026 | 281,40 | 296,26 | -5,02% |
| mai/2026 | 285,58 | 300,54 | -4,98% |
| jun/2026 | 287,31 | 301,22 | -4,62% |
| jul/2026 | 282,74 | 296,84 | -4,75% |
| ago/2026 | 284,19 | 298,61 | -4,83% |

Dados calculados preservados:

- faixa jan–ago do gap: **-4,62% a -5,02%**;
- média simples dos oito gaps: **-4,85%**;
- mudança de nível jan→ago: FO **+3,19%**; RS **+3,03%**;
- não chamar essas mudanças de inflação acumulada oficial.

Status: **promovido ao sucessor como série regional completa jan–ago/2026**.

Artefatos principais:
- `docs/data_sources/precos_dinamicos_pca_fo_rs_2026_jan_ago_v002.csv`;
- `docs/caderno_base/analise_precos_dinamicos_fo_rs_2026_jan_ago_v002.md`;
- aba Drive `PCA_2026_full`.

## 3. Farmácias/drogarias — delta 42.110

Revalidação corrente via CNES/DATASUS, consulta de 22/09/2026:

- 23 registros privados;
- 23 CNPJs únicos;
- 7 raízes;
- 4 raízes multiunidade;
- 20/23 unidades em raízes multi = **86,96%**;
- maior raiz: 8/23 = **34,78%**.

Raízes principais:

- MB Farmácias: 8;
- São João: 7;
- Panvel: 3;
- Farmácias Fronteira: 2.

Crosswalk CNES × POM:

- 19/23 CNPJs já estavam no POM;
- 4 CNPJs CNES adicionais:
  - 93.641.710/0044-11 — MB Farmácias;
  - 93.641.710/0080-85 — MB Farmácias Filial 80;
  - 92.665.611/0561-21 — Panvel;
  - 15.567.315/0001-92 — Phormula Central.

Correção Panvel:

- 92.665.611/0467-54 → General Marques, 902;
- 92.665.611/0561-21 → Andradas, 2161.

Controle:

- Agafarma 26.710.619/0001-83 apresenta sinais operacionais recentes, mas não consta no recorte CNES;
- 23 CNES privados não devem ser chamados de censo exaustivo da oferta privada;
- 86,96% não é market share.

Status: **promovido ao sucessor do caderno de Saúde/Higiene como estrutura cadastral CNES corrente**.

## 4. Bens não essenciais — bloco 42.111 em andamento

Universo documental corrente:

- 120 linhas;
- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes;
- 16 linhas sem CNPJ extraível;
- duplicidade explícita: Lojas Quero-Quero.

Triagem já concluída:

### Excêntrica — 18.283.007/0001-23
- fonte cadastral secundária: **BAIXADA desde 24/05/2022**;
- marca pode continuar operacional sob outro CNPJ;
- status provisório: `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`.

### Rilu Armarinhos e Presentes — 90.859.091/0001-08
- fonte cadastral secundária: **BAIXADA desde 09/05/2019**;
- eventual continuidade da marca exige identificação de outro CNPJ;
- status provisório: `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`.

### Lojas Quero-Quero — 96.418.264/0357-81
- mesmo CNPJ aparece em duas linhas do inventário;
- fontes cadastrais secundárias: **ATIVA**, filial, Rua Coronel Aparício Mariense, 2635;
- status provisório: `CNPJ_SECUNDARIO_ATIVO_DUPLICIDADE_DE_LINHA_CONFIRMADA`;
- contar como uma única unidade/CNPJ até evidência distinta.

Artefatos:

- `docs/data_sources/bens_nao_essenciais_revalidacao_triage_20260922_v001.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_revalidacao_triage_20260922_v001.md`;
- aba Drive `BNE_validacao`.

Status editorial: **controle de revalidação; nenhum delta ainda**.

## 5. Controles herdados

### Bens essenciais
- 54 operadores/linhas;
- 52 CNPJs documentais validados;
- 52 CNPJs únicos;
- 50 raízes;
- 2 raízes multiunidade;
- 4 unidades em raízes multi;
- 7,69%.

Bedi Padaria e Confeitaria e Sabor mineiro da Lu Delícias caseiras permanecem sem CNPJ documental suficientemente confiável.

### Join RFB dirigido
Permanece bloqueado no runner hospedado pelo GitHub por falha de transporte antes da leitura de `Municipios.zip`.

Não repetir a mesma estratégia até:
- nova rota operacional;
- outro ambiente/rede;
- ou bytes oficiais adquiridos e preservados com SHA-256.

### Cesta Nutricional Familiar
Gate permanece fechado até existir valor reproduzível do COREDE Fronteira Oeste na mesma competência do valor estadual.

## 6. Próxima retomada

**Prioridade principal: continuar a revalidação dos 103 CNPJs únicos de bens não essenciais em lotes pequenos e auditáveis.**

Ordem recomendada:

1. inconsistências/baixas já sinalizadas;
2. grandes redes e filiais;
3. raízes multiunidade;
4. demais CNPJs por subcategoria.

Para cada registro, preservar:

- CNPJ;
- operador/marca;
- situação encontrada;
- data/competência da evidência;
- endereço;
- compatibilidade com o inventário;
- fonte;
- natureza da fonte;
- necessidade de reconciliação;
- decisão provisória manter/excluir/substituir.

**Não recalcular ainda**:
- oferta ativa;
- proporção multiunidade;
- concentração;
- número final de operadores.

Essas métricas só devem ser recalculadas quando a cobertura da revalidação for suficiente.

## 7. Regras metodológicas de retomada

- não municipalizar COREDE;
- não tratar raiz CNPJ como market share;
- não somar universos RFB, SINAC/SIMEI, CNES, POM e RAIS;
- separar dado observado, cálculo, estimativa, hipótese e interpretação;
- fonte cadastral secundária não substitui RFB oficial;
- marca operacional não prova atividade do CNPJ documental;
- duplicidade de linha deve ser resolvida antes de qualquer contagem;
- não criar sucessora da v028 sem novo bloco maduro.

## 8. Estado de fechamento da conversa

A conversa atingiu o limite de duração antes de nova rodada substantiva de revalidação dos 103 CNPJs.

Portanto, **nenhum novo resultado analítico posterior ao bloco 42.111 deve ser presumido**.

O próximo chat deve retomar diretamente pela revalidação de bens não essenciais, sem refazer 42.109, 42.110 ou a triagem inicial de 42.111.
