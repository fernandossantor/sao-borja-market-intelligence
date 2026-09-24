# Bens não essenciais — estrutura de operadores por grupo mercadológico — 24/09/2026

## 1. Objeto

Cruzar a taxonomia harmonizada dos **122 storefronts** com a consolidação por `operator_key`, para distinguir dispersão de pontos comerciais de presença de redes/raízes multiunidade dentro de cada grupo.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- unidade de análise: storefront;
- concentração: apenas em **unidades**, nunca em faturamento.

## 2. Método

Para cada grupo analítico:

- `storefronts` = número de unidades no cenário-base;
- `operator_keys` = raízes reconciliadas + chaves sintéticas individuais;
- `raizes_multiunidade_no_grupo` = operator_keys com mais de um storefront dentro do próprio grupo;
- `share_storefronts_em_raizes_multiunidade` = unidades desses operator_keys / storefronts do grupo;
- `maior_operator_key_share` = maior número de unidades de uma chave / storefronts do grupo.

O cálculo mede estrutura física documentada. Não mede receita, vendas, área de loja ou market share.

## 3. Resultado

| Grupo | Storefronts | Operator keys | Raízes multiunidade no grupo | Unidades nessas raízes | % das unidades do grupo | Maior chave (unidades) | % da maior chave |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| MODA_CALCADOS_ACESSORIOS | 57 | 51 | 4 | 10 | 17,54% | 4 | 7,02% |
| PET_VETERINARIA_AGRO | 20 | 19 | 1 | 2 | 10,00% | 2 | 10,00% |
| JOALHERIA_OPTICA_RELOJOARIA | 12 | 12 | 0 | 0 | 0,00% | 1 | 8,33% |
| CASA_UTILIDADES_PRESENTES_DECORACAO | 7 | 7 | 0 | 0 | 0,00% | 1 | 14,29% |
| ELETRODOMESTICOS_AUDIO_VIDEO | 7 | 5 | 2 | 4 | 57,14% | 2 | 28,57% |
| MISTO_MULTISSEGMENTO | 5 | 5 | 0 | 0 | 0,00% | 1 | 20,00% |
| LOJA_FRANCA_DUTY_FREE | 3 | 1 | 1 | 3 | 100,00% | 3 | 100,00% |
| ARMARINHO_TECIDOS | 2 | 2 | 0 | 0 | 0,00% | 1 | 50,00% |
| DEPARTAMENTOS_MAGAZINES | 2 | 2 | 0 | 0 | 0,00% | 1 | 50,00% |
| FERRAGENS_MATERIAIS_ELETRICOS | 2 | 2 | 0 | 0 | 0,00% | 1 | 50,00% |
| PAPELARIA | 2 | 2 | 0 | 0 | 0,00% | 1 | 50,00% |
| ACESSORIOS_DISPOSITIVOS_MOVEIS | 1 | 1 | 0 | 0 | 0,00% | 1 | 100,00% |
| ARTIGOS_MILITARES | 1 | 1 | 0 | 0 | 0,00% | 1 | 100,00% |
| MOVEIS | 1 | 1 | 0 | 0 | 0,00% | 1 | 100,00% |

## 4. Leituras principais

### Moda, calçados e acessórios

- 57 storefronts;
- 51 operator_keys;
- 4 raízes com mais de uma unidade dentro do grupo;
- 10 storefronts pertencem a essas quatro raízes;
- participação dessas raízes em número de pontos do grupo: **17,54%**;
- a maior raiz dentro do grupo é o Grupo Grazziotin, com 4 unidades de moda, equivalentes a **7,02%** dos storefronts do grupo.

A estrutura continua majoritariamente formada por chaves de um único ponto, embora existam redes e grupos multimarca.

### Pet, veterinária e agro

- 20 storefronts;
- 19 operator_keys;
- uma raiz multiunidade no grupo, com 2 unidades;
- participação dessa raiz em número de pontos: **10,00%**.

### Eletrodomésticos, áudio e vídeo

- 7 storefronts;
- 5 operator_keys;
- duas raízes possuem 2 unidades cada;
- 4 dos 7 pontos pertencem a raízes multiunidade, ou **57,14%**.

Esse percentual é estruturalmente relevante em unidades, mas o número absoluto do grupo é pequeno e não permite inferir liderança econômica.

### Lojas francas / duty free

- 3 storefronts;
- 1 operator_key;
- as três unidades pertencem à mesma raiz Brasil Free Shop.

Logo, a concentração em **unidades jurídicas/operacionais** é de 100% numa única raiz dentro deste recorte. Isso não deve ser generalizado para o mercado fronteiriço como um todo nem interpretado como market share de vendas.

### Demais grupos

Nos demais grupos, não há mais de uma unidade do mesmo operator_key dentro do próprio grupo, embora uma raiz possa aparecer em grupos diferentes. O principal exemplo é o Grupo Grazziotin, que participa simultaneamente de moda, casa/utilidades e óptica.

## 5. Sensibilidade

A retirada conservadora de 7 Povos Kids afeta apenas `MODA_CALCADOS_ACESSORIOS`:

- storefronts: 57 → 56;
- operator_keys: 51 → 50.

As raízes multiunidade e seus números de unidades não mudam.

## 6. Implicação mercadológica

A oferta física não apresenta uma única arquitetura competitiva.

- Moda combina muitos operadores de um ponto com algumas raízes multimarca.
- Eletrodomésticos possui presença proporcionalmente maior de redes multiunidade.
- Duty free, neste inventário reconciliado, está concentrado em uma única raiz com três pontos.
- Pet/veterinária/agro é predominantemente pulverizado em unidades.

Essas diferenças justificam evitar uma única medida agregada de “concorrência” para todo o mercado BNE.

## 7. Limitações

- a unidade é storefront, não vendas;
- operator_key pode usar CNPJ candidato ou chave sintética quando a identidade jurídica corrente ainda não está fechada;
- grupos pequenos produzem percentuais elevados com poucos pontos;
- multissegmento permanece em grupo próprio para evitar dupla contagem;
- não inferir causalidade, desempenho ou poder de mercado a partir da contagem de unidades.

## 8. Próxima etapa

Integrar esta estrutura de oferta com os dados de **demanda e comportamento de consumo** já existentes no caderno setorial de bens não essenciais, separando:

- evidência observada de consumidores;
- estrutura de oferta calculada nesta auditoria;
- interpretação mercadológica;
- lacunas que não podem ser resolvidas sem nova coleta.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_estrutura_operadores_por_grupo_20260924_v001.csv`
