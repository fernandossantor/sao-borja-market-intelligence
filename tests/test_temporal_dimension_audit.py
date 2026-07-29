from pathlib import Path

import pandas as pd
import pytest

from sbmi.temporal_dimension_audit import DIMENSIONS, audit_temporal_dimensions


def _run(tmp_path: Path):
    canonical = tmp_path / "canonical"
    canonical.mkdir()
    pd.DataFrame([
        {"theme": "economy", "reference_year": year, "indicator_id": "economic.x",
         "source_dataset": "sidra"}
        for year in range(1996, 2025)
    ] + [
        {"theme": "demography", "reference_year": 2022, "indicator_id": "demography.x",
         "source_dataset": "census"},
        {"theme": "social", "reference_year": 2026, "indicator_id": "social.x",
         "source_dataset": "ips"},
    ]).to_parquet(canonical / "fact_territorial_indicator.parquet", index=False)
    return audit_temporal_dimensions(canonical, tmp_path / "audit", "run")


def test_reports_only_existing_dimensions_and_explicit_gaps(tmp_path):
    result = _run(tmp_path)
    assert set(result.coverage.dimension) == set(DIMENSIONS)
    economy = result.coverage.set_index("dimension").loc[
        "economia_estrutura_produtiva"
    ]
    assert (economy.first_year, economy.last_year, economy.years_covered) == (
        1996, 2024, 29
    )
    assert economy.coverage_status == "PARTIAL"
    assert result.coverage.coverage_status.eq("NO_CANONICAL_EVIDENCE").sum() == 7
    assert (result.output_path / "temporal_dimension_gaps.csv").is_file()


def test_refuses_overwrite(tmp_path):
    result = _run(tmp_path)
    with pytest.raises(FileExistsError):
        audit_temporal_dimensions(
            result.output_path.parent.parent / "canonical",
            result.output_path.parent,
            result.output_path.name,
        )
