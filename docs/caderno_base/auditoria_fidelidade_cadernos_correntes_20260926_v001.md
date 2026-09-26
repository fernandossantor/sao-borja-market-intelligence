# Auditoria de fidelidade dos cinco cadernos correntes — v001 — 2026-09-26

## 1. Objetivo e escopo

Auditar, em profundidade, se os cinco reports editoriais correntes reproduzem fielmente os dados observados ou derivam deles por cálculos, modelos e interpretações rastreáveis, sem introduzir números, causalidades, prevalências, participações econômicas ou conclusões não sustentadas.

### Camada corrente auditada

- Bens Essenciais — Report Empresarial v005 — Drive `1y7uXCTHiMnD8o0tuhAn2ikR0uQJ3Yer4rSFoujS2qS0`
- Saúde/Higiene — Report Empresarial v005 — Drive `1_UEEkci4sYrVkDOFjVDIreu5r0vFHLbxSQEXBKso4DQ`
- Bens Não Essenciais — Report Empresarial v005 — Drive `1q5SUsMnj92ouwSxh9AOfita7ukmZ3f87uJFDBvB2wec`
- Alimentação Fora do Lar e Serviços — Report Empresarial v005 — Drive `1mdk-QHcQT7injbBh1oan0ZH6ksg7OkABMZl9_LBGA7o`
- Caderno Geral — Report Empresarial v006 — Drive `1mhwDUMLnez0lw0PMglvL-JINjcDLGAeE8Dn5xKsrJcg`

Bases: Caderno-Base Territorial v029 narrativa/planilha, Registro Metodológico v029 e quatro bases setoriais v002. A v028 permanece READ-ONLY.

## 2. Classes de auditoria

- **CONFIRMADO DIRETO** — valor/texto existente na fonte.
- **CONFIRMADO DERIVADO** — cálculo ou transformação transparente e reexecutável.
- **INTERPRETAÇÃO CONTROLADA** — leitura sustentada, separada de fato observado.
- **LIMITE VÁLIDO** — pergunta corretamente mantida como não respondível.
- **CORREÇÃO NECESSÁRIA** — erro material, troca de conceito/unidade/período/geografia ou inferência não sustentada.

## 3. Procedimentos

1. Leitura dos cinco reports correntes.
2. Leitura das quatro bases técnicas setoriais v002.
3. Leitura da planilha v029: origem de dados, rastreabilidade, auditorias e abas canônicas.
4. Confronto direto com os quatro relatórios POM originais.
5. Rechecagem aritmética dos principais derivados.
6. Reexecução independente da estrutura setorial RAIS 2024 a partir de `rais_consolidated.csv`.
7. Varredura automatizada de valores canônicos e linguagem causal.
8. Verificação cruzada entre reports setoriais e Caderno Geral.

## 4. Resultado executivo

**APROVADO COM ALTA CONFIANÇA PARA FIDELIDADE MATERIAL.**

Não foi encontrada divergência material entre os principais números publicados e as bases técnicas/fontes primárias examinadas. Também não foi encontrada conversão indevida de:

- contagem cadastral em market share;
- entrevista qualitativa em prevalência populacional;
- contrato em pagamento;
- fluxo de fronteira em gasto;
- REGIC em vendas;
- correlação/simultaneidade em causalidade.

Varredura de valores críticos: **115 verificações**, sendo **107 correspondências literais** e **8 valores sustentados tecnicamente mas não repetidos literalmente** no texto editorial. **Zero valor conflitante** entre os itens testados.

**Correções materiais necessárias: 0.**

## 5. Bens Essenciais

### POM original
Confirmados: 12 entrevistas em profundidade, coleta em 24/06/2026; preço/promoções e variedade; distinção abastecimento/reposição; proximidade em reposição; maior deslocamento quando economia/variedade justificam; Instagram/WhatsApp/apps; filas, poucos caixas, divergência de preços, organização e self-checkout.

O report v005 conserva tudo como evidência qualitativa e não produz prevalência municipal.

### Demanda modelada

[
61.311 	imes (487/2,72) 	imes 1,781742384675 = R$ 19.558.852,34/mês
]

[
R$ 19.558.852,34 	imes 12 = R$ 234.706.228,14/ano
]

Natureza preservada: **ESTIMATIVA MODELADA**, não faturamento, share ou retenção.

### Oferta

- 138 linhas brutas
- 135 nomes únicos
- 54 linhas correntes
- 52 reconciliadas/documentadas
- 52/54 = 96,30%

O 96,30% é prontidão documental interna, não cobertura municipal.

**Status: confirmado.**

