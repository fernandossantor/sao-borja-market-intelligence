# Compras públicas — auditoria de publicação dos resultados PE34, PE39 e PE44 — 2026 — v002

## 1. Objetivo

Esta versão complementa a v001 e distingue duas situações que não podem ser tratadas como equivalentes:

1. **resultado não capturado pelo SBMI**;
2. **fonte secundária atual informa que o resultado ainda não foi publicado**.

A distinção evita transformar uma limitação de acesso em inferência sobre participação, homologação ou ausência de competição.

Data da verificação: **20/09/2026**.

## 2. PE 39/2026 — materiais elétricos

### Evidência observada

A página municipal continua expondo o edital/fase preparatória, objeto, critério e data da sessão.

Fonte oficial:
https://antigo.saoborja.rs.gov.br/index.php/licitacoes-e-contratos/itemlist/category/25-pregao-eletronico

Um indexador secundário consultado em 20/09/2026, com rastreamento recente, informa explicitamente:

> “O resultado deste edital ainda não foi publicado.”

O mesmo indexador reproduz **86 itens** do certame e o valor estimado de R$ 1.074.671,14.

Fonte secundária:
https://mabus.com.br/licitacao/3630558/pregao-eletronico-municipio-de-sao-borja-sao-borja-rs

### Classificação

- prazo de propostas encerrado: **SIM**;
- resultado capturado pelo SBMI: **NÃO**;
- publicação de resultado segundo o indexador secundário consultado: **NÃO PUBLICADO**;
- homologação: **NÃO DEMONSTRADA**.

**Status controlado:** `PRAZO_ENCERRADO_RESULTADO_NAO_PUBLICADO_EM_INDEXADOR_SECUNDARIO`.

### Implicação

A falta de vencedor/preço não deve ser tratada como falha de busca resolvível por coleta ampla. Há evidência de possível **latência de publicação**.

O SBMI deve preservar a estrutura dos 86 itens e aguardar/consultar fontes oficiais de resultado, sem preencher vencedor por inferência.

## 3. PE 44/2026 — CBUQ e emulsão

### Evidência observada

A Prefeitura confirma o edital e a sessão de 19/08/2026.

Fonte oficial:
https://antigo.saoborja.rs.gov.br/index.php/licitacoes-e-contratos/itemlist/category/25-pregao-eletronico

Dois indexadores secundários apresentam o certame como “encerrado”, mas esse rótulo está associado ao encerramento do prazo de propostas.

Um indexador secundário consultado em 20/09/2026 informa explicitamente:

> “O resultado deste edital ainda não foi publicado.”

Fonte secundária:
https://mabus.com.br/licitacao/4550465/pregao-eletronico-municipio-de-sao-borja-sao-borja-rs

Outro espelho exibe “Encerrada” e os dois itens/quantidades, mas não expõe vencedor nem preço homologado.

Fonte secundária PNCP:
https://www.todaslicitacoes.com.br/licitacao/portal-de-compras-publicas-registro-de-precos-para-sao-borja-rs-88489786000101-2026-158

### Correção de leitura

**“Encerrada” não deve ser traduzida como “homologada”.**

No contexto das páginas consultadas, o rótulo é compatível com o fim do recebimento/disputa. Sem resultado, ata ou homologação oficial, o estado correto é:

`PRAZO/DISPUTA_ENCERRADO_RESULTADO_NAO_PUBLICADO_EM_INDEXADOR_SECUNDARIO`.

A expressão anterior “disputa encerrada no espelho” continua descritivamente válida, mas **não é evidência de adjudicação/homologação**.

## 4. PE 34/2026 — medicamentos

A Prefeitura confirma edital e sessão. Indexadores confirmam metadados do certame.

Nesta rodada, porém, não foi localizada fonte que declare explicitamente “resultado não publicado”.

Portanto, o controle permanece mais conservador:

- resultado capturado: **NÃO**;
- publicação do resultado: **NÃO DETERMINADA**;
- homologação: **NÃO DEMONSTRADA**.

**Status:** `RESULTADO_NAO_CAPTURADO_PUBLICACAO_INDETERMINADA`.

Não transportar para PE34 a conclusão documental obtida em PE39/PE44.

## 5. Consequência metodológica

Para o SBMI há agora três estados distintos:

1. `RESULTADO_CAPTURADO`;
2. `RESULTADO_NAO_CAPTURADO_PUBLICACAO_INDETERMINADA`;
3. `RESULTADO_NAO_PUBLICADO_EM_INDEXADOR_SECUNDARIO`.

A terceira categoria continua sendo evidência secundária e pode ser superada por publicação oficial posterior.

## 6. Decisão operacional

Não ampliar buscas genericamente.

Para PE39 e PE44:

1. manter verificação dirigida em Portal de Compras Públicas, PNCP, Diário Oficial de São Borja e extratos de ARP;
2. se resultado oficial não aparecer, preservar o bloqueio documental;
3. prosseguir analiticamente com **estrutura de itens, requisitos e oferta local**, sem atribuir vencedores.

Para PE34:

1. manter tentativa dirigida de recuperar ata/resultado;
2. não afirmar ainda que o resultado não foi publicado;
3. não recorrer a pesquisa primária enquanto o documento oficial não estiver resolvido ou formalmente indisponível.

## 7. Governança

- Caderno-Base v028: **read-only**;
- PR #41: **aberto, draft e sem merge**;
- branch: `explore/receita-estadual-rs-market-intel-v1`;
- nenhuma fonte secundária substitui ata, homologação ou resultado oficial.
