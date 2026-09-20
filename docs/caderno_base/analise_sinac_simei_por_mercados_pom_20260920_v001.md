# SINAC/SIMEI × mercados POM — crosswalk CNAE e recortes setoriais de São Borja — v001

**Data:** 20/09/2026  
**Posição SINAC/SIMEI:** 12/09/2026  
**Geografia:** São Borja/RS  
**Fonte quantitativa:** Receita Federal — Estatísticas do Simples Nacional  
**Fonte de delimitação mercadológica:** quatro POM 2026 do projeto  
**Classificação CNAE:** CNAE/CONCLA-IBGE como referência classificatória  
**Status:** crosswalk analítico conservador, auditável e pronto para alimentar os quatro cadernos setoriais.

## 1. Objetivo

Transformar a decomposição municipal oficial SINAC/SIMEI por CNAE em recortes compatíveis com os mercados efetivamente investigados pelos POM.

O objetivo não é reconstruir toda a economia de São Borja, mas responder:

> quantos optantes SINAC/SIMEI aparecem nas subclasses CNAE que correspondem, de forma documentalmente sustentada, aos mercados dos quatro cadernos?

## 2. Regra metodológica

O crosswalk foi construído em duas etapas:

1. preservar a definição de mercado dos POM;
2. associar apenas CNAEs com correspondência direta ou suficientemente forte.

Cada regra recebe um status:

- `CORE`: entra no total primário;
- `ADJACENT_REVIEW`: relação plausível, mas fora do total primário;
- `ADJACENT_NOT_PRIMARY`: atividade relacionada, porém não comparável diretamente ao núcleo;
- `EXCLUDED`: explicitamente fora do recorte;
- `REVIEW_NOT_PRIMARY`: caso limítrofe ainda não somado.

Isso evita expandir o mercado apenas porque um CNAE está disponível.

## 3. Delimitação documental dos POM

### Bens essenciais

O POM define o setor como comércio varejista de mercadorias de consumo básico, com predominância de alimentos, bebidas e itens de primeira necessidade.

Cita como formatos:
- supermercados e hipermercados;
- atacarejos;
- minimercados de bairro;
- açougues;
- padarias;
- fruteiras.

### Saúde, higiene e cuidados pessoais

O POM delimita o varejo de produtos voltados à prevenção, tratamentos e cuidados com o corpo.

Inclui:
- farmácias;
- drogarias;
- perfumarias;
- cosméticos;
- artigos médicos e ortopédicos;
- óticas, desde que não atuem apenas no ramo estético.

### Bens não essenciais

A introdução do POM explicita:
- moda;
- vestuário;
- calçados;
- móveis;
- eletrodomésticos;
- materiais de construção;
- papelaria;
- mercado pet.

### Serviços

O questionário do POM pede que o respondente considere:
- salões de beleza;
- barbearias;
- clínicas;
- consultórios;
- oficinas;
- lavanderias;
- hotelaria;
- assistências técnicas.

Essa lista foi usada como delimitação operacional conservadora do recorte de serviços.

### Alimentação fora do lar

O questionário explicita:
- restaurantes;
- lanchonetes;
- pizzarias;
- bares;
- cafeterias;
- sorveterias;
- padarias;
- outros estabelecimentos de alimentação fora de casa.

A regra operacional utiliza a Divisão CNAE 56, com discriminação posterior por subsegmento.

## 4. Resultado geral

| Mercado | SINAC | % do SINAC municipal | SIMEI | % do SIMEI municipal | SIMEI/SINAC |
|---|---:|---:|---:|---:|---:|
| Bens essenciais | 688 | 9,59% | 398 | 8,15% | 57,85% |
| Saúde, higiene e cuidados | 95 | 1,32% | 66 | 1,35% | 69,47% |
| Bens não essenciais | 768 | 10,70% | 456 | 9,34% | 59,38% |
| Serviços | 947 | 13,20% | 728 | 14,91% | 76,87% |
| Alimentação fora do lar | 498 | 6,94% | 378 | 7,74% | 75,90% |

