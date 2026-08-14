from datetime import date
from pathlib import Path

import pandas as pd
from openpyxl import Workbook

from sbmi.inbox_anomaly_review import (
    build_content_duplicate_pairs,
    build_duplicate_row_groups,
    build_review_summary,
    build_temporal_review,
    parse_date_observation,
)
from sbmi.inbox_content_audit import LoadedTable, load_profiled_tables


def _write_workbook(path: Path, title: str, rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Dados"
    worksheet.append([title, None, None])
    for row in rows:
        worksheet.append(row)
    workbook.save(path)
    workbook.close()


def _profile(*paths: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": path,
                "sheet_name": "Dados",
                "sheet_index": 1,
                "header_row_candidate_estimate": 2,
                "observed_max_column": 3,
            }
            for path in paths
        ]
    )


def test_content_duplicate_detects_binary_different_copy(tmp_path: Path) -> None:
    left = "raw/new_files/Federal/base.xlsx"
    right = "raw/new_files/Federal/base(1).xlsx"
    rows = [
        ["Mês Ano", "Tipo", "Valor"],
        ["01/2026", "Corrente", 100],
    ]
    _write_workbook(tmp_path / left, "Relatório A", rows)
    _write_workbook(tmp_path / right, "Relatório B", rows)

    profile = _profile(left, right)
    tables, errors = load_profiled_tables(tmp_path, profile)
    pairs = build_content_duplicate_pairs(tmp_path, tables)

    assert errors == []
    assert len(pairs) == 1
    assert pairs.loc[0, "duplicate_class"] == "CONTENT_DUPLICATE"
    assert pairs.loc[0, "binary_same"] == False  # noqa: E712
    assert pairs.loc[0, "suggested_primary_path"] == left
    assert pairs.loc[0, "suggested_duplicate_path"] == right


def test_same_file_tables_are_not_classified_as_binary_duplicates(
    tmp_path: Path,
) -> None:
    path = "raw/agro/base.xlsx"
    target = tmp_path / path
    target.parent.mkdir(parents=True)
    target.write_bytes(b"same-workbook")
    common = {
        "relative_path": path,
        "source_declared": "agro",
        "headers": ("ano", "valor"),
        "normalized_headers": ("ano", "valor"),
        "rows": (("2024", 10),),
    }
    tables = [
        LoadedTable(sheet_name="Dados", sheet_index=1, **common),
        LoadedTable(sheet_name="Copia", sheet_index=2, **common),
    ]

    pairs = build_content_duplicate_pairs(tmp_path, tables)
    assert pairs.loc[0, "duplicate_class"] == "INTRA_FILE_TABLE_DUPLICATE"
    assert pairs.loc[0, "same_file"] == True  # noqa: E712
    assert {
        pairs.loc[0, "left_sheet"],
        pairs.loc[0, "right_sheet"],
    } == {"Dados", "Copia"}


def test_documentation_duplicates_remain_recorded_separately(tmp_path: Path) -> None:
    paths = ("raw/agro/a.xlsx", "raw/pib/b.xlsx")
    for path in paths:
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.encode("utf-8"))
    common = {
        "sheet_name": "Notas",
        "sheet_index": 1,
        "headers": ("nota",),
        "normalized_headers": ("nota",),
        "rows": (("Conteúdo institucional",),),
    }
    tables = [
        LoadedTable(relative_path=paths[0], source_declared="agro", **common),
        LoadedTable(relative_path=paths[1], source_declared="pib", **common),
    ]

    pairs = build_content_duplicate_pairs(tmp_path, tables)

    assert len(pairs) == 1
    assert pairs.loc[0, "duplicate_class"] == "DOCUMENTATION_CONTENT_DUPLICATE"
    assert pairs.loc[0, "review_status"] == "PENDING_MANUAL_DISPOSITION"

    summary = build_review_summary(
        pairs,
        pd.DataFrame(),
        pd.DataFrame(),
        pd.DataFrame(),
    ).set_index("indicator")
    assert summary.loc["content_duplicate_binary_different_pairs", "value"] == 1
    assert summary.loc["cross_file_content_duplicate_pairs", "value"] == 0
    assert summary.loc["documentation_content_duplicate_pairs", "value"] == 1


def test_duplicate_rows_preserve_source_row_numbers(tmp_path: Path) -> None:
    path = "raw/new_files/Estadual/icms.xlsx"
    _write_workbook(
        tmp_path / path,
        "Relatório",
        [
            ["Data", "Município", "Valor"],
            [date(2026, 1, 5), "São Borja", 100],
            [date(2026, 1, 5), "São Borja", 100],
            [date(2026, 2, 5), "São Borja", 200],
        ],
    )

    groups = build_duplicate_row_groups(tmp_path, _profile(path))

    assert len(groups) == 1
    assert groups.loc[0, "occurrence_count"] == 2
    assert groups.loc[0, "duplicate_excess"] == 1
    assert groups.loc[0, "source_row_numbers"] == "3|4"
    assert groups.loc[0, "duplicate_class"] == "STRICT_EXACT_ROW"


def test_parse_date_observation_flags_possible_reversal() -> None:
    parsed = parse_date_observation("05/12/2026")

    assert parsed["parsed_date"] == date(2026, 12, 5)
    assert parsed["alternative_date"] == date(2026, 5, 12)
    assert parsed["ambiguous"] is True
    assert parsed["parse_method"] == "DMY_ASSUMED"
    compact = parse_date_observation("202303")
    short_text = parse_date_observation("fev/20")
    invalid = parse_date_observation("202313")
    assert compact["parsed_date"] == date(2023, 3, 1)
    assert compact["parse_method"] == "COMPACT_YEAR_MONTH"
    assert short_text["parsed_date"] == date(2020, 2, 1)
    assert short_text["parse_method"] == "TEXT_MONTH_YEAR"
    assert invalid["parsed_date"] is None


def test_temporal_review_separates_future_and_ambiguous_values(tmp_path: Path) -> None:
    path = "raw/new_files/Estadual/transferencias.xlsx"
    _write_workbook(
        tmp_path / path,
        "Relatório",
        [
            ["Data", "Município", "Valor"],
            ["05/12/2026", "São Borja", 100],
            [date(2026, 8, 1), "São Borja", 200],
            [date(2026, 6, 1), "São Borja", 300],
        ],
    )

    summary, anomalies = build_temporal_review(
        tmp_path,
        _profile(path),
        snapshot_date=date(2026, 7, 23),
    )

    assert summary.loc[0, "future_values"] == 2
    assert summary.loc[0, "ambiguous_values"] == 1
    assert summary.loc[0, "possible_reversal_values"] == 1
    assert set(anomalies["anomaly_class"]) == {
        "AMBIGUOUS_DATE_POSSIBLE_REVERSAL",
        "FUTURE_DATE",
    }


def test_temporal_review_preserves_empty_anomaly_schema(tmp_path: Path) -> None:
    path = "raw/social/bolsa.xlsx"
    _write_workbook(
        tmp_path / path,
        "Relatório",
        [
            ["Mês Competência", "Município", "Valor"],
            ["202303", "São Borja", 100],
        ],
    )

    summary, anomalies = build_temporal_review(
        tmp_path,
        _profile(path),
        snapshot_date=date(2026, 8, 14),
    )

    assert summary.loc[0, "parse_failures"] == 0
    assert summary.loc[0, "period_min_observed"] == "2023-03-01"
    assert anomalies.empty
    assert "anomaly_class" in anomalies.columns
    assert "review_status" in anomalies.columns
