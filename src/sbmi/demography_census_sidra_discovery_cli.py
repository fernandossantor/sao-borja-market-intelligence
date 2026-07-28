"""CLI da descoberta de metadados censitários no SIDRA."""

from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.demography_census_sidra_discovery import discover_sidra_metadata


def main():
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    ident = f"sidra-metadata-discovery-{stamp}"
    with requests.Session() as session:
        result = discover_sidra_metadata(
            session,
            snapshots_root=Path(".data/snapshots/web/demography_census_sidra_metadata"),
            audit_root=Path(".data/audit/base_territorial/demography_census_sidra_discovery"),
            snapshot_id=ident,
            run_id=ident,
        )
    print(f"snapshot_path={result.snapshot_path}")
    print(f"output_path={result.output_path}")
    for row in result.summary.itertuples(index=False):
        print(f"{row.indicator}={row.value}")
    print("downloads_performed=0\nstatus=ok")


if __name__ == "__main__":
    main()
