"""Comando para auditar períodos, duplicidades internas e sobreposição federal."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath

import pandas as pd

from sbmi.inbox_content_audit import audit_snapshot_content
from sbmi.inbox_profile_cli import latest_snapshot
from sbmi.inbox_structure_triage_cli import latest_profile_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Audita o conteúdo das tabelas capturadas sem modificar os arquivos locais "
            "ou acessar o Google Drive."
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
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--max-pairs", type=int, default=20)
    return parser


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def _filename(value: object) -> str:
    return PurePosixPath(str(value)).name


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
    sheet_profile_path = profile_dir / "sheet_profile.csv"
    if not sheet_profile_path.is_file():
        raise FileNotFoundError(f"Perfil de planilhas não encontrado: {sheet_profile_path}")

    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/new_files/content_audit") / snapshot_path.name
    )
    result, errors = audit_snapshot_content(
        snapshot_path,
        pd.read_csv(sheet_profile_path),
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    result.audit_summary.to_csv(output_dir / "content_audit_summary.csv", index=False)
    result.table_summary.to_csv(output_dir / "table_content_summary.csv", index=False)
    result.federal_overlap_candidates.to_csv(
        output_dir / "federal_row_overlap_candidates.csv",
        index=False,
    )
    errors.to_csv(output_dir / "content_audit_errors.csv", index=False)

    indicators = _indicator_map(result.audit_summary)
    print(f"snapshot_path={snapshot_path}")
    print(f"profile_dir={profile_dir}")
    for name in (
        "tables_loaded",
        "tables_error",
        "federal_tables",
        "tables_with_internal_duplicate_rows",
        "tables_with_date_header",
        "date_parse_failures_total",
        "federal_overlap_pairs",
        "identical_normalized_content_pairs",
        "containment_pairs",
        "partial_row_overlap_pairs",
    ):
        print(f"{name}={indicators[name]}")

    table_summary = result.table_summary.sort_values(
        ["source_declared", "relative_path", "sheet_index"]
    )
    for row in table_summary.itertuples(index=False):
        print(
            "table="
            f"{row.source_declared}/{_filename(row.relative_path)}"
            f"\trows={row.rows_observed}"
            f"\tunique={row.unique_rows_normalized}"
            f"\tduplicates={row.duplicate_rows_within_file}"
            f"\tdate_header={row.date_header_observed or '-'}"
            f"\tperiod_min={row.period_min_observed or '-'}"
            f"\tperiod_max={row.period_max_observed or '-'}"
            f"\tdate_failures={row.date_parse_failures}"
        )

    pairs = result.federal_overlap_candidates.head(max(args.max_pairs, 0))
    print(f"overlap_pairs_printed={len(pairs)}")
    for row in pairs.itertuples(index=False):
        print(
            "pair="
            f"{row.candidate_class}"
            f"\tleft={_filename(row.left_path)}"
            f"\tright={_filename(row.right_path)}"
            f"\tshared_unique_rows={row.shared_unique_rows}"
            f"\tjaccard={row.jaccard_row_similarity}"
            f"\tleft_containment={row.left_containment}"
            f"\tright_containment={row.right_containment}"
        )

    print(f"output_dir={output_dir.resolve()}")
    print("status=ok" if indicators["tables_error"] == 0 else "status=completed_with_errors")


if __name__ == "__main__":
    main()
