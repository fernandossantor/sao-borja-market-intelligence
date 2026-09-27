"""CLI da camada analítica das séries públicas do SBMI."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.public_market_series_analysis import build_public_market_series_analysis


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--curated-root", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--execution-id", required=True)
    parser.add_argument("--source-run-id", required=True)
    args = parser.parse_args()

    result = build_public_market_series_analysis(
        args.curated_root,
        args.output_dir,
        execution_id=args.execution_id,
        source_run_id=args.source_run_id,
    )
    print(f"output_dir={result.output_dir}")
    print(f"validation_pass={result.validation['status'].eq('PASS').all()}")
    print("STATUS=PUBLIC_MARKET_SERIES_ANALYSIS_OK")


if __name__ == "__main__":
    main()