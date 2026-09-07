"""Promote the audited territorial-wage derivatives to the project Drive exports folder."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.drive_promotion import (
    ExpectedDerivative,
    build_authorized_write_session,
    promote_derivatives,
)
from sbmi.google_drive import service_account_info_from_environment

DEFAULT_EXECUTION_ID = "territorial-wage-rais2025-rfb2026-08-drive-20260907-200236"
DEFAULT_OUTPUT_DIR = Path(
    ".data/exports/base_territorial/territorial_wage_estimation"
) / DEFAULT_EXECUTION_ID
DEFAULT_DRIVE_FOLDER_ID = "12TDHgZ6_M63f98RMRUckTqcEA5FCRp_x"

EXPECTED = [
    ExpectedDerivative(
        "run_metadata.csv",
        1062,
        "88e00fc30380a7ae0ea12bd97882677d9cd45ad25a04dc05ee77497ecae448f7",
    ),
    ExpectedDerivative(
        "source_manifest.csv",
        616,
        "334a77029b14e3a0f51be34adda280f62ec2e253440244fc8026ec9137729839",
    ),
    ExpectedDerivative(
        "territorial_wage_by_division.csv",
        10450,
        "c6d8fe91d95324da28ad35a77d08317309ecc3c358b6f070e21a86a9ef3e667a",
    ),
    ExpectedDerivative(
        "territorial_wage_cells.csv",
        55816,
        "0c2a6bb20e2a3abcca9840536639a3f2b516802d8c0cf2fffe6e83d1e109144f",
    ),
    ExpectedDerivative(
        "territorial_wage_coverage.csv",
        680,
        "337b5e080d93b76f9dc67357c03c915ed1cb44524f72aa08d5c5ecd92b44c812",
    ),
    ExpectedDerivative(
        "territorial_wage_summary.csv",
        1490,
        "1c72ebfa313548050eb9d6684ea1e02ee5b05208e9a08634729d27d748ac5f1e",
    ),
    ExpectedDerivative(
        "validation.csv",
        306,
        "3379431961f8fc030bf85c1d6ffaaf74624b37074661f7a2406b6d33e8eede7d",
    ),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--drive-folder-id", default=DEFAULT_DRIVE_FOLDER_ID)
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    args = parser.parse_args()

    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_write_session(info)
    results = promote_derivatives(
        session,
        output_dir=args.output_dir,
        parent_folder_id=args.drive_folder_id,
        expected=EXPECTED,
    )

    for result in results:
        print(
            f"file={result.name} drive_file_id={result.drive_file_id} "
            f"bytes={result.size_bytes} sha256={result.sha256} "
            f"reused_existing={str(result.reused_existing).lower()}"
        )
    print(f"drive_folder_id={args.drive_folder_id}")
    print(f"files_promoted={len(results)}")
    print("STATUS=TERRITORIAL_WAGE_DRIVE_PROMOTION_OK")


if __name__ == "__main__":
    main()
