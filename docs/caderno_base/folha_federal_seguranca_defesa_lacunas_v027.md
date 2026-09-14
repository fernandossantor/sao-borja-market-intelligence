# Folha pública não municipal — lacunas federais de segurança e Defesa — v027

**Data da auditoria:** 2026-09-13  
**Geografia:** São Borja/RS  
**Período principal:** julho/2026 para SIAPE civil/policial; junho/2026 para o arquivo aberto de militares  
**Objetivo:** revisar lacunas materiais restantes antes do fechamento metodológico da v027.

## 1. Resultado executivo

A revisão final identificou três componentes materiais da folha pública não municipal que permanecem fora da massa monetária territorializada:

- Polícia Federal;
- Polícia Rodoviária Federal;
- Forças Armadas, com presença local do Exército.

A diferença em relação ao estado anterior é importante: a **presença institucional local está agora validada**, mas as bases remuneratórias abertas da CGU **suprimem ou não publicam a chave territorial necessária** para agregar headcount e remuneração de São Borja.

Portanto:

**presença local validada ≠ folha territorializada.**

Nenhum valor foi imputado.

## 2. Federal civil já territorializado

Fonte:

**Portal da Transparência / CGU — SIAPE — julho/2026.**

Regras institucionais auditadas:

- Unipampa Campus São Borja;
- IFFar Campus São Borja;
- INSS APS São Borja;
- MAPA/Vigiagro São Borja;
- RFB Inspetoria São Borja.

Resultado:

- **247 IDs/vínculos**;
- **246** com registro remuneratório;
- **R$ 3.748.393,85** em Remuneração Básica Bruta.

Composição de vínculos:

- IFFar: 123;
- Unipampa: 103;
- INSS: 7;
- MAPA/Vigiagro: 13;
- RFB: 1.

**Natureza:** DADO OBSERVADO + AGREGADO CALCULADO.

**Limitação:** subtotal federal civil não exaustivo.

## 3. Controle: regra territorial genérica do SIAPE

Como controle independente, foi testada a presença literal de `SAO BORJA` nas UORGs.

Resultado:

| Critério | IDs | Remuneração Básica Bruta |
|---|---:|---:|
| UORG_EXERCICIO contém SAO BORJA | 28 | R$ 459.731,81 |
| UORG_LOTACAO contém SAO BORJA | 149 | R$ 2.174.486,35 |
| União lotação ou exercício | 157 | R$ 2.308.123,91 |

Esse resultado **não substitui** o subtotal institucional de 247 vínculos.

Motivo: unidades-filhas de exercício de Unipampa e IFFar nem sempre carregam literalmente `São Borja` no nome da UORG, embora estejam subordinadas a campi localizados no município.

**Uso:** controle de sensibilidade e diagnóstico da estrutura de UORG.

## 4. Polícia Federal — presença local validada

A página institucional da Polícia Federal no Rio Grande do Sul mantém explicitamente:

**Delegacia da Polícia Federal em São Borja/RS — DPF/SBA/RS.**

A página informa sede local e serviços permanentes, incluindo migração, passaportes, controle de armas e produtos químicos.

**Classificação:** DADO OBSERVADO.

### 4.1 Limitação do SIAPE aberto

Workflow:

`federal-police-uorg-inventory`

Run:

`34771941037`

Universo filtrado nacional PF/PRF:

- **31.762 linhas**.

Campos organizacionais observados no universo policial:

- `COD_UORG_LOTACAO = -11`;
- `UORG_LOTACAO = SIGILOSO`;
- `COD_UORG_EXERCICIO = -11`;
- `UORG_EXERCICIO = SIGILOSO`;
- `UF_EXERCICIO = -1`.

Candidatos textuais São Borja:

**0**

### Interpretação correta

O zero é efeito da **supressão da dimensão territorial**, não evidência de ausência de servidores em São Borja.

### Decisão

**PRESENÇA LOCAL VALIDADA / FOLHA NÃO PROMOVIDA.**

## 5. Polícia Rodoviária Federal — presença local validada

A página institucional da PRF no Rio Grande do Sul registra:

- **Delegacia em São Borja**;
- **Unidade Operacional São Borja**, na BR-285.

A página da Unidade Operacional foi modificada em fevereiro de 2026, fornecendo evidência institucional contemporânea à v027.

**Classificação:** DADO OBSERVADO.

### Limitação

A PRF está incluída no mesmo bloqueio do SIAPE descrito acima: UORGs aparecem como `SIGILOSO` e `UF_EXERCICIO = -1`.

Não é possível, portanto, derivar headcount ou massa remuneratória local de forma reproduzível a partir do arquivo aberto.

### Decisão

**PRESENÇA LOCAL VALIDADA / FOLHA NÃO PROMOVIDA.**

## 6. Forças Armadas — presença local validada

Fontes oficiais do Exército Brasileiro documentam a presença do:

- **2º Regimento de Cavalaria Mecanizado — 2º RC Mec**, em São Borja;
- **Coudelaria de Rincão**;
- **Campo de Instrução de Rincão**, sediado em São Borja em documentação institucional/de compras do Exército.

A presença militar local é, portanto, material e documentalmente verificável.

**Classificação:** DADO OBSERVADO.

