# Compras públicas — hierarquia de evidência para retenção territorial — v001

**Status:** exploratório — não canônico.  
**Fontes:** TCE-RS/LicitaCon; TCE-RS/SIAPC; Receita Federal do Brasil — CNPJ.

## Regra central

Para responder “quanto da despesa pública municipal é direcionado a fornecedores locais?”, a medida principal deve ser **pagamento**, não valor contratado.

A cadeia administrativa deve permanecer separada:

**contrato → empenho → liquidação → pagamento.**

Cada etapa responde a uma pergunta diferente.

## Hierarquia

### 1. LicitaCon — contrato

VL_CONTRATO mede o valor contratual registrado. É útil para:
- objetos;
- fornecedores;
- modalidades;
- concentração;
- estrutura das compras;
- comparação entre contrato e execução.

Não mede, por si só, saída financeira efetiva.

### 2. SIAPC — empenho

O empenho representa comprometimento orçamentário. É mais próximo da execução que o contrato, mas ainda pode ser anulado, reduzido ou não pago.

### 3. SIAPC — liquidação

A liquidação reconhece obrigação após verificação da entrega/execução. É evidência forte de execução econômica, mas ainda não equivale a pagamento.

### 4. SIAPC — pagamento

O pagamento é a variável preferencial para a primeira rodada de saída financeira da administração municipal.

**Indicador estrito:**

participação local paga = valor pago a CNPJ LOCAL_EXACT / valor pago total elegível.

**Indicador operacional ampliado:**

participação com presença local = valor pago a LOCAL_EXACT + ROOT_WITH_LOCAL_FOOTPRINT / valor pago total elegível.

## Classificação cadastral

LOCAL_EXACT:
o CNPJ credor é estabelecimento ativo em São Borja.

ROOT_WITH_LOCAL_FOOTPRINT:
o CNPJ credor é externo, mas sua raiz empresarial possui estabelecimento ativo em São Borja.

EXTERNAL_NO_LOCAL_FOOTPRINT:
a raiz não apresenta estabelecimento ativo em São Borja na competência RFB utilizada.

PF_OUTRO_INDETERMINADO:
CPF, outro documento, ou caso sem cobertura cadastral suficiente.

## O que ainda não é medido

Mesmo o pagamento a fornecedor local não garante retenção integral. O fornecedor pode:
- comprar mercadorias fora;
- importar equipamentos;
- pagar financiamento externo;
- distribuir lucro a proprietário não residente.

Da mesma forma, fornecedor externo pode:
- empregar trabalhadores locais;
- subcontratar empresa local;
- recolher tributos locais;
- manter filial operacional no município.

Portanto, o indicador mede **exposição territorial de primeira ordem da despesa pública**, não multiplicador total nem taxa final de vazamento.

## Uso editorial

No Caderno Geral, compras públicas devem aparecer como um dos pontos de passagem do modelo de conversão territorial:

**entrada de recursos públicos → despesa municipal → pagamento a credores → cadeia subsequente de fornecedores/trabalho → retenção ou saída.**

LicitaCon e SIAPC são complementares, não substitutos.
