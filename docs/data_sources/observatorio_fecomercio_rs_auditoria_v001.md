# Observatório do Comércio Fecomércio-RS — auditoria exploratória

**Versão:** v001  
**Data:** 2026-09-17  
**Status:** exploratório — não canônico  
**Produtor:** Instituto Fecomércio-RS de Pesquisas (IFEP-RS)  
**Plataforma:** https://observatorio.fecomercio-rs.org.br/page/home

## Finalidade no SBMI

Usar o Observatório como fonte complementar e de validação cruzada para indicadores empresariais e setoriais, preservando a prioridade das fontes primárias quando estas já forem utilizadas diretamente pelo projeto.

## Conteúdo confirmado

Materiais públicos do lançamento descrevem dados sobre:
- empresas/estabelecimentos;
- emprego/trabalho;
- receitas;
- despesas;
- segmentação regional;
- segmentação por atividade econômica.

Também são divulgados indicadores próprios do IFEP-RS, incluindo rotatividade, concentração territorial e tempo de vida/atividade das empresas.

## Origem dos dados

A plataforma possui seção “Fonte dos dados”, que deve ser tratada como referência para mapear a proveniência de cada indicador.

Nesta v001, foram confirmadas externamente como fontes utilizadas pelo Observatório:
- Receita Federal;
- Ministério do Trabalho.

A lista detalhada da seção “Fonte dos dados” ainda não foi transcrita nesta auditoria, porque a aplicação é carregada dinamicamente e essa camada não ficou disponível no rastreamento textual automatizado. Não inferir outras bases sem validação direta na plataforma.

## Regra de integração

1. Se o Observatório reproduzir/transformar uma fonte primária já canonizada no SBMI, manter a fonte primária como referência principal.
2. Se o indicador for próprio do IFEP-RS, registrar:
   - nome do indicador;
   - definição;
   - fórmula/metodologia;
   - periodicidade;
   - geografia;
   - fonte(s) de entrada;
   - limitações.
3. Não comparar automaticamente indicadores que usem conceitos diferentes de estabelecimento, empresa, emprego, receita ou despesa.
4. Recortes municipais e regionais só serão incorporados depois de verificação explícita dos filtros da plataforma.

## Próxima auditoria específica

Transcrever a seção “Fonte dos dados” e produzir uma matriz:

`indicador | fonte_original | produtor | periodicidade | menor_geografia | unidade | transformação_IFEP | uso_SB​​MI`

Depois, testar explicitamente:
- São Borja;
- Fronteira Oeste/região comparável, quando houver;
- Rio Grande do Sul.


## Verificação adicional — rota “Fonte dos dados”

Foi identificada como rota válida da aplicação:

https://observatorio.fecomercio-rs.org.br/page/fonte-dos-dados

A aplicação é client-side e o conteúdo da rota não é exposto no HTML estático recuperável pela ferramenta de auditoria utilizada nesta sessão. Portanto, a existência da página foi confirmada, mas **a lista interna de fontes ainda não foi transcrita automaticamente**.

Fontes confirmadas por material público sobre o lançamento:
- Receita Federal;
- Ministério do Trabalho.

Essas duas confirmações não autorizam presumir que sejam as únicas fontes. A matriz de proveniência continuará pendente até leitura direta do conteúdo dinâmico da rota.

## Evidência de granularidade municipal

Material de imprensa de maio/2026, ao relatar apresentação da plataforma no Vale do Rio Pardo, utilizou indicadores de emprego formal para municípios individuais da região. Isso confirma que **há pelo menos indicadores do Observatório com granularidade municipal**.

Regra: a granularidade será registrada indicador a indicador; não se assumirá que todos os módulos permitem município.


## Auditoria aprofundada — 18/09/2026

### O que foi possível confirmar sem a rota dinâmica de metadados

A página `/page/fonte-dos-dados` continua sendo carregada client-side e não expõe seu conteúdo textual no mecanismo automatizado.

Mesmo assim, três tipos de evidência pública permitiram avançar sem inventar vínculos de fonte:

1. materiais institucionais da própria Fecomércio-RS;
2. cobertura do lançamento, que registra Receita Federal e Ministério do Trabalho como fontes oficiais integradas;
3. reportagem de maio/2026 baseada em demonstração do Observatório, que reproduz variáveis e valores municipais concretos.

