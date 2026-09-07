# Retenção territorial, vazamento econômico e circulação da renda

**Status:** texto-base atualizado após execução e auditoria do pipeline oficial da Receita Federal, competência 2026-08; ainda não constitui um índice monetário de retenção territorial.  
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

A distinção é fundamental porque **filial não significa necessariamente matriz externa**: uma organização são-borjense pode possuir uma matriz e várias filiais no próprio município. Também é necessário distinguir a expressão geral **vinculação cadastral a matriz externa** de **estrutura empresarial de matriz externa**, pois o universo CNPJ inclui entidades empresariais, organizações sem fins lucrativos, administração pública e outras naturezas jurídicas.

## 4. Evidência oficial: estrutura cadastral predominantemente local, com concentração setorial da vinculação externa

A execução oficial do pipeline com os Dados Abertos CNPJ da Receita Federal, competência 2026-08, identificou **7.306 estabelecimentos com situação cadastral ativa em São Borja**. O resultado foi auditado sem duplicidades, sem identificadores matriz/filial inválidos, sem matrizes de filiais não localizadas e com os 21 arquivos-fonte conferidos por manifesto de integridade.

Do total de estabelecimentos ativos, **6.881 (94,18%) são matrizes localizadas em São Borja**, **102 (1,40%) são filiais cujas matrizes também estão no município** e **323 (4,42%) são filiais vinculadas a matrizes situadas em outros municípios**. Assim, **95,58% dos estabelecimentos ativos pertencem a raízes CNPJ cuja matriz cadastral está em São Borja**.

A leitura muda quando se observa somente o universo das filiais. Dos **425 estabelecimentos classificados oficialmente como filiais**, 323 possuem matriz externa e 102 possuem matriz local. Portanto, **76,0% das filiais estão vinculadas a matrizes de outros municípios**, enquanto 24,0% pertencem a organizações cuja matriz permanece em São Borja. Isso confirma que filial e matriz externa não são sinônimos, embora a vinculação externa seja predominante dentro do subconjunto das filiais.

O cruzamento com a Natureza Jurídica também alterou a interpretação. Dos 7.306 estabelecimentos ativos, **6.906 pertencem ao grande grupo oficial “Entidades Empresariais”**. Nesse subconjunto, **284 estabelecimentos (4,11%) estão vinculados a matrizes externas** e **6.622 (95,89%) a estruturas cuja matriz está em São Borja**. Entre as 284 unidades empresariais de matriz externa, 190 são Sociedades Empresárias Limitadas, 43 Sociedades Anônimas Fechadas e 29 Sociedades Anônimas Abertas. Essas três naturezas somam **262 unidades, ou 92,25% das filiais externas do grupo Entidades Empresariais**.

A análise por divisão CNAE demonstra forte concentração setorial. O comércio — divisões **45, 46 e 47** — reúne **153 das 284 unidades empresariais de matriz externa, ou 53,87%**. O comércio varejista (divisão 47) responde sozinho por **114 unidades**, equivalentes a **40,14%** do total empresarial externo. O comércio por atacado (46) reúne 27 unidades, e comércio e reparação de veículos (45), 12.

Transporte terrestre (49), armazenamento e atividades auxiliares dos transportes (52) e correio e outras atividades de entrega (53) somam **41 unidades empresariais externas, ou 14,44%**. A divisão 64, de atividades de serviços financeiros, contabiliza 11 unidades empresariais externas. Esses resultados indicam que a presença de matrizes externas não se distribui de forma uniforme pela estrutura econômica local.

A análise também identificou um limite conceitual importante. A divisão 94 — Atividades de organizações associativas — possui 26 estabelecimentos de matriz externa no universo geral, mas **nenhum deles pertence ao grupo Entidades Empresariais**: 24 são entidades sem fins lucrativos e 2 pertencem à administração pública. Por isso, essa divisão deve ser tratada como evidência de vinculação institucional externa, e não de controle empresarial externo.

As categorias cadastrais de porte também apresentam incidência desigual de filiais externas: 0,75% na categoria 1, 10,20% na categoria 3 e 30,75% na categoria 5. Como a nomenclatura oficial dessas categorias não foi expandida nesta etapa, o resultado é mantido pelos códigos originais da Receita Federal. A associação entre categoria de porte e peso econômico deve ser interpretada com cautela e não substitui medidas de emprego, faturamento ou valor adicionado.

Esses resultados são **dados calculados pelo projeto a partir dos microdados oficiais da Receita Federal — Dados Abertos CNPJ, competência 2026-08**. Não constituem estatísticas oficiais publicadas pela RFB para São Borja, mas indicadores derivados por pipeline auditado e reproduzível.

## 5. Do controle cadastral ao peso econômico

