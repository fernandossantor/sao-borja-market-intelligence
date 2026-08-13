"""Captura incremental das séries demográficas históricas oficiais do SIDRA."""

import argparse
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory

import pandas as pd
import requests

from sbmi.sidra_historical_values import collect_sidra_historical_values

QUERIES = (
    {
        "query_id": "demography_population_estimates_6579",
        "table_id": "6579",
        "municipality_code": "4318002",
        "period_start": "2001",
        "period_end": "2025",
        "variable_ids": "9324",
        "classification_id": "",
        "category_ids": "",
        "url": "https://apisidra.ibge.gov.br/values/t/6579/n6/4318002/p/all/v/9324",
        "execution_status": "PREPARED_NOT_EXECUTED",
    },
    {
        "query_id": "demography_households_census_156",
        "table_id": "156",
        "municipality_code": "4318002",
        "period_start": "1991",
        "period_end": "2010",
        "variable_ids": "2048,134,619",
        "classification_id": "",
        "category_ids": "",
        "url": "https://apisidra.ibge.gov.br/values/t/156/n6/4318002/p/all/v/2048,134,619",
        "execution_status": "PREPARED_NOT_EXECUTED",
    },
)


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    execution_id = f"demography-historical-values-{timestamp}"
    with TemporaryDirectory(prefix="sbmi-demography-plan-") as temporary:
        plan = Path(temporary) / "demography_query_plan.csv"
        pd.DataFrame(QUERIES).to_csv(plan, index=False)
        with requests.Session() as session:
            result = collect_sidra_historical_values(
                session,
                query_plan_path=plan,
                snapshot_root=Path(".data/snapshots/web/demography_historical_values"),
                staging_root=Path(".data/staging/base_territorial/demography_historical_values"),
                curated_root=Path(".data/curated/base_territorial/demography_historical_values"),
                export_root=Path(".data/exports/base_territorial/demography_historical_values"),
                audit_root=Path(".data/audit/base_territorial/demography_historical_values"),
                execution_id=execution_id,
                timeout_seconds=30,
                max_response_bytes=250_000,
            )
    print(f"execution_id={execution_id}")
    print(f"rows={len(result.curated)}")
    print(f"snapshot={result.snapshot_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