## 6. Saúde/Higiene

### POM original
Confirmados: 12 entrevistas; 6 homens/6 mulheres; 03–10/07/2026; ciclos relatados de higiene 15–20 dias; beleza/estética/suplementos 1–2 meses; conveniência de farmácias; confiança técnica em especializadas; pesquisa Google/TikTok/IA; pressão online em itens de maior valor.

O report reduz corretamente a linguagem forte do POM original a **indícios qualitativos**.

### CNES 22/09/2026

- 23 registros/CNPJs privados
- 7 raízes
- 4 raízes multiunidade
- 20/23 = 86,96%
- maior raiz = 8/23 = 34,78%
- 19/23 com match POM
- 4 registros privados adicionais
- 4 públicos municipais excluídos
- Agafarma como controle de possível subcobertura

Não há conversão em market share nem promoção de 23 como total exaustivo.

**Status: confirmado.**

## 7. Bens Não Essenciais

### POM original
Confirmados: 10 entrevistas semiestruturadas; perfis presencial/híbrido/digital; julho/2026 sem janela diária documentada; preço/variedade online; busca digital; páginas/respostas locais deficientes em relatos; experimentar/trocar/crediário; atendimento e sortimento como fricções.

O report não transforma perfis em segmentos populacionais nem inventa datas.

### Oferta reconciliada 24/09/2026

- cenário-base 122 storefronts
- sensibilidade 121
- 109 operator_keys
- 8 raízes multiunidade
- 21 storefronts nessas raízes = 17,21%
- 120→122 = saneamento/reconciliação, não crescimento

Taxonomia:
- moda 57 = 46,72%
- pet/vet/agro 20 = 16,39%
- joalheria/óptica/relojoaria 12 = 9,84%
- casa/utilidades/presentes/decoração 7
- eletro/áudio-vídeo 7
- demais 19

REGIC:
- Q1 São Borja = 13.037,63
- Q2 = 10.525,92
- cobertura temática direta = 64/122 = 52,46%

O report não estende REGIC aos grupos sem correspondência direta e não usa storefront como share.

**Status: confirmado.**

## 8. Alimentação Fora do Lar e Serviços

### Survey POM original
Confirmados diretamente nos gráficos:

- n=153; 22/06–06/07/2026
- 58,2% 18–25 anos
- 64,1% mulheres
- pesquisa online sempre/muitas vezes 79,7%
- avaliações muito/parcialmente 88,3%
- desistência por demora 90,2%
- agendamento digital 91,5%
- alimentação ao menos semanal 55,6%
- qualidade 95,4%
- preço 66,0%
- atendimento 58,8%
- ambiente 54,2%
- escolha após conteúdo digital 92,8%
- delivery 94,2%
- atendimento humanizado 98,1%
- hospitalidade/cultura local 81,7%

O POM original informa 90% de confiança e erro 6,62%, mas não demonstra seleção probabilística suficiente. O SBMI corretamente rebaixa os percentuais para **descrição da amostra**.

Foi confirmado um gráfico com legenda duplicada na pergunta sobre presença ativa em redes sociais; o SBMI corretamente o exclui da síntese formal.

### Serviços — Simples 12/09/2026

- 947 SINAC / 728 SIMEI
- salões 385/370
- oficinas 318/261
- clínicas 106/0
- reparos 100/84
- hotelaria 27/6
- lavanderias 11/7
- salões+oficinas = 74,23% SINAC / 86,68% SIMEI

Optante ≠ empresa ativa ≠ ponto físico ≠ market share.

### Alimentação — RFB/PNAE

- CNAE 56: 409 estabelecimentos; 4 filiais de matriz externa = 0,98%
- PNAE CNPJ: R$ 869.843,54 pagos
- local: R$ 327.021,02 = 37,60%
- externo: R$ 542.822,52 = 62,40%
- agricultura familiar: 19 contratos; R$ 447.585,44 contratados

Contrato ≠ pagamento; B2G ≠ consumo privado; universos não aditivos.

**Status: confirmado.**

## 9. Caderno Geral v006

### Demografia
Confirmados na v029:
- 63.783 (1991), 61.671 (2010), 59.676 (2022), 61.311 estimados (2025)
- 1991→2022 = -6,44%
- 2010→2022 = -3,23%
- domicílios 16.214→19.613 (1991–2010) = +20,96%
- moradores/domicílio 3,92→3,13
- urbanização 82,41%→89,41%

### Renda Censo
- mediana per capita = R$ 1.100
- sem rendimento ou até 2 SM pc = 85,79%
- universo SIDRA 10296 = 59.038
- sem conversão para classes ABEP