Para o caderno editorial combinado **Serviços e Alimentação Fora do Lar**:

- SINAC: `947 + 498 = 1.445`;
- SIMEI: `728 + 378 = 1.106`;
- SIMEI/SINAC: `1.106 / 1.445 × 100 = 76,54%`.

Os cinco recortes primários, somados sem sobreposição entre suas regras, representam:

- **2.996 optantes SINAC = 41,75%** do total municipal;
- **2.026 optantes SIMEI = 41,49%** do total municipal.

Esse percentual é apenas cobertura dos escopos POM selecionados dentro do SINAC/SIMEI, e não participação econômica desses mercados na economia municipal.

## 5. Bens essenciais — composição do recorte

SINAC:

- supermercados/minimercados: **350**;
- padarias/laticínios: **44**;
- açougues/peixarias: **34**;
- bebidas: **187**;
- hortifrúti: **23**;
- conveniência/outros alimentos: **50**.

Total:
`350 + 44 + 34 + 187 + 23 + 50 = 688`.

SIMEI:

- supermercados/minimercados: 176;
- padarias/laticínios: 22;
- açougues/peixarias: 10;
- bebidas: 144;
- hortifrúti: 18;
- conveniência/outros alimentos: 28.

Total: **398**.

### Controle de escopo

Não entram no total primário:
- tabacaria;
- doces/confeitos como categoria específica;
- CNAE atacadista utilizado por possíveis atacarejos.

O POM cita atacarejos, mas não se deve somar automaticamente CNAE atacadista ao recorte varejista sem reconciliação por estabelecimento.

## 6. Saúde, higiene e cuidados pessoais

SINAC:

- farmácias humanas: **7**;
- cosméticos/perfumaria/higiene: **71**;
- artigos médicos/ortopédicos: **7**;
- óticas: **10**.

Total: **95**.

SIMEI:

- farmácias humanas: **0**;
- cosméticos/perfumaria/higiene: **61**;
- artigos médicos/ortopédicos: **4**;
- óticas: **1**.

Total: **66**.

### Interpretação

O recorte mostra que, entre os optantes do Simples capturados pelo crosswalk, cosméticos/perfumaria/higiene possui presença cadastral muito superior ao varejo farmacêutico.

Isso não contradiz o inventário POM de farmácias, porque:
- grandes redes/unidades podem não estar enquadradas no mesmo regime;
- SINAC/SIMEI mede optantes do regime, não universo total de lojas;
- quantidade de optantes não mede faturamento ou participação de mercado.

Medicamentos veterinários foram excluídos do núcleo de saúde/higiene humano e mantidos como adjacência ao mercado pet.

## 7. Bens não essenciais

SINAC:

- materiais de construção: **102**;
- eletrodomésticos/áudio e vídeo: **19**;
- móveis/decoração/artigos domésticos: **108**;
- papelaria: **19**;
- vestuário: **468**;
- calçados: **14**;
- petshop: **38**.

Total: **768**.

SIMEI:

- materiais de construção: 26;
- eletrodomésticos/áudio e vídeo: 14;
- móveis/decoração/artigos domésticos: 64;
- papelaria: 4;
- vestuário: 323;
- calçados: 4;
- petshop: 21.

Total: **456**.

### Principal achado

Vestuário responde por:

`468 / 768 × 100 = 60,94%`

dos optantes SINAC do recorte conservador de bens não essenciais.

No SIMEI:

`323 / 456 × 100 = 70,83%`.

Isso indica forte peso cadastral do vestuário dentro do recorte POM.

Não significa 60,94% ou 70,83% das vendas do mercado.

Informática e telefonia foram mantidas como adjacências de revisão porque o roteiro menciona “eletrônicos”, mas a introdução delimita explicitamente eletrodomésticos.

## 8. Serviços

