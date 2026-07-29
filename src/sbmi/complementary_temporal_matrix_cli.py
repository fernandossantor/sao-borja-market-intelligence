"""CLI da matriz temporal das fontes complementares."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.complementary_temporal_matrix import build_complementary_temporal_matrix


def main() -> None:
    run_id = f"complementary-temporal-matrix-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = build_complementary_temporal_matrix(
        values_path=Path(
            ".data/curated/base_territorial/complementary_source_values/"
            "complementary-source-values-20260729-220618/complementary_values.csv"
        ),
        semantic_register_path=Path(
            ".data/audit/base_territorial/complementary_semantic_audit/"
            "complementary-semantic-audit-20260729-220823/"
            "indicator_semantic_register.csv"
        ),
        canonical_facts_path=Path(
            ".data/curated/base_territorial/canonical_extended/"
            "canonical-extended-20260729-200621/fact_territorial_indicator.parquet"
        ),
        output_root=Path(
            ".data/audit/base_territorial/complementary_temporal_matrix"
        ),
        run_id=run_id,
    )
    candidates = result.validation.set_index("indicator").loc[
        "candidate_contracts", "value"
    ]
    print(f"run_id={run_id}")
    print(f"matrix_rows={len(result.matrix)}")
    print(f"candidate_indicators={int(candidates)}")
    print("canonical_rows_promoted=0")
    print(f"output={result.output_path}")


if __name__ == "__main__":
    main()
