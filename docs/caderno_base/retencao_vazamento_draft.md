# Retenção territorial, vazamento econômico e circulação da renda

**Status:** texto-base em construção.  
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

Esse esquema não atribui valor moral aos fluxos. Uma filial externa pode gerar empregos, aluguel, demanda de serviços e retorno fiscal local; da mesma forma, uma empresa com sede em São Borja pode adquirir quase todos os seus insumos fora do município. O interesse analítico está em identificar **a intensidade e a composição dos fluxos**, e não em classificar empresas ou setores como positivos ou negativos em função da localização da sede.

## 3. Estrutura empresarial: sede, matriz e filial

A primeira dimensão empiricamente investigada foi a localização do controle cadastral das empresas que operam em São Borja. O levantamento mercadológico utilizado pelos quatro cadernos setoriais mostrou forte presença de redes empresariais nos segmentos de supermercados, atacarejos, drogarias e comércio de móveis e eletrodomésticos. Essa evidência qualitativa e nominal motivou uma investigação específica sobre matriz e filial.

A etapa inicial (v002) utilizou a ordem numérica do estabelecimento no CNPJ como sinal exploratório. Esse procedimento foi posteriormente corrigido. A Receita Federal mantém um campo cadastral próprio denominado **Identificador Matriz/Filial**, e a ordem do estabelecimento no CNPJ não pode substituí-lo. O caso da Lojas Quero-Quero é demonstrativo: a sede da companhia em Cachoeirinha utiliza CNPJ com ordem diferente de `/0001`. A versão v003 registrou formalmente essa correção metodológica e a v004 implementou um pipeline específico para utilizar o campo oficial da Receita Federal.

A classificação definitiva adotada pelo projeto possui quatro situações principais:

- **MATRIZ_LOCAL:** a matriz oficial está em São Borja;
- **FILIAL_DE_MATRIZ_LOCAL:** a unidade é filial, mas pertence a empresa cuja matriz também está em São Borja;
- **FILIAL_DE_MATRIZ_EXTERNA:** a unidade está em São Borja e a matriz oficial encontra-se em outro município;
- **FILIAL_MATRIZ_NAO_LOCALIZADA / INDETERMINADO:** situações que exigem auditoria e não devem ser forçadas para uma das categorias anteriores.

A distinção é fundamental porque **filial não significa necessariamente controle externo**: uma empresa são-borjense pode possuir uma matriz e várias filiais no próprio município.

## 4. Evidência preliminar: controle externo concentrado em operadores de maior escala

Antes da execução integral da base oficial da Receita Federal, a validação individual das principais redes identificadas pelos levantamentos setoriais confirmou matrizes fora de São Borja para operadores relevantes de supermercados, atacarejos, drogarias e comércio de móveis e eletrodomésticos. Entre as redes verificadas estão, entre outras, Peruzzo, Baklizi, Nicolini, Stok Center, Farmácias São João, Panvel, Droga Raia/RD Saúde, Magazine Luiza, Lojas Quero-Quero, Deltasul, Lojas Colombo, Benoit, Becker e Lebes.

Ao mesmo tempo, uma fotografia cadastral secundária derivada dos dados da Receita Federal indicou que as filiais representam uma parcela minoritária do estoque total de CNPJs ativos do município. As duas evidências não são contraditórias. Pelo contrário, sugerem uma característica estrutural relevante: **o controle empresarial externo parece concentrar-se em determinados operadores e formatos de maior escala, enquanto a maior parte numérica do tecido empresarial é formada por matrizes locais, especialmente pequenos negócios**.

Essa assimetria mostra por que o simples percentual de filiais no total de CNPJs é insuficiente para avaliar dependência externa. Um estabelecimento de uma grande rede e um pequeno negócio individual entram na contagem cadastral com peso unitário, embora possuam capacidades muito distintas de geração de vendas, emprego, área comercial, compras e valor adicionado.

**[ATUALIZAR após a execução oficial da Receita Federal: inserir distribuição municipal por MATRIZ_LOCAL, FILIAL_DE_MATRIZ_LOCAL e FILIAL_DE_MATRIZ_EXTERNA, com cortes por divisão CNAE e porte.]**

