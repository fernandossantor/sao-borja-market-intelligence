# Receita Estadual RS — especificação de extração agregada DFe para dimensão de mercado — v001

**Data:** 2026-09-26  
**Geografia-alvo:** São Borja/RS — código IBGE 4318002  
**Fonte administrativa pretendida:** Documentos Fiscais Eletrônicos da Receita Estadual do Rio Grande do Sul  
**Finalidade:** obter faturamento fiscal agregado por setor/categoria sem identificação de contribuintes.  
**Status:** especificação técnica; nenhuma solicitação protocolada nesta etapa.

## 1. Problema

A publicação pública de DFe oferece duas camadas úteis, porém separadas:

- município: `município × modelo DFe × período × valor/quantidade`;
- setor: `COREDE × divisão CNAE × modelo DFe × período × valor/quantidade`.

A auditoria do modelo público não encontrou interseção direta:

`município × CNAE`

nem:

`município × NCM`.

Para dimensionar mercado formal em São Borja sem proxies arbitrários, é necessária uma extração agregada que combine território e categoria econômica.

## 2. Extração mínima — município × CNAE

Solicitar tabela agregada com chave:

`ano-mês × município × modelo DFe × CNAE`.

Campos:

1. ano-mês de emissão;
2. código IBGE do município do emitente;
3. nome do município;
4. modelo do documento fiscal;
5. código CNAE;
6. descrição CNAE;
7. nível da classificação CNAE informado — divisão, grupo, classe ou subclasse;
8. quantidade de DFe;
9. valor total dos DFe;
10. quantidade de contribuintes distintos na célula, exclusivamente para controle de sigilo;
11. indicador de célula suprimida, quando aplicável.

Prioridade geográfica:
- São Borja/RS — 4318002.

Prioridade temporal:
- janeiro/2023 até a última competência fechada disponível de 2026.

Modelos prioritários:
- NFC-e;
- NF-e, preservada separadamente;
- demais modelos somente se metodologicamente justificados.

## 3. Nível CNAE preferencial

A divisão CNAE é útil para contexto, mas insuficiente para três dos cinco mercados do SBMI, porque a divisão 47 — Comércio varejista — agrega simultaneamente alimentação, farmácias, vestuário, móveis, eletrodomésticos e outros varejos.

Ordem de preferência:

1. **classe CNAE**;
2. grupo CNAE;
3. divisão CNAE.

Se a regra de sigilo impedir classe/grupo em células específicas, solicita-se:
- agregação ao nível imediatamente superior; ou
- célula marcada como suprimida.

Não preencher células suprimidas com zero.

## 4. Extração complementar — município × NCM

Para varejos de mix amplo, o CNAE do estabelecimento não identifica necessariamente a categoria do item vendido.

Solicitar, se tecnicamente disponível:

`ano-mês × município × modelo DFe × NCM × quantidade × valor`.

Campos desejados:

1. ano-mês;
2. código/nome do município;
3. modelo DFe;
4. NCM;
5. descrição NCM ou categoria oficial associada;
6. quantidade de itens/unidades, se metodologicamente comparável;
7. valor total dos itens/documentos associados;
8. número de contribuintes distintos na célula;
9. indicador de supressão.

Caso o NCM não esteja disponível em formato agregado, solicitar informação explícita sobre:
- existência da variável nos dados de origem;
- possibilidade de agregação estatística;
- restrições de sigilo/metodologia que impeçam sua divulgação.

## 5. Tratamento fiscal e metodológico solicitado

Para permitir interpretação correta, pedir metadados sobre:

- CFOPs incluídos/excluídos, especialmente na NF-e;
- tratamento de cancelamentos;
- devoluções;
- notas de ajuste/complementares;
- valores negativos;
- substituições;
- data de emissão versus data de autorização;
- regra de associação territorial — município do emitente/estabelecimento;
- eventuais mudanças metodológicas em 2023-2026;
- regra de sigilo estatístico;
- atualização/reprocessamento dos dados.

