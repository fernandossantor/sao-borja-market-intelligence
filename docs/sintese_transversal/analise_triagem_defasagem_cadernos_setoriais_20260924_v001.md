# Triagem de defasagem dos cadernos setoriais remanescentes — 24/09/2026

## Objeto

Verificar se os três cadernos setoriais ainda em v001 apresentam defasagem material frente aos dados já auditados depois de 10/09/2026, sem abrir novas auditorias amplas.

## Resultado

| Setor | Defasagem de dados | Defasagem editorial | Materialidade | Decisão |
|---|---|---|---|---|
| Bens essenciais | Baixa | Média | Média | harmonização editorial focal; não reabrir auditoria |
| Saúde/higiene | Alta | Alta | Muito alta | criar v002 com estrutura CNES corrente |
| Alimentação fora/serviços | Alta | Baixa | Alta | criar v002 com SINAC/SIMEI por submercado |

## Bens essenciais

O caderno v001 já incorpora o market size potencial modelado de R$ 234.706.228,14/ano para alimentação no domicílio e uma oferta documental explicitamente não censitária: 54 linhas classificadas, 52 documentalmente reconciliadas. O artefato `demanda_potencial_bens_essenciais_v005.md` confirma o benchmark estadual já usado.

A defasagem é principalmente editorial: permanecem seções de pesquisa prioritária/complementar, enquanto a governança atual determina que não haverá pesquisa primária.

**Decisão:** não abrir nova auditoria de oferta; harmonizar a redação em etapa posterior.

## Saúde, higiene e cuidados pessoais

O artefato `analise_farmacias_cnes_corrente_20260922_v001.md` muda materialmente a leitura da oferta de farmácias.

No recorte privado CNES consultado em 22/09/2026:
- 23 registros privados;
- 23 CNPJs únicos;
- 7 raízes CNPJ;
- 4 raízes multiunidade;
- 20 unidades em raízes multiunidade;
- 20/23 = 86,96%;
- maior raiz: MB Farmácias, 8/23 = 34,78%.

Raízes multiunidade:
- MB Farmácias: 8;
- São João: 7;
- Panvel: 3;
- Farmácias Fronteira: 2.

O crosswalk identificou quatro CNPJs privados CNES adicionais frente ao inventário POM anterior e corrigiu a duplicidade Panvel:
- 92.665.611/0467-54 → General Marques, 902;
- 92.665.611/0561-21 → Andradas, 2161.

Agafarma funciona como controle de cobertura: possui sinais operacionais recentes, mas não aparece no recorte CNES consultado.

**Decisão:** criar Caderno Saúde/Higiene v002. Promover a estrutura CNES com universo explicitamente rotulado; preservar 85% como métrica legacy do inventário POM; não chamar 23 de total do mercado; não converter 86,96% em market share.

## Alimentação fora do lar e serviços

O artefato `analise_servicos_sinac_simei_por_submercado_20260920_v001.md` fornece decomposição estrutural nova do mercado de Serviços.

Posição 12/09/2026:
- 947 optantes SINAC;
- 728 optantes SIMEI.

Por submercado:
- salões/barbearias: 385 SINAC / 370 SIMEI;
- oficinas automotivas: 318 / 261;
- clínicas/consultórios — recorte CNAE POM: 106 / 0;
- assistências técnicas/reparos: 100 / 84;
- hotelaria/alojamento: 27 / 6;
- lavanderias: 11 / 7.

Salões + oficinas:
- 703/947 = 74,23% do recorte SINAC;
- 631/728 = 86,68% do recorte SIMEI.

Isso descreve composição formal dos optantes do recorte, não participação econômica, faturamento, pontos físicos ou demanda.

A análise PNAE/B2G 2026 é relevante como circuito institucional separado. Não deve ser somada ao consumo fora do lar das famílias nem misturar contrato e pagamento.

**Decisão:** criar Caderno Alimentação/Serviços v002, priorizando a estrutura por submercado SINAC/SIMEI. Inserir B2G/PNAE apenas como contexto institucional separado.

## Ordem de execução

1. Saúde/Higiene v002;
2. Alimentação/Serviços v002;
3. Bens Essenciais — harmonização editorial focal.

## Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- não abrir nova auditoria ampla por padrão;
- promover apenas evidência já madura e documentada;
- preservar distinção entre unidade cadastral, empresa, ponto físico, gasto e market share.
