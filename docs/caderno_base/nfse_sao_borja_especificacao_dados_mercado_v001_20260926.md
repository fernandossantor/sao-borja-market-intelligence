# NFS-e/CFS-e de São Borja — especificação de extração agregada para dimensão de mercado — v001

**Data:** 2026-09-26  
**Geografia:** São Borja/RS  
**Objeto:** Serviços  
**Status:** especificação técnica para obtenção de dados agregados; nenhuma solicitação protocolada nesta etapa.

## 1. Objetivo

Definir o menor conjunto de dados fiscais agregados necessário para estimar faturamento observado de serviços prestados no território de São Borja sem acessar informação individual protegida por sigilo fiscal.

A finalidade analítica é construir denominadores monetários por submercado de serviços e, quando houver numerador empresarial compatível, permitir cálculo futuro de participação de mercado.

## 2. Evidência de disponibilidade administrativa

O Portal do ISS Digital de São Borja informa operação de:

- Nota Fiscal de Serviços Eletrônica — NFS-e;
- NFS-e mobile;
- Cupom Fiscal de Serviço Eletrônico — CFS-e;
- consulta de notas e sistema de gestão fiscal.

O manual vigente da NFS-e contém campos estruturados de tomador, serviço e local da prestação. A legislação municipal obriga contribuintes do ISSQN, nas condições regulamentares, a emitir NFS-e e determina observância do sigilo fiscal e da consistência dos dados.

Fontes:
- https://nfse.saoborja.rs.gov.br/portal/sobre
- https://nfse.saoborja.rs.gov.br/portal/
- https://nfse.saoborja.rs.gov.br/services/arquivos/download/arquivosportal?id=36&nomeArquivo=NFSe-ManualDoContribuinte.pdf&pasta=arquivos
- Decreto municipal publicado em 02/02/2024: https://www.saoborja.rs.gov.br/images/DOESB/2024/Fevereiro/doesb02_02_2024.pdf

## 3. Unidade estatística recomendada

A unidade analítica mínima deve ser uma **célula agregada**, nunca uma nota ou contribuinte identificável.

Chave recomendada:

`competência mensal × item de serviço × município/local do tomador × situação da nota`

Quando tecnicamente disponível, acrescentar:

`CNAE do prestador × natureza do documento (NFS-e/CFS-e)`.

## 4. Campos solicitados

### Dimensões

1. ano-mês de emissão/competência;
2. código do item de serviço da lista da LC 116/2003 ou código municipal equivalente;
3. descrição padronizada do item de serviço;
4. CNAE do prestador, se armazenado no sistema;
5. município do estabelecimento prestador;
6. município do tomador/destinatário, quando informado;
7. município/local da prestação do serviço, quando informado;
8. tipo/modelo do documento: NFS-e, CFS-e ou outro documento de serviço compatível;
9. situação do documento: vigente, cancelado, substituído, quando aplicável.

### Métricas

1. quantidade de documentos;
2. valor bruto dos serviços;
3. valor de deduções, se houver e se comparável;
4. base de cálculo do ISS;
5. valor do ISS;
6. quantidade de prestadores distintos na célula, exclusivamente para controle de sigilo e cobertura;
7. quantidade de tomadores distintos na célula, se tecnicamente possível e sem identificação.

## 5. Proteção de sigilo

A extração deve ser entregue somente em nível agregado.

Recomendação de controle:

- suprimir células com número de prestadores abaixo do limiar definido pela administração tributária;
- não fornecer CNPJ/CPF, razão social, nome, endereço ou chave de nota;
- agregar categorias raras a nível superior quando necessário;
- preservar a distinção entre célula suprimida por sigilo e zero econômico real;
- registrar a regra de supressão utilizada.

O SBMI não necessita de microdados fiscais identificáveis para dimensionar o mercado.

## 6. Recorte temporal

Prioridade:

`2023-01 a última competência fechada disponível em 2026`.

Se a estrutura do sistema ou a comparabilidade mudou durante o período, solicitar indicação explícita da data de mudança e dos campos afetados.

## 7. Produtos analíticos possíveis

Com a extração agregada, podem ser produzidos:

- faturamento observado mensal/anual por item de serviço;
- sazonalidade nominal e, após deflação adequada, real;
- composição do mercado formal de serviços;
- concentração por categorias de serviço, sem inferir concentração empresarial;
- parcela de serviços prestados a tomadores do próprio município versus tomadores externos, quando o município do tomador estiver disponível;
- primeira aproximação de demanda não residente/captura externa **somente quando o município do tomador for efetivamente informado e conceitualmente adequado**.

## 8. Limites

Mesmo com NFS-e/CFS-e agregada:

- nota emitida não prova pagamento/recebimento financeiro;
- faturamento fiscal não equivale a valor adicionado;
- município do tomador não é sempre residência da pessoa consumidora;
- serviços B2C e B2B podem coexistir na mesma categoria;
- informalidade e operações dispensadas de documento fiscal permanecem fora;
- cancelamentos/substituições precisam ser tratados para evitar dupla contagem;
- NFS-e não cobre comércio de mercadorias sujeito a ICMS.

## 9. Condição para market share

O denominador por submercado pode ser utilizado para market share apenas se:

1. o item de serviço representar perímetro econômico claro;
2. o total fiscal estiver líquido de cancelamentos/substituições conforme regra conhecida;
3. o numerador da empresa for apurado no mesmo período, no mesmo item/perímetro e no mesmo conceito de valor;
4. a empresa não misturar no numerador receitas de outros municípios/categorias;
5. a cobertura fiscal do denominador for explicitada.

Sem essas condições, deve-se reportar apenas dimensão de mercado formal observada, não participação empresarial.

