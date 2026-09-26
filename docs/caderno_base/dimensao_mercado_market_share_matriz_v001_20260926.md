# Dimensão de mercado e market share — matriz metodológica e de viabilidade v001

**Data:** 2026-09-26  
**Geografia-base:** São Borja/RS  
**Branch:** `feature/cnpj-territorial-control-v1`  
**PR:** #41 — manter OPEN + DRAFT + UNMERGED  
**Base técnica corrente:** Caderno-Base Territorial v029  
**Status:** início da construção metodológica e empírica pós-auditoria de fidelidade dos cinco cadernos.

## 1. Objetivo

Estabelecer uma arquitetura comum para mensurar, sem misturar conceitos, sete dimensões:

1. faturamento empresarial territorial;
2. demanda residente;
3. demanda não residente;
4. mercado capturado;
5. faturamento observado;
6. faturamento estimado;
7. participação de mercado.

A regra central é que **CNPJ, número de lojas, storefronts, vínculos, remuneração, CNES, SINAC/SIMEI ou presença cadastral não são proxies de faturamento nem de market share**.

## 2. Definições operacionais

### 2.1 Faturamento empresarial territorial — FET

Valor de vendas/receitas atribuível às unidades econômicas localizadas em São Borja no período e perímetro setorial definidos.

Pode incluir vendas a residentes, não residentes e, em alguns setores, vendas remotas a clientes externos. Por isso, **FET não é automaticamente igual a mercado capturado local**.

### 2.2 Demanda residente — DR

Despesa dos residentes usuais de São Borja com a categoria, independentemente do território ou canal em que a compra ocorre.

`DR_s = gasto dos residentes com o setor s em São Borja + e-commerce externo + outros municípios + exterior`.

A DR mede a carteira de consumo dos residentes, não o faturamento das empresas locais.

### 2.3 Demanda não residente — DNR

Despesa realizada em São Borja por consumidores/clientes cuja residência usual está fora do município.

Inclui, conforme o setor, visitantes, trabalhadores pendulares, usuários de serviços, consumidores de municípios vizinhos e fluxos fronteiriços. **Fluxo de pessoas não equivale a gasto**.

### 2.4 Mercado capturado — MC

Valor de demanda efetivamente convertido por fornecedores localizados em São Borja, dentro do perímetro de mercado.

Para um mercado B2C territorial:

`MC_s = gasto dos residentes realizado em fornecedores locais + gasto dos não residentes realizado em fornecedores locais`.

Vendas de uma empresa local para clientes de fora do território por canais remotos podem compor FET, mas só entram em MC quando o perímetro de mercado for definido para incluí-las.

### 2.5 Faturamento observado — FO

Valor diretamente registrado por fonte fiscal, transacional ou contábil compatível com:
- setor/produto ou serviço;
- geografia;
- período;
- unidade econômica;
- tratamento de cancelamentos/devoluções;
- base de valor.

Exemplos de fontes potenciais: NFC-e/NF-e, NFS-e/CFS-e, registros de programas públicos, demonstrações contábeis ou dados empresariais voluntariamente fornecidos.

### 2.6 Faturamento estimado — FE

Receita empresarial obtida por modelo e não por observação integral das vendas.

Exemplos defensáveis podem incluir faixas de faturamento empresarial de bases privadas, extrapolação de dados contábeis amostrais ou modelos calibrados por variáveis empresariais monetárias. Toda estimativa deve preservar fórmula, hipótese, faixa de incerteza e teste de sensibilidade.

**Controle conceitual:** POF territorializada e atualizada por preços estima **demanda residente**, não faturamento empresarial. Ela só poderia integrar um modelo de faturamento se existisse uma ponte empiricamente sustentada entre gasto dos residentes e parcela efetivamente capturada pelas empresas locais. Essa ponte ainda não existe no SBMI.

### 2.7 Participação de mercado — PM

`PM_i = V_i / V_mercado × 100`

Só é defensável quando numerador e denominador possuem **o mesmo perímetro setorial, geográfico, temporal, de canal e de conceito monetário**.

Podem existir duas leituras diferentes:
- **share do mercado capturado local**: vendas da empresa dentro do mercado local / MC;
- **share da carteira residente**: vendas da empresa a residentes / DR.

