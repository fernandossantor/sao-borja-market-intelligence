# TJRS — roster territorial e cargos por comarca — v027

**Data da auditoria:** 2026-09-12  
**Geografia:** São Borja/RS  
**Escopo:** localizar chave territorial oficial para futura reconciliação da folha do TJRS.

## 1. Resultado principal

O TJRS **não está mais bloqueado por ausência de fonte territorial**.

A página oficial **Relação de Membros da Magistratura e Demais Agentes Públicos**, conforme a Resolução CNJ nº 102/2009 — Anexo V, publica arquivos mensais em PDF e CSV. O relatório de **31/07/2026** possui explicitamente as colunas:

- Nome;
- Numfunc;
- Tipo de Vínculo;
- Lotação.

A leitura documental confirma múltiplas lotações vinculadas a São Borja.

**Decisão metodológica:** usar o Anexo V como roster territorial mensal e reconciliá-lo com a folha de julho/2026. Nomes e identificadores devem permanecer apenas no ambiente transitório de crosswalk; os artefatos promovidos armazenam apenas agregados.

## 2. Fonte oficial — julho/2026

Página:
`https://www.tjrs.jus.br/novo/institucional/transparencia/transparencia-e-prestacao-de-contas/gestao-de-pessoas/relacao-de-membros-da-magistratura-e-demais-agentes-publicos/`

PDF oficial:
`https://www.tjrs.jus.br/static/2026/08/2026-07-relacao-de-membros-da-magistratura-e-demais-agentes-publicos.pdf`

CSV oficial publicado:
`https://www.tjrs.jus.br/static/2026/08/2026-07-relacao-de-membros-da-magistratura-e-demais-agentes-publicos.csv`

### Controle de transporte

A URL do CSV é explicitamente publicada pelo TJRS, mas:

- a ferramenta de navegação reconheceu a URL e o MIME `text/csv`, sem renderizá-lo;
- o ambiente de container não conseguiu baixar o domínio;
- runners GitHub usados nesta auditoria também apresentaram timeout para o domínio TJRS;
- Google Sheets `IMPORTDATA`, testado em HTTPS e HTTP, também não conseguiu transferir o CSV.

**Classificação:** limitação do canal de transporte, não ausência da fonte.

Não usar contagem manual de ocorrências no PDF como contagem canônica de vínculos.

## 3. Exemplos de lotações territoriais observadas

Sem persistir nomes pessoais, o Anexo V de julho/2026 contém registros com lotações como:

- Foro de São Borja;
- Comarca de São Borja;
- 1ª e 2ª Varas Cíveis de São Borja;
- 1ª e 2ª Varas Criminais de São Borja;
- Juizado Especial Cível de São Borja;
- Central de Cumprimento Cartorário de São Borja;
- Central de Atendimento ao Público de São Borja;
- Central de Mandados — Direção do Foro de São Borja;
- UNICAA - Multicom - São Borja;
- CEJUSC de São Borja.

Isso demonstra a existência de uma chave territorial funcional suficientemente explícita para um crosswalk documental.

## 4. Quantitativo de cargos providos — junho/2026

**Fonte:** TJRS — Quantitativo de Cargos Providos nas Comarcas.  
**Referência:** junho/2026.  
**Unidade:** cargos providos.

### Comarca de São Borja

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

**Controle conceitual:** os 32 cargos providos em junho/2026 não são substituto da quantidade de pessoas do Anexo V de julho/2026. Período e universo são diferentes; o Anexo V inclui magistrados e demais agentes públicos.

## 5. Benchmark absoluto — mesma fonte/mês

| Comarca | Cargos providos | Razão vs. São Borja |
|---|---:|---:|
| São Borja | 32 | 100,00% |
| Alegrete | 30 | 93,75% |
| São Gabriel | 29 | 90,63% |
| Santiago | 36 | 112,50% |
| Sant'Ana do Livramento | 36 | 112,50% |
| Uruguaiana | 56 | 175,00% |

**Interpretação:** São Borja ocupa posição intermediária no grupo comparável em número absoluto de cargos providos.

**Limitação:** não há ajuste por população jurisdicionada, volume processual, número de unidades, especialização ou extensão territorial; portanto, o benchmark não mede eficiência, acesso à Justiça nem intensidade de renda.

## 6. Estado da folha remuneratória

A página oficial de Gestão de Pessoas também oferece:

- **Folha de Pagamento — Detalhamento**, com pesquisa individual;
- **Folha de Pagamento — Consolidada**, com seleção de ano, mês e tipo de folha e saída informada em PDF/CSV.

O workflow `tjrs-transparency-api-deep-probe` confirmou que o bloqueio anterior era de conectividade dos runners, não de inexistência documental:

- DNS resolvido para `177.66.6.143`;
- 18/18 tentativas HTTPS ao Swagger/OpenAPI expiraram;
- nenhum schema foi recuperado.

O workflow `tjrs-payroll-page-backend-discovery` também falhou por timeout ao `www.tjrs.jus.br`.

**Decisão:** parar de tratar a API como pré-requisito. O caminho prioritário é **Anexo V mensal → roster São Borja → folha normal de julho/2026 → crosswalk privado → agregados**.

## 7. Próxima etapa

1. Obter o CSV oficial do Anexo V por canal compatível.
2. Filtrar `Lotação` por São Borja.
3. Obter a folha normal de julho/2026 em formato estruturado.
4. Reconciliar identificadores/nome apenas em ambiente transitório privado.
5. Auditar duplicidades, vínculos múltiplos, afastamentos e parcelas eventuais.
6. Promover somente agregados.

### Status atual

- **Roster territorial oficial:** VALIDADO.
- **Estrutura de cargos por comarca:** PROMOVIDA.
- **Massa remuneratória TJRS/São Borja:** NÃO PROMOVIDA.
- **Motivo:** crosswalk roster × folha ainda pendente.

## 8. Artefatos Drive

Planilha v027:
`1HjfbGo8qA2ZydfCrbouBVjlHDo8DRZs04H3cYr_FKMo`

Abas:
- `TJRS_lotacao_jul2026_v027`
- `TJRS_benchmark_cargos_v027`
- `TJRS_api_probe_v027`
- `Auditoria_v027`

Caderno narrativo v027:
`1g2xnVccRF8Eu-JRVCpwJb2wZodgbymuFdhOaVW1G2y4`

Registro metodológico v027:
`1TL2Hd6SmcjxPPck8v49VSyvZjQAK9sUH5IHRM2FNACM`

## 9. Governança

PR #41 deve permanecer **aberto, draft e sem merge**.

Branch:
`feature/cnpj-territorial-control-v1`

Nenhuma integração à `main` está autorizada.


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
