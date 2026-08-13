"""CLI da série oficial DCA de São Borja."""

from __future__ import annotations

import argparse
from pathlib import Path

from .siconfi_dca_series import curate_siconfi_dca_series


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-dir", type=Path, required=True)
    parser.add_argument("--execution-id", required=True)
    parser.add_argument("--data-root", type=Path, default=Path(".data"))
    args = parser.parse_args()
    roots = {
        layer: args.data_root / layer / "base_territorial" / "siconfi_dca_series"
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_siconfi_dca_series(
        args.snapshot_dir, roots=roots, execution_id=args.execution_id
    )
    missing = int((result.coverage.status == "MISSING").sum())
    print(
        f"rows={len(result.values)} accounts={result.values.account_code.nunique()} "
        f"missing={missing}"
    )


if __name__ == "__main__":
    main()
