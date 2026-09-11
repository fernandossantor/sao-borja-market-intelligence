# Retenção territorial, vazamento econômico e circulação da renda

**Status:** texto-base atualizado após execução e auditoria do pipeline oficial da Receita Federal, competência 2026-08, da ponderação estimada pelo emprego formal e da primeira ponderação remuneratória com RAIS 2025; ainda não constitui um índice monetário de retenção territorial.  
**Abrangência:** município de São Borja/RS, com desdobramentos setoriais posteriores.  
**Objetivo:** interpretar não apenas quanto valor econômico é produzido ou movimentado em São Borja, mas quanto desse valor permanece, recircula ou é transferido para fora do território.

## 1. Por que produção e retenção territorial não são a mesma coisa

Os indicadores tradicionais de atividade econômica — como Produto Interno Bruto (PIB), Valor Adicionado Bruto (VAB), número de estabelecimentos, empregos e faturamento — descrevem dimensões relevantes da economia local, mas não respondem integralmente a uma pergunta central para a inteligência territorial: **quem se apropria do valor gerado ou realizado no município e onde essa renda volta a circular?**

Uma atividade pode ocorrer fisicamente em São Borja e, ao mesmo tempo, manter relações econômicas intensas com outros territórios. Mercadorias podem ser adquiridas de fornecedores externos; serviços administrativos, financeiros, logísticos e tecnológicos podem ser contratados fora do município; e o excedente empresarial pode ser apropriado por proprietários ou matrizes sediadas em outras cidades. No sentido inverso, recursos originados fora de São Borja podem ingressar na economia local por meio de salários públicos, transferências intergovernamentais, aposentadorias, exportações, prestação de serviços a não residentes e outras fontes.

Por essa razão, este caderno distingue quatro conceitos que não devem ser tratados como equivalentes:

- **produção realizada no território**;
- **valor adicionado gerado no território**;
- **renda recebida por agentes que atuam no território**;
- **renda efetivamente apropriada, gasta ou reinvestida por residentes e organizações locais**.

A análise de retenção territorial procura aproximar a quarta dimensão sem substituir as anteriores. Trata-se, portanto, de uma camada complementar ao estudo do PIB e do VAB, e não de uma alternativa a eles.

## 2. Um modelo de fluxos territoriais

A dinâmica econômica de São Borja pode ser representada, de forma simplificada, como um sistema de entradas, circulação interna e saídas. O modelo analítico adotado considera cinco componentes:

1. **entradas externas de recursos**, como salários públicos financiados por orçamentos estadual e federal, transferências governamentais, exportações e gastos de consumidores não residentes;
2. **retenção pela renda do trabalho**, especialmente salários recebidos por trabalhadores residentes;
3. **retenção por encadeamentos locais**, quando empresas compram bens e serviços de fornecedores do próprio município;
4. **retorno fiscal ao território**, respeitando as regras específicas de cada tributo e transferência;
5. **vazamentos**, formados por compras externas de mercadorias e insumos, serviços corporativos contratados fora, despesas financeiras e logísticas externas e apropriação do excedente por controladores não locais.

Esse esquema não atribui valor moral aos fluxos. Uma filial de matriz externa pode gerar empregos, aluguel, demanda de serviços e retorno fiscal local; da mesma forma, uma organização com matriz em São Borja pode adquirir quase todos os seus insumos fora do município. O interesse analítico está em identificar **a intensidade e a composição dos fluxos**, e não em classificar empresas ou setores como positivos ou negativos em função da localização da sede.

## 3. Estrutura empresarial: sede, matriz e filial

A primeira dimensão empiricamente investigada foi a localização da matriz cadastral das organizações que operam em São Borja. O levantamento mercadológico utilizado pelos quatro cadernos setoriais mostrou forte presença de redes empresariais nos segmentos de supermercados, atacarejos, drogarias e comércio de móveis e eletrodomésticos. Essa evidência qualitativa e nominal motivou uma investigação específica sobre matriz e filial.

A etapa inicial (v002) utilizou a ordem numérica do estabelecimento no CNPJ como sinal exploratório. Esse procedimento foi posteriormente corrigido. A Receita Federal mantém um campo cadastral próprio denominado **Identificador Matriz/Filial**, e a ordem do estabelecimento no CNPJ não pode substituí-lo. O caso da Lojas Quero-Quero é demonstrativo: a sede da companhia em Cachoeirinha utiliza CNPJ com ordem diferente de `/0001`. A versão v003 registrou formalmente essa correção metodológica e a v004 implementou um pipeline específico para utilizar o campo oficial da Receita Federal.

