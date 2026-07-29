from pathlib import Path

import pandas as pd
import pytest

from sbmi.complementary_temporal_matrix import (
    build_complementary_temporal_matrix,
)


def _inputs(tmp_path: Path) -> tuple[Path, Path, Path]:
    values = pd.DataFrame([
        {
            "source_id": "source", "query_id": "q1", "dimension": "educacao",
            "reference_year": "2024", "field_name": "Matrículas",
        },
        {
            "source_id": "source", "query_id": "q1", "dimension": "educacao",
            "reference_year": "2026", "field_name": "Matrículas",
        },
    ])
    register = pd.DataFrame([{
        "source_id": "source", "query_id": "q1", "dimension": "educacao",
        "field_name": "Matrículas", "normalized_name": "matriculas",
        "classification": "COMPLEMENTARY",
        "decision": "VERIFY_PRIMARY_SOURCE_BEFORE_INTEGRATION",
    }])
    facts = pd.DataFrame([{
        "theme": "economy", "reference_year": 2025,
        "indicator_id": "economy.x", "indicator_name": "Produção",
        "source_dataset": "sidra",
    }])
    values_path = tmp_path / "values.csv"
    register_path = tmp_path / "register.csv"
    facts_path = tmp_path / "facts.parquet"
    values.to_csv(values_path, index=False)
    register.to_csv(register_path, index=False)
    facts.to_parquet(facts_path, index=False)
    return values_path, register_path, facts_path


def _run(tmp_path: Path):
    values, register, facts = _inputs(tmp_path)
    return build_complementary_temporal_matrix(
        values_path=values,
        semantic_register_path=register,
        canonical_facts_path=facts,
        output_root=tmp_path / "audit",
        run_id="run",
        start_year=2024,
        end_year=2026,
    )


def test_builds_year_by_year_matrix_without_inferring_continuity(tmp_path):
    result = _run(tmp_path)
    candidate = result.matrix.loc[
        result.matrix.evidence_origin.eq("complementary_candidate")
    ]
    assert candidate.reference_year.tolist() == [2024, 2025, 2026]
    assert candidate.evidence_status.tolist() == ["OBSERVED", "GAP", "OBSERVED"]
    assert len(result.matrix) == 6
    assert result.validation.status.eq("PASS").all()
    assert (result.output_path / "indicator_temporal_coverage.csv").is_file()


def test_preserves_only_existing_dimensions(tmp_path):
    result = _run(tmp_path)
    assert set(result.dimension_priority.dimension) >= {
        "educacao", "economia_estrutura_produtiva"
    }
    assert len(result.dimension_priority) == 10
    assert int(result.validation.set_index("indicator").loc[
        "canonical_rows_promoted", "value"
    ]) == 0


def test_refuses_overwrite(tmp_path):
    values, register, facts = _inputs(tmp_path)
    output_root = tmp_path / "audit"
    build_complementary_temporal_matrix(
        values_path=values,
        semantic_register_path=register,
        canonical_facts_path=facts,
        output_root=output_root,
        run_id="run",
        start_year=2024,
        end_year=2026,
    )
    with pytest.raises(FileExistsError):
        build_complementary_temporal_matrix(
            values_path=values,
            semantic_register_path=register,
            canonical_facts_path=facts,
            output_root=output_root,
            run_id="run",
            start_year=2024,
            end_year=2026,
        )
