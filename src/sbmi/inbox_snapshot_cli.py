"""Comando para capturar localmente os arquivos de ``raw/new_files``."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.google_drive import (
    build_authorized_session,
    service_account_info_from_environment,
)
from sbmi.inbox_audit import DEFAULT_INBOX_PREFIX
from sbmi.inbox_snapshot import snapshot_inbox


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Baixa somente raw/new_files para uma captura local verificada, "
            "sem escrever no Google Drive."
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
        default=Path(".data/snapshots/new_files"),
    )
    parser.add_argument("--inbox-prefix", default=DEFAULT_INBOX_PREFIX)
    parser.add_argument("--snapshot-id")
    parser.add_argument("--max-total-bytes", type=int, default=10_000_000)
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if not args.inventory_csv.is_file():
        raise FileNotFoundError(f"Inventário não encontrado: {args.inventory_csv}")
    if args.max_total_bytes <= 0:
        raise ValueError("--max-total-bytes deve ser maior que zero.")

    inventory = pd.read_csv(args.inventory_csv)
    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_session(info)
    result = snapshot_inbox(
        session=session,
        inventory=inventory,
        snapshots_root=args.snapshots_root,
        inbox_prefix=args.inbox_prefix,
        snapshot_id=args.snapshot_id,
        max_total_bytes=args.max_total_bytes,
    )

    print(f"snapshot_path={result.snapshot_path}")
    print(f"files={result.files}")
    print(f"bytes={result.bytes}")
    print("verification=SIZE_AND_SHA256")
    print("drive_mode=read_only")
    print("status=ok")


if __name__ == "__main__":
    main()
