# Compras públicas — retenção seletiva e semântica do objeto — 2026 parcial — v003

**Data:** 20/09/2026  
**Período dos pagamentos:** 01/01/2026 a 18/09/2026  
**Geografia:** São Borja/RS  
**Fonte de pagamentos:** Portal da Transparência PMSB  
**Fonte cadastral:** Receita Federal do Brasil — Dados Abertos CNPJ, competência 2026-08  
**Unidade:** R$ pagos e percentuais calculados  
**Status:** análise exploratória controlada; v003 corrige a interpretação semântica da v002.

## 1. Correção metodológica

A v002 agrupou três rubricas orçamentárias sob a expressão abreviada “bens, materiais e equipamentos”. O valor de **R$ 12.420.349,81** permanece correto como soma de pagamentos a credores sem footprint local em:

1. Material de Consumo;
2. Material, Bem ou Serviço para Distribuição Gratuita;
3. Equipamentos e Material Permanente.

Entretanto, o valor **não pode ser interpretado literalmente como mercado de bens físicos externos**. O probe de 35 pares credor × rubrica mostrou que essas rubricas abrigam também serviços, intermediação e objetos mistos.

## 2. Probe dirigido

O probe capturou:

- **35 pares prioritários**;
- **478 empenhos**;
- **0 falhas**;
- **R$ 9.832.866,60** em pagamentos nos pares selecionados;
- cobertura de **54,31%** de toda a parcela externa do CORE_PROCUREMENT.

Dentro das três rubricas acima, o probe cobre **R$ 9.298.109,07**, ou **74,86%** dos R$ 12.420.349,81 externos.

No subconjunto auditado:

- **R$ 1.246.213,73** são pagamentos claramente vinculados a transporte de pacientes/serviços de transporte;
- **R$ 701.877,60** estão vinculados a credor com função de gerenciamento/intermediação de abastecimento na relação documental conhecida, exigindo reconciliação do instrumento 2026;
- **R$ 1.221.733,83** pertencem a objeto documental misto de iluminação LED, com aquisição e instalação.

Esses três blocos somam **R$ 3.169.825,16**, equivalentes a **34,09%** do subconjunto de três rubricas auditado. No caso de iluminação, o valor mistura bem e serviço; portanto esse percentual mede apenas a parcela que não pode ser tratada como “bem puro”.

## 3. O que permanece válido da v002

Permanece válido como estatística cadastral/orçamentária:

- CORE_PROCUREMENT = **R$ 72.039.491,18**;
- presença local ampliada = **74,87%**;
- externo sem footprint local = **25,13%**;
- sensibilidade sem HIG: presença local ampliada **58,57%**, externo **41,43%**;
- forte heterogeneidade territorial entre rubricas;
- maior parte da parcela externa localizada em outros municípios do próprio RS.

O que muda é a interpretação econômica das rubricas. A rubrica não identifica, por si só, o objeto mercadológico.

## 4. Evidência por finalidade administrativa

A camada `action_territorial_2026.csv` permite avançar uma etapa porque cruza finalidade orçamentária e geografia do credor. A ação ainda não é o item adquirido, mas reduz ambiguidades.

| Finalidade/ação | Pago total | Externo sem footprint | Externo |
|---|---:|---:|---:|
| Transporte sanitário eletivo | R$ 3,035 mi | R$ 2,606 mi | 85,86% |
| Iluminação pública | R$ 3,583 mi | R$ 1,498 mi | 41,82% |
| Recadastramento imobiliário | R$ 1,379 mi | R$ 1,379 mi | 100,00% |
| Farmácia básica e demandas judiciais | R$ 1,004 mi | R$ 0,980 mi | 97,59% |
| Educação infantil — novos | R$ 0,703 mi | R$ 0,703 mi | 100,00% |
| Aquisição de veículos | R$ 0,675 mi | R$ 0,675 mi | 100,00% |
| Manutenção do CER | R$ 0,665 mi | R$ 0,597 mi | 89,68% |
| Combustíveis/lubrificantes* | R$ 0,886 mi | R$ 0,524 mi | 59,09% |
| Benefícios eventuais | R$ 0,606 mi | R$ 0,513 mi | 84,75% |
| Alimentação escolar | R$ 0,870 mi | R$ 0,543 mi | 62,40% |
| Sistema de informática | R$ 0,480 mi | R$ 0,232 mi | 48,27% |
| Restaurante popular | R$ 0,260 mi | R$ 0,200 mi | 77,10% |

*Combina as duas grafias observadas da ação. A presença de gestor/intermediador exige distinguir fornecedor financeiro/operacional do posto que efetivamente entrega combustível.

## 5. Leitura mercadológica revisada

A pergunta correta não é mais:

> “quanto dos bens comprados pela Prefeitura é externo?”

A sequência correta é:

> **rubrica → ação/finalidade → objeto/instrumento → fornecedor efetivo → geografia → possibilidade de substituição/contestação.**

Isso reduz falsos positivos de oportunidade. Transporte de pacientes registrado em 3.3.90.32, por exemplo, não deve ser comparado à oferta de varejo de bens. Da mesma forma, um gestor de abastecimento não identifica automaticamente a geografia do posto que forneceu o combustível.

## 6. Sinais já suficientemente claros

### Serviços territorialmente contestados
- transporte sanitário eletivo: exposição externa elevada;
- recadastramento imobiliário: 100% externo no recorte;
- parte dos serviços TIC permanece extralocal.

### Produtos/cadeias especializadas
- farmácia básica e demandas judiciais: 97,59% externo na finalidade;
- CER/reabilitação: 89,68% externo, mas a ação não distingue produto de serviço;
- veículos: aquisição 100% externa no recorte, coerente com bens de capital especializados.

### Consumo recorrente
- alimentação escolar: 62,40% externo;
- restaurante popular: 77,10% externo.

Esses percentuais medem **geografia cadastral da primeira rodada do pagamento**, não participação de mercado nem vazamento econômico.

## 7. Contestabilidade

Somente após identificar o objeto é possível classificar a demanda como:

- oferta local comprovada;
- oferta local potencial, mas escala/habilitação não conhecida;
- ausência plausível de oferta local;
- fornecimento estruturalmente externo/especializado;
- intermediação/pass-through, em que a geografia do credor não é a geografia econômica final.

A próxima etapa é usar o detalhe completo dos empenhos do CORE_PROCUREMENT para reduzir o universo semanticamente indeterminado e abrir documentos apenas para os maiores valores residuais.

## 8. Governança

A v002 permanece preservada como etapa histórica da análise. Esta v003 a **corrige semanticamente**, sem apagar os cálculos por rubrica.

O Caderno-Base v028 permanece read-only.
