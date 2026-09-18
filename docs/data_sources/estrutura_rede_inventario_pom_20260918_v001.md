# Estrutura de rede por raiz CNPJ no inventário POM — 18/09/2026

**Status:** exploratório — não canônico  
**Fonte:** planilha “Empresas de Varejo de São Borja”  
**Unidade:** CNPJ extraível do inventário, deduplicado; raiz = 8 primeiros dígitos do CNPJ.

## 1. Finalidade

A análise procura responder a uma questão mais específica que “quantas empresas existem?”:

**o inventário é composto predominantemente por empresas com uma única unidade local ou por grupos empresariais com múltiplos estabelecimentos em São Borja?**

Essa leitura é especialmente relevante para confrontar os POM com a estrutura competitiva observável.

## 2. Método

1. Extrair CNPJs do texto do inventário.
2. Deduplicar CNPJ completo.
3. Agrupar pelos 8 primeiros dígitos — raiz CNPJ.
4. Contar quantas unidades únicas aparecem por raiz.
5. Definir “raiz multiunidade” apenas quando a mesma raiz possui mais de um CNPJ completo no inventário.

### Controle

A raiz CNPJ identifica uma raiz empresarial, mas:
- não é sinônimo perfeito de marca ou rede;
- franquias podem ter raízes diferentes;
- uma mesma marca pode operar por diferentes empresas;
- a base contém status cadastrais pendentes;
- nenhuma métrica abaixo é market share.

## 3. Bens essenciais

- 47 linhas com CNPJ extraível;
- 46 CNPJs únicos;
- 44 raízes únicas;
- 2 raízes multiunidade;
- 4 das 46 unidades únicas pertencem a raízes multiunidade — **8,70%**;
- maior raiz local: 2 unidades — 4,35%.

### Interpretação

O inventário de essenciais é amplamente pulverizado por raiz empresarial.

Isso não contradiz a presença de grandes redes: uma rede pode possuir apenas uma unidade local e ainda assim ter grande escala funcional.

Por isso a leitura deve ser combinada com o modelo RAIS×RFB, no qual estruturas externas têm peso de emprego muito superior à presença cadastral.

## 4. Saúde, higiene e cuidados — total

- 39 linhas com CNPJ extraível;
- 37 CNPJs únicos;
- 24 raízes únicas;
- 4 raízes multiunidade;
- 17 das 37 unidades únicas estão em raízes multiunidade — **45,95%**;
- maior raiz: 7 unidades — 18,92%.

O valor é muito superior ao observado em essenciais e não essenciais, mas o macrobloco inclui diferentes submercados.

## 5. Farmácia/drogaria — principal achado

Após retirar duplicidades de CNPJ:

- 20 CNPJs únicos;
- apenas 7 raízes CNPJ;
- 4 raízes possuem mais de uma unidade;
- 17 das 20 unidades — **85,00%** — pertencem a raízes multiunidade;
- a maior raiz aparece em 7 das 20 unidades — **35,00%**;
- a distribuição de unidades por raiz é: 7, 6, 2, 2, 1, 1, 1.

### Interpretação

O resultado fornece uma base estrutural para qualificar um achado do POM: a saliência de grandes farmácias não aparece apenas no discurso dos entrevistados. O inventário também mostra **forte presença local de grupos empresariais com múltiplas unidades** no submercado farmácia/drogaria.

Isso **não permite** afirmar:
- concentração de vendas;
- domínio de mercado;
- participação de cada rede;
- superioridade de faturamento.

Mas permite distinguir o submercado farmacêutico de outros varejos mais pulverizados.

## 6. Bens não essenciais

- 104 linhas com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes únicas;
- 4 raízes multiunidade;
- 8 unidades em raízes multiunidade — **7,77%**;
- maior raiz: 2 unidades — 1,94%.

### Interpretação

A estrutura nominal é muito pulverizada.

Isso é coerente com um mercado em que a competição externa pode ocorrer menos por múltiplas unidades locais da mesma empresa e mais por:
- e-commerce;
- redes com uma única unidade local;
- viagens a centros superiores;
- plataformas digitais.

Essa é interpretação apoiada pela triangulação com o POM e REGIC, não inferência causal.

## 7. Implicação transversal

Os mercados apresentam arquiteturas competitivas diferentes:

- essenciais: operadores muito pulverizados por raiz, mas com grandes unidades funcionais de redes;
- farmácias/drogarias: forte presença de raízes multiunidade;
- não essenciais: alta pulverização empresarial e competição externa fortemente mediada por digital/centralidade territorial.

Logo, estratégias de concorrência não devem ser transpostas de um mercado para outro.

Arquivo:
`estrutura_rede_inventario_pom_20260918_v001.csv`.
