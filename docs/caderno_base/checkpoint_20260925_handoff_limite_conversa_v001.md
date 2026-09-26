# CHECKPOINT — SBMI — handoff por limite máximo da conversa
**Data:** 25/09/2026  
**Motivo:** a conversa atingiu a duração máxima da interface.  
**Reinício recomendado:** continuar deste arquivo em um novo chat do projeto.

## 1. Estado editorial corrente

A prioridade atual é **QA textual profundo**, não gráficos.

Regra editorial:
`evidência → contexto → relação → mecanismo → interpretação → implicação → decisão → indicador/teste → limite`.

Critério do usuário:
- não economizar texto quando profundidade for necessária;
- preferir demonstração e argumentação a objetividade genérica;
- todos os cadernos devem ser úteis para tomada de decisão;
- evitar recomendações vagas;
- recomendações devem ser específicas, testáveis e rastreáveis;
- sem inventar dados, market share, causalidade, benchmarks locais ou projeções não sustentadas.

## 2. Versões editoriais correntes

### Caderno Geral v004
Drive:
`13yqwDHKJuEag4I0l7XaUZ_oDIg5lh0UvQsmJWc3H2Co`

### Bens Essenciais v003
Drive:
`190arYFyxKq_xynAbqU3fGThlpbJiqPXlmqMOrtRHss0`

### Saúde, Higiene e Cuidados Pessoais v003
Drive:
`1d141fQT3aTMtHoj5el9FOlR0mXqTgcNp2E7QqV28ZjI`

### Bens Não Essenciais v003
Drive:
`1uBIiR9pH6wqzIH2T5nO_dRpDEu2Cu-qP3v4cCcs2DDE`

### Alimentação Fora do Lar e Serviços v003
Drive:
`1pyUYH5APuuRR72XZ9Pd1BjpQDcgDQ1yTNActUkium3Y`

## 3. O que já foi aprofundado

Nos quatro setoriais:
- seções analíticas expandidas;
- diagnósticos empresariais aprofundados;
- recomendações específicas por mecanismo;
- indicadores associados às decisões;
- exercícios mentais decisórios;
- seção `RASTREABILIDADE DAS CONCLUSÕES`;
- seção `TRILHAS DE RACIOCÍNIO — DA EVIDÊNCIA À DECISÃO`;
- considerações finais reescritas com maior densidade.

No Caderno Geral:
- aprofundamento de retenção/captura;
- implicações empresariais;
- prioridades de inteligência;
- sistema de acompanhamento;
- seção `RASTREABILIDADE DAS TESES CENTRAIS — DA EVIDÊNCIA À DECISÃO`;
- considerações finais reescritas.

## 4. Último ponto efetivamente executado antes do travamento

Foi iniciada a **varredura fina de linguagem e causalidade**.

Correções já aplicadas incluem:
- substituição de formulações causalmente fortes por formulações associativas quando a base não sustenta causalidade;
- exemplo em Alimentação/Serviços: “qualidade, atendimento, tempo, ambiente ou entrega determinam satisfação e recompra” foi alterado para formulação que indica que esses fatores compõem a experiência e podem estar associados à satisfação/recompra, explicitando que o projeto não estima efeito causal;
- exemplo em Bens Essenciais: “rupturas provocam perda” / “fila elimina vantagem” foi suavizado para associação/hipótese observável.

Nenhuma nova base canônica foi alterada.

## 5. QA estrutural já conferido

Os cinco documentos:
- preservam os principais números promovidos;
- possuem metodologia;
- possuem referências;
- possuem limitações;
- possuem decisões e indicadores;
- evitam, como recomendação suficiente, frases genéricas do tipo “investir em marketing”, “melhorar atendimento”, “conhecer o consumidor” etc.

## 6. Próximo passo exato

Continuar o QA textual profundo, documento por documento:

1. varrer causalidade indevida;
2. localizar trechos ainda genéricos;
3. localizar saltos de raciocínio;
4. verificar se toda conclusão material está ligada a fonte/período/unidade/abrangência;
5. verificar se toda recomendação muda de fato uma decisão;
6. verificar se cada recomendação possui indicador/teste e condição de revisão quando aplicável;
7. revisar redundâncias;
8. revisar se “não respondível” foi preservado onde necessário;
9. somente depois congelar editorialmente.

Ordem sugerida:
1. Bens Essenciais;
2. Saúde/Higiene;
3. Bens Não Essenciais;
4. Alimentação/Serviços;
5. Caderno Geral;
6. QA cruzado final.

## 7. Governança

- PR #41 permanece **aberto, draft e sem merge**;
- Caderno-Base v028 permanece **read-only**;
- Caderno-Base v029 permanece base corrente;
- sem nova pesquisa primária;
- não reabrir auditorias encerradas sem evidência material nova;
- não produzir gráficos antes de fechar o QA textual;
- não mesclar PR #41 sem autorização explícita.

## 8. Arquivos de governança relacionados

- `docs/governance/padrao_editorial_decisorio_cadernos_20260925_v001.md`
- `docs/caderno_base/checkpoint_20260925_reconstrucao_argumentativa_cadernos_v001.md`

## 9. Prompt recomendado para o novo chat

> Continuar o projeto São Borja — Inteligência Mercadológica exatamente a partir de `docs/caderno_base/checkpoint_20260925_handoff_limite_conversa_v001.md`. A prioridade é QA textual profundo dos cinco cadernos correntes, com profundidade argumentativa, rastreabilidade e utilidade decisória. Não priorizar gráficos. Preservar PR #41 aberto/draft/sem merge e Caderno-Base v028 read-only.
