# PMSB — diagnóstico da rota de contratos

## Objetivo

Probe exploratório da página oficial:

`https://transparencia.saoborja.rs.gov.br/acordos`

Finalidade: identificar parâmetros e rotas dinâmicas para futura extração **censitária e reproduzível** de contratos municipais, mantendo esta camada separada de:

- processos de Licitações;
- termos aditivos;
- empenhos/liquidações;
- pagamentos.

O probe **não promove valores de contratos como execução financeira**.

## Resultado observado — 19/09/2026

### Página inicial

- GET `/acordos`: HTTP 200;
- instituição Prefeitura Municipal de São Borja: valor interno **1**;
- Câmara de Vereadores: valor interno **3**;
- script específico: `/js/acordos/index.js`.

O JavaScript da página confirma que a lista de exercícios é carregada por:

`/acordos/buscarExercicios/{instituicao}`

Para a Prefeitura (`instituicao=1`), o endpoint retornou oficialmente os exercícios:

**2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 e 2026.**

Isso confirma que o módulo de contratos possui cobertura histórica de, no mínimo, **2018–2026** na camada de seleção.

### Rota de pesquisa

A rota:

`/acordos/pesquisar`

responde HTTP 200.

Foram testadas chamadas GET e POST para 2019–2025. A resposta recebida é uma página de resultado/estrutura, mas os registros contratuais não ficaram expostos diretamente no corpo HTML da primeira tentativa.

**Conclusão:** a rota é acessível; a etapa ainda aberta é localizar a chamada assíncrona ou estrutura interna que carrega as linhas do resultado.

Isso é diferente do bloqueio SIAPC: aqui há conectividade, página, instituição, exercícios e rota funcional; falta completar o mapeamento do mecanismo de dados.

## Evidência técnica

Arquivo:

`diagnostics.json`

Registra:

- status HTTP;
- lista de instituições;
- endpoint de exercícios;
- cobertura 2018–2026;
- JavaScript `/js/acordos/index.js`;
- testes GET/POST da rota `/acordos/pesquisar`;
- candidatos de rotas encontrados.

## Implicação para o histórico B2G

A camada de contratos é uma rota oficial viável para complementar:

`docs/data_sources/sao_borja_licitacoes_history_2019_2025/licitacoes_processos_2019_2025.csv`

O piloto Fundação Ivan Goulart/HIG já mostrou que a camada contratual recupera informação que pode não estar explícita no resumo do processo.

Artefato relacionado:

`docs/data_sources/sao_borja_hig_contracts_history_2020_2025/`

## Próxima ação

1. identificar a chamada de dados usada pela página de resultados;
2. extrair contratos da Prefeitura por exercício 2019–2025;
3. construir chave/crosswalk entre processo, contrato e aditivo;
4. identificar contratado/CNPJ, objeto, valor-base, vigência e origem declarada;
5. manter pagamento realizado em camada separada.

## Limitações

- cobertura de exercícios no seletor não prova completude de todos os contratos;
- contrato publicado não equivale a empenho, liquidação ou pagamento;
- valor estimado/mensal/aditivo requer controle de temporalidade;
- aditivos podem substituir ou modificar componentes, não necessariamente acrescentar fluxos independentes;
- o endpoint de linhas contratuais ainda não foi fechado nesta rodada.

