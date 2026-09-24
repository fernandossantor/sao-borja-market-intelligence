# Bens não essenciais — operadores, raízes econômicas e concentração em unidades — 24/09/2026

## 1. Objeto

Consolidar o primeiro cenário exploratório de **122 storefronts** de bens não essenciais em São Borja por operador/raiz econômica e medir a distribuição das unidades físicas entre essas chaves.

A análise usa **participação em número de storefronts**, não faturamento.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- nenhuma métrica desta rodada é promovida automaticamente a indicador canônico.

## 2. Regra de consolidação

Para cada storefront:

1. quando existe CNPJ de referência corrente ou candidato reconciliado e raiz de oito dígitos, a chave de operador é `RAIZ_<raiz>`;
2. quando a identidade jurídica corrente permanece pendente, é usada uma **chave sintética individual** `OPERACAO_<storefront_id>`;
3. uma raiz com vários CNPJs não é convertida automaticamente em várias empresas;
4. uma raiz com vários storefronts é agregada apenas quando o vínculo documental já está reconciliado.

Esta regra impede que Marlin Fashion, Ka Lopes Fitness, Bicho Mimado e Pet House sejam artificialmente associados a outras operações por CNPJ histórico ou identidade não demonstrada.

## 3. Correção Lins Ferrão

A versão v003 preserva o texto original do inventário, mas acrescenta `operador_marca_reconciliado`.

Para a raiz `87.345.021`:

- `87.345.021/0122-14` = **Gang / Lins Ferrão**;
- `87.345.021/0033-04` = **Lojas Pompéia / Lins Ferrão**.

Portanto, são **dois storefronts distintos sob a mesma raiz**, e não uma duplicidade de Pompéia.

## 4. Dados calculados — cenário-base

### 4.1 Operadores/chaves

- storefronts: **122**;
- operator_keys: **109**;
- raízes/chaves com mais de um storefront: **8**;
- chaves com um único storefront: **101**;
- storefronts pertencentes às 8 raízes multiunidade: **21**;
- storefronts pertencentes a chaves de uma única unidade: **101**.

Participação das raízes multiunidade:

`21 / 122 × 100 = 17,21%`.

Assim, **17,21% das unidades** estão em oito raízes multi-storefront e **82,79%** estão em chaves com apenas um storefront.

Isso descreve dispersão de **pontos comerciais**, não de receita.

### 4.2 Raízes multi-storefront

| Raiz / operador | Unidades | % dos 122 storefronts | Padrão |
| --- | ---: | ---: | --- |
| Grupo Grazziotin | 6 | 4,92% | MULTIMARCA_CONFIRMADA |
| Brasil Free Shop Comércio Varejista de Mercadorias Ltda | 3 | 2,46% | MULTIMARCA_CONFIRMADA |
| Lojas Becker Ltda | 2 | 1,64% | MESMA_MARCA |
| Daniela Pitrovski Dornelles / Cia dos Bichos | 2 | 1,64% | MESMA_MARCA_OU_VARIANTE |
| Rogéria Tatiane Machado Loureiro | 2 | 1,64% | MULTIMARCA_CONFIRMADA |
| Lins Ferrão Artigos do Vestuário Ltda | 2 | 1,64% | MULTIMARCA_CONFIRMADA |
| José Altamir Silveira da Rosa Ltda | 2 | 1,64% | MARCA_PENDENTE_EM_UMA_UNIDADE |
| Lojas Quero-Quero S.A. | 2 | 1,64% | MESMA_MARCA |

A maior raiz em número de unidades é o **Grupo Grazziotin**, com 6 storefronts (**4,92%** do total).

A Brasil Free Shop possui 3 storefronts (**2,46%**).

As outras seis raízes multiunidade possuem 2 storefronts cada (**1,64%** por raiz).

As duas maiores raízes, juntas, representam:

`(6 + 3) / 122 × 100 = 7,38%` das unidades.

## 5. HHI de unidades — métrica diagnóstica

Foi calculado um HHI apenas para descrever a dispersão dos storefronts por `operator_key`:

`HHI_unidades = Σ (100 × storefronts_i / storefronts_total)^2`

Resultado:

- cenário-base: **114.22**;
- sensibilidade conservadora: **115.43**.

### Limite crítico

Este **não é um HHI de market share**. Não deve ser comparado mecanicamente com limiares concorrenciais/antitruste, porque a variável é quantidade de unidades físicas, não vendas, receita, capacidade ou participação de mercado.

## 6. Estruturas relevantes

### Grupo Grazziotin — raiz 92.012.467

6 storefronts:

- Franco Giorgi;
- Lojas Grazziotin;
- Tottal Casa & Lazer;
- Por Menos;
- Tech Box;
- Pormenos.

É uma raiz **multimarca e multissegmento**, distribuída entre moda, casa/utilidades e óptica.

### Brasil Free Shop — raiz 32.195.385

3 storefronts no grupo loja franca/duty free:

- Brasil Free Shop /0006-90;
- Monaco Freeshop /0012-39;
- Brasil Free Shop /0011-58.

### Lins Ferrão — raiz 87.345.021

2 storefronts e duas marcas:

- Gang;
- Lojas Pompéia.

### Rogéria Tatiane Machado Loureiro — raiz 10.343.219

2 storefronts:

- Lolita Lingerie;
- Volúpia Moda Íntima.

### José Altamir Silveira da Rosa Ltda — raiz 93.202.695

2 storefronts:

- Requinte Modas;
- unidade Presidente Vargas com marca de fachada ainda pendente.

### Quero-Quero — raiz 96.418.264

2 storefronts reconciliados:

- Coronel Aparício Mariense;
- General Marques.

### Lojas Becker — raiz 04.415.928

2 storefronts da mesma marca.

### Cia dos Bichos — raiz 07.195.827

2 storefronts sob a mesma operação/variante de marca.

## 7. Interpretação mercadológica

### Dado observado/calculado

A estrutura em unidades é numericamente pulverizada: 109 chaves de operador para 122 storefronts, com apenas oito raízes apresentando mais de uma unidade.

### Interpretação

Isso indica que a oferta física documentada é composta majoritariamente por operações de um único ponto, ao lado de poucas redes/raízes multiunidade.

### Limite

Não é possível concluir, a partir disso, que o mercado seja economicamente desconcentrado. Uma rede com poucas unidades pode ter faturamento, área de loja, estoque, marca ou tráfego muito superiores aos de operadores independentes.

## 8. Sensibilidade

O cenário conservador retira apenas 7 Povos Kids:

- storefronts: 121;
- operator_keys: 108;
- raízes multiunidade: 8;
- HHI de unidades: 115.43.

A estrutura das oito raízes multiunidade não muda.

## 9. Próxima etapa

A próxima análise deve combinar a taxonomia mercadológica com a estrutura de operador, produzindo para cada grupo:

- número de storefronts;
- número de operator_keys;
- número e peso das raízes multiunidade;
- maior raiz em unidades;
- presença de multimarca/multissegmento.

Depois, cruzar essa estrutura com evidências de demanda e comportamento já existentes no caderno setorial, sem converter participação em unidades em market share.

## 10. Artefatos

- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v003.csv`
- `docs/data_sources/bens_nao_essenciais_operadores_raizes_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_concentracao_unidades_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_raizes_multiunidade_20260924_v001.csv`