A classificação definitiva adotada pelo projeto possui quatro situações principais:

- **MATRIZ_LOCAL:** a matriz oficial está em São Borja;
- **FILIAL_DE_MATRIZ_LOCAL:** a unidade é filial, mas pertence a organização cuja matriz também está em São Borja;
- **FILIAL_DE_MATRIZ_EXTERNA:** a unidade está em São Borja e a matriz oficial encontra-se em outro município;
- **FILIAL_MATRIZ_NAO_LOCALIZADA / INDETERMINADO:** situações que exigem auditoria e não devem ser forçadas para uma das categorias anteriores.

A distinção é fundamental porque **filial não significa necessariamente matriz externa**. Também é necessário distinguir a expressão geral **vinculação cadastral a matriz externa** de **estrutura empresarial de matriz externa**, pois o universo CNPJ inclui entidades empresariais, organizações sem fins lucrativos, administração pública e outras naturezas jurídicas.

## 4. Evidência oficial: estrutura cadastral predominantemente local, com concentração setorial da vinculação externa

A execução oficial do pipeline com os Dados Abertos CNPJ da Receita Federal, competência 2026-08, identificou **7.306 estabelecimentos com situação cadastral ativa em São Borja**. O resultado foi auditado sem duplicidades, sem identificadores matriz/filial inválidos, sem matrizes de filiais não localizadas e com os 21 arquivos-fonte conferidos por manifesto de integridade.

Do total de estabelecimentos ativos, **6.881 (94,18%) são matrizes localizadas em São Borja**, **102 (1,40%) são filiais cujas matrizes também estão no município** e **323 (4,42%) são filiais vinculadas a matrizes situadas em outros municípios**. Assim, **95,58% dos estabelecimentos ativos pertencem a raízes CNPJ cuja matriz cadastral está em São Borja**.

Dos **425 estabelecimentos classificados oficialmente como filiais**, 323 possuem matriz externa e 102 possuem matriz local. Portanto, **76,0% das filiais estão vinculadas a matrizes de outros municípios**, enquanto 24,0% pertencem a organizações cuja matriz permanece em São Borja.

Dos 7.306 estabelecimentos ativos, **6.906 pertencem ao grande grupo oficial “Entidades Empresariais”**. Nesse subconjunto, **284 estabelecimentos (4,11%) estão vinculados a matrizes externas** e **6.622 (95,89%) a estruturas cuja matriz está em São Borja**. Entre as 284 unidades empresariais de matriz externa, 190 são Sociedades Empresárias Limitadas, 43 Sociedades Anônimas Fechadas e 29 Sociedades Anônimas Abertas. Essas três naturezas somam **262 unidades, ou 92,25% das filiais externas do grupo Entidades Empresariais**.

A análise por divisão CNAE demonstra forte concentração setorial. O comércio — divisões **45, 46 e 47** — reúne **153 das 284 unidades empresariais de matriz externa, ou 53,87%**. O comércio varejista (47) responde sozinho por **114 unidades**, equivalentes a **40,14%** do total empresarial externo. Transporte terrestre (49), armazenamento e atividades auxiliares dos transportes (52) e correio e outras atividades de entrega (53) somam **41 unidades empresariais externas, ou 14,44%**. A divisão 64, de atividades de serviços financeiros, contabiliza 11 unidades empresariais externas.

A divisão 94 — Atividades de organizações associativas — possui 26 estabelecimentos de matriz externa no universo geral, mas **nenhum pertence ao grupo Entidades Empresariais**: 24 são entidades sem fins lucrativos e 2 pertencem à administração pública. Essa divisão deve ser tratada como evidência de vinculação institucional externa, e não de controle empresarial externo.

As categorias cadastrais de porte apresentam incidência desigual de filiais externas: 0,75% na categoria 1, 10,20% na categoria 3 e 30,75% na categoria 5. Como a nomenclatura oficial dessas categorias não foi expandida nesta etapa, o resultado é mantido pelos códigos originais da Receita Federal. A associação entre categoria de porte e peso econômico não substitui medidas de emprego, faturamento ou valor adicionado.

Esses resultados são **dados calculados pelo projeto a partir dos microdados oficiais da Receita Federal — Dados Abertos CNPJ, competência 2026-08**. Não constituem estatísticas oficiais publicadas pela RFB para São Borja, mas indicadores derivados por pipeline auditado e reproduzível.

