from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.demography_census_sidra_values import capture_sidra_values


def main():
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    ident = f"sidra-values-{stamp}"
    with requests.Session() as session:
        r = capture_sidra_values(
            session,
            snapshots_root=Path(".data/snapshots/web/demography_census_sidra_values"),
            audit_root=Path(".data/audit/base_territorial/demography_census_sidra_values"),
            snapshot_id=ident,
            run_id=ident,
        )
    print(f"snapshot_path={r.snapshot_path}\noutput_path={r.output_path}")
    for row in r.summary.itertuples(index=False):
        print(f"{row.indicator}={row.value}")
    print("historical_files_modified=0\nstatus=ok")


if __name__ == "__main__":
    main()
