"""CLI da auditoria de linhagem RAIS."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.rais_lineage_audit import audit_rais_lineage, write_rais_lineage_audit


def main() -> None:
    run_id = f"rais-lineage-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = audit_rais_lineage(
        Path(".data/snapshots/sources/rais/rais-raw-20260729-043100"),
        Path(".data/snapshots/derived_products/derived-products-20260723/processed/rais"),
    )
    output = write_rais_lineage_audit(
        result, Path(".data/audit/base_territorial/rais_lineage") / run_id
    )
    summary = result.summary.set_index("indicator")["value"]
    print(f"output_path={output}")
    for indicator in (
        "raw_files",
        "processed_files",
        "candidate_pairs",
        "content_equivalent_pairs",
        "value_difference_pairs",
        "decimal_separator_loss_cells",
        "raw_value_lost_cells",
        "unsupported_xls_files",
        "unmatched_processed_files",
    ):
        print(f"{indicator}={summary[indicator]}")
    print("promotion_allowed=0")
    print("external_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
