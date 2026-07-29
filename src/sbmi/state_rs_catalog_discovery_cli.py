"""CLI da descoberta segura do catálogo estadual."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_catalog_discovery import discover_state_rs_catalog


def main() -> None:
    run_id = f"state-rs-catalog-discovery-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = discover_state_rs_catalog(
        output_root=Path(
            ".data/audit/base_territorial/state_rs_catalog_discovery"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"catalog_rows={len(result.metadata)}")
    print("data_rows_captured=0")
    print("token_stored=0")
    print("canonical_rows_promoted=0")
    print(f"output={result.output_path}")


if __name__ == "__main__":
    main()