## 5. Do controle cadastral ao peso laboral estimado

A localização da matriz identifica onde está formalmente situado o centro cadastral da raiz CNPJ, mas não mede, por si só, o peso econômico das unidades. A primeira ponderação foi realizada com o emprego formal da **RAIS Estabelecimentos 2025**, restringindo-se a estabelecimentos do tipo CNPJ e ao grande grupo de Natureza Jurídica **Entidades Empresariais**.

Na RAIS Estabelecimentos 2025 foram observados **2.197 registros empresariais do tipo CNPJ em São Borja e 8.595 vínculos ativos**. Esse total não deve ser comparado diretamente aos 6.906 CNPJs empresariais ativos da Receita Federal: são universos administrativos diferentes.

Como a base pública da RAIS não preserva o CNPJ do estabelecimento, não foi possível executar um join empresarial direto. O projeto adotou uma compatibilização hierárquica entre as duas fontes. A chave principal combina **CNAE 2.0 subclasse × Natureza Jurídica detalhada**. Quando essa combinação não existe na RFB 2026, o algoritmo recua, sucessivamente, para subclasse CNAE, classe × natureza, classe e divisão.

A cobertura foi elevada: **8.581 dos 8.595 vínculos, ou 99,84%, encontram correspondência exata em CNAE subclasse × Natureza Jurídica**. Outros 14 vínculos utilizam algum nível de recuo. Para cada célula compatível, os vínculos observados na RAIS são distribuídos entre matriz local, filial de matriz local e filial de matriz externa segundo a participação dos estabelecimentos RFB de cada grupo na mesma célula:

**emprego estimado do grupo na célula = vínculos RAIS da célula × estabelecimentos RFB do grupo na célula / total de estabelecimentos RFB da célula.**

O resultado é uma **estimativa**, não uma contagem observada de trabalhadores de empresas individualmente identificadas. O cenário-base produz aproximadamente **6.080,6 vínculos associados a matrizes locais**, **351,8 a filiais de matriz local** e **2.162,5 a filiais de matriz externa**. Assim, a participação estimada das estruturas empresariais de matriz externa no emprego formal empresarial é de **25,16%**.

Esse resultado contrasta com os **4,11% dos estabelecimentos empresariais** vinculados a matrizes externas. A razão entre os dois pesos é aproximadamente **6,12**. Esse indicador deve ser lido como **sobrerrepresentação do peso laboral estimado em relação ao peso cadastral**, e não como afirmação de que uma filial externa individual empregue 6,12 vezes mais trabalhadores do que uma empresa local.

Usando somente as células com correspondência exata, a participação externa estimada é de **25,08%**, apenas 0,08 ponto percentual abaixo do resultado completo. A análise de sensibilidade mostra 21,31% se o emprego médio das unidades externas nas células mistas for metade do emprego médio das unidades locais e 29,85% se for o dobro. Esses valores são cenários de sensibilidade, não intervalos de confiança estatística.

## 6. Evidência setorial: comércio concentra o peso externo estimado

As divisões **45, 46 e 47** reúnem **3.706 vínculos empresariais observados na RAIS 2025**. O modelo estima aproximadamente **1.315,5 vínculos associados a matrizes externas**, ou **35,50% do emprego empresarial do comércio**. Esse bloco responde por cerca de **60,83% de todo o emprego externo estimado**.

O comércio varejista, divisão 47, possui 2.893 vínculos e aproximadamente **1.083,7 vínculos externos estimados**, correspondentes a **37,46% do emprego empresarial da divisão** e a pouco mais de metade de todo o emprego externo estimado no município. Transporte terrestre (49), comércio atacadista (46), atividades de serviços financeiros (64) e armazenamento e apoio aos transportes (52) aparecem em seguida em contribuição absoluta ao emprego externo estimado.

Há 105 células com contribuição externa positiva; a maior responde por 8,26% do emprego externo estimado, as cinco maiores por 28,77%, as dez maiores por 47,24% e as vinte maiores por 68,80%. Assim, o resultado não depende de uma única combinação excepcional, embora exista concentração setorial relevante.

Nos grandes supermercados, atacarejos, redes de farmácias e lojas de eletrodomésticos, permanece plausível esperar maior centralização de compras, logística, tecnologia, marketing, administração e decisões financeiras. **Essa continua sendo uma hipótese estrutural sobre os fluxos monetários, não uma estimativa de vazamento para São Borja.**

