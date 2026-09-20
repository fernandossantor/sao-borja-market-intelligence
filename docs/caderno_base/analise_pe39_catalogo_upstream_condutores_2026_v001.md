# PE 39/2026 — catálogo upstream de condutores / Cigame — v001

## 1. Objetivo

Testar se a cadeia de abastecimento documentada historicamente para a Iluminar possui, no **catálogo público atual da Cigame**, produtos tecnicamente próximos aos nove clusters prioritários do PE39.

O POM 2025 registra a Cigame como fornecedora da Iluminar para cabos/cordoalhas. A consulta ao catálogo atual mede apenas **acesso potencial upstream**.

Ela **não mede**:
- estoque atual da Iluminar;
- estoque efetivamente disponível na Cigame;
- limite de crédito;
- preço da Iluminar;
- lead time contratado;
- participação no PE39.

## 2. Fonte e período

- relação Iluminar–Cigame: POM Iluminar, 2025;
- catálogo upstream: site público Cigame, consulta em 20/09/2026;
- especificações PE39: normalização SBMI baseada ainda no espelho secundário do certame.

A própria Cigame informa no site institucional que trabalha com estoque variado e logística para o RS, normalmente até 24h em 90% das regiões e até 48h nas demais. Isso descreve a política geral da distribuidora, não prazo garantido para São Borja nem para os itens do PE39.

## 3. Resultado por cluster

| Cluster | Valor PE39 estimado | Evidência atual Cigame | Status |
|---|---:|---|---|
| T01 | R$ 26.208,00 | CABO CHUMBO COBRE PVC 70G 2X4MM CINZA - CORFIO | STRONG_CURRENT_UPSTREAM_MATCH |
| T02 | R$ 27.468,00 | Não localizado em busca dirigida | NOT_DEMONSTRATED_IN_SEARCH |
| T03 | R$ 117.520,00 | ATox/Corfitox 16mm² 0,6/1kV — azul e preto localizados; verde localizado apenas HEPR/PVC não-ATOX | PARTIAL_COLOR_MATCH |
| T04 | R$ 19.836,00 | CABO PP COBRE PVC 70G 500V 2X2,5MM PRETO | CRITICAL_VOLTAGE_MISMATCH |
| T05 | R$ 103.353,00 | Cabos flexíveis HEPR/ATOX 4x10mm 1kV localizados, mas não identificados como PP | CRITICAL_CONSTRUCTION_MISMATCH |
| T06 | R$ 45.534,40 | CABO ALUMINIO QUADRUPLEX 3X16+16MM NEUTRO ISOLADO | POTENTIAL_ARCHITECTURE_MATCH_REQUIRES_TR |
| T07 | R$ 50.520,00 | CABO FLEXIVEL COBRE PVC 70G 750V 1X6MM — azul, verde e preto | STRONG_CURRENT_UPSTREAM_MATCH |
| T08 | R$ 68.850,00 | CABO FLEXIVEL COBRE PVC 70G 750V 1X10MM VERDE - RCM; outras cores requeridas não localizadas na busca dirigida | PARTIAL_COLOR_MATCH |
| T09 | R$ 73.905,00 | CABO FLEXIVEL COBRE PVC 70G 750V 1X25MM — azul, verde e preto | STRONG_CURRENT_UPSTREAM_MATCH |

## 4. Matches fortes atuais

### T01 — plastichumbo 2x4mm 450/750V

O catálogo atual possui **Cabo Chumbo Cobre PVC 70G 2x4mm**, 450/750V, cobre, NBR 8661 e NBR NM 280.

Fonte:
https://www.cigame.com.br/produto/46883/cabo-chumbo-cobre-pvc-70g-2x4mm-cinza---corfio

Classificação: **STRONG_CURRENT_UPSTREAM_MATCH**.

### T07 — flexível cobre 6mm² PVC 70°C

Foram localizadas as três cores necessárias na descrição secundária do PE39 — azul, verde e preto — em produtos de cobre 6mm², PVC BWF, 750V, com certificações.

Fontes principais:
- https://www.cigame.com.br/produto/53193/cabo-flexivel-cobre-pvc-70g-750v-1x6mm-azul---rcm
- https://www.cigame.com.br/produto/53197/cabo-flexivel-cobre-pvc-70g-750v-1x6mm-verde---rcm
- https://www.cigame.com.br/produto/39953/cabo-flexivel-cobre-pvc-70g-750v-1x6mm-preto---rcm

Classificação: **STRONG_CURRENT_UPSTREAM_MATCH**.

### T09 — flexível cobre 25mm² PVC 70°C

Foram localizadas versões azul, verde e preta de cobre 25mm² / PVC 70°C / 750V.

Fontes:
- https://www.cigame.com.br/produto/5443/cabo-flexivel-cobre-pvc-70g-750v-1x25mm-azul---sil
- https://cigame.com.br/produto/47784/cabo-flexivel-cobre-pvc-70g-750v-1x25mm-verde
- https://cigame.com.br/produto/47783/cabo-flexivel-cobre-pvc-70g-750v-1x25mm-preto

