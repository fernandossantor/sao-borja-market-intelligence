# Auditoria cruzada final — quatro cadernos setoriais v002 + síntese transversal
**Data:** 24/09/2026

## 1. Objeto

Verificar consistência editorial, numérica e de rastreabilidade entre os quatro cadernos setoriais v002 e a Síntese Executiva Empresarial v002.

## 2. Artefatos auditados

### Bens Essenciais
- documento: `1r9p39EaDSdHtxLYyqzahjG6xIaWlO-sNcbFBZBQ3L-c`
- planilha: `1MdDysTN-rnFi60O6TA865cvHgUt9lDHpAmQ-kx448YE`

### Saúde/Higiene
- documento: `1sJudMz_AFVw1T7xDYwx10TLPSaZyKfXWkD5NU09MMT8`
- planilha: `112obn025oVqF4muFMod5yCbokP27Wsoy4Xmf6U3HGJY`

### Bens Não Essenciais
- documento: `1gNCKoKPj2SECZf3ocNhiXorftSoQgfqDTAbo-_U0e9A`
- planilha: `1BiHO31FJTpt9jZUM5wIIKL78QOKG0QBeHcc6W4G0oTk`

### Alimentação Fora do Lar e Serviços
- documento: `1BmyJR43OmSp1VDw1nA4oO0iSTna9BiRHs3WYc54Ny3s`
- planilha: `1FjtEZSJiNbhAVDXz5Tff7KGBMMVcf26QQskdcUDt6AY`

### Síntese transversal
- documento: `1-EGjPoFqovGzr1EjZgPb3WPpVYIu9cVRRoW1FNZMNj4`
- planilha: `1wR0CkD1UnWrkKGrttGQPRmZL95QB0S4n0BrKJhJNDQw`

## 3. Verificações editoriais

Confirmado nos quatro cadernos:

- cabeçalho = Diagnóstico v002;
- data = 24 de setembro de 2026;
- nenhum título residual `PESQUISA PRIORITÁRIA`;
- nenhum título residual `PRÓXIMA ETAPA`;
- menções a pesquisa primária aparecem somente para registrar que **não haverá nova aplicação no escopo corrente**;
- IDs dos documentos e planilhas v002 aparecem na rastreabilidade corrente.

## 4. Consistência numérica

### Bens Essenciais

Documento e planilha mantêm:
- demanda anual = R$ 234.706.228,14;
- demanda mensal = R$ 19.558.852,34;
- base corrente = 54 linhas;
- reconciliadas = 52.

Controle:
52/54 não é cobertura municipal.

### Saúde/Higiene

Documento e planilha mantêm:
- 23 registros privados CNES;
- 23 CNPJs;
- 7 raízes;
- 4 raízes multiunidade;
- 20/23 = 86,96%;
- MB = 8/23 = 34,78%;
- Agafarma como controle de possível subcobertura.

Controle:
86,96% e 34,78% não são market share.

### Bens Não Essenciais

Documento e planilha mantêm:
- 122 storefronts no cenário-base;
- 121 na sensibilidade;
- 109 operator_keys;
- 8 raízes multiunidade;
- 21 storefronts nessas raízes;
- moda = 57;
- pet/vet/agro = 20;
- moda + eletro = 64/122 = 52,46%.

Controle:
120→122 não é crescimento e unidades não são market share.

### Alimentação/Serviços

Documento e planilha mantêm:
- 947 optantes SINAC;
- 728 optantes SIMEI;
- salões = 385/370;
- oficinas = 318/261;
- salões + oficinas = 74,23% SINAC / 86,68% SIMEI;
- CNAE 56 = 409 estabelecimentos;
- PNAE CNPJ = R$ 869.843,54 pagos;
- agricultura familiar = 19 contratos / R$ 447.585,44 contratados.

Controles:
- optantes não são pontos físicos nem market share;
- contrato ≠ pagamento;
- B2G ≠ consumo das famílias.

## 5. Consistência transversal

A Síntese Executiva Empresarial v002:

- possui cabeçalho v002 de 24/09/2026;
- contém os quatro IDs setoriais v002 correntes;
- não contém os IDs v001 antigos como referência corrente;
- contém os números-chave dos quatro setores;
- mantém os limites metodológicos específicos de cada caderno.

A planilha transversal registra explicitamente:

> os quatro cadernos setoriais estão em v002 corrente de trabalho.

## 6. Compatibilidade metodológica

Não foram identificadas comparações diretas indevidas entre:

- storefronts BNE e estabelecimentos RFB;
- CNES e RFB como se fossem o mesmo universo;
- optantes SINAC/SIMEI e pontos físicos;
- contratos PNAE e pagamentos;
- REGIC e gasto;
- demanda modelada e faturamento observado;
- entrevistas qualitativas e prevalência populacional.

## 7. Resultado

**AUDITORIA CRUZADA APROVADA PARA O ESTÁGIO DE TRABALHO CORRENTE.**

Os quatro cadernos v002 e a Síntese Executiva Empresarial v002 estão coerentes entre si para:

- leitura empresarial;
- diagnóstico territorial/setorial;
- rastreabilidade;
- continuidade do projeto sem nova coleta primária.

## 8. Limitações transversais remanescentes

Continuam indisponíveis, conforme o setor:

- market share;
- retenção/vazamento monetário;
- faturamento por operador;
- gasto por canal;
- participação monetária digital;
- gasto de visitantes;
- compras na Argentina;
- conversão causal entre ações e vendas.

Essas lacunas não bloqueiam o fechamento setorial.

## 9. Governança

- Caderno-Base v028 permanece read-only;
- PR #41 permanece aberto, draft e sem merge;
- nenhuma auditoria ampla deve ser reaberta sem evidência material nova.
