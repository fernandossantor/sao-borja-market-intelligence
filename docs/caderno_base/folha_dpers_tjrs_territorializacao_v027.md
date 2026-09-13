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

## 6. Ordem de grandeza da folha pública não municipal — correção conceitual

A v025 registrou:

**R$ 9.551.979,21/mês**

como ordem de grandeza documental para federal civil parcial + Executivo estadual + MPRS.

### Auditoria conceitual

A base v025 já combina conceitos remuneratórios não perfeitamente homogêneos:

- federal civil: remuneração básica bruta;
- Executivo estadual: remuneração bruta da fonte estadual;
- MPRS: Total Bruto da folha normal.

A DPERS permite separar **remuneração mensal bruta recorrente** de um **envelope bruto amplo [1]–[7]**.

Por isso, a inclusão da DPERS é mantida como **SENSIBILIDADE**, e não como novo subtotal canônico.

### Sensibilidade — componente recorrente DPERS

- núcleo estrito: R$ 9.551.979,21 + R$ 66.464,44 = **R$ 9.618.443,65/mês**;
- núcleo ampliado provável: R$ 9.551.979,21 + R$ 75.690,43 = **R$ 9.627.669,64/mês**.

### Sensibilidade — envelope bruto amplo DPERS

- núcleo estrito: R$ 9.551.979,21 + R$ 87.911,55 = **R$ 9.639.890,76/mês**;
- núcleo ampliado provável: R$ 9.551.979,21 + R$ 99.804,37 = **R$ 9.651.783,58/mês**.

**Regra:** nenhum dos quatro resultados é promovido como total homogêneo da folha pública. Eles demonstram apenas a sensibilidade da ordem de grandeza anterior à incorporação da DPERS sob conceitos alternativos.

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

## 8. Pivô TJRS — roster territorial oficial validado

A auditoria localizou uma fonte oficial que elimina a dependência conceitual da API para territorialização:

**TJRS — Relação de Membros da Magistratura e Demais Agentes Públicos — Resolução CNJ nº 102/2009, Anexo V.**

O relatório de **31/07/2026** é publicado oficialmente em PDF e CSV e possui as colunas `Nome`, `Numfunc`, `Tipo de Vínculo` e **`Lotação`**. A leitura documental confirma múltiplas lotações associadas a São Borja.

Página oficial:

`https://www.tjrs.jus.br/novo/institucional/transparencia/transparencia-e-prestacao-de-contas/gestao-de-pessoas/relacao-de-membros-da-magistratura-e-demais-agentes-publicos/`

PDF julho/2026:

`https://www.tjrs.jus.br/static/2026/08/2026-07-relacao-de-membros-da-magistratura-e-demais-agentes-publicos.pdf`

CSV oficial publicado:

`https://www.tjrs.jus.br/static/2026/08/2026-07-relacao-de-membros-da-magistratura-e-demais-agentes-publicos.csv`

**Resultado:** o TJRS passa de “chave territorial não demonstrada” para **ROSTER TERRITORIAL OFICIAL DISPONÍVEL**.

### Limitação de transporte

A URL do CSV é explicitamente publicada pelo TJRS, mas os canais técnicos usados nesta auditoria não conseguiram transferir o arquivo:

- a navegação reconhece o URL/MIME `text/csv`, mas não o renderiza;
- o container não conseguiu baixar o domínio;
- o runner GitHub sofreu timeouts no domínio TJRS;
- Google Sheets `IMPORTDATA`, testado por HTTPS e HTTP, também não conseguiu transferir o CSV;
- os workflows de proxy neutro para o CSV e para o PDF retornaram HTTP 422, sem recuperar o conteúdo.

Isso é uma limitação de transporte, não ausência da fonte. Não usar contagem manual de ocorrências do PDF como contagem canônica de vínculos.

## 9. TJRS — estrutura de cargos providos

**Fonte:** TJRS — Quantitativo de Cargos Providos nas Comarcas.  
**Referência:** junho/2026.  
**Unidade:** cargos providos.

### São Borja

| Cargo | Quantidade | Participação |
|---|---:|---:|
| Analista do Poder Judiciário — Área Administrativa | 1 | 3,13% |
| Analista do Poder Judiciário — Área Judiciária | 2 | 6,25% |
| Analista do Poder Judiciário — Serviço Social | 1 | 3,13% |
| Auxiliar de Serviços Gerais | 1 | 3,13% |
| Oficial Ajudante | 1 | 3,13% |
| Oficial de Justiça Estadual | 7 | 21,88% |
| Técnico do Poder Judiciário | 19 | 59,38% |
| **Total** | **32** | **100,00%** |

