# Checkpoint — remediação pré-publicação concluída — cinco cadernos — 2026-09-27

## Objeto

Este checkpoint registra o encerramento da frente de auditoria e remediação pré-publicação dos cinco cadernos correntes do São Borja — Inteligência Mercadológica (SBMI).

A intervenção foi editorial, metodológica e de rastreabilidade. O baseline técnico v029 permanece congelado; não foi criada v030, não foram recalculados indicadores canônicos e não houve nova pesquisa primária.

## Baseline preservado

- Caderno-Base Territorial — São Borja — v029 — congelamento — 20260927  
  Drive: `1Fj6MgIPDetaN8PPUeJ7k8zsH5L6jeHoClmb3ZST9oD4`
- Planilha técnica v029  
  Drive: `1CHn1JZ-IcDxG3V9M5y0PKvN5lTkcvlVcov_vVw3je3c`
- Registro Metodológico v029 — fechamento e congelamento — 20260927  
  Drive: `1aHHbEBLjJKTp61zkdH7ysSz3rrvkfRA8-Iv3KvYtC2w`

v028 permanece como antecedente read-only.

## Cinco cadernos correntes

1. Caderno Geral — Report Empresarial v008  
   Drive: `1E-yRiQlE_YUgrv-qy3dqCceX1rq4PhvCF0xklWLM5Co`
2. Comércio de Bens Essenciais — Report Empresarial v006  
   Drive: `1ctUB-OYxQp1L90tIdoSjOp6Uf2_k8jIekZMnRzEZ3po`
3. Saúde, Higiene e Cuidados Pessoais — Report Empresarial v006  
   Drive: `17fa2arlqa9UrwuEyf8r86WS5GmO1hEI_eiD21txKAaE`
4. Bens Não Essenciais — Report Empresarial v006  
   Drive: `1hgUYwKRV7XD6jMEWA-M52Ah15sXB8LpDHExauLlDzK0`
5. Alimentação Fora do Lar e Serviços — Report Empresarial v006  
   Drive: `1Rk6Zx3NqoKortoEG8mVvMHx-a_NVry-5EnoygHKFojg`

## Auditoria pré-publicação

Documento:
**Auditoria pré-publicação — cinco cadernos — coerência, fidelidade e rastreabilidade — v001 — 20260927**

Drive: `16BTYzs1-FR6q-npTDIO55wXBt1W9QPVU1723eXapy7U`

Resultado substantivo: **PASS**.

Não foram identificados erros críticos de número, fórmula, desenho POM, classificação de evidência, REGIC, market share, DFe/Cesta/Radar, contratos × pagamentos, comparabilidade territorial ou causalidade.

## Remediação A1–A4

### A1 — referências das séries públicas
**RESOLVIDO.**

Foram incorporadas aos cinco cadernos, conforme uso efetivo:
- Documentos Eletrônicos / DFe;
- Preços Dinâmicos da Receita Estadual;
- Radar do Mercado da Receita Estadual.

### A2 — quadros de sustentação
**RESOLVIDO.**

Cada caderno recebeu um **Quadro de sustentação — séries públicas recentes**, com indicador, período, geografia, resultado, natureza e limitação.

### A3 — VAB terciário
**RESOLVIDO.**

No Caderno Geral v008, 54,46% do VAB de 2021 passou a ser identificado como **terciário amplo — comércio, serviços e administração pública**.

O valor numérico não foi alterado.

### A4 — higiene de versionamento
**RESOLVIDO.**

As referências internas foram atualizadas para:
**Caderno-Base Territorial — São Borja — v029 — congelamento — 20260927**.

Também foi saneada a referência do Registro Metodológico para:
**Registro metodológico v029 — fechamento e congelamento — 20260927**.

## Uso de inteligência artificial generativa

Os cinco cadernos passaram a conter subseção metodológica específica sobre IAG.

- Ferramenta: ChatGPT
- Modelo: GPT-5.6 Sol
- Proprietário/desenvolvedor: OpenAI
- Data de referência: 27/09/2026

Uso documentado:
- organização e confronto de evidências;
- apoio à verificação aritmética;
- detecção de inconsistências de versão, unidade, período, conceito e abrangência;
- apoio à formulação/teste de cadeias argumentativas;
- redação, revisão e padronização editorial;
- documentação, rastreabilidade e controle de versões;
- localização de informação externa, mantendo como referência a fonte original verificada.

Controle metodológico:
a IAG não é fonte empírica nem bibliográfica; não autoriza criação de números, categorias, séries ou nomenclaturas oficiais; não substitui validação humana. A reprodutibilidade permanece ancorada em fontes, planilhas, scripts, arquivos, commits e regras versionadas.

Referência:
OPENAI. *GPT-5.6: inteligência de fronteira que acompanha a sua ambição*. 9 jul. 2026. https://openai.com/pt-BR/index/gpt-5-6/. Acesso em: 27 set. 2026.

## QA pós-remediação

Verificação textual concluída nos cinco Docs:
- 1 subseção de IAG por caderno;
- 1 quadro de sustentação das séries recentes por caderno;
- referências oficiais das séries inseridas;
- nenhuma ocorrência remanescente de “integração setorial v002” como título bibliográfico do Caderno-Base;
- rótulo do VAB corrigido no Caderno Geral;
- título final v029 presente nas referências;
- números canônicos preservados.

Resultado: **PASS FINAL — DOCS PUBLICÁVEIS**.

Nenhum PDF foi gerado nesta etapa, conforme solicitação do usuário.

## Rastreabilidade

Planilha técnica v029:
- `Auditoria_5cadernos_v001`: PASS FINAL — DOCS;
- `Rastreabilidade_v029`: estado final registrado.

Registro Metodológico v029:
- A1–A4 registrados como resolvidos;
- uso de IAG registrado;
- PASS FINAL registrado.

Auditoria GitHub:
`docs/governance/auditoria_pre_publicacao_5_cadernos_v001_20260927.md`

Commit de remediação:
`f4a9b6d54ef023fca7f860c1399f904f7a7c2007`

Checkpoint Drive:
`1XV4KCtwgQETkYJI4bnnc6UQObd1tgXidf1eC_jClNAA`

## Governança do PR #41

Estado imediatamente antes da criação deste checkpoint:
- state: **open**
- draft: **true**
- merged: **false**
- mergeable: **true**
- head: `feature/cnpj-territorial-control-v1`
- head SHA: `f4a9b6d54ef023fca7f860c1399f904f7a7c2007`
- base: `main`

Regra: PR #41 deve permanecer **aberto, draft e sem merge**. Nenhum merge, retarget ou fechamento está autorizado sem autorização explícita do usuário.

## Estado final

- Cinco cadernos: **PASS FINAL — DOCS PUBLICÁVEIS**
- A1–A4: **RESOLVIDOS**
- Uso de IAG: **DOCUMENTADO**
- Baseline v029: **CONGELADO**
- v030: **NÃO CRIADA**
- PDFs: **NÃO GERADOS NESTA ETAPA**
- PR #41: **OPEN / DRAFT / UNMERGED**

Este checkpoint encerra a frente de auditoria e remediação pré-publicação.
