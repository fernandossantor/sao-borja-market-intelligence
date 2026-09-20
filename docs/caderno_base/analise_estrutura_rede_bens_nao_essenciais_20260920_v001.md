# Bens não essenciais — estrutura de rede do inventário documental — v001

**Data:** 20/09/2026  
**Geografia:** São Borja/RS  
**Fonte-base:** planilha documental `Empresas de Varejo de São Borja`  
**Período do inventário:** 2026  
**Status:** apto à promoção como **estrutura do subconjunto documental**, não como censo de oferta ativa ou market share.

## 1. Objeto

Recalcular a estrutura por CNPJ e raiz empresarial do inventário POM de bens não essenciais, controlando linhas sem CNPJ e duplicidades antes de interpretar pulverização ou multiunidade.

## 2. Cobertura documental do inventário

O bloco contém:

- 120 linhas;
- 104 linhas com CNPJ extraível;
- 16 linhas sem CNPJ extraível;
- `104 / 120 × 100 = 86,67%` das linhas com CNPJ extraível;
- 103 CNPJs únicos.

Uma duplicidade de CNPJ foi identificada:

- CNPJ `96.418.264/0357-81` — Lojas Quero-Quero — aparece em duas linhas do inventário.

Logo:

> 104 linhas com CNPJ ≠ 104 unidades cadastrais distintas.

As métricas por raiz utilizam **103 CNPJs únicos**.

## 3. Estrutura por raiz CNPJ

No subconjunto com CNPJ único:

- 103 CNPJs únicos;
- 99 raízes CNPJ únicas;
- 4 raízes com dois CNPJs únicos cada;
- 8 CNPJs únicos pertencentes a raízes multiunidade;
- `8 / 103 × 100 = 7,77%`;
- maior raiz no recorte: 2 CNPJs;
- `2 / 103 × 100 = 1,94%`.

### Raízes multiunidade no inventário

| Raiz CNPJ | Identificação documental | CNPJs únicos |
|---|---|---:|
| 10343219 | Lolita Lingerie / Volúpia Moda Íntima | 2 |
| 92012467 | Franco Giorgi / Lojas Grazziotin | 2 |
| 04415928 | Lojas Becker | 2 |
| 07195827 | Companhia dos Bichos / Cia dos Bichos (Aquarium) | 2 |

## 4. Interpretação

**Interpretação sustentada:** entre os 103 CNPJs únicos documentados no inventário de bens não essenciais, a estrutura por raiz é fortemente pulverizada.

A formulação defensável é:

> “99 raízes CNPJ estão representadas entre 103 CNPJs únicos documentados; apenas 8 CNPJs pertencem a raízes com mais de uma unidade mapeada no próprio recorte.”

Isso é compatível com um mercado local nominalmente atomizado por raiz empresarial, mas não exclui competição de grandes redes, franquias, marcas, marketplaces ou e-commerce.

## 5. O que a raiz CNPJ não captura

A pulverização por raiz não mede:

- concentração de faturamento;
- poder de marca;
- franquias que operam sob raízes distintas;
- grupos econômicos com diferentes raízes;
- marketplaces;
- e-commerce sem estabelecimento local;
- compras em centros regionais;
- participação de vendas das redes que possuem uma única unidade local.

Portanto, a estrutura cadastral local pode ser pulverizada ao mesmo tempo em que a pressão competitiva percebida pelo consumidor é concentrada em canais ou marcas de escala superior.

## 6. Limitações

1. 16/120 linhas não possuem CNPJ extraível.
2. A situação cadastral ativa não foi revalidada linha a linha contra a RFB 2026-08 neste artefato.
3. Ao menos uma duplicidade documental de CNPJ permanece no inventário.
4. Há registros com notas históricas de baixa cadastral em outras auditorias do bloco.
5. CNPJ/raiz não equivale a estabelecimento efetivamente operante, marca, rede comercial ou grupo econômico.
6. Não há faturamento, vendas, ticket ou market share.

## 7. Decisão editorial

**PROMOVER AO SUCESSOR DO CADERNO DE BENS NÃO ESSENCIAIS como estrutura do subconjunto documental.**

Sempre apresentar o denominador:

- 120 linhas totais;
- 104 com CNPJ extraível;
- 103 CNPJs únicos;
- 99 raízes.

Não usar “7,77% multiunidade” sem informar que o denominador são os 103 CNPJs únicos documentados.

## 8. Próxima validação

- revalidar situação cadastral RFB 2026-08 dos 103 CNPJs únicos;
- resolver/explicar a duplicidade da Lojas Quero-Quero;
- recuperar CNPJ das 16 linhas faltantes apenas quando houver evidência documental suficientemente confiável;
- cruzar estrutura local com presença digital e Radar estadual sem converter nenhum deles em market share.

## 9. Artefato estruturado

- `docs/data_sources/bens_nao_essenciais_network_roots_20260920_v001.csv`.

## 10. Governança

- Caderno-Base v028 permanece read-only;
- promoção apenas por delta ao sucessor setorial;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
