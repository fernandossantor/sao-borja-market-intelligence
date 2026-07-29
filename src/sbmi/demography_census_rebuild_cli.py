"""CLI da reconstrução incremental dos produtos censitários em quarentena."""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from sbmi.demography_census_rebuild import rebuild_census_products


def main() -> None:
    stamp = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    run_id = f"demography-census-rebuild-{stamp}"
    result = rebuild_census_products(
        source_root=Path(
            ".data/snapshots/sources/demography_census/"
            "census-2022-sao-borja-sources-20260724/raw/social"
        ),
        historical_root=Path(
            ".data/snapshots/derived_products/derived-products-20260723/processed/social"
        ),
        staging_root=Path(".data/staging/base_territorial/demography/census_rebuild"),
        curated_root=Path(".data/curated/base_territorial/demography/census_rebuild"),
        audit_root=Path(".data/audit/base_territorial/demography_census_rebuild"),
        run_id=run_id,
    )
    print(f"staging_path={result.staging_path}")
    print(f"curated_path={result.curated_path}")
    print(f"audit_path={result.audit_path}")
    for row in result.summary.itertuples(index=False):
        print(f"{row.indicator}={row.value}")
    print("status=ok")


if __name__ == "__main__":
    main()
