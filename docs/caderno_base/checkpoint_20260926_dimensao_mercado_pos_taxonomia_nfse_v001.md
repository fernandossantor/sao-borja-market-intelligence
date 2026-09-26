# Checkpoint — dimensão de mercado pós-taxonomia NCM e auditoria NFS-e — v001

**Data:** 2026-09-26  
**Repositório:** `fernandossantor/sao-borja-market-intelligence`  
**Branch:** `feature/cnpj-territorial-control-v1`  
**PR:** #41 — **OPEN / DRAFT / UNMERGED**  
**Regra:** não mesclar sem autorização explícita do usuário.

## 1. Estado metodológico

A etapa de fidelidade dos cinco cadernos permanece encerrada.

O eixo corrente é:
**DIMENSÃO DE MERCADO e, somente quando defensável, MARKET SHARE**.

Distinções obrigatórias:
- DR — demanda residente;
- DNR — demanda não residente;
- FET — faturamento empresarial territorial;
- MC — mercado capturado;
- FO — faturamento observado;
- FE — faturamento estimado/modelado;
- PM — participação de mercado.

Continua proibido usar como proxy de faturamento/share:
- CNPJ;
- lojas/storefronts;
- vínculos;
- remuneração;
- CNES;
- SINAC/SIMEI;
- REGIC;
- participação cadastral de matriz local/externa.

## 2. Demanda residente modelada — estado corrente

Fonte-base:
- IBGE/POF 2017-2018 — RS;
- população IBGE 2025 — São Borja = 61.311;
- tamanho médio familiar POF/RS = 2,72;
- IPCA específico por módulo até jun/2026.

| Mercado / módulo | Demanda anual modelada |
|---|---:|
| Bens Essenciais — alimentação no domicílio | R$ 234.706.228,14 |
| Alimentação Fora do Lar | R$ 107.390.938,78 |
| Saúde/Higiene — Higiene e Cuidados | R$ 57.577.114,03 |
| Saúde/Higiene — Remédios | R$ 69.588.767,08 |
| Saúde/Higiene — cesta-núcleo | R$ 127.165.881,11 |
| BNE — Mobiliários/artigos do lar | R$ 32.823.271,13 |
| BNE — Eletrodomésticos | R$ 27.404.143,52 |
| BNE — Vestuário | R$ 73.130.722,82 |
| BNE — soma dos três módulos | R$ 133.358.137,47 |
| Serviços — Serviços pessoais | R$ 18.419.423,64 |

Natureza:
**ESTIMATIVAS MODELADAS DE DEMANDA RESIDENTE**.

Controles:
- cesta-núcleo Saúde/Higiene não é mercado total;
- três módulos BNE não são mercado total;
- Serviços pessoais não representam Serviços gerais;
- DR não é faturamento local nem mercado capturado.

## 3. DFe municipal — envelope fiscal observado

Fonte:
Receita Estadual RS — arquivos públicos `DFe_Totais_Municipio`.

São Borja — NFC-e:

| Ano | Valor |
|---|---:|
| 2023 | R$ 843.874.412,06 |
| 2024 | R$ 1.043.404.535,44 |
| 2025 | R$ 1.189.327.276,47 |
| 2026* | R$ 810.740.309,61 |

`* até 14/09/2026`.

Natureza:
**DADO FISCAL OBSERVADO / ENVELOPE MUNICIPAL AMPLO**.

Não é market size setorial.

## 4. Interseção município × setor

Auditoria dos modelos públicos da Receita Estadual encerrada.

Resultado:
- `município × modelo × período × valor/quantidade`: disponível;
- `COREDE × CNAE divisão × modelo × período × valor/quantidade`: disponível;
- `São Borja × CNAE × valor`: **não localizada publicamente**;
- `São Borja × NCM × valor`: **não localizada publicamente**.

Decisão:
não ratear o envelope municipal por estrutura regional, CNPJs, lojas, emprego ou folha.

## 5. Benchmark COREDE Fronteira Oeste

NFC-e total:
- 2023: R$ 8.872.450.065,47;
- 2024: R$ 10.078.977.261,66;
- 2025: R$ 11.129.327.451,44.

