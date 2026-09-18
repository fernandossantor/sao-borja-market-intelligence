# Radar do Mercado — protocolo de ingestão dos Dados Abertos

**Versão:** v001  
**Data:** 2026-09-18  
**Status:** exploratório — não canônico  
**Branch:** `explore/receita-estadual-rs-market-intel-v1`

## Objetivo

Preparar uma ingestão reproduzível dos CSVs que a NT CIET 05/2026 documenta na página **Dados Abertos** do Radar de Mercado.

Este protocolo não cria nem altera base canônica.

## Bases documentadas pela NT

1. Saídas por Setor;
2. Exportações por NCM;
3. Composição de Mercado;
4. Importações por NCM;
5. Portfólio de NCMs por Setor;
6. Categorias de Produtos.

## Cesta piloto

O módulo filtra apenas:

- 10062010;
- 10062020;
- 10063011;
- 10063019;
- 10063021;
- 10063029;
- 10064000.

## Procedimento

Depois de obter os arquivos públicos, armazená-los fora das camadas canônicas, preferencialmente em uma pasta de entrada exploratória.

Executar:

```bash
python -m sbmi.radar_open_data_cli \
  --source-dir <pasta-dos-csvs> \
  --execution-id radar-open-data-YYYYMMDD-HHMMSS
```

Saída padrão:

`.data/audit/receita_rs/radar_open_data/<execution-id>/`

Arquivos produzidos:

- `schema_inventory.csv` — nome, hash SHA-256, encoding, tamanho lógico, colunas e mapeamentos reconhecidos;
- `rice_ncm_matches.csv` — todas as linhas brutas que correspondam aos sete NCMs;
- `rice_composition_summary.csv` — resumo INT/OUF/EXT, demanda e Part.RS **somente quando o schema permitir mapear esses campos com segurança**;
- `validation.csv` — verificações da execução;
- `limitations.csv` — schemas ou campos que não puderam ser interpretados sem inferência.

## Regras de não-inferência

O módulo não tenta adivinhar a estrutura real de um CSV desconhecido.

Quando não identifica:
- coluna NCM; ou
- INT/OUF/EXT em formato largo; ou
- tipo de origem + valor em formato longo,

o cálculo é bloqueado e a limitação é registrada.

Nenhum market share é criado a partir de campos desconhecidos.

## Fórmula permitida

Quando os dados necessários forem inequivocamente identificados:

`Part.RS = INT / (INT + OUF + EXT)`

Classificação oficial da NT CIET 05/2026:
- crítica: Part.RS < 5%;
- alta: 5% ≤ Part.RS < 15%;
- média: 15% ≤ Part.RS < 30%;
- acima desse limite o módulo registra `FORA_DAS_FAIXAS_NT`, sem inventar uma quarta categoria.

## Testes

Foram preparados testes sintéticos para:
- composição em formato largo;
- composição em formato longo;
- filtragem de exportações por NCM sem fabricar market share;
- bloqueio quando o schema de composição não é interpretável.

Em execução local controlada na preparação desta versão: **4 testes aprovados**.

## Pendência operacional

O pipeline está pronto, mas os CSVs públicos reais ainda não foram obtidos por uma rota reproduzível no ambiente de auditoria.

Foi também preparado `.github/workflows/radar-open-data-discovery.yml` para tentar capturar os downloads públicos pelo navegador automatizado. O push efetuado pelo conector não disparou GitHub Actions, portanto esse caminho permanece preparado, mas não executado.

## Critério de promoção futura

Mesmo após extração bem-sucedida, os resultados permanecem exploratórios até:
1. schema auditado;
2. período/unidade confirmados;
3. conciliação das somas com o painel ou documentação;
4. validação dos sete NCMs;
5. decisão explícita de promoção.
