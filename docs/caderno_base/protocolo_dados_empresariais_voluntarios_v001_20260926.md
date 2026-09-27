# Protocolo de dados empresariais voluntários — dimensão de mercado e market share — v001

**Data:** 2026-09-26  
**Geografia:** São Borja/RS  
**Finalidade:** definir a estrutura mínima para receber dados voluntários de empresas sem confundir faturamento empresarial com demanda residente ou criar market share incompatível.

## 1. Objetivos

Os dados empresariais voluntários podem cumprir três funções:

1. fornecer **numerador empresarial** compatível para market share quando houver denominador fiscal agregado;
2. calibrar a diferença entre venda documentada, POS e contabilidade;
3. medir origem do cliente/canal quando a empresa possuir informação agregável por município.

Eles **não substituem** o denominador do mercado.

## 2. Unidade analítica

Unidade preferencial:

`competência mensal × empresa participante × unidade local × módulo de mercado × canal × origem geográfica agregada`.

Para redes:
- usar somente operação/unidade atribuível a São Borja;
- não dividir faturamento nacional/estadual por número de lojas;
- se o sistema não separar a unidade local, o dado não é adequado para numerador municipal.

## 3. Campos mínimos

| Campo | Tipo | Uso |
|---|---|---|
| participante_id | texto pseudonimizado | identifica empresa no banco analítico |
| competencia | AAAA-MM | compatibilidade temporal |
| unidade_local | texto/código interno | separar operação de São Borja |
| modulo_sbmi | taxonomia SBMI | compatibilidade de produto/serviço |
| canal | taxonomia SBMI | presencial, retirada, delivery, online atribuído à unidade |
| faturamento_bruto | R$ | valor antes de devoluções/cancelamentos |
| devolucoes_cancelamentos | R$ | reconciliação |
| faturamento_liquido | R$ | numerador preferencial quando compatível |
| transacoes | número | intensidade transacional |
| documentos_fiscais | número | reconciliação opcional |
| origem_municipio_cliente | município/UF ou agregado | DNR/MC, quando disponível |
| origem_pais_cliente | país | fronteira/estrangeiro, quando disponível |
| fonte_sistema | texto | POS, ERP, contabilidade, fiscal |
| conceito_valor | texto | bruto/líquido, tributos incluídos, competência/caixa |
| data_extracao | data | rastreabilidade |
| observacao_cobertura | texto | lacunas/canais não cobertos |

## 4. Fórmulas

### Faturamento líquido empresarial

Quando os campos forem compatíveis:

`FL = faturamento_bruto - devolucoes_cancelamentos`.

### Market share formal local

Somente com denominador fiscal agregado compatível:

`PM_formal = FL_empresa_compatível / FO_mercado_compatível × 100`.

Obrigatório alinhar:
- mesma competência;
- mesma geografia;
- mesmo módulo/categoria;
- mesmo canal/perímetro;
- tratamento de cancelamentos/devoluções;
- tributos e conceito de valor.

### Parcela externa do faturamento participante

Se origem estiver disponível:

`PE_empresa = vendas_a_clientes_externos / vendas_totais_com_origem_conhecida × 100`.

Esse indicador descreve **a empresa participante**, não o mercado municipal inteiro.

## 5. Reconciliação fiscal/POS

Quando empresa fornecer POS/ERP e documentos fiscais:

`diferença_relativa = (valor_POS - valor_fiscal) / valor_fiscal × 100`.

A diferença deve ser investigada antes de qualquer uso como numerador.

Possíveis causas a registrar:
- vendas a prazo;
- cancelamentos;
- devoluções;
- operações B2B;
- canais faturados por outra unidade;
- períodos de competência diferentes;
- documentos fiscais não incluídos no extrato do POS.

## 6. Origem do cliente

Preferência:
- município/UF do cliente já disponível no CRM/POS/fidelidade;
- ou agregação por CEP realizada pela própria empresa.

Não solicitar:
- nome;
- CPF;
- telefone;
- e-mail;
- endereço completo;
- identificador individual de cartão.

O SBMI necessita apenas de agregados territoriais.

Categorias analíticas podem ser derivadas posteriormente:
- São Borja;
- outros municípios do RS;
- outras UFs;
- Argentina;
- outros países;
- origem desconhecida.

Essas são **categorias analíticas do SBMI**, não classificações oficiais.

## 7. Confidencialidade e publicação

Antes da coleta, definir com cada participante:

- finalidade;
- período;
- campos;
- quem terá acesso;
- nível de identificação permitido na publicação;
- possibilidade de divulgação somente agregada;
- regra de supressão quando grupo contiver poucos participantes.

Nenhum limiar numérico de supressão é fixado nesta versão: ele deve ser acordado conforme o desenho da parceria e as exigências institucionais.

## 8. Market share — condição de promoção

Mesmo com faturamento de uma empresa, **não publicar market share** enquanto não houver denominador compatível.

Estados permitidos:

- `NUMERADOR DISPONÍVEL / DENOMINADOR AUSENTE`;
- `NUMERADOR E DENOMINADOR COMPATÍVEIS`;
- `SHARE CALCULÁVEL`;
- `NÃO COMPARÁVEL`.

Nunca preencher denominador usando:
- número de lojas;
- CNPJs;
- funcionários;
- estimativas de faturamento de concorrentes somadas sem cobertura demonstrada.

## 9. Prioridade setorial

### Bens Essenciais
Priorizar venda líquida por módulo/produto e origem do cliente, se disponível.

### Saúde/Higiene
Separar remédios, higiene/beleza, suplementos e artigos médicos quando o sistema permitir.

### Bens Não Essenciais
Separar módulos compatíveis com o crosswalk POF/NCM, evitando um total heterogêneo.

### Alimentação Fora do Lar
Capturar valor da conta/pedido, canal e origem territorial.

### Serviços
Preferir receita por código/linha de serviço compatível com a futura NFS-e agregada.

## 10. Entregável técnico

A matriz Google Sheets de dimensão de mercado deve conter uma aba-modelo com campos mínimos e validações.

O protocolo é voluntário e somente será ativado quando houver empresa parceira ou decisão explícita de campo.