A localização da matriz é apenas a primeira etapa. Ela identifica onde está formalmente situado o centro cadastral da raiz CNPJ, mas não mede, por si só, o valor que deixa ou permanece no município. A contagem de estabelecimentos atribui peso unitário a organizações de escalas muito diferentes.

A primeira ponderação será feita pelo emprego formal e pela massa salarial. O objetivo é comparar a participação dos estabelecimentos com matriz local e externa no número de vínculos e, quando metodologicamente possível, na remuneração total. Essa etapa é importante porque permite diferenciar **quantidade de estabelecimentos** de **peso econômico aproximado**.

A segunda dimensão é fiscal. No comércio de mercadorias, a análise deve considerar especialmente o ICMS e os mecanismos relacionados ao Valor Adicionado Fiscal (VAF) e à participação municipal nas receitas estaduais, enquanto o ISSQN é particularmente relevante para atividades de serviços. Esses instrumentos possuem bases de incidência e mecanismos de apropriação distintos e não devem ser somados ou atribuídos aos setores sem a devida compatibilização metodológica.

A terceira dimensão é o encadeamento produtivo. Para ela, os dados secundários são mais limitados. Será necessário estimar ou pesquisar a proporção das compras realizadas junto a fornecedores locais, regionais, nacionais ou internacionais. A mesma necessidade se aplica aos serviços corporativos e ao destino do excedente empresarial, dimensões em que empresas privadas raramente divulgam informações territorializadas com o detalhe necessário.

## 6. Hipótese setorial: comércio e vazamento econômico

O comércio desempenha uma função ambivalente no território. Ele organiza a distribuição de bens, gera postos de trabalho, ocupa imóveis, demanda serviços e transforma renda domiciliar em atividade econômica local. Ao mesmo tempo, a análise cadastral mostra que o comércio concentra **mais da metade das unidades empresariais de matriz externa identificadas no município**.

Nos grandes supermercados, atacarejos, redes de farmácias e lojas de eletrodomésticos, é plausível esperar maior centralização de compras, logística, tecnologia, marketing, administração e decisões financeiras. **Essa é uma hipótese estrutural baseada na forma de organização das redes, não uma estimativa monetária para São Borja.** A magnitude do eventual vazamento dependerá da cadeia concreta de cada setor, das margens, da política de compras, do emprego local, da propriedade dos imóveis e dos mecanismos fiscais.

Por isso, o caderno não tratará o faturamento comercial como renda retida e não converterá o percentual de filiais externas em percentual de vazamento. A relação a investigar é mais próxima de:

**valor movimentado localmente → custos intermediários externos + custos locais + remuneração do trabalho + tributos/retornos fiscais + excedente → parcela efetivamente retida no território.**

## 7. O movimento inverso: serviços, indústria e setor público

A hipótese transversal do projeto é que diferentes setores apresentam capacidades distintas de importar, reter e exportar renda. Serviços intensivos em trabalho local podem manter parcela maior de sua receita na forma de remuneração e renda dos proprietários residentes, embora esse padrão não possa ser generalizado para telecomunicações, finanças, plataformas digitais, franquias ou grandes redes de saúde.

A indústria pode atuar como importante mecanismo de retenção quando combina transformação local, emprego e fornecedores do território, mas seu efeito depende da origem dos insumos e do controle do capital. Assim, não se presume automaticamente que toda indústria local apresente alta retenção.

O setor público possui uma característica particularmente relevante para São Borja: parte de seus recursos é financiada por receitas arrecadadas fora do município e convertida em salários, bolsas, contratos e compras que ingressam na economia local. Instituições federais e estaduais, por exemplo, podem funcionar como mecanismos de **injeção territorial de renda externa**. Esse efeito não significa que todo gasto público permaneça em São Borja, pois a renda recebida por servidores e fornecedores também pode vazar por consumo e compras externas; ainda assim, a origem orçamentária dos recursos diferencia estruturalmente esse fluxo do movimento de uma filial comercial que realiza vendas localmente e transfere parte de seus pagamentos para fora.

Essa dimensão será posteriormente relacionada aos módulos de finanças públicas, emprego e renda, educação superior, saúde e presença institucional do Estado.

## 8. Diagnóstico atual

As evidências disponíveis permitem formular um diagnóstico mais preciso, embora ainda não monetário.

Primeiro, **a estrutura cadastral e empresarial de São Borja é numericamente predominantemente local**: 95,58% de todos os estabelecimentos ativos e 95,89% dos estabelecimentos do grupo Entidades Empresariais pertencem a raízes cuja matriz cadastral está em São Borja. Segundo, **a presença de matrizes externas é concentrada**, tanto em formas societárias organizadas — especialmente sociedades limitadas e anônimas — quanto em determinados setores, sobretudo comércio, transporte/logística e atividades financeiras. Terceiro, **a contagem cadastral não representa o peso econômico dessas unidades**, tornando indispensável a ponderação por emprego, massa salarial e outras medidas de escala.

