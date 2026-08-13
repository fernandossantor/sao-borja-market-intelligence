"""CLI da série fiscal municipal."""

from __future__ import annotations

import argparse
from pathlib import Path

from .public_finance_series import curate_public_finance_series


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--execution-id", required=True)
    p.add_argument("--source-dir", type=Path, required=True)
    p.add_argument("--data-root", type=Path, default=Path(".data"))
    a = p.parse_args()
    files = {
        "revenue_total": "sebrae_candidate_021.json",
        "capital_expense": "sebrae_candidate_010.json",
        "current_expense": "sebrae_candidate_094.json",
        "revenue_categories": "sebrae_candidate_097.json",
        "transfer_categories": "sebrae_candidate_099.json",
    }
    roots = {
        x: a.data_root / x / "base_territorial" / "public_finance_series"
        for x in ("staging", "curated", "exports", "audit")
    }
    r = curate_public_finance_series(
        sources={k: a.source_dir / v for k, v in files.items()},
        roots=roots,
        execution_id=a.execution_id,
    )
    minimum_year = r.values.reference_year.min()
    maximum_year = r.values.reference_year.max()
    print(
        f"rows={len(r.values)} indicators={r.values.indicator_id.nunique()} "
        f"years={minimum_year}-{maximum_year}"
    )


if __name__ == "__main__":
    main()
