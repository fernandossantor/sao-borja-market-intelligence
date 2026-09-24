# Bens não essenciais — taxonomia harmonizada e distribuição exploratória por grupo — 24/09/2026

## 1. Objeto

Harmonizar os rótulos heterogêneos do inventário de BNE e produzir a primeira distribuição exploratória dos **storefronts reconciliados** por grupo mercadológico em São Borja/RS.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only;
- os resultados abaixo são exploratórios e não canônicos.

## 2. Auditoria da base

A tabela `BNE_storefronts_v001` contém 127 registros de controle de storefront: 120 linhas do inventário original e 7 storefronts adicionais reconciliados.

No cenário-base, **122 storefronts** são incluídos. No cenário de sensibilidade conservadora, **121 storefronts** são incluídos, pois 7 Povos Kids é retirado até confirmação cadastral oficial direta.

Os 122 storefronts incluídos apresentavam **47 rótulos textuais distintos** de subcategoria. A heterogeneidade decorre de grafias, níveis diferentes de detalhe e casos multissegmento.

## 3. Método de harmonização

Foi criada uma taxonomia de grupos analíticos primários. A regra é determinística e auditável:

`grupo_harmonizado = mapa(subcategoria_inventario)`

Há uma única sobrescrita explícita por operador:

`se operador = Americanas → DEPARTAMENTOS_MAGAZINES`

Essa exceção foi mantida porque a descrição original da linha não representa adequadamente o papel da operação no recorte BNE, enquanto a reconciliação do lote 19 identificou a unidade corrente como loja de departamentos/magazine.

Casos que cruzam dois grupos sem base suficiente para escolher uma primazia foram classificados como `MISTO_MULTISSEGMENTO`, em vez de forçar uma categoria única.

A Tottal Casa & Lazer, antes pendente, foi classificada como `CASA_UTILIDADES_PRESENTES_DECORACAO` a partir da descrição de primeira parte do Grupo Grazziotin.

## 4. Dados calculados — cenário-base

Fórmula para cada grupo:

`participação_em_unidades (%) = storefronts_do_grupo / 122 × 100`

| Grupo analítico | Storefronts | % das unidades |
| --- | ---: | ---: |
| MODA_CALCADOS_ACESSORIOS | 57 | 46,72% |
| PET_VETERINARIA_AGRO | 20 | 16,39% |
| JOALHERIA_OPTICA_RELOJOARIA | 12 | 9,84% |
| CASA_UTILIDADES_PRESENTES_DECORACAO | 7 | 5,74% |
| ELETRODOMESTICOS_AUDIO_VIDEO | 7 | 5,74% |
| MISTO_MULTISSEGMENTO | 5 | 4,10% |
| LOJA_FRANCA_DUTY_FREE | 3 | 2,46% |
| ARMARINHO_TECIDOS | 2 | 1,64% |
| DEPARTAMENTOS_MAGAZINES | 2 | 1,64% |
| FERRAGENS_MATERIAIS_ELETRICOS | 2 | 1,64% |
| PAPELARIA | 2 | 1,64% |
| ACESSORIOS_DISPOSITIVOS_MOVEIS | 1 | 0,82% |
| ARTIGOS_MILITARES | 1 | 0,82% |
| MOVEIS | 1 | 0,82% |
| **TOTAL** | **122** | **100,00%** |

**Unidade:** storefronts físicos/operacionais e percentual de unidades.  
**Abrangência geográfica:** município de São Borja/RS.  
**Período de referência:** melhor evidência consolidada até 24/09/2026.

## 5. Sensibilidade conservadora

A única diferença entre os dois cenários é 7 Povos Kids, classificada em `MODA_CALCADOS_ACESSORIOS`.

Assim:

- cenário-base: 122 storefronts; `MODA_CALCADOS_ACESSORIOS` = 57;
- sensibilidade conservadora: 121 storefronts; `MODA_CALCADOS_ACESSORIOS` = 56.

Nenhum outro grupo muda em número absoluto.

## 6. Interpretação

### Dado calculado

O grupo `MODA_CALCADOS_ACESSORIOS` reúne 57 das 122 unidades do cenário-base, ou **46,72%** dos storefronts.

### Interpretação

Isso mostra forte presença **em número de pontos comerciais** de moda/calçados/acessórios no inventário reconciliado.

### Limite

Esse percentual **não é market share**, não representa faturamento, área de venda, emprego, estoque ou capacidade competitiva. Uma loja conta como uma unidade independentemente do porte.

O segundo maior grupo em unidades é `PET_VETERINARIA_AGRO`, com 20 storefronts (**16,39%**), seguido de `JOALHERIA_OPTICA_RELOJOARIA`, com 12 (**9,84%**).

Os 5 storefronts classificados como `MISTO_MULTISSEGMENTO` foram preservados como grupo próprio para evitar atribuição arbitrária a um único mercado.

## 7. Limitações

- a taxonomia é uma **classificação analítica calculada**, não nomenclatura oficial da CNAE;
- os rótulos originais continuam preservados linha a linha;
- algumas empresas possuem mix muito mais amplo que seu grupo primário;
- lojas francas permanecem em categoria própria por natureza multissegmento;
- a distribuição mede **unidades físicas/operacionais**, não empresas, raízes de CNPJ ou participação econômica;
- a classificação não autoriza inferir concentração econômica sem consolidar redes/raízes e sem deixar explícita a métrica de unidades.

## 8. Próxima etapa

Consolidar os 122 storefronts por **operador/raiz econômica**, distinguindo:

- unidades independentes;
- redes com múltiplos storefronts;
- múltiplas marcas sob a mesma raiz;
- operações sem CNPJ corrente reconciliado.

Somente depois calcular concentração de rede em **participação de unidades**, nunca como market share de faturamento.

## 9. Artefatos

- `docs/data_sources/bens_nao_essenciais_taxonomia_harmonizada_20260924_v001.csv`
- `docs/data_sources/bens_nao_essenciais_storefronts_reconciliados_20260924_v002.csv`
- `docs/data_sources/bens_nao_essenciais_subcategorias_exploratorias_20260924_v001.csv`
