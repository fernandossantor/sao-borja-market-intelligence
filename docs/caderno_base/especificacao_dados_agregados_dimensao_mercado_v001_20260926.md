# Especificação de dados agregados para dimensão de mercado — v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica  
**Finalidade:** obter denominadores monetários territoriais para dimensão de mercado sem acesso a dados fiscais individualizados e sem utilizar proxies de faturamento.

## 1. Princípio

O projeto **não necessita de identificação de contribuintes individuais**.

O pedido deve privilegiar dados agregados e compatíveis com regras de sigilo estatístico, inclusive supressão de células com poucos contribuintes.

## 2. Solicitação à Receita Estadual do RS — DFe

### Geografia
- município emissor: São Borja;
- código IBGE: 4318002.

### Período
- janeiro/2023 em diante;
- periodicidade mensal.

### Modelos fiscais
- NFC-e separadamente;
- NF-e separadamente;
- não somar os dois modelos.

### Recorte setorial mínimo

Campos desejados:

| Campo | Descrição |
|---|---|
| competência | AAAA-MM |
| município emissor | São Borja / 4318002 |
| modelo_dfe | NFC-e ou NF-e |
| CNAE divisão | código e descrição |
| CNAE classe | código e descrição, se permitido |
| quantidade_dfe | total no agregado |
| valor_total_dfe | soma no agregado |
| contribuintes_distintos | opcional, apenas se compatível com sigilo |
| indicador_supressão | célula suprimida por sigilo, quando aplicável |

### Recorte de produto desejável

Se tecnicamente disponível para NFC-e:

- NCM 4 dígitos e/ou NCM 8 dígitos;
- quantidade de itens;
- valor total dos itens;
- competência mensal;
- município emissor São Borja.

Não é necessário CNPJ.

### Regra de sigilo

Aceita-se integralmente:
- supressão de células abaixo do mínimo de contribuintes;
- agregação de classes;
- arredondamento;
- qualquer procedimento institucional de anonimização.

## 3. Solicitação à Prefeitura de São Borja — NFS-e/CFS-e

### Objetivo

Mensurar faturamento observado agregado de serviços prestados por estabelecimentos localizados em São Borja e, quando possível, distinguir tomadores residentes de não residentes.

### Período
- janeiro/2023 em diante;
- competência mensal.

### Campos desejados

| Campo | Uso |
|---|---|
| competência | série temporal |
| item da LC 116 | delimitação de mercado |
| CNAE do prestador | crosswalk com cadernos |
| valor bruto dos serviços | dimensão monetária |
| valor de deduções | controle da base |
| base de cálculo | auditoria fiscal |
| quantidade de notas | intensidade transacional |
| município do tomador | residente vs. não residente |
| UF do tomador | fluxos externos |
| tipo de tomador PF/PJ | opcional e agregado |
| número de prestadores distintos | opcional, sujeito a sigilo |
| indicador de cancelamento | excluir documentos cancelados |

### Agregação recomendada

`competência × item LC116 × CNAE × município do tomador`

com supressão de células sensíveis.

## 4. O que esses dados permitiriam

### Receita Estadual

Com `São Borja × CNAE × NFC-e`:
- faturamento fiscal observado setorial B2C formal;
- evolução histórica;
- comparação com demanda residente;
- investigação de retenção/vazamento, ainda sem origem do consumidor.

Com `São Borja × NCM × NFC-e`:
- separação de categorias dentro de varejos de mix amplo;
- melhor compatibilidade com Bens Essenciais, Saúde/Higiene e Bens Não Essenciais.

### Prefeitura

Com NFS-e agregada:
- faturamento observado de submercados de serviços;
- separação parcial entre demanda local e não residente quando o município do tomador estiver preenchido;
- denominadores para market share de empresas que voluntariamente fornecerem faturamento compatível.

## 5. O que continuará não sendo possível automaticamente

Mesmo com os dados:
- market share por empresa exige numerador empresarial compatível;
- NFC-e por município emissor não identifica residência do consumidor;
- e-commerce e vendas fora do território podem exigir tratamento separado;
- informalidade não será observada;
- dados fiscais são dimensão formal do mercado, não necessariamente mercado econômico total.

## 6. Prioridade

1. **Receita Estadual: São Borja × CNAE × NFC-e**;
2. **Prefeitura: NFS-e agregada por item/CNAE e município do tomador**;
3. **Receita Estadual: São Borja × NCM × NFC-e**, se disponível;
4. dados empresariais voluntários para calibração e numerador de share.
