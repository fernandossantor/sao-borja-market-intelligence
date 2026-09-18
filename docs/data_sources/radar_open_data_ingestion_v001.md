# Radar do Mercado — protocolo de ingestão dos Dados Abertos

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Preparar uma ingestão reproduzível dos CSVs documentados pela NT CIET 05/2026 na página **Dados Abertos** do Radar de Mercado.

O desenho é **multissetorial**. O arroz permanece apenas como cesta-piloto inicial; a rotina aceita qualquer cesta auditável de NCMs fornecida explicitamente.

Nenhuma execução promove dados para camadas canônicas.

## Bases documentadas pela NT

1. Saídas por Setor;
2. Exportações por NCM;
3. Composição de Mercado;
4. Importações por NCM;
5. Portfólio de NCMs por Setor;
6. Categorias de Produtos.

## Cesta-piloto padrão

Sem parâmetro adicional, o módulo usa os sete NCMs do arroz já auditados.

Essa cesta serve para validar:
- schema;
- granularidade;
- fórmula de Part.RS;
- classificação de dependência;
- fluxos OUF/EXT.

Ela **não define o escopo analítico do SBMI**.

## Cestas multissetoriais

Para qualquer outro setor/cadeia, criar um CSV com:

```csv
ncm,descricao
XXXXXXXX,Descrição auditada do produto
YYYYYYYY,Descrição auditada do produto
```

A classificação deve vir de fonte oficial compatível, como NCM/CLASSIF ou tabela oficial utilizada pelo projeto. Não inventar agrupamentos sem documentação.

## Execução

### Piloto padrão do arroz

```bash
python -m sbmi.radar_open_data_cli \
  --source-dir <pasta-dos-csvs> \
  --execution-id radar-open-data-YYYYMMDD-HHMMSS
```

### Cesta própria

```bash
python -m sbmi.radar_open_data_cli \
  --source-dir <pasta-dos-csvs> \
  --basket-file <cesta_ncm.csv> \
  --basket-name <nome_da_cesta> \
  --execution-id radar-open-data-YYYYMMDD-HHMMSS
```

## Saída padrão

`.data/audit/receita_rs/radar_open_data/<execution-id>/`

Arquivos:
- `schema_inventory.csv`;
- `ncm_basket.csv`;
- `ncm_matches.csv`;
- `composition_summary.csv`;
- `validation.csv`;
- `limitations.csv`.

Quando a cesta padrão do arroz é usada, são mantidos também aliases de compatibilidade:
- `rice_ncm_matches.csv`;
- `rice_composition_summary.csv`.

## Regras de não-inferência

O módulo não tenta adivinhar a estrutura de um CSV desconhecido.

Só calcula composição quando identifica inequivocamente:
- coluna NCM; e
- INT/OUF/EXT em formato largo;

ou:
- coluna NCM;
- tipo de origem;
- valor;
- categorias INT, OUF e EXT.

Quando o schema não satisfaz essas condições, nenhum market share é produzido.

## Fórmula permitida

`Part.RS = INT / (INT + OUF + EXT)`

Classificação da NT CIET 05/2026:
- crítica: Part.RS < 5%;
- alta: 5% ≤ Part.RS < 15%;
- média: 15% ≤ Part.RS < 30%.

Acima de 30%, o código registra `FORA_DAS_FAIXAS_NT`. Isso **não é uma quarta categoria oficial**; é apenas um marcador de que a observação não pertence às três faixas expressamente nomeadas na NT.

## Testes preparados

A suíte cobre:
1. composição em formato largo;
2. composição em formato longo;
3. arquivo de exportações filtrado sem fabricar market share;
4. bloqueio para schema de composição não interpretável;
5. cesta customizada de NCM fora do arroz.

A execução da suíte deve ser refeita no ambiente local/CI após cada alteração.

## Próximas cestas analíticas

A seleção deve partir das perguntas territoriais, e não de uma tentativa de varrer indiscriminadamente toda a NCM.

Candidatas:
- agroindústrias e alimentos;
- saúde/higiene e cuidados;
- categorias de bens essenciais;
- cadeias de bens não essenciais com relevância local;
- produtos associados a atividades industriais locais relevantes.

Cada cesta exige:
1. regra de seleção documentada;
2. relação CNAE/NCM quando pertinente;
3. fonte oficial de classificação;
4. justificativa mercadológica;
5. registro de itens incluídos/excluídos.

## Pendência operacional

Os CSVs públicos reais ainda precisam ser obtidos por rota reproduzível.

O workflow `.github/workflows/radar-open-data-discovery.yml` permanece preparado para descoberta automatizada, mas ainda não foi executado pelo GitHub Actions.

## Critério de promoção futura

Mesmo após extração bem-sucedida, os resultados permanecem exploratórios até:
1. schema auditado;
2. período/unidade confirmados;
3. conciliação das somas com painel/documentação;
4. validação da cesta;
5. decisão explícita de promoção.