## 5. Do controle cadastral ao peso econômico

A localização da matriz é apenas a primeira etapa. Ela identifica onde está formalmente situado o centro empresarial da raiz CNPJ, mas não mede, por si só, o valor que deixa o município. Para avançar da estrutura cadastral para a retenção econômica, o projeto combinará o resultado da Receita Federal com outras bases.

A primeira ponderação será feita pelo emprego formal e pela massa salarial. O objetivo é comparar a participação dos estabelecimentos sob controle local e externo no número de vínculos e, quando metodologicamente possível, na remuneração total. Essa etapa é importante porque permite diferenciar **quantidade de estabelecimentos** de **peso econômico aproximado**.

A segunda dimensão é fiscal. No comércio de mercadorias, a análise deve considerar especialmente o ICMS e os mecanismos relacionados ao Valor Adicionado Fiscal (VAF) e à participação municipal nas receitas estaduais, enquanto o ISSQN é particularmente relevante para atividades de serviços. Esses instrumentos possuem bases de incidência e mecanismos de apropriação distintos e não devem ser somados ou atribuídos aos setores sem a devida compatibilização metodológica.

A terceira dimensão é o encadeamento produtivo. Para ela, os dados secundários são mais limitados. Será necessário estimar ou pesquisar a proporção das compras realizadas junto a fornecedores locais, regionais, nacionais ou internacionais. A mesma necessidade se aplica aos serviços corporativos e ao destino do excedente empresarial, dimensões em que empresas privadas raramente divulgam informações territorializadas com o detalhe necessário.

## 6. Hipótese setorial: comércio e vazamento econômico

O comércio desempenha uma função ambivalente no território. Ele organiza a distribuição de bens, gera postos de trabalho, ocupa imóveis, demanda serviços e transforma renda domiciliar em atividade econômica local. Entretanto, em setores dominados por filiais de redes externas, uma parcela expressiva do valor bruto das vendas corresponde ao custo de mercadorias adquiridas fora do município e a outros pagamentos destinados a agentes externos.

Nos grandes supermercados, atacarejos, redes de farmácias e lojas de eletrodomésticos, é plausível esperar maior centralização de compras, logística, tecnologia, marketing, administração e decisões financeiras. **Essa é uma hipótese estrutural baseada na forma de organização das redes, não uma estimativa monetária para São Borja.** A magnitude desse vazamento dependerá da cadeia concreta de cada setor, das margens, da política de compras, do emprego local, da propriedade dos imóveis e dos mecanismos fiscais.

Por isso, o caderno não tratará o faturamento comercial como renda retida. A relação a investigar é mais próxima de:

**valor movimentado localmente → custos intermediários externos + custos locais + remuneração do trabalho + tributos/retornos fiscais + excedente → parcela efetivamente retida no território.**

## 7. O movimento inverso: serviços, indústria e setor público

A hipótese transversal do projeto é que diferentes setores apresentam capacidades distintas de importar, reter e exportar renda. Serviços intensivos em trabalho local podem manter parcela maior de sua receita na forma de remuneração e renda dos proprietários residentes, embora esse padrão não possa ser generalizado para telecomunicações, finanças, plataformas digitais, franquias ou grandes redes de saúde.

A indústria pode atuar como importante mecanismo de retenção quando combina transformação local, emprego e fornecedores do território, mas seu efeito depende da origem dos insumos e do controle do capital. Assim, não se presume automaticamente que toda indústria local apresente alta retenção.

O setor público possui uma característica particularmente relevante para São Borja: parte de seus recursos é financiada por receitas arrecadadas fora do município e convertida em salários, bolsas, contratos e compras que ingressam na economia local. Instituições federais e estaduais, por exemplo, podem funcionar como mecanismos de **injeção territorial de renda externa**. Esse efeito não significa que todo gasto público permaneça em São Borja, pois a renda recebida por servidores e fornecedores também pode vazar por consumo e compras externas; ainda assim, a origem orçamentária dos recursos diferencia estruturalmente esse fluxo do movimento de uma filial comercial que realiza vendas localmente e transfere parte de seus pagamentos para fora.

