# SINAC/SIMEI — estrutura empresarial por regime e CNAE — São Borja — v002

**Data de consolidação:** 12/09/2026  
**Geografia:** São Borja/RS  
**Fonte primária:** Receita Federal — Estatísticas do Simples Nacional  
**Unidade:** optantes/ocorrências na consulta oficial por município e CNAE  
**Status:** reprodução municipal fechada e reconciliada; candidata à incorporação no Caderno-Base sucessor da v028.

## 1. Fechamento da lacuna anterior

A auditoria v001 registrava como pendente a submissão reproduzível do formulário oficial para São Borja.

Essa lacuna foi encerrada.

A consulta oficial foi reproduzida com:
- UF = RS;
- município = São Borja, código interno 8863;
- posição consolidada = **12/09/2026**;
- consultas totais e por CNAE para SINAC e SIMEI.

Resultados observados:
- **SINAC: 7.176 optantes**;
- **SIMEI: 4.883 optantes**;
- SINAC por CNAE: **427 linhas**;
- SIMEI por CNAE: **233 linhas**.

Validação:
- soma SINAC por CNAE = **7.176**;
- soma SIMEI por CNAE = **4.883**;
- reconciliação total × soma CNAE = **exata nos dois regimes**.

## 2. Relação SIMEI / SINAC

A Receita Federal define SIMEI como o sistema de recolhimento em valores fixos mensais dos tributos abrangidos pelo Simples Nacional devido pelo Microempreendedor Individual. O MEI é optante do Simples Nacional.

Fonte conceitual:
https://www8.receita.fazenda.gov.br/SimplesNacional/Documentos/Pagina.aspx?id=4

Como as duas consultas municipais possuem a mesma posição de consolidação, pode-se calcular:

`4.883 / 7.176 × 100 = 68,05%`.

**Dado calculado:** os optantes SIMEI equivalem a **68,05%** do estoque de optantes SINAC observado na consulta de São Borja em 12/09/2026.

### Limite

Esse percentual:
- não é participação dos MEIs em todos os estabelecimentos ativos do município;
- não pode usar como denominador os 7.306 estabelecimentos ativos da base CNPJ sem reconciliação conceitual;
- não mede faturamento, emprego, valor adicionado ou sobrevivência empresarial.

## 3. Estrutura por divisão CNAE

A decomposição por CNAE mostra forte concentração das opções do Simples em comércio e serviços.

### SINAC — principais divisões

| Divisão CNAE | Optantes | Participação no SINAC |
|---|---:|---:|
| 47 — Comércio varejista | 1.943 | 27,08% |
| 43 — Serviços especializados para construção | 702 | 9,78% |
| 49 — Transporte terrestre | 599 | 8,35% |
| 56 — Alimentação | 498 | 6,94% |
| 45 — Comércio e reparação de veículos automotores e motocicletas | 490 | 6,83% |
| 96 — Outras atividades de serviços pessoais | 447 | 6,23% |

As seis divisões somam:

`4.679 / 7.176 × 100 = 65,21%`.

### SIMEI — principais divisões

| Divisão CNAE | Optantes | Participação no SIMEI |
|---|---:|---:|
| 47 — Comércio varejista | 1.107 | 22,67% |
| 43 — Serviços especializados para construção | 624 | 12,78% |
| 49 — Transporte terrestre | 438 | 8,97% |
| 96 — Outras atividades de serviços pessoais | 420 | 8,60% |
| 56 — Alimentação | 378 | 7,74% |
| 45 — Comércio e reparação de veículos automotores e motocicletas | 327 | 6,70% |

As seis divisões somam:

`3.294 / 4.883 × 100 = 67,46%`.

## 4. Intensidade relativa do SIMEI dentro do SINAC

Como SIMEI está contido no universo do Simples Nacional e as consultas utilizam a mesma data e geografia, a razão por divisão pode ser usada como indicador descritivo da presença relativa de MEI entre optantes do Simples daquela divisão.

Principais razões:

