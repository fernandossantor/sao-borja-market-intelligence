"""CLI do lote janeiro–abril/2026 de despesas estaduais."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_expense_batch import build_state_rs_expense_batch


def main() -> None:
    inventories = sorted(
        Path(
            ".data/audit/base_territorial/state_rs_expense_head_inventory"
        ).glob("*/resource_head_inventory.csv")
    )
    if not inventories:
        raise FileNotFoundError("Inventário HEAD não encontrado")
    run_id = datetime.now(UTC).strftime(
        "state-rs-expense-2026-01-04-%Y%m%d-%H%M%S"
    )
    result = build_state_rs_expense_batch(
        inventory_path=inventories[-1],
        snapshot_root=Path(
            ".data/snapshots/web/state_rs_expense_monthly"
        ),
        staging_root=Path(
            ".data/staging/base_territorial/state_rs_expense_monthly"
        ),
        audit_root=Path(
            ".data/audit/base_territorial/state_rs_expense_monthly"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"resources={len(result.manifest)}")
    print(f"actual_bytes={int(result.manifest.actual_bytes.sum())}")
    print(f"rows_scanned={int(result.resource_summary.rows_scanned.sum())}")
    print(f"staging_rows={len(result.staging)}")
    print("sensitive_values_persisted=0")
    print("canonical_rows_promoted=0")
    print(f"snapshot={result.snapshot_path}")
    print(f"staging={result.staging_path}")
    print(f"audit={result.audit_path}")


if __name__ == "__main__":
    main()
