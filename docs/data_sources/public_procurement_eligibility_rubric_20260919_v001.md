# Compras públicas PMSB — regra conservadora de elegibilidade por rubrica — v001

**Status:** exploratório — não canônico.  
**Fonte:** Portal da Transparência da Prefeitura de São Borja.  
**Período:** 01/01/2026 a 18/09/2026.  
**Data de atualização indicada pelo portal:** 18/09/2026.

## 1. Auditoria de reconciliação

A extração por CNPJ e rubrica foi concluída sem erro:

- **669** credores CNPJ com pagamento positivo;
- **669/669** processados;
- **33** rubricas observadas;
- valor pago a CNPJ no endpoint de credores: **R$ 132.146.080,70**;
- soma do valor pago nos grids de empenhos: **R$ 132.146.080,70**;
- diferença de reconciliação: **R$ 0,00**;
- **669/669** credores reconciliados ao centavo.

Isso fecha a consistência interna entre o nível “credor” e o nível “empenho”.

## 2. Regra conservadora

Para medir exposição territorial das **compras de bens, serviços, obras e equipamentos**, não é metodologicamente aceitável usar todo o fluxo pago a CNPJs.

Foi criado um núcleo conservador **CORE_PROCUREMENT**, composto apenas por rubricas cuja natureza indica diretamente contratação mercantil de bens/serviços/obras:

- outros serviços de terceiros — pessoa jurídica;
- material de consumo;
- material/bem/serviço para distribuição gratuita;
- equipamentos e material permanente;
- obras e instalações;
- serviços de tecnologia da informação e comunicação;
- serviços de consultoria;
- passagens e despesas com locomoção.

As duas variantes nominais de “outros serviços de terceiros — pessoa jurídica” são mantidas separadas no arquivo-fonte e somadas no núcleo.

## 3. Resultado calculado

**CORE_PROCUREMENT pago:** **R$ 72.039.491,18**.

Fórmula:

CORE_PROCUREMENT / pagamentos a CNPJ
= 72.039.491,18 / 132.146.080,70
= **54,52%**.

Em relação ao total pago a todos os credores (CNPJ + CPF):

72.039.491,18 / 275.649.734,78
= **26,13%**.

Esses percentuais medem apenas o peso do núcleo de rubricas de compra dentro dos pagamentos observados. **Ainda não medem retenção local nem vazamento.**

## 4. Rubricas ambíguas

Foram mantidas fora do núcleo:

- auxílio alimentação;
- despesas de exercícios anteriores;
- outros serviços de terceiros — pessoa física, quando aparece associado a credor CNPJ.

Total ambíguo: **R$ 960.295,65** = **0,73%** do pago a CNPJs.

A inclusão desses valores depende de inspeção do empenho ou da função econômica específica.

## 5. Rubricas excluídas

Pagamentos a CNPJ classificados como não compras no modelo conservador totalizam:

**R$ 59.146.293,87** = **44,76%** do pago a CNPJs.

Incluem dívida, juros, obrigações patronais/tributárias, previdência, pessoal, sentenças, subvenções, contribuições, indenizações e outros fluxos sem natureza de aquisição de bens/serviços.

## 6. Próxima etapa

O indicador territorial deve ser calculado **somente dentro do núcleo elegível**, após enriquecimento cadastral do CNPJ:

**participação local estrita = valor pago CORE_PROCUREMENT a LOCAL_EXACT / valor pago CORE_PROCUREMENT elegível × 100.**

Indicador ampliado:

**participação com presença local = valor pago CORE_PROCUREMENT a (LOCAL_EXACT + ROOT_WITH_LOCAL_FOOTPRINT) / valor pago CORE_PROCUREMENT elegível × 100.**

A classificação RFB 2026-08 está em nova execução. O host oficial apresentou timeout no GitHub Actions; a rotina agora tenta primeiro o host oficial e, apenas se persistir a falha, usa o espelho do snapshot de agosto/2026 como transporte provisório. Qualquer resultado obtido via espelho permanece exploratório até reconciliação com o host oficial/hash.

## 7. Limitações

- rubrica orçamentária não identifica a cadeia completa do fornecedor;
- fornecedor local pode adquirir insumos externamente;
- fornecedor externo pode empregar/subcontratar localmente;
- pagamento do exercício não inclui Restos a Pagar segundo a documentação do portal;
- a métrica proposta é exposição territorial de primeira ordem, não multiplicador econômico nem taxa final de vazamento.
