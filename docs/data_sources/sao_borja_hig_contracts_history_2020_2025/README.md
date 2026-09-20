# Fundação Ivan Goulart / HIG — contratos e instrumentos municipais observados — 2020–2025

## Objetivo

Registrar, em camada exploratória e auditável, contratos, inexigibilidades, dispensas e termos aditivos da Prefeitura de São Borja que identificam explicitamente a Fundação Ivan Goulart, CNPJ **96.488.598/0001-89**.

O conjunto complementa o histórico agregado de licitações:

`docs/data_sources/sao_borja_licitacoes_history_2019_2025/licitacoes_processos_2019_2025.csv`

A finalidade é reconstruir a arquitetura B2G institucional por instrumento e origem econômica, **sem transformar valores administrativos em pagamentos realizados**.

## Fonte

Fontes oficiais municipais:

- Portal/site da Prefeitura de São Borja — Licitações e Contratos;
- Diário Oficial Eletrônico do Município de São Borja;
- PDFs integrais de contratos/aditivos publicados pela Prefeitura.

Geografia: São Borja/RS.  
Beneficiário/contratado: Fundação Ivan Goulart, CNPJ 96.488.598/0001-89.  
Período observado nesta primeira passagem: 2020–2025.  
Unidade monetária: R$ correntes do instrumento publicado.

## Estado do conjunto

**EXPLORATÓRIO — NÃO É CENSO COMPLETO DE CONTRATOS.**

A coleta foi feita por busca dirigida e crosswalk entre:

`processo licitatório → contrato/extrato → termo aditivo → origem declarada`

O conjunto não deve ser interpretado como lista exaustiva de todos os instrumentos entre Município/FMS e Fundação. A página geral de contratos (`/acordos`) é acessível, mas o endpoint de consulta ainda precisa ser sistematicamente mapeado para uma extração censitária e reproduzível.

## Descoberta metodológica

A série de **processos de licitação** já extraída não é suficiente, sozinha, para recuperar todo o histórico institucional da Fundação.

Razões observadas:

1. o nome/CNPJ da Fundação pode não aparecer no resumo agregado do processo;
2. a camada de contrato pode ter numeração distinta da licitação/inexigibilidade/dispensa;
3. aditivos posteriores introduzem ou alteram origens, valores e periodicidades;
4. relações não assistenciais — por exemplo, locação de imóvel — também geram pagamentos à Fundação;
5. contratos estimados e serviços pós-fixados não equivalem ao valor efetivamente pago.

Portanto:

**processo ≠ contrato ≠ aditivo ≠ empenho ≠ liquidação ≠ pagamento.**

## Campos do CSV

- `year`: exercício do instrumento;
- `date`: data observada de assinatura/publicação relevante;
- `contract_number`: número do contrato ou contrato/aditivo;
- `procurement_instrument`: modalidade/instrumento administrativo;
- `object`: objeto resumido;
- `cnpj`: CNPJ da Fundação;
- `observed_value_R$`: valor publicado;
- `value_basis`: significado do valor (mensal, total, estimado, acréscimo etc.);
- `economic_origin`: origem econômica declarada ou classificação ainda a decompor;
- `admin_channel`: canal administrativo;
- `payment_evidence`: se a fonte prova pagamento realizado;
- `overlap_group`: grupo para controle de sobreposição;
- `source_url`: fonte oficial;
- `limitations`: restrições de uso.

## Regras de soma

Os valores **não podem ser somados diretamente** para produzir “receita do HIG”, “repasse municipal”, “financiamento SUS anual” ou “pagamento histórico”.

Antes de qualquer agregação, é obrigatório:

1. identificar se o aditivo apenas altera o contrato-base;
2. delimitar a competência temporal de valores mensais;
3. distinguir valor estimado, autorizado, contratado e efetivamente pago;
4. separar custeio de investimento;
5. decompor origem federal, estadual e municipal própria;
6. excluir sobreposição entre contrato, aditivo, portaria e transferência;
7. reconciliar com execução orçamentária/financeira por fonte.

## Exemplos relevantes desta primeira passagem

### Contrato 20/2023 — recurso federal

A Inexigibilidade 13/2023 e o Contrato 20/2023 registram **R$ 1.023.851,21** de recurso federal para a Fundação.

Esse valor substitui a lacuna de valor que existia no inventário de processos, mas ainda **não é prova de pagamento realizado**.

### Contrato 124/2022 — hemodiálise

Instrumento-base de **R$ 2.584.531,56** para doença renal crônica/hemodiálise. Em 2024, o 1º aditivo acrescentou **R$ 1.263.465,75** via Portaria GM/MS 1.992/2023, inicialmente em 15 parcelas de R$ 84.231,05. Em 2025, o 3º aditivo alterou esse componente para repasse mensal contínuo a partir de janeiro de 2025.

Esses valores pertencem ao mesmo encadeamento contratual e não devem ser tratados como fluxos independentes.

### 21º aditivo do Contrato 99/2021 — SERMulher

Em 2025, o aditivo incluiu:
- **R$ 200.000,00** em parcela única para implantação;
- **R$ 125.000,00 mensais** de custeio, totalizando R$ 1,5 milhão em 12 meses se todas as competências forem transferidas.

Origem declarada: programa estadual SERMulher. A execução deve ser confirmada antes de qualquer anualização.

### Contrato 20/2022 — locação

O 3º aditivo registra locação de edificações do antigo Hospital São Francisco de Borja para diversos programas municipais de saúde, com valor mensal reajustado para **R$ 36.799,28** e vigência até 17/03/2026.

Esse fluxo demonstra que **nem todo pagamento municipal à Fundação corresponde a assistência hospitalar SUS do HIG**. A classificação contábil da receita deve ser verificada na Fundação.

## Próximas etapas

1. mapear de forma reproduzível o módulo oficial de contratos da Prefeitura;
2. construir crosswalk completo 2019–2025 entre processo, contrato, aditivo e Fundação/CNPJ;
3. recuperar execução financeira por instrumento e fonte quando houver rota oficial acessível;
4. reconciliar com DRE/balanços/relatórios anuais da Fundação;
5. manter SIAPC como rota oficial pendente de outro ambiente de rede.

## Arquivo

- `hig_contracts_observed_2020_2025.csv`

Este diretório não altera o Caderno-Base v028 e não autoriza promoção automática de qualquer taxa de dependência financeira.