Essa dimensão será posteriormente relacionada aos módulos de finanças públicas, emprego e renda, educação superior, saúde e presença institucional do Estado.

## 8. Diagnóstico provisório

As evidências disponíveis permitem formular, até o momento, um diagnóstico provisório composto por três elementos.

Primeiro, São Borja possui um tecido empresarial numericamente dominado por pequenos negócios e matrizes locais, mas segmentos comerciais de maior escala apresentam presença relevante de redes com sede externa. Segundo, a contagem cadastral simples não representa adequadamente o peso econômico dessas redes, sendo necessário ponderar a estrutura de controle por emprego, massa salarial, capacidade operacional e retorno fiscal. Terceiro, o território combina atividades potencialmente geradoras de vazamento com fontes relevantes de ingresso de renda externa, especialmente aquelas associadas ao setor público e às relações econômicas interterritoriais.

A hipótese mais útil, portanto, não é a de uma economia que simplesmente “perde” riqueza, mas a de uma economia submetida a **fluxos simultâneos de entrada e saída**, cuja composição varia por setor. O desafio analítico é identificar quais fluxos predominam, em que intensidade e com quais efeitos sobre renda disponível, consumo, reinvestimento e formação de capital local.

## 9. Implicações para os cadernos setoriais

A matriz de retenção territorial será replicada nos quatro cadernos setoriais, preservando a comparabilidade. No comércio de bens essenciais, o foco recairá sobre supermercados, atacarejos e demais formatos alimentares; em saúde, higiene e cuidados pessoais, sobre redes de farmácias e distribuidores; em bens não essenciais, sobre móveis, eletrodomésticos, vestuário e outros formatos; e em serviços e alimentação fora do lar, sobre a intensidade do trabalho, propriedade local, franquias, plataformas e origem dos insumos.

Cada caderno deverá distinguir:

- participação de empresas locais e filiais de matrizes externas;
- emprego e massa salarial associados a cada grupo;
- fornecedores e serviços contratados dentro e fora do município, quando mensuráveis;
- retorno fiscal compatível com a atividade;
- destino do excedente e reinvestimento, quando houver evidência verificável;
- entrada de gasto de consumidores não residentes e saída de gasto dos residentes, quando pertinente.

## 10. Limitações e próximos dados

A análise ainda não permite calcular um **índice monetário de retenção territorial**. Também não permite afirmar quanto do lucro das filiais é remetido para fora, qual a parcela das compras realizada com fornecedores externos ou qual multiplicador local está associado a cada tipo de empresa.

Os próximos avanços dependem de quatro conjuntos de dados: (1) classificação oficial matriz/filial e município da matriz para os CNPJs ativos de São Borja; (2) emprego e massa salarial por estabelecimento ou recorte compatível; (3) VAF e demais dados fiscais territorializados e setorialmente compatíveis; e (4) pesquisa primária ou documentação empresarial sobre origem dos fornecedores, serviços contratados e reinvestimento.

Somente depois dessa integração será avaliada a viabilidade de construir um **Índice de Retenção Territorial do Valor (IRTV)**. Até lá, a análise permanecerá modular, apresentando separadamente os componentes observados, calculados, estimados e hipotéticos.

## Fontes principais desta versão

- Receita Federal do Brasil — Dados Abertos CNPJ e leiaute cadastral.
- IBGE — PIB dos Municípios e CEMPRE, conforme módulos do Caderno-Base.
- Ministério do Trabalho e Emprego — RAIS, conforme bases incorporadas ao projeto.
- DataSebrae — fotografia empresarial utilizada na Base Territorial.
- Levantamentos POM 2026 dos quatro mercados setoriais de São Borja.
- Verificações cadastrais/corporativas registradas na v003 do Caderno-Base.

**Nota de método:** valores e proporções definitivos da Receita Federal serão inseridos somente após a execução e validação do pipeline oficial. Nenhum percentual provisório derivado de heurística de ordem do CNPJ será reutilizado como estatística oficial.
