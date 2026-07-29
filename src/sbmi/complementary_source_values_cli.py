"""CLI da coleta auditável das quatro fontes complementares."""

from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.complementary_source_values import collect_complementary_source_values


def main() -> None:
    execution_id = f"complementary-source-values-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    with requests.Session() as session:
        result = collect_complementary_source_values(
            session,
            sebrae_plan_path=Path(
                ".data/audit/base_territorial/complementary_sources/"
                "complementary-source-inventory-20260729-204156/"
                "candidate_query_inventory.csv"
            ),
            snapshot_root=Path(".data/snapshots/web/complementary_source_values"),
            staging_root=Path(".data/staging/base_territorial/complementary_source_values"),
            curated_root=Path(".data/curated/base_territorial/complementary_source_values"),
            export_root=Path(".data/exports/base_territorial/complementary_source_values"),
            audit_root=Path(".data/audit/base_territorial/complementary_source_values"),
            execution_id=execution_id,
        )
    print(f"execution_id={execution_id}")
    print(f"sources={result.manifest.source_id.nunique()}")
    print(f"queries={len(result.manifest)}")
    print(f"rows={len(result.values)}")
    print(f"snapshot={result.snapshot_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
