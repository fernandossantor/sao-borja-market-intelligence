"""CLI for RAIS × RFB territorial employment estimation."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.territorial_employment_estimation import (
    build_source_manifest,
    estimate_territorial_employment,
    write_estimation_outputs,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rais-establishments-csv", type=Path, required=True)
    parser.add_argument("--rfb-cells-csv", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--municipality-code", default="431800")
    parser.add_argument("--rais-reference-year", default="2025")
    parser.add_argument("--rfb-competence", default="2026-08")
    args = parser.parse_args()

    rais = pd.read_csv(args.rais_establishments_csv, encoding="latin1", dtype=str)
    rfb = pd.read_csv(args.rfb_cells_csv, dtype=str)
    result = estimate_territorial_employment(
        rais,
        rfb,
        municipality_code=args.municipality_code,
    )
    manifest = build_source_manifest(args.rais_establishments_csv, args.rfb_cells_csv)
    metadata = pd.DataFrame(
        [
            ("municipality_code", args.municipality_code, "parameter"),
            ("rais_reference_year", args.rais_reference_year, "observed_source_period"),
            ("rfb_competence", args.rfb_competence, "observed_source_period"),
            (
                "temporal_comparability",
                "RAIS 2025-12-31 versus RFB 2026-08; estimates are not same-period observations",
                "limitation",
            ),
            (
                "estimation_rule",
                "RAIS active links allocated by RFB establishment shares "
                "within hierarchical CNAE/nature cells",
                "method",
            ),
        ],
        columns=["field", "value", "nature"],
    )
    write_estimation_outputs(
        result,
        args.output_dir,
        source_manifest=manifest,
        run_metadata=metadata,
    )
    summary = result.summary.set_index("indicator")["value"]
    print(
        f"rais_business_active_links={summary['rais_business_active_links']:.0f}\n"
        f"estimated_external_share_pct={summary['estimated_external_share_pct']:.6f}\n"
        f"exact_match_active_links_share_pct="
        f"{summary['exact_match_active_links_share_pct']:.6f}\n"
        f"output_dir={args.output_dir}"
    )


if __name__ == "__main__":
    main()