Classificação: **STRONG_CURRENT_UPSTREAM_MATCH**.

### Cobertura financeira conservadora

Os três clusters com match forte atual somam:

**R$ 150.633,00 = 28,25%** dos R$533.194,40 estimados nos condutores prioritários.

Essa porcentagem mede **cobertura documental do catálogo upstream**, não capacidade local de fornecimento.

## 5. Matches parciais

### T03 — 16mm² 0,6/1kV ATOX

O catálogo atual possui:
- azul ATOX/Corfitox;
- preto ATOX;
- verde 16mm² HEPR 1kV, porém sem evidência na página consultada de cobertura não-halogenada ATOX.

Fontes:
- https://www.cigame.com.br/produto/47339/cabo-flexivel-cobre-hepr-90g-1kv-1x16mm-azul-atox---corfio
- https://cigame.com.br/produto/47685/cabo-flexivel-cobre-hepr-90g-1kv-1x16mm-preto-atox---cobrecom
- https://cigame.com.br/produto/4485/cabo-flexivel-cobre-hepr-90g-1kv-1x16mm-verde---cobrecom

Classificação: **PARTIAL_COLOR_MATCH**.

Se T03 fosse contado apenas como evidência de **família upstream**, os três matches fortes + T03 representariam R$ 268.153,00, ou 50,29% dos condutores prioritários. Esse percentual **não deve ser chamado de equivalência técnica**.

### T08 — 10mm² PVC70°C

Foi localizada a família de cabo flexível de cobre 10mm²/PVC/750V e a cor verde. As cores azul e vermelha exigidas na descrição secundária não foram demonstradas na busca dirigida.

Classificação: **PARTIAL_COLOR_MATCH**.

## 6. Mismatches críticos

### T04 — PP 2x2,5mm

O catálogo atual contém PP cobre 2x2,5mm certificado, mas a tensão é **500V**, enquanto a descrição secundária do PE39 informa **1kV**.

Classificação: **CRITICAL_VOLTAGE_MISMATCH**.

Não substituir.

### T05 — 4x10mm 1kV

Foram encontrados cabos 4x10mm/1kV HEPR e ATOX, mas a descrição secundária do PE39 diz **PP 4x10mm 1kV**.

Classificação: **CRITICAL_CONSTRUCTION_MISMATCH**.

Se o TR oficial confirmar PP, os produtos encontrados não devem ser tratados como equivalentes apenas por seção/tensão.

## 7. T06 — multiplex 4x16mm² alumínio

O catálogo atual possui cabo de alumínio **quadruplex 3x16+16mm**, 0,6/1kV, XLPE, NBR 8182/NM280.

Fonte:
https://www.cigame.com.br/produto/46530/cabo-aluminio-quadruplex-3x16-16mm-neutro-isolado

A descrição secundária do PE39 diz apenas “multiplex 4x16mm² 1kV alumínio”. O produto é arquiteturalmente compatível com quatro condutores de 16mm², mas não há informação suficiente para declarar equivalência.

Classificação: **POTENTIAL_ARCHITECTURE_MATCH_REQUIRES_TR**.

## 8. T02 — plastichumbo 2x2,5mm

A busca dirigida no catálogo público não encontrou produto exato 2x2,5mm / 450/750V.

Classificação: **NOT_DEMONSTRATED_IN_SEARCH**.

Isso não é evidência de ausência. A Cigame possui plataforma B2B e o site público pode não expor todo o estoque/portfólio acessível.

## 9. Diagnóstico

A hipótese de que a cadeia local esteja isolada de fornecedores tecnicamente compatíveis perde força.

Existe evidência contemporânea de catálogo upstream para uma parcela materialmente relevante da cesta, incluindo matches fortes em T01, T07 e T09.

Mas a cadeia causal ainda não fecha:

`catálogo Cigame → disponibilidade para a Iluminar → estoque/crédito → prazo → preço entregue → habilitação → participação PE39`.

O próximo gargalo já não é “há fornecedor upstream?”. Ele é **transformar catálogo em capacidade comercial local observável**.

## 10. Próxima ação dirigida

1. materializar/reconciliar edital e TR oficial;
2. confirmar as especificações secundárias;
3. para T01, T07 e T09, verificar diretamente na Iluminar:
   - marca/modelo;
   - acesso ao fornecedor;
   - estoque;
   - quantidade;
   - lead time;
   - preço entregue;
4. para T03/T08, resolver as cores faltantes;
5. para T04/T05, manter bloqueio enquanto persistir mismatch técnico;
6. para T06, confirmar arquitetura no TR;
7. só depois calcular contestabilidade por cluster.

## 11. Limitações

- POM liga Iluminar–Cigame em 2025, não comprova compra em 2026;
- catálogo público atual ≠ estoque;
- produto no fornecedor ≠ produto disponível à Iluminar;
- match upstream ≠ habilitação B2G;
- especificação PE39 ainda é secundária;
- percentuais de cobertura são **calculados sobre valor estimado**, não contratado.

## 12. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`.
