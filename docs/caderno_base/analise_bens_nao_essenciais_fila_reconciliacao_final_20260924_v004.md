# Bens não essenciais — fila priorizada de reconciliação final v004 — 24/09/2026

## 1. Atualização

A v004 incorpora os lotes 21 e 22 e o universo candidato reconciliado v004.

Contagem atual:

- **P0: 1 registros de controle**;
- **P1: 24 registros de controle**;
- **P2: 17 registros de controle**;
- **P3: 37 registros de controle**;
- **P4: 61 registros de controle**;

Total: **140 registros de controle**.

## 2. Mudança central

Restou apenas **um P0**:

- linha 122 — 7 Povos Kids — conflito cadastral ativa × baixada.

Os demais casos anteriormente P0 foram tratados por uma das regras:

- presença operacional atual comprovada → inclusão no cenário-base e reconciliação jurídica rebaixada para P1/P2;
- ausência de evidência atual → exclusão do cenário-base, preservando histórico/sensibilidade;
- registro histórico sem presença corrente → fora do cenário-base.

## 3. Consequência metodológica

A fila deixa de ser dominada por dúvidas de existência corrente e passa a concentrar-se em:

- P1 — identidade jurídica, sucessão, função física e número de unidades;
- P2 — situação cadastral/endereço/metadado ainda pendentes, mas com presença operacional suficientemente demonstrada.

## 4. P0 remanescente

### 7 Povos Kids — 62.201.625/0001-79

Fichas específicas recentes apresentam situação ativa, mas persiste uma listagem genérica que apresenta o mesmo CNPJ como baixado.

Enquanto não houver fonte oficial atual inequívoca, o registro permanece P0 e fora da decisão final do denominador.

## 5. Regra para o primeiro recálculo exploratório

Há duas alternativas tecnicamente aceitáveis após o fechamento dos P1 que alterem storefronts:

1. aguardar fonte oficial para 7 Povos Kids; ou
2. calcular cenário-base e cenário de sensibilidade com/sem 7 Povos Kids, explicitando a incerteza.

Nenhuma métrica canônica deve ser publicada ainda.

## 6. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Não houve recálculo canônico de oferta, operadores, raízes ou concentração.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_fila_reconciliacao_final_20260924_v004.csv`
