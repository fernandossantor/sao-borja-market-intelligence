"""CLI do inventário de consultas complementares."""

from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.complementary_source_inventory import build_complementary_source_inventory


def main() -> None:
    execution_id = f"complementary-source-inventory-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    with requests.Session() as session:
        result = build_complementary_source_inventory(
            session,
            snapshot_root=Path(".data/snapshots/web/complementary_sources"),
            audit_root=Path(".data/audit/base_territorial/complementary_sources"),
            execution_id=execution_id,
        )
    print(f"execution_id={execution_id}")
    print(f"query_candidates={len(result.queries)}")
    print(f"distinct_cubes={result.queries['cube'].nunique()}")
    print(f"snapshot={result.snapshot_path}")
    print(f"audit={result.output_path}")


if __name__ == "__main__":
    main()
