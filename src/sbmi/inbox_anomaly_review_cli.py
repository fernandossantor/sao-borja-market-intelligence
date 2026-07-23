"""Comando para revisar duplicidades e anomalias temporais da captura."""

from __future__ import annotations

import argparse
import re
from datetime import date, datetime
from pathlib import Path, PurePosixPath

import pandas as pd

from sbmi.inbox_anomaly_review import review_snapshot_anomalies
from sbmi.inbox_content_audit import load_profiled_tables
from sbmi.inbox_profile_cli import latest_snapshot
from sbmi.inbox_structure_triage_cli import latest_profile_dir

SNAPSHOT_DATE_PATTERN = re.compile(r"(\d{8})$")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Detalha conteúdos duplicados, linhas repetidas e anomalias temporais "
            "sem alterar a captura local."
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
    parser.add_argument("--snapshot-date", type=date.fromisoformat)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--max-details", type=int, default=20)
    return parser


def _date_from_snapshot_name(snapshot_path: Path) -> date:
    match = SNAPSHOT_DATE_PATTERN.search(snapshot_path.name)
    if not match:
        raise ValueError(
            "Não foi possível inferir a data da captura. Use --snapshot-date YYYY-MM-DD."
        )
    return datetime.strptime(match.group(1), "%Y%m%d").date()


def _filename(value: object) -> str:
    return PurePosixPath(str(value)).name


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
    snapshot_date = args.snapshot_date or _date_from_snapshot_name(snapshot_path)
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/new_files/anomaly_review") / snapshot_path.name
    )

    sheet_profile_path = profile_dir / "sheet_profile.csv"
    if not sheet_profile_path.is_file():
        raise FileNotFoundError(f"Perfil de planilhas não encontrado: {sheet_profile_path}")
    sheet_profile = pd.read_csv(sheet_profile_path)
    tables, errors = load_profiled_tables(snapshot_path, sheet_profile)
    if errors:
        raise RuntimeError(f"Falha ao carregar {len(errors)} tabela(s) para revisão.")

    result = review_snapshot_anomalies(
        snapshot_path,
        sheet_profile,
        tables,
        snapshot_date=snapshot_date,
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    result.review_summary.to_csv(output_dir / "anomaly_review_summary.csv", index=False)
    result.content_duplicate_pairs.to_csv(
        output_dir / "content_duplicate_pairs.csv",
        index=False,
    )
    result.duplicate_row_groups.to_csv(
        output_dir / "duplicate_row_groups.csv",
        index=False,
    )
    result.temporal_table_summary.to_csv(
        output_dir / "temporal_table_summary.csv",
        index=False,
    )
    result.temporal_anomalies.to_csv(
        output_dir / "temporal_anomalies.csv",
        index=False,
    )

    indicators = _indicator_map(result.review_summary)
    print(f"snapshot_path={snapshot_path}")
    print(f"profile_dir={profile_dir}")
    print(f"snapshot_date={snapshot_date.isoformat()}")
    for name in (
        "content_duplicate_pairs",
        "content_duplicate_binary_different_pairs",
        "duplicate_row_groups",
        "duplicate_row_excess",
        "tables_with_duplicate_rows",
        "temporal_tables",
        "future_date_values",
        "ambiguous_date_values",
        "possible_date_reversal_values",
        "date_parse_failures",
    ):
        print(f"{name}={indicators[name]}")

    limit = max(args.max_details, 0)
    for row in result.content_duplicate_pairs.head(limit).itertuples(index=False):
        print(
            "content_pair="
            f"{row.duplicate_class}"
            f"\tleft={_filename(row.left_path)}"
            f"\tright={_filename(row.right_path)}"
            f"\tbinary_same={row.binary_same}"
            f"\tsuggested_primary={_filename(row.suggested_primary_path) if row.suggested_primary_path else '-'}"
            f"\tsuggestion_basis={row.suggestion_basis}"
        )

    duplicate_by_file = (
        result.duplicate_row_groups.groupby("relative_path", dropna=False)
        .agg(
            groups=("normalized_row_hash", "size"),
            duplicate_excess=("duplicate_excess", "sum"),
            strict_groups=(
                "duplicate_class",
                lambda values: int(pd.Series(values).eq("STRICT_EXACT_ROW").sum()),
            ),
        )
        .reset_index()
        if not result.duplicate_row_groups.empty
        else pd.DataFrame()
    )
    for row in duplicate_by_file.head(limit).itertuples(index=False):
        print(
            "duplicate_rows="
            f"{_filename(row.relative_path)}"
            f"\tgroups={row.groups}"
            f"\tduplicate_excess={row.duplicate_excess}"
            f"\tstrict_groups={row.strict_groups}"
        )

    temporal_by_file = (
        result.temporal_anomalies.groupby(["relative_path", "anomaly_class"], dropna=False)
        .size()
        .reset_index(name="count")
        if not result.temporal_anomalies.empty
        else pd.DataFrame()
    )
    for row in temporal_by_file.head(limit).itertuples(index=False):
        print(
            "temporal_anomaly="
            f"{_filename(row.relative_path)}"
            f"\tclass={row.anomaly_class}"
            f"\tcount={row.count}"
        )

    print(f"output_dir={output_dir.resolve()}")
    print("status=ok")


if __name__ == "__main__":
    main()