Sem identificação compatível da origem do consumidor, as duas leituras não devem ser confundidas.

## 3. Regra de classificação da evidência

| Grau | Critério |
|---|---|
| ALTA | valor monetário observado em fonte fiscal/transacional/contábil, com escopo setorial, territorial e temporal compatível |
| MÉDIA-ALTA | estimativa baseada em fonte oficial de despesa/consumo, territorialização explícita e atualização de preços tecnicamente compatível |
| MÉDIA | evidência monetária parcial ou modelo com boa base, mas com lacuna de cobertura/classificação/origem do consumidor |
| BAIXA | benchmark indireto, modelo privado, extrapolação territorial forte ou incompatibilidade relevante de escopo |
| NÃO DEFENSÁVEL | contagens estruturais ou qualitativas usadas para inferir faturamento/share sem base monetária |

## 4. Matriz setorial de viabilidade — estado em 2026-09-26

| Setor | Unidade monetária recomendada | Faturamento empresarial local | Demanda residente | Demanda não residente | Mercado capturado | Faturamento observado | Faturamento estimado | Market share | Confiança atual |
|---|---|---|---|---|---|---|---|---|---|
| Bens Essenciais | produto/transação; fronteira canônica = alimentação no domicílio | não observado por setor | **R$ 234.706.228,14/ano** — alimentação no domicílio, POF/RS + população + preços | não monetizada | não observado | DFe municipal amplo disponível, mas ainda sem setor/produto | **não calculado**; DR modelada não é faturamento | não disponível | DR = MÉDIA-ALTA; FET/MC/PM ainda não defensáveis |
| Saúde, Higiene e Cuidados Pessoais | módulos separados: higiene/cuidados, medicamentos e demais submercados | não observado | **Higiene/Cuidados: R$ 57.577.114,03/ano; Remédios: R$ 69.588.767,08/ano; cesta-núcleo = R$ 127.165.881,11/ano** | não monetizada | não observado | potencial via DFe; Farmácia Popular/BNAFAR permanece submercado a auditar | **não calculado**; módulos POF/IPCA são DR | não disponível | DR modular = MÉDIA/MÉDIA-ALTA; PM não defensável |
| Bens Não Essenciais | módulos: vestuário; mobiliários/artigos do lar; eletrodomésticos; demais categorias depois | não observado | **três módulos = R$ 133.358.137,47/ano**: vestuário R$ 73,13 mi; mobiliários R$ 32,82 mi; eletrodomésticos R$ 27,40 mi | não monetizada | não observado | potencial via DFe, preferencialmente item/NCM | **não calculado**; módulos POF/IPCA são DR | não disponível | DR de três módulos = MÉDIA; agregado total ainda não definido |
| Serviços | item de serviço/NFS-e; categorias separadas | não observado | **Serviços pessoais = R$ 18.419.423,64/ano**, somente submercado | não monetizada | não observado | NFS-e/CFS-e municipal é rota prioritária; valores agregados ainda não obtidos | **não calculado** | não disponível | submercado POF = MÉDIA; FO potencial alto via NFS-e |
| Alimentação Fora do Lar | transação de consumo em estabelecimento/delivery | não observado para mercado privado | **R$ 107.390.938,78/ano** — alimentação fora do domicílio, POF/RS + IPCA específico | não monetizada | não observado | DFe municipal amplo disponível sem setor; PNAE é B2G parcial observado | **não calculado**; DR modelada não é faturamento | não disponível | DR = MÉDIA-ALTA; MC/PM privados não defensáveis |

**Nota:** valores de DR são estimativas modeladas a preços aproximados de junho/2026 e não devem ser somados entre setores sem auditoria de sobreposição de categorias.

## 5. O que já existe no projeto

### Bens Essenciais
- POF 2017–2018/RS: R$ 487,00 por família/mês em alimentação no domicílio;
- tamanho familiar: 2,72;
- população 2025: 61.311;
- fator de preços utilizado: 1,781742384675;
- demanda modelada: R$ 234.706.228,14/ano;
- inventário corrente: 54 linhas, 52 CNPJs documentalmente validados; **uso exclusivamente estrutural/documental**.

