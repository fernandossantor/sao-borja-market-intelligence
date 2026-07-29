"""CLI da auditoria semântica fiscal."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.fiscal_semantic_audit import audit_fiscal_semantics, write_fiscal_semantic_audit


def main() -> None:
    run_id = f"fiscal-semantic-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = audit_fiscal_semantics(
        Path(".data/staging/new_files/new-files-20260723"),
        Path(".data/snapshots/derived_products/derived-products-20260723/processed/fiscal"),
    )
    output = write_fiscal_semantic_audit(
        result, Path(".data/audit/base_territorial/fiscal_semantic") / run_id,
    )
    summary = result.summary.set_index("indicator")["value"]
    print(f"output_path={output}")
    print(f"staging_rows={summary['staging_rows']}")
    print(f"federal_overlap_rows={summary['federal_overlap_rows']}")
    print(f"federal_staging_only_rows={summary['federal_staging_only_rows']}")
    print(f"historical_duplicate_excess={summary['historical_duplicate_excess']}")
    print("promotion_allowed=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
