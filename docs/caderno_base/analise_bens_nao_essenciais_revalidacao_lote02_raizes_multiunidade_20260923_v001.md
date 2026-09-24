# Revalidação de CNPJs — bens não essenciais — lote 02 — raízes multiunidade — 23/09/2026

## 1. Objeto e governança

Continuação direta do lote 01 e do checkpoint de 23/09/2026.

Regras preservadas:

- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 permanece aberto, draft e sem merge;
- Caderno-Base Territorial v028 permanece read-only;
- nenhum recálculo de oferta ativa, número final de operadores, concentração ou proporção multiunidade é autorizado nesta etapa;
- CNPJ/raiz é unidade cadastral, não market share nem necessariamente storefront físico;
- fontes cadastrais secundárias permanecem subordinadas à confirmação oficial RFB.

## 2. Escopo

Este lote prioriza três raízes já sinalizadas como multiunidade no inventário:

1. `10.343.219` — Rogeria Tatiane Machado Loureiro — Volúpia / Lolita;
2. `92.012.467` — Grazziotin S.A.;
3. `07.195.827` — Daniela Pitrovski Dornelles — Companhia dos Bichos.

Foram revalidados **6 CNPJs pertencentes ao universo original de 103 CNPJs** e identificados **4 CNPJs adicionais** da raiz Grazziotin em São Borja.

A cobertura do universo original passa, portanto, de 11 para **17 dos 103 CNPJs** com alguma revalidação. Esse valor é apenas **cobertura de auditoria**.

## 3. Resultados

### 3.1 Volúpia / Lolita — raiz 10.343.219

Foram confirmados por fontes cadastrais secundárias:

- `10.343.219/0001-47` — Volúpia Moda Íntima — matriz — Rua Cândido Falcão, 908, sala 101 — ativa;
- `10.343.219/0002-28` — Lolita Lingerie — filial — Rua General Osório, 2215, sala 101 — ativa.

Os endereços são distintos e a própria ficha da matriz lista a filial.

**Interpretação:** o inventário representa corretamente dois CNPJs distintos da raiz.  
**Decisão provisória:** manter ambos; nenhuma inferência de participação de mercado ou número de storefronts será feita antes de confirmação operacional/RFB.

### 3.2 Grazziotin — raiz 92.012.467

O inventário registrava apenas dois CNPJs da raiz em São Borja:

- `92.012.467/0190-08` — Franco Giorgi;
- `92.012.467/0037-80` — rotulado no inventário como “Lojas Grazziotin”.

A revalidação mostrou que:

- `/0190-08` permanece ativo como **Franco Giorgi**, atualmente em Rua General Marques, 969, sala 102;
- `/0037-80` permanece ativo, mas a fantasia cadastral corrente é **GZT Express**, em Rua General Marques, 969, sala 101.

Há, portanto, **co-localização no mesmo número**, com salas diferentes. Isso impede converter automaticamente dois CNPJs em dois pontos de venda independentes.

Além disso, foram identificados quatro CNPJs ativos da mesma raiz em São Borja que não estavam no inventário:

- `92.012.467/0094-79` — Tottal Casa & Lazer — Rua Eddie Freire Nunes, 1999;
- `92.012.467/0121-86` — Por Menos — Avenida Presidente Vargas, 1206;
- `92.012.467/0265-60` — Tech Box — Rua General Marques, 1066;
- `92.012.467/0451-90` — Pormenos — Rua Cândido Falcão, 940, sala 02.

**Dado observado:** o inventário documental está subcoberto em relação à raiz Grazziotin.

**Interpretação:** há pelo menos seis estabelecimentos cadastrais da raiz em São Borja nas fontes consultadas. Isso não equivale, sem reconciliação adicional, a seis lojas físicas independentes.

**Decisão provisória:** manter os dois CNPJs originais, atualizar no sucessor a fantasia corrente de `/0037-80` para GZT Express com preservação do histórico, e registrar os quatro adicionais em camada de controle até confirmação oficial/operacional.

### 3.3 Companhia dos Bichos — raiz 07.195.827

Foram encontrados:

- `07.195.827/0001-47` — Companhia dos Bichos — matriz — Rua Félix da Cunha, 766 — ativa;
- `07.195.827/0002-28` — Companhia dos Bichos — filial — Rua Riachuelo, 1329, sala 101 — ativa segundo a listagem da raiz e fontes empresariais.

Documento oficial municipal histórico também vincula a matriz ao endereço da Rua Félix da Cunha.

**Interpretação:** a estrutura documental multiunidade do inventário é compatível com as evidências disponíveis.

**Decisão provisória:** manter ambos, sem extrapolar para market share, faturamento ou participação concorrencial.

## 4. Auditoria dos dados

### Observado

- situação cadastral informada pelas fontes consultadas;
- CNPJ, natureza matriz/filial, fantasia e endereço;
- quatro CNPJs adicionais da raiz Grazziotin;
- co-localização atual de GZT Express e Franco Giorgi no mesmo número;
- divergência entre o rótulo histórico “Lojas Grazziotin” do inventário e a fantasia corrente GZT Express.

### Calculado

- cobertura do universo original após este lote: `17 / 103 × 100 = 16,50%`.

Esse percentual mede apenas o avanço da revalidação.

### Interpretação

- a raiz Grazziotin estava sub-representada no inventário;
- o número de CNPJs de uma raiz não pode ser transformado automaticamente em número de lojas físicas;
- mudanças de fantasia/endereço precisam ser preservadas temporalmente, não corrigidas retroativamente sem nota.

## 5. Limitações

- A rota de confirmação oficial direta da RFB permanece indisponível no ambiente atual.
- A maior parte das situações cadastrais deste lote provém de republicadores da base pública do CNPJ.
- Documentos institucionais/históricos foram usados apenas como triangulação de CNPJ/endereço.
- Não há medição de faturamento, fluxo de clientes ou participação de mercado.
- A co-localização de CNPJs da Grazziotin exige validação física/operacional antes de qualquer contagem de unidades comerciais.

## 6. Artefato auditável

CSV:

`docs/data_sources/bens_nao_essenciais_revalidacao_lote02_raizes_multiunidade_20260923_v001.csv`

Cada registro distingue CNPJ de origem do inventário de CNPJ adicional descoberto na revalidação.

## 7. Próxima etapa

Prosseguir com redes e reconciliações de alta prioridade:

- Lins Ferrão / Pompéia;
- Monjuá / Lojas Três Passos;
- RM2S / MAXX Outlet;
- Lojas P & S;
- Brasil Free Shop / Monaco;
- corrigenda do lote 01 para a terceira filial Quero-Quero identificada durante a expansão da auditoria.

Nenhuma métrica estrutural será recalculada até cobertura suficiente.
