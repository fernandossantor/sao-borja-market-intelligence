# v026 — complemento de escopo da folha pública: TCE-RS e ALRS

**Data:** 2026-09-12  
**Geografia:** São Borja/RS  
**Relação com a documentação anterior:** este complemento atualiza a fila técnica do arquivo `fluxos_financeiros_agro_folha_outros_poderes_v026.md`: a triagem institucional de TCE-RS e ALRS foi concluída no nível de presença territorial corrente. Nenhum valor foi promovido.

## TCE-RS

**Fontes oficiais consultadas**

- TCE-RS — página de contato/sede e auditorias regionais;
- TCE-RS — notícia de 12/09/2025 sobre os 57 municípios fiscalizados pelo Serviço Regional de Auditoria de Santo Ângelo;
- TCE-RS — Processo Seletivo 01/2026.

**DADO OBSERVADO:** São Borja integra os 57 municípios fiscalizados pelo Serviço Regional de Auditoria de Santo Ângelo. A relação institucional de sede e auditorias regionais não inclui unidade em São Borja. O Processo Seletivo 01/2026 também usa sede e regionais como locais de cadastro reserva, incluindo Santo Ângelo, sem São Borja.

**INTERPRETAÇÃO CONTROLADA:** a relação funcional territorial identificada para São Borja ocorre por meio do Serviço Regional de Santo Ângelo, e não por uma unidade fixa local do TCE-RS.

**STATUS:** **NÃO PROMOVIDO — sem unidade local fixa identificada.**

**LIMITAÇÃO:** ausência de unidade local não demonstra que nenhum servidor resida ou teletrabalhe em São Borja. Residência, lotação e local de exercício são conceitos distintos. Portanto, não se publica “valor zero”.

## ALRS

**Fontes oficiais consultadas**

- Ouvidoria/SIC da Assembleia Legislativa do Estado do Rio Grande do Sul;
- Plataforma de Conhecimento/Escola do Legislativo da ALRS.

**DADO OBSERVADO:** as fontes oficiais consultadas situam SIC/Ouvidoria e atividades de recepção/formação de servidores efetivos em Porto Alegre, incluindo Palácio Farroupilha, Memorial do Legislativo e prédio anexo.

**RESULTADO DA TRIAGEM:** não foi identificada unidade administrativa permanente da ALRS em São Borja e não foi extraída, na pesquisa corrente, fonte remuneratória com campo reproduzível de lotação/local de exercício no município.

**STATUS:** **NÃO PROMOVIDO — territorialização não demonstrada.**

**LIMITAÇÃO:** não é possível concluir valor zero. Assessores parlamentares podem residir ou trabalhar regionalmente fora da sede sem constituir unidade administrativa municipal.

**REGRA DE NÃO INFERÊNCIA:** não usar base política, domicílio eleitoral, notícia, município de origem ou vínculo partidário como proxy de local de exercício.

## Diagnóstico do escopo dos demais poderes/instituições

- **MPRS:** territorialização documental já promovida em etapa anterior.
- **DPERS:** folha oficial estruturada, mas sem campo territorial; quadro local dinâmico e roster mensal completo ainda não obtido. Total local não promovido.
- **TJRS:** folha/API oficiais identificadas; schema territorial ainda não demonstrado. Total local não promovido.
- **TCE-RS:** sem unidade fixa local identificada; São Borja está na área do Serviço Regional de Santo Ângelo. Valor não promovido.
- **ALRS:** centralização administrativa observada em Porto Alegre; presença funcional local não demonstrada. Valor não promovido.

## Prioridade técnica após a triagem

1. **DPERS:** obter ou reconstruir roster mensal completo de julho/2026 e reconciliar com os CSVs oficiais.
2. **TJRS:** extrair schema Swagger por rota alternativa; procurar campos de comarca, foro, unidade ou lotação. Se ausentes, buscar roster oficial mensal do Foro/Comarca de São Borja.
3. **TCE-RS e ALRS:** manter em espera documental e reabrir somente diante de evidência oficial nova de vínculo funcional local.
4. Preservar resultados negativos de auditoria: “não territorializável com segurança” é resultado metodológico válido.

## Artefatos Drive atualizados

- Planilha v026: `1taW8Ha_FSyGWNKYd3aPMjESpEcBhsF7-GJj17s5tBD4`
  - `TCERS_folha_escopo_v026`
  - `ALRS_folha_escopo_v026`
  - `Auditoria_v026` atualizado
- Caderno narrativo v026: `1xCGpLs4K4-Dv520uz3wa9A82h7YeczeMpM5liuVikSo`
  - seção 26.10 adicionada
- Registro metodológico v026: `1fLFJLHaKn1wJUlDHuE-tTNUWxa4P2DP-YV8yTp2Xq9s`
  - triagem TCE-RS/ALRS adicionada

## Governança

PR #41 deve permanecer **aberto, draft e sem merge**.  
Branch: `feature/cnpj-territorial-control-v1`.  
Nenhuma integração à `main` está autorizada.