**Controle conceitual:** os 32 cargos providos em junho não equivalem à quantidade de pessoas do Anexo V de julho. Períodos e universos diferem.

### Benchmark absoluto — mesma fonte e mês

| Comarca | Cargos providos | Razão vs. São Borja |
|---|---:|---:|
| São Borja | 32 | 100,00% |
| Alegrete | 30 | 93,75% |
| São Gabriel | 29 | 90,63% |
| Santiago | 36 | 112,50% |
| Sant'Ana do Livramento | 36 | 112,50% |
| Uruguaiana | 56 | 175,00% |

**Interpretação:** São Borja ocupa posição intermediária no grupo selecionado em número absoluto de cargos providos.

**Limitação:** não há normalização por população jurisdicionada, volume processual, quantidade de unidades, especialização ou extensão territorial.

## 9.1 Critério de promoção remuneratória TJRS

A existência de `Lotação` no Anexo V resolve a chave territorial, mas **não resolve automaticamente a massa remuneratória**.

Próxima sequência:

1. obter o CSV oficial do Anexo V por canal compatível;
2. filtrar privadamente lotações contendo São Borja;
3. obter a folha normal de julho/2026 em formato estruturado;
4. reconciliar roster × folha;
5. auditar duplicidades, vínculos múltiplos e parcelas eventuais;
6. publicar somente agregados.

**Status atual:**

- roster territorial oficial: **VALIDADO**;
- estrutura de cargos por comarca: **PROMOVIDA**;
- massa remuneratória TJRS/São Borja: **NÃO PROMOVIDA**.

Não usar cargo, nome, atuação processual, notícia, residência ou município de origem como proxy de lotação.



## 9.2 Controle estrutural — TLP × cargos providos

As Tabelas de Lotação de Pessoal do TJRS fornecem um controle adicional independente.

**TLP 1 — referência 31/12/2025:** seis unidades judiciárias de São Borja somam `LR_EFET = 16`.

**TLP 2 — referência 01/01/2026:** quatro unidades de apoio direto identificadas em São Borja somam `LR_EFET = 16`.

**TLP 3 — referência 01/01/2026:** não foi localizada unidade territorial em São Borja na busca documental.

Portanto:

`LR_EFET TLP1 + TLP2 = 16 + 16 = 32`.

O relatório **Quantitativo de Cargos Providos nas Comarcas**, de junho/2026, registra também **32 cargos providos** em São Borja.

**DADO CALCULADO:** diferença = 0; razão de consistência = 100%.

**Classificação:** **COERÊNCIA CRUZADA FORTE**, não prova de identidade. Os períodos e conceitos diferem; movimentações podem ocorrer mantendo a mesma contagem. O valor 32 deve ser usado como controle estrutural do núcleo efetivo, não como total de pessoas remuneradas pelo TJRS no município.

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


## Atualização normativa CNJ — unidade de efetivo exercício

**DADO NORMATIVO.** O art. 3º, VI, da Resolução CNJ nº 102/2009, com redação dada pela Resolução nº 151/2012, exige que a transparência remuneratória identifique nominalmente o beneficiário e a **unidade na qual efetivamente presta os seus serviços**.

A disciplina posterior reforça essa chave territorial. A Resolução CNJ nº 215/2015, com redação da Resolução nº 273/2018, determina detalhamento individualizado da remuneração e da unidade de efetivo exercício. O Anexo I do marco consolidado, no quadro **“Detalhamento da folha de pagamento de pessoal”**, inclui explicitamente as colunas **Nome, Lotação e Cargo**, além das rubricas de rendimentos, descontos e rendimento líquido.

Fontes oficiais CNJ:

- Resolução nº 102/2009: `https://atos.cnj.jus.br/atos/detalhar/69`
- Resolução nº 151/2012: `https://atos.cnj.jus.br/atos/detalhar/68`
- Resolução nº 215/2015: `https://atos.cnj.jus.br/atos/detalhar/2236`
- Resolução nº 273/2018: `https://atos.cnj.jus.br/atos/detalhar/2791`

**DADO OBSERVADO — TJRS.** A página oficial **Detalhamento da Folha de Pagamento de Pessoal** (`https://www.tjrs.jus.br/novo/institucional/transparencia/fpp/`) permite selecionar ano, mês, tipo de folha, cargo e nome e informa que a consulta atende às normas de transparência do CNJ. A página-mãe de Gestão de Pessoas distingue esse detalhamento da Folha Consolidada e do Anexo V.

