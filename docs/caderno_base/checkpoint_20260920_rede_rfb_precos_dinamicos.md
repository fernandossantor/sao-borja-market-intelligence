# Checkpoint — São Borja Inteligência Mercadológica — rede POM, join RFB e Preços Dinâmicos — 20/09/2026

## 1. Governança

- branch de trabalho: `explore/receita-estadual-rs-market-intel-v1`;
- head ao fechar o checkpoint: `b91288272a588b806559dffdc5db18738a6ff510`;
- PR #41: **aberto, draft e sem merge**;
- Caderno-Base v028: **read-only**;
- não criar sucessora da v028 apenas por controles técnicos;
- novas evidências maduras seguem como deltas para o sucessor;
- compras públicas/B2G continuam válidas, sem monopolizar a agenda.

## 2. Estrutura de rede — bens essenciais

A camada documental corrente foi localizada no Drive e também está explicitamente codificada no workflow de join dirigido:

- Drive: `matriz_operadores_bens_essenciais_prejoin_rfb_v002_20260909`;
- workflow: `.github/workflows/bens-essenciais-operadores-rfb-join.yml`.

O recálculo corrente já está consolidado sobre os 52 CNPJs documentais:

- 54 operadores/linhas;
- 52 linhas com CNPJ documental validado = **96,30%**;
- 52 CNPJs únicos;
- 50 raízes CNPJ;
- 2 raízes multiunidade;
- 4 unidades em raízes multi;
- **7,69%** das unidades documentadas em raízes multi;
- maior raiz: 2 unidades = **3,85%** do denominador com CNPJ.

Raízes multiunidade:

- `87397865` — PGL Distribuição de Alimentos / Peruzzo: 2 unidades;
- `91292987` — Libraga, Brandão / Rede Vivo + Rancho Atacadista: 2 unidades.

Pendentes sem CNPJ documental suficientemente confiável:

- Bedi Padaria e Confeitaria;
- Sabor mineiro da Lu Delícias caseiras.

A métrica antiga 46 CNPJs / 44 raízes / 8,70% permanece **LEGACY** e não deve ser reutilizada.

Artefato corrente:
`docs/caderno_base/analise_estrutura_rede_pom_20260920_v001.md`.

## 3. Join RFB dirigido dos 52 CNPJs

Objetivo: validar situação cadastral, identificador oficial matriz/filial, município da unidade, município da matriz e classificação territorial contra RFB 2026-08.

Cinco registros corrigidos/identificados documentalmente em 09/09/2026 permanecem aguardando confirmação oficial RFB:

- Supermercado Baklizi — 00.610.350/0017-37;
- Supermercado Nicolini — 89.835.672/0036-50;
- Mercado Precioso — 55.330.974/0001-25;
- Mercado Santa Lúcia — 07.934.366/0001-87;
- Minimercado D'Gringa — 51.634.027/0001-77.

Foram executados três testes adicionais de transporte em 20/09/2026:

- run `35547624975` — rota estática no domínio oficial;
- run `35547812277` — raiz DAV do compartilhamento público corrente;
- run `35547962441` — variante WebDAV do compartilhamento público.

Em todos:

- checkout/ambiente/preparação dos 52 alvos: sucesso;
- primeiro arquivo `Municipios.zip`: zero bytes;
- retentativas de transporte;
- erro final: `curl: (56) Recv failure: Connection reset by peer`;
- construção do join e upload: não executados.

**Diagnóstico operacional:** bloqueio de transporte/conectividade entre runner hospedado pelo GitHub e o host de arquivos da RFB, antes da leitura dos dados.

**Decisão:** não repetir por ora a mesma estratégia em runner hospedado pelo GitHub. Retomar em rede/ambiente diferente, ou com bytes oficiais previamente adquiridos e SHA-256 preservado.

Artefato consolidado:
`docs/data_sources/rfb_targeted_join_transport_blocker_20260920_v002.md`.

Documento-mestre:
- §42.107 atualizado no Drive;
- nenhum novo `Delta_cadernos`, pois o bloco é controle técnico.

## 4. Preços Dinâmicos — correção auditada de março/2026

A reauditoria do PCA-RE estadual de março/2026 corrigiu um erro de transcrição do seed.

### Dado observado corrigido

Rio Grande do Sul — março/2026:

- PCA-RE: **R$ 287,85**;
- mês: **-0,17%**;
- ano: **-1,16%**;
- 12 meses: **-2,84%**.

O valor anterior **R$ 289,85** foi invalidado como erro de transcrição.

