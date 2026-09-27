# Checkpoint — congelamento editorial dos cinco cadernos — 2026-09-26

## Estado da rodada

A fase de acabamento editorial foi concluída nos cinco cadernos correntes. As versões abaixo passam a constituir o **congelamento editorial** da rodada de 26/09/2026.

Não foram reabertas auditorias de dados já encerradas, não foram produzidos novos gráficos e os números estruturantes consolidados não foram alterados.

## Governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`
- Branch: `feature/cnpj-territorial-control-v1`
- PR #41: **OPEN + DRAFT + UNMERGED**
- Não fazer merge sem autorização explícita do usuário.
- Caderno-Base Territorial v028: antecedente preservado em somente leitura.
- Caderno-Base Territorial v029: base técnica corrente.
- `Painel_final_v003` permanece ativo distinto.

## Versões editoriais congeladas

| Caderno | Versão | Google Doc ID | Prioridades / condições |
|---|---|---|---:|
| Comércio de Bens Essenciais | v005 — congelamento editorial — 20260926 | `1y7uXCTHiMnD8o0tuhAn2ikR0uQJ3Yer4rSFoujS2qS0` | 8 / 8 |
| Saúde, Higiene e Cuidados Pessoais | v005 — congelamento editorial — 20260926 | `1_UEEkci4sYrVkDOFjVDIreu5r0vFHLbxSQEXBKso4DQ` | 8 / 8 |
| Bens Não Essenciais | v005 — congelamento editorial — 20260926 | `1q5SUsMnj92ouwSxh9AOfita7ukmZ3f87uJFDBvB2wec` | 10 / 10 |
| Alimentação Fora do Lar e Serviços | v005 — congelamento editorial — 20260926 | `1mdk-QHcQT7injbBh1oan0ZH6ksg7OkABMZl9_LBGA7o` | 10 / 10 |
| Caderno Geral | v006 — congelamento editorial — 20260926 | `1mhwDUMLnez0lw0PMglvL-JINjcDLGAeE8Dn5xKsrJcg` | 8 / 8 |

Checkpoint Drive desta rodada:
`1gQHy3tmNfTuomtT8yAI74pYFTW5UnHHgp6jaKz-Xb90`

## Correções editoriais executadas

### Estrutura dos documentos

Foi identificado problema herdado das versões anteriores: grande quantidade de parágrafos de corpo estava marcada como `HEADING_1`, contaminando navegação e potencialmente sumário/exportação.

Correções de estilo:

- Bens Essenciais: 363;
- Saúde/Higiene: 354;
- BNE: 380;
- Alimentação/Serviços: 431;
- Caderno Geral: 283 correções iniciais, mais 22 entradas de sumário/sequência de uso corrigidas.

Estrutura final:

| Caderno | H1 | H2 |
|---|---:|---:|
| Bens Essenciais | 30 | 43 |
| Saúde/Higiene | 30 | 47 |
| BNE | 31 | 45 |
| Alimentação/Serviços | 32 | 47 |
| Geral | 26 | 30 |

### Sumários

Os títulos numerados dos sumários foram confrontados com os títulos reais do corpo.

Divergências corrigidas:

- Saúde: seção 7;
- BNE: seções 5 e 6;
- Alimentação/Serviços: seção 9.

Estado final: **zero divergências detectadas entre os títulos numerados do sumário e os títulos do corpo**.

### Prova textual e tipográfica

Foram tratados:

- referências cruzadas de versão;
- crases e regências residuais;
- duplicação de expressão em BNE;
- espaço duplo em título de exercício;
- aspas retas em BNE;
- hífen simples usado como separador editorial;
- anglicismos dispensáveis como `playbook` e `lead`;
- espaços literais usados para simular recuo no sumário do Caderno Geral;
- formulações ainda excessivamente causais ou determinísticas.

A distribuição RAIS no Caderno Geral passou a ser descrita como **heterogeneidade remuneratória**, sem convertê-la diretamente em capacidade domiciliar de desembolso.

## Consistência entre versões

- quatro reports setoriais v005 → Caderno Geral v006;
- Caderno Geral v006 → quatro reports setoriais v005;
- zero referências editoriais a report v004;
- v028 apenas como antecedente em somente leitura;
- v029 como base técnica corrente;
- `Painel_final_v003` preservado como ativo distinto.

Também não restaram ocorrências editoriais de:

- `read-only`;
- `market size`;
- `acabamento editorial`;
- espaços duplos tipográficos detectados pelo controle automatizado.

## Controles numéricos preservados

### Bens Essenciais

- demanda modelada mensal: R$ 19.558.852,34;
- demanda modelada anual: R$ 234.706.228,14;
- CNPJs documentalmente validados: 52/54 = 96,30%;
- Censo 2022: mediana domiciliar per capita R$ 1.100,00 por pessoa/mês;
- RAIS 2024: 56,57% dos vínculos até 2 SM; 81,33% até 3 SM.

### Saúde/Higiene

- CNES privado: 23 registros/CNPJs;
- 7 raízes;
- 20/23 em raízes multiunidade;
- maior raiz: 8/23;
- posição 22/09/2026.

### BNE

- cenário-base: 122 storefronts;
- sensibilidade: 121;
- 109 `operator_keys`;
- 21 storefronts em raízes multiunidade;
- 17,21%;
- cobertura temática REGIC: 64/122 = 52,46%.

### Alimentação/Serviços

- 947 SINAC;
- 728 SIMEI;
- CNAE 56: 409 estabelecimentos;
- filiais de matriz externa: 0,98%;
- PNAE/B2G: R$ 869.843,54 pagos no universo CNPJ auditado;
- local: R$ 327.021,02 = 37,60%;
- externo: R$ 542.822,52 = 62,40%;
- agricultura familiar/agroindústria: R$ 447.585,44 contratados.

## Não respondíveis preservados

Sem base adicional compatível, permanecem não respondíveis:

- market share por operador/formato/empresa;
- retenção/vazamento monetário municipal;
- gasto efetivo de visitantes;
- participação econômica real do e-commerce local;
- elasticidades preço/conveniência;
- efeito causal do digital sobre vendas;
- impacto monetário de políticas públicas sobre vendas privadas;
- causalidade entre ciclos agro/macroeconômicos e vendas empresariais.

## Regra do congelamento

Não reabrir análise, número ou interpretação sem:

- evidência material nova;
- contradição entre fonte e texto;
- erro aritmético;
- erro de unidade/período/geografia;
- mudança oficial de base/metodologia;
- inconsistência entre setorial e Geral;
- solicitação explícita do usuário.

Correções estritamente ortográficas ou de layout podem ser feitas sem reabrir o conteúdo analítico, desde que registradas.

## Próxima fase

A camada analítica/editorial está congelada.

A próxima fase, quando solicitada, é de **produção/entrega**:

1. inspeção visual final em modo de página;
2. conferência de quebras, tabelas, figuras e legendas;
3. padronização final de capa, cabeçalho e rodapé, se necessária;
4. exportação para PDF;
5. validação visual dos PDFs;
6. manifesto final de entregáveis.

Não priorizar nova pesquisa externa nem novos gráficos.

## Checkpoint anterior

- Drive: `1GjUDRt-7cdouuFrE5S8Ba0N5KTW4D-SQXtXM3dDBL0Y`
- GitHub: `docs/caderno_base/checkpoint_20260926_handoff_pos_qa_v001.md`
- commit: `1562646aeb7857c1da323d06761e33a9bdc91f72`
