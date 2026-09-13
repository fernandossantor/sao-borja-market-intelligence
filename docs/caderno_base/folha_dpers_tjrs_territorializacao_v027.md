# Caderno-Base Territorial — v027 — territorialização DPERS/TJRS

**Data:** 2026-09-12  
**Geografia:** São Borja/RS  
**Objeto:** aprofundar a folha pública estadual fora do Executivo, preservando diferença entre lotação, exercício, residência e remuneração.

## Artefatos canônicos no Drive

- Planilha v027: `1HjfbGo8qA2ZydfCrbouBVjlHDo8DRZs04H3cYr_FKMo`
- Caderno narrativo v027: `1g2xnVccRF8Eu-JRVCpwJb2wZodgbymuFdhOaVW1G2y4`
- Registro metodológico v027: `1TL2Hd6SmcjxPPck8v49VSyvZjQAK9sUH5IHRM2FNACM`

Novas abas:

- `DPERS_roster_recon_v027`
- `DPERS_remuneracao_v027`
- `TJRS_api_probe_v027`
- `Auditoria_v027`

## 1. DPERS — problema metodológico

A folha oficial de julho/2026 é estruturada, mas não contém comarca, município, lotação, unidade ou sede.

**Fonte:** Defensoria Pública do Estado do Rio Grande do Sul — Portal da Transparência.  
**Competência:** julho/2026.  
**Abrangência original:** Estado do RS.

Registros auditados:

- defensores ativos: **449**;
- servidores ativos: **881**.

Por isso, a territorialização foi construída em duas etapas:

1. reconstruir um roster mínimo por atos oficiais de lotação, remoção, exoneração, vacância, afastamento, designação e acumulação;
2. reconciliar esse roster com a folha oficial.

Nomes e remunerações individuais não são promovidos para os artefatos do projeto.

## 2. Roster documental DPERS — julho/2026

### Núcleo estrito

**DADO CALCULADO a partir de documentação funcional corrente:**

- 3 posições por lotação documental;
- 2 dessas posições estavam em **efetivo exercício** na competência.

O núcleo inclui:

- titular da 1ª Defensoria Pública de São Borja;
- titular da 2ª Defensoria Pública de São Borja, embora afastada na folha do mês;
- uma Técnica-Administrativa com ato de lotação na Defensoria Pública Regional de São Borja em 2026.

### 3ª Defensoria Pública

**DADO OBSERVADO:** o cargo titular aparece **vago**.

A unidade recebeu cobertura temporária por designações/acumulações.

**Regra:** não criar salário titular fictício e não apropriar a remuneração-base integral de agentes lotados em outras unidades.

### Núcleo ampliado provável

**ESTIMATIVA DOCUMENTAL CONTROLADA:** 4 posições por lotação provável e 3 em exercício.

O quarto vínculo é uma Analista-Processual formalmente lotada em São Borja em 2024, ativa na folha de julho/2026, para a qual não foi localizado movimento posterior na busca dirigida.

**Limitação:** ausência de ato posterior recuperado não equivale a confirmação oficial corrente do roster. Portanto, o vínculo entra apenas no envelope ampliado.

### Exclusões

Foram explicitamente excluídos:

- vínculos removidos de São Borja em 2025;
- vínculos locais encerrados por exoneração em fevereiro e março de 2026.

Isso evita atribuir folha local apenas porque a pessoa continua presente no arquivo estadual.

## 3. Conceito de remuneração mensal bruta recorrente

**Fonte conceitual:** Resolução DPGE nº 13/2018.

A definição oficial exclui, entre outros itens, férias, substituições, acumulações, gratificação natalina, retroativos, abono de permanência, verbas indenizatórias e pagamentos eventuais.

No CSV oficial resumido de julho/2026, as categorias relevantes são:

- [1] REMUNERAÇÃO;
- [2] FG / GD;
- [3] VANTAGENS TEMPORAIS;
- [4] GRATIFICAÇÃO NATALINA;
- [5] FÉRIAS / LICENÇA-PRÊMIO;
- [6] ABONO PERMANÊNCIA;
- [7] INDENIZAÇÕES.

### Fórmula SBMI

`remuneração mensal bruta recorrente = [1] + [2] + [3]`

Antes da agregação, o CSV detalhado foi usado como controle para evitar manter parcela de substituição dentro de [1].

## 4. DPERS — envelopes agregados

### Núcleo estrito — lotação

**Natureza:** DADO CALCULADO.  
**Posições:** 3.

| Item | Valor |
|---|---:|
| [1] Remuneração | R$ 65.854,34 |
| [2] FG/GD | R$ 610,10 |
| [3] Vantagens temporais | R$ 0,00 |
| **Remuneração mensal bruta recorrente** | **R$ 66.464,44** |
| Itens [1]–[7] antes de estornos/descontos | R$ 87.911,55 |
| Descontos obrigatórios | R$ 20.590,25 |
| Total líquido oficial | R$ 67.321,30 |

### Núcleo estrito — efetivo exercício

