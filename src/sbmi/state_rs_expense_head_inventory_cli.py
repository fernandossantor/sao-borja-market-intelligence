"""CLI do inventário HEAD das despesas estaduais."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.state_rs_expense_head_inventory import (
    inventory_state_rs_expense_heads,
)


def main() -> None:
    run_id = datetime.now(UTC).strftime(
        "state-rs-expense-head-inventory-%Y%m%d-%H%M%S"
    )
    result = inventory_state_rs_expense_heads(
        output_root=Path(
            ".data/audit/base_territorial/state_rs_expense_head_inventory"
        ),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"resources={len(result.inventory)}")
    print(
        "head_successes="
        f"{int(result.inventory.head_status.fillna(0).between(200, 299).sum())}"
    )
    print(f"sizes_observed={int(result.inventory.content_length.notna().sum())}")
    print(f"observed_bytes={int(result.inventory.content_length.sum())}")
    print("response_bodies_downloaded=0")
    print(f"audit={result.output_path}")


if __name__ == "__main__":
    main()
