"""CLI da descoberta histórica de metadados SIDRA."""

from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.sidra_historical_discovery import discover_sidra_historical_metadata


def main():
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    identifier = f"sidra-historical-discovery-{stamp}"
    with requests.Session() as session:
        result = discover_sidra_historical_metadata(
            session,
            snapshots_root=Path(".data/snapshots/web/sidra_historical_metadata"),
            audit_root=Path(".data/audit/base_territorial/sidra_historical_discovery"),
            snapshot_id=identifier,
            run_id=identifier,
        )
    print(f"snapshot_path={result.snapshot_path}")
    print(f"output_path={result.output_path}")
    for row in result.summary.itertuples(index=False):
        print(f"{row.indicator}={row.value}")
    print("drive_writes=0")
    print("status=ok")


if __name__ == "__main__":
    main()
