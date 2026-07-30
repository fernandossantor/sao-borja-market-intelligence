"""CLI do snapshot piloto de recursos públicos estaduais."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_public_funds_snapshot import snapshot_state_rs_public_funds


def main() -> None:
    run_id = f"state-rs-public-funds-pilot-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = snapshot_state_rs_public_funds(
        snapshot_root=Path(".data/snapshots/web/state_rs_public_funds"),
        audit_root=Path(
            ".data/audit/base_territorial/state_rs_public_funds"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"resources={len(result.manifest)}")
    print(f"archive_members={len(result.archive_inventory)}")
    print(f"total_bytes={int(result.manifest.bytes.sum())}")
    print("archives_extracted=0")
    print("canonical_rows_promoted=0")
    print(f"snapshot={result.snapshot_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