### RAIS 2024 — reexecução independente
Arquivo `rais_consolidated.csv`, filtro ativo em 31/12 e não abandonado:

- total 13.125
- agro 1.635 = 12,46%
- indústria 1.285 = 9,79%
- construção 543 = 4,14%
- comércio 3.586 = 27,32%
- serviços 6.076 = 46,29%
- comércio+serviços = 73,62%

Abas canônicas:
- remuneração dezembro positiva: 12.156 vínculos
- mediana = R$ 2.605,595
- até 2 SM = 56,57%
- até 3 SM = 81,33%
- jornada >=40h = 90,44%
- mediana de horas = 44

Todos coincidem com v006.

### VAB × RAIS 2021
- agro 33,87% VAB / 12,41% emprego
- indústria+construção 11,67% / 18,13%
- comércio+serviços 54,46% / 69,45%

O report preserva denominadores distintos e não chama a diferença de produtividade causal.

### Fluxos recorrentes
- INSS jul/2026 = R$ 24.535.168,54
- NBF jul/2026 = R$ 1.513.564,00
- RAIS empresarial dez/2025 = R$ 23.940.059,71
- folha pública não municipal parcial v025 ≈ R$ 9,552 mi/mês

O report não soma esses universos.

### Agro e crédito
- SICOR real-proxy pico 2023 ≈ R$ 1,026 bi
- 2024 -22,72%
- 2025 -25,38%
- jan–ago/2026 -36,31% a/a
- ESTBAN rural 47,64%–55,55% no recorte junho

### Fronteira
- 2022 ≈ US$ 5,829 bi, 29%
- 2024 US$ 5,64 bi, 29%
- mobilidade vicinal ≈10 mil→≈23 mil veículos/mês
- 206 mil atendimentos migratórios em 2023

O report explicita: circulação ≠ gasto/permanência/captura.

### Demografia empresarial
Mai–jul/2026:
- SB abertura 1,43%, fechamento 0,87%, turnover 2,30%
- RS 1,66%, 1,05%, 2,71%
- tempo abertura SB 34,46 dias; São Gabriel 14,40; Alegrete 15,27; Santiago 10,00

Janela curta e ausência de causalidade burocrática preservadas.

**Status geral do Caderno Geral: confirmado.**

## 10. Linguagem causal

Varredura de verbos fortes nos cinco reports não encontrou causalidade material apresentada como fato sem lastro compatível. Ocorrências remanescentes são predominantemente:
- negações;
- variações observadas;
- mecanismos modalizados;
- hipóteses;
- recomendações condicionadas.

**Status: aprovado.**

## 11. Achados menores

Nenhum altera conclusão material:

1. Caderno Geral: pequenas duplicações editoriais de “Unidade/Abrangência/Limitação” em algumas fontes/legendas.
2. `Origem_dados` v029 traz RAIS 2025 como referência geral, enquanto o report também usa RAIS 2024 em análises específicas; os textos distinguem corretamente os anos, mas o registro-mestre pode separar usos.
3. Algumas bases setoriais mantêm referências legadas a “Caderno-Base v016” em colunas de proveniência. São linhagem histórica, não governança corrente.
4. Expressão editorial de fronteira “nó de passagem e conexão em escala muito superior à sua população” pode ser tornada ainda mais precisa, embora esteja corretamente limitada no contexto.
5. Gráfico POM AFS com legenda duplicada permanece bloqueado, como deve.

## 12. Veredito

**APROVADO — FIDELIDADE MATERIAL CONFIRMADA, SEM CORREÇÃO NUMÉRICA OU INTERPRETATIVA CENTRAL NECESSÁRIA NESTE MOMENTO.**

A fidelidade foi confirmada em quatro níveis:

1. **Numérico** — valores centrais conferem.
2. **Aritmético** — fórmulas/percentuais críticos rechecados.
3. **Conceitual** — unidade, período, geografia e universo preservados.
4. **Inferencial** — qualitativo ≠ prevalência; survey descritivo ≠ população; cadastro ≠ share; REGIC ≠ gasto; contrato ≠ pagamento; circulação ≠ consumo; correlação ≠ causalidade.

Reabrir apenas diante de nova evidência material, contradição fonte×texto, erro aritmético, erro de unidade/período/geografia, mudança metodológica oficial, inconsistência cruzada ou solicitação explícita.

## 13. Governança

- v028: READ-ONLY.
- v029: base técnica corrente.
- PR #41: manter aberto, draft e sem merge.
- Esta auditoria não altera os cinco reports; documenta a confirmação de fidelidade e alertas menores.