## 7. Do peso laboral ao peso remuneratório estimado

A etapa seguinte utilizou os **microdados públicos RAIS Vínculos 2025 da Região Sul**, filtrados para São Borja. O arquivo municipal preserva as 62 colunas do microdado público. Para compatibilizar o estoque de trabalhadores com a RAIS Estabelecimentos 2025, o universo analítico exige simultaneamente **Ind Vínculo Ativo 31/12 = 1** e **Ind Vínculo Abandonado = 0**, além de estabelecimento tipo CNPJ e Natureza Jurídica pertencente ao grande grupo 2, Entidades Empresariais.

Essa regra foi validada por reconciliação independente. Antes do filtro de vínculo abandonado, a RAIS Vínculos continha 13.674 registros ativos, dos quais 122 estavam marcados como abandonados. Excluindo-os, o total passa exatamente a **13.552 vínculos ativos**, igual à soma de `Qtd Vínculos Ativos` da RAIS Estabelecimentos. A mesma igualdade ocorre no universo CNPJ (**11.847**) e no subconjunto de Entidades Empresariais (**8.595**). No universo empresarial, os 95 vínculos ativos marcados como abandonados possuem remuneração média zero e nenhuma remuneração de dezembro informada.

As 23 linhas exatamente duplicadas do extrato de vínculos não foram removidas. Como a base pública não contém identificador individual do trabalhador, igualdade em todas as variáveis publicadas não comprova duplicidade de pessoa. Além disso, a reconciliação com RAIS Estabelecimentos fecha exatamente quando essas linhas são preservadas.

No universo empresarial reconciliado de **8.595 vínculos**, a RAIS registra **R$ 23.940.059,71** na soma das remunerações nominais de dezembro efetivamente informadas. Há 7.800 vínculos com remuneração de dezembro informada e 795 sem valor; não há zeros reais entre os valores informados. Para `Vl Rem Média Nom`, há informação para os 8.595 vínculos, dos quais 552 possuem valor zero. A **soma das remunerações médias nominais** é **R$ 24.174.457,09**, com média aritmética de **R$ 2.812,62 por vínculo** e mediana de **R$ 2.313,84**.

Essas duas grandezas não são equivalentes a massa salarial anual. A soma de `Vl Rem Dezembro Nom` representa a remuneração de dezembro disponível na base; a soma de `Vl Rem Média Nom` é adotada como **indicador principal de peso remuneratório mensal médio agregado**, por possuir cobertura para todos os 8.595 vínculos. A remuneração de dezembro é mantida como verificação complementar.

A mesma estrutura hierárquica CNAE × Natureza Jurídica usada para o emprego foi aplicada às grandezas remuneratórias. O algoritmo reproduziu integralmente os 8.595 vínculos e reconciliou, sem diferença material, os totais de emprego, remuneração de dezembro e soma da remuneração média. A correspondência exata CNAE subclasse × Natureza Jurídica cobre **99,84% dos vínculos**, **99,79% da remuneração de dezembro** e **99,77% da soma das remunerações médias**.

O resultado estimado mostra uma progressão de peso econômico: as estruturas de matriz externa representam **4,11% dos estabelecimentos empresariais**, **25,16% do emprego empresarial**, **29,09% da soma das remunerações médias nominais** e **29,69% da remuneração de dezembro informada**. Usando apenas as correspondências exatas, os valores são 25,08%, 28,99% e 29,60%, respectivamente, demonstrando que os fallbacks exercem influência mínima sobre o resultado.

A estimativa associa aproximadamente **R$ 7,03 milhões da soma das remunerações médias nominais** às estruturas de matriz externa. A remuneração média implícita nesse grupo é de cerca de **R$ 3.251,91 por vínculo**, contra aproximadamente **R$ 2.664,93** nas estruturas associadas a matrizes locais, diferença estimada de cerca de 22%. Essa diferença **não demonstra que uma empresa externa pague 22% mais do que uma empresa local comparável**. No cenário-base, a remuneração é distribuída proporcionalmente dentro de cada célula; a diferença agregada resulta principalmente da composição setorial e ocupacional das células em que a presença externa é maior.

