"""CLI da série definitiva de IPM de São Borja."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.ipm_definitive_series import (
    build_ipm_series_from_archives,
    write_ipm_series_outputs,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--archive-root",
        type=Path,
        required=True,
        help="Pasta contendo ipm_2003.zip ... ipm_2026.zip.",
    )
    parser.add_argument(
        "--execution-id",
        default="ipm-definitive-sao-borja-2003-2026-v001",
    )
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    outputs = build_ipm_series_from_archives(
        args.archive_root,
        execution_id=args.execution_id,
        municipality=args.municipality,
    )
    write_ipm_series_outputs(outputs, args.output_dir)

    series = outputs.series
    print(f"execution_id={args.execution_id}")
    print(f"rows={len(series)}")
    print(f"first_year={int(series['distribution_year'].min())}")
    print(f"last_year={int(series['distribution_year'].max())}")
    print(f"ipm_2025={series.loc[series.distribution_year == 2025, 'ipm_definitive_text'].iloc[0]}")
    print(f"ipm_2026={series.loc[series.distribution_year == 2026, 'ipm_definitive_text'].iloc[0]}")
    print(
        "yoy_2026_pct="
        f"{series.loc[series.distribution_year == 2026, 'yoy_change_pct'].iloc[0]:.6f}"
    )
    print(f"output_dir={args.output_dir}")
    print("STATUS=IPM_DEFINITIVE_SERIES_OK")


if __name__ == "__main__":
    main()
