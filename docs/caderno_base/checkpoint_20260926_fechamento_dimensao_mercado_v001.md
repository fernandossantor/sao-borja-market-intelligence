# Checkpoint — fechamento da etapa de dimensão de mercado e preparação de dados — v001

**Data:** 2026-09-26  
**Projeto:** São Borja — Inteligência Mercadológica  
**Repositório:** `fernandossantor/sao-borja-market-intelligence`  
**Branch:** `feature/cnpj-territorial-control-v1`  
**PR:** #41 — **OPEN / DRAFT / UNMERGED**  
**Base:** `main`  
**Head de partida deste checkpoint:** `3c6fadb0fb7c5870bab497db610a0c4fd5fb7bca`  
**Regra de governança:** não mesclar o PR sem autorização explícita do usuário.

## 1. Escopo da etapa encerrada

Esta etapa fechou a preparação metodológica e técnica para avançar de diagnósticos territoriais/setoriais para:

1. dimensão de mercado;
2. faturamento fiscal observado, quando disponível;
3. demanda residente modelada;
4. demanda não residente, quando observável;
5. mercado capturado;
6. market share, somente quando numerador e denominador forem compatíveis.

A auditoria de fidelidade dos cinco cadernos permanece encerrada. Não reabrir salvo surgimento de evidência material nova.

## 2. Definições canônicas

### DR — Demanda residente

Gasto dos residentes na categoria, independentemente do território/canal.

### DNR — Demanda não residente

Gasto realizado junto a fornecedores de São Borja por pessoas ou organizações cuja base residencial/econômica relevante está fora do município.

### FET — Faturamento empresarial territorial

Receita atribuível a unidades/operações localizadas em São Borja, podendo incluir clientes residentes e não residentes.

### MC — Mercado capturado

`MC = gasto de residentes em fornecedores locais + gasto de não residentes em fornecedores locais`.

### FO — Faturamento observado

Valor administrativo/fiscal/transacional efetivamente observado em fonte compatível.

### FE — Faturamento estimado

Valor produzido por modelo. Deve carregar fórmula, premissas e incerteza.

### PM — Participação de mercado

`PM_i = V_i / V_mercado × 100`.

Só é publicável com:
- mesma categoria;
- mesmo período;
- mesma geografia;
- mesmo canal/perímetro;
- mesmo conceito monetário;
- tratamento compatível de cancelamentos/devoluções;
- cobertura conhecida.

## 3. Proibições metodológicas preservadas

Não utilizar como proxy de faturamento ou market share:

- CNPJ;
- quantidade de lojas/storefronts;
- vínculos;
- remuneração/folha;
- CNES;
- SINAC/SIMEI;
- REGIC;
- presença cadastral de matriz local/externa;
- contagem de notas sem valor;
- ISS arrecadado dividido por alíquota arbitrária;
- participação estadual/regional rateada ao município.

Também permanece proibido distribuir faturamento de rede multiunidade pelo número de lojas.

## 4. Demanda residente modelada — estado corrente

Fonte-base:
- IBGE — POF 2017–2018, Rio Grande do Sul;
- população estimada 2025 de São Borja: 61.311;
- tamanho familiar médio POF/RS: 2,72;
- atualização por IPCA específico até aproximadamente jun/2026.

| Mercado / módulo | Valor anual |
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

Limites:
- Saúde/Higiene: cesta-núcleo não é total do setor;
- BNE: três módulos não representam todo o mercado;
- Serviços pessoais não representam Serviços gerais;
- DR não é faturamento local nem mercado capturado.

## 5. DFe municipal — envelope fiscal observado

Fonte:
Receita Estadual RS — dados públicos de Documentos Fiscais Eletrônicos.

São Borja — NFC-e:

| Ano | Valor observado |
|---|---:|
| 2023 | R$ 843.874.412,06 |
| 2024 | R$ 1.043.404.535,44 |
| 2025 | R$ 1.189.327.276,47 |
| 2026* | R$ 810.740.309,61 |

`* até 14/09/2026`.

Classificação:
**DADO FISCAL OBSERVADO / ENVELOPE MUNICIPAL AMPLO**.

Não é dimensão de nenhum setor específico.

## 6. Interseção pública município × setor

A auditoria dos modelos públicos da Receita Estadual confirmou:

