"""Comando para capturar a fonte bruta do IDSC-BR 2025."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.google_drive import (
    build_authorized_session,
    service_account_info_from_environment,
)
from sbmi.source_snapshot import snapshot_source_files

DEFAULT_SOURCE_PATH = "raw/social/Base_de_Dados_IDSC-BR_2025.xlsx"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Baixa e verifica somente a fonte bruta do IDSC-BR 2025, "
            "sem modificar o Google Drive."
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
        default=Path(".data/snapshots/sources/social_idsc"),
    )
    parser.add_argument("--snapshot-id", default="idsc-br-2025")
    parser.add_argument("--source-path", default=DEFAULT_SOURCE_PATH)
    parser.add_argument("--max-total-bytes", type=int, default=100_000_000)
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if not args.inventory_csv.is_file():
        raise FileNotFoundError(f"Inventário não encontrado: {args.inventory_csv}")

    inventory = pd.read_csv(args.inventory_csv)
    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_session(info)
    result = snapshot_source_files(
        session=session,
        inventory=inventory,
        snapshots_root=args.snapshots_root,
        relative_paths=(args.source_path,),
        snapshot_id=args.snapshot_id,
        max_total_bytes=args.max_total_bytes,
    )

    print(f"snapshot_path={result.snapshot_path}")
    print(f"source_path={args.source_path}")
    print(f"files={result.files}")
    print(f"bytes={result.bytes}")
    print("verification=SIZE_AND_SHA256")
    print("drive_mode=read_only")
    print("status=ok")


if __name__ == "__main__":
    main()
