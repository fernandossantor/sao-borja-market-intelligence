# Auditoria pré-publicação — cinco cadernos — v001 — 2026-09-27

## Escopo

Auditoria de coerência, fidelidade à base, cálculos, raciocínios, conclusões e rastreabilidade dos cinco cadernos correntes de publicação:

- Caderno Geral v008 — Drive `1E-yRiQlE_YUgrv-qy3dqCceX1rq4PhvCF0xklWLM5Co`
- Bens Essenciais v006 — Drive `1ctUB-OYxQp1L90tIdoSjOp6Uf2_k8jIekZMnRzEZ3po`
- Saúde/Higiene v006 — Drive `17fa2arlqa9UrwuEyf8r86WS5GmO1hEI_eiD21txKAaE`
- Bens Não Essenciais v006 — Drive `1hgUYwKRV7XD6jMEWA-M52Ah15sXB8LpDHExauLlDzK0`
- Alimentação Fora do Lar e Serviços v006 — Drive `1Rk6Zx3NqoKortoEG8mVvMHx-a_NVry-5EnoygHKFojg`

Baseline: Caderno-Base Territorial v029 + planilha técnica v029 + Registro Metodológico v029. A auditoria não reabre a v029 e não cria v030.

## Resultado

**PASS FINAL — DOCS PUBLICÁVEIS.**

Não foi identificado erro crítico em:
- números centrais;
- fórmulas centrais;
- amostras e desenhos POM;
- distinção observado/calculado/estimado/benchmark/interpretação;
- controles de market share;
- REGIC;
- DFe/Cesta/Radar;
- contratos × pagamentos;
- escalas municipal/COREDE/RS;
- causalidade.

## Verificações principais

### Caderno Geral v008

PASS substantivo.

Âncoras confrontadas: demografia 1991–2025; renda Censo 2022; RAIS 2024; VAB × emprego 2021; fluxos públicos; fronteira; headlines setoriais; DFe/Cesta/Radar.

**Correção conceitual obrigatória:** no contraste de 2021, o valor de **54,46% do VAB** corresponde ao **terciário amplo, incluindo comércio, serviços e administração pública**. A redação abreviada “comércio e serviços” é conceitualmente imprecisa, embora o número esteja correto.

### Bens Essenciais v006

PASS substantivo.

- POM: 12 entrevistas em profundidade, 24/06/2026, 28 questões.
- Demanda modelada: R$ 19.558.852,34/mês e R$ 234.706.228,14/ano.
- Fórmula reproduzida: `61.311 × (487 / 2,72) × 1,781742384675 × 12`.
- 52/54 = 96,30% preservado como maturidade documental, não cobertura.
- DFe/Cesta/Radar usados como sinais, sem recalibração automática do modelo.

### Saúde/Higiene v006

PASS substantivo.

- POM: 12 entrevistas, 03–10/07/2026, predominantemente Google Meet.
- CNES: 23 registros; 7 raízes; 4 multiunidade; 20/23 = 86,96%; maior raiz 8/23 = 34,78%.
- CNES explicitamente não exaustivo e não convertido em market share.
- Radar/RS +16,12% preservado como benchmark estadual.

A versão de publicação corrige adequadamente a força excessiva da formulação de “supremacia” presente no relatório POM original.

### Bens Não Essenciais v006

PASS substantivo.

- POM: 10 entrevistas semiestruturadas presenciais.
- 122 storefronts base; 121 sensibilidade; 109 operator_keys.
- 21/122 = 17,21% em raízes multiunidade.
- Moda = 57/122 = 46,72%; pet/vet/agro = 20/122 = 16,39%.
- REGIC direta = 64/122 = 52,46%.
- 120→122 não é tratado como crescimento.
- Radar/RS -2,97% não é promovido a retração municipal.

A versão corrente converte adequadamente afirmações fortes do POM original em hipóteses/mecanismos qualitativos.

### Alimentação Fora do Lar e Serviços v006

PASS substantivo.

- Survey n=153, residentes 18+, 22/06–06/07/2026.
- Relatório original declara 90% de confiança e 6,62% de erro, mas não documenta seleção probabilística suficiente.
- Versão corrente trata percentuais como **descritivos da amostra**.
- Principais percentuais POM conferidos.
- 947 SINAC / 728 SIMEI.
- Salões+oficinas = 74,23% SINAC / 86,68% SIMEI.
- CNAE 56 = 409.
- PNAE: R$ 869.843,54 no universo CNPJ auditado; R$ 327.021,02 locais = 37,60%.
- Serviços/ADJACENT +6,48% explicitamente não representa prestação de serviços.

## Ajustes obrigatórios antes da publicação

