"""CLI da descoberta de links oficiais para produtos censitários."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import requests

from sbmi.demography_census_official_discovery import (
    discover_official_census_products,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Captura duas páginas oficiais do IBGE e registra links candidatos "
            "sem baixar bases ou atribuir equivalência conceitual."
        )
    )
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(
            ".data/snapshots/web/demography_census_official_products"
        ),
    )
    parser.add_argument(
        "--audit-root",
        type=Path,
        default=Path(
            ".data/audit/base_territorial/"
            "demography_census_official_discovery"
        ),
    )
    parser.add_argument("--snapshot-id")
    parser.add_argument("--run-id")
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    parser.add_argument("--max-page-bytes", type=int, default=5_000_000)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    snapshot_id = args.snapshot_id or f"official-products-discovery-{stamp}"
    run_id = args.run_id or f"official-products-discovery-{stamp}"
    with requests.Session() as session:
        result = discover_official_census_products(
            session,
            snapshots_root=args.snapshots_root,
            audit_root=args.audit_root,
            snapshot_id=snapshot_id,
            run_id=run_id,
            timeout_seconds=args.timeout_seconds,
            max_page_bytes=args.max_page_bytes,
        )
    indicators = {
        str(row.indicator): int(row.value)
        for row in result.summary.itertuples(index=False)
    }
    print(f"snapshot_path={result.snapshot_path}")
    print(f"output_path={result.output_path}")
    for name in result.summary["indicator"]:
        print(f"{name}={indicators[str(name)]}")
    print("downloads_performed=0")
    print("conceptual_equivalence_claimed=0")
    print("historical_files_modified=0")
    print("drive_write_operations=0")
    status = (
        "ok" if indicators["pages_successful"] == indicators["pages_captured"]
        else "incomplete"
    )
    print(f"status={status}")


if __name__ == "__main__":
    main()
