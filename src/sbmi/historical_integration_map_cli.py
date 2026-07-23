"""Comando para mapear candidatos de integração com o acervo histórico."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.historical_integration_map import (
    TARGET_SCOPES,
    build_historical_integration_map,
    write_historical_integration_map,
)
from sbmi.inbox_staging_validation_cli import latest_staging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Compara por metadados as fontes ativas do staging com arquivos de "
            "processed, warehouse e exports, sem baixar conteúdos históricos."
        )
    )
    parser.add_argument(
        "--inventory-path",
        type=Path,
        default=Path(".data/manifests/google_drive_inventory.csv"),
    )
    parser.add_argument("--staging-path", type=Path)
    parser.add_argument(
        "--staging-root",
        type=Path,
        default=Path(".data/staging/new_files"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--scope", action="append", dest="scopes")
    parser.add_argument("--top-n", type=int, default=5)
    parser.add_argument("--replace", action="store_true")
    return parser


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    inventory_path = args.inventory_path.expanduser().resolve()
    if not inventory_path.is_file():
        raise FileNotFoundError(f"Inventário do Drive não encontrado: {inventory_path}")

    staging_path = (
        args.staging_path.expanduser().resolve()
        if args.staging_path is not None
        else latest_staging(args.staging_root)
    )
    manifest_path = staging_path / "source_manifest.csv"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifesto do staging não encontrado: {manifest_path}")

    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/historical_integration_map") / staging_path.name
    )
    scopes = tuple(args.scopes) if args.scopes else TARGET_SCOPES

    result = build_historical_integration_map(
        pd.read_csv(inventory_path),
        pd.read_csv(manifest_path),
        scopes=scopes,
        top_n=args.top_n,
    )
    target = write_historical_integration_map(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.mapping_summary)

    print(f"inventory_path={inventory_path}")
    print(f"staging_path={staging_path}")
    print(f"scopes={'|'.join(scopes)}")
    for name in (
        "active_staging_source_files",
        "historical_target_files",
        "historical_data_like_files",
        "candidate_pairs_retained",
        "sources_with_candidates",
        "sources_without_candidates",
        "exact_sha256_pairs",
        "exact_normalized_name_pairs",
        "strong_name_match_pairs",
        "possible_name_match_pairs",
    ):
        print(f"{name}={indicators[name]}")
    for row in result.scope_summary.itertuples(index=False):
        print(
            f"scope={row.scope}"
            f"\tfiles={row.files}"
            f"\tdata_like={row.data_like_files}"
            f"\tknown_bytes={row.known_bytes}"
            f"\tsha256={row.files_with_sha256}"
        )
    print(f"output_dir={target}")
    print("historical_files_downloaded=0")
    print("raw_files_modified=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