## 6. Sigilo

O SBMI não necessita de:
- CNPJ;
- CPF;
- razão social;
- nome fantasia;
- endereço individual;
- chave de acesso;
- identificação do consumidor;
- qualquer documento fiscal individual.

Aceita-se a mesma regra de proteção estatística utilizada pela Receita Estadual na publicação aberta — ou regra mais restritiva definida pela administração.

A entrega pode:
- suprimir células com poucos contribuintes;
- agregar CNAE ao nível superior;
- arredondar valores conforme regra institucional;
- omitir categorias residuais quando necessário.

É essencial apenas diferenciar:
- zero econômico observado;
- informação inexistente;
- célula suprimida por sigilo.

## 7. Produtos analíticos permitidos se a extração for obtida

### Faturamento observado setorial formal

Com `São Borja × CNAE × período × valor`, será possível estimar o volume fiscal documentado por perímetro econômico, desde que a cobertura CNAE seja compatível com o setor.

### Alimentação Fora do Lar

Divisão/grupos/classes ligados à alimentação poderão produzir uma camada municipal observada mais próxima do caderno de AFL.

### Bens Essenciais, Saúde/Higiene e Bens Não Essenciais

A simples divisão 47 continuará insuficiente. Classes CNAE ou NCM são preferíveis para separar as arenas.

### Market share

Mesmo com denominador agregado, market share só será calculável para uma empresa se houver numerador monetário da própria operação de São Borja no mesmo:
- período;
- categoria;
- modelo/conceito fiscal;
- território;
- tratamento de cancelamentos/devoluções.

## 8. O que a extração não resolve automaticamente

Mesmo com município × CNAE:

- faturamento fiscal não é demanda residente;
- não identifica residência do consumidor;
- não mede vazamento para outros municípios/e-commerce/Argentina;
- não captura informalidade;
- CNAE do emitente pode misturar produtos de categorias distintas;
- não identifica participação empresarial sem numerador compatível.

## 9. Texto-base do pedido técnico

Solicita-se, para finalidade acadêmica de inteligência mercadológica territorial, exclusivamente em formato agregado e sem identificação de contribuintes ou consumidores, extração dos Documentos Fiscais Eletrônicos emitidos por estabelecimentos localizados em São Borja/RS (IBGE 4318002), para o período de janeiro de 2023 à última competência fechada de 2026, contendo, preferencialmente:

`ano-mês | município | modelo DFe | CNAE classe/grupo/divisão | quantidade de documentos | valor total | número de contribuintes da célula | indicador de supressão`.

Quando tecnicamente disponível e estatisticamente divulgável, solicita-se adicionalmente agregado por NCM/categoria de mercadoria.

Aceita-se aplicação integral das regras de sigilo estatístico da Receita Estadual, inclusive supressão ou agregação de células. Não são solicitados CNPJ, CPF, razão social, chave de documento ou microdados individualizados.

Solicita-se também documentação metodológica mínima sobre CFOPs considerados, cancelamentos/devoluções, regra territorial e mudanças de metodologia no período.

## 10. Rastreabilidade da necessidade

A especificação decorre de três auditorias do SBMI:

1. envelope municipal DFe de São Borja;
2. esquema público Power BI município × setor;
3. benchmark COREDE Fronteira Oeste por divisão CNAE.

Documentos relacionados:
- `dfe_sao_borja_envelope_fiscal_v001_20260926.md`;
- `dfe_powerbi_intersecao_municipio_setor_v001_20260926.md`;
- `dfe_corede_fronteira_oeste_benchmark_setorial_v001_20260926.md`.

## 11. Prioridade

**ALTA.**

Esta é a rota oficial com maior potencial de transformar os atuais benchmarks de demanda residente em uma análise comparável com faturamento fiscal observado por mercado, sem recorrer a CNPJ, lojas, emprego ou outras proxies estruturais.
