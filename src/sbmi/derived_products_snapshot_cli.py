"""Comando para capturar produtos derivados sem reconstrução."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.derived_products_snapshot import (
    DEFAULT_DERIVED_SCOPES,
    snapshot_derived_products,
)
from sbmi.google_drive import (
    build_authorized_session,
    service_account_info_from_environment,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Baixa processed, exports e warehouse para uma captura local "
            "verificada, sem reconstruir produtos nem escrever no Drive."
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
        default=Path(".data/snapshots/derived_products"),
    )
    parser.add_argument("--snapshot-id", default="derived-products-20260723")
    parser.add_argument(
        "--scope",
        action="append",
        dest="scopes",
        help="Escopo derivado. Pode ser repetido.",
    )
    parser.add_argument("--max-total-bytes", type=int, default=350_000_000)
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if not args.inventory_csv.is_file():
        raise FileNotFoundError(f"Inventário não encontrado: {args.inventory_csv}")

    inventory = pd.read_csv(args.inventory_csv)
    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_session(info)
    result = snapshot_derived_products(
        session=session,
        inventory=inventory,
        snapshots_root=args.snapshots_root,
        snapshot_id=args.snapshot_id,
        scopes=tuple(args.scopes or DEFAULT_DERIVED_SCOPES),
        max_total_bytes=args.max_total_bytes,
    )

    print(f"snapshot_path={result.snapshot_path}")
    print(f"scopes={'|'.join(result.scopes)}")
    print(f"files={result.files}")
    print(f"bytes={result.bytes}")
    print("verification=SIZE_AND_SHA256")
    print("transformation=NONE")
    print("drive_mode=read_only")
    print("status=ok")


if __name__ == "__main__":
    main()