Setorialmente, o varejo (47) continua liderando a remuneração externa estimada, com cerca de **36,41%** do total de dezembro. Serviços financeiros (64) respondem por aproximadamente 15,01%, transporte terrestre (49) por 11,45% e comércio atacadista (46) por 10,18%. As divisões 45, 46 e 47, somadas, respondem por cerca de **49,33% da remuneração externa estimada de dezembro**, participação menor que os 60,83% observados no emprego externo estimado. Isso sugere que o peso remuneratório externo é mais diversificado setorialmente que o peso laboral.

A maior célula responde por 9,30% da remuneração externa estimada de dezembro; as cinco maiores, por 27,52%; as dez maiores, por 44,90%; e as vinte maiores, por 69,11%. Há concentração, mas o resultado não depende de uma única célula extrema.

## 8. O movimento inverso: serviços, indústria e setor público

A hipótese transversal do projeto é que diferentes setores apresentam capacidades distintas de importar, reter e exportar renda. Serviços intensivos em trabalho local podem manter parcela maior de sua receita na forma de remuneração e renda dos proprietários residentes, embora esse padrão não possa ser generalizado para telecomunicações, finanças, plataformas digitais, franquias ou grandes redes de saúde.

A indústria pode atuar como importante mecanismo de retenção quando combina transformação local, emprego e fornecedores do território, mas seu efeito depende da origem dos insumos e do controle do capital. Assim, não se presume automaticamente que toda indústria local apresente alta retenção.

O setor público possui uma característica particularmente relevante para São Borja: parte de seus recursos é financiada por receitas arrecadadas fora do município e convertida em salários, bolsas, contratos e compras que ingressam na economia local. Instituições federais e estaduais, por exemplo, podem funcionar como mecanismos de **injeção territorial de renda externa**. Esse efeito não significa que todo gasto público permaneça em São Borja.

## 9. Diagnóstico atual

As evidências disponíveis permitem formular um diagnóstico mais preciso, embora ainda não equivalente a um balanço monetário territorial.

Primeiro, **a estrutura cadastral e empresarial de São Borja é numericamente predominantemente local**: 95,58% de todos os estabelecimentos ativos e 95,89% dos estabelecimentos do grupo Entidades Empresariais pertencem a raízes cuja matriz cadastral está em São Borja.

Segundo, **a presença de matrizes externas é concentrada**, tanto em formas societárias organizadas quanto em determinados setores, sobretudo comércio, transporte/logística e atividades financeiras.

Terceiro, a ponderação pelo emprego indica que **o peso laboral estimado das estruturas empresariais de matriz externa é muito superior ao seu peso cadastral**: 4,11% dos estabelecimentos empresariais contra aproximadamente 25,16% do emprego formal empresarial estimado.

Quarto, a ponderação remuneratória amplia essa diferença: as mesmas estruturas são associadas a aproximadamente **29,09% da soma das remunerações médias nominais** e **29,69% da remuneração de dezembro informada**. A evidência indica que a sobrerrepresentação externa não se limita ao número de trabalhadores; ela também aparece na remuneração, em grande medida por composição setorial. Isso continua sendo uma estimativa por células e não uma identificação direta empresa a empresa.

Quinto, a composição é setorialmente desigual. O comércio concentra a maior parcela do emprego externo estimado, mas seu peso relativo diminui quando a análise passa para remuneração, enquanto finanças, transporte, utilidades e serviços especializados ganham importância relativa.

A hipótese mais útil, portanto, não é a de uma economia que simplesmente “perde” riqueza, mas a de uma economia submetida a **fluxos simultâneos de entrada e saída**, cuja composição varia por setor e tipo de organização. Emprego e remuneração gerados por filiais externas constituem renda local do trabalho; localização externa da matriz, por sua vez, sinaliza apenas uma possível dimensão de centralização de decisões e excedentes. Nenhuma das duas dimensões, isoladamente, mede vazamento líquido.

## 10. Implicações para os cadernos setoriais

A matriz de retenção territorial será replicada nos quatro cadernos setoriais, preservando a comparabilidade. Cada caderno deverá distinguir:

- participação de estruturas com matriz local e de filiais vinculadas a matrizes externas;
- natureza jurídica das organizações, quando relevante para a interpretação;
- emprego observado por setor e emprego territorial estimado pelo método RAIS × RFB;
- soma da remuneração média nominal e remuneração de dezembro associadas a cada grupo, com a natureza estimada explicitada;
- fornecedores e serviços contratados dentro e fora do município, quando mensuráveis;
- retorno fiscal compatível com a atividade;
- destino do excedente e reinvestimento, quando houver evidência verificável;
- entrada de gasto de consumidores não residentes e saída de gasto dos residentes, quando pertinente.

