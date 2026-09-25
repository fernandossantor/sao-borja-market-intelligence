# Manifesto de entregáveis finais — SBMI
**Data:** 24/09/2026  
**Projeto:** São Borja — Inteligência Mercadológica

## 1. Regra central de entrega

A arquitetura final do projeto preserva três camadas diferentes:

1. **publicação empresarial** — leitura humana, narrativa contínua, análise orientada à decisão;
2. **apêndice técnico seletivo** — tabelas, fórmulas e notas necessárias ao leitor;
3. **dossiê de auditoria** — planilhas técnicas, Caderno-Base, registros metodológicos, checkpoints, GitHub e derivados auditáveis.

Planilhas e tabelas são lastro técnico. Elas não substituem os reports empresariais.

A sequência argumentativa preferencial é:

`problema → evidência → comparação/contraste → explicação → interpretação → implicação mercadológica → decisão → limitação`.

## 2. Entregáveis principais

### 2.1. Porta de entrada
**Síntese Executiva Empresarial v002**

- documento: `1-EGjPoFqovGzr1EjZgPb3WPpVYIu9cVRRoW1FNZMNj4`
- planilha transversal: `1wR0CkD1UnWrkKGrttGQPRmZL95QB0S4n0BrKJhJNDQw`

Status: atualizado em 24/09/2026, mas deve receber revisão final depois que os cinco reports publicáveis estiverem fechados.

### 2.2. Caderno Geral — Report Empresarial

Protótipo editorial atual:
`1hy7q3HtRbgU2lukpR6X79Z-_o0ITTSOXsVAUl6ykCpI`

Status:
desatualizado em relação ao Caderno-Base v029.

Próxima ação:
criar v003 do Report Empresarial, preservando o padrão editorial de 14/09 e incorporando somente conclusões maduras da v029.

### 2.3. Quatro reports setoriais

#### Comércio de Bens Essenciais
Report empresarial v001:
`1kGIdV5nISJNhQ0JwOg-9PrPS0NdByCN8`

Base técnica corrente:
`1r9p39EaDSdHtxLYyqzahjG6xIaWlO-sNcbFBZBQ3L-c`

#### Saúde, Higiene e Cuidados Pessoais
Report empresarial v001:
`1sgRDFsrBqpjK9vnZ6e1Z0aD4sRZu4eNL`

Base técnica corrente:
`1sJudMz_AFVw1T7xDYwx10TLPSaZyKfXWkD5NU09MMT8`

#### Bens Não Essenciais
Report empresarial v001:
`1mGvIXD0N-F9KMF7Jic-c2-ZZo8x1K6D3`

Base técnica corrente:
`1gNCKoKPj2SECZf3ocNhiXorftSoQgfqDTAbo-_U0e9A`

#### Alimentação Fora do Lar e Serviços
Report empresarial v001:
`1XikL1wQHLGErn7rXLOQATSMiQCH5Cs5f`

Base técnica corrente:
`1BmyJR43OmSp1VDw1nA4oO0iSTna9BiRHs3WYc54Ny3s`

Status dos quatro:
os reports de 14/09 são a base editorial correta, mas precisam incorporar as camadas técnicas v002 fechadas em 24/09.

## 3. Entregáveis estruturantes complementares

### Factsheets
Produzir:
- 1 factsheet territorial;
- 4 factsheets setoriais.

Cada factsheet deve informar:
- indicador;
- valor;
- natureza: observado/calculado/estimado;
- período;
- unidade;
- geografia;
- fonte;
- limitação;
- vínculo de rastreabilidade.

Factsheet não é infográfico promocional sem lastro.

### Storyboards
Produzir:
- 1 storyboard transversal/territorial;
- storyboards setoriais conforme necessidade editorial.

A sequência deve ser:
`evidência → interpretação → consequência prática → decisão apoiada`.

Storyboards podem alimentar PDF, slides ou website, mas não substituem o report.

### Painéis e séries históricas
O painel final deve selecionar séries e indicadores com função analítica, não acumular variáveis por disponibilidade.

Requisitos:
- fonte;
- período;
- unidade;
- natureza do indicador;
- comparabilidade;
- limitação;
- pergunta analítica associada.

### CSVs auditáveis
O pacote final deverá conter um **manifesto dos CSVs promovidos**.

Cada arquivo promovido deve possuir:
- nome;
- domínio;
- origem;
- período;
- estágio: curated/export;
- status: canônico/publicável;
- linhagem;
- hash/snapshot quando disponível;
- observação metodológica.

Arquivos exploratórios não devem aparecer como dados finais.

## 4. PDFs publicáveis

Os cinco PDFs/documentos consolidados em 13/09 foram reclassificados em 14/09 como **versões técnicas intermediárias**, não edições publicáveis.

Portanto, somente após a atualização dos cinco reports empresariais deverão ser regenerados:

1. Caderno Geral;
2. Comércio de Bens Essenciais;
3. Saúde, Higiene e Cuidados Pessoais;
4. Bens Não Essenciais;
5. Alimentação Fora do Lar e Serviços.

As versões finais não devem conter versões históricas empilhadas no mesmo arquivo.

## 5. Parâmetros prioritários permanentes

1. **São Borja é a unidade territorial principal.**
2. Dados regionais só podem ser apresentados como regionais.
3. Diferenciar DADO OBSERVADO, DADO CALCULADO, ESTIMATIVA, BENCHMARK EXTERNO, HIPÓTESE, INTERPRETAÇÃO, RECOMENDAÇÃO e NÃO RESPONDÍVEL.
4. Não comparar universos diferentes sem explicar conceito e unidade.
5. Não converter correlação em causalidade.
6. Não converter contagem de unidades/cadastros em market share.
7. Não converter benchmark nacional em estatística municipal.
8. POM qualitativa não produz prevalência populacional.
9. REGIC não mede gasto.
10. Contrato não é pagamento.
11. Demanda modelada não é faturamento.
12. Não somar fluxos heterogêneos de renda/benefícios/folha/compras públicas.
13. Não abrir nova pesquisa primária no escopo corrente.
14. Não reabrir auditorias já esgotadas sem evidência material nova.
15. Preservar narrativa empresarial e rastreabilidade técnica separadas.

## 6. Governança

- Caderno-Base v028: preservado como antecedente read-only.
- Caderno-Base v029: versão corrente de integração.
- PR #41: permanece aberto, draft e sem merge.
- Nenhuma integração à `main` sem autorização explícita.

## 7. Ordem de execução a partir de 24/09

1. atualizar **Caderno Geral — Report Empresarial** com a v029;
2. atualizar os quatro **reports setoriais** com seus v002 técnicos;
3. revisar a **Síntese Executiva Empresarial**;
4. produzir **factsheets**;
5. produzir **storyboards**;
6. consolidar **painel final e séries prioritárias**;
7. gerar **manifesto dos CSVs promovidos**;
8. regenerar os cinco **PDFs publicáveis**;
9. criar **README/manifesto do pacote final**;
10. executar auditoria editorial e técnica final do pacote.
