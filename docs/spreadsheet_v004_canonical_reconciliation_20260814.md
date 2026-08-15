# Reconciliação da planilha v004 com o modelo canônico — 2026-08-14

## Objetivo

Registrar a comparação entre a planilha Google Sheets `São Borja — Base
Histórica Sistematizada — 2026-08-13 — v004` e a execução local
`canonical-series-20260813-review-comments-001`, sem modificar a planilha,
os produtos canônicos ou os arquivos históricos.

Esta auditoria verifica cobertura estrutural, contagens e correspondência de
valores. Ela não promove dados entre camadas e não substitui uma auditoria de
linhagem baseada nos arquivos originais e em seus hashes criptográficos.

## Evidências observadas

- A planilha possui 19 abas, incluindo oito pares de abas de dados e
  metadados.
- As abas de dados contêm 407 linhas de séries, 315 indicadores únicos e
  3.584 células numéricas preenchidas.
- O canônico local contém 3.041 fatos e 145 indicadores provenientes de 14
  conjuntos-fonte.
- Todos os 14 conjuntos-fonte possuem alguma representação temática na
  planilha, mas representação temática não comprova cobertura integral ou
  equivalência conceitual.
- As abas de metadados registram indicador, categoria, unidade, natureza,
  comparabilidade, fonte e limitações.
- Essas abas não registram, por linha, SHA-256 do arquivo original, captura de
  origem, URL final efetivamente obtida, data e hora da obtenção, identificador
  de execução ou transformações aplicadas.

## Resultados calculados

| Dimensão comparada | Fatos no canônico | Valores na v004 | Reconciliados | Ausentes na v004 | Adicionais na v004 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Demografia | 489 | 495 | 486 | 3 | 9 |
| Economia — PIB | 252 | 209 | 209 | 43 | 0 |
| Agropecuária | 1.850 | 1.850 | 1.850 | 0 | 0 |
| Empresas, emprego e renda | 30 | 41 | 30 | 0 | 11 |
| Educação | 67 | 67 | 67 | 0 | 0 |
| Social | 65 | 65 | 65 | 0 | 0 |
| Finanças públicas | 288 | 857 | 288 | 0 | 569 |
| **Total** | **3.041** | **3.584** | **2.995** | **46** | **589** |

A reconciliação aritmética foi aprovada:

```text
3.041 fatos canônicos - 46 ausentes + 589 adicionais = 3.584 valores na v004
```

As contagens e as assinaturas determinísticas de `ano|valor` coincidiram para:

- os 209 fatos de PIB efetivamente incluídos na planilha;
- as 1.850 observações agropecuárias;
- as 30 observações RAIS;
- as 67 observações educacionais;
- as 48 observações IPS e 17 observações IDSC;
- os 288 fatos da base financeira canônica.

As assinaturas determinísticas usadas nesta comparação não são hashes
criptográficos dos arquivos de origem. Elas apoiam a reconciliação dos valores
observados, mas não comprovam autoridade, linhagem ou validade conceitual.

## Diferenças registradas

### Fatos canônicos ausentes na planilha

- três fatos de composição domiciliar provenientes do Panorama do Censo;
- vinte fatos de VAB total da metodologia atual do PIB municipal;
- vinte fatos de impostos líquidos de subsídios da metodologia atual;
- três fatos de impostos líquidos de subsídios da metodologia 1999–2001.

Essas 46 ausências foram classificadas como `ERROR` para a hipótese de que a
planilha contenha integralmente o canônico. Os fatos locais permanecem
preservados e nenhuma substituição ou promoção foi realizada.

### Valores da planilha ainda fora do canônico

- nove valores demográficos adicionais, conceitualmente distintos dos três
  fatos demográficos ausentes;
- onze valores adicionais do retrato empresarial;
- 569 valores de despesas públicas por função, distribuídos em 95 séries.

Os nove valores demográficos foram classificados como `EXPECTED_CHANGE`. Os
valores empresariais e fiscais adicionais foram classificados como
`SOURCE_UPDATE`. Essas classificações registram a diferença observada e não
autorizam promoção automática.

