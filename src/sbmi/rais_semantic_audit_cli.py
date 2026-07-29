"""CLI da auditoria semântica local da família RAIS."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.rais_semantic_audit import audit_rais_semantics, write_rais_semantic_audit


def main() -> None:
    run_id = f"rais-semantic-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = audit_rais_semantics(
        Path(".data/snapshots/derived_products/derived-products-20260723")
    )
    output = write_rais_semantic_audit(
        result, Path(".data/audit/base_territorial/rais_semantic") / run_id
    )
    summary = result.summary.set_index("indicator")["value"]
    print(f"output_path={output}")
    for indicator in (
        "processed_files",
        "processed_rows",
        "unique_schemas",
        "exact_duplicate_groups",
        "unmapped_semantic_rows",
        "future_period_rows",
    ):
        print(f"{indicator}={summary[indicator]}")
    print("promotion_allowed=0")
    print("external_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
