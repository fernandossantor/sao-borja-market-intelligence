# Bens não essenciais — linhas originalmente sem CNPJ — lote 16A — vestuário — 23/09/2026

## 1. Objeto

Este lote inicia a revisão das **16 linhas originalmente sem CNPJ extraível** no inventário de bens não essenciais.

O lote 16A cobre oito linhas de vestuário/calçados:

- 121 — Magazine Bandeirante;
- 123 — 7 Povos Confecções e Calçados;
- 125 — Loja CHICMI;
- 126 — Loja do Ramada;
- 130 — Ka Lopes Fitness;
- 132 — Loja Portal;
- 134 — Elegância Moda e Acessórios;
- 141 — Carol Modas.

A regra metodológica é mais conservadora do que a aplicada aos 103 CNPJs originais: **nenhum CNPJ é preenchido apenas por coincidência de endereço, telefone, nome pessoal ou categoria comercial**.

## 2. Resultado do lote

### CNPJ recuperado com evidência forte — 1

**Carol Modas — linha 141**

Foi identificado:

- CNPJ `88.721.220/0001-55`;
- razão social Carolina Oliveira Maciel;
- situação ativa em fonte cadastral;
- Rua Cândido Falcão, 1247;
- CNAE principal de comércio varejista de vestuário.

A associação à marca recebe triangulação operacional: seller **Carol_Modas_Saoborja** no Magalu utiliza exatamente o mesmo CNPJ, razão social e endereço.

**Decisão provisória:** preencher o CNPJ na linha 141 do sucessor.

### Candidatos de identidade, mas sem CNPJ seguro — 2

**Ka Lopes Fitness — linha 130**

A marca continua listada em Avenida Presidente Vargas, 1938, telefone 3431-5212. O mesmo telefone e o mesmo endereço histórico aparecem, em documento de 2013, associados a Ana Karine Mello Lopes, CNPJ `15.009.711/0001-02`.

Esse CNPJ permanece ativo, porém a ficha atual utiliza outro número da Presidente Vargas e CNAE principal de informática.

**Interpretação:** existe um indício relevante de relação histórica, mas não evidência suficiente para preencher o CNPJ da Ka Lopes em 2026.

**Decisão:** registrar `15.009.711/0001-02` apenas como **candidato fraco**, sem promoção.

**Loja Portal — linha 132**

A Loja Portal continua listada na Rua General Marques, 1236. No mesmo endereço aparecem:

- Nayef Abdo Hijazi;
- registro empresarial “Nayef Abdo Hijazi Filial 2”;
- atividade de varejo de roupas.

O CNPJ não foi recuperado.

**Decisão:** registrar Nayef Abdo Hijazi apenas como **candidato de identidade jurídica**, sem preencher CNPJ.

### Presença/marca documentada, mas CNPJ não recuperado — 3

**Magazine Bandeirante — linha 121**

Há evidência histórica forte: notícia regional de 2021 registrou que a loja, aberta no endereço em 1976, seguia funcionando. Diretórios rastreados em 2026 continuam listando Magazine Bandeirante em General Osório, 1373.

**Decisão:** manter linha sem CNPJ, com presença documentada; buscar pessoa jurídica por fonte fiscal/municipal.

**7 Povos Confecções e Calçados — linha 123**

Diretórios atuais continuam listando a marca em São Borja, inclusive com descrição de operação há mais de 30 anos. CNPJ específico não foi recuperado.

**Decisão:** manter sem CNPJ e não agregar a outras empresas “7 Povos”, pois as raízes conhecidas são distintas.

**Loja do Ramada — linha 126**

A marca aparece em lista histórica de estabelecimentos conveniados de São Borja, mas não foi obtida evidência cadastral ou operacional recente suficientemente específica.

**Decisão:** preservar como registro histórico com status 2026 pendente.

### Sem evidência independente recuperável — 2

- Loja CHICMI — linha 125;
- Elegância Moda e Acessórios — linha 134.

Buscas dirigidas não retornaram fonte empresarial específica confiável.

**Não é possível concluir:** baixa, encerramento, troca de nome, troca de CNPJ ou inexistência.

## 3. Dados calculados

No lote 16A:

- linhas examinadas: **8**;
- CNPJ recuperado com evidência forte: **1**;
- candidato de identidade/CNPJ ainda insuficiente: **2**;
- presença documentada sem CNPJ: **3**;
- sem evidência independente recuperável: **2**.

Essas contagens são de **auditoria de lacunas**, não de oferta ativa.

## 4. Implicação metodológica

A revisão confirma que as 16 linhas sem CNPJ não podem ser resolvidas por uma única estratégia:

- algumas permitem recuperação robusta de CNPJ;
- outras só permitem identificar a marca/ponto;
- outras produzem candidatos jurídicos fracos;
- outras permanecem sem evidência.

Isso reforça que o universo reconciliado deverá possuir um campo de **grau de identificação documental** em vez de tratar todas as linhas sem CNPJ como equivalentes.

## 5. Próxima etapa

Lote 16B:

- Casa A Favorita;
- Akazzo;
- Amei Presentes Criativos;
- Bella Cestas & Presentes;
- Monaco Freeshop;
- Pet House;
- Marco Relojoeiro;
- Mais Top Papelaria.

Monaco e Mais Top já possuem CNPJs recuperados em lotes anteriores e entrarão no fechamento das 16 linhas para evitar dupla contagem.

## 6. Governança

- Caderno-Base v028 permanece read-only.
- PR #41 permanece aberto, draft e sem merge.
- Nenhuma linha recuperada é incorporada ainda ao denominador de oferta ativa.

## 7. Artefato

`docs/data_sources/bens_nao_essenciais_sem_cnpj_lote16a_vestuario_20260923_v001.csv`