- `município × modelo DFe × período × valor/quantidade`: disponível;
- `COREDE × divisão CNAE × modelo × período × valor/quantidade`: disponível;
- `São Borja × CNAE × valor`: **não localizada publicamente**;
- `São Borja × NCM × valor`: **não localizada publicamente**.

Decisão:
não ratear a composição regional/estadual para São Borja.

## 7. Benchmark fiscal regional — COREDE Fronteira Oeste

NFC-e total observada:

- 2023: R$ 8.872.450.065,47;
- 2024: R$ 10.078.977.261,66;
- 2025: R$ 11.129.327.451,44.

Em 2025:
- CNAE 47 — Comércio varejista: R$ 10.123.462.565,95;
- CNAE 56 — Alimentação: R$ 316.172.104,88.

Natureza:
**DADO OBSERVADO REGIONAL**.

Uso:
benchmark de composição/evolução.

Proibição:
não converter em faturamento municipal por rateio.

## 8. Radar do Mercado — taxonomia NCM canonizada

A auditoria do Radar do Mercado confirmou:

- forte estrutura por NCM, grupo de afinidade, atividade/setor, UF/país;
- ausência de dimensão municipal/COREDE no modelo central auditado;
- valores do Radar não podem ser atribuídos a São Borja.

Catálogo taxonômico corrente:

- **110 grupos de afinidade**;
- **11.765 associações grupo × NCM8**;
- **0 grupos faltantes** após recomposição;
- **0 NCM8 inválidos** após normalização.

Workflow:
`.github/workflows/radar-mercado-ncm-taxonomy-complete-v1.yml`.

Run de completude:
`36267773156`.

Drive:
`SBMI_Radar_Mercado_taxonomia_NCM_completa_v001.zip`  
ID: `1hXk6FCqM4nf3gMwPD5mm-UEoyXfsitlz`.

## 9. Pacote NCM prioritário

O crosswalk dos cadernos foi aplicado ao catálogo completo.

Resultado:

- **43 grupos de prioridade ALTA**;
- **3.424 NCM8 prioritários**;
- **0 NCM8 duplicados entre grupos prioritários**.

Distribuição:

| Setor | NCM8 prioritários |
|---|---:|
| Bens Essenciais | 1.485 |
| Saúde/Higiene/Cuidados Pessoais | 640 |
| Bens Não Essenciais | 1.299 |
| **Total** | **3.424** |

Arquivo operacional:
`radar_ncm_priority_request.csv`.

Run:
`36268054427`.

Artifact:
`10913619323`.

Digest:
`sha256:0807e87c3f943c3ca99199a6af45ff4b61aef322a21b65064a00e31dd7a5c0e3`.

Drive:
`SBMI_Radar_Mercado_taxonomia_NCM_completa_com_pedido_prioritario_v001.zip`  
ID: `1dN3e3r0Q-PYaW069dbAm3c7XS9eJLNNj`.

Documento explicativo:
- GitHub: `docs/caderno_base/radar_ncm_pedido_prioritario_v001_20260926.md`;
- Drive: `1aA_007FT1gm-nbvmGfGYwxzmC5oRO4DDm6JVi3-TbgE`.

## 10. NFS-e/CFS-e — auditoria pública encerrada

O portal público de NFS-e de São Borja foi auditado sem login, credenciais ou contorno de controle de acesso.

Chamadas públicas observadas:
- configuração do portal;
- contador de emitentes;
- contador de NFS-e;
- conteúdos;
- parâmetros de interface.

No run da auditoria:
- emitentes: **6.900**;
- NFS-e emitidas: **4.225.020**.

Natureza:
contadores acumulados/dinâmicos, sem período explícito.

Não foi localizado endpoint público anônimo para:
- valor bruto agregado;
- valor por competência;
- valor por item/código de tributação;
- CNAE;
- município do tomador;
- base de cálculo/ISS agregados.

O endpoint:
`/services/relatorios/public/relatorioTela/requisitar`

foi auditado e classificado como:
**renderizador genérico de relatórios**, não API pública de dados fiscais.

Conclusão:
**PUBLICAÇÃO PÚBLICA DIRETA INSUFICIENTE PARA DIMENSÃO MONETÁRIA DE SERVIÇOS**.