### Checagem calculada

Fevereiro/2026 = R$ 288,33.

`(287,85 / 288,33 - 1) × 100 = -0,1665%`, arredondado para **-0,17%**.

### Fronteira Oeste × RS

Fronteira Oeste em março/2026 permanece **R$ 274,55**.

`(274,55 / 287,85 - 1) × 100 = -4,62%`.

Portanto, o cálculo anterior de **-5,28%** fica invalidado.

### Gravações concluídas e verificadas

GitHub:
- `docs/data_sources/precos_dinamicos_pca_fo_rs_historico_seed_20260920_v001.csv`;
- `docs/caderno_base/analise_precos_dinamicos_serie_historica_seed_20260920_v001.md`;
- `docs/data_sources/precos_dinamicos_pca_marco_2026_auditoria_corretiva_20260920_v001.md`.

Drive:
- aba `PCA_seed` corrigida;
- documento-mestre recebeu §42.108.

Status editorial:
- correção de controle do seed;
- nenhum novo `Delta_cadernos` isoladamente;
- benchmark de agosto/2026 permanece válido.

## 5. Série histórica PCA-RE — estado ao fechar

Seed validado/corrigido:

- jul/2024: FO R$ 248,70 | RS R$ 258,80;
- nov/2024: FO R$ 270,33 | RS R$ 283,92;
- mar/2026: FO R$ 274,55 | RS **R$ 287,85**;
- ago/2026: FO R$ 284,19 | RS R$ 298,61.

Lacunas de 2026 ainda abertas para o par FO × RS:

- janeiro;
- fevereiro;
- abril;
- maio;
- junho;
- julho.

**Não interpolar.**

## 6. Cesta Nutricional Familiar

Gate permanece fechado.

Valor estadual reproduzível para maio/2026:

- RS: R$ 1.453,77;
- mês: +2,86%;
- 12 meses: +2,94%;
- ano: +3,13%;
- composição: 2 adultos com alimentação regular + 1 criança de 4–10 anos.

Não promover enquanto não houver valor reproduzível do COREDE Fronteira Oeste para a mesma competência.

## 7. Outras frentes preservadas

### Saúde/higiene

- 37 CNPJs únicos;
- 24 raízes;
- 17 unidades em raízes multi;
- 45,95%.

Farmácias/drogarias:
- 20 CNPJs únicos;
- 7 raízes;
- 17/20 em raízes multi = 85%;
- maior raiz: 7 unidades = 35%.

Próximo gate: revalidar atividade cadastral das 20 unidades.

### Bens não essenciais

- 103 CNPJs únicos;
- 99 raízes;
- 8 unidades em raízes multi;
- 7,77%;
- maior raiz: 2 unidades = 1,94%.

Próximo gate: revalidar atividade cadastral dos 103 CNPJs.

### Serviços

Não usar 80 linhas do POM como número de operadores: há 3 empresas nomeadas e 77 placeholders.

Recorte RFB amplo — divisões 62+69+71+73+74+82:
- 597 estabelecimentos;
- 97,99% com matriz local.

### Alimentação fora do lar

RFB divisão 56, ago/2026:
- 409 estabelecimentos ativos;
- 4 filiais externas;
- 99,02% com matriz local.

Não interpretar como market share, 409 restaurantes comparáveis ou retenção de faturamento.

## 8. Próxima sequência recomendada para 21/09/2026

1. **Preços Dinâmicos:** continuar busca competência a competência por jan., fev., abr., mai., jun. e jul./2026, sempre FO × RS e sem reconstrução por percentuais arredondados.
2. **RFB dirigido:** manter estacionado no runner GitHub; só retomar após nova rota operacional ou aquisição dos bytes oficiais em outro ambiente.
3. **Farmácias:** iniciar revalidação cadastral das 20 unidades, em bloco pequeno e auditável.
4. **Bens não essenciais:** somente depois do bloco de farmácias, aplicar mesma metodologia aos 103 CNPJs.
5. **Cesta Nutricional:** continuar busca apenas se houver perspectiva de reproduzir Fronteira Oeste para a mesma competência; caso contrário, manter gate fechado.
6. **Editorial:** não criar sucessora da v028 até haver novo bloco analítico maduro.

## 9. Estado de fechamento

- GitHub gravado e verificado em blocos pequenos;
- Drive atualizado e verificado;
- PR #41 confirmado aberto, draft e sem merge;
- v028 não alterada;
- nenhum merge realizado.
