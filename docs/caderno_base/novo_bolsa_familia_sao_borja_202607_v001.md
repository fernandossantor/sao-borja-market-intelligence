# Novo Bolsa Família — São Borja/RS — julho de 2026

## Objetivo

Incorporar ao Caderno-Base Territorial uma medida oficial de transferência monetária diretamente registrada no Portal da Transparência para favorecidos do Novo Bolsa Família em São Borja/RS, distinguindo-a de repasses administrativos como o IGD transferido ao FMAS.

## Fonte, período, unidade e abrangência

- **Fonte:** Portal da Transparência do Governo Federal / Controladoria-Geral da União — Dados Abertos — Novo Bolsa Família.
- **Página oficial:** `https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia`.
- **Competência selecionada na interface:** julho de 2026.
- **Link oficial gerado:** `https://portaldatransparencia.gov.br/download-de-dados/novo-bolsa-familia/202607`.
- **Arquivo nacional:** `202607_NovoBolsaFamilia.zip`.
- **Abrangência:** São Borja/RS.
- **Filtro:** `UF = RS` e `NOME MUNICÍPIO`, normalizado, igual a `SAO BORJA`.
- **Código Município SIAFI observado:** `8863`.
- **Campo monetário:** `VALOR PARCELA`.
- **Unidade:** reais correntes.

## Auditoria da fonte

O link gerado pela página oficial retornou HTTP 200 e redirecionou para o repositório de dados abertos da CGU. O ZIP nacional possui **333.637.049 bytes** e SHA-256 `f66e621bfdbb945cf324679e216d3d3b42d2029f39be7f646e046fd28b4c30d4`. O CSV interno possui **2.090.838.330 bytes**.

Foram lidas **18.986.686 linhas nacionais**, com **0 linhas de largura inválida** na rotina validada.

### Esquema efetivamente observado em julho de 2026

O arquivo contém exatamente nove colunas:

1. `MÊS COMPETÊNCIA`;
2. `MÊS REFERÊNCIA`;
3. `UF`;
4. `CÓDIGO MUNICÍPIO SIAFI`;
5. `NOME MUNICÍPIO`;
6. `CPF FAVORECIDO`;
7. `NIS FAVORECIDO`;
8. `NOME FAVORECIDO`;
9. `VALOR PARCELA`.

Codificação: `latin-1`. Delimitador: `;`.

O arquivo efetivamente baixado **não contém `DATA DISPONIBILIZAÇÃO`**. Portanto, a análise desta competência usa somente os campos observados no arquivo e não transpõe silenciosamente campos presentes em outras descrições ou versões da fonte.

## Controle de privacidade

CPF, NIS e nome do favorecido foram processados apenas transitoriamente para controles agregados. **Nenhum identificador individual ou nome foi persistido** no repositório, artifact final, Google Drive ou Caderno-Base.

O pacote preservado contém somente manifestos, esquema, validações e agregados.

## Resultados observados e calculados

### Dados observados no recorte

- **2.199 registros** com `UF = RS` e município literal `SAO BORJA`;
- código Município SIAFI `8863` em **2.199/2.199** registros;
- `MÊS COMPETÊNCIA = 202607` em **2.199/2.199** registros;
- `MÊS REFERÊNCIA = 202607` em **2.199/2.199** registros.

### Resultados calculados a partir dos registros oficiais

- registros municipais: **2.199**;
- registros com `VALOR PARCELA` válido: **2.199**;
- soma de `VALOR PARCELA`: **R$ 1.513.564,00**;
- média por registro/parcela: **R$ 688,30**;
- NIS não vazios distintos: **2.198**; um registro possui NIS vazio;
- CPF não vazios distintos: **1.746**; 439 registros possuem CPF vazio.

Os identificadores são usados somente como controles agregados de integridade. Não se conclui que existam 2.199 famílias nem 2.199 pessoas beneficiárias únicas. A unidade observada é o **registro/parcela**; a unidade “família” exige regra explícita da fonte.

## Distinção em relação ao IGD/FMAS

A planilha do Bolsa Família anteriormente localizada no Drive registra **IGD transferido ao Fundo Municipal de Assistência Social**, isto é, recurso administrativo de gestão. Ela continua excluída de renda domiciliar e demanda de consumo.

A extração atual é conceitualmente distinta: `VALOR PARCELA` pertence à base oficial de favorecidos do Novo Bolsa Família e representa transferência monetária registrada no programa. Mesmo assim, valor da parcela não equivale a consumo efetivo nem a valor necessariamente retido em São Borja.

## Limitações

1. Registro/parcela não equivale automaticamente a família ou pessoa única.
2. O valor de julho de 2026 é mensal e não deve ser anualizado automaticamente.
3. Não é possível inferir quanto do valor foi consumido em São Borja, poupado, transferido ou gasto fora do município.
4. A série mensal ainda não está construída; julho de 2026 é uma primeira referência observada, não média estrutural.
5. Censo 2022, RAIS 2025, INSS/SUIBE 2026-07 e Novo Bolsa Família 2026-07 têm conceitos e universos diferentes; suas massas não devem ser somadas mecanicamente.

## Implicação mercadológica

O Novo Bolsa Família acrescenta uma fonte oficial de **transferência monetária direta** à caracterização do mercado consumidor. Em julho de 2026, o fluxo observado em São Borja foi de **R$ 1,514 milhão**.

Esse fluxo complementa as referências de rendimento domiciliar do Censo 2022, remuneração formal da RAIS 2025 e benefícios emitidos pelo INSS/SUIBE em julho de 2026. A coexistência dessas fontes reforça que a capacidade econômica residente não pode ser descrita somente pela renda formal do trabalho.

Para estimar renda disponível ou capacidade de compra será necessária metodologia explícita para harmonizar períodos, universos, conceitos e possíveis sobreposições entre pessoas/programas.

## Reprodutibilidade e preservação

- workflow: `novo-bolsa-familia-sao-borja-extract`;
- run: `34284691474`;
- job: `102257430159`;
- artifact: `10079014259`;
- SHA-256 do artifact: `41a27542e9b94ce07606ea7cb15868d6aafc67c073f7c8d86e21b9bc7d44c15e`;
- SHA-256 do ZIP nacional: `f66e621bfdbb945cf324679e216d3d3b42d2029f39be7f646e046fd28b4c30d4`;
- SHA-256 do CSV agregado municipal: `fc4ab012979f5802567bd028f2b87ad2fbb208d5dec99fb02bc24323a9c5d07e`.

Google Drive:

- pasta: `_sao_borja/raw/social/novo_bolsa_familia_portal_transparencia/`, ID `15loZ2NDpNcwIwI4hFTxjsNKjFzaxekhq`;
- pacote final agregado e sem PII: ID `1am7E0ILJCp26z9X8MjLu7sdSxqYRN1jn`;
- CSV agregado: ID `1cR1KfPWe_MMwGF9KHHrwNoGJYT5RcjUs`;
- auditoria da fonte: ID `1ZROAIF_0mGaRwL9aWjEHFROQF6qULG42`;
- auditoria por navegador da URL gerada: ID `1UmOptki0AFh_yFBnN1IVsHx99v8pQfHu`;
- nota metodológica nativa: ID `11LpVM7KSmgzZ7hk6Hl5eZix_FVAzPhMP9tRfXheaDNc`.

## Próximo passo

Construir série mensal do Novo Bolsa Família com a mesma regra territorial e de privacidade, verificando em cada competência eventuais mudanças de esquema. Somente depois considerar médias móveis, sazonalidade ou comparação longitudinal.