O recorte primário segue os exemplos efetivamente apresentados ao respondente.

SINAC:

- oficinas automotivas: **318**;
- hotelaria/alojamento: **27**;
- clínicas/consultórios e atividades diretamente associadas: **106**;
- assistências técnicas/reparos: **100**;
- lavanderias: **11**;
- salões de beleza/barbearias: **385**.

Total:
`318 + 27 + 106 + 100 + 11 + 385 = 947`.

SIMEI:

- oficinas automotivas: 261;
- hotelaria/alojamento: 6;
- clínicas/consultórios: 0;
- assistências técnicas/reparos: 84;
- lavanderias: 7;
- salões de beleza/barbearias: 370.

Total: **728**.

### Estrutura

Salões/barbearias e oficinas respondem conjuntamente por:

`(385 + 318) / 947 × 100 = 74,23%`

do SINAC do recorte de serviços.

No SIMEI:

`(370 + 261) / 728 × 100 = 86,68%`.

### Limites

Hospitais, apoio à gestão de saúde e outros serviços pessoais não delimitados no questionário foram mantidos fora do total primário.

A ausência de SIMEI nas clínicas/consultórios reflete as regras e a estrutura da consulta; não significa ausência de pequenos prestadores de saúde.

## 9. Alimentação fora do lar

A Divisão 56 soma:

- **498 optantes SINAC**;
- **378 optantes SIMEI**.

Razão:

`378 / 498 × 100 = 75,90%`.

A divisão contém diferentes modalidades de foodservice. Portanto, o total é adequado ao caderno amplo de alimentação fora do lar, mas análises de restaurantes/lanchonetes/padarias devem voltar às subclasses.

## 10. Diagnóstico transversal

**Dado observado:** a fotografia oficial SINAC/SIMEI permite agora recortar os quatro mercados com uma regra reproduzível.

**Dado calculado:** os recortes POM conservadores abrangem 41,75% dos optantes SINAC e 41,49% dos optantes SIMEI de São Borja.

**Interpretação:** os mercados cobertos pelos POM representam uma parcela cadastral relevante do universo de optantes do Simples, com presença de SIMEI particularmente forte em serviços e alimentação fora do lar.

**Não concluir:**
- que esses percentuais representem PIB ou VAB;
- que representem emprego;
- que representem faturamento;
- que representem participação de mercado;
- que SINAC seja o universo empresarial total;
- que SIMEI/SINAC seja taxa de informalidade ou fragilidade.

## 11. Comparabilidade com outros módulos

### RFB/CNPJ

Usar para:
- universo de estabelecimentos;
- situação cadastral;
- raiz/filiais;
- estrutura empresarial.

### SINAC/SIMEI

Usar para:
- optantes dos regimes;
- composição por CNAE;
- presença relativa de MEI entre optantes do Simples.

### RAIS

Usar para:
- vínculos formais;
- estabelecimentos com emprego;
- remuneração.

As três bases podem ser trianguladas, mas não somadas diretamente.

## 12. Artefatos

- `docs/data_sources/cnae_pom_crosswalk_20260920_v001.csv`;
- `docs/data_sources/sinac_simei_pom_recut_20260920_v001.csv`;
- `docs/data_sources/sinac_simei_pom_market_summary_20260920_v001.csv`;
- `docs/data_sources/sinac_simei_discovery/sao_borja_cnae.csv`.

## 13. Próximo passo

1. registrar os quatro deltas setoriais;
2. integrar o recorte com inventários RFB/POM sem misturar conceitos;
3. avançar para Radar do Mercado como benchmark estadual;
4. depois incorporar Preços Dinâmicos e Cesta Nutricional como benchmarks COREDE/RS;
5. manter a v028 intacta até a consolidação do sucessor.

## 14. Governança

- Caderno-Base v028 permanece **read-only**;
- PR #41 permanece **aberto, draft e sem merge**;
- crosswalk v001 deve ser alterado somente com justificativa documental e nova versão.