2025:
- CNAE 47 — Comércio varejista: R$ 10.123.462.565,95;
- CNAE 56 — Alimentação: R$ 316.172.104,88.

Natureza:
**DADO OBSERVADO REGIONAL**.

Uso:
benchmark de composição/evolução, nunca faturamento de São Borja.

## 6. Radar do Mercado — taxonomia NCM completa

A auditoria do Radar confirmou:
- forte estrutura por NCM, grupo de afinidade, atividade/setor, UF/país;
- nenhuma dimensão municipal/COREDE identificada no modelo central;
- valores do Radar não são valores de São Borja.

Catálogo completo corrente:
- **110 grupos de afinidade**;
- **11.765 associações grupo × NCM8**;
- **0 grupos faltantes**;
- **0 NCM8 inválidos**.

Workflow:
`.github/workflows/radar-mercado-ncm-taxonomy-complete-v1.yml`.

Run canônico da completude:
`36267773156`.

Drive:
`SBMI_Radar_Mercado_taxonomia_NCM_completa_v001.zip`  
ID: `1hXk6FCqM4nf3gMwPD5mm-UEoyXfsitlz`.

## 7. Pacote NCM prioritário para pedido à Receita

Foi cruzado o catálogo completo com o crosswalk dos cadernos.

Resultado:
- 43 grupos de prioridade ALTA;
- **3.424 NCM8 prioritários**;
- sem duplicação de NCM8 entre grupos prioritários.

Por setor:
- Bens Essenciais: 1.485;
- Saúde/Higiene/Cuidados Pessoais: 640;
- Bens Não Essenciais: 1.299.

Arquivo operacional:
`radar_ncm_priority_request.csv`.

Workflow/run:
- run `36268054427`;
- artifact `10913619323`;
- digest `sha256:0807e87c3f943c3ca99199a6af45ff4b61aef322a21b65064a00e31dd7a5c0e3`.

Drive:
`SBMI_Radar_Mercado_taxonomia_NCM_completa_com_pedido_prioritario_v001.zip`  
ID: `1dN3e3r0Q-PYaW069dbAm3c7XS9eJLNNj`.

Documento:
- GitHub: `docs/caderno_base/radar_ncm_pedido_prioritario_v001_20260926.md`;
- Drive: `1aA_007FT1gm-nbvmGfGYwxzmC5oRO4DDm6JVi3-TbgE`.

## 8. NFS-e São Borja — auditoria da superfície pública

Portal auditado de forma anônima, sem login/credencial.

Chamadas públicas observadas:
- configuração do portal;
- contador de emitentes;
- contador de NFS-e;
- conteúdos;
- parâmetros de interface.

No run da auditoria:
- emitentes: **6.900**;
- NFS-e emitidas: **4.225.020**.

Esses números são contadores sem período explícito e não representam mercado.

Não foi localizado endpoint público anônimo de:
- valor bruto agregado;
- valor por competência;
- valor por item/código de tributação;
- CNAE;
- município do tomador;
- base de cálculo/ISS agregados.

O endpoint:
`/services/relatorios/public/relatorioTela/requisitar`
foi auditado e é um **renderizador genérico de relatórios**, não API de dados fiscais.

Conclusão:
**superfície pública insuficiente para dimensão monetária de Serviços**.

Rastreabilidade:
- discovery run `36268105386`, artifact `10914950672`;
- context run `36268475097`, artifact `10915030891`;
- Drive discovery `1wc3XCSKBD60FaTg7ioK0ZPj5VGrv1rDI`;
- Drive context `1XHfjjd0sYwOKQopGaqMQanvuyYobM0-H`;
- doc Drive `1Ei1e4tSSwjbnt1S58n5dQVEvRn7PqO5tnBokn5yi9sQ`.

Contato público ISSQN observado:
`iss@saoborja.rs.gov.br`.

## 9. Solicitações institucionais preparadas

### Receita Estadual

Especificação técnica:
`docs/caderno_base/receita_dfe_especificacao_extracao_municipio_setor_v001_20260926.md`

Drive:
`14Pokuwwnc57inTA892twC8ww0IOnp2--KblEGpDCZ6o`.

Minuta pronta:
`docs/caderno_base/minuta_solicitacao_receita_dfe_dimensao_mercado_v001_20260926.md`

