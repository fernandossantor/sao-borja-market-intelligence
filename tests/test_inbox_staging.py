from decimal import Decimal
from pathlib import Path

import pandas as pd
import pytest
from openpyxl import Workbook

from sbmi.inbox_staging import (
    FEDERAL_HEADERS,
    ESTADUAL_ICMS_HEADERS,
    StagingResult,
    build_staging,
    classify_dataset,
    parse_decimal_value,
    write_staging_output,
)


def _write_workbook(path: Path, headers: tuple[str, ...], rows: list[list[object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Dados"
    worksheet.append(["Relatório", *([None] * (len(headers) - 1))])
    worksheet.append(list(headers))
    for row in rows:
        worksheet.append(row)
    workbook.save(path)
    workbook.close()


def _profile(*paths: str, widths: dict[str, int]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": path,
                "sheet_name": "Dados",
                "sheet_index": 1,
                "header_row_candidate_estimate": 2,
                "observed_max_column": widths[path],
            }
            for path in paths
        ]
    )


def test_parse_decimal_value_preserves_observed_decimal() -> None:
    assert parse_decimal_value("1.234,56") == Decimal("1234.56")
    assert parse_decimal_value(10.5) == Decimal("10.5")
    assert parse_decimal_value("") is None


def test_classify_dataset_requires_explicit_contract() -> None:
    assert classify_dataset("Federal", FEDERAL_HEADERS) == "federal_transferencias"
    assert classify_dataset("Estadual", ESTADUAL_ICMS_HEADERS) == "estadual_icms"
    with pytest.raises(ValueError, match="Estrutura sem contrato"):
        classify_dataset("Federal", ("coluna_desconhecida",))


def test_build_staging_excludes_content_copy_and_flags_icms_rows(tmp_path: Path) -> None:
    federal_primary = "raw/new_files/Federal/programa.xlsx"
    federal_copy = "raw/new_files/Federal/programa(1).xlsx"
    icms = "raw/new_files/Estadual/icms.xlsx"

    federal_row = [
        "01/2026",
        "Corrente",
        "Município",
        "RS",
        "São Borja",
        "123",
        "São Borja",
        "Saúde",
        "Programa",
        "Ação",
        "Linguagem",
        "1.234,56",
    ]
    _write_workbook(tmp_path / federal_primary, FEDERAL_HEADERS, [federal_row])
    _write_workbook(tmp_path / federal_copy, FEDERAL_HEADERS, [federal_row])
    icms_rows = [
        ["2026-01-02", "1", "São Borja", 100, 0.5, "R", "D", "I", "C"],
        ["2026-01-02", "1", "São Borja", 100, 0.5, "R", "D", "I", "C"],
    ]
    _write_workbook(tmp_path / icms, ESTADUAL_ICMS_HEADERS, icms_rows)

    profile = _profile(
        federal_primary,
        federal_copy,
        icms,
        widths={
            federal_primary: len(FEDERAL_HEADERS),
            federal_copy: len(FEDERAL_HEADERS),
            icms: len(ESTADUAL_ICMS_HEADERS),
        },
    )
    content_duplicates = pd.DataFrame(
        [
            {
                "suggested_duplicate_path": federal_copy,
                "suggestion_basis": "COPY_SUFFIX_HEURISTIC",
                "duplicate_class": "CONTENT_DUPLICATE",
            }
        ]
    )
    duplicate_rows = pd.DataFrame(
        [
            {
                "relative_path": icms,
                "normalized_row_hash": "abc",
                "occurrence_count": 2,
                "source_row_numbers": "3|4",
                "duplicate_class": "STRICT_EXACT_ROW",
                "review_status": "PENDING_SOURCE_VALIDATION",
            }
        ]
    )

    result = build_staging(
        tmp_path,
        profile,
        content_duplicates,
        duplicate_rows,
        snapshot_id="new-files-20260723",
    )

    federal = result.datasets["federal_transferencias"]
    icms_frame = result.datasets["estadual_icms"]
    assert len(federal) == 1
    assert federal.loc[0, "valor_transferido"] == Decimal("1234.56")
    assert len(icms_frame) == 2
    assert icms_frame["_duplicate_group_id"].notna().sum() == 2
    dispositions = result.source_manifest.set_index("relative_path")["disposition"]
    assert dispositions[federal_copy] == "EXCLUDED_CONTENT_DUPLICATE_FROM_STAGING"


def test_write_staging_output_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = StagingResult(
        datasets={"teste": pd.DataFrame([{"valor": 1}])},
        source_manifest=pd.DataFrame([{"relative_path": "a.xlsx"}]),
        quality_summary=pd.DataFrame(
            [{"indicator": "staging_rows", "value": 1, "nature": "calculated"}]
        ),
    )
    target = tmp_path / "staging"
    written = write_staging_output(result, target)

    assert written == target.resolve()
    assert (target / "teste.parquet").is_file()
    assert (target / "source_manifest.csv").is_file()
    with pytest.raises(FileExistsError):
        write_staging_output(result, target)
