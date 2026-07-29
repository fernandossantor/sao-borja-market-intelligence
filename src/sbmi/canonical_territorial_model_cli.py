"""CLI do modelo canônico territorial."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.canonical_territorial_model import build_canonical_territorial_model


def main() -> None:
    run_id = f"canonical-territorial-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = build_canonical_territorial_model(
        census_root=Path(".data/curated/base_territorial/demography/census_rebuild/demography-census-rebuild-20260729-001426"),
        idsc_root=Path(".data/curated/base_territorial/social/idsc/2025"),
        ips_root=Path(".data/curated/base_territorial/social/ips/published_2024_2026"),
        output_root=Path(".data/curated/base_territorial/canonical"), run_id=run_id)
    print(f"output_path={result.output_path}")
    print(f"fact_rows={len(result.facts)}")
    print(f"distinct_indicators={len(result.indicators)}")
    print(f"distinct_territories={len(result.territories)}")
    print("status=ok")


if __name__ == "__main__":
    main()
