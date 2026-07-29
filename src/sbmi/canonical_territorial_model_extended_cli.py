"""CLI da extensão canônica histórica."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.canonical_territorial_model_extended import build_extended_canonical_model


def main() -> None:
    run_id = f"canonical-extended-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = build_extended_canonical_model(
        census_root=Path(
            ".data/curated/base_territorial/demography/census_rebuild/"
            "demography-census-rebuild-20260729-001426"
        ),
        idsc_root=Path(".data/curated/base_territorial/social/idsc/2025"),
        ips_root=Path(
            ".data/curated/base_territorial/social/ips/published_2024_2026"
        ),
        sidra_root=Path(
            ".data/curated/base_territorial/sidra_historical_values/"
            "sidra-historical-values-20260729-195000"
        ),
        output_root=Path(".data/curated/base_territorial/canonical_extended"),
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"output_path={result.output_path}")
    print(f"fact_rows={len(result.facts)}")
    print(f"distinct_indicators={len(result.indicators)}")


if __name__ == "__main__":
    main()
