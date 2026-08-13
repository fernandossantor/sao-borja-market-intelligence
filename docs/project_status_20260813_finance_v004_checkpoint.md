# Checkpoint da auditoria fiscal e publicação da planilha v004 — 2026-08-13

## Escopo

Este checkpoint registra a auditoria da dimensão de finanças públicas da
planilha `v003` e a publicação não destrutiva da planilha `v004`. A revisão foi
motivada pela apresentação inconsistente das casas decimais, pelos valores
agregados de centenas de milhões de reais e pela ausência de identificadores
que informassem a função da despesa, como Saúde e Educação.

O trabalho usou exclusivamente as capturas locais já preservadas do
DCA/SICONFI. Não houve nova coleta em serviço externo, reconstrução de
snapshots, alteração de dados brutos ou substituição de planilha histórica.

## Evidências observadas

- A planilha auditada foi `São Borja — Base Histórica Sistematizada —
  2026-08-13 — v003`, ID
  `1k15_YX8ufRE1y4xw3BrcmvlY16PEeqXDFe_V2rNl06E`.
- Na aba `09_Financas_Publicas_Dados`, valores exibidos com zero ou uma casa
  decimal preservavam os centavos no valor efetivo da célula. Exemplos:
  `239445326,5` correspondia a `239445326,52`, `291622924,8` correspondia a
  `291622924,84` e `298379481` correspondia a `298379481,03`.
- Os valores de centenas de milhões correspondiam a agregados anuais de
  receita ou despesa e coincidiam com os valores das capturas DCA/SICONFI e da
  série curada local. Não foi observada multiplicação por 100, inversão de
  separador decimal ou mudança de escala.
- Os 56 indicadores fiscais da `v003` identificavam principalmente natureza
  econômica, conta e estágio contábil. Eles não identificavam a função da
  despesa.
- O `DCA-Anexo I-E`, preservado no snapshot
  `siconfi-dca-4318002-2019-2025-20260813-002510`, contém despesa por função e
  subfunção. Foram observadas 19 funções de nível superior no período, entre
  elas Saúde, Educação, Assistência Social, Urbanismo, Cultura, Saneamento e
  Desporto e Lazer.

## Resultados calculados

A soma das funções de nível superior foi comparada ao total de despesas exceto
intraorçamentárias para cada exercício e estágio contábil. Todas as
reconciliações resultaram em diferença de `R$ 0,00`.

A publicação funcional acrescentou:

- 19 funções governamentais;
- 5 estágios contábeis por função;
- 95 séries novas;
- 569 valores anuais observados, entre 2019 e 2025;
- 95 identificadores únicos;
- zero identificadores duplicados.

Exemplos de valores empenhados conferidos após a escrita:

| Função | 2019 | 2025 |
| --- | ---: | ---: |
| Saúde | R$ 57.819.895,69 | R$ 119.333.046,20 |
| Educação | R$ 45.582.500,60 | R$ 79.333.187,38 |

A cobertura fiscal da nova planilha registra 857 observações e 151
indicadores. A aba fiscal passou de 58 linhas usadas na `v003`, incluindo os
dois cabeçalhos, para 153 linhas usadas na `v004`.

## Estimativas

Nenhuma estimativa, imputação, interpolação ou conversão de ausência em zero
foi realizada. Combinações ausentes na fonte permaneceram vazias.

## Interpretações

- A inconsistência decimal era um erro de apresentação, não perda de precisão
  dos valores armazenados.
- Os valores elevados são compatíveis com agregados municipais anuais. Sua
  interpretação exige distinguir totais, componentes e estágios contábeis.
- A ausência de destino funcional na `v003` era uma lacuna metodológica real da
  curadoria publicada, embora a informação estivesse disponível na fonte.
- Função de governo não identifica automaticamente programa, ação, órgão
  executor ou fonte de financiamento.
- Receita vinculada a uma finalidade e despesa executada por função são
  perspectivas contábeis distintas e não foram combinadas.

## Alterações publicadas na v004

Foi criada uma cópia independente com os seguintes dados:

- título: `São Borja — Base Histórica Sistematizada — 2026-08-13 — v004`;
- ID: `1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM`;
- URL:
  `https://docs.google.com/spreadsheets/d/1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM/edit`;
- pasta pai: `new_files`, ID `14O39dWi2Wq4HATj_xLkHQ7y5OzX44z6C`;
- pai confirmado de `new_files`: `_sao_borja`, ID
  `1or8_CYJYYWPjU3cIAmzgYPLRhKTGv91V`.

Foram alteradas somente na nova cópia:

- `09_Financas_Publicas_Dados!A59:CQ153`: 95 séries por função e estágio;
- `09_Financas_Publicas_Metadados!A58:I152`: proveniência,
  comparabilidade e limitações das novas séries;