- divisão 96 — outras atividades de serviços pessoais: **93,96%**;
- divisão 43 — serviços especializados para construção: **88,89%**;
- divisão 10 — fabricação de produtos alimentícios: **88,33%**;
- divisão 73 — publicidade e pesquisa de mercado: **80,93%**;
- divisão 56 — alimentação: **75,90%**;
- divisão 49 — transporte terrestre: **73,12%**;
- divisão 45 — comércio/reparação de veículos: **66,73%**;
- divisão 47 — comércio varejista: **56,97%**.

### Interpretação

Há evidência de forte presença de microempreendedores individuais em diversas atividades de serviços, construção, alimentação e transporte entre os optantes do Simples.

Isso sugere uma estrutura empresarial atomizada em parte importante da economia local formal simplificada.

### Não concluir

A razão SIMEI/SINAC não mede:
- informalidade;
- fragilidade empresarial;
- produtividade;
- renda;
- faturamento;
- emprego;
- participação de mercado.

Também não se deve interpretar ausência ou baixa presença SIMEI em uma divisão como ausência de pequenas empresas, porque as regras de elegibilidade do MEI variam por atividade.

## 5. Implicações para os cadernos

### Caderno-Base Territorial

A inclusão fortalece a dimensão de **demografia e estrutura empresarial**, acrescentando um recorte tributário/formal que a base RFB de estabelecimentos ativos não fornece sozinha.

Formulação recomendada:

> Em 12/09/2026, São Borja possuía 7.176 optantes do Simples Nacional na consulta SINAC e 4.883 optantes do SIMEI. A razão SIMEI/SINAC era de 68,05%. Comércio varejista, serviços especializados para construção, transporte terrestre, alimentação, comércio/reparação de veículos e serviços pessoais concentravam 65,21% dos optantes SINAC e 67,46% dos optantes SIMEI. O indicador descreve o regime tributário dos optantes e não deve ser confundido com o universo total de estabelecimentos, faturamento ou emprego.

### Cadernos setoriais

A base por CNAE permite produzir recortes específicos para:
- comércio de bens essenciais;
- saúde, higiene e cuidados pessoais;
- bens não essenciais;
- serviços e alimentação fora do lar.

Esses recortes devem ser construídos por crosswalk explícito `CNAE → mercado do projeto`, sem classificar automaticamente todas as subclasses de uma divisão como pertencentes ao mesmo mercado.

## 6. Comparabilidade com a base CNPJ

A base RFB/CNPJ e SINAC/SIMEI usam conceitos diferentes.

RFB/CNPJ:
- estabelecimentos ativos;
- unidade cadastral;
- competência mensal.

SINAC/SIMEI:
- optantes de regimes tributários;
- consulta consolidada em 12/09/2026.

Portanto:

`7.176 SINAC ≠ 7.306 estabelecimentos ativos RFB`.

A proximidade numérica não autoriza calcular cobertura do Simples sobre o estoque cadastral sem reconciliação por CNPJ e competência.

## 7. Artefatos

Fonte reproduzida:
- `docs/data_sources/sinac_simei_discovery/sao_borja_totals.csv`;
- `docs/data_sources/sinac_simei_discovery/sao_borja_cnae.csv`;
- `docs/data_sources/sinac_simei_discovery/summary.json`;
- `docs/data_sources/sinac_simei_discovery/README.md`.

Derivado:
- `docs/data_sources/sinac_simei_division_summary_20260920_v001.csv`.

## 8. Próximo passo

1. promover o bloco municipal SINAC/SIMEI ao delta do Caderno-Base;
2. construir crosswalk CNAE → quatro mercados dos cadernos setoriais;
3. calcular os recortes setoriais preservando CNAEs incluídos/excluídos;
4. em paralelo, avançar para Cadastur/ANP como próximo bloco municipal observado.

## 9. Governança

- Caderno-Base v028 permanece **read-only**;
- novas inclusões devem compor versão sucessora;
- PR #41 permanece **aberto, draft e sem merge**.
