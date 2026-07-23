from pathlib import Path

import pandas as pd
from openpyxl import Workbook

from sbmi.inbox_profile import normalize_label, profile_snapshot
from sbmi.inbox_profile_cli import latest_snapshot


def build_snapshot(tmp_path: Path) -> Path:
    snapshot = tmp_path / "snapshots" / "snapshot-001"
    federal = snapshot / "raw" / "new_files" / "Federal"
    municipal = snapshot / "raw" / "new_files" / "Municipal"
    federal.mkdir(parents=True)
    municipal.mkdir(parents=True)

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Dados"
    worksheet.append(["Relatório territorial 2020"])
    worksheet.append(["Município", "Ano", "Valor"])
    worksheet.append(["São Borja", 2020, 10.5])
    worksheet.append(["São Borja", 2021, 11.5])
    worksheet.append(["Total", None, "=SUM(C3:C4)"])

    hidden = workbook.create_sheet("Apoio")
    hidden.sheet_state = "hidden"
    hidden.append(["Código", "Descrição"])
    hidden.append([1, "Teste"])
    workbook.save(federal / "dados.xlsx")

    (municipal / "dados.csv").write_text(
        "Município;Ano;Valor\nSão Borja;2022;12,5\n",
        encoding="utf-8",
    )
    (municipal / "notas.pdf").write_bytes(b"%PDF-1.4")
    return snapshot


def test_profile_snapshot_records_supported_and_unsupported_files(tmp_path: Path) -> None:
    result = profile_snapshot(build_snapshot(tmp_path))

    assert len(result.files) == 3
    statuses = dict(zip(result.files["extension"], result.files["profile_status"], strict=True))
    assert statuses["xlsx"] == "PROFILED"
    assert statuses["csv"] == "PROFILED"
    assert statuses["pdf"] == "UNSUPPORTED_FORMAT"
    assert len(result.sheets) == 3


def test_profile_detects_header_candidate_types_and_years(tmp_path: Path) -> None:
    result = profile_snapshot(build_snapshot(tmp_path))
    data_sheet = result.sheets.loc[result.sheets["sheet_name"].eq("Dados")].iloc[0]

    assert data_sheet["header_row_candidate_estimate"] == 2
    assert data_sheet["header_confidence_estimate"] == "HIGH"
    assert data_sheet["year_min_observed"] == 2020
    assert data_sheet["year_max_observed"] == 2021

    value_column = result.columns.loc[
        result.columns["relative_path"].str.endswith("dados.xlsx")
        & result.columns["sheet_name"].eq("Dados")
        & result.columns["header_normalized"].eq("valor")
    ].iloc[0]
    assert value_column["decimal_count"] == 2
    assert value_column["formula_count"] == 1


def test_profile_groups_exact_normalized_schemas(tmp_path: Path) -> None:
    result = profile_snapshot(build_snapshot(tmp_path))

    assert result.schema_groups["schema_signature_sha256"].nunique() == 1
    assert len(result.schema_groups) == 2
    assert set(result.schema_groups["group_size"]) == {2}


def test_normalization_and_latest_snapshot_resolution(tmp_path: Path) -> None:
    root = tmp_path / "snapshots"
    (root / ".partial").mkdir(parents=True)
    (root / "snapshot-001").mkdir()
    (root / "snapshot-002").mkdir()

    assert normalize_label("Município / Código") == "municipio_codigo"
    assert latest_snapshot(root).name == "snapshot-002"


def test_profile_outputs_are_tabular_dataframes(tmp_path: Path) -> None:
    result = profile_snapshot(build_snapshot(tmp_path))

    assert isinstance(result.files, pd.DataFrame)
    assert isinstance(result.sheets, pd.DataFrame)
    assert isinstance(result.columns, pd.DataFrame)
    assert isinstance(result.schema_groups, pd.DataFrame)
