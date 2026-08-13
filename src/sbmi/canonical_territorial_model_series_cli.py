"""CLI da extensão canônica das séries territoriais."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.canonical_territorial_model_series import build_series_canonical_model


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    run_id = f"canonical-series-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    root = Path(".data/curated/base_territorial")
    result = build_series_canonical_model(
        base_root=root / "canonical_extended/canonical-extended-20260729-200621",
        series_paths={
            "demography_historical": root
            / "demography_historical_values/demography-historical-values-20260813-002503"
            / "sidra_historical_values.csv",
            "demography_census": root
            / "demography_census_series/demography-census-series-20260813-002505"
            / "demography_census_series.csv",
            "economy_gdp": root
            / "economy_gdp_series/economy-gdp-series-20260813-002507"
            / "economy_gdp_series.csv",
            "business_employment": root
            / "business_employment_series/business-employment-series-20260813-002203"
            / "business_employment_series.csv",
            "education": root
            / "education_series/education-series-20260813-002204"
            / "education_series.csv",
            "public_finance": root
            / "public_finance_series/public-finance-series-20260813-002204"
            / "public_finance_series.csv",
            "siconfi_dca": root
            / "siconfi_dca_series/siconfi-dca-series-20260813-002543"
            / "siconfi_dca_series.csv",
        },
        output_root=root / "canonical_series",
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"output_path={result.output_path}")
    print(f"fact_rows={len(result.facts)}")
    print(f"distinct_indicators={len(result.indicators)}")


if __name__ == "__main__":
    main()
