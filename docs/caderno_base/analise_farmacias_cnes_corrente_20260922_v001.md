# Farmácias/drogarias — estrutura corrente no CNES × inventário POM — v001

**Data da consulta/crosswalk:** 22/09/2026  
**Geografia:** São Borja/RS  
**Fonte institucional principal:** CNES/DATASUS — estabelecimentos do tipo FARMÁCIA  
**Objeto:** estrutura cadastral privada corrente e comparação com o inventário POM 2026  
**Status:** evidência estrutural madura para promoção com escopo CNES explícito; não é market share nem censo RFB.

## 1. Delimitação

O universo desta análise é o conjunto de registros **privados** recuperados no CNES para o tipo de estabelecimento FARMÁCIA em São Borja na consulta de 22/09/2026.

Foram excluídos do denominador privado quatro registros da rede pública municipal:

- Farmácia Básica do Centro;
- Farmácia Básica do Passo;
- Farmácia Básica Zona Sul;
- Farmácia Especializada.

Agafarma permanece como controle externo ao CNES: há sinais operacionais recentes em 2026, mas ela não aparece no recorte CNES consultado. Portanto, **23 registros CNES privados não devem ser chamados de total do mercado privado municipal**.

## 2. Dados observados no CNES privado

- **23 registros CNES privados**;
- **23 CNPJs únicos**;
- **7 raízes CNPJ**;
- **4 raízes multiunidade**;
- **20 unidades em raízes multiunidade**;
- **3 unidades em raízes que aparecem uma única vez no recorte**.

Raízes multiunidade:

| Raiz CNPJ | Grupo analítico | Unidades CNES | % dos 23 registros privados |
|---|---|---:|---:|
| 93.641.710 | MB Farmácias | 8 | 34,78% |
| 88.212.113 | São João | 7 | 30,43% |
| 92.665.611 | Panvel | 3 | 13,04% |
| 94.963.576 | Farmácias Fronteira | 2 | 8,70% |

## 3. Dados calculados

### Unidades em raízes multiunidade

`20 / 23 × 100 = 86,96%`.

**Dado calculado:** **86,96%** dos registros privados do recorte CNES pertencem a raízes que possuem mais de uma unidade no próprio recorte.

### Maior raiz

`8 / 23 × 100 = 34,78%`.

**Dado calculado:** a maior raiz cadastral no recorte CNES é MB Farmácias, com **8/23 = 34,78%** dos registros.

Esses percentuais descrevem **unidades cadastradas**, não vendas, faturamento, clientes ou market share.

## 4. Comparação com o inventário POM

O inventário POM processado anteriormente possuía:

- 20 CNPJs únicos;
- 7 raízes;
- 17 unidades em raízes multi;
- 85,00% do recorte em raízes multi;
- maior raiz: 7/20 = 35,00%.

A revalidação mostra que esse universo não é uma fotografia corrente completa.

No crosswalk CNES × POM:

- **19 dos 23 CNPJs privados CNES** aparecem no inventário POM;
- **4 CNPJs privados CNES** são adicionais em relação ao universo anterior.

Adicionais CNES:

1. **93.641.710/0044-11 — MB Farmácias**;
2. **93.641.710/0080-85 — MB Farmácias Filial 80**;
3. **92.665.611/0561-21 — Panvel Farmácias**;
4. **15.567.315/0001-92 — Phormula Central**.

## 5. Correção importante: Panvel

O inventário antigo repetia o CNPJ **92.665.611/0467-54** em dois endereços.

O CNES corrente permite resolver a duplicidade:

- 92.665.611/0467-54 → **General Marques, 902**;
- 92.665.611/0561-21 → **Andradas, 2161**.

Portanto, a duplicidade anterior escondia uma unidade/CNPJ Panvel distinto.

## 6. Agafarma como controle de cobertura

O CNPJ **26.710.619/0001-83 — Agafarma São Borja** integra o inventário POM e possui sinais operacionais recentes em 2026, incluindo comunicação de mudança de endereço, mas não foi localizado no recorte CNES consultado.

Consequência metodológica:

> CNES é uma excelente camada institucional de revalidação da estrutura de farmácias, mas não deve ser convertido automaticamente em censo exaustivo da oferta varejista privada.

Não somar mecanicamente “23 CNES + Agafarma” para criar um total de mercado sem regra de universo e reconciliação cadastral adicional.

## 7. Interpretação mercadológica

**Fato observado/calculado:** a arquitetura multiunidade continua muito saliente no recorte institucional corrente. Quatro raízes concentram 20 dos 23 registros privados CNES.

**Interpretação:** a presença estrutural de redes/grupos observada no POM não era mero efeito do inventário antigo; ela reaparece em uma camada institucional corrente e mais completa.

Essa interpretação é sobre **arquitetura cadastral da oferta**. Não permite afirmar:

- concentração de vendas;
- poder de mercado;
- market share;
- preferência dos consumidores;
- intensidade concorrencial efetiva;
- faturamento por rede.

## 8. Relação com a métrica legacy de 85%

A métrica **85,00%** continua documentada como descrição do inventário POM antigo.

Para fotografia cadastral corrente, a referência preferível passa a ser:

- **86,96% dos registros privados CNES em raízes multiunidade**;
- maior raiz: **34,78%**.

Os dois percentuais não são diretamente equivalentes como universos:

- 85%: inventário POM, 20 CNPJs únicos;
- 86,96%: registros privados CNES correntes, 23 CNPJs únicos.

A proximidade numérica não deve ser apresentada como estabilidade estatística sem série temporal comparável.

## 9. Limitações

- CNES é cadastro de estabelecimento de saúde e não situação cadastral oficial da RFB;
- registro corrente não equivale automaticamente a venda/atendimento no dia da consulta;
- Agafarma evidencia possível subcobertura do CNES para o universo varejista pretendido;
- raiz CNPJ não é necessariamente igual à marca percebida ou grupo econômico final;
- não há vendas, faturamento, área de loja, ticket, clientes ou participação de mercado;
- quatro estabelecimentos públicos foram excluídos deliberadamente do denominador privado.

## 10. Artefatos

- `docs/data_sources/farmacias_cnes_pom_crosswalk_20260922_v001.csv`;
- `docs/data_sources/farmacias_revalidacao_batch01_20260922_v001.csv`;
- `docs/data_sources/farmacias_revalidacao_batch02_20260922_v001.csv`;
- `docs/data_sources/farmacias_revalidacao_batch03_20260922_v001.csv`;
- `docs/data_sources/farmacias_revalidacao_batch04_20260922_v001.csv`.

## 11. Status editorial

**PROMOVER AO SUCESSOR DO CADERNO DE SAÚDE/HIGIENE COMO ESTRUTURA CADASTRAL CNES CORRENTE.**

A promoção deve:

- manter o universo CNES explicitamente rotulado;
- substituir a leitura corrente baseada apenas nos 20 CNPJs POM;
- preservar 85% como métrica histórica/legacy do inventário;
- não usar 86,96% como market share.

## 12. Próximo gate

1. validar CNAE/situação RFB quando a camada oficial linha a linha estiver operacional;
2. reconciliar o endereço corrente da Agafarma;
3. acompanhar entradas/saídas futuras no CNES;
4. somente criar indicador de concentração econômica se houver variável econômica adequada.

## 13. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