**Natureza:** DADO CALCULADO.  
**Posições:** 2.

- remuneração mensal bruta recorrente: **R$ 35.348,98**;
- itens [1]–[7]: R$ 50.545,60;
- descontos obrigatórios: R$ 10.303,47;
- total líquido oficial: R$ 40.242,13.

### Núcleo ampliado — lotação provável

**Natureza:** ESTIMATIVA DOCUMENTAL CONTROLADA.  
**Posições:** 4.

- [1] Remuneração: R$ 75.080,33;
- [2] FG/GD: R$ 610,10;
- [3] vantagens temporais: R$ 0,00;
- **remuneração mensal bruta recorrente: R$ 75.690,43**;
- itens [1]–[7]: R$ 99.804,37;
- descontos obrigatórios: R$ 22.408,05;
- total líquido oficial: R$ 77.396,32.

### Núcleo ampliado — efetivo exercício provável

**Natureza:** ESTIMATIVA DOCUMENTAL CONTROLADA.  
**Posições:** 3.

- remuneração mensal bruta recorrente: **R$ 44.574,97**;
- itens [1]–[7]: R$ 62.438,42;
- descontos obrigatórios: R$ 12.121,27;
- total líquido oficial: R$ 50.317,15.

## 5. Substituições e acumulações

A remuneração-base integral de substitutos externos **não** é atribuída a São Borja.

Apenas uma parcela adicional de substituição/acumulação poderia ser territorializada, desde que a própria folha ou outro documento oficial permita ligá-la à designação específica em São Borja.

A 3ª Defensoria vaga não gera salário titular fictício.

## 6. Ordem de grandeza da folha pública não municipal

Subtotal documental já registrado na v025:

**R$ 9.551.979,21/mês**

Escopo do subtotal anterior: federal civil parcial + Executivo estadual + MPRS.

### Com DPERS — núcleo estrito de lotação

**R$ 9.618.443,65/mês**

### Com DPERS — núcleo ampliado provável

**R$ 9.627.669,64/mês**

Esses valores continuam sendo **ordens de grandeza documentais**, não massa salarial pública total de São Borja.

## 7. TJRS — estado da auditoria

Fontes oficiais:

- página **API de Dados Abertos** do TJRS;
- **Folha de Pagamento de Pessoal Consolidada**;
- Swagger oficial hospedado em `adm-inter.tjrs.jus.br`.

### Deep probe

Workflow: `tjrs-transparency-api-deep-probe`  
Run: `34726826100`  
Artifact: `10308660088`

**DADOS OBSERVADOS — auditoria técnica:**

- DNS: `adm-inter.tjrs.jus.br → 177.66.6.143`;
- 9 rotas Swagger/OpenAPI testadas;
- cada rota em modo padrão e IPv4 forçado;
- total: **18 tentativas**;
- 18/18 terminaram por timeout de conexão TCP/443;
- HTTP `000`;
- zero bytes recebidos;
- nenhum schema recuperado.

### Interpretação

O resultado demonstra **falha de alcançabilidade da API a partir do runner GitHub**.

Não demonstra:

- inexistência da API;
- indisponibilidade pública geral;
- ausência de campos territoriais.

## 8. Pivô TJRS — relatório oficial de folha

A página oficial da Folha Consolidada permite selecionar ano, mês e tipo de folha.

Um **espelho externo**, não oficial, de relatório do TJRS baseado na Resolução CNJ nº 102 — Anexo VIII sugere a existência de uma coluna **“Local de Origem (15)”**.

**Classificação atual:** INDÍCIO EXTERNO — NÃO PROMOVIDO.

A coluna somente poderá ser usada após verificação em documento ou resposta oficial do TJRS.

Foi criado o workflow:

`tjrs-payroll-page-backend-discovery`

Objetivos:

1. baixar a página oficial da folha;
2. identificar forms, scripts e endpoints;
3. localizar a rota real usada pelo filtro;
4. encontrar o relatório oficial;
5. verificar se existe campo territorial no relatório.

## 9. Critério de promoção TJRS

Somente agregar valor TJRS/São Borja quando houver:

1. campo territorial explícito na própria fonte remuneratória oficial; **ou**
2. roster oficial mensal de lotação/unidade reconciliável com a folha nominal.

Não usar cargo, nome, atuação processual, notícia, residência ou município de origem como proxy de lotação.

## 10. Limitações

- folha bruta ≠ renda líquida;
- lotação/exercício ≠ residência;
- remuneração ≠ gasto local;
- afastamento não elimina necessariamente vínculo de lotação;
- substituição temporária não transfere toda a remuneração do substituto para a unidade substituída;
- ausência de movimento posterior em pesquisa documental não prova continuidade absoluta;
- nenhum envelope DPERS é apresentado como total oficial completo da instituição em São Borja.

## 11. Governança

PR #41 deve permanecer:

- **aberto**;
- **draft**;
- **sem merge**.

Branch: `feature/cnpj-territorial-control-v1`.

Nenhuma integração à `main` está autorizada sem aprovação explícita do usuário.