### Dimensões institucionais confirmadas

A Fecomércio-RS informa que o Observatório reúne:
- empresas;
- empregos;
- receitas;
- despesas;
- recortes por região;
- recortes por atividade econômica.

Também confirma indicadores próprios do IFEP-RS:
- rotatividade;
- concentração territorial;
- tempo de vida/atividade das empresas.

### Evidência concreta de granularidade municipal

Reportagem da Gazeta do Sul de 07/05/2026 reproduz resultados apresentados pelo Observatório para municípios do Vale do Rio Pardo.

Para Santa Cruz do Sul, a publicação registra que a plataforma permite observar, entre outros:
- participação feminina nos contratos formais;
- composição do emprego por setor;
- tempo médio de contrato;
- opção da empresa empregadora pelo Simples Nacional;
- distribuição por horas semanais;
- estoque/número de empresas;
- participação de optantes do Simples;
- número de MEIs;
- empregos formais;
- criação de vagas no período;
- estoque de contratos;
- rotatividade;
- remuneração média;
- remuneração cruzada com sexo, jornada, ocupação, idade e tempo de atuação.

A mesma evidência traz municípios individuais, portanto a **granularidade municipal está confirmada para parte relevante dos módulos empresariais e trabalhistas**.

### Regra de proveniência reforçada

Embora Receita Federal e Ministério do Trabalho sejam fontes gerais confirmadas da plataforma, a auditoria **não vinculará automaticamente**:

`indicador → Receita Federal`

ou

`indicador → RAIS/Novo Caged`

sem que a seção “Fonte dos dados” ou metadado equivalente confirme essa relação.

Exemplo:
- remuneração com última referência em 2024 é metodologicamente compatível com uma base anual de emprego;
- criação de vagas no primeiro quadrimestre de 2026 é compatível com base conjuntural;
- porém essas compatibilidades são apenas **hipóteses de origem**, não fontes documentadas.

### Indicadores próprios IFEP-RS

Para rotatividade, concentração territorial e tempo de atividade:
- existência: confirmada;
- produtor: IFEP-RS;
- fórmula: pendente;
- periodicidade: pendente;
- fonte(s) de entrada: pendente;
- comparabilidade com indicadores homônimos externos: **não autorizada** até recuperar metodologia.

### Consequência para São Borja

A plataforma possui capacidade comprovada de trabalhar no nível municipal.

Ainda falta testar diretamente São Borja na interface. Até esse teste, a regra será:

> “granularidade municipal confirmada no Observatório; disponibilidade específica do recorte São Borja a validar na interface.”

Não se importarão valores de outro município como proxy de São Borja.

### Artefato estruturado

`docs/data_sources/observatorio_fecomercio_rs_matriz_indicadores_v001.csv`

A matriz separa:
- indicador;
- geografia;
- unidade;
- status da fonte primária;
- transformação IFEP;
- uso no SBMI;
- limitação.

### Fontes públicas utilizadas nesta etapa

- Fecomércio-RS — publicação institucional de lançamento/uso do Observatório;
- Grupo Amanhã — 04/12/2025, cobertura do lançamento, confirmando integração de bases oficiais como Ministério do Trabalho e Receita Federal;
- Gazeta do Sul — 07/05/2026, reprodução de resultados municipais apresentados pelo Observatório;
- Sindilojas Caxias — 27/08/2026, confirmação de uso para empresas, emprego, vendas, setores e regiões.

Nenhuma dessas fontes substitui a página interna “Fonte dos dados” para o vínculo fino indicador→base original.


## Matriz de sobreposição com a base canônica v028 — 18/09/2026

A auditoria comparou os indicadores identificados no Observatório com a planilha técnica v028, **somente em leitura**.

### Já coberto no SBMI

A v028 já possui de forma auditada:
- empresas abertas;
- empresas fechadas;
- empresas ativas;
- saldo mensal;
- proxies de abertura/fechamento/rotatividade empresarial;
- série curta de comparação de turnover-proxy São Borja × RS;
- emprego formal RAIS;
- remuneração média e mediana;
- massa remuneratória;
- jornada contratada;
- perfil por escolaridade;
- perfil por grandes grupos CBO;
- perfil por setor.

