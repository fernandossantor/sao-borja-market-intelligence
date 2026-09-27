# NFS-e/CFS-e de São Borja — auditoria de endpoints públicos — v001

**Data:** 2026-09-26  
**Geografia:** São Borja/RS  
**Sistema:** Portal do ISS / NFS-e — domínio `nfse.saoborja.rs.gov.br`  
**Finalidade:** verificar se o portal público e não autenticado expõe dados agregados monetários que permitam dimensionar o mercado de Serviços sem solicitar extração à Prefeitura.  
**Natureza:** auditoria técnica de superfície pública; não foram utilizados login, cookies autenticados, credenciais, tokens privados ou tentativa de contornar controle de acesso.

## 1. Pergunta

Existe endpoint público anônimo que forneça, para São Borja, valores agregados de NFS-e/CFS-e por período, atividade/item de serviço ou outra dimensão útil à dimensão de mercado?

## 2. Método

Foram executadas duas auditorias reprodutíveis:

1. carregamento automatizado do portal público, captura apenas de requisições anônimas do próprio domínio e inspeção das respostas;
2. inspeção estática do bundle JavaScript público `/portal/app.js`, restrita a referências de endpoints marcados como `public` e ao contexto funcional em que são chamados.

A persistência excluiu cabeçalhos de autenticação, cookies e credenciais.

## 3. Endpoints efetivamente acionados pelo portal público

Na abertura da página inicial, foram observadas as seguintes chamadas XHR anônimas relevantes:

| Endpoint | Resposta observada | Uso |
|---|---|---|
| `/services/cadastros/public/portal/configuracao/issqn` | JSON de configuração do portal | menus, funcionalidades, contato e parametrização |
| `/services/cadastros/public/consulta/qtdEmitentesNFSe` | `6.900` | contador de emitentes |
| `/services/nfse/public/consulta/qtdNotasEmitidas` | `4.225.020` | contador de NFS-e emitidas no momento da auditoria |
| `/services/cadastros/public/portal/conteudos` | `[]` | conteúdos públicos |
| `/services/parametros/public/valueOf/P_EXIBIR_NOME_DESIF_MENU_DIFE` | `S` | parâmetro de interface |

**Dado observado:** nenhum desses endpoints retorna valor monetário de serviços, competência, item de serviço, CNAE, município do tomador ou base de cálculo.

Os contadores são dinâmicos. Em consulta anterior no mesmo dia, o portal exibia quantidade menor de NFS-e emitidas. Portanto, `qtdNotasEmitidas` deve ser tratado como contador acumulado no instante da consulta, sem período explícito, e não como série estatística.

## 4. Configuração pública do portal

A resposta de configuração confirma:

- cliente: São Borja;
- módulo: ISSQN;
- consulta externa de NFS-e por chave;
- acesso ao sistema autenticado;
- ambiente de testes;
- contato da Secretaria Municipal de Fazenda;
- e-mail de contato publicado: `iss@saoborja.rs.gov.br`.

**Uso correto:** rota institucional de contato e evidência de operação do sistema.

**Uso incorreto:** interpretar a existência do sistema ou quantidade de emitentes/notas como faturamento.

## 5. Endpoint público de relatórios

O bundle público contém a rota:

`/services/relatorios/public/relatorioTela/requisitar`.

A inspeção do código mostra que essa rota é acionada por um **componente genérico de renderização/exportação de relatórios** quando a propriedade `public` está habilitada.

O componente monta um payload contendo, entre outros:

- `dados`, quando os dados já estão no cliente;
- `colunas`;
- formato;
- título/subtítulo;
- ou `urlDados`, quando existe outra fonte de dados.

Depois envia esse payload ao endpoint de relatório para gerar arquivo/saída.

**Conclusão técnica:** a existência de `/relatorios/public/relatorioTela/requisitar` **não constitui uma API pública de microdados ou agregados de NFS-e**. É uma camada de geração de relatório a partir de dados previamente fornecidos ao componente.

