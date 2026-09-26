# Checkpoint — início da dimensão de mercado e market share — 2026-09-26

## Governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`
- Branch: `feature/cnpj-territorial-control-v1`
- PR #41: **OPEN + DRAFT + UNMERGED**
- Base técnica corrente: Caderno-Base Territorial v029
- Auditoria de fidelidade dos cinco cadernos: encerrada
- Merge sem autorização explícita: proibido

## Entrega concluída nesta etapa

Foi criada a primeira arquitetura metodológica comum para:
- faturamento empresarial territorial;
- demanda residente;
- demanda não residente;
- mercado capturado;
- faturamento observado;
- faturamento estimado;
- market share.

Arquivo canônico:
`docs/caderno_base/dimensao_mercado_market_share_matriz_v001_20260926.md`

Commit inicial:
`216137e1a06e639297b22cb6f703c66f58cdf0a8`

Drive:
- documento metodológico: `1ren1_4KuNFUwj2wKMz4GzOpZq8PG4Jr5-YRNyafA_L8`
- matriz técnica Google Sheets: `1tkVQt1N0hrAICehL-w-PRnv3AJGonUYfBhOnFOOvFuI`

## Decisões metodológicas

1. CNPJ, lojas, storefronts, vínculos, remuneração, CNES, SINAC/SIMEI e localização de matriz permanecem proibidos como proxies de faturamento ou market share.
2. `faturamento observado` e `faturamento estimado` são estados de mensuração; não são componentes adicionais da demanda.
3. `market share` é uma razão e só pode ser calculada com numerador e denominador compatíveis em setor, geografia, período, canal e conceito monetário.
4. O primeiro perímetro monetário defensável de Bens Essenciais continua sendo **alimentação no domicílio**, porque é o único já modelado com POF/RS.
5. Saúde/Higiene, Bens Não Essenciais e Serviços exigem crosswalks explícitos; não agregar categorias heterogêneas antes disso.
6. Serviços devem ser mensurados por item de serviço/NFS-e, não como um mercado único.
7. Alimentação Fora do Lar permanece separada de Serviços.
8. PNAE é evidência monetária B2G parcial e não representa mercado privado.
9. Econodata e equivalentes podem ser usados apenas como benchmark/modelo externo, nunca como faturamento fiscal observado.

## Descoberta empírica nova

A Receita Estadual do RS disponibiliza dados abertos de Documentos Fiscais Eletrônicos:
- DFe Totais Município 2018–2026;
- DFe Totais CNAE Classe 2018–2026;
- valor e quantidade de DFe por dia;
- atualização semanal;
- tratamento de sigilo com mínimo de quatro contribuintes.

Fonte:
https://receitadados.sefaz.rs.gov.br/paineis/documentos-eletronicos/

A documentação consultada apresenta **município e CNAE em arquivos separados**. Ainda não foi comprovado publicamente um extrato conjunto `município × CNAE`, nem `município × NCM`.

Consequência: o total municipal de DFe pode funcionar como envelope monetário formal; o total estadual por CNAE, como benchmark setorial estadual. **Não é permitido repartir o total municipal usando número de empresas/lojas ou estrutura cadastral.**

## Outras rotas localizadas

### Preços Dinâmicos — Receita Estadual
Usa NFC-e de transações formais ao consumidor e NCM dos produtos. A publicação de preços é agregada por COREDE.

Uso: preços, deflatores e auditoria de cesta.
Não usar como faturamento municipal sem valor/quantidade publicados no recorte compatível.

### NFS-e/CFS-e — Prefeitura de São Borja
O município possui sistema operacional de NFS-e/CFS-e/ISS Digital.

Próximo objetivo:
obter agregado `mês × item LC 116/CNAE × valor bruto × número de notas × município do tomador`, com proteção de sigilo.

### Farmácia Popular/BNAFAR
Fonte potencial para submercado público observado de medicamentos/insumos.

Ainda é necessário auditar:
- acesso;
- variável monetária;
- granularidade municipal;
- granularidade por estabelecimento;
- período.

## Status por setor

| Setor | Demanda residente | Faturamento observado local | Mercado capturado | Market share |
|---|---|---|---|---|
| Bens Essenciais | já modelada para alimentação no domicílio | não setorializado | não disponível | não disponível |
| Saúde/Higiene | obtível após crosswalk POF | potencial DFe + Farmácia Popular parcial | não disponível | não disponível |
| Bens Não Essenciais | obtível por módulos POF | potencial DFe | não disponível | não disponível |
| Serviços | parcial via POF; heterogêneo | potencialmente forte via NFS-e agregada | não disponível | não disponível |
| Alimentação Fora do Lar | obtível via POF fora do domicílio | potencial DFe; PNAE B2G parcial observado | não disponível privado | não disponível |

## Próxima execução

1. obter/ingerir DFe Totais Município 2023–2026;
2. filtrar São Borja e separar NFC-e/NF-e;
3. testar no Power BI/arquivos a existência de cruzamento `município × CNAE`;
4. procurar possibilidade de `município × NCM`;
5. construir crosswalk POF → cinco setores;
6. começar pela estimativa de DR de Alimentação Fora do Lar e Saúde/Higiene;
7. preparar pedido técnico agregado de NFS-e à Prefeitura.

## Controle de continuidade

Não reabrir a auditoria de fidelidade dos cinco cadernos salvo evidência material nova.