### A1 — Referências das séries públicas
**Severidade: média / bloqueadora de publicação.**

Os cinco cadernos usam DFe, Cesta Alimentos e/ou Radar do Mercado no corpo analítico, mas as seções finais de Referências não listam explicitamente esses produtos da Receita Estadual/SEFAZ-RS.

**Ação:** incluir referência com produto, período, geografia e uso.

### A2 — Tabelas/apêndices de sustentação das séries recentes
**Severidade: média / bloqueadora de publicação.**

Os apêndices/tabelas de sustentação foram montados antes da última integração e não contêm os novos valores DFe/Cesta/Radar que agora sustentam argumentos.

**Ação:** incluir quadro com indicador, período, geografia, valor, natureza e limitação.

### A3 — Rótulo do VAB terciário no Caderno Geral
**Severidade: média / correção conceitual.**

Trocar redação equivalente a “comércio e serviços = 54,46% do VAB” por “terciário amplo — comércio, serviços e administração pública = 54,46% do VAB”.

### A4 — Higiene de versionamento
**Severidade: baixa / obrigatória para versão final.**

Atualizar referências internas que ainda usam o título de trabalho “Caderno-Base Territorial v029 — integração setorial v002” para o título final congelado:
**Caderno-Base Territorial — São Borja — v029 — congelamento — 20260927**.

## Pontos não bloqueadores

- Preferir “pode/tende/é necessário testar” a formulações normativas absolutas quando não houver obrigação regulatória.
- Evitar comparativos de intensidade (“mais por missão do que por categoria”) quando a base não mensura a magnitude relativa.

## O que não precisa ser refeito

Não é necessário recalcular:
- demanda de Bens Essenciais;
- CNES;
- oferta BNE;
- survey AFS;
- DFe/Cesta/Radar;
- taxonomia Radar.

Não é necessário reabrir a v029 nem executar pesquisa primária.

## Decisão

O conjunto é **substantivamente coerente e fiel à base**. Não há erro crítico identificado.

**A1–A4 foram remediados nos cinco Google Docs e a conferência textual pontual foi concluída. O conjunto está liberado para publicação em formato Doc.**

## Governança

PR #41 deve permanecer **open / draft / unmerged**.

Nenhum merge, retarget ou fechamento está autorizado.


## Remediação concluída — 27/09/2026

### A1 — resolvido
Foram inseridas referências oficiais da Receita Estadual/SEFAZ-RS para Documentos Eletrônicos/DFe, Preços Dinâmicos da Receita Estadual e Radar do Mercado, conforme o uso efetivo em cada caderno.

### A2 — resolvido
Os cinco cadernos receberam, na metodologia, um **Quadro de sustentação — séries públicas recentes** com indicador, período, geografia, resultado, natureza e limitação.

### A3 — resolvido
No Caderno Geral v008, o rótulo de 54,46% do VAB de 2021 foi corrigido para **terciário amplo — comércio, serviços e administração pública**. O valor numérico permaneceu inalterado.

### A4 — resolvido
As referências bibliográficas passaram a usar o título final **Caderno-Base Territorial — São Borja — v029 — congelamento — 20260927**. A variante remanescente no Caderno Geral também foi saneada, assim como o título do Registro Metodológico.

## Uso de inteligência artificial generativa

Foi incluída nos cinco cadernos uma subseção metodológica específica.

- Ferramenta: ChatGPT.
- Modelo: GPT-5.6 Sol.
- Proprietário/desenvolvedor: OpenAI.
- Referência temporal: 27/09/2026.

A IAG foi utilizada para organização e confronto de evidências, apoio à verificação aritmética e de consistência, teste de cadeias argumentativas, redação/revisão editorial, documentação e rastreabilidade. Não foi tratada como fonte empírica ou bibliográfica, não autorizou a criação de números, categorias ou séries, e não substituiu a validação humana.

A reprodutibilidade permanece ancorada nas fontes, planilhas, scripts, arquivos, commits e regras versionadas, e não na reprodução literal de respostas generativas.

Referência oficial:
OPENAI. GPT-5.6: inteligência de fronteira que acompanha a sua ambição. 9 jul. 2026. https://openai.com/pt-BR/index/gpt-5-6/. Acesso em: 27 set. 2026.

## Estado pós-remediação

- A1–A4: **RESOLVIDOS**.
- Transparência sobre IAG: **INCORPORADA**.
- QA textual pontual: **PASS**.
- PDFs: **não gerados**, conforme solicitação do usuário.
- Caderno-Base v029: **permanece congelado**.
- v030: **não criada**.
- PR #41: **open / draft / unmerged**.
