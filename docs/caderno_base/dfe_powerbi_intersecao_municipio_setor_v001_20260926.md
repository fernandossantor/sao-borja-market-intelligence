# DFe Receita Estadual RS — auditoria da interseção município × setor no Power BI público — v001

**Data:** 2026-09-26  
**Fonte:** Receita Estadual do Rio Grande do Sul — Receita Dados — Documentos Eletrônicos  
**Objeto:** verificar se os painéis públicos permitem observar simultaneamente município e setor/CNAE para dimensionar faturamento formal de mercados em São Borja.  
**Natureza:** auditoria técnica do esquema público do Power BI; nenhuma inferência por proxy.

## 1. Pergunta

O painel público de Documentos Fiscais Eletrônicos permite recuperar diretamente:

`São Borja × CNAE/setor × modelo DFe × período × valor`

ou, idealmente:

`São Borja × NCM × modelo DFe × período × valor`?

## 2. Método

Foi criado um workflow reprodutível que:

1. abriu a página pública de DFe da Receita Dados;
2. identificou os iframes Power BI de:
   - Quantidade — Setor;
   - Valor — Setor;
   - Quantidade — Município;
   - Valor — Município;
3. capturou apenas respostas públicas de metadados/esquema e consultas;
4. removeu tokens e cookies antes de persistir qualquer artefato;
5. comparou entidades e propriedades dos modelos sem executar tentativa de acesso privado.

Workflow:
`.github/workflows/dfe-powerbi-schema-discovery-v1.yml`

## 3. Resultado observado — painéis de Setor

Os relatórios públicos de Setor usam a entidade:

`v_PBI_Dfe_Totais_Corede_Setor`.

Propriedades observadas no esquema conceitual:

- `Modelo`;
- `AnoMes`;
- `Data`;
- `nro_mes`;
- `Mês_abrev`;
- `Mês`;
- `cod_corede`;
- `corede`;
- `cod_cnae_divisao`;
- `nome_cnae_divisao`;
- `qtde_dfe`;
- `vlr_total_dfe`;
- `qtde_contrib`;
- `Ano`;
- `dth_atu_dado`;
- filtros de ano e mês.

**Dado observado:** o modelo público setorial possui COREDE + divisão CNAE + modelo fiscal + quantidade + valor.

**Limite:** o esquema não contém código ou nome do município.

## 4. Resultado observado — painéis de Município

Os relatórios públicos de Município usam a entidade:

`v_PBI_Dfe_Totais_Municipio`.

Propriedades observadas:

- `Modelo`;
- `AnoMes`;
- `Data`;
- `nro_mes`;
- `Mês_abrev`;
- `Mês`;
- `qtde_dfe`;
- `vlr_total_dfe`;
- `qtde_contrib`;
- `Ano`;
- `dth_atu_dado`;
- `cod_municipio`;
- `nome_municipio`;
- filtros de ano e mês.

**Dado observado:** o modelo municipal possui município + modelo fiscal + quantidade + valor.

**Limite:** o esquema não contém CNAE, setor ou NCM.

## 5. Resultado sobre NCM

Nenhuma propriedade NCM foi observada nas entidades centrais dos quatro relatórios auditados.

Uma ocorrência textual isolada de “NCM” apareceu no material capturado, mas **não como campo da entidade setorial ou municipal**. Portanto, não há base técnica para afirmar que o painel público auditado permita consulta `município × NCM`.

## 6. Conclusão metodológica

A resposta, para os painéis públicos auditados, é:

**NÃO FOI ENCONTRADA INTERSEÇÃO PÚBLICA DIRETA MUNICÍPIO × SETOR/CNAE, NEM MUNICÍPIO × NCM.**

As duas visões são materializadas em entidades diferentes:

- setor: `COREDE × CNAE divisão × modelo × período × valor/quantidade`;
- município: `município × modelo × período × valor/quantidade`.

Consequentemente, o SBMI não deve:

- repartir o total municipal segundo participação estadual/COREDE do CNAE;
- repartir por número de CNPJs, lojas, vínculos ou remuneração;
- chamar o total do COREDE de faturamento de São Borja;
- inferir NCM municipal a partir de preços ou composição de outras geografias.

Essas operações criariam um faturamento setorial municipal artificial.

## 7. O que permanece utilizável

### Envelope municipal

Os arquivos `DFe_Totais_Municipio` continuam válidos como envelope fiscal amplo de São Borja por modelo e período.

### Benchmark regional-setorial

A entidade `v_PBI_Dfe_Totais_Corede_Setor` pode ser usada como benchmark regional de composição e evolução por divisão CNAE, desde que identificada como COREDE, não município.

Ela poderá auxiliar:

- contexto setorial;
- sazonalidade regional;
- seleção de divisões CNAE prioritárias;
- comparação entre dinâmica municipal ampla e regional-setorial, **sem decompor uma pela outra**.

## 8. Consequência para market share

Com a publicação atual, DFe público não entrega o denominador monetário municipal-setorial exigido para market share dos cinco cadernos.

Market share continua bloqueado enquanto não houver uma das seguintes alternativas:

1. extração oficial agregada `município × CNAE × modelo × mês × valor`;
2. extração oficial `município × NCM × modelo × mês × valor`;
3. base transacional privada/empresarial com cobertura de mercado documentada;
4. outra fonte fiscal pública que preserve simultaneamente território e categoria econômica.

## 9. Recomendação de solicitação à Receita Estadual

Solicitar, em formato agregado e respeitando a mesma regra de sigilo estatístico já aplicada pela Receita Estadual:

`ano-mês | código município | modelo DFe | CNAE divisão/classe | quantidade DFe | valor total DFe | quantidade de contribuintes`.

Para varejos de mix amplo, solicitar adicionalmente, se tecnicamente disponível:

`ano-mês | código município | modelo DFe | NCM/categoria | quantidade | valor | quantidade de contribuintes`.

São Borja: código IBGE **4318002**.

A solicitação não requer identificação de contribuintes.

## 10. Rastreabilidade

Workflow:
`.github/workflows/dfe-powerbi-schema-discovery-v1.yml`

Execução bem-sucedida:
- push run: `36259482012`;
- job: `108452431228`;
- commit: `0b1e7efe5fa5631b4b6b15bff2b8553e9eadbf5b`.

Artifact GitHub:
- ID: `10911359954`;
- digest: `sha256:10b155320338143f65f66aca0e1d1aaef2b65ff8e1d6c406ee2b86b5b041ba62`.

Google Drive:
- `SBMI_DFe_PowerBI_schema_discovery_v001.zip`;
- ID: `10DSvQr01Ij6LVOXPvyPGju5nRQfDDfH9`.

Fonte pública:
- https://receitadados.sefaz.rs.gov.br/paineis/documentos-eletronicos/

## 11. Próximo passo

Como a interseção municipal-setorial não está exposta nos painéis auditados, a prioridade muda para:

1. formalizar pedido agregado à Receita Estadual;
2. avançar com NFS-e municipal para Serviços, onde a administração local detém diretamente o recorte territorial;
3. auditar Farmácia Popular/BNAFAR como submercado de Saúde/Higiene;
4. preservar DFe municipal e COREDE-setor como camadas distintas de evidência.
