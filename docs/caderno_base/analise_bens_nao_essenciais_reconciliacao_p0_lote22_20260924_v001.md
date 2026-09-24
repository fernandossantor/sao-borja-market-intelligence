# Bens não essenciais — reconciliação final P0 — lote 22 — 24/09/2026

## 1. Objeto

Quarto lote de resolução da fila P0. O foco foi fechar registros cuja permanência no cenário-base exploratório não é sustentada por evidência atual suficiente.

Foram tratados:

- Pimentas Boutique Sensual;
- Loja CHICMI;
- Loja do Ramada;
- Akazzo.

A decisão tomada aqui é **de cenário-base exploratório**, não uma afirmação ontológica de inexistência, fechamento ou informalidade.

Governança preservada:

- branch `explore/receita-estadual-rs-market-intel-v1`;
- PR #41 aberto, draft e sem merge;
- Caderno-Base v028 read-only.

## 2. Critério aplicado

Quando uma linha do inventário:

- não possui CNPJ/identidade jurídica confirmada;
- não apresenta presença operacional recente verificável;
- e não possui outra evidência atual independente,

ela deixa de bloquear o cenário-base e passa para uma camada de **histórico/sensibilidade**.

Isso evita manter indefinidamente no denominador empresas cuja atualidade não pode ser demonstrada, sem concluir que estejam necessariamente fechadas.

## 3. Pimentas Boutique Sensual — linha 120

Nova rodada de busca por:

- CNPJ `28.597.654/0001-63`;
- marca;
- titular;
- combinações locais;

não produziu evidência atual suficientemente específica.

### Decisão provisória

- excluir do cenário-base exploratório;
- preservar o registro na trilha histórica;
- manter possibilidade de reinclusão se surgir evidência independente.

## 4. Loja CHICMI — linha 125

Buscas repetidas por nome exato, variações de grafia e combinações com São Borja/CNPJ/empresa permanecem inconclusivas.

### Decisão provisória

- excluir do cenário-base exploratório;
- preservar a linha como pendência histórica;
- reabrir somente com fonte local, fiscal, cadastral ou de primeira parte.

## 5. Loja do Ramada — linha 126

A marca foi confirmada apenas por listagem histórica de conveniados de São Borja.

Não foi localizada:

- presença operacional atual;
- razão social;
- CNPJ;
- fonte empresarial recente.

### Decisão provisória

- classificar como registro histórico;
- excluir do cenário-base corrente.

## 6. Akazzo — linha 154

Buscas por Akazzo + São Borja + calçados/CNPJ/loja não localizaram fonte local específica.

Resultados homônimos de outros estados foram descartados.

### Decisão provisória

- excluir do cenário-base exploratório;
- preservar a linha na camada histórica/pendente.

## 7. Resultado do lote

Os quatro registros deixam de ser P0.

Após o lote 22, resta **apenas um P0**:

- linha 122 — 7 Povos Kids — conflito cadastral ativa × baixada.

Os demais bloqueios capazes de alterar o denominador passam a estar concentrados em P1/P2.

## 8. Próxima etapa

Tentar uma última resolução dirigida do P0 de 7 Povos Kids em fonte oficial/estadual inequívoca.

Se a fonte oficial não estiver acessível, preparar dois cenários exploratórios:

- cenário-base sem decisão final do registro;
- cenário de sensibilidade incluindo 7 Povos Kids.

## 9. Artefato

`docs/data_sources/bens_nao_essenciais_reconciliacao_p0_lote22_20260924_v001.csv`
