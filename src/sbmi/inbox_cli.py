"""Comando independente para auditar ``raw/new_files`` por metadados."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.inbox_audit import (
    DEFAULT_INBOX_PREFIX,
    classify_inbox_files,
    inbox_source_summary,
    inbox_summary,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audita a caixa raw/new_files sem baixar ou alterar dados do Drive."
    )
    parser.add_argument(
        "--inventory-csv",
        type=Path,
        default=Path(".data/manifests/google_drive_inventory.csv"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(".data/audit/new_files"),
    )
    parser.add_argument("--inbox-prefix", default=DEFAULT_INBOX_PREFIX)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if not args.inventory_csv.is_file():
        raise FileNotFoundError(f"Inventário não encontrado: {args.inventory_csv}")

    inventory = pd.read_csv(args.inventory_csv)
    classified = classify_inbox_files(inventory, args.inbox_prefix)
    summary = inbox_summary(classified)
    by_source = inbox_source_summary(classified)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output_dir / "new_files_summary.csv", index=False)
    by_source.to_csv(args.output_dir / "new_files_by_source.csv", index=False)
    classified.to_csv(args.output_dir / "new_files_file_classification.csv", index=False)

    indicators = dict(zip(summary["indicator"], summary["value"], strict=True))
    for indicator in (
        "inbox_files",
        "inbox_known_bytes",
        "inbox_files_with_sha256",
        "inbox_files_without_sha256",
        "unique_by_sha256_rows",
        "exact_duplicate_outside_groups",
        "exact_duplicate_outside_rows",
        "exact_duplicate_within_groups",
        "exact_duplicate_within_rows",
    ):
        print(f"{indicator}={indicators[indicator]}")

    print(f"declared_sources={len(by_source)}")
    for row in by_source.itertuples(index=False):
        print(
            "source="
            f"{row.inbox_source}\tfiles={row.files}\tbytes={row.known_bytes}"
            f"\toutside={row.exact_duplicate_outside_rows}"
            f"\twithin={row.exact_duplicate_within_rows}"
            f"\tunique={row.unique_by_sha256_rows}"
            f"\tmissing_sha256={row.missing_sha256_rows}"
        )
    print(f"output_dir={args.output_dir.resolve()}")
    print("status=ok")


if __name__ == "__main__":
    main()
