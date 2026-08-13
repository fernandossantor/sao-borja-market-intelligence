"""CLI da captura anual DCA/SICONFI para São Borja."""

from __future__ import annotations

import argparse
from pathlib import Path

import requests

from .siconfi_dca_snapshot import snapshot_siconfi_dca


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--snapshot-id", required=True)
    parser.add_argument(
        "--snapshots-root", type=Path, default=Path(".data/snapshots/web/siconfi_dca")
    )
    args = parser.parse_args()
    result = snapshot_siconfi_dca(
        requests.Session(), args.snapshots_root, snapshot_id=args.snapshot_id
    )
    print(
        f"files={result.files} rows={result.rows} bytes={result.bytes} path={result.snapshot_path}"
    )


if __name__ == "__main__":
    main()
