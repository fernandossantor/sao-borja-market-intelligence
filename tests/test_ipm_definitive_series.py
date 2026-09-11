from __future__ import annotations

from pathlib import Path

import pytest

from sbmi.ipm_archive_audit import IpmArchiveAuditResult
from sbmi.ipm_definitive_series import (
    build_ipm_series_from_audits,
    parse_final_ipm,
)


def _result(year: int, value: str) -> IpmArchiveAuditResult:
    return IpmArchiveAuditResult(
        distribution_year=year,
        archive_path=Path(f"ipm_{year}.zip"),
        archive_bytes=1000 + year,
        archive_sha256=f"{year:064x}"[-64:],
        import_member="DAIM545X.TXT",
        encoding="utf-8-sig",
        matched_lines=(f"117 SAO BORJA 123 456 {value}",),
    )


def test_parse_final_ipm_uses_only_last_six_decimal_field() -> None:
    assert str(parse_final_ipm("117 SAO BORJA 1,234567 0,533647")) == "0.533647"
    with pytest.raises(ValueError, match="seis casas"):
        parse_final_ipm("117 SAO BORJA 0,53364")


def test_build_ipm_series_requires_complete_benchmarked_series() -> None:
    results = []
    for year in range(2003, 2027):
        if year == 2025:
            value = "0,527880"
        elif year == 2026:
            value = "0,533647"
        else:
            value = f"0,{500000 + (year - 2003):06d}"
        results.append(_result(year, value))

    outputs = build_ipm_series_from_audits(results, execution_id="test-v001")
    assert len(outputs.series) == 24
    assert outputs.validation["status"].eq("PASS").all()

    ipm_2025 = outputs.series.loc[
        outputs.series.distribution_year == 2025,
        "ipm_definitive",
    ].iloc[0]
    yoy_2026 = outputs.series.loc[
        outputs.series.distribution_year == 2026,
        "yoy_change_pct",
    ].iloc[0]
    assert ipm_2025 == pytest.approx(0.52788)
    assert yoy_2026 == pytest.approx(1.0924831401)
    assert len(outputs.source_manifest) == 24


def test_build_ipm_series_rejects_multiple_municipality_matches() -> None:
    results = [_result(year, "0,500000") for year in range(2003, 2027)]
    bad = results[-1]
    results[-1] = IpmArchiveAuditResult(
        distribution_year=bad.distribution_year,
        archive_path=bad.archive_path,
        archive_bytes=bad.archive_bytes,
        archive_sha256=bad.archive_sha256,
        import_member=bad.import_member,
        encoding=bad.encoding,
        matched_lines=("117 SAO BORJA 0,533647", "117 SAO BORJA 0,533647"),
    )
    with pytest.raises(ValueError, match="único match"):
        build_ipm_series_from_audits(results, execution_id="test-v001")
