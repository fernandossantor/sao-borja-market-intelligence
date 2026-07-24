# Encerramento da auditoria de estabilização

Data de encerramento técnico: 24 de julho de 2026.

## 1. Objeto

A auditoria de estabilização teve como objeto a organização técnica do projeto São Borja — Inteligência Mercadológica, a preservação do acervo histórico, a validação da pasta `raw/new_files` e a verificação dos produtos derivados existentes em `processed`, `exports` e `warehouse`.

Não foi objetivo desta fase validar integralmente o mérito substantivo de cada indicador, reconstruir todos os builders históricos ou publicar dados no Supabase.

## 2. Dados observados

### 2.1 Inventário do Google Drive

- 1.127 entradas;
- 40 pastas;
- 1.087 arquivos;
- 2.042.029.593 bytes com tamanho informado;
- 1.083 arquivos com SHA-256 disponível;
- 15 grupos de duplicidade física exata no acervo total;
- acesso somente leitura pela Google Drive API.

### 2.2 Auditoria de `raw/new_files`

- 34 arquivos;
- 590.693 bytes;
- 29 arquivos federais, 3 municipais e 2 estaduais;
- 34 arquivos únicos por SHA-256 em relação ao inventário;
- 1 par federal com conteúdo normalizado idêntico, mas binário diferente;
- 1 tabela estadual com 10 grupos de linhas estritamente repetidas e 19 ocorrências excedentes;
- nenhuma data futura, ambígua ou não interpretável após revisão por formatos temporais explícitos.

### 2.3 Staging produzido

- 34 tabelas e 8.477 linhas observadas nas fontes;
- 1 arquivo federal de 64 linhas excluído somente do staging por duplicidade integral de conteúdo;
- 8.413 linhas publicadas em 6 datasets Parquet;
- 28 arquivos federais distintos consolidados em 2.038 linhas;
- 3.818 linhas de ICMS preservadas integralmente;
- 29 ocorrências pertencentes aos 10 grupos repetidos do ICMS sinalizadas, sem exclusão;
- 2.505 linhas de transferências estaduais;
- 52 linhas municipais distribuídas em três estruturas;
- validação de contratos, proveniência, tipos, datas, hashes e reconciliação sem erros ou advertências.

### 2.4 Produtos derivados existentes

- 924 arquivos capturados em modo somente leitura;
- 250.125.612 bytes verificados por tamanho e SHA-256;
- 920 arquivos legíveis com conteúdo;
- 3 arquivos vazios;
- 1 arquivo WAL auxiliar;
- 0 erros de leitura;
- 0 formatos não suportados;
- 932 tabelas observadas;
- 4.564.680 linhas observadas;
- 17 famílias de produtos;
- 14 grupos de duplicidade física, com 28 arquivos envolvidos.

## 3. Dados calculados

Excluído o WAL auxiliar, 920 de 923 arquivos analisáveis possuem conteúdo:

```text
920 / 923 = 99,67%
```

Os três arquivos vazios representam:

```text
3 / 923 = 0,33%
```

Os 14 grupos de duplicidade física possuem exatamente dois arquivos em cada grupo.

## 4. Revisão dos arquivos vazios

### 4.1 `exports/fiscal_other_audit.csv`

- 48 bytes;
- estrutura CSV;
- interpretação: provável relatório de auditoria sem ocorrências, contendo somente cabeçalho;
- decisão: preservar; não classificar como falha sem evidência adicional.

### 4.2 Observações do Banco Central

- `processed/202601_aposentados_bacen/202601_Observacoes.parquet`;
- `processed/202601_pensionistas_bacen/202601_Observacoes.parquet`;
- 600 bytes cada;
- conteúdo físico idêntico;
- interpretação: provável estrutura válida sem observações registradas para as duas categorias;
- decisão: preservar; revisar apenas quando essas famílias forem utilizadas analiticamente.

As interpretações acima são hipóteses fundamentadas no nome, tamanho e posição dos arquivos. Não constituem validação do conteúdo de origem.

## 5. Revisão das duplicidades físicas

### 5.1 Arquivos de notas

Foram identificados pares de notas idênticas em `processed/agro` e `processed/rais`. A repetição pode refletir o compartilhamento legítimo de uma mesma nota metodológica entre tabelas relacionadas.

Decisão: preservar e registrar como duplicidade intencional provável.

### 5.2 Layouts da RAIS

Foram identificados onze pares de arquivos com nomes equivalentes, distinguindo-se principalmente pelo marcador `layout2020`.

Interpretação: provável manutenção simultânea de nomes históricos e nomes versionados para o mesmo layout.

Decisão: preservar durante esta estabilização. Em futura catalogação da RAIS, definir um alias canônico sem excluir automaticamente os arquivos históricos.

### 5.3 Observações do Banco Central

O par de arquivos vazios de observações também constitui duplicidade física entre duas famílias.

Decisão: preservar, pois a posição em famílias diferentes mantém significado de proveniência mesmo quando o conteúdo é vazio e idêntico.

## 6. Interpretação da utilidade estrutural

A classificação heurística identificou 77 tabelas com sinais nominais simultâneos de medida e dimensão e deixou 852 tabelas como `STRUCTURED_REVIEW_REQUIRED`.

Essa classificação não representa 852 falhas. Ela é limitada pelos nomes das colunas e pela fragmentação do acervo em séries pequenas, notas, layouts, tabelas anuais e exportações heterogêneas.

As famílias `agro`, `pib`, `rais` e `exports` apresentam grande número de tabelas e múltiplos esquemas, mas foram tecnicamente legíveis e não exibiram erros de formato. Sua utilidade substantiva deve ser avaliada conforme cada pergunta analítica, e não por reprocessamento geral.

## 7. Decisões de governança

1. O conteúdo de `raw` permanece imutável.
2. Nenhum arquivo do Google Drive foi alterado, movido ou excluído.
3. Os produtos existentes em `processed`, `exports` e `warehouse` serão preservados.
4. Duplicidades entre camadas derivadas não serão tratadas automaticamente como erro.
5. Arquivos vazios serão considerados estruturas válidas até que haja evidência de falha de geração.
6. O staging de `raw/new_files` passa a ser a referência técnica para integração futura dos seis novos datasets.
7. Builders históricos serão revisados apenas quando uma família for retomada ou quando uma divergência substantiva for observada.
8. DuckDB permanece como mecanismo local e reconstruível, não como fonte canônica sincronizada.
9. Supabase continua adiado para uma fase posterior de publicação e consulta.

## 8. Limitações

- integridade técnica não comprova correção metodológica;
- legibilidade não comprova completude;
- igualdade estrutural não comprova comparabilidade temporal;
- presença de colunas geográficas, temporais ou quantitativas não comprova unidade ou abrangência corretas;
- não foi realizada validação substantiva de todos os 4.564.680 registros;
- não foi reconstruído o pipeline histórico para comparação linha a linha;
- os três arquivos vazios e os pares de layout permanecem documentados como itens de revisão sob demanda.

## 9. Conclusão

A auditoria de estabilização está encerrada com resultado técnico satisfatório.

Não foi encontrada evidência de corrupção generalizada, perda estrutural ou necessidade de reconstrução completa do acervo. Os riscos remanescentes são localizados, documentados e podem ser tratados quando cada família temática for utilizada.

O projeto está apto a retornar à construção da Base Territorial Comum, à retomada dos builders prioritários e à análise substantiva dos novos datasets auditados.
