"""Comando para capturar as fontes brutas do Censo 2022 de São Borja."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.demography_census_sources import (
    EXPECTED_CENSUS_SOURCE_FILES,
    select_census_source_files,
    selected_source_paths,
)
from sbmi.google_drive import (
    build_authorized_session,
    service_account_info_from_environment,
)
from sbmi.source_snapshot import snapshot_source_files


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Baixa e verifica somente as planilhas brutas do Censo 2022 de "
            "São Borja, sem modificar o Google Drive."
        )
    )
    parser.add_argument(
        "--inventory-csv",
        type=Path,
        default=Path(".data/manifests/google_drive_inventory.csv"),
    )
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(".data/snapshots/sources/demography_census"),
    )
    parser.add_argument(
        "--snapshot-id",
        default="census-2022-sao-borja-sources-20260724",
    )
    parser.add_argument(
        "--expected-files",
        type=int,
        default=EXPECTED_CENSUS_SOURCE_FILES,
    )
    parser.add_argument("--max-total-bytes", type=int, default=25_000_000)
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    inventory_path = args.inventory_csv.expanduser().resolve()
    if not inventory_path.is_file():
        raise FileNotFoundError(f"Inventário não encontrado: {inventory_path}")
    if args.expected_files <= 0:
        raise ValueError("expected-files deve ser maior que zero.")

    inventory = pd.read_csv(inventory_path)
    selected = select_census_source_files(inventory)
    if len(selected) != args.expected_files:
        raise ValueError(
            "Quantidade inesperada de fontes censitárias: "
            f"observado={len(selected)}, esperado={args.expected_files}"
        )

    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_session(info)
    result = snapshot_source_files(
        session=session,
        inventory=inventory,
        snapshots_root=args.snapshots_root,
        relative_paths=selected_source_paths(selected),
        snapshot_id=args.snapshot_id,
        max_total_bytes=args.max_total_bytes,
    )

    selected.to_csv(result.snapshot_path / "census_source_selection.csv", index=False)
    print(f"inventory_path={inventory_path}")
    print(f"snapshot_path={result.snapshot_path}")
    print(f"selected_sources={len(selected)}")
    print(f"files={result.files}")
    print(f"bytes={result.bytes}")
    print(f"topic_keys={selected['topic_key'].nunique()}")
    print("verification=SIZE_AND_SHA256_WHEN_AVAILABLE")
    print("selection_rule=RAW_XLSX_EXACT_CENSUS_2022_SAO_BORJA_TITLE")
    print("transformation=NONE")
    print("drive_mode=read_only")
    print("raw_files_modified=0")
    print("status=ok")


if __name__ == "__main__":
    main()