## 7. Arquivo CGU de militares — ausência estrutural de territorialização

Fonte:

**Portal da Transparência / CGU — Militares — junho/2026.**

Workflow:

`military-cadastro-schema-audit`

Run:

`34772038863`

Universo:

**351.607 linhas nacionais.**

Resultado estrutural:

- `COD_UORG_LOTACAO = -1` em todo o universo;
- `UORG_LOTACAO = SEM INFORMACAO` em todo o universo;
- `COD_UORG_EXERCICIO = -1` em todo o universo;
- `UORG_EXERCICIO = SEM INFORMACAO` em todo o universo;
- `UF_EXERCICIO = -1` em todo o universo.

A diferenciação organizacional disponível é apenas por Força:

- Comando do Exército: **209.680** linhas;
- Comando da Marinha: **74.699**;
- Comando da Aeronáutica: **67.228**.

### Consequência

A base pública não contém a variável necessária para localizar 2º RC Mec, Rincão ou qualquer organização militar por município.

A busca textual por São Borja ou pelo nome da organização militar é, portanto, estruturalmente inviável nesse arquivo.

### Decisão

**PRESENÇA LOCAL VALIDADA / FOLHA NÃO PROMOVIDA.**

## 8. Regra de não imputação

A v027 não utilizará:

- média salarial nacional ou estadual de PF/PRF;
- remuneração média por patente militar;
- efetivo teórico ou doutrinário de regimento/delegacia;
- tabelas de cargos normativas como roster corrente;
- benchmarks de unidades comparáveis;
- multiplicação de “efetivo provável” por salário médio;
- ausência de registro territorial na CGU como valor zero.

Esses procedimentos produziriam uma falsa precisão incompatível com a governança do projeto.

## 9. Implicação para a ordem de grandeza de folha pública

O valor já documentado de:

**R$ 9.551.979,21/mês**

permanece classificado como:

**ORDEM DE GRANDEZA DOCUMENTAL PARCIAL.**

Não representa a folha pública não municipal total de São Borja.

Estão explicitamente ausentes da massa monetária, entre outros:

- TJRS real;
- Polícia Federal;
- Polícia Rodoviária Federal;
- Forças Armadas;
- cobertura temporária DPERS não atribuível;
- outros vínculos sem chave territorial suficiente.

Os valores:

- R$ 9.618.443,65;
- R$ 9.627.669,64;

permanecem apenas como sensibilidades `base v025 + DPERS recorrente`, e não subtotais canônicos.

## 10. Implicação mercadológica

PF, PRF e Exército representam fontes de renda pública potencialmente estáveis em São Borja.

Sem quantificar causalidade ou magnitude, sua presença é compatível com demanda recorrente por:

- moradia;
- alimentação;
- educação;
- serviços pessoais;
- transporte;
- comércio cotidiano;
- lazer e consumo discricionário.

A omissão monetária desses grupos implica que a folha pública já documentada deve ser interpretada como **piso**, não como teto.

## 11. Fechamento metodológico da v027

O critério de fechamento não é cobertura monetária de 100%.

O critério é:

> cada lacuna material deve possuir uma decisão explícita de promoção, envelope, bloqueio técnico/documental ou não promoção.

Estado final:

- federal civil parcial: **PROMOVIDO / NÃO EXAUSTIVO**;
- Executivo estadual: **PROMOVIDO** segundo a convenção documentada;
- MPRS: **PROMOVIDO**;
- DPERS: **PROMOVIDA POR ENVELOPES DOCUMENTAIS**;
- TJRS: **ESTRUTURA TERRITORIAL PROMOVIDA / MASSA REAL NÃO PROMOVIDA**;
- PF: **PRESENÇA VALIDADA / FOLHA NÃO PROMOVIDA**;
- PRF: **PRESENÇA VALIDADA / FOLHA NÃO PROMOVIDA**;
- Forças Armadas: **PRESENÇA VALIDADA / FOLHA NÃO PROMOVIDA**;
- TCE-RS: **NÃO PROMOVIDO**;
- ALRS: **NÃO PROMOVIDA**.

**Conclusão:** a v027 pode ser fechada no limite documental atual.

## 12. Artefatos Drive atualizados

Planilha técnica v027:

`1HjfbGo8qA2ZydfCrbouBVjlHDo8DRZs04H3cYr_FKMo`

Nova aba:

`Folha_federal_lacunas_v027`

Também atualizadas:

- `Auditoria_v027`;
- `Diagnostico_fluxos_v027`.

Caderno narrativo:

`1g2xnVccRF8Eu-JRVCpwJb2wZodgbymuFdhOaVW1G2y4`

Seções:

- 27.18 — revisão final das lacunas materiais;
- 27.19 — fechamento da v027.

Registro metodológico:

`1TL2Hd6SmcjxPPck8v49VSyvZjQAK9sUH5IHRM2FNACM`

Seções:

- 26 — revisão final das lacunas federais;
- 27 — fechamento metodológico da v027.

## 13. Governança

Branch:

`feature/cnpj-territorial-control-v1`

PR #41:

- deve permanecer **ABERTO**;
- deve permanecer **DRAFT**;
- deve permanecer **SEM MERGE**;
- nenhuma integração à `main` é autorizada.