Uma auditoria posterior reconciliou os 589 valores com as evidências de origem
disponíveis: nove com capturas SIDRA preservadas, onze com o arquivo
empresarial citado pela v004 e 569 com capturas DCA preservadas. Os hashes
disponíveis foram recalculados e coincidiram. Essa reconciliação comprova o
vínculo de conteúdo examinado, mas não substitui modelagem conceitual nem
integração incremental ao canônico. Por isso, todos permanecem sem promoção.

## Inconsistências internas da cobertura

A aba de cobertura declara 102 linhas para Demografia, enquanto a aba de dados
possui 102 linhas de séries e 495 valores numéricos. Para Economia, a cobertura
declara 31 linhas, enquanto a aba possui 10 linhas de séries e 209 valores.
Nas outras seis dimensões, a contagem declarada coincide com o número de
valores numéricos.

Portanto, o campo de cobertura não utiliza uma definição uniforme entre
linhas de séries e observações. Essa inconsistência precisa ser corrigida ou
documentada antes de usar a cobertura como medida agregada de completude.

## Estimativas

Nenhuma estimativa, imputação ou inferência numérica foi usada. Diferenças sem
equivalência conceitual comprovada foram mantidas separadas.

## Interpretações

- A v004 é uma base analítica organizada e contém integralmente vários blocos
  do canônico.
- Ela não é uma réplica integral do produto canônico local.
- A planilha também contém dados cuja linhagem disponível foi reconciliada,
  mas que ainda não foram modelados nem promovidos ao canônico.
- A presença de fonte e limitações nas abas de metadados melhora a
  interpretabilidade, mas não constitui linhagem completa até os arquivos
  originais.

## O que pode ser concluído

- Agropecuária, RAIS, educação, IPS, IDSC e a base financeira canônica foram
  reconciliados em contagem e valores.
- O subconjunto de PIB publicado na v004 foi reconciliado em contagem e
  valores.
- A equação global de cobertura fecha sem diferença aritmética.
- Os 46 fatos ausentes e os 589 valores adicionais estão identificados por
  bloco e decisão de preservação.

## O que não pode ser concluído

- Que todos os dados canônicos estejam consolidados na v004.
- Que todos os dados da v004 estejam integrados ao canônico.
- Que correspondência de valores comprove autoridade, linhagem ou adequação
  metodológica.
- Que os 589 valores adicionais possam ser promovidos apenas com a
  reconciliação de conteúdo e hashes, sem modelagem conceitual.
- Que a planilha seja integralmente auditável até os arquivos originais.

## Artefatos locais

A execução local de auditoria
`spreadsheet-v004-vs-canonical-20260814-001` criou, sem sobrescrever produtos
anteriores:

```text
.data/audit/base_territorial/spreadsheet_reconciliation/
└── spreadsheet-v004-vs-canonical-20260814-001/
    ├── reconciliation_summary.csv
    ├── difference_register.csv
    └── validation.csv
```

Os artefatos pertencem a `.data`, são ignorados pelo Git e não acompanham um
clone do repositório. Este documento preserva as conclusões e os totais, mas
não substitui os registros locais detalhados.

A auditoria posterior de linhagem e prontidão criou, também sem sobrescrita:

```text
.data/audit/base_territorial/spreadsheet_reconciliation/
├── spreadsheet-v004-company-lineage-20260814-001/
├── spreadsheet-v004-noncanonical-lineage-20260814-001/
└── spreadsheet-v004-noncanonical-readiness-20260814-001/
```

Esses artefatos registram 589 valores reconciliados, 111 séries com linhagem
verificada ainda não modeladas, quatro séries vazias e bloqueio de promoção
para todas as 115 séries examinadas.

## Recomendações

1. corrigir ou documentar a semântica das contagens na aba de cobertura;
2. avaliar separadamente a inclusão dos 46 fatos ausentes na planilha;
3. modelar incrementalmente os 589 valores adicionais em pipelines canônicos,
   preservando as diferenças conceituais já registradas;
4. acrescentar proveniência por execução e hashes SHA-256 antes de declarar a
   planilha integralmente auditada;
5. preservar a v004 e os produtos canônicos atuais durante qualquer revisão.

## Operações externas e estado do Git

A leitura da planilha foi explicitamente autorizada e executada sem escrita no
Google Drive. Nenhum arquivo bruto, snapshot ou produto histórico foi
alterado, sobrescrito, movido, renomeado ou removido. Esta etapa não realizou
commit, push, criação ou atualização de pull request, nem merge.
