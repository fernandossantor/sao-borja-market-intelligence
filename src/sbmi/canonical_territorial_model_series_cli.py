"""CLI da extensão canônica das séries territoriais."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.canonical_territorial_model_series import build_series_canonical_model

SERIES_ARGUMENTS = {
    "demography_historical": "--demography-historical-path",
    "demography_census": "--demography-census-path",
    "economy_gdp": "--economy-gdp-path",
    "business_employment": "--business-employment-path",
    "education": "--education-path",
    "public_finance": "--public-finance-path",
    "siconfi_dca": "--siconfi-dca-path",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-root", type=Path, required=True)
    for option in SERIES_ARGUMENTS.values():
        parser.add_argument(option, type=Path, required=True)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(".data/curated/base_territorial/canonical_series"),
    )
    parser.add_argument("--run-id")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run_id = args.run_id or f"canonical-series-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = build_series_canonical_model(
        base_root=args.base_root,
        series_paths={
            family: getattr(args, option.removeprefix("--").replace("-", "_"))
            for family, option in SERIES_ARGUMENTS.items()
        },
        output_root=args.output_root,
        run_id=run_id,
    )
    print(f"run_id={run_id}")
    print(f"output_path={result.output_path}")
    print(f"fact_rows={len(result.facts)}")
    print(f"distinct_indicators={len(result.indicators)}")


if __name__ == "__main__":
    main()