- colunas absolutas de 2019 a 2025 na aba fiscal: formato monetário brasileiro
  com símbolo `R$` e duas casas decimais;
- `00_Leia_me`: identificador de execução atualizado para `v004`;
- `01_Cobertura`: contagens e fundamento fiscal atualizados.

Os identificadores funcionais seguem o contrato:

```text
public_finance.siconfi.expense_function.<codigo>.<funcao>.<estagio>
```

Exemplos:

```text
public_finance.siconfi.expense_function.10.saude.despesas_empenhadas
public_finance.siconfi.expense_function.12.educacao.despesas_empenhadas
```

## Comparação e classificação das diferenças

| Diferença | Classificação | Justificativa | Decisão |
| --- | --- | --- | --- |
| Formato monetário fixo com duas casas | `EXPECTED_CHANGE` | corrige somente a apresentação; valores efetivos foram preservados | publicar na nova versão |
| Inclusão de despesa por função | `METHODOLOGY_CHANGE` | amplia a curadoria com o Anexo I-E e novos identificadores sem substituir séries anteriores | publicar na nova versão |
| Aumento de 58 para 153 linhas usadas | `EXPECTED_CHANGE` | corresponde exatamente às 95 séries novas | publicar na nova versão |
| V003 preservada | `IDENTICAL` quanto ao tamanho auditado | permaneceu com 58 linhas usadas após a publicação | preservar histórico |

Não foi identificada diferença `UNEXPLAINED`.

## Validações executadas

- Reconciliação local de cada ano e estágio com o total oficial do Anexo I-E:
  diferença `R$ 0,00`.
- Leitura de retorno da planilha: 95 séries funcionais, 95 IDs únicos, zero
  duplicidades e 569 células numéricas.
- Conferência direta das séries empenhadas de Saúde e Educação de 2019 a 2025.
- Conferência do formato monetário exibido com `R$` e duas casas decimais.
- Conferência dos 95 registros de metadados e das limitações de
  comparabilidade.
- Confirmação de que a `v003` permaneceu com 58 linhas usadas.
- Confirmação da cadeia de pastas autorizada
  `_sao_borja → new_files → v004`.
- `make verify`: 274 testes aprovados e Ruff aprovado.

A transformação local e o lote de escrita/validação no Google Sheets foram o
pipeline real diretamente associado à publicação. A verificação visual foi
realizada por leitura dos valores formatados e metadados de célula da API do
Google Sheets; não foi usada automação visual de navegador.

## O que pode ser concluído

- A precisão monetária está preservada e agora é apresentada de forma
  consistente na `v004`.
- Os agregados elevados examinados são compatíveis com a fonte DCA/SICONFI.
- A `v004` permite analisar despesa por função e por estágio contábil.
- As novas séries possuem proveniência, período, unidade, natureza e
  limitações documentadas.
- A publicação não substituiu nem modificou a `v003`.

## O que não pode ser concluído

- Os dados funcionais não identificam, por si só, programa, ação, unidade
  orçamentária, órgão executor, credor ou fonte específica de financiamento.
- Não se pode somar empenhado, liquidado, pago e restos a pagar como se fossem
  componentes independentes.
- A reconciliação contábil não comprova eficiência, mérito, legalidade ou
  impacto das despesas.
- A auditoria não torna receitas vinculadas equivalentes às despesas por
  função.

## Artefatos e arquivos

Arquivo criado neste checkpoint:

- `docs/project_status_20260813_finance_v004_checkpoint.md`.

Artefato externo criado e validado:

- planilha Google Sheets `v004`, ID
  `1I722PRJ5fyE12WParfsHgsb1YTxR40FVjdw5AM_fCJM`.

Nenhum arquivo bruto, snapshot, produto curado, exportação histórica ou
planilha anterior foi modificado, removido, renomeado ou sobrescrito.

## Operações externas e estado de Git

A operação externa criou uma cópia da `v003` dentro de `new_files` e escreveu
somente na nova `v004`, após autorização explícita. Não houve acesso adicional
aos endpoints de origem, exclusão, movimentação, sobrescrita, commit, push,
criação ou atualização de pull request, nem merge.

O trabalho permanece na branch `feature/new-files-temporal-coverage`. O
repositório já continha alterações locais anteriores, que foram preservadas e
não foram modificadas incidentalmente por esta etapa.

## Recomendações

A próxima ação recomendada é revisar este checkpoint e a `v004` em pull
request antes de qualquer decisão de promoção. A `v003` deve permanecer como
registro histórico, e futuras ampliações para programa, ação, órgão ou fonte de
recursos devem ser tratadas como nova etapa metodológica.
