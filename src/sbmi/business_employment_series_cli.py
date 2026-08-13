"""CLI da curadoria local de empresas e emprego."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.business_employment_series import curate_business_employment_series

BASE = Path(
    ".data/snapshots/web/complementary_source_values/complementary-source-values-20260729-220618/sebrae_observatorio_profile"
)


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    execution_id = f"business-employment-series-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"
    roots = {
        layer: Path(f".data/{layer}/base_territorial/business_employment_series")
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_business_employment_series(
        establishments_path=BASE / "sebrae_candidate_113.json",
        workers_path=BASE / "sebrae_candidate_116.json",
        roots=roots,
        execution_id=execution_id,
    )
    print(f"execution_id={execution_id}\nrows={len(result.values)}\naudit={result.paths['audit']}")


if __name__ == "__main__":
    main()