**CONTROLE METODOLÓGICO.** A obrigação normativa não prova, sozinha, que o output TJRS recuperável pelo projeto já foi observado contendo `Lotação`. A implementação técnica do arquivo/resultado de julho de 2026 ainda precisa ser verificada.

**ROTA PRIORITÁRIA ATUALIZADA:**

1. recuperar o output oficial do Detalhamento da Folha de julho/2026 e verificar diretamente `Lotação`/unidade de efetivo exercício;
2. se houver exportação estruturada com a chave territorial, agregar São Borja diretamente;
3. se o detalhamento não puder ser extraído em lote ou não expuser a chave no formato acessível, usar o Anexo V mensal como roster oficial e reconciliá-lo com a Folha Consolidada ou consultas individuais;
4. usar TLP e quantitativo de cargos apenas como controles de estrutura e plausibilidade.

**STATUS:** chave territorial funcional **VALIDADA** pelo Anexo V; obrigação normativa de unidade de efetivo exercício **VALIDADA** pelo CNJ; output remuneratório TJRS com `Lotação` **AINDA NÃO OBSERVADO**; massa remuneratória TJRS/São Borja **NÃO PROMOVIDA**.


## Atualização v027 — contracheque único e envelope estatutário TJRS

### Regra CNJ vigente em 2026

A Resolução CNJ nº 681/2026 introduziu o **contracheque único**. No texto compilado da Resolução CNJ nº 215/2015, os dados remuneratórios publicados devem originar-se exclusivamente do contracheque único, vedada a divulgação de informações parciais ou fragmentadas que não correspondam ao total efetivamente pago no mês.

Isso muda a regra de agregação do SBMI: os tipos de folha `Normal`, `Complementar`, `Mensal Complementar` e `Complementar Extraordinária` **não podem ser somados mecanicamente**. O objetivo é obter um único total mensal por vínculo/pessoa, territorializado por `Lotação`/unidade de efetivo exercício.

Fontes CNJ:

- Resolução nº 215/2015: `https://atos.cnj.jus.br/atos/detalhar/2236`
- Resolução nº 273/2018: `https://atos.cnj.jus.br/atos/detalhar/2791`
- Resolução nº 681/2026: `https://atos.cnj.jus.br/atos/detalhar/1349`

### Envelope estatutário de vencimento básico

**Estrutura observada:** 32 cargos providos na Comarca de São Borja em junho/2026.

| Grupo | Qtde. | Mínimo legal | Máximo legal | Piso ponderado | Teto ponderado |
|---|---:|---:|---:|---:|---:|
| Analista do Poder Judiciário | 4 | R$ 9.226,01 | R$ 18.452,01 | R$ 36.904,04 | R$ 73.808,04 |
| Técnico do Poder Judiciário | 19 | R$ 4.843,63 | R$ 11.993,81 | R$ 92.028,97 | R$ 227.882,39 |
| Oficial de Justiça Estadual | 7 | R$ 7.982,58 | R$ 17.529,42 | R$ 55.878,06 | R$ 122.705,94 |
| Auxiliar de Serviços Gerais | 1 | R$ 2.463,19 | R$ 4.926,38 | R$ 2.463,19 | R$ 4.926,38 |
| Oficial Ajudante | 1 | R$ 8.491,68 | R$ 16.983,37 | R$ 8.491,68 | R$ 16.983,37 |
| **Total** | **32** |  |  | **R$ 195.765,94** | **R$ 446.306,12** |

**Fonte normativa:** Lei Estadual nº 16.390/2025, que altera a Lei nº 15.737/2021.  
Fonte primária DOE-RS: `https://www.diariooficial.rs.gov.br/materia?id=1351751`.

**Classificação:** DADO CALCULADO / ENVELOPE MECÂNICO DE CONTROLE.

Esse intervalo **não é folha real**, não é estimativa central e não entra no subtotal de renda pública. Exclui vantagens pessoais, funções, gratificações, GEA, indenizações, férias, eventuais/retroativos, magistrados e agentes fora do núcleo efetivo de 32.

### Estado do TJRS

- chave territorial: **VALIDADA**;
- estrutura de 32 cargos efetivos: **VALIDADA por duas famílias documentais**;
- envelope estatutário: **PROMOVIDO somente como controle de plausibilidade**;
- massa remuneratória real: **NÃO PROMOVIDA** enquanto faltar output estruturado compatível com contracheque único.

A camada estadual de outros poderes pode ser considerada **fechada no limite documental atual**: MPRS promovido; DPERS promovido por envelopes; TJRS estruturado, mas sem folha real; TCE-RS e ALRS com decisão explícita de não promoção.
