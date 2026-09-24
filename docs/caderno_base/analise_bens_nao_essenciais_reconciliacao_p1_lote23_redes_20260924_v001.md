# Bens não essenciais — reconciliação P1 — lote 23 — redes e função física — 24/09/2026

## 1. Objeto

Primeiro lote dirigido à fila **P1**, priorizando CNPJs adicionais de grandes redes cuja principal pendência era distinguir:

- estabelecimento jurídico;
- unidade comercial aberta ao público;
- duplicidade documental;
- unidade adicional sem evidência de storefront.

Foram tratados seis CNPJs:

- Lojas Quero-Quero — `96.418.264/0028-59`;
- Lojas Quero-Quero — `96.418.264/0533-30`;
- Tottal Casa & Lazer — `92.012.467/0094-79`;
- Por Menos — `92.012.467/0121-86`;
- Tech Box — `92.012.467/0265-60`;
- Pormenos — `92.012.467/0451-90`.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhum indicador canônico recalculado.

## 2. Regra metodológica

Um CNPJ adicional de uma raiz já presente **não é automaticamente uma nova loja**.

Para ser incorporado como storefront no cenário-base exploratório, este lote exigiu convergência entre:

1. situação cadastral compatível;
2. endereço próprio;
3. evidência operacional/comercial da unidade no endereço.

Quando existe apenas o CNPJ ativo, sem evidência de atendimento ao público, o estabelecimento jurídico permanece fora da contagem-base de storefronts e é mantido em sensibilidade.

## 3. Lojas Quero-Quero — raiz 96.418.264

### 3.1 CNPJ 96.418.264/0028-59 — General Marques, 694

### Dados observados

A unidade apresenta:

- CNPJ ativo em bases cadastrais recentes;
- endereço cadastral Rua General Marques, 694;
- diretório operacional rastreado em 2026 com loja, telefone e horários;
- lista de representantes da Assurant em 2025 com unidade de São Borja na General Marques, 694;
- lista institucional da Tramontina com **duas Lojas Quero-Quero em São Borja**, uma na General Marques, 694 e outra na Coronel Aparício Mariense, 2635.

Há um localizador rastreado há aproximadamente 1,3 ano que marcava a unidade da General Marques como “fechada”. Essa evidência é temporalmente conflitante com fontes cadastrais e operacionais posteriores.

### Interpretação

A evidência mais recente e específica sustenta que `/0028-59` corresponde a uma **unidade comercial distinta** da `/0357-81`.

### Decisão provisória

- resolver a duplicidade do inventário;
- manter `96.418.264/0357-81` para Aparício Mariense, 2635;
- substituir a segunda ocorrência repetida pelo CNPJ `96.418.264/0028-59`, General Marques, 694;
- contar as duas como storefronts distintos no **cenário-base exploratório**.

Isso corrige a identidade das unidades; não altera ou estima faturamento.

### 3.2 CNPJ 96.418.264/0533-30 — Homero Pereira Coimbra, 54

### Dados observados

O CNPJ está ativo e corresponde a filial da Lojas Quero-Quero, aberta em 03/09/2021, em Rua Homero Pereira Coimbra, 54.

Não foi encontrada, contudo, evidência operacional comparável à das duas lojas centrais:

- não foi localizado diretório atual de loja aberta ao público nesse endereço;
- as listas operacionais consultadas registram General Marques e Aparício Mariense, mas não Homero Pereira Coimbra.

### Interpretação

É um estabelecimento jurídico ativo da raiz, mas sua **função física não está demonstrada como storefront**.

### Decisão provisória

- retirar o caso do P1 para efeito do denominador-base;
- **não contar `/0533-30` como storefront no cenário-base**;
- mantê-lo em cenário de sensibilidade e na camada jurídica da raiz;
- reabrir a função física caso apareça evidência de atendimento ao público.

Ausência de evidência de loja não equivale a prova de que a unidade não exerça varejo.

## 4. Grazziotin — raiz 92.012.467

