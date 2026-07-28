from pathlib import Path

import pandas as pd
import pytest
from openpyxl import Workbook
from openpyxl.comments import Comment

from sbmi.demography_census_provenance import (
    audit_census_provenance,
    write_census_provenance_audit,
)


def _lineage(relative_path: str = "raw/social/censo.xlsx") -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dataset_identity": "censo 2022 teste sao borja rs",
                "raw_source_count": 1,
                "processed_product_count": 1,
                "raw_source_paths": relative_path,
                "processed_product_paths": "processed/social/censo.parquet",
                "lineage_match_status": "MATCHED_ONE_TO_ONE_BY_NAME",
            }
        ]
    )


def _manifest(relative_path: str, path: Path) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": relative_path,
                "expected_size_bytes": path.stat().st_size,
                "downloaded_size_bytes": path.stat().st_size,
                "expected_sha256": "a" * 64,
                "local_sha256": "a" * 64,
                "verification_status": "VERIFIED",
            }
        ]
    )


def _write_source_workbook(path: Path, *, with_provenance: bool = True) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Dados"
    sheet.append(["Município", "Porcentagem de domicílios", "Área km2"])
    sheet.append(["São Borja", 23.18, 3616.69])
    sheet["B2"].number_format = "0.00"
    sheet["C2"].number_format = "0.00"
    if with_provenance:
        workbook.properties.creator = "Equipe de dados"
        workbook.properties.lastModifiedBy = "Analista"
        workbook.properties.title = "Censo 2022 - São Borja"
        sheet["A4"] = "Fonte: IBGE / Censo 2022"
        sheet["A5"] = "https://sidra.ibge.gov.br/"
        sheet["A5"].hyperlink = "https://sidra.ibge.gov.br/"
        sheet["A6"].comment = Comment("Unidade: porcentagem", "Equipe")
    workbook.save(path)


def test_audit_detects_embedded_source_domain_and_unit_hints(
    tmp_path: Path,
) -> None:
    relative_path = "raw/social/censo.xlsx"
    workbook_path = tmp_path / relative_path
    _write_source_workbook(workbook_path)

    result = audit_census_provenance(
        _lineage(relative_path),
        _manifest(relative_path, workbook_path),
        raw_snapshot_root=tmp_path,
    )
    workbook = result.workbooks.iloc[0]
    evidence_kinds = set(result.evidence["evidence_kind"])
    unit_hints = set(result.columns["unit_hint"])

    assert workbook["provenance_status"] == "EMBEDDED_PROVENANCE_EVIDENCE_DETECTED"
    assert workbook["source_authority_status"] == "PENDING_EXTERNAL_VERIFICATION"
    assert workbook["detected_domains"] == "sidra.ibge.gov.br"
    assert "SOURCE_LABEL" in evidence_kinds
    assert "HYPERLINK_TARGET" in evidence_kinds
    assert "PERCENT" in unit_hints
    assert "SQUARE_KILOMETERS" in unit_hints


def test_audit_keeps_document_metadata_separate_from_authority(
    tmp_path: Path,
) -> None:
    relative_path = "raw/social/censo.xlsx"
    workbook_path = tmp_path / relative_path
    _write_source_workbook(workbook_path, with_provenance=False)
    workbook = Workbook()
    workbook.active.append(["População"])
    workbook.active.append([100])
    workbook.properties.creator = "Pessoa não verificada"
    workbook.save(workbook_path)

    result = audit_census_provenance(
        _lineage(relative_path),
        _manifest(relative_path, workbook_path),
        raw_snapshot_root=tmp_path,
    )
    row = result.workbooks.iloc[0]

    assert row["provenance_status"] == "DOCUMENT_METADATA_ONLY"
    assert row["source_authority_status"] == "NOT_ESTABLISHED"
    assert row["conceptual_validation_status"] == "NOT_VALIDATED"


def test_audit_rejects_path_outside_snapshot(tmp_path: Path) -> None:
    outside = tmp_path.parent / "outside.xlsx"
    _write_source_workbook(outside)
    relative_path = "../outside.xlsx"

    with pytest.raises(ValueError, match="fora da captura"):
        audit_census_provenance(
            _lineage(relative_path),
            _manifest(relative_path, outside),
            raw_snapshot_root=tmp_path,
        )


def test_summary_does_not_claim_authority_or_conceptual_validation(
    tmp_path: Path,
) -> None:
    relative_path = "raw/social/censo.xlsx"
    workbook_path = tmp_path / relative_path
    _write_source_workbook(workbook_path)

    result = audit_census_provenance(
        _lineage(relative_path),
        _manifest(relative_path, workbook_path),
        raw_snapshot_root=tmp_path,
    )
    summary = result.summary.set_index("indicator")

    assert int(summary.loc["workbooks_reviewed", "value"]) == 1
    assert int(summary.loc["manifest_verified_workbooks", "value"]) == 1
    assert int(summary.loc["source_authority_reviews_completed", "value"]) == 0
    assert int(summary.loc["conceptually_validated_datasets", "value"]) == 0


def test_write_provenance_audit_is_atomic_and_refuses_overwrite(
    tmp_path: Path,
) -> None:
    relative_path = "raw/social/censo.xlsx"
    workbook_path = tmp_path / relative_path
    _write_source_workbook(workbook_path)
    result = audit_census_provenance(
        _lineage(relative_path),
        _manifest(relative_path, workbook_path),
        raw_snapshot_root=tmp_path,
    )
    target = tmp_path / "audit"

    written = write_census_provenance_audit(result, target)

    assert written == target.resolve()
    assert (target / "demography_census_workbook_provenance.csv").is_file()
    assert (target / "demography_census_sheet_register.csv").is_file()
    assert (target / "demography_census_column_metadata.csv").is_file()
    assert (target / "demography_census_provenance_evidence.csv").is_file()
    assert (target / "demography_census_provenance_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_census_provenance_audit(result, target)