Não foi identificada, na carga pública do portal, URL pública que forneça para esse componente uma tabela monetária de NFS-e.

## 6. Evidência de capacidade interna, não de abertura pública

O bundle genérico do sistema contém opções de ordenação/relatórios com campos como:

- `valor_servico`;
- `valor_base_calculo`;
- `iss_tomador`;
- `iss_proprio`;
- situação/cancelamento;
- prestador e tomador.

Isso é consistente com a documentação técnica da NFS-e já auditada e reforça a **viabilidade técnica** de solicitar uma extração agregada à administração.

Porém, o bundle é software de aplicação e pode compartilhar funcionalidades entre módulos/clientes. Portanto, esses nomes de campos não provam, isoladamente:

- completude histórica em São Borja;
- disponibilidade anônima;
- disponibilidade em uma única consulta;
- cobertura uniforme de 2023–2026.

## 7. Resultado da auditoria pública

### Observado

- endpoints públicos de configuração e contagem;
- contador de 6.900 emitentes;
- contador de 4.225.020 NFS-e no instante da execução;
- consulta externa individual por chave;
- componente público genérico para renderizar relatórios.

### Não localizado

Nenhum endpoint público anônimo foi localizado para:

- valor bruto agregado de NFS-e;
- valor por competência;
- valor por item/código de tributação;
- valor por CNAE;
- valor por município do tomador;
- quantidade de notas por período/categoria;
- base de cálculo/ISS agregados em formato estatístico.

### Classificação

**PUBLICAÇÃO PÚBLICA DIRETA: INSUFICIENTE PARA DIMENSÃO MONETÁRIA DO MERCADO DE SERVIÇOS.**

Isso não demonstra inexistência dos dados no sistema administrativo; demonstra apenas que eles não foram encontrados na superfície pública anônima auditada.

## 8. Implicação para o SBMI

A rota prioritária permanece a solicitação institucional de dados agregados à Prefeitura/Secretaria Municipal de Fazenda.

A especificação já definida continua válida:

`competência × código de tributação/item × município/local da prestação × município do tomador × situação × tipo de documento`

com métricas como:

- valor bruto do serviço;
- base tributável;
- número de documentos;
- número de prestadores na célula;
- indicador de cancelamento/substituição.

Nenhum dado individual é necessário.

## 9. Rastreabilidade

### Descoberta de endpoints

Workflow:
`.github/workflows/nfse-sao-borja-public-endpoint-discovery-v1.yml`

Run:
`36268105386`

Commit:
`a8d7d38a739a0c49cfb35d147d2158621482329f`

Artifact:
`10914950672`

Digest:
`sha256:58f91fd933a8f527626f767d255dc12f42564fd0a0fd1a43d994ca7b4658c98e`

Google Drive:
`SBMI_NFSe_Sao_Borja_endpoints_publicos_auditoria_v001.zip`  
ID: `1wc3XCSKBD60FaTg7ioK0ZPj5VGrv1rDI`

### Contexto do endpoint de relatórios

Workflow:
`.github/workflows/nfse-sao-borja-public-report-context-v1.yml`

Run:
`36268475097`

Artifact:
`10915030891`

Digest:
`sha256:8750db7d59d8c8b0825adb22377954b59219fd65ada8f12ab3066e9bcc9c043d`

Google Drive:
`SBMI_NFSe_Sao_Borja_contexto_endpoints_publicos_v001.zip`  
ID: `1XHfjjd0sYwOKQopGaqMQanvuyYobM0-H`

## 10. Decisão

A busca por uma API pública anônima de valores de NFS-e é encerrada nesta etapa.

**Não utilizar:**
- contador de notas como receita;
- número de emitentes como tamanho de mercado;
- ISS arrecadado dividido por alíquota como faturamento;
- endpoints autenticados/internos como fonte pública.

**Próximo passo:** formalizar a solicitação agregada à Secretaria Municipal de Fazenda, usando a especificação técnica já documentada.
