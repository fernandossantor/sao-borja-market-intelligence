"""Comando para construir o staging auditado de ``raw/new_files``."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.inbox_profile_cli import latest_snapshot
from sbmi.inbox_staging import build_staging, write_staging_output
from sbmi.inbox_structure_triage_cli import latest_profile_dir


def latest_anomaly_dir(root: Path) -> Path:
    """Seleciona o diretório mais recente de revisão de anomalias."""
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Diretório de revisões não encontrado: {resolved}")
    candidates = sorted(
        path
        for path in resolved.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    if not candidates:
        raise FileNotFoundError(f"Nenhuma revisão encontrada em: {resolved}")
    return candidates[-1]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Constrói a camada local de staging a partir da captura e das decisões "
            "registradas na auditoria de anomalias."
        )
    )
    parser.add_argument("--snapshot-path", type=Path)
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(".data/snapshots/new_files"),
    )
    parser.add_argument("--profile-dir", type=Path)
    parser.add_argument(
        "--profiles-root",
        type=Path,
        default=Path(".data/audit/new_files/content_profile"),
    )
    parser.add_argument("--anomaly-dir", type=Path)
    parser.add_argument(
        "--anomalies-root",
        type=Path,
        default=Path(".data/audit/new_files/anomaly_review"),
    )
    parser.add_argument("--output-dir", type=Path)
    return parser


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    snapshot_path = (
        args.snapshot_path.expanduser().resolve()
        if args.snapshot_path is not None
        else latest_snapshot(args.snapshots_root)
    )
    profile_dir = (
        args.profile_dir.expanduser().resolve()
        if args.profile_dir is not None
        else latest_profile_dir(args.profiles_root)
    )
    anomaly_dir = (
        args.anomaly_dir.expanduser().resolve()
        if args.anomaly_dir is not None
        else latest_anomaly_dir(args.anomalies_root)
    )
    snapshot_id = snapshot_path.name
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/staging/new_files") / snapshot_id
    )

    sheet_profile_path = profile_dir / "sheet_profile.csv"
    duplicate_pairs_path = anomaly_dir / "content_duplicate_pairs.csv"
    duplicate_rows_path = anomaly_dir / "duplicate_row_groups.csv"
    for required in (
        sheet_profile_path,
        duplicate_pairs_path,
        duplicate_rows_path,
    ):
        if not required.is_file():
            raise FileNotFoundError(f"Entrada obrigatória não encontrada: {required}")

    result = build_staging(
        snapshot_path,
        pd.read_csv(sheet_profile_path),
        pd.read_csv(duplicate_pairs_path),
        pd.read_csv(duplicate_rows_path),
        snapshot_id=snapshot_id,
    )
    target = write_staging_output(result, output_dir)
    indicators = _indicator_map(result.quality_summary)

    print(f"snapshot_path={snapshot_path}")
    print(f"profile_dir={profile_dir}")
    print(f"anomaly_dir={anomaly_dir}")
    for name in (
        "source_tables_observed",
        "source_rows_observed",
        "source_files_excluded_from_staging",
        "source_rows_excluded_from_staging",
        "staging_datasets",
        "staging_rows",
        "federal_source_files_included",
        "federal_rows",
        "icms_rows_retained",
        "icms_duplicate_rows_flagged",
    ):
        print(f"{name}={indicators[name]}")
    for dataset, frame in sorted(result.datasets.items()):
        print(f"dataset={dataset}\trows={len(frame)}\tcolumns={len(frame.columns)}")
    print(f"output_dir={target}")
    print("raw_files_modified=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
