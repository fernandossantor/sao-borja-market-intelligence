# Execução — fluxos territoriais Censo 2022 × REGIC 2018

## Objetivo

Construir camada reprodutível de mobilidade dos residentes e centralidade regional de São Borja e referências comparáveis.

## Descoberta de esquema

Workflow `territorial-flows-discovery`.

Run final de descoberta: `34535564511` — success.  
Artifact: `10175249702`, SHA-256 `7f700bd6431edc8c8f99c78a253616392818292890754e13b4717b1707167909`.

A descoberta confirmou:
- Censo 2022 tabela 10329 para local de trabalho principal e retorno;
- Censo 2022 tabela 10324 para local de estudo e curso frequentado;
- REGIC 2018: arquivos oficiais de hierarquia, ligações e atração por tema.

## Ajustes metodológicos observados durante a execução

### Tentativa 1

Run `34535879729` falhou porque o total da tabela 10329 não se reconciliou apenas com as categorias explicitamente selecionadas. Em Alegrete restaram 190 pessoas.

Conclusão: o total inclui casos de local ignorado. O pipeline foi corrigido para preservar o residual, em vez de forçar reconciliação.

### Tentativa 2

Run `34535948836` falhou porque a célula “país estrangeiro” de Santiago estava suprimida.

Conclusão: célula suprimida não é zero. O pipeline foi corrigido para preservar `None` e bloquear agregados dependentes quando necessário.

### Execução canônica

Run `34536030079` — **success**.  
Artifact `10175426211` — SHA-256 `9b6624dcbabbe05da3c684e84c35d69b459181f36fb6b2382e2b423ccc6f7ab2`.

## Regra canônica

1. valor suprimido permanece ausente;
2. nunca imputar zero;
3. residual ignorado só é calculado quando todas as categorias necessárias são observadas;
4. “outro município” é o indicador intermunicipal principal por ser explicitamente observado em todos os comparáveis;
5. “fora do município” agregado só é produzido quando outro município + país estrangeiro + múltiplos são todos observados;
6. Censo e REGIC permanecem separados temporal e conceitualmente.

## Validação

- 6 trabalho;
- 6 estudo;
- 6 hierarquia;
- 6 atração;
- 9 entradas temáticas São Borja;
- 16 saídas São Borja;
- 1 vínculo hierárquico direto;
- reconciliação IA máxima `3.456079866737127e-11`;
- PASS.

## Fonte operacional

Download direto das APIs/bases oficiais do IBGE durante o GitHub Actions. Os arquivos brutos foram preservados dentro do artifact final e promovidos ao Drive dentro do pacote integral.

Drive: `1i95-MMLE5llDxiLYAAPhWBmJ7pQK3TOT`.