## 10. Pedido técnico sugerido à Secretaria Municipal da Fazenda

Solicita-se, para finalidade acadêmica de inteligência mercadológica territorial e exclusivamente em formato agregado, uma tabela mensal de NFS-e/CFS-e contendo:

`ano-mês | item LC 116/código municipal | descrição | CNAE (se disponível) | município do tomador | município/local da prestação | tipo de documento | situação | número de documentos | valor bruto dos serviços | base ISS | ISS | número de prestadores da célula`.

Aceita-se aplicação de supressão estatística ou agregação adicional definida pela Secretaria para preservar o sigilo fiscal.

## 11. Integração ao SBMI

Esta fonte, se obtida, será classificada como:

- **DADO OBSERVADO ADMINISTRATIVO/FISCAL** para valores agregados;
- geografia: São Borja/RS;
- unidade: R$ e número de documentos;
- período: competência mensal;
- cobertura: operações documentadas pelo sistema municipal conforme legislação e regras operacionais vigentes.

Ela substituirá proxies estruturais como SINAC/SIMEI para perguntas de dimensão monetária, sem invalidar o uso desses cadastros para caracterização da oferta.


## 12. Evidência pública adicional de viabilidade operacional

Consulta ao portal público do ISS/NFS-e de São Borja em 2026-09-26 mostrou contadores de:

- **6.900 empresas autorizadas a emitir NFS-e**;
- **4.222.101 NFS-e emitidas**.

Fonte oficial:
- https://nfse.saoborja.rs.gov.br/portal/

**Classificação:** DADO OBSERVADO NO PORTAL, sem período explícito associado ao contador.

Esses números **não são utilizados como dimensão de mercado**:
- o total de empresas não é proxy de faturamento;
- o total de notas é acumulado e não informa período, valor, situação/cancelamento ou item de serviço;
- contagem de documentos não equivale a receita.

A utilidade dos contadores é apenas confirmar que o sistema municipal possui escala transacional suficiente para uma extração agregada relevante.

Também foi localizada especificação técnica municipal do sistema de gestão fiscal que exige, entre outras funcionalidades, relatórios sobre:
- empresas tomadoras de serviços e retenções;
- cancelamentos de NFS-e;
- ISS variável;
- local de tributação em outro município.

Fonte oficial:
- https://www.saoborja.rs.gov.br/images/conteudo/Licitacoes/2022/PRE8422anexoIIretif.pdf

**Interpretação:** há evidência documental de que a infraestrutura administrativa foi especificada para produzir relatórios fiscais úteis ao recorte proposto. Isso aumenta a viabilidade técnica da solicitação, mas não prova que todos os campos solicitados estejam hoje disponíveis em uma única exportação.

A LDO/LOA municipal também publica arrecadação/previsão de ISS como receita tributária. Esse dado pode futuramente funcionar como **controle de consistência fiscal**, porém não deve ser convertido em faturamento de serviços dividindo-se o ISS por uma alíquota arbitrária, pois as alíquotas, bases, retenções, regimes e local de incidência são heterogêneos.


## 13. Controle fiscal auxiliar — arrecadação de ISS

A metodologia de cálculo das receitas da LOA 2026, emitida em 01/12/2025 pelo Município, informa para a rubrica agregada **Imposto sobre Serviços de Qualquer Natureza — ISSQN**:

| Referência | Valor arrecadado |
|---|---:|
| 2023 | R$ 15.171.513,67 |
| 2024 | R$ 17.461.817,14 |
| 2025* | R$ 18.225.601,93 |

`* valor constante no demonstrativo emitido em 01/12/2025; não tratar como fechamento definitivo de 2025 sem confirmação posterior.`

O mesmo demonstrativo registra previsão atualizada de **R$ 18.556.000,00** para 2025 e projeção de **R$ 20.895.000,00** para 2026.

Fonte oficial:
- https://www.saoborja.rs.gov.br/images/LOA2026/28_-_METODOLOGIA_DE_CLCULO_DAS_RECEITAS.pdf

**Uso correto:** controle de consistência fiscal para uma futura extração de NFS-e/ISS.

**Uso incorreto:** dividir o ISS arrecadado por uma alíquota única para estimar faturamento de serviços. A arrecadação agrega principal, multas/juros e dívida ativa, e o universo de serviços possui alíquotas, regimes, retenções, bases e locais de incidência heterogêneos. Portanto, ISS arrecadado não é proxy defensável de faturamento empresarial.


## 14. Município do destinatário — viabilidade para demanda não residente

O manual de conectividade da NFS-e padrão INFISC/RTC publicado para São Borja documenta, no grupo de endereço nacional do destinatário, o campo:

- `cMun` — código IBGE do município do endereço do destinatário do serviço.

O mesmo manual contém também:
- `cLocPrestacao` — local da prestação;
- país da prestação;
- informações de destinatário e endereço;
- município de intermediário quando aplicável.

Fonte oficial:
- https://nfse.saoborja.rs.gov.br/services/arquivos/download/arquivosportal?id=45

**Implicação:** existe suporte técnico no layout atual para produzir, em dados agregados, uma separação entre destinatários com endereço em São Borja e em outros municípios.

Isso melhora a viabilidade de estimar uma camada de **demanda/captura externa em serviços**, mas com três controles:

1. `município do destinatário` não é necessariamente residência usual da pessoa consumidora;
2. é preciso medir completude histórica do campo, especialmente antes da adoção do novo layout nacional/RTC;
3. operações B2B podem atribuir o endereço da empresa tomadora, não o local efetivo do usuário final.

Portanto, o campo deve ser solicitado e auditado, mas só pode ser promovido a proxy de demanda não residente após avaliar cobertura e significado por submercado.
