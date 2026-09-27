# Benchmark territorial comparável v003 — emprego e estrutura setorial

## Objetivo

Contextualizar a renda domiciliar de São Borja por meio da escala das unidades econômicas e da composição setorial do pessoal ocupado, sem atribuir causalidade.

## CEMPRE total — tabela 9509

Fonte: IBGE/SIDRA, CEMPRE 2022.

Workflow `benchmark-cempre-sidra`; run `34533091424`; artifact `10174285643`; SHA-256 `47d2652ceaf3e11e162cbf567473affade12addd67afe7f2dfdf3f6ee30ea5af`.

| Município | Unidades locais | Pessoal ocupado | Salário médio mensal |
|---|---:|---:|---:|
| São Borja | 2.782 | 13.528 | R$ 2.708,09 |
| São Gabriel | 2.228 | 11.208 | R$ 2.646,27 |
| Alegrete | 3.143 | 15.193 | R$ 2.630,97 |
| Santiago | 2.477 | 10.799 | R$ 2.703,19 |

São Borja possui o maior salário médio CEMPRE no grupo de comparáveis de escala, embora praticamente empatado com Santiago.

Razão contextual de pessoal ocupado em unidades locais por 1.000 residentes:
- São Borja: 226,69;
- Santiago: 220,67;
- Alegrete: 209,82;
- São Gabriel: 191,63.

**Limitação crítica:** essa razão não é taxa de emprego. O CEMPRE conta pessoas no local da atividade; o Censo conta população por residência.

## Estrutura setorial — tabela 9528

Workflow `benchmark-cempre-sectors-sidra`; run `34533594730`; artifact `10174485372`; SHA-256 `37643eceb7e0f109ac958027518b9df8fd0d8684a84dd4dad613c444313a843f`.

Participação no pessoal ocupado:

| Bloco | São Borja | São Gabriel | Alegrete | Santiago |
|---|---:|---:|---:|---:|
| Comércio — G | 32,58% | 34,06% | 32,93% | 39,44% |
| Adm. pública — O | 13,65% | 13,01% | 12,93% | 10,75% |
| Indústria — C | 9,71% | 15,28% | 11,32% | 7,57% |
| Transporte — H | 7,60% | 3,27% | 4,20% | 2,42% |
| Construção — F | 7,25% | 2,05% | 5,49% | 3,13% |
| Educação + saúde — P+Q* | 8,23% | 11,09% | 10,87% | 12,77% |
| J+K+M* | 5,29% | 5,21% | 7,72% | 8,32% |

\* Agregações analíticas do SBMI, não categorias oficiais.

Foram preservadas 58 células suprimidas. A cobertura conhecida do pessoal ocupado por seção é 100% para São Borja, Alegrete e Santiago; 99,53% São Gabriel; 99,97% Sant'Ana; 99,79% Uruguaiana.

## Diagnóstico

Santiago tem renda domiciliar mediana 22,04% superior à de São Borja apesar de salário médio CEMPRE 0,18% inferior e menor razão contextual de pessoal ocupado local por residente.

São Borja apresenta mais peso relativo em transporte, construção, administração pública e indústria; Santiago, em comércio, educação/saúde e J+K+M.

**Interpretação:** as estruturas econômicas são distintas, mas a composição setorial não é tratada como causa da diferença de renda.

## Próxima pergunta

Testar mobilidade para trabalho/estudo e centralidade regional. Isso permite separar onde as pessoas residem, trabalham, recebem renda e consomem.

## Drive

CEMPRE total: pasta `1505jbpnsyfyUIiQN6IvvfYMu-K9I210e`.

CEMPRE setorial: pasta `1m-uMXlfT6-bnV59NxRIjW2KlJ6jGSbqS`.

Documento nativo: `1DNRXTmokXBmFjAyv5J9xKAR_010mki8cAXm1HOpPH3A`.