### Saúde/Higiene
- POM qualitativa n=12;
- estrutura CNES/RFB e diagnóstico de arenas competitivas;
- POF/IPCA: dois módulos de demanda residente modelados;
- Higiene e Cuidados Pessoais: **R$ 57.577.114,03/ano**;
- Remédios: **R$ 69.588.767,08/ano**;
- cesta-núcleo calculada: **R$ 127.165.881,11/ano**;
- faturamento municipal permanece não observado.

### Bens Não Essenciais
- POM qualitativa n=10;
- inventário de storefronts e REGIC temática parcial;
- POF/IPCA: Vestuário **R$ 73.130.722,82/ano**; Mobiliários e artigos do lar **R$ 32.823.271,13/ano**; Eletrodomésticos **R$ 27.404.143,52/ano**;
- três módulos somam **R$ 133.358.137,47/ano**, sem serem tratados como total do setor;
- faturamento local permanece não observado.

### Serviços
- survey POM n=153 como evidência comportamental descritiva;
- SINAC/SIMEI e estrutura cadastral;
- POF/IPCA: **Serviços pessoais = R$ 18.419.423,64/ano**, somente como submercado;
- ausência de valores agregados de NFS-e no projeto.

### Alimentação Fora do Lar
- survey POM n=153 como evidência comportamental descritiva;
- CNAE 56 estrutural;
- POF/IPCA específico: demanda residente modelada **R$ 107.390.938,78/ano**;
- pagamentos PNAE CNPJ observados: R$ 869.843,54, dos quais R$ 327.021,02 a fornecedores locais e R$ 542.822,52 a fornecedores externos;
- contratos de agricultura familiar não são tratados como pagamentos;
- PNAE permanece como submercado institucional B2G e não é somado ao mercado privado sem definição explícita.

## 6. Fontes novas/localizadas e fontes a obter

| Fonte | Estado | Unidade/abrangência | Uso correto | Limite atual |
|---|---|---|---|---|
| Receita Estadual RS — Dados Abertos de Documentos Fiscais Eletrônicos | **LOCALIZADA** | valor e quantidade de DFe; arquivos por município e por CNAE classe; 2018–2026 | envelope monetário formal e investigação de faturamento observado | a descrição pública encontrada disponibiliza município e CNAE em arquivos separados; ainda não foi comprovado um recorte público conjunto `município × setor/produto` |
| Receita Estadual — Preços Dinâmicos | **LOCALIZADA** | NFC-e de vendas formais ao consumidor; preços publicados por COREDE/produto | atualizar preços, price audit e construir deflatores/índices locais-regionais | publicação de preços, não de faturamento municipal; agregação pública em COREDE |
| Menor Preço Nota Gaúcha | **LOCALIZADA** | preços efetivamente praticados por estabelecimentos | price audit/microvalidação | não fornece, por si, volume de vendas ou faturamento agregado |
| Prefeitura de São Borja — NFS-e/CFS-e/ISS Digital | **LOCALIZADA** | notas de serviços emitidas por prestadores locais | faturamento observado agregado por item de serviço/CNAE e período | valores agregados não estão publicamente expostos na página consultada; requer extração/solicitação institucional |
| POF 2017–2018/IBGE — RS | **JÁ USADA / EXPANDIR** | despesa familiar por categorias | DR por setor/submercado | transferência UF→município é modelagem; requer atualização de preços e crosswalk |
| Farmácia Popular / BNAFAR / DBPOPFARMA | **A AUDITAR** | dispensações do programa | submercado observado de medicamentos financiados pelo programa | não representa varejo total; confirmar acesso, valor, período e granularidade municipal/estabelecimento |
| Dados contábeis/POS de empresas | **A OBTER VOLUNTARIAMENTE** | faturamento real por operação/canal | numerador de share e calibração | disponibilidade privada; precisa de padrão comum e anonimização quando agregado |
| Adquirência/cartões/geolocalização de origem | **A OBTER / PRIVADA** | gasto por território e origem do consumidor | separar DR local, vazamento e DNR | custo/acesso e cobertura por meio de pagamento |
| Econodata e equivalentes | **BENCHMARK EXTERNO** | faturamento estimado/faixa empresarial | triangulação e sensibilidade | não é dado fiscal observado; para redes, faturamento consolidado não identifica a filial de São Borja |