Rastreabilidade:
- discovery run: `36268105386`;
- artifact: `10914950672`;
- context run: `36268475097`;
- artifact: `10915030891`;
- Drive endpoints: `1wc3XCSKBD60FaTg7ioK0ZPj5VGrv1rDI`;
- Drive contexto: `1XHfjjd0sYwOKQopGaqMQanvuyYobM0-H`;
- documento Drive: `1Ei1e4tSSwjbnt1S58n5dQVEvRn7PqO5tnBokn5yi9sQ`.

Contato público do módulo ISSQN identificado:
`iss@saoborja.rs.gov.br`.

## 11. Solicitações institucionais preparadas

### 11.1 Receita Estadual

Especificação técnica:
`docs/caderno_base/receita_dfe_especificacao_extracao_municipio_setor_v001_20260926.md`.

Drive:
`14Pokuwwnc57inTA892twC8ww0IOnp2--KblEGpDCZ6o`.

Minuta:
`docs/caderno_base/minuta_solicitacao_receita_dfe_dimensao_mercado_v001_20260926.md`.

Drive:
`1_2yH9CIOZs-vB4RKhzq0zMr_RROgZWMxqTROq1jjYcM`.

Estratégia:
1. Fale Conosco / Receita Dados;
2. se necessário, SIC/LAI — acesso/abertura de dados;
3. preferir universo completo NCM se tecnicamente viável;
4. se houver limitação de volume, utilizar os 3.424 NCM8 prioritários.

Recorte solicitado:
`ano-mês × município × modelo DFe × CNAE/NCM × quantidade × valor × nº contribuintes × indicador de supressão`.

### 11.2 Prefeitura — NFS-e/CFS-e

Especificação técnica:
`docs/caderno_base/nfse_sao_borja_especificacao_dados_mercado_v001_20260926.md`.

Drive:
`1dse3ZPiwF1zLi-1NHrVKAYOoLE2RCC1oCmK11L0243Q`.

Minuta:
`docs/caderno_base/minuta_solicitacao_prefeitura_nfse_dimensao_mercado_v001_20260926.md`.

Drive:
`185ETNJtakDuXcijT-KGjRoI-nlyNcrOvpWNm7Nn_Lag`.

Recorte preferencial:
`competência × código de tributação/item × município do destinatário × local da prestação × valor bruto × nº notas × situação`.

## 12. Demanda não residente e mercado capturado

Documento metodológico:
`docs/caderno_base/demanda_nao_residente_mercado_capturado_matriz_v001_20260926.md`.

Estado atual:
- REGIC delimita influência, não monetiza DNR;
- NFC-e municipal não identifica origem do consumidor;
- NFS-e pode permitir parcela por município do destinatário, caso a extração administrativa tenha cobertura adequada;
- adquirência/CRM/POS continuam rotas preferenciais para varejo/AFL;
- pesquisa intercept é rota subsidiária.

**Nenhum valor municipal de DNR foi estimado.**

## 13. Protocolo de dados empresariais voluntários

Documento:
`docs/caderno_base/protocolo_dados_empresariais_voluntarios_v001_20260926.md`.

Drive:
`1ibZebz-f-_Edu_8cNHy6ZTVl3GK_NRoAZYiMpGhYddw`.

Objetivo:
preparar numeradores empresariais compatíveis para futuro market share e calibração.

Campos principais:
- participante/unidade local;
- competência;
- módulo;
- canal;
- origem territorial agregada;
- faturamento bruto;
- devoluções/cancelamentos;
- faturamento líquido;
- transações;
- documentos;
- fonte do sistema;
- conceito do valor;
- cobertura da origem.

Fórmula:
`faturamento líquido = faturamento bruto - devoluções/cancelamentos`.

Regra:
numerador empresarial **não substitui denominador do mercado**.

## 14. Instrumento futuro de DNR — varejo/AFL

Documento:
`docs/caderno_base/instrumento_dnr_varejo_afl_v001_20260926.md`.

Drive:
`1F0A47VpgCWK6V1nI7yoXs9R0S5MqMN5oXYW_Mjb6bxw`.

Status:
**DESENHO METODOLÓGICO / NÃO OPERACIONAL**.

Unidade proposta:
transação/ocasião.

Variáveis:
- município/UF/país de residência;
- valor da transação;
- categoria;
- canal;
- data/faixa horária;
- motivo da presença;
- frequência;
- pernoite;
- comparação territorial/digital.

Controle:
sem desenho probabilístico/fator de expansão, resultados futuros seriam apenas descritivos da amostra.

Nenhuma amostra foi definida ou ativada.

