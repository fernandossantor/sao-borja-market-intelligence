"""CLI da captura histórica de valores agropecuários do SIDRA."""

from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.sidra_historical_values import collect_sidra_historical_values


def main() -> None:
    timestamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    execution_id = f"sidra-historical-values-{timestamp}"
    plan = Path(
        ".data/audit/base_territorial/sidra_historical_discovery/"
        "sidra-historical-discovery-20260729-193028/sidra_historical_query_plan.csv"
    )
    with requests.Session() as session:
        result = collect_sidra_historical_values(
            session,
            query_plan_path=plan,
            snapshot_root=Path(".data/snapshots/web/sidra_historical_values"),
            staging_root=Path(".data/staging/base_territorial/sidra_historical_values"),
            curated_root=Path(".data/curated/base_territorial/sidra_historical_values"),
            export_root=Path(".data/exports/base_territorial/sidra_historical_values"),
            audit_root=Path(".data/audit/base_territorial/sidra_historical_values"),
            execution_id=execution_id,
        )
    print(f"execution_id={execution_id}")
    print(f"rows={len(result.curated)}")
    print(f"snapshot={result.snapshot_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
