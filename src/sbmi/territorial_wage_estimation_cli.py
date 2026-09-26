"""CLI for RAIS workers × RFB territorial wage estimation."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from sbmi.territorial_wage_estimation import (
    build_source_manifest,
    estimate_territorial_wages,
    write_wage_outputs,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rais-workers-csv", type=Path, required=True)
    parser.add_argument("--rfb-cells-csv", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--municipality-code", default="431800")
    parser.add_argument("--rais-reference-year", default="2025")
    parser.add_argument("--rfb-competence", default="2026-08")
    parser.add_argument("--expected-business-active-links", type=int, default=8595)
    args = parser.parse_args()

    rais = pd.read_csv(args.rais_workers_csv, encoding="utf-8", dtype=str, keep_default_na=False)
    rfb = pd.read_csv(args.rfb_cells_csv, dtype=str)
    result = estimate_territorial_wages(
        rais,
        rfb,
        municipality_code=args.municipality_code,
        expected_business_active_links=args.expected_business_active_links,
    )
    manifest = build_source_manifest(args.rais_workers_csv, args.rfb_cells_csv)
    metadata = pd.DataFrame(
        [
            ("municipality_code", args.municipality_code, "parameter"),
            ("rais_reference_year", args.rais_reference_year, "observed_source_period"),
            ("rfb_competence", args.rfb_competence, "observed_source_period"),
            ("rais_active_link_rule", "Ind Vínculo Ativo 31/12 - Código = 1", "method"),
            ("rais_abandoned_link_rule", "Ind Vínculo Abandonado - Código = 0", "method"),
            (
                "temporal_comparability",
                "RAIS 2025-12-31 versus RFB 2026-08; estimates are not same-period observations",
                "limitation",
            ),
            (
                "december_metric",
                "sum of Vl Rem Dezembro Nom where informed; not annual payroll",
                "method",
            ),
            (
                "primary_wage_metric",
                "sum of Vl Rem Média Nom across active non-abandoned business links; "
                "not annual payroll",
                "method",
            ),
            (
                "estimation_rule",
                "RAIS employment and remuneration allocated by RFB establishment shares "
                "within hierarchical CNAE/nature cells",
                "method",
            ),
        ],
        columns=["field", "value", "nature"],
    )
    write_wage_outputs(
        result,
        args.output_dir,
        source_manifest=manifest,
        run_metadata=metadata,
    )
    summary = result.summary.set_index("indicator")["value"]
    print(
        f"rais_business_active_links={summary['rais_business_active_links']:.0f}\n"
        f"estimated_external_active_links_share_pct="
        f"{summary['estimated_external_active_links_share_pct']:.6f}\n"
        f"estimated_external_avg_rem_sum_share_pct="
        f"{summary['estimated_external_avg_rem_sum_share_pct']:.6f}\n"
        f"estimated_external_dec_mass_share_pct="
        f"{summary['estimated_external_dec_mass_share_pct']:.6f}\n"
        f"output_dir={args.output_dir}"
    )


if __name__ == "__main__":
    main()