## 7. Descoberta empírica prioritária desta etapa

A Receita Estadual passou a disponibilizar dados abertos de **valor e quantidade de documentos fiscais eletrônicos**. A documentação pública informa atualização semanal, tratamento de sigilo por mínimo de quatro contribuintes e arquivos anuais por município e por CNAE classe.

Isso muda a prioridade da investigação: antes de qualquer modelo privado de faturamento, deve ser testado se o painel/arquivos permitem recuperar, direta ou indiretamente, a interseção:

`São Borja × período × modelo NFC-e/NF-e × classe CNAE e, idealmente, produto/NCM`.

Sem essa interseção, o total municipal de DFe é apenas um **envelope monetário agregado**, e o total estadual por CNAE é apenas um **benchmark setorial estadual**. Não é metodologicamente válido multiplicar ou repartir um pelo outro usando número de empresas/lojas.

Para varejos de mix amplo — supermercados, farmácias e lojas de variedades — a classificação por CNAE do emissor também pode misturar categorias. Sempre que possível, a unidade preferível é **item/produto (NCM) + transação + estabelecimento**, e não somente CNAE do estabelecimento.

## 8. Condições mínimas para market share

### Market share observado
Exigir simultaneamente:
- denominador monetário observado do mercado;
- numerador monetário observado da empresa/operação;
- mesmo período;
- mesmo território;
- mesmo perímetro de produto/serviço;
- mesmo tratamento de canais, impostos, devoluções/cancelamentos;
- cobertura conhecida.

### Market share estimado
Só admitir quando:
- numerador e denominador forem estimados com metodologia compatível;
- houver cobertura dos principais operadores;
- redes multiunidade tiverem valor atribuível à operação de São Borja sem rateio por número de lojas;
- o resultado for reportado como intervalo/sensibilidade, e não como ponto de falsa precisão.

**Não admitir**:
- CNPJ/lojas ÷ total de CNPJs/lojas;
- vínculos ÷ vínculos como share de vendas;
- folha/remuneração ÷ folha/remuneração como share de faturamento;
- matriz local/externa como participação de mercado;
- CNES/SINAC/SIMEI como market share;
- REGIC como volume de vendas.

## 9. Estado de execução e próxima prioridade

Concluído nesta rodada:
- DFe Totais Município 2023–2026 ingerido e auditado para São Borja, com NF-e, NFC-e e CT-e separados;
- crosswalk monetário POF → módulos dos cinco cadernos;
- fatores IPCA específicos por módulo, com reprodução de controle do fator alimentar canônico;
- primeira camada de demanda residente modelada para Alimentação Fora do Lar, Saúde/Higiene, três módulos de Bens Não Essenciais e submercado de Serviços pessoais.

Próxima prioridade:
1. testar/solicitar o cruzamento `São Borja × CNAE × modelo DFe × mês × valor`;
2. procurar `São Borja × NCM × modelo DFe × mês × valor` para varejos de mix amplo;
3. preparar especificação de solicitação agregada de NFS-e à Prefeitura: `mês × item LC 116/CNAE × valor bruto × número de notas × município do tomador`, com proteção de sigilo;
4. auditar Farmácia Popular/BNAFAR como submercado observado de medicamentos;
5. somente com faturamento monetário territorial-setorial compatível decidir onde market share pode ser calculado.

## 10. Governança

PR #41 permanece **aberto, draft e sem merge**.  
Nenhuma integração à `main` está autorizada sem aprovação explícita do usuário.


## 11. Artefatos empíricos vinculados

- DFe São Borja: `docs/caderno_base/dfe_sao_borja_envelope_fiscal_v001_20260926.md`.
- POF crosswalk: `docs/caderno_base/pof_rs_crosswalk_dimensao_mercado_v001_20260926.md`.
- Demanda residente modular: `docs/caderno_base/demanda_residente_modulos_setoriais_v001_20260926.md`.
- Planilha técnica Drive: `1tkVQt1N0hrAICehL-w-PRnv3AJGonUYfBhOnFOOvFuI`.
- Documento metodológico Drive: `1ren1_4KuNFUwj2wKMz4GzOpZq8PG4Jr5-YRNyafA_L8`.
