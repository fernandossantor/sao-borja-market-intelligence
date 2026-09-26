# QA Argumentativo e Decisório — Cadernos SBMI — v003
**Data:** 25/09/2026

## Objeto

Versão corrente do QA textual dos cinco cadernos editoriais. Incorpora o QA v002 e acrescenta uma revisão específica de precisão metodológica e editorial.

## Documentos correntes

- Caderno Geral v004 — `13yqwDHKJuEag4I0l7XaUZ_oDIg5lh0UvQsmJWc3H2Co`
- Bens Essenciais v003 — `190arYFyxKq_xynAbqU3fGThlpbJiqPXlmqMOrtRHss0`
- Saúde/Higiene v003 — `1d141fQT3aTMtHoj5el9FOlR0mXqTgcNp2E7QqV28ZjI`
- Bens Não Essenciais v003 — `1uBIiR9pH6wqzIH2T5nO_dRpDEu2Cu-qP3v4cCcs2DDE`
- Alimentação/Serviços v003 — `1pyUYH5APuuRR72XZ9Pd1BjpQDcgDQ1yTNActUkium3Y`

## Critério

`evidência → contexto → relação → mecanismo → interpretação → implicação → decisão → indicador → limite`

## Revisões adicionais desta versão

1. **Números ilustrativos não observados removidos.**
   - exercícios com valores/taxas fictícios foram eliminados do Caderno Geral;
   - exercícios agora usam dados observados, cálculos derivados ou relações conceituais sem valores inventados;
   - a regra metodológica dos setoriais foi ajustada para impedir números fictícios em exercícios mentais.

2. **Causalidade revisada.**
   - formulações fortes foram substituídas por “pode estar associado”, “mecanismo plausível”, “deve ser testado na operação” ou equivalentes quando a base não sustenta efeito causal;
   - qualidade, atendimento, digital, resposta, disponibilidade, renda e cadência não são tratados como causas automáticas de venda/recompra.

3. **Rastreabilidade das considerações finais.**
   - os cinco cadernos receberam nota explícita informando que a síntese final não introduz novos dados;
   - as conclusões remetem às seções analíticas, trilhas de raciocínio e bases técnicas.

4. **Coerência de versões e entregáveis.**
   - Caderno Geral v004 e quatro setoriais v003 permanecem a camada editorial corrente;
   - README do pacote foi atualizado para as versões atuais;
   - gráficos permanecem opcionais e não bloqueiam o fechamento.

## Consistência numérica revalidada

Os principais valores promovidos continuam presentes e coerentes:
- população 59.676 / estimativa 61.311;
- RAIS 13.125; mediana dezembro R$ 2.605,60; 56,57% até 2 SM; 81,33% até 3 SM;
- Bens Essenciais R$ 19.558.852,34/mês e R$ 234.706.228,14/ano; 54/52 = 96,30%;
- Saúde 23 registros, 7 raízes, 20/23 = 86,96%, maior raiz 8/23 = 34,78%;
- BNE 122/121, 109 operator_keys, 21/122 = 17,21%, cobertura REGIC direta 64/122 = 52,46%;
- Serviços 947 SINAC / 728 SIMEI; alimentação CNAE 56 = 409;
- PNAE/B2G preservado com contrato ≠ pagamento.

## Resultado

**PASSA O QA ARGUMENTATIVO, DE RASTREABILIDADE E PRECISÃO.**

Pendência residual:
- última leitura humana integrada dos cinco documentos;
- ajuste fino de redundância, ritmo, transições e referências;
- revisão visual/formatação depois do fechamento textual.

Não há necessidade de reabrir auditorias técnicas sem evidência material nova.

## Governança

- Caderno-Base v028 permanece read-only.
- Caderno-Base v029 permanece base técnica corrente.
- PR #41 permanece aberto, draft e sem merge.
- Nenhum merge/retarget sem autorização explícita.
