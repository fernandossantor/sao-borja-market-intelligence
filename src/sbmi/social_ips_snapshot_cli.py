"""Comando para capturar scorecards renderizados do IPS Brasil."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.ips_web_snapshot import DEFAULT_SNAPSHOT_ID, snapshot_published_ips_pages


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Renderiza os scorecards públicos do IPS Brasil para São Borja "
            "e preserva o DOM final do Phoenix LiveView."
        )
    )
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(".data/snapshots/web/social_ips"),
    )
    parser.add_argument("--snapshot-id", default=DEFAULT_SNAPSHOT_ID)
    parser.add_argument("--ibge-code", default="4318002")
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    parser.add_argument("--max-total-bytes", type=int, default=20_000_000)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = snapshot_published_ips_pages(
        snapshots_root=args.snapshots_root,
        snapshot_id=args.snapshot_id,
        ibge_code=args.ibge_code,
        municipality=args.municipality,
        timeout_seconds=args.timeout_seconds,
        max_total_bytes=args.max_total_bytes,
    )
    print(f"snapshot_path={result.snapshot_path}")
    print(f"years={'|'.join(str(year) for year in result.years)}")
    print(f"pages_captured={result.pages}")
    print(f"stored_bytes={result.stored_bytes}")
    print(f"browser_navigations={result.browser_navigations}")
    print(f"ibge_code={args.ibge_code}")
    print("capture=PLAYWRIGHT_RENDERED_LIVEVIEW_DOM")
    print("aggregates_expected=16_PER_EDITION")
    print("static_html_status=STRUCTURE_ONLY_WITHOUT_NUMERIC_SCORES")
    print("temporal_series=NOT_INCLUDED")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
