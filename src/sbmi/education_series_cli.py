"""CLI da curadoria local das séries educacionais."""

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.education_series import curate_education_series

BASE = Path(
    ".data/snapshots/web/complementary_source_values/complementary-source-values-20260729-220618/sebrae_observatorio_profile"
)


def main() -> None:
    argparse.ArgumentParser(description=__doc__).parse_args()
    execution_id = f"education-series-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"
    sources = {
        name: BASE / f"sebrae_candidate_{candidate}.json"
        for name, candidate in {
            "ideb": "003",
            "rates": "006",
            "basic_enrollment": "007",
            "early_enrollment": "008",
            "higher_education": "090",
        }.items()
    }
    roots = {
        layer: Path(f".data/{layer}/base_territorial/education_series")
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_education_series(sources=sources, roots=roots, execution_id=execution_id)
    print(f"execution_id={execution_id}\nrows={len(result.values)}\naudit={result.paths['audit']}")


if __name__ == "__main__":
    main()
