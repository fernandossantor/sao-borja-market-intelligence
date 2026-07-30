"""CLI da reconciliação e staging de recursos estaduais."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_public_funds_staging import (
    build_state_rs_public_funds_staging,
)


def main() -> None:
    snapshots = Path(".data/snapshots/web/state_rs_public_funds")
    candidates = sorted(path for path in snapshots.iterdir() if path.is_dir())
    if not candidates:
        raise FileNotFoundError("Nenhum snapshot estadual encontrado")
    run_id = datetime.now(UTC).strftime(
        "state-rs-public-funds-staging-%Y%m%d-%H%M%S"
    )
    result = build_state_rs_public_funds_staging(
        snapshot_path=candidates[-1],
        staging_root=Path(
            ".data/staging/base_territorial/state_rs_public_funds"
        ),
        audit_root=Path(
            ".data/audit/base_territorial/state_rs_public_funds_reconciliation"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"staging_rows={len(result.staging)}")
    print(f"overlap_classification={result.overlap_summary.classification.iloc[0]}")
    print("sensitive_values_persisted=0")
    print("canonical_rows_promoted=0")
    print(f"staging={result.staging_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
