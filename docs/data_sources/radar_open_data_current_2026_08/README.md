# Radar do Mercado — Dados Abertos — ingestão corrente ago/2026

**Fonte observada:** Receita Estadual/SEFAZ-RS — Radar do Mercado — Dados Abertos.
**Data de atualização exibida no painel:** 11/09/2026 para os arquivos correntes localizados.
**Período principal:** agosto/2026 para Composição de Mercado.
**Abrangência:** Rio Grande do Sul e fluxos INT/OUF/EXT conforme a Nota Técnica CIET 05/2026.
**Natureza:** arquivos oficiais observados; Part.RS e classificação de dependência são cálculos do SBMI sobre os campos oficiais quando o schema permite.

Arquivos baixados diretamente da infraestrutura oficial:
- Categorias_Produtos.csv;
- Portfolio_NCMs_Setor.csv;
- Composicao_de_Mercado_08_2026.csv.

source_manifest.tsv preserva URL, tamanho e SHA-256. Os CSVs brutos não são adicionados ao Git; os resultados compactos de auditoria e o inventário de schema são persistidos.

Fórmula permitida: Part.RS = INT / (INT + OUF + EXT).

Faixas expressamente documentadas na NT CIET 05/2026:
- crítica: Part.RS < 5%;
- alta: 5% <= Part.RS < 15%;
- média: 15% <= Part.RS < 30%.

Valores acima de 30% são marcados pelo pipeline como FORA_DAS_FAIXAS_NT; este marcador não constitui categoria oficial adicional.

**Limitação:** esta execução usa a cesta-piloto auditada de sete NCMs do arroz apenas para validar schema e cálculo. Não define o escopo setorial do projeto nem transforma indicador estadual em demanda municipal.