A análise de natureza jurídica também mostra que o conceito de matriz externa precisa ser aplicado de forma diferenciada. No universo geral do CNPJ, a vinculação externa inclui organizações empresariais, entidades associativas e estruturas públicas. Para a análise econômica de retenção e vazamento, o subconjunto de Entidades Empresariais é mais adequado, embora ainda precise ser refinado quando o objetivo exigir separar sociedades privadas, cooperativas, empresas públicas e sociedades de economia mista.

A hipótese mais útil, portanto, não é a de uma economia que simplesmente “perde” riqueza, mas a de uma economia submetida a **fluxos simultâneos de entrada e saída**, cuja composição varia por setor e tipo de organização. O desafio analítico é identificar quais fluxos predominam, em que intensidade e com quais efeitos sobre renda disponível, consumo, reinvestimento e formação de capital local.

## 9. Implicações para os cadernos setoriais

A matriz de retenção territorial será replicada nos quatro cadernos setoriais, preservando a comparabilidade. No comércio de bens essenciais, o foco recairá sobre supermercados, atacarejos e demais formatos alimentares; em saúde, higiene e cuidados pessoais, sobre redes de farmácias e distribuidores; em bens não essenciais, sobre móveis, eletrodomésticos, vestuário e outros formatos; e em serviços e alimentação fora do lar, sobre a intensidade do trabalho, propriedade local, franquias, plataformas e origem dos insumos.

Cada caderno deverá distinguir:

- participação de estruturas com matriz local e de filiais vinculadas a matrizes externas;
- natureza jurídica das organizações, quando relevante para a interpretação;
- emprego e massa salarial associados a cada grupo;
- fornecedores e serviços contratados dentro e fora do município, quando mensuráveis;
- retorno fiscal compatível com a atividade;
- destino do excedente e reinvestimento, quando houver evidência verificável;
- entrada de gasto de consumidores não residentes e saída de gasto dos residentes, quando pertinente.

## 10. Limitações e próximos dados

A análise ainda não permite calcular um **índice monetário de retenção territorial**. Também não permite afirmar quanto do lucro das filiais é remetido para fora, qual a parcela das compras realizada com fornecedores externos ou qual multiplicador local está associado a cada tipo de organização.

A situação cadastral ativa da Receita Federal não comprova, isoladamente, que o estabelecimento esteja operando economicamente na data de referência. Além disso, a localização da matriz formal não demonstra onde ocorrem todas as decisões empresariais, compras, receitas, pagamentos ou reinvestimentos.

Com a classificação oficial matriz/filial, o município da matriz e a natureza jurídica já concluídos, os próximos avanços dependem principalmente de três conjuntos de dados: (1) emprego formal e massa salarial por estabelecimento ou recorte compatível; (2) VAF e demais dados fiscais territorializados e setorialmente compatíveis; e (3) pesquisa primária ou documentação empresarial sobre origem dos fornecedores, serviços contratados, destino do excedente e reinvestimento.

Somente depois dessa integração será avaliada a viabilidade de construir um **Índice de Retenção Territorial do Valor (IRTV)**. Até lá, a análise permanecerá modular, apresentando separadamente os componentes observados, calculados, estimados e hipotéticos.

## Fontes principais desta versão

- Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08, arquivos de Estabelecimentos, Empresas e Municípios utilizados pelo pipeline oficial do projeto.
- CONCLA/IBGE — classificação de Natureza Jurídica e CNAE 2.0, conforme códigos preservados nos microdados da Receita Federal.
- IBGE — PIB dos Municípios e CEMPRE, conforme módulos do Caderno-Base.
- Ministério do Trabalho e Emprego — RAIS, conforme bases incorporadas ao projeto.
- DataSebrae — fotografia empresarial utilizada na Base Territorial.
- Levantamentos POM 2026 dos quatro mercados setoriais de São Borja.
- Verificações cadastrais/corporativas registradas nas versões anteriores do Caderno-Base.

**Nota de método:** as proporções desta versão foram calculadas a partir dos microdados oficiais da Receita Federal — Dados Abertos CNPJ, competência 2026-08, por meio do pipeline auditado do projeto. A execução canônica `cnpj-territorial-control-202608-manual-v002` reproduziu integralmente os 7.306 estabelecimentos da v001, acrescentando apenas a coluna `natureza_juridica`; as 22 colunas comuns, os agregados por CNAE e porte e os manifestos dos 21 arquivos-fonte permaneceram idênticos. Nenhum percentual derivado da antiga heurística de ordem do CNPJ foi reutilizado como resultado definitivo.