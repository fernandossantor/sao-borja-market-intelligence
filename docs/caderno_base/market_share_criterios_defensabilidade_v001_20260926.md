# Market share — critérios de defensabilidade e estado por setor — v001

**Data:** 2026-09-26  
**Geografia:** São Borja/RS  
**Finalidade:** impedir que uma disponibilidade parcial de dados seja convertida prematuramente em participação de mercado.

## 1. Fórmula

`market_share_i = valor_i / valor_total_mercado × 100`

A fórmula só é válida quando numerador e denominador compartilham o mesmo:

1. perímetro de produto/serviço;
2. território;
3. período;
4. canal/conceito fiscal ou contábil;
5. tratamento de cancelamentos, devoluções e impostos;
6. universo de cobertura.

## 2. Gates obrigatórios

### G0 — perímetro definido
O mercado precisa ter fronteira explícita. Ex.: alimentação no domicílio, medicamentos, vestuário, serviços de cabeleireiro, CNAE 56.

### G1 — denominador monetário
Deve existir valor total do mercado no mesmo perímetro. Para **share observado**, o denominador precisa ser fiscal/transacional/contábil observado e ter cobertura conhecida.

### G2 — numerador empresarial
A empresa precisa fornecer ou ter fonte verificável de valor atribuível à sua operação de São Borja no mesmo conceito do denominador.

### G3 — compatibilidade temporal e territorial
Mesmo período e regra geográfica. Faturamento consolidado de rede nacional não pode ser rateado por lojas.

### G4 — compatibilidade de canal
Venda presencial, delivery, e-commerce, NF-e/NFC-e/NFS-e e B2B/B2C não podem ser combinados sem regra explícita.

### G5 — cobertura/sigilo
Deve ser possível saber o que o denominador inclui, exclui ou suprime. Células fiscais suprimidas não são zero.

### G6 — origem do consumidor, quando a pergunta exigir
Necessário para “share da carteira residente” ou para separar residente/não residente. Não é obrigatório para “share do mercado formal capturado no território” se o perímetro for explicitamente territorial.

## 3. Tipos de participação permitidos

### 3.1 Share observado do mercado formal capturado
`vendas observadas da empresa em São Borja / vendas observadas totais do mesmo mercado em São Borja`.

É a primeira modalidade a perseguir.

### 3.2 Share estimado
Só admissível quando numerador e denominador forem estimados com metodologia compatível e incerteza explícita. Deve ser publicado como faixa/sensibilidade quando a precisão não for observada.

### 3.3 Share da carteira residente
`vendas da empresa para residentes de São Borja / demanda total dos residentes`.

Requer identificação compatível da origem/residência do cliente. Não pode ser inferido da localização da loja.

## 4. Estado atual dos gates

| Setor | G0 perímetro | G1 denominador monetário compatível | G2 numerador empresarial | G6 origem cliente | Estado atual |
|---|---|---|---|---|---|
| Bens Essenciais | parcial: alimentação no domicílio está definida | DR estimada existe; **faturamento local setorial observado não** | não disponível | não disponível | market share não defensável |
| Saúde/Higiene | módulos Remédios e Higiene definidos; escopo ampliado em construção | DR núcleo estimada; **faturamento local por produto não** | não disponível | não disponível | market share não defensável |
| Bens Não Essenciais | módulos Vestuário, Móveis e Eletro definidos; escopo ampliado em construção | DR modular estimada; **faturamento local por módulo não** | não disponível | não disponível | market share não defensável |
| Serviços | precisa ser definido por item/submercado de serviço | NFS-e agregada é fonte potencial, ainda não obtida | possível via empresa participante, mas não coletado | cMun do destinatário é campo potencial, a auditar | market share não defensável hoje |
| Alimentação Fora do Lar | POF fora do domicílio e CNAE 56 são referências compatíveis, mas conceitos distintos | DR estimada; COREDE×CNAE56 regional observado; **São Borja×CNAE56 não** | não disponível | não disponível | market share não defensável |

## 5. Dados que NÃO atendem G1 ou G2

Não usar como numerador nem denominador de market share:

- número de CNPJs;
- número de lojas ou storefronts;
- número de vínculos;
- remuneração/folha;
- CNES;
- SINAC/SIMEI;
- localização de matriz;
- IA/PERC_LIG da REGIC;
- quantidade de NFS-e/NFC-e sem valor e perímetro compatível;
- valor do ISS dividido por alíquota presumida;
- participação setorial do COREDE aplicada ao total de São Borja.

## 6. Caminho mínimo por setor

### Bens Essenciais
Obter `São Borja × NCM × NFC-e × valor` para grupos alimentares CORE. Depois, para empresa participante, obter vendas locais no mesmo NCM/período/conceito.

### Saúde/Higiene
Obter NCMs de Medicamentos, Produtos Farmacêuticos, Perfumaria/Cosméticos e demais módulos priorizados. Auditar sobreposição entre “Medicamentos” e “Produtos Farmacêuticos” antes de somar.

### Bens Não Essenciais
Obter NCMs de Vestuário, Calçados, Mobiliário/Iluminação e Eletrodomésticos como primeiro núcleo. Eletrônicos e demais discricionários entram em camada posterior.

### Serviços
Obter NFS-e agregada por `competência × item LC116/CNAE × valor`. Numerador pode vir da contabilidade/NFS-e da empresa participante. Essa estrutura pode gerar share observado por submercado sem identificar concorrentes individualmente.

### Alimentação Fora do Lar
Obter `São Borja × CNAE 56 × NFC-e × valor` ou extração transacional equivalente. Não usar NCM de ingredientes como denominador do serviço de alimentação fora do lar.

## 7. Regra de publicação

Enquanto G1 e G2 não forem simultaneamente atendidos:

**não publicar percentual de market share empresarial.**

Pode-se publicar:
- dimensão da demanda residente estimada;
- envelope fiscal observado;
- benchmark regional observado;
- estrutura competitiva;
- centralidade/atração;
- readiness dos dados.

## 8. Diagnóstico

A principal lacuna não é mais conceitual. O projeto já dispõe de:
- perímetros de demanda residente em vários módulos;
- envelope fiscal municipal;
- benchmark COREDE×CNAE;
- taxonomia NCM;
- especificação de NFS-e e DFe agregados.

O gargalo para market share é agora **empírico**: denominador monetário municipal-setorial e numerador empresarial compatível.

## 9. Próximos marcos

1. solicitar/obter DFe agregado município×CNAE/NCM;
2. solicitar/obter NFS-e agregada por item de serviço;
3. definir protocolo voluntário padronizado de numerador empresarial;
4. calcular share apenas nos submercados em que os gates forem satisfeitos;
5. preservar “não defensável” nos demais.