Nesses casos, o Observatório não deve substituir a fonte primária já canonizada. Seu uso será:
- validação cruzada;
- interface de consulta;
- eventualmente atualização, desde que conceito/período sejam equivalentes.

### Lacunas com alto valor incremental

Foram identificados como potencialmente novos para a camada atual:
- MEI;
- participação de optantes do Simples Nacional;
- tempo médio de atividade das empresas;
- concentração territorial;
- tempo médio de contrato/vínculo;
- emprego segundo regime Simples do empregador;
- rotatividade do trabalho, se esse for o conceito do indicador IFEP;
- vendas locais/setoriais;
- receitas;
- despesas.

### Lacunas que podem ser recalculáveis com fonte primária

Alguns indicadores exibidos pelo Observatório podem ser produzidos diretamente a partir de microdados já disponíveis no projeto, caso os campos estejam presentes:
- sexo;
- idade;
- tempo de vínculo;
- remuneração por características;
- possivelmente jornada por faixa.

Nesse caso, o procedimento preferido será:
1. usar o Observatório para identificar a pergunta/indicador;
2. verificar a definição;
3. reproduzir pela fonte primária RAIS quando tecnicamente possível;
4. manter o Observatório como referência metodológica/validação, não como substituto.

### Distinção crítica de “rotatividade”

A v028 já possui **rotatividade empresarial proxy** calculada como movimentação de empresas sobre o estoque.

O Observatório apresenta “rotatividade” no contexto de contratos/emprego em material público.

Sem a fórmula do IFEP, é proibido:
- tratar as duas medidas como equivalentes;
- compará-las numericamente;
- somá-las;
- chamar qualquer uma simplesmente de “taxa de rotatividade” sem qualificador.

### Prioridade real de integração

**MUITO ALTA**
- vendas;
- receitas;
- despesas.

**ALTA**
- MEI;
- Simples Nacional;
- tempo de vida empresarial;
- concentração territorial;
- tempo médio de vínculo;
- vínculo trabalhador × regime da empresa;
- rotatividade do trabalho.

**MÉDIA**
- segmentações de sexo/idade/ocupação quando não estiverem consolidadas.

**BAIXA**
- indicadores já diretamente reproduzidos por MEMP/DREI, RFB e RAIS.

Arquivo:
`docs/data_sources/observatorio_fecomercio_rs_gap_v028_v001.csv`

## Retomada da proveniência — 18/09/2026

A rota oficial `/page/fonte-dos-dados` foi revalidada, mas o conteúdo permanece carregado client-side e não é exposto textualmente no mecanismo automatizado utilizado nesta auditoria.

### Evidência institucional adicional

Material institucional recente sobre o Observatório reforça que a plataforma:
- reúne dados e indicadores calculados pelo IFEP-RS sobre atividade empresarial;
- permite analisar informações de diferentes cidades e regiões;
- centraliza dimensões de empresas, empregos, receitas e despesas.

Isso reforça a **capacidade territorial municipal da plataforma**, mas não resolve a proveniência fina por indicador.

### Decisão de auditoria

A matriz `observatorio_fecomercio_rs_matriz_indicadores_v001.csv` permanece com `PENDENTE` na coluna de fonte primária por indicador sempre que a relação não estiver documentada.

Não foram feitas associações automáticas do tipo:
- empregos → RAIS/Novo Caged;
- empresas/MEI/Simples → Receita Federal;
- receitas/despesas → qualquer base específica.

Essas associações continuam metodologicamente plausíveis em alguns casos, mas **não verificadas**.

### Pendência objetiva

Recuperar diretamente da interface:
`indicador | fonte_original | produtor | periodicidade | menor_geografia | unidade | transformação_IFEP`.

Até lá, o Observatório permanece fonte integradora/secundária, e as bases primárias já canônicas no SBMI mantêm precedência.

## Retomada 18/09/2026 — rota primária para MEI/Simples

A auditoria avançou na estratégia de fechar duas lacunas de alto valor — **MEI** e **Simples Nacional** — sem depender da plataforma secundária.

### Evidência oficial

A página de Cadastros da Receita Federal, atualizada em 03/09/2026, confirma:
- existência de **Painel de MEIs**;
- disponibilização do **Cadastro Nacional da Pessoa Jurídica (CNPJ)** em Dados Abertos.

