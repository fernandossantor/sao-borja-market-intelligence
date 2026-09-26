# TJRS — rota CNJ para remuneração da magistratura — v027

**Data da auditoria:** 2026-09-13  
**Geografia analítica:** São Borja/RS  
**Competência remuneratória-alvo:** julho/2026  
**Unidade pretendida:** R$/mês  
**Escopo da rota:** magistratura; não substitui a folha de servidores e demais agentes do TJRS.

## 1. Objetivo

Testar uma rota oficial e reproduzível, independente do portal do TJRS, para verificar se o **Painel de Remuneração dos Magistrados** do Conselho Nacional de Justiça poderia contribuir para territorializar a parcela da magistratura vinculada a São Borja.

A investigação preservou a regra do SBMI:

- nenhum nome, matrícula ou linha individual é persistido nos artefatos promovidos;
- norma, template e implementação observada são tratados como camadas distintas;
- nenhum valor remuneratório é promovido sem output territorial verificável;
- o contracheque único impede somas mecânicas de folhas fragmentadas.

## 2. Página oficial do CNJ e painel QlikSense

A página oficial corrente do CNJ **Remuneração dos Magistrados** mantém:

1. acesso ao painel público QlikSense;
2. vínculo para um **documento-padrão** de remessa de dados remuneratórios.

O painel foi identificado na rota oficial:

`https://paineisanalytics.cnj.jus.br/single/?appid=8ccb93ca-848f-4ffe-bf9b-96d57878c4d7&sheet=a710d8e5-fddb-4fa7-9098-4dbca30a391a&lang=pt-BR&theme=Mix_Theme&opt=ctxmenu,currsel`

Identificadores técnicos:

- appid: `8ccb93ca-848f-4ffe-bf9b-96d57878c4d7`;
- sheet: `a710d8e5-fddb-4fa7-9098-4dbca30a391a`.

**Classificação:** DADO OBSERVADO.

## 3. Documento-padrão CNJ — esquema territorial

A página corrente do CNJ vincula o arquivo oficial:

`https://www.cnj.jus.br/wp-content/uploads/2017/11/becada0200f03cb5a129ce57513f8ff3.xls`

Auditoria técnica:

- tamanho: **275.968 bytes**;
- formato: Microsoft Excel legado / OLE;
- metadados: último salvamento em setembro de 2017.

Foram observados no esquema/rótulos do arquivo, entre outros:

- Nome;
- Cargo;
- **Lotação**;
- Matrícula;
- Total Vantagens Pessoais;
- Total Vantagens Eventuais;
- Total Indenizações;
- Total de Rendimentos;
- Total de Descontos;
- Cargo de Origem;
- Remuneração;
- Abono de permanência;
- abono constitucional de 1/3 de férias;
- indenização por encargo curso/concurso;
- pagamentos retroativos.

O próprio arquivo informa que a primeira aba, **Contracheque**, possui campos que totalizam dados presentes em outras abas.

**Classificação:** DADO OBSERVADO — ESQUEMA DOCUMENTAL.

### Interpretação controlada

O padrão nacional vinculado pelo CNJ contempla uma **chave territorial de Lotação** associada a rubricas remuneratórias. Isso reforça a plausibilidade metodológica de uma territorialização direta da magistratura.

### Limitação

O arquivo é legado. O fato de continuar oficialmente vinculado em 2026 **não prova** que o aplicativo QlikSense corrente exponha todas as mesmas dimensões, nem que `Lotação` esteja atualmente disponível como filtro ou coluna exportável.

Portanto:

**template com Lotação ≠ implementação corrente empiricamente observada com Lotação.**

## 4. Auditorias técnicas do painel

### 4.1 Descoberta da rota oficial

Workflow:

`cnj-remuneracao-panel-discovery`

Run:

`34771335721`

Resultado:

- página oficial do CNJ recuperada;
- link atual do painel QlikSense identificado;
- link do documento-padrão identificado.

**Status:** sucesso.

### 4.2 Single Object / transporte HTTP

Workflow:

`cnj-remuneracao-qlik-audit`

Run:

`34771515553`

Resultados observados:

- HTTP **200**;
- conteúdo: `text/html;charset=utf-8`;
- tamanho do shell: **3.428 bytes**;
- servidor: `Microsoft-HTTPAPI/2.0`;
- título: `Single Object`;
- script principal observado: `/resources/main.js`.

**Interpretação:** o painel oficial existe e seu shell é alcançável pelo runner.

**Limitação:** HTTP 200 do shell não equivale a acesso ao modelo analítico.

### 4.3 Qlik Engine — WebSocket

Workflow:

`cnj-remuneracao-qlik-engine-schema`

Run:

`34771614486`

Foram testadas duas tentativas diretas ao app:

- sem subprotocolo;
- com `qlik-json-protocol`.

Ambas retornaram:

**HTTP/1.1 403 Forbidden**

durante o handshake WebSocket.

**Classificação:** DADO OBSERVADO — AUDITORIA TÉCNICA.

**Interpretação:** o motor Qlik não aceitou o acesso direto anônimo por esse canal.

**Não significa:** inexistência do painel ou indisponibilidade para usuários em navegador.