Drive:
`1_2yH9CIOZs-vB4RKhzq0zMr_RROgZWMxqTROq1jjYcM`.

Estratégia:
1. Fale Conosco / Receita Dados;
2. se necessário, SIC/LAI — pedido de informação/abertura de dados;
3. preferir universo completo NCM se viável;
4. se volume for obstáculo, anexar lista de 3.424 NCM8 prioritários.

### Prefeitura — NFS-e/CFS-e

Especificação técnica:
`docs/caderno_base/nfse_sao_borja_especificacao_dados_mercado_v001_20260926.md`

Drive:
`1dse3ZPiwF1zLi-1NHrVKAYOoLE2RCC1oCmK11L0243Q`.

Minuta pronta:
`docs/caderno_base/minuta_solicitacao_prefeitura_nfse_dimensao_mercado_v001_20260926.md`

Drive:
`185ETNJtakDuXcijT-KGjRoI-nlyNcrOvpWNm7Nn_Lag`.

Prioridade:
`competência × código de tributação/item × município do destinatário × local da prestação × valor bruto × nº notas × situação`.

## 10. Demanda não residente / mercado capturado

Matriz metodológica:
`docs/caderno_base/demanda_nao_residente_mercado_capturado_matriz_v001_20260926.md`.

Estado:
- REGIC delimita influência, não monetiza DNR;
- NFC-e municipal não identifica origem do consumidor;
- NFS-e pode permitir parcela por município do destinatário, mas depende de extração institucional e auditoria de completude;
- adquirência/CRM/intercept continuam rotas para varejo/AFL.

Nenhum valor de DNR foi estimado.

## 11. Cadernos setoriais atualizados

READMEs técnicos foram atualizados com a dimensão de mercado corrente:

- `docs/cadernos_setoriais/bens_essenciais/README.md`;
- `docs/cadernos_setoriais/saude_higiene_cuidados/README.md`;
- `docs/cadernos_setoriais/bens_nao_essenciais/README.md`;
- `docs/cadernos_setoriais/alimentacao_servicos/README.md`.

Não foi alterado o princípio:
**market share segue bloqueado sem denominador monetário municipal-setorial e numerador empresarial compatível.**

## 12. Matriz técnica no Drive

Planilha:
`SBMI — Matriz técnica dimensão de mercado e market share v001 — 20260926`

ID:
`1tkVQt1N0hrAICehL-w-PRnv3AJGonUYfBhOnFOOvFuI`.

Abas correntes:
- Matriz_setorial;
- DFe_envelope;
- POF_crosswalk;
- Rastreabilidade;
- Demanda_residente;
- DFe_COREDE_setor;
- Servicos_controle_ISS;
- DNR_mercado_capturado;
- Radar_NCM_crosswalk.

A planilha preserva:
- dados observados;
- modelagens;
- status de fontes;
- limitações;
- rastreabilidade.

## 13. Estado de market share

Com as fontes públicas e modelagens correntes:

| Setor | Market share atual |
|---|---|
| Bens Essenciais | NÃO DEFENSÁVEL |
| Saúde/Higiene | NÃO DEFENSÁVEL |
| Bens Não Essenciais | NÃO DEFENSÁVEL |
| Serviços | NÃO DEFENSÁVEL |
| Alimentação Fora do Lar | NÃO DEFENSÁVEL |

Não criar share por contagem de lojas/CNPJ ou alocação regional.

## 14. Próxima execução autorizada

### Dependência externa principal

1. encaminhar solicitação agregada à Receita Estadual;
2. encaminhar solicitação agregada à Prefeitura/ISSQN;
3. registrar protocolo/resposta e atualizar a matriz quando houver retorno.

### Enquanto aguarda resposta

Pode-se avançar, sem inventar faturamento, em:
- especificação de pesquisa de DNR para varejo/AFL;
- desenho de protocolo voluntário de dados empresariais/POS;
- definição de indicadores que serão calculados quando os agregados fiscais forem recebidos;
- fechamento editorial das novas notas metodológicas nos cadernos.

## 15. Governança

PR #41 deve permanecer:
- **OPEN**;
- **DRAFT**;
- **UNMERGED**.

Nenhuma autorização de merge foi concedida.
