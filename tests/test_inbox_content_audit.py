from pathlib import Path

import pandas as pd
from openpyxl import Workbook

from sbmi.inbox_content_audit import (
    audit_snapshot_content,
    build_federal_overlap_candidates,
    build_table_summary,
    load_profiled_tables,
    parse_temporal_value,
)


def _write_workbook(path: Path, rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Dados"
    for row in rows:
        worksheet.append(row)
    workbook.save(path)
    workbook.close()


def _profile(*relative_paths: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": relative_path,
                "sheet_name": "Dados",
                "sheet_index": 1,
                "header_row_candidate_estimate": 2,
                "observed_max_column": 3,
            }
            for relative_path in relative_paths
        ]
    )


def test_parse_temporal_value_uses_explicit_date_formats() -> None:
    assert parse_temporal_value("01/2024") == "2024-01-01"
    assert parse_temporal_value("2025-07") == "2025-07-01"
    assert parse_temporal_value("fevereiro/2026") == "2026-02-01"
    assert parse_temporal_value("codigo 2026") is None


def test_load_and_summarize_periods_without_false_years(tmp_path: Path) -> None:
    relative_path = "raw/new_files/Federal/a.xlsx"
    _write_workbook(
        tmp_path / relative_path,
        [
            ["Relatório", None, None],
            ["Mês Ano", "CPF CNPJ", "Valor Transferido"],
            ["01/2024", "20261234567890", 100.0],
            ["02/2024", "20261234567890", 100.0],
            ["02/2024", "20261234567890", 100.0],
        ],
    )

    tables, errors = load_profiled_tables(tmp_path, _profile(relative_path))
    summary = build_table_summary(tables)

    assert errors == []
    assert summary.loc[0, "rows_observed"] == 3
    assert summary.loc[0, "duplicate_rows_within_file"] == 1
    assert summary.loc[0, "period_min_observed"] == "2024-01-01"
    assert summary.loc[0, "period_max_observed"] == "2024-02-01"
    assert summary.loc[0, "date_parse_failures"] == 0


def test_federal_overlap_detects_identical_normalized_content(tmp_path: Path) -> None:
    left = "raw/new_files/Federal/a.xlsx"
    right = "raw/new_files/Federal/b.xlsx"
    common_header = ["Mês Ano", "Tipo", "Valor Transferido"]
    rows_a = [
        ["01/2024", "Corrente", 100],
        ["02/2024", "Capital", 200],
    ]
    rows_b = list(reversed(rows_a))
    _write_workbook(tmp_path / left, [["Título", None, None], common_header, *rows_a])
    _write_workbook(tmp_path / right, [["Outro título", None, None], common_header, *rows_b])

    tables, errors = load_profiled_tables(tmp_path, _profile(left, right))
    summary = build_table_summary(tables)
    overlap = build_federal_overlap_candidates(summary)

    assert errors == []
    assert len(overlap) == 1
    assert overlap.loc[0, "candidate_class"] == "IDENTICAL_NORMALIZED_CONTENT"
    assert overlap.loc[0, "shared_unique_rows"] == 2
    assert overlap.loc[0, "jaccard_row_similarity"] == 1.0


def test_audit_snapshot_content_detects_containment(tmp_path: Path) -> None:
    left = "raw/new_files/Federal/menor.xlsx"
    right = "raw/new_files/Federal/maior.xlsx"
    header = ["Mês Ano", "Tipo", "Valor Transferido"]
    row_a = ["01/2024", "Corrente", 100]
    row_b = ["02/2024", "Capital", 200]
    _write_workbook(tmp_path / left, [["Título", None, None], header, row_a])
    _write_workbook(tmp_path / right, [["Título", None, None], header, row_a, row_b])

    result, errors = audit_snapshot_content(tmp_path, _profile(left, right))

    assert errors.empty
    assert result.audit_summary.set_index("indicator").loc["containment_pairs", "value"] == 1
    assert result.federal_overlap_candidates.loc[0, "candidate_class"] == (
        "LEFT_CONTAINED_IN_RIGHT"
    )