## 11. Limitações e próximos dados

A análise ainda não permite calcular um **índice monetário de retenção territorial**. Também não permite afirmar quanto do lucro das filiais é remetido para fora, qual a parcela das compras realizada com fornecedores externos ou qual multiplicador local está associado a cada tipo de organização.

As estimativas de emprego e remuneração possuem duas limitações centrais. A primeira é a ausência de CNPJ identificador na RAIS pública, que obriga a distribuição por células CNAE × Natureza Jurídica em vez de um join estabelecimento a estabelecimento. A segunda é a diferença temporal entre as fontes: a RAIS representa o estoque em 31/12/2025, enquanto a estrutura cadastral RFB utilizada corresponde à competência 2026-08. Mudanças de abertura, encerramento, natureza jurídica ou CNAE entre as duas datas podem alterar a composição das células.

A situação cadastral ativa da Receita Federal não comprova, isoladamente, que o estabelecimento esteja operando economicamente na data de referência. A localização da matriz formal também não demonstra onde ocorrem todas as decisões empresariais, compras, receitas, pagamentos, lucros ou reinvestimentos.

A remuneração de dezembro possui 795 vínculos empresariais sem valor informado e, por isso, não é utilizada como indicador principal. A soma de `Vl Rem Média Nom` possui cobertura integral no universo de 8.595 vínculos, mas 552 registros apresentam valor zero. Essa variável é interpretada como indicador de remuneração média nominal agregada, **não como massa salarial anual**.

Com controle cadastral, emprego e remuneração já integrados, os próximos avanços dependem principalmente de: (1) VAF e demais dados fiscais territorializados e setorialmente compatíveis; (2) pesquisa primária ou documentação empresarial sobre origem dos fornecedores, serviços contratados, destino do excedente e reinvestimento; e (3) medidas de mobilidade do consumo e gasto de não residentes, quando disponíveis.

Somente depois dessa integração será avaliada a viabilidade de construir um **Índice de Retenção Territorial do Valor (IRTV)**. Até lá, a análise permanecerá modular, apresentando separadamente os componentes observados, calculados, estimados e hipotéticos.

## Fontes principais desta versão

- Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08, arquivos de Estabelecimentos, Empresas e Municípios utilizados pelo pipeline oficial do projeto.
- Ministério do Trabalho e Emprego — RAIS Estabelecimentos, ano-base 2025, arquivo público nacional `RAIS_ESTAB_PUB.7z`, filtrado para São Borja no derivado municipal do projeto.
- Ministério do Trabalho e Emprego — RAIS Vínculos, ano-base 2025, arquivo público regional `RAIS_VINC_PUB_SUL.7z`, filtrado em streaming para São Borja no projeto.
- CONCLA/IBGE — classificação de Natureza Jurídica e CNAE 2.0, conforme códigos preservados nos microdados da Receita Federal e da RAIS.
- IBGE — PIB dos Municípios e CEMPRE, conforme módulos do Caderno-Base.
- DataSebrae — fotografia empresarial utilizada na Base Territorial.
- Levantamentos POM 2026 dos quatro mercados setoriais de São Borja.
- Verificações cadastrais/corporativas registradas nas versões anteriores do Caderno-Base.

**Nota de método:** a execução canônica `cnpj-territorial-control-202608-manual-v002` reproduziu integralmente os 7.306 estabelecimentos da v001 e preservou a Natureza Jurídica. O derivado RFB utilizado na ponderação contém 982 células territoriais CNAE × natureza × status. O arquivo bruto `RAIS_ESTAB_PUB.7z` possui SHA-256 `6844c2fbd7b9e74354f616a18180001f5d5e4cc73425128a9008a217a49f4457`; o arquivo bruto regional `RAIS_VINC_PUB_SUL.7z` utilizado na etapa de remuneração possui 704.888.712 bytes e SHA-256 `c537caaaa8318b04e6f4cbbc7e59b130988668b7ea58ce67a0ab2caebf2f5bd0`. A rotina `sbmi.territorial_employment_estimation` registra a ponderação laboral e a rotina `sbmi.territorial_wage_estimation` registra o filtro de vínculos ativos não abandonados, cobertura, fallback, estimativas de emprego e remuneração, reconciliação e manifesto das entradas imediatas. Nenhum percentual estimado deve ser apresentado como observação direta por CNPJ ou como percentual de vazamento monetário.
