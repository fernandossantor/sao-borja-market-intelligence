# Checkpoint — handoff pós-QA textual — 2026-09-26

## Governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`
- Branch: `feature/cnpj-territorial-control-v1`
- PR #41: **OPEN + DRAFT + UNMERGED**.
- Não fazer merge sem autorização explícita do usuário.
- Caderno-Base Territorial v028: **read-only**.
- Caderno-Base Territorial v029: base técnica corrente.
- Gráficos não são prioridade nesta fase.

## Regra de retomada

Retomar exatamente deste ponto. O QA textual profundo dos cinco cadernos foi concluído. A próxima sessão deve priorizar **acabamento editorial + congelamento das versões correntes**, e não nova pesquisa ou reabertura de auditorias já fechadas.

Cadeia metodológica preservada:

`evidência → contexto → relação → mecanismo → interpretação → implicação → decisão → indicador/teste → limite`

## Cinco cadernos correntes

| Caderno | Versão | Google Doc ID | Prioridades / condições de revisão |
|---|---|---|---:|
| Comércio de Bens Essenciais | v004 — QA textual profundo | `1lkTmsTB-oeADdqxPAkG0gneTt4CKBY2R0_aEBPKg07k` | 8 / 8 |
| Saúde, Higiene e Cuidados Pessoais | v004 — QA textual profundo | `17MCoSOZGXNxO2MWfgYF2RnujxAviuAez6-LVyD8RQXM` | 8 / 8 |
| Bens Não Essenciais | v004 — QA textual profundo | `1lILyRBgjj1iZ7B_SO4-tkxgwEMGX_zwRyg2rEj4UOJE` | 10 / 10 |
| Alimentação Fora do Lar e Serviços | v004 — QA textual profundo | `1xUf5c6rsuzIruJmNJTaHVBFSb7Ug0qn0A-PDQVV5YIQ` | 10 / 10 |
| Caderno Geral | v005 — QA textual profundo | `1-9V5hMadSRGhgI-SMcF8b5Q5AZlhYArswaYBkYkdMqg` | 8 / 8 |

Checkpoint Google Drive desta sessão:
`1GjUDRt-7cdouuFrE5S8Ba0N5KTW4D-SQXtXM3dDBL0Y`

## QA concluído

### Causalidade

Formulações determinísticas foram revistas quando a base sustentava apenas associação, mecanismo plausível ou hipótese operacional. Recomendações passaram a exigir teste por indicadores internos, como conversão, recorrência, ticket, margem, ruptura, reclamação, motivo de perda, origem, tempo de resposta ou recompra.

### Renda e orçamento

Censo e RAIS permanecem separados:

- Censo 2022: mediana do rendimento domiciliar per capita = **R$ 1.100,00 por pessoa/mês**.
- RAIS 2024: **56,57%** dos vínculos com remuneração positiva em dezembro em até 2 SM; **81,33%** em até 3 SM.

Esses dados justificam testar restrição de desembolso; não medem consumo individual, gasto setorial ou uma métrica única de capacidade financeira.

### POF

POF 2017–2018 permanece **BENCHMARK EXTERNO**. Não transportar percentuais regionais/nacionais diretamente para São Borja.

### Bens essenciais

`R$ 234.706.228,14/ano` permanece identificado como **ESTIMATIVA MODELADA** de gasto residente com alimentação no domicílio. Para leitura decisória: R$ 234,71 milhões/ano. Não é faturamento observado, market share ou retenção municipal.

### Oferta e market share

- Saúde/Higiene: 23 registros/CNPJs CNES privados; 7 raízes; 20/23 em raízes multiunidade; maior raiz 8/23. Controle Agafarma impede tratar 23 como total exaustivo.
- BNE: 122 storefronts; sensibilidade 121; 109 operator_keys; 8 raízes multiunidade; 21 storefronts em raízes multi. Storefront ≠ CNPJ ≠ raiz ≠ market share.
- Serviços: 947 SINAC; 728 SIMEI. Optante ≠ empresa ativa ≠ ponto físico ≠ faturamento ≠ market share.
- Alimentação: 409 estabelecimentos CNAE 56. Cadastro ≠ operação corrente ≠ participação de vendas.

