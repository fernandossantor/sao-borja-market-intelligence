# Checkpoint — São Borja Inteligência Mercadológica — preços, farmácias e revalidação de bens não essenciais — 22/09/2026

## 1. Governança

- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- PR #41: **aberto, draft e sem merge**;
- Caderno-Base v028: **read-only**;
- novas evidências maduras entram como deltas para o sucessor;
- blocos de auditoria/controle não geram sucessora isoladamente;
- gravações devem continuar em blocos pequenos, com verificação após cada escrita;
- compras públicas/B2G seguem válidas, mas não monopolizam a agenda.

## 2. Estado herdado do checkpoint de 20/09

Permanecem válidos:

- bens essenciais: 54 operadores/linhas; 52 CNPJs documentais; 52 CNPJs únicos; 50 raízes; 2 raízes multiunidade; 4 unidades em raízes multi = **7,69%**;
- Bedi Padaria e Confeitaria e Sabor mineiro da Lu Delícias caseiras seguem sem CNPJ documental suficientemente confiável;
- join RFB dirigido dos 52 CNPJs segue bloqueado por transporte no runner GitHub;
- não repetir a mesma estratégia de download no runner hospedado até haver nova rota operacional ou bytes oficiais previamente adquiridos com hash;
- Cesta Nutricional Familiar segue com gate fechado até obter valor reproduzível do COREDE Fronteira Oeste para a mesma competência.

## 3. Delta 42.109 — Preços Dinâmicos jan–ago/2026

A série mensal do PCA-RE Fronteira Oeste × Rio Grande do Sul foi fechada para **janeiro a agosto de 2026, sem interpolação**.

### Série consolidada

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

### Dados observados e calculados

- valores e taxas mensais: transcritos dos boletins oficiais da Receita Estadual;
- março/2026 estadual corrigido e preservado em **R$ 287,85**;
- `Gap FO vs RS = (PCA_FO / PCA_RS - 1) × 100`;
- faixa jan–ago do gap: **-4,62% a -5,02%**;
- média simples dos oito gaps: **-4,85%**;
- FO mínimo: **R$ 273,97 em fevereiro**;
- FO máximo: **R$ 287,31 em junho**;
- RS mínimo: **R$ 287,85 em março**;
- RS máximo: **R$ 301,22 em junho**.

Mudança de nível janeiro → agosto, apenas como cálculo descritivo:

- FO: **+3,19%**;
- RS: **+3,03%**.

Não chamar essas duas mudanças de inflação acumulada oficial. Em agosto, as taxas oficiais acumuladas no ano eram:

- FO: **+2,01%**;
- RS: **+2,54%**.

### Readiness

**PROMOVER AO SUCESSOR COMO SÉRIE REGIONAL COMPLETA JAN–AGO/2026.**

O delta anterior de agosto/2026 permanece válido como fotografia corrente; 42.109 acrescenta a dimensão temporal.

### Artefatos

- `docs/data_sources/precos_dinamicos_pca_fo_rs_2026_jan_ago_v002.csv`;
- `docs/caderno_base/analise_precos_dinamicos_fo_rs_2026_jan_ago_v002.md`;
- `docs/data_sources/precos_dinamicos_2026_target_extract_20260922_v001.md`;
- `docs/data_sources/precos_dinamicos_rs_jun_jul_2026_ocr_target_20260922_v001.md`;
- aba Drive: `PCA_2026_full`.

Delta registrado em `Delta_cadernos`.

## 4. Delta 42.110 — Farmácias/drogarias CNES × POM

A arquitetura de rede de farmácias/drogarias foi revalidada com o **CNES/DATASUS**, consulta de 22/09/2026.

### Universo privado CNES

- 23 registros privados do tipo FARMÁCIA;
- 23 CNPJs únicos;
- 7 raízes CNPJ;
- 4 raízes multiunidade;
- 20 unidades em raízes multi;
- **20/23 = 86,96%** dos registros privados em raízes multi;
- maior raiz: **8/23 = 34,78%**.

### Principais raízes

- MB Farmácias: 8 registros;
- São João: 7;
- Panvel: 3;
- Farmácias Fronteira: 2.

### Crosswalk CNES × POM

- 19 dos 23 CNPJs privados CNES já apareciam no inventário POM;
- 4 CNPJs privados CNES são adicionais ao universo POM anterior:
  - 93.641.710/0044-11 — MB Farmácias;
  - 93.641.710/0080-85 — MB Farmácias Filial 80;
  - 92.665.611/0561-21 — Panvel;
  - 15.567.315/0001-92 — Phormula Central.

### Correção Panvel

A duplicidade antiga foi resolvida:

- 92.665.611/0467-54 → General Marques, 902;
- 92.665.611/0561-21 → Andradas, 2161.

### Controle de cobertura

Agafarma 26.710.619/0001-83 apresenta sinais operacionais em 2026, mas não aparece no recorte CNES consultado.

Consequência:

- os 23 registros privados CNES **não são censo exaustivo da oferta varejista privada**;
- não somar automaticamente 23 + Agafarma;
- quatro farmácias públicas municipais foram excluídas deliberadamente do denominador privado.

### Relação com a métrica legacy

- 85,00% = inventário POM anterior, 20 CNPJs;
- 86,96% = registros privados CNES correntes, 23 CNPJs.

Os universos diferem. A proximidade dos percentuais não demonstra estabilidade temporal.

### Readiness

**PROMOVER AO SUCESSOR DO CADERNO DE SAÚDE/HIGIENE COMO ESTRUTURA CADASTRAL CNES CORRENTE.**

Não interpretar 86,96% como market share, vendas ou poder de mercado.