Isso estabelece uma rota primária adequada para reproduzir os indicadores de estrutura empresarial.

### Cross-check secundário localizado

Foi localizado um agregador que declara processar os Dados Abertos CNPJ da Receita Federal, competência **agosto/2026**, e publica para São Borja:
- 7.306 estabelecimentos ativos;
- 3.829 estabelecimentos ativos de empresas optantes do MEI;
- 52,41% dos estabelecimentos ativos vinculados a MEI;
- 102 aberturas no mês;
- 54 baixas no mês.

**Status metodológico:** `SECONDARY_CROSSCHECK_NOT_ACCEPTED`.

Esses valores **não são incorporados como dados oficiais do SBMI**. Servem apenas para:
1. estabelecer uma expectativa de ordem de grandeza;
2. validar posteriormente a reprodução direta;
3. detectar divergências de conceito/competência na extração primária.

Arquivo:
`docs/data_sources/fecomercio_mei_simples_crosscheck_v001.csv`

### Pendência primária

Ainda é necessário obter e processar diretamente a competência correspondente dos Dados Abertos CNPJ/RFB, incluindo o arquivo de opção pelo Simples/MEI.

Até isso ocorrer:
- MEI continua **lacuna em reprodução primária**;
- Simples Nacional continua **lacuna em reprodução primária**;
- nenhum valor secundário será promovido.

### Conciliação com a base RFB já processada no SBMI

O Caderno-Base v028, lido sem alteração, registra **7.306 estabelecimentos ativos** na camada RFB 2026-08.

O cross-check secundário publica exatamente **7.306** para a mesma competência.

Cálculo:
`7.306 - 7.306 = 0`.

**Resultado:** concordância exata no estoque total de estabelecimentos ativos.

Esta conciliação aumenta a confiança de que o agregador está operando sobre a mesma competência geral da base RFB usada pelo SBMI. Contudo, **não valida automaticamente** os valores de MEI, Simples, aberturas ou baixas, porque essas métricas dependem de arquivos/regras adicionais e ainda não foram reproduzidas diretamente.

## Fechamento adicional de lacunas com RAIS 2024

A retomada da matriz de gaps mostrou que dois indicadores anteriormente marcados como lacunas já podem ser respondidos diretamente pela camada primária RAIS 2024, sem depender do Observatório.

### Participação feminina no emprego formal

Universo:
13.125 vínculos ativos válidos em São Borja em 31/12/2024.

Resultados:
- homens: 7.665 vínculos — 58,40%;
- mulheres: 5.460 vínculos — **41,60%**.

Natureza:
DADO CALCULADO sobre MTE/RAIS 2024.

Limitação:
vínculos não equivalem a pessoas únicas.

### Tempo de emprego do vínculo

- média: **61,92 meses**;
- mediana: **28 meses**.

Distribuição analítica SBMI:
- até 12 meses: 30,27%;
- 13–36 meses: 26,86%;
- 37–60 meses: 13,17%;
- 61–120 meses: 13,21%;
- mais de 120 meses: 16,49%.

Natureza:
DADO CALCULADO sobre MTE/RAIS 2024.

Limitação:
o campo representa tempo de emprego do vínculo. A identidade conceitual com eventual indicador “tempo médio de contrato” do IFEP permanece a verificar.

### Remuneração por sexo

Para vínculos com remuneração média nominal positiva:
- homens: média R$ 3.334,00; mediana R$ 2.689,55;
- mulheres: média R$ 2.961,37; mediana R$ 2.241,81.

Diferenças brutas calculadas:
- média: -11,18%;
- mediana: -16,65%.

Essas diferenças são descritivas e **não demonstram discriminação salarial**, pois não controlam ocupação, setor, jornada, escolaridade ou tempo de vínculo.

Fonte estruturada já existente:
`docs/data_sources/rais_2024_perfil_complementar_fecomercio_v001.csv`.

### Decisão

A matriz de gaps foi reclassificada:
- participação feminina: de lacuna para **coberto exploratoriamente por fonte primária**;
- tempo médio de vínculo: de lacuna para **coberto exploratoriamente por fonte primária**;
- remuneração por sexo/idade/ocupação/tempo: permanece parcial, mas remuneração por sexo passa a estar coberta.

Não houve alteração de bases canônicas.
