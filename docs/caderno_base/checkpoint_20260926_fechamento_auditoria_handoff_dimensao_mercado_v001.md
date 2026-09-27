# Checkpoint — fechamento da auditoria de fidelidade e handoff para dimensão de mercado — 2026-09-26

## Governança

- Repositório: `fernandossantor/sao-borja-market-intelligence`
- Branch: `feature/cnpj-territorial-control-v1`
- PR #41: **OPEN + DRAFT + UNMERGED**
- Base: `main`
- Não fazer merge sem autorização explícita do usuário.
- Caderno-Base v028: antecedente preservado em somente leitura.
- Caderno-Base v029: base técnica corrente.

## Fechamento da auditoria de fidelidade

A rodada revisou a derivação interna dos cinco reports congelados contra as bases técnicas correntes do projeto, sem nova pesquisa externa.

Cadeia auditada, conforme aplicável:

`report editorial → caderno/base técnica setorial → planilha técnica → registro metodológico / documento-fonte preservado`

Não foi feita nova reextração integral de todas as estatísticas diretamente dos portais oficiais; isso seria uma reauditoria de fonte primária distinta.

### Conclusão

Não foi encontrada discrepância material que invalide as conclusões centrais dos cinco cadernos.

No nível **base técnica corrente → report editorial**, os cinco cadernos estão confirmados quanto a:
- números estruturantes;
- fórmulas centrais;
- unidades;
- períodos;
- denominadores;
- natureza do dado;
- limitações metodológicas;
- integração entre cadernos.

### Bens Essenciais

Confirmados:
- R$ 487,00/família/mês na POF RS;
- 2,72 pessoas/família;
- fator 1,781742384675;
- população 61.311;
- R$ 19.558.852,34/mês;
- R$ 234.706.228,14/ano;
- 54 linhas e 52 CNPJs validados = 96,30%;
- POM qualitativa n=12 em 24/06/2026;
- abastecimento/reposição como missões, não segmentos populacionais;
- demanda modelada não tratada como faturamento ou share.

### Saúde/Higiene

Confirmados:
- POM qualitativa n=12;
- 23 registros/CNPJs privados CNES;
- 7 raízes;
- 4 raízes multiunidade;
- 20/23 = 86,96%;
- maior raiz 8/23 = 34,78%;
- São João 7, Panvel 3, Fronteira 2;
- Agafarma como controle de possível subcobertura;
- CNES não tratado como market share.

### Bens Não Essenciais

Confirmados:
- 122 storefronts; sensibilidade 121;
- 109 operator_keys;
- 8 raízes multiunidade;
- 21 storefronts em raízes multiunidade = 17,21%;
- moda 57;
- pet/vet/agro 20;
- joalheria/óptica/relojoaria 12;
- casa/utilidades/presentes/decoração 7;
- eletro/áudio-vídeo 7;
- moda + eletro = 64/122 = 52,46% de cobertura temática REGIC direta;
- POM qualitativa n=10;
- 120→122 = reconciliação, não crescimento;
- storefront ≠ market share.

### Alimentação Fora do Lar e Serviços

Confirmados:
- POM online n=153, 22/06–06/07/2026;
- percentuais tratados como descritivos da amostra;
- 58,2% de 18–25 anos; 64,1% mulheres;
- 947 SINAC; 728 SIMEI;
- salões 385/370;
- oficinas 318/261;
- clínicas 106/0;
- reparos 100/84;
- hotelaria 27/6;
- lavanderias 11/7;
- salões + oficinas = 74,23% SINAC e 86,68% SIMEI;
- CNAE 56 = 409 estabelecimentos;
- 4 filiais externas = 0,98%;
- PNAE CNPJ = R$ 869.843,54 pagos;
- local = R$ 327.021,02 = 37,60%;
- externo = R$ 542.822,52 = 62,40%;
- agricultura familiar = 19 contratos; R$ 447.585,44 contratados;
- contrato ≠ pagamento; B2G ≠ consumo privado.

### Caderno Geral

Confirmados contra a planilha v029:
- população 1991 63.783; 2010 61.671; 2022 59.676; estimativa 2025 61.311;
- 1991→2022 = -6,44%;
- 2010→2022 = -3,23%;
- domicílios 1991→2010 = +20,96%;
- moradores/domicílio 3,92→3,13;
- urbanização 82,41%→89,41%;
- mediana rendimento domiciliar per capita = R$ 1.100;
- 85,79% sem rendimento ou até 2 SM per capita no universo SIDRA 10296;
- RAIS 2024: 13.125 vínculos no universo primário;
- 12.156 vínculos com remuneração positiva em dezembro;
- mediana dezembro = R$ 2.605,60;
- 56,57% até 2 SM;
- 81,33% até 3 SM;
- jornada >=40h = 90,44%;
- mediana = 44h;
- VAB 2021: agro 33,87%; indústria+construção 11,67%; terciário amplo 54,46%;
- emprego 2021: agro 12,41%; indústria+construção 18,13%; comércio+serviços 69,45%;
- fluxos recorrentes não aditivos;
- integração setorial coerente.

## Controles metodológicos preservados

- vínculo ≠ pessoa;
- remuneração ≠ renda domiciliar;
- PIB per capita ≠ renda disponível;
- estabelecimento ≠ atividade corrente;
- SINAC/SIMEI ≠ ponto físico;
- CNES ≠ market share;
- storefront ≠ participação econômica;
- contrato ≠ pagamento;
- fluxo fronteiriço ≠ gasto;
- REGIC ≠ vendas;
- POM qualitativa ≠ prevalência;
- survey não probabilístico ≠ estimativa municipal;
- demanda modelada ≠ faturamento observado.

## Achados não materiais

Apenas resíduos editoriais pontuais foram observados, sem efeito sobre dados ou interpretação. Podem ser tratados na inspeção visual final e não reabrem a análise.

## Próximo eixo autorizado pelo usuário

**DIMENSÃO DE MERCADO E, SE DEFENSÁVEL, PARTICIPAÇÃO DE MERCADO**

Construir uma matriz por:
1. Bens Essenciais
2. Saúde/Higiene/Cuidados Pessoais
3. Bens Não Essenciais
4. Serviços
5. Alimentação Fora do Lar

Para cada frente:
- universo empresarial observado;
- unidade econômica adequada;
- fontes monetárias disponíveis;
- faturamento observado possível?;
- faturamento estimado possível?;
- demanda residente estimada?;
- demanda não residente estimável?;
- market share real possível?;
- share aproximado possível?;
- dados adicionais;
- grau de confiança.

Princípios:
- não usar CNPJ como proxy de faturamento;
- não usar número de lojas como market share;
- diferenciar faturamento empresarial, gasto residente e mercado capturado;
- priorizar fontes fiscais/transacionais agregadas;
- tratar Econodata como benchmark/modelagem externa, não como dado fiscal observado;
- preferir intervalos a falsa precisão.

## Checkpoint Drive

`1F0dQ_I5ZrScg7aXs5LbdSesjiR2cSX3mau3Gi4kDqbU`

## Checkpoints anteriores

- Drive congelamento editorial: `1gQHy3tmNfTuomtT8yAI74pYFTW5UnHHgp6jaKz-Xb90`
- GitHub: `docs/caderno_base/checkpoint_20260926_congelamento_editorial_v001.md`
- commit: `9d78826534100403c2509f6b82ce19eade7b3488`
