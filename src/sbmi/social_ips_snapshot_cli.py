"""Comando para capturar scorecards publicados do IPS Brasil."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.ips_web_snapshot import snapshot_published_ips_pages


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Captura os scorecards publicados do IPS Brasil para São Borja, "
            "sem baixar a base nacional integral."
        )
    )
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(".data/snapshots/web/social_ips"),
    )
    parser.add_argument(
        "--snapshot-id",
        default="ips-brasil-published-2024-2026",
    )
    parser.add_argument("--ibge-code", default="4318002")
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument("--max-total-bytes", type=int, default=10_000_000)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = snapshot_published_ips_pages(
        snapshots_root=args.snapshots_root,
        snapshot_id=args.snapshot_id,
        ibge_code=args.ibge_code,
        municipality=args.municipality,
        max_total_bytes=args.max_total_bytes,
    )
    print(f"snapshot_path={result.snapshot_path}")
    print(f"years={'|'.join(str(year) for year in result.years)}")
    print(f"pages_captured={result.pages}")
    print(f"stored_bytes={result.bytes}")
    print(f"requests={result.requests}")
    print(f"transferred_bytes={result.transferred_bytes}")
    print(f"ibge_code={args.ibge_code}")
    print("capture=PUBLIC_MUNICIPAL_SCORECARDS")
    print("aggregates_expected=16_PER_EDITION")
    print("individual_indicator_values=NOT_AVAILABLE_IN_SCORECARD_HTML")
    print("temporal_series=NOT_INCLUDED")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
