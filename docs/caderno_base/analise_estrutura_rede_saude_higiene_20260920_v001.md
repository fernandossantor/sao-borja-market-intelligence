# Saúde, higiene e cuidados pessoais — estrutura de rede do inventário documental — v001

**Data:** 20/09/2026  
**Geografia:** São Borja/RS  
**Fonte-base:** planilha documental `Empresas de Varejo de São Borja`  
**Período do inventário:** 2026  
**Status:** apto à promoção como **estrutura do inventário**, não como censo de oferta ativa ou market share.

## 1. Objeto

Recalcular e documentar a estrutura por CNPJ e raiz empresarial do bloco POM de saúde, higiene e cuidados pessoais, com foco no submercado de farmácias/drogarias.

A unidade de análise é o **CNPJ documental único dentro do inventário**. Quando o mesmo CNPJ aparece em mais de uma linha, ele é contado uma única vez nas métricas por raiz.

## 2. Macrobloco saúde/higiene

Inventário:

- 41 linhas;
- 39 linhas com CNPJ extraível;
- 37 CNPJs únicos;
- 24 raízes CNPJ únicas;
- 4 raízes com mais de um CNPJ único no inventário;
- 17 CNPJs únicos pertencentes a essas raízes;
- `17 / 37 × 100 = 45,95%`.

**Dado calculado:** 45,95% dos CNPJs únicos extraíveis do macrobloco pertencem a raízes que possuem mais de uma unidade documental no próprio inventário.

Esse resultado não deve ser generalizado ao macrobloco como “concentração”, porque todas as quatro raízes multiunidade estão no recorte de farmácias/drogarias.

## 3. Farmácias/drogarias

O recorte documental contém:

- 22 linhas do inventário;
- 20 CNPJs únicos;
- 7 raízes CNPJ únicas;
- 4 raízes multiunidade;
- 17 CNPJs únicos em raízes multiunidade;
- `17 / 20 × 100 = 85,00%`;
- maior raiz: 7 CNPJs únicos;
- `7 / 20 × 100 = 35,00%`.

### Raízes multiunidade no inventário

| Raiz CNPJ | Identificação documental | CNPJs únicos | % dos 20 CNPJs únicos |
|---|---|---:|---:|
| 88212113 | São João Farmácias | 7 | 35,00% |
| 93641710 | MB Farmácias | 6 | 30,00% |
| 92665611 | Panvel/Dimed | 2 | 10,00% |
| 94963576 | Farmácia Fronteira | 2 | 10,00% |

As três raízes unitárias no recorte correspondem documentalmente a Farmácia Maria do Carmo, Agafarma e Droga Raia.

## 4. Controle de duplicidades do inventário

Duas linhas repetem CNPJ já presente em outra linha:

- CNPJ `93.641.710/0038-73` — duas linhas MB Farmácias;
- CNPJ `92.665.611/0467-54` — duas linhas Panvel/Dimed.

Por isso:

> 22 linhas de farmácias/drogarias ≠ 22 unidades cadastrais distintas.

As métricas deste artefato utilizam **20 CNPJs únicos**, evitando dupla contagem.

A duplicidade pode refletir erro documental, mudança/endereço distinto associado à mesma inscrição ou outro problema do inventário. Sem evidência complementar, não escolher uma explicação.

## 5. Interpretação

**Interpretação sustentada:** no inventário documental POM, o submercado de farmácias/drogarias apresenta arquitetura empresarial muito mais orientada a grupos multiunidade do que os demais blocos varejistas auditados.

Isso dá suporte estrutural à saliência de redes já observada no estudo POM.

A formulação correta é:

> “17 dos 20 CNPJs únicos de farmácias/drogarias no inventário documental pertencem a quatro raízes com mais de uma unidade mapeada.”

Não escrever:

- “85% do mercado pertence a redes”;
- “quatro redes controlam 85% das vendas”;
- “a concentração de mercado é 85%”.

## 6. Limitações

1. O inventário não é censo municipal.
2. Situação cadastral ativa em 2026-08 não foi revalidada linha a linha neste artefato.
3. Raiz CNPJ não é necessariamente marca, franquia ou grupo econômico em sentido concorrencial.
4. Número de unidades do inventário não é número total de unidades da rede.
5. Não há vendas, faturamento, ticket ou participação monetária.
6. O CNPJ da loja de produtos médicos/ortopédicos não é extraível.
7. O registro de O Boticário permanece sem CNPJ utilizável no inventário e traz anotação de CNPJ baixado em julho/2025; isso não autoriza inferir ausência atual da marca ou da operação.

## 7. Decisão editorial

**PROMOVER AO SUCESSOR DO CADERNO DE SAÚDE/HIGIENE como estrutura do inventário documental.**

Usar principalmente o recorte de farmácias/drogarias.

O macrobloco 45,95% pode ser apresentado apenas com a explicação de que o efeito multiunidade é conduzido pelas farmácias; não deve ser usado como indicador sintético de concentração de saúde/higiene.

## 8. Próxima validação

- cruzar os 20 CNPJs únicos de farmácias/drogarias com a base oficial RFB 2026-08 quando a camada linha a linha estiver novamente acessível;
- revalidar os dois CNPJs duplicados do inventário;
- separar marca percebida, raiz CNPJ e controle territorial;
- somente com vendas/faturamento discutir concentração econômica.

## 9. Artefato estruturado

- `docs/data_sources/saude_higiene_network_roots_20260920_v001.csv`.

## 10. Governança

- Caderno-Base v028 permanece read-only;
- promoção apenas por delta ao sucessor setorial;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