### 4.4 Renderização com Chromium

Workflow:

`cnj-remuneracao-qlik-chromium-audit`

Run:

`34771747237`

Resultados:

- Chromium presente no runner;
- execução concluída com código 0;
- shell Qlik renderizado;
- DOM serializado: **197.784 bytes**;
- componentes/classes Qlik foram observados;
- o DOM serializado não materializou textos correspondentes a:
  - São Borja;
  - Lotação;
  - Tribunal.

**Classificação:** DADO OBSERVADO — AUDITORIA TÉCNICA.

### Limitação crítica

Objetos Qlik podem ser virtualizados, renderizados fora do texto convencional do DOM, depender de sessão do motor ou ser materializados de maneira assíncrona. Logo:

**ausência no DOM serializado ≠ ausência da dimensão no modelo Qlik.**

O teste apenas demonstra que esse método não produziu um output territorial reproduzível.

## 5. Relação com o contracheque único

A Resolução CNJ nº 681/2026 introduziu o **contracheque único** e reforçou que a transparência remuneratória deve corresponder ao total mensal efetivamente pago, evitando divulgação fragmentada.

Para o SBMI, a consequência permanece:

- não somar mecanicamente folhas `Normal`, `Complementar`, `Mensal Complementar` e `Complementar Extraordinária`;
- qualquer agregado final deve representar um único total mensal por vínculo/pessoa;
- a territorialização deve usar chave observada de lotação/unidade de efetivo exercício.

## 6. Resultado metodológico

### Dado observado

Há uma rota oficial CNJ para remuneração da magistratura e o documento-padrão nacional atualmente vinculado contém `Lotação`.

### Dado não observado

Não foi recuperado, nesta auditoria, um output corrente do QlikSense que combine empiricamente:

- TJRS;
- julho/2026;
- São Borja;
- remuneração mensal;
- lotação/unidade territorial.

### Consequência

**Nenhum valor de remuneração foi promovido.**

A rota CNJ permanece útil como fallback oficial para a magistratura, mas não fecha a folha do TJRS em São Borja.

## 7. Escopo: magistratura não equivale ao TJRS territorial completo

Mesmo que o painel CNJ fosse territorializado com sucesso, ele cobriria a magistratura.

A massa TJRS de São Borja também envolve:

- os **32 cargos providos** do núcleo efetivo controlado por TLP e relatório de cargos;
- outros agentes eventualmente presentes no Anexo V;
- vantagens e rubricas próprias da folha;
- situações funcionais que não podem ser imputadas a partir de tabela de vencimentos.

Por isso, a rota CNJ é **complementar**, não substitutiva.

## 8. Decisão da v027

A rota CNJ é considerada **auditada e esgotada no nível necessário para a v027**.

Status:

- roster territorial TJRS: **VALIDADO**;
- estrutura de 32 cargos efetivos: **VALIDADA**;
- coerência TLP × cargos: **FORTE**;
- envelope estatutário: **PROMOVIDO COMO CONTROLE**;
- padrão CNJ com Lotação: **VALIDADO DOCUMENTALMENTE**;
- output corrente territorial de remuneração: **NÃO RECUPERADO**;
- massa remuneratória real TJRS/São Borja: **NÃO PROMOVIDA**.

Novo ganho quantitativo material requer:

1. output oficial do TJRS compatível com o contracheque único e com chave territorial; ou
2. dataset oficial equivalente que exponha remuneração mensal e lotação/unidade de exercício de forma observável e reproduzível.

Não serão usados:

- imputação por cargo;
- média estadual;
- benchmark entre comarcas;
- envelope estatutário como estimativa de folha;
- template CNJ como substituto da implementação observada.

## 9. Impacto sobre o fechamento da camada estadual

O resultado não altera a decisão geral:

- **MPRS:** promovido por territorialização direta;
- **DPERS:** promovida por envelopes documentais controlados;
- **TJRS:** estrutura territorial promovida; massa real não promovida;
- **TCE-RS:** não promovido;
- **ALRS:** não promovida.

A camada estadual de demais poderes permanece **FECHADA NO LIMITE DOCUMENTAL ATUAL**.

## 10. Artefatos Drive

Planilha técnica v027:

`1HjfbGo8qA2ZydfCrbouBVjlHDo8DRZs04H3cYr_FKMo`

Nova aba:

`TJRS_CNJ_painel_v027`

Caderno narrativo v027:

`1g2xnVccRF8Eu-JRVCpwJb2wZodgbymuFdhOaVW1G2y4`

Seção adicionada:

`27.17 Rota CNJ para a magistratura — padrão territorial confirmado, output corrente não recuperado`

Registro metodológico v027:

`1TL2Hd6SmcjxPPck8v49VSyvZjQAK9sUH5IHRM2FNACM`

Seção adicionada:

`25. ROTA CNJ DE REMUNERAÇÃO DA MAGISTRATURA — AUDITORIA DE FALLBACK`

## 11. Governança

Branch:

`feature/cnpj-territorial-control-v1`

PR #41 deve permanecer:

- **ABERTO**;
- **DRAFT**;
- **SEM MERGE**.

Nenhuma integração à `main` está autorizada.