## 15. Matriz técnica do Drive

Planilha:
`SBMI — Matriz técnica dimensão de mercado e market share v001 — 20260926`.

ID:
`1tkVQt1N0hrAICehL-w-PRnv3AJGonUYfBhOnFOOvFuI`.

Abas atuais:

1. `Matriz_setorial`;
2. `DFe_envelope`;
3. `POF_crosswalk`;
4. `Rastreabilidade`;
5. `Demanda_residente`;
6. `DFe_COREDE_setor`;
7. `Servicos_controle_ISS`;
8. `DNR_mercado_capturado`;
9. `Radar_NCM_crosswalk`;
10. `Market_share_gates`;
11. `Dados_empresa_template`;
12. `DNR_intercept_template`.

Aba `Dados_empresa_template`:
- validações;
- fórmula de faturamento líquido por linha;
- estrutura pronta para parceiro futuro.

Aba `DNR_intercept_template`:
- formulário tabular futuro;
- explicitamente não operacional nesta etapa.

## 16. Estado setorial consolidado

| Setor | DR | FO municipal-setorial | DNR | Numerador empresarial | Market share |
|---|---|---|---|---|---|
| Bens Essenciais | disponível/modelada | não obtido | não monetizada | protocolo pronto, sem dados | NÃO DEFENSÁVEL |
| Saúde/Higiene | módulos disponíveis/modelados | não obtido | não monetizada | protocolo pronto, sem dados | NÃO DEFENSÁVEL |
| Bens Não Essenciais | módulos disponíveis/modelados | não obtido | não monetizada | protocolo pronto, sem dados | NÃO DEFENSÁVEL |
| Serviços | submercado pessoal modelado | NFS-e a solicitar | potencial via destinatário | protocolo pronto, sem dados | NÃO DEFENSÁVEL |
| Alimentação Fora do Lar | disponível/modelada | CNAE 56 municipal a solicitar | não monetizada | protocolo pronto, sem dados | NÃO DEFENSÁVEL |

## 17. Atualização dos cadernos setoriais

READMEs técnicos atualizados:

- `docs/cadernos_setoriais/bens_essenciais/README.md`;
- `docs/cadernos_setoriais/saude_higiene_cuidados/README.md`;
- `docs/cadernos_setoriais/bens_nao_essenciais/README.md`;
- `docs/cadernos_setoriais/alimentacao_servicos/README.md`.

Eles incorporam:
- DR modelada;
- situação das fontes fiscais;
- pacote NCM;
- limites de market share;
- rotas futuras.

Os documentos editoriais congelados não foram reabertos.

## 18. Próxima etapa

### Dependências externas prioritárias

1. encaminhar solicitação agregada à Receita Estadual;
2. encaminhar solicitação agregada à Prefeitura/ISSQN;
3. registrar protocolo, retorno, prazo e arquivo recebido;
4. preservar resposta negativa/limitação como evidência metodológica.

### Preparação interna paralela

Enquanto aguarda respostas:
- estruturar ingestão/QA para dados DFe e NFS-e recebidos;
- preparar plano de recrutamento de empresas parceiras sem iniciar coleta;
- definir tabela de compatibilidade entre NCM/CNAE/códigos de serviço e módulos SBMI;
- preparar cálculo de indicadores com gates automáticos de defensabilidade;
- incorporar as novas camadas à versão editorial futura dos cadernos apenas quando os dados forem efetivamente obtidos.

## 19. Regra para retomada

Ao retomar o projeto a partir deste checkpoint:

1. não reabrir auditorias encerradas sem evidência nova;
2. não transformar DR modelada em faturamento observado;
3. não converter benchmark regional em valor municipal;
4. não produzir market share por lojas/CNPJ/emprego;
5. priorizar resposta oficial das duas solicitações;
6. usar o pacote NCM prioritário somente como filtro técnico;
7. manter os templates de dados empresariais e DNR inativos até decisão explícita;
8. preservar PR #41 aberto, draft e sem merge.

## 20. Governança ao fechamento

Estado conferido antes da criação deste checkpoint:
- PR #41: **OPEN**;
- draft: **TRUE**;
- merged: **FALSE**;
- branch: `feature/cnpj-territorial-control-v1`;
- head anterior ao checkpoint: `3c6fadb0fb7c5870bab497db610a0c4fd5fb7bca`.

Nenhuma autorização de merge foi concedida.
