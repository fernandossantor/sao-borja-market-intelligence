"""Comando para validar e reconciliar o staging de ``raw/new_files``."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.inbox_staging_validation import (
    validate_staging_directory,
    write_validation_output,
)


def latest_staging(root: Path) -> Path:
    """Seleciona o staging mais recente disponível."""
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Diretório de staging não encontrado: {resolved}")
    candidates = sorted(
        path
        for path in resolved.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    if not candidates:
        raise FileNotFoundError(f"Nenhum staging encontrado em: {resolved}")
    return candidates[-1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Valida contratos, proveniência, tipos, duplicidades e reconciliação "
            "do staging local."
        )
    )
    parser.add_argument("--staging-path", type=Path)
    parser.add_argument(
        "--staging-root",
        type=Path,
        default=Path(".data/staging/new_files"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--replace", action="store_true")
    return parser


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    staging_path = (
        args.staging_path.expanduser().resolve()
        if args.staging_path is not None
        else latest_staging(args.staging_root)
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/new_files/staging_validation") / staging_path.name
    )

    result = validate_staging_directory(staging_path)
    target = write_validation_output(result, output_dir, replace=args.replace)
    indicators = _indicator_map(result.validation_summary)

    print(f"staging_path={staging_path}")
    for name in (
        "datasets_expected",
        "datasets_loaded",
        "missing_dataset_files",
        "unexpected_dataset_files",
        "rows_validated",
        "source_manifest_rows",
        "included_source_tables",
        "excluded_source_tables",
        "row_reconciliation_failures",
        "quality_indicator_failures",
        "missing_required_columns",
        "unexpected_columns",
        "column_order_mismatch",
        "provenance_null_values",
        "provenance_key_duplicate_rows",
        "source_file_mismatches",
        "source_level_mismatches",
        "snapshot_id_mismatches",
        "row_hash_invalid",
        "source_row_invalid",
        "date_null_values",
        "date_parse_failures",
        "future_date_values",
        "numeric_type_failures",
        "duplicate_flagged_rows",
        "duplicate_groups",
        "duplicate_excess",
        "duplicate_flag_inconsistencies",
        "validation_errors",
        "validation_warnings",
    ):
        print(f"{name}={indicators[name]}")

    for row in result.dataset_summary.itertuples(index=False):
        print(
            f"dataset={row.dataset}"
            f"\trows={row.rows}"
            f"\tcolumns={row.columns}"
            f"\tsource_files={row.source_files}"
            f"\tdate_min={row.date_min or '-'}"
            f"\tdate_max={row.date_max or '-'}"
            f"\tflagged={row.duplicate_flagged_rows}"
            f"\tstatus={row.status}"
        )

    print(f"output_dir={target}")
    print("raw_files_modified=0")
    print("drive_operations=0")
    if indicators["validation_errors"]:
        raise SystemExit("status=error")
    print("status=ok")


if __name__ == "__main__":
    main()
