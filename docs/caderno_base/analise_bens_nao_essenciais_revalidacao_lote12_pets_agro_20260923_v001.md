# Revalidação de CNPJs — bens não essenciais — lote 12 — pets e agropecuárias — 23/09/2026

## 1. Escopo e governança

Este lote cobre sete CNPJs do universo original:

- João e Maria Pet e Rações;
- Animed;
- Agrolago Rações;
- Barraca Missões;
- Máximo Agropecuária;
- Agropecuária Vieira;
- Agropecuária Centauro.

Também foram identificados dois CNPJs adicionais em São Borja, pertencentes a raízes já presentes no inventário:

- `59.205.031/0001-21` — matriz de Mariza Matoso Pedebos Ltda;
- `92.293.703/0011-45` — nova filial Barraca Missões.

Mantêm-se:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhuma recomposição de oferta ativa, número final de operadores, concentração ou proporção multiunidade.

Cobertura acumulada após este lote:

- examinados: **87/103 = 84,47%**;
- com evidência independente de revalidação/reconciliação: **86/103 = 83,50%**.

Pimentas Boutique Sensual permanece como o único CNPJ já examinado sem evidência externa independente suficiente nesta sequência.

## 2. João e Maria Pet e Rações — raiz 59.205.031

### 2.1 Filial do inventário — 59.205.031/0002-02

Duas fontes cadastrais recentes convergem para:

- situação ativa;
- filial;
- abertura em 20/03/2026;
- fantasia João e Maria Pet e Rações;
- Rua Coronel Aparício Mariense, 2287, sala 101;
- CNAE principal de varejo de animais e artigos/alimentos para pets.

**Decisão provisória:** manter.

### 2.2 Matriz adicional — 59.205.031/0001-21

Foi localizada a matriz da mesma raiz em São Borja:

- ativa;
- aberta em 30/01/2025;
- 10A Rua Borges do Canto, 385, sala 101, bairro Tiro;
- CNAE principal de varejo pet;
- sem fantasia cadastral disponível nas fontes consultadas.

**Interpretação:** a raiz está subcoberta no inventário.

**Limite:** não é correto atribuir automaticamente a marca João e Maria à matriz sem evidência operacional específica.

**Decisão provisória:** adicionar a matriz à camada de controle, sem incorporá-la ao denominador canônico antes de mapear função e ponto físico.

## 3. Animed — 32.010.824/0001-39

Duas fontes cadastrais apresentam:

- situação ativa;
- matriz;
- fantasia Animed;
- atividade principal veterinária;
- Rua Vereador Fausto de Lourenço Aquino, 1731.

Há também licença municipal oficial de 2019 para o mesmo CNPJ como clínica veterinária, mas então localizada no nº 1801 da mesma via.

**Interpretação:** CNPJ, marca e atividade são compatíveis; o endereço deve ser tratado temporalmente.

**Decisão provisória:** manter o CNPJ e utilizar o endereço cadastral corrente com nota histórica da licença municipal.

## 4. Agrolago Rações — 50.578.611/0001-90

A Econodata, em lista de empresas de rações de São Borja atualizada em agosto/2026, apresenta:

- CNPJ `50.578.611/0001-90`;
- Tusnel Segobia Lago;
- fantasia Agrolago Rações;
- 10A Rua Vereador Joceimar Carpes, 77, bairro Passo;
- CNAE principal de varejo pet;
- inclusão no conjunto classificado pela plataforma como empresas ativas.

Diretório operacional muito recente mantém **Agrolago Rações Agropecuária** no mesmo endereço.

**Interpretação:** identidade, marca, atividade e presença operacional convergem.

**Limite:** nesta rodada não foi recuperada ficha individual da situação cadastral do CNPJ.

**Decisão provisória:** manter, classificando explicitamente o status como derivado de listagem setorial recente, e não como confirmação direta da ficha RFB.

## 5. Barraca Missões — raiz 92.293.703

### 5.1 Filial do inventário — 92.293.703/0005-05

Duas fontes cadastrais recentes convergem para:

- situação ativa;
- filial;
- fantasia Barraca Missões;
- Rua Engenheiro Manoel Luís Fagundes, 1372;
- CNAE principal de varejo de medicamentos veterinários.

**Decisão provisória:** manter.

### 5.2 Segunda filial em São Borja — 92.293.703/0011-45

Foi localizada outra filial ativa da mesma raiz:

- aberta em 28/10/2025;
- fantasia Barraca Missões;
- Avenida Bernardo de Mello, 150, Pirahy;
- CNAE principal de varejo de medicamentos veterinários;
- fonte que informa consulta à RFB em 08/08/2026.

**Interpretação:** a raiz Barraca Missões está subcoberta no inventário.

**Limite:** dois CNPJs locais da mesma raiz não significam automaticamente duas lojas abertas ao público; uma filial pode exercer outra função operacional.

**Decisão provisória:** adicionar `/0011-45` à camada de controle e mapear função física antes de qualquer recálculo.

## 6. Máximo Agropecuária — 58.600.410/0001-53

A empresa foi revalidada como:

- ativa;
- matriz;
- fantasia Máximo Agropecuária;
- aberta em 02/01/2025;
- 10A Rua Patrício Petit Jean, 2475, bairro Passo;
- CNAE principal de varejo pet;
- atividades secundárias em ferragens, calçados e outros itens.

**Decisão provisória:** manter.

## 7. Agropecuária Vieira — 11.263.905/0001-70

Este caso requer cautela nos metadados jurídicos.

Evidências atuais mostram:

- operação **Agropecuária Vieira** muito recente na Rua Almirante Tamandaré, 239, bairro Passo;
- agregadores recentes a listam como ativa;
- fonte societária afirma que Vanessa Vieira da Silva integra o CNPJ `11.263.905/0001-70` como sócio-administrador, com quadro societário verificado na RFB em 08/2026;
- registro oficial JUCISRS de 2020 menciona alteração de **Neri T. Vieira Benites & Cia Ltda**, razão social usada no inventário.

**Dado observado:** CNPJ, marca e endereço atual convergem.

**Não é possível concluir ainda:** se a razão social corrente continua exatamente “Neri T. Vieira Benites & Cia Ltda”.

**Decisão provisória:** manter o CNPJ e preservar a razão social do inventário como histórica até confirmação por ficha RFB atual.

## 8. Agropecuária Centauro — 29.263.180/0001-86

Fonte cadastral atualizada em agosto/2026 apresenta:

- situação ativa;
- matriz;
- razão social Valdecir L. de Assunção;
- fantasia Agropecuária Centauro;
- Rua Borges do Canto, 84, bairro Tiro;
- CNAE principal de varejo pet;
- atividades secundárias de ferragens e artigos de caça, pesca e camping.

Diretório operacional recente confirma a presença da marca no mesmo endereço.

**Decisão provisória:** manter.

## 9. Resultado metodológico

### Dados observados

- João e Maria, Animed, Barraca Missões, Máximo e Centauro possuem evidência cadastral ativa convergente;
- Agrolago possui evidência setorial recente de atividade e presença operacional, mas sem ficha individual recuperada;
- Agropecuária Vieira tem presença operacional e vínculo atual do CNPJ, porém razão social corrente ainda requer confirmação;
- duas raízes estavam subcobertas: João e Maria e Barraca Missões.

### Dados calculados

- examinados acumulados: `87 / 103 × 100 = 84,47%`;
- com evidência independente acumulada: `86 / 103 × 100 = 83,50%`.

### Interpretação

A cobertura já supera 80%, mas ainda não deve ser confundida com cobertura de **oferta ativa reconciliada**. Para o primeiro recálculo estrutural será necessário, no mínimo:

1. terminar os CNPJs restantes;
2. separar CNPJ ativo de marca ativa;
3. resolver baixadas/inaptas e sucessões;
4. reconciliar CNPJs adicionais;
5. remover registros fora do escopo varejista;
6. tratar linhas sem CNPJ que puderem ser identificadas com segurança.

## 10. Próxima etapa

Prosseguir para joalherias, ópticas e papelaria:

- Joalheria e Ótica Diamante Saoborjense;
- Finger Joias;
- Elegance;
- J Martins Joalheiros;
- Joias El Shadday;
- Esmeralda Joias;
- Lela Joias;
- Óptica Moca;
- Tayne Joias;
- Encanto Semijoias;
- Joalheria Brilhante;
- Gaffiti Papelaria;
- Consermaq.

As linhas sem CNPJ extraível devem ser tratadas separadamente, apenas quando houver identificação documental robusta.

## 11. Artefato

`docs/data_sources/bens_nao_essenciais_revalidacao_lote12_pets_agro_20260923_v001.csv`