### POM

- Entrevistas qualitativas não sustentam prevalência populacional.
- Survey online Alimentação/Serviços (n=153) permanece descritivo; recrutamento probabilístico não demonstrado.

### Proxies operacionais formalizados

- Bens Essenciais: proxy de resolução de missão.
- BNE: proxy de resolução por ocasiões registradas atendidas sem falta/abandono conhecido.
- Alimentação/Serviços: taxa de resolução automática baseada em conclusão sem transferência e sem recontato conhecido na janela definida.

Todos são indicadores internos dependentes da qualidade de registro.

## Rastreabilidade

Os cinco cadernos passaram a registrar, quando aplicável:

- fonte;
- período;
- unidade;
- abrangência;
- natureza;
- limitação.

No Caderno Geral, as fontes das Figuras 1–9 foram reforçadas para evitar confusão entre universos, períodos, denominadores e unidades.

## Consistência entre versões

Validação final já executada:

- sem referência editorial obsoleta a reports setoriais v003;
- sem referência a integração editorial v003;
- sem referência a Caderno Geral v004 nos setoriais;
- Caderno Geral v005 referencia os quatro reports setoriais v004;
- `Painel_final_v003` permanece por ser ativo distinto;
- v028 aparece apenas como antecedente read-only;
- prioridades/condições de revisão completas: **8/8, 8/8, 10/10, 10/10, 8/8**.

## Números centrais rechecados

- 52/54 = 96,30%
- 20/23 = 86,96%
- 8/23 = 34,78%
- 21/122 = 17,21%
- 64/122 = 52,46%
- 4/409 = 0,98%
- R$ 327.021,02 / R$ 869.843,54 = 37,60%
- R$ 542.822,52 / R$ 869.843,54 = 62,40%

## Não respondíveis preservados

Sem nova base compatível, continuam não respondíveis, conforme o caderno:

- market share por operador/formato/empresa;
- retenção/vazamento monetário municipal;
- gasto efetivo de visitantes;
- participação econômica real do e-commerce local;
- elasticidades preço/conveniência;
- efeito causal do digital sobre vendas;
- impacto monetário de políticas públicas sobre vendas privadas;
- causalidade entre ciclos agro/macroeconômicos e vendas empresariais.

## Redundância

Foi executado rastreio de similaridade entre parágrafos longos. Não houve duplicação alta que justificasse cortes automáticos. Preservar profundidade argumentativa e remover apenas repetição sem ganho analítico.

## Próxima sessão

### Fase A — acabamento dos quatro setoriais

Ordem sugerida:

1. Bens Essenciais
2. Saúde/Higiene
3. BNE
4. Alimentação/Serviços

Checklist:
- ortografia e pontuação residual;
- consistência de títulos/subtítulos;
- padronização de Fonte/Período/Unidade/Abrangência/Limitação;
- termos-chave;
- numeração;
- tabelas;
- notas e legendas;
- referências internas;
- quebras visuais;
- redundância residual real.

Não alterar números ou interpretações consolidadas sem evidência material de erro.

### Fase B — acabamento do Caderno Geral

Executar depois dos quatro setoriais para garantir coerência das referências cruzadas.

Checar:
- versões citadas;
- exemplos setoriais;
- títulos de figuras/tabelas;
- unidades/períodos;
- prioridades;
- não respondíveis;
- considerações finais;
- referências bibliográficas/documentais.

### Fase C — congelamento editorial

Quando os cinco estiverem aprovados:

- registrar as versões como correntes/finais da rodada;
- gerar novo checkpoint;
- decidir só então eventual exportação/PDF;
- preservar v028 read-only;
- não fazer merge do PR #41 sem autorização.

## Critério para reabrir análise

Só reabrir auditoria, número ou interpretação se houver:

- evidência material nova;
- contradição entre fonte e texto;
- erro aritmético;
- erro de unidade/período/geografia;
- mudança oficial de base/metodologia;
- inconsistência entre setorial e Geral;
- solicitação explícita do usuário.

Fora dessas condições, a prioridade é acabamento e congelamento.
