"""Comando para auditar produtos derivados existentes."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.derived_products_audit import (
    audit_derived_products_snapshot,
    write_derived_products_audit,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Valida legibilidade, estrutura e sinais de utilidade dos produtos "
            "derivados existentes, sem reconstruí-los."
        )
    )
    parser.add_argument(
        "--snapshot-path",
        type=Path,
        default=Path(
            ".data/snapshots/derived_products/derived-products-20260723"
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(
            ".data/audit/derived_products/derived-products-20260723"
        ),
    )
    parser.add_argument("--replace", action="store_true")
    return parser


def _value(summary, indicator: str) -> int:
    row = summary.loc[summary["indicator"].eq(indicator), "value"]
    return int(row.iloc[0]) if not row.empty else 0


def main() -> None:
    args = build_parser().parse_args()
    result = audit_derived_products_snapshot(args.snapshot_path)
    output_dir = write_derived_products_audit(
        result,
        args.output_dir,
        replace=args.replace,
    )

    print(f"snapshot_path={args.snapshot_path.expanduser().resolve()}")
    for indicator in result.summary["indicator"]:
        print(f"{indicator}={_value(result.summary, str(indicator))}")
    for row in result.families.sort_values("family").itertuples(index=False):
        print(
            f"family={row.family}\tfiles={row.files}\tbytes={row.known_bytes}"
            f"\ttables={row.tables}\trows={row.rows_observed}"
            f"\tschemas={row.unique_schemas}\tsignal={row.analytical_signal_tables}"
            f"\tstatus={row.family_status}"
        )
    print(f"output_dir={output_dir}")
    print("raw_reprocessing=0")
    print("derived_reconstruction=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
