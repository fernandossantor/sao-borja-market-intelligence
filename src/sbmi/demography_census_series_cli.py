"""CLI da captura censitária de sexo, idade, situação e cor/raça."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.demography_census_series import collect_demography_census_series

AGE_GROUPS = "1140,1141,1142,1143,1144,1145,1146,1147,1148,1149,1150,1151,1152,1153,1154,1155,6802,6803,92963,92964,92965"  # noqa: E501
QUERIES = (
    {
        "query_id": "census_age_sex_1991_2010",
        "table_id": "200",
        "years": ("1991", "2000", "2010"),
        "variable_ids": ("93", "1000093"),
        "expected_rows": 378,
        "url": f"https://apisidra.ibge.gov.br/values/t/200/n6/4318002/p/1991,2000,2010/v/93,1000093/c2/0,4,5/c1/0/c58/{AGE_GROUPS}",
        "comparability_note": "Tabela de amostra; não equiparar automaticamente às tabelas do universo de 2022.",  # noqa: E501
    },
    {
        "query_id": "census_sex_situation_1991_2010",
        "table_id": "202",
        "years": ("1991", "2000", "2010"),
        "variable_ids": ("93", "1000093"),
        "expected_rows": 54,
        "url": "https://apisidra.ibge.gov.br/values/t/202/n6/4318002/p/1991,2000,2010/v/93,1000093/c2/0,4,5/c1/0,1,2",
        "comparability_note": "Preservar os cruzamentos de sexo e situação publicados pelo SIDRA.",
    },
    {
        "query_id": "census_race_sex_2010_2022",
        "table_id": "9606",
        "years": ("2010", "2022"),
        "variable_ids": ("93", "1000093"),
        "expected_rows": 60,
        "url": "https://apisidra.ibge.gov.br/values/t/9606/n6/4318002/p/2010,2022/v/93,1000093/c86/2776,2777,2778,2779,2780/c2/6794,4,5/c287/100362",
        "comparability_note": "Cor ou raça disponível nesta seleção apenas em 2010 e 2022; observar notas metodológicas.",  # noqa: E501
    },
)


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    execution_id = f"demography-census-series-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"
    roots = {
        layer: Path(path)
        for layer, path in {
            "raw": ".data/snapshots/web/demography_census_series",
            "staging": ".data/staging/base_territorial/demography_census_series",
            "curated": ".data/curated/base_territorial/demography_census_series",
            "exports": ".data/exports/base_territorial/demography_census_series",
            "audit": ".data/audit/base_territorial/demography_census_series",
        }.items()
    }
    with requests.Session() as session:
        result = collect_demography_census_series(
            session, queries=QUERIES, roots=roots, execution_id=execution_id
        )
    print(
        f"execution_id={execution_id}\nrows={len(result.values)}\nraw={result.paths['raw']}\naudit={result.paths['audit']}"
    )


if __name__ == "__main__":
    main()
