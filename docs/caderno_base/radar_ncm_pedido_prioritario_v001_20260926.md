# Radar do Mercado — pacote NCM prioritário para solicitação à Receita Estadual — v001

**Data:** 2026-09-26  
**Fonte taxonômica:** Receita Estadual do RS — Radar do Mercado — dimensão pública `d_ncms`  
**Finalidade:** transformar o crosswalk setorial do SBMI em uma lista operacional de NCM8 para o pedido agregado `São Borja × NCM × valor`.  
**Natureza:** TAXONOMIA / ESPECIFICAÇÃO DE PEDIDO. Nenhum valor estadual do Radar é atribuído a São Borja.

## 1. Resultado

O catálogo completo do Radar contém:

- **110 grupos de afinidade**;
- **11.765 associações grupo × NCM8**;
- **0 grupos ausentes** após recomposição;
- **0 NCM8 inválidos** após normalização.

Aplicando o crosswalk dos cadernos e selecionando apenas grupos com prioridade **ALTA**, o pacote operacional contém:

- **43 grupos prioritários**;
- **3.424 NCM8 distintos**;
- **0 NCM8 duplicados entre grupos prioritários**.

Distribuição por setor:

| Setor | NCM8 prioritários |
|---|---:|
| Bens Essenciais | 1.485 |
| Saúde/Higiene/Cuidados Pessoais | 640 |
| Bens Não Essenciais | 1.299 |
| **Total** | **3.424** |

## 2. Distribuição por módulo

| Setor | Módulo | Status | NCM8 |
|---|---|---|---:|
| Bens Essenciais | Alimentação no domicílio | CORE | 1.418 |
| Bens Essenciais | Limpeza doméstica | ADJACENT | 67 |
| Saúde/Higiene/Cuidados Pessoais | Remédios/farmacêuticos | CORE | 394 |
| Saúde/Higiene/Cuidados Pessoais | Higiene, beleza e cosméticos | CORE | 65 |
| Saúde/Higiene/Cuidados Pessoais | Artigos médicos/ortopédicos | EXPANDED | 151 |
| Saúde/Higiene/Cuidados Pessoais | Suplementação | EXPANDED | 30 |
| Bens Não Essenciais | Vestuário | CORE | 304 |
| Bens Não Essenciais | Vestuário e calçados | CORE | 50 |
| Bens Não Essenciais | Móveis e decoração | CORE | 126 |
| Bens Não Essenciais | Eletrodomésticos | CORE | 117 |
| Bens Não Essenciais | Eletrônicos de consumo | EXPANDED | 702 |

## 3. Arquivo operacional

O artifact contém o arquivo:

`radar_ncm_priority_request.csv`

Campos:

- `setor_sbmi`;
- `modulo_sbmi`;
- `status_crosswalk`;
- `relacao_pof`;
- `prioridade`;
- `grupo_afinidade_final`;
- `ncm8`;
- `ncm4`;
- `codxdescr_ncm8`;
- `justificativa`.

Esse CSV é o anexo preferencial quando a Receita Estadual solicitar uma lista fechada de NCMs.

## 4. Regra de interpretação

A lista prioritária não define, por si só, o tamanho monetário dos mercados.

Ela responde apenas:

**quais NCM8 devem ser considerados prioritariamente em uma eventual extração municipal agregada?**

A monetização só ocorre se a Receita fornecer valores observados em células compatíveis, por exemplo:

`competência × município emissor × modelo DFe × NCM8 × valor × quantidade × nº contribuintes × indicador de supressão`.

## 5. Controles setoriais

### Bens Essenciais

Os 1.418 NCM8 CORE correspondem ao perímetro taxonômico de alimentação no domicílio. Os 67 NCM8 de limpeza doméstica são mantidos separados como ADJACENT, pois o benchmark monetário POF canônico atual é restrito à alimentação no domicílio.

### Saúde/Higiene

Os grupos `Medicamentos` e `Produtos Farmacêuticos` aparecem como grupos de afinidade distintos no Radar. No catálogo prioritário não há NCM8 duplicado entre eles. Ainda assim, sua soma monetária futura deverá respeitar a taxonomia efetivamente retornada pela Receita e o perímetro do caderno.

### Bens Não Essenciais

O núcleo CORE cobre vestuário, calçados, móveis/decoração e eletrodomésticos. Eletrônicos de consumo são mantidos como EXPANDED porque integram o escopo POM amplo, mas não os três módulos POF atualmente modelados.

## 6. Alimentação Fora do Lar e Serviços

Nenhum NCM8 é usado como denominador principal desses dois mercados:

- **Alimentação Fora do Lar:** prioridade para CNAE 56 / transação do estabelecimento;
- **Serviços:** prioridade para NFS-e/CFS-e por código de tributação/item de serviço.

NCM pode ser utilizado apenas como camada complementar em operações mistas ou análises de suprimento.

## 7. Rastreabilidade

Workflow:
`.github/workflows/radar-mercado-ncm-taxonomy-complete-v1.yml`

Execução que gerou a lista prioritária:
- run: `36268054427`;
- commit: `4a6e5036fa0f50ce12e503d8ede5eaaee702eae7`;
- artifact: `10913619323`;
- digest: `sha256:0807e87c3f943c3ca99199a6af45ff4b61aef322a21b65064a00e31dd7a5c0e3`.

Google Drive:
- `SBMI_Radar_Mercado_taxonomia_NCM_completa_com_pedido_prioritario_v001.zip`;
- ID: `1dN3e3r0Q-PYaW069dbAm3c7XS9eJLNNj`.

Documento de crosswalk:
`docs/caderno_base/radar_ncm_crosswalk_cadernos_v001_20260926.md`.

## 8. Decisão operacional

Ao solicitar dados à Receita Estadual:

1. preferir a extração integral de NCM8 de São Borja, se viável;
2. se a Receita exigir redução de escopo, anexar o CSV de **3.424 NCM8 prioritários**;
3. solicitar sempre indicador de supressão e número de contribuintes por célula, quando divulgável;
4. não preencher células suprimidas com zero;
5. não usar participação estadual ou regional para preencher lacunas municipais.
