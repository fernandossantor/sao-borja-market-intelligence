# Bens não essenciais — reconciliação final P0 — lote 21 — 24/09/2026

## 1. Objeto

Terceiro lote de resolução da fila P0. O foco foi separar **presença operacional corrente** de **regularidade/identidade cadastral**, evitando que uma pendência jurídica bloqueie automaticamente a existência mercadológica observável do estabelecimento.

Foram tratados seis casos:

- Loja Marlin Fashion;
- Mundi Calçados;
- Ciranda Boutique;
- Bicho Mimado;
- Pet House;
- Ponto dos Pets.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhum recálculo canônico de oferta, operadores, raízes ou concentração.

## 2. Critério metodológico novo aplicado

Para o futuro cenário-base exploratório, foram separados dois planos:

1. **presença operacional/mercadológica** — existe evidência atual de que a marca/ponto opera no mercado;
2. **situação/identidade jurídica** — o CNPJ corrente pode estar ativo, inapto, desconhecido ou ainda não reconciliado.

Quando a presença operacional corrente é forte, a pendência do CNPJ deixa de ser P0 e passa a P1/P2, desde que a incerteza permaneça explicitamente registrada.

Isso **não** transforma CNPJ inapto em ativo e **não** dispensa a reconciliação jurídica.

## 3. Loja Marlin Fashion — linha 100

### Dados observados

- perfil local estruturado atual mantém **Loja Marlin Fashion** em Rua General Osório, 2186, com avaliações, categoria comercial e horários;
- Econodata e Serasa continuam apresentando o CNPJ `18.556.994/0001-92` como **INAPTO**;
- Econodata informa inaptidão desde 19/05/2026 por omissão de declarações.

### Interpretação

Há evidência suficiente de **presença operacional corrente**, mas não de regularidade cadastral.

### Decisão provisória

- resolver o P0 quanto à presença mercadológica;
- incluir a operação Marlin Fashion no cenário-base exploratório;
- **não** tratar `18.556.994/0001-92` como CNPJ ativo;
- mover a identificação jurídica corrente para P1.

## 4. Mundi Calçados — linha 144

Diretório empresarial atual lista simultaneamente:

- **Mundi Calçados**;
- **Calcemoda Comércio de Calçados Ltda**;
- Avenida Presidente Vargas, 2240.

A situação cadastral corrente do CNPJ `38.128.053/0001-65` ainda não foi obtida diretamente.

### Decisão provisória

- presença operacional resolvida;
- incluir Mundi no cenário-base exploratório;
- rebaixar a situação cadastral pendente para P2.

## 5. Ciranda Boutique — linha 147

Solutudo rastreado em setembro/2026 lista:

- Ciranda Boutique;
- Rua General Osório, 2070;
- telefone 3431-3228.

Esses elementos coincidem com os dados históricos do CNPJ `90.134.701/0001-06`.

### Decisão provisória

- resolver P0 quanto à presença operacional;
- incluir a operação no cenário-base exploratório;
- manter confirmação do status cadastral como P2.

## 6. Bicho Mimado — linha 188

### Dados observados

- Pet Shop Bicho Mimado aparece em diretórios operacionais recentes na Rua Inhandoi, 141;
- perfil local estruturado atual também registra a operação;
- o CNPJ histórico `22.663.567/0001-80` permanece inadequado como ativo cadastral.

### Decisão provisória

- incluir **a marca/operação** no cenário-base exploratório;
- não usar o CNPJ histórico como ativo;
- mover a identificação do CNPJ corrente para P1.

## 7. Pet House — linha 189

TutorCanino atualizado recentemente apresenta:

- Pet House;
- Rua Joaquim Gonçalves Ledo, 354;
- bairro Itachere;
- avaliações e horário de funcionamento.

Nenhum CNPJ confiável foi identificado.

### Decisão provisória

- incluir o operador no cenário-base exploratório como **operador sem CNPJ identificado**;
- mover a identidade jurídica para P1.

## 8. Ponto dos Pets — linha 190

### Dados observados

- diretórios atuais mantêm Ponto dos Pets em operação;
- Prefeitura de São Borja vinculou historicamente o CNPJ `34.338.660/0001-07` a Bastiani & Ferreira Ltda / clínica veterinária;
- diretórios atuais divergem de endereço: Bento Martins, 846 versus Borges do Canto, 1167.

### Decisão provisória

- resolver P0 quanto à presença operacional;
- incluir a operação no cenário-base exploratório;
- manter situação cadastral 2026 e endereço corrente como P2.

## 9. Resultado do lote

Os seis registros deixam de bloquear diretamente o cenário-base exploratório.

Mudanças:

- Marlin Fashion: P0 → P1;
- Mundi Calçados: P0 → P2;
- Ciranda Boutique: P0 → P2;
- Bicho Mimado: P0 → P1;
- Pet House: P0 → P1;
- Ponto dos Pets: P0 → P2.

A fila P0, que estava em 11 registros após o lote 20, cai para **5 registros** antes do lote seguinte.

## 10. P0 ainda remanescentes após o lote 21

- Pimentas Boutique Sensual;
- 7 Povos Kids;
- Loja CHICMI;
- Loja do Ramada;
- Akazzo.

## 11. Próxima etapa

Resolver o bloco final de P0 por regra de cenário-base:

- excluir do cenário-base operações sem evidência atual suficiente, preservando-as como pendências/sensibilidade;
- manter 7 Povos Kids isolado até fonte oficial atual inequívoca, pois existe conflito cadastral explícito.

## 12. Artefato

`docs/data_sources/bens_nao_essenciais_reconciliacao_p0_lote21_20260924_v001.csv`
