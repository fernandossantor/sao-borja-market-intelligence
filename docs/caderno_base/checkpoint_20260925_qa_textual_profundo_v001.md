# Checkpoint — QA textual profundo dos cinco cadernos — 2026-09-25

## Governança preservada

- Repositório: `fernandossantor/sao-borja-market-intelligence`
- Branch: `feature/cnpj-territorial-control-v1`
- PR #41: **manter aberto, draft e sem merge**.
- Caderno-Base Territorial v028: **antecedente read-only**.
- Caderno-Base Territorial v029: base técnica corrente.
- Gráficos não foram priorizados nesta etapa.

## Regra editorial aplicada

O QA seguiu a cadeia:

`evidência → contexto → relação → mecanismo → interpretação → implicação → decisão → indicador/teste → limite`.

Foram priorizados: controle de causalidade; generalizações sem sustentação; comparabilidade entre universos; explicitação de fonte/período/unidade/geografia/limitação; distinção entre observado/calculado/estimado/hipótese/interpretação/recomendação; indicadores/testes e condições de revisão para cada prioridade.

## Versões editoriais correntes

| Caderno | Versão QA | Google Doc ID | Prioridades / condições de revisão |
|---|---|---|---:|
| Comércio de Bens Essenciais | v004 | `1lkTmsTB-oeADdqxPAkG0gneTt4CKBY2R0_aEBPKg07k` | 8 / 8 |
| Saúde, Higiene e Cuidados Pessoais | v004 | `17MCoSOZGXNxO2MWfgYF2RnujxAviuAez6-LVyD8RQXM` | 8 / 8 |
| Bens Não Essenciais | v004 | `1lILyRBgjj1iZ7B_SO4-tkxgwEMGX_zwRyg2rEj4UOJE` | 10 / 10 |
| Alimentação Fora do Lar e Serviços | v004 | `1xUf5c6rsuzIruJmNJTaHVBFSb7Ug0qn0A-PDQVV5YIQ` | 10 / 10 |
| Caderno Geral | v005 | `1-9V5hMadSRGhgI-SMcF8b5Q5AZlhYArswaYBkYkdMqg` | 8 / 8 |

Checkpoint em Google Drive: `1lY8lgdQqZzfq3z7aye03S6P7LB69zoEzcKtqa1e_yd0`.

## Alterações centrais do QA

### Causalidade e linguagem

Afirmações determinísticas foram reescritas quando a base permitia apenas associação, mecanismo plausível ou hipótese operacional. Recomendação empresarial passa a exigir confirmação por indicador próprio: conversão, recorrência, ruptura, reclamação, motivo de perda, ticket, margem ou equivalente.

### Renda e orçamento

Censo e RAIS permanecem separados:

- Censo 2022: mediana do rendimento domiciliar per capita de São Borja = **R$ 1.100,00 por pessoa/mês**.
- RAIS 2024: entre vínculos com remuneração positiva em dezembro, **56,57% até 2 SM** e **81,33% até 3 SM**.

Não há indicador combinado. Os dados justificam **testar** restrição de desembolso; não provam consumo individual ou gasto setorial.

### Estimativa de bens essenciais

A ordem de grandeza de **R$ 234.706.228,14/ano** permanece explicitamente como **ESTIMATIVA MODELADA** de gasto residente com alimentação no domicílio. Para leitura decisória usa-se R$ 234,71 milhões. Não é faturamento observado, market share ou retenção local.

### Cobertura e market share

- Saúde/Higiene: 23 registros/CNPJs CNES privados, 7 raízes, 20/23 em raízes multiunidade, maior raiz 8/23. Controle Agafarma impede tratar 23 como total exaustivo.
- BNE: cenário-base 122 storefronts; sensibilidade 121; 109 operator_keys; 8 raízes multiunidade; 21 storefronts em raízes multi. Storefront ≠ CNPJ ≠ market share.
- Serviços: 947 SINAC e 728 SIMEI são optantes no recorte; não equivalem automaticamente a operação ativa, ponto físico, faturamento ou market share.
- Alimentação: 409 estabelecimentos CNAE 56 no recorte cadastral; cadastro ≠ operação corrente nem participação de vendas.

### POM e POF

- Entrevistas qualitativas não foram tratadas como prevalência populacional.
- Survey online Alimentação/Serviços (n=153) permanece descritivo; recrutamento probabilístico não demonstrado.
- POF 2017–2018 permanece **BENCHMARK EXTERNO**; proporções regionais/nacionais não são transportadas diretamente para São Borja.

### Proxies internos formalizados

- Bens Essenciais: proxy de resolução da missão com registro de item crítico indisponível/necessidade não atendida.
- BNE: proxy de resolução por ocasiões registradas atendidas sem falta/abandono conhecido.
- Alimentação/Serviços: taxa de resolução automática por interações concluídas sem transferência e sem recontato na janela definida.

Todos dependem da qualidade do registro e não são indicadores populacionais.

## QA de rastreabilidade

Os blocos finais de rastreabilidade foram enriquecidos com, quando aplicável:

- fonte;
- período;
- unidade;
- abrangência geográfica;
- natureza;
- limitação.

No Caderno Geral, as fontes das Figuras 1–9 foram reforçadas para evitar leitura cruzada indevida entre universos, períodos e unidades.

## Validações de consistência

- Nenhum dos cinco cadernos correntes mantém referência editorial obsoleta a reports setoriais v003, integração editorial v003 ou Caderno Geral v004.
- `Painel_final_v003` permanece porque é ativo distinto e legitimamente versionado.
- v028 aparece apenas como antecedente preservado/read-only.
- Caderno Geral v005 referencia os quatro reports setoriais v004.
- Contagem de prioridades e condições de revisão: **8/8, 8/8, 10/10, 10/10, 8/8**.
- Rastreio de similaridade entre parágrafos longos não encontrou duplicação alta que justificasse cortes automáticos.

## Aritmética rechecada

- 52/54 = 96,30%
- 20/23 = 86,96%
- 8/23 = 34,78%
- 21/122 = 17,21%
- 64/122 = 52,46%
- 4/409 = 0,98%
- R$ 327.021,02 / R$ 869.843,54 = 37,60%
- R$ 542.822,52 / R$ 869.843,54 = 62,40%

## Não respondíveis preservados

Sem base adicional compatível, permanecem não respondíveis conforme o caderno: market share por empresa/operador/formato; retenção/vazamento monetário municipal; gasto efetivo de visitantes; participação econômica real do e-commerce local; elasticidades preço/conveniência; efeito causal do digital; impacto monetário de políticas públicas sobre vendas privadas; causalidade entre ciclos macroeconômicos/agropecuários e vendas empresariais.

## Estado para continuidade

A camada editorial está pronta para **acabamento e congelamento editorial**, condicionado apenas a uma última leitura humana de ortografia, paginação, estilos e quebras visuais. Não há justificativa metodológica para reabrir auditorias fechadas ou priorizar novos gráficos antes desse acabamento, salvo evidência material nova.

Ao retomar:
1. preservar PR #41 aberto/draft/sem merge;
2. preservar v028 read-only;
3. usar v029 como base técnica;
4. usar as cinco versões QA listadas acima como camada editorial corrente;
5. só reabrir números ou auditorias mediante evidência material nova.
