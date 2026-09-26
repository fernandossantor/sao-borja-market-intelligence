"""CLI para a camada curated/normalized de séries públicas de mercado."""

from __future__ import annotations

import argparse
from pathlib import Path

from public_market_series_curated import build_curated_public_market_series


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-series-root", type=Path, required=True)
    parser.add_argument("--taxonomy-csv", type=Path, required=True)
    parser.add_argument("--crosswalk-md", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--execution-id", default="public-market-series-curated-v001")
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--taxonomy-run-id", required=True)
    args = parser.parse_args()

    result = build_curated_public_market_series(
        args.public_series_root,
        args.taxonomy_csv,
        args.crosswalk_md,
        args.output_dir,
        execution_id=args.execution_id,
        source_run_id=args.source_run_id,
        taxonomy_run_id=args.taxonomy_run_id,
    )
    print(f"execution_id={args.execution_id}")
    print(f"output_dir={result.output_dir}")
    print(f"validation_pass={result.validation['status'].eq('PASS').all()}")
    print(f"manifest_files={len(result.manifest)}")
    print("STATUS=PUBLIC_MARKET_SERIES_CURATED_OK")


if __name__ == "__main__":
    main()