Quatro CNPJs adicionais da raiz receberam evidência suficiente de unidade comercial distinta.

### 4.1 Tottal Casa & Lazer — 92.012.467/0094-79

- situação ativa;
- filial;
- Rua Eddie Freire Nunes, 1999;
- fantasia Tottal Casa & Lazer;
- diretório empresarial atual no mesmo endereço.

**Decisão:** incorporar como storefront distinto no cenário-base exploratório.

### 4.2 Por Menos — 92.012.467/0121-86

- situação ativa;
- Grazziotin S.A. — Por Menos;
- Avenida Presidente Vargas, 1206;
- comércio varejista de vestuário;
- diretório atual com CNPJ e endereço.

**Decisão:** incorporar como storefront distinto.

### 4.3 Tech Box — 92.012.467/0265-60

- situação ativa;
- filial;
- fantasia Tech Box;
- Rua General Marques, 1066;
- CNAE principal de comércio varejista de artigos de óptica;
- diretório atual no mesmo CNPJ/endereço.

**Decisão:** incorporar como storefront distinto, preservando sua classificação setorial própria.

### 4.4 Pormenos — 92.012.467/0451-90

- situação ativa;
- filial;
- fantasia Pormenos;
- Rua Cândido Falcão, 940, sala 02;
- diretório empresarial rastreado em setembro/2026 no mesmo CNPJ/endereço.

**Decisão:** incorporar como storefront distinto.

### Observação sobre as duas marcas Por Menos/Pormenos

Os CNPJs `/0121-86` e `/0451-90` não devem ser deduplicados pelo nome semelhante. São estabelecimentos completos distintos, em endereços diferentes.

## 5. Registro histórico adicional não promovido

Durante a investigação apareceu o CNPJ `92.012.467/0095-50`, associado historicamente a Por Menos em Rua General Marques, 850, em listas antigas de emitentes NF-e do Rio Grande do Sul.

Não foi localizada evidência corrente suficiente em 2026.

**Decisão:** não adicionar ao universo corrente nesta versão. Preservar apenas como pista histórica para futura auditoria temporal da raiz Grazziotin.

## 6. Resultado do lote

### Dados observados

- cinco dos seis CNPJs tratados possuem evidência suficiente para decisão de storefront;
- quatro CNPJs adicionais Grazziotin são unidades comerciais distintas;
- Quero-Quero `/0028-59` é unidade distinta e corrige a duplicidade do inventário;
- Quero-Quero `/0533-30` permanece estabelecimento jurídico ativo sem prova suficiente de storefront.

### Decisões calculadas

Para o cenário-base exploratório:

- **5 storefronts adicionais/corrigidos são elegíveis**;
- **1 estabelecimento jurídico ativo não é contado como storefront**.

Isso **não significa aumento líquido de cinco lojas sobre o inventário original**, pois `/0028-59` substitui uma linha duplicada já existente. O efeito líquido só poderá ser calculado ao consolidar o cenário-base completo.

## 7. Efeito sobre a fila

Os seis registros deixam de P1:

- `/0028-59`: função storefront resolvida;
- `/0533-30`: decisão conservadora de não contar no cenário-base, mantendo sensibilidade;
- quatro CNPJs Grazziotin: função storefront resolvida.

A próxima versão da fila deve reduzir P1 de 24 para **18 registros de controle**, salvo inclusão de nova pendência estruturante descoberta na atualização.

## 8. Próxima etapa

Continuar P1 com os demais casos capazes de alterar número de unidades ou identidade do operador, priorizando:

- M.H. Moda Íntima — matriz adicional;
- Brasil Free Shop — CNPJ adicional;
- RM2S — filial adicional sem marca identificada;
- João e Maria Pet — matriz adicional;
- Barraca Missões — segunda filial;
- Requinte — CNPJ adicional;
- Pompéia — correção da associação de CNPJ;
- sucessões/homonímias de Amei, Veterinária São Francisco, Excêntrica e Rilu.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_reconciliacao_p1_lote23_redes_20260924_v001.csv`
