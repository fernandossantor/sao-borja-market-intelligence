"""Comando para construir os agregados publicados do IPS Brasil."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.social_ips import build_published_ips, write_published_ips


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Constrói índice, dimensões e componentes de São Borja nas edições "
            "publicadas do IPS Brasil, sem comparar anos não equivalentes."
        )
    )
    parser.add_argument(
        "--snapshot-path",
        type=Path,
        default=Path(
            ".data/snapshots/web/social_ips/"
            "ips-brasil-published-2024-2026"
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(
            ".data/curated/base_territorial/social/ips/published_2024_2026"
        ),
    )
    parser.add_argument("--ibge-code", default="4318002")
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument("--replace", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = build_published_ips(
        args.snapshot_path,
        ibge_code=args.ibge_code,
        municipality=args.municipality,
    )
    output_dir = write_published_ips(
        result,
        args.output_dir,
        replace=args.replace,
    )
    print(f"snapshot_path={args.snapshot_path.expanduser().resolve()}")
    print(f"municipality={args.municipality}")
    print(f"ibge_code={args.ibge_code}")
    print(
        "reference_years="
        f"{'|'.join(str(year) for year in result.metadata['reference_years'])}"
    )
    print(f"published_summary_rows_observed={len(result.published_summary_long)}")
    print(f"summary_2026_rows_observed={len(result.summary_2026)}")
    print("summary_contract=index_1|dimensions_3|components_12")
    print(
        "comparability_status="
        f"{result.metadata['comparability_status']}"
    )
    print(
        "temporal_change_calculated="
        f"{int(bool(result.metadata['temporal_change_calculated']))}"
    )
    print(
        "individual_indicator_values_status="
        f"{result.metadata['individual_indicator_values_status']}"
    )
    print(
        "harmonized_series_status="
        f"{result.metadata['harmonized_series_status']}"
    )
    print(f"output_dir={output_dir}")
    print("historical_outputs_modified=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
