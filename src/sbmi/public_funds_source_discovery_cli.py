"""CLI da descoberta de fontes de recursos públicos."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.public_funds_source_discovery import discover_public_funds_sources


def main() -> None:
    run_id = f"public-funds-discovery-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = discover_public_funds_sources(
        snapshot_root=Path(".data/snapshots/web/public_funds_discovery"),
        audit_root=Path(".data/audit/base_territorial/public_funds_discovery"),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"sources={len(result.inventory)}")
    print("data_samples_captured=0")
    print("personal_data_files=0")
    print("canonical_rows_promoted=0")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