### Artefatos

- `docs/data_sources/farmacias_cnes_pom_crosswalk_20260922_v001.csv`;
- `docs/caderno_base/analise_farmacias_cnes_corrente_20260922_v001.md`;
- batches de revalidação `farmacias_revalidacao_batch01...04_20260922_v001.csv`;
- aba Drive: `Farmacias_CNES_2026`.

Delta registrado em `Delta_cadernos`.

## 5. Bloco 42.111 — Bens não essenciais — início da revalidação cadastral

Universo documental corrente:

- 120 linhas;
- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes;
- 16 linhas sem CNPJ extraível;
- uma duplicidade explícita de CNPJ nas linhas da Lojas Quero-Quero.

### Triagem de alto risco concluída

#### Excêntrica — 18.283.007/0001-23

- inventário já indicava CNPJ baixado + Instagram atualizado;
- fonte cadastral secundária consultada em 22/09/2026: **BAIXADA desde 24/05/2022**;
- status provisório: `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`;
- não contar este CNPJ como oferta formal ativa sem identificar eventual sucessor cadastral.

#### Rilu Armarinhos e Presentes — 90.859.091/0001-08

- inventário já indicava CNPJ baixado + redes sociais ativas;
- fonte cadastral secundária: **BAIXADA desde 09/05/2019**;
- status provisório: `CNPJ_DOCUMENTAL_BAIXADO_MARCA_OPERACIONAL_POSSIVEL`;
- eventual continuidade da marca precisa ser reconciliada com outro CNPJ.

#### Lojas Quero-Quero — 96.418.264/0357-81

- mesmo CNPJ aparece em duas linhas do inventário;
- fontes cadastrais secundárias correntes: **ATIVA**, filial, Rua Coronel Aparício Mariense, 2635;
- status provisório: `CNPJ_SECUNDARIO_ATIVO_DUPLICIDADE_DE_LINHA_CONFIRMADA`;
- manter **um único CNPJ/unidade** no denominador até evidência de segunda unidade distinta.

### Status editorial

**CONTROLE DE REVALIDAÇÃO — NÃO GERAR DELTA AINDA.**

As fontes desta triagem são secundárias e não substituem RFB oficial linha a linha.

### Artefatos

- `docs/data_sources/bens_nao_essenciais_revalidacao_triage_20260922_v001.csv`;
- `docs/caderno_base/analise_bens_nao_essenciais_revalidacao_triage_20260922_v001.md`;
- aba Drive: `BNE_validacao`.

## 6. Estado do documento-mestre

Documento Drive:
`Auditoria Receita Estadual RS — integração exploratória SBMI — v001 — 20260917`.

Seções mais recentes registradas:

- 42.109 — Preços Dinâmicos jan–ago/2026;
- 42.110 — Farmácias/drogarias CNES × POM;
- 42.111 — Bens não essenciais, triagem inicial de revalidação.

Caderno-Base v028 não foi alterado.

## 7. Próxima sequência para retomada

### Prioridade 1 — Bens não essenciais

Continuar a revalidação dos **103 CNPJs únicos** em lotes pequenos e auditáveis.

Ordem:

1. registros com baixa/inconsistência;
2. grandes redes/filiais;
3. raízes multiunidade;
4. demais CNPJs por subcategoria.

Para cada CNPJ registrar:

- situação encontrada;
- período/data da evidência;
- endereço;
- compatibilidade com operador do inventário;
- fonte;
- natureza institucional/secundária;
- necessidade de reconciliação;
- decisão provisória manter/excluir/substituir.

Não recalcular “oferta ativa”, proporção multiunidade ou concentração até a cobertura ser suficiente.

### Prioridade 2 — Farmácias

Pendências após 42.110:

- validar CNAE/situação RFB quando a camada oficial linha a linha estiver operacional;
- reconciliar endereço corrente da Agafarma;
- monitorar entradas/saídas no CNES;
- manter CNES separado de market share.

### Prioridade 3 — Preços Dinâmicos

A série PCA-RE jan–ago está fechada. Próximo aprofundamento só deve ocorrer se houver pergunta analítica clara, por exemplo:

- itens/grupos específicos;
- arroz;
- feijão;
- leite;
- pão;
- carnes;
- frango;
- ovos;
- óleo;
- café;
- frutas/hortaliças.

Não expandir apenas por disponibilidade de dado.

### Prioridade 4 — Join RFB dirigido

Manter estacionado no runner GitHub até nova rota operacional ou acesso aos bytes oficiais em outro ambiente.

### Prioridade 5 — Cesta Nutricional Familiar

Gate continua fechado enquanto não houver valor reproduzível do COREDE Fronteira Oeste para a mesma competência do valor estadual.

## 8. Regras de retomada

- não municipalizar dados de COREDE;
- não tratar raiz CNPJ como market share;
- não somar universos RFB, SINAC/SIMEI, CNES, POM e RAIS;
- separar dado observado, cálculo, estimativa, hipótese e interpretação;
- não transformar fonte secundária de CNPJ em equivalente à RFB oficial;
- não criar sucessora da v028 até haver novo bloco maduro que justifique edição.

## 9. Estado de fechamento

- GitHub e Drive contêm os artefatos de 42.109, 42.110 e 42.111;
- abas `PCA_2026_full`, `Farmacias_CNES_2026` e `BNE_validacao` existem no Drive;
- `Delta_cadernos` contém os deltas maduros de preços e farmácias;
- 42.111 permanece somente como controle de revalidação;
- PR #41 permanece aberto, draft e sem merge;
- Caderno-Base v028 permanece read-only.
