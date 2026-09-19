# São Borja — diagnóstico técnico da rota histórica de despesas — 2019–2026

**Fonte:** Portal da Transparência da Prefeitura de São Borja.
**Abrangência geográfica:** município de São Borja/RS.
**Período testado:** exercícios de 2019 a 2026.
**Natureza:** auditoria técnica da rota, não série fiscal substantiva.

O teste compara quatro variantes de `dtDataImportacao` para cada exercício:
data corrente de importação informada pelo portal, fim do próprio exercício,
início do próprio exercício e parâmetro vazio.

O objetivo é distinguir falha de parametrização/endpoint de ausência de dados.
Nenhum detalhe de CPF/CNPJ/credor é persistido nesta camada; respostas não JSON
têm números e e-mails redigidos antes do registro.

**Regra:** falha de endpoint não equivale a ausência de dados históricos.
