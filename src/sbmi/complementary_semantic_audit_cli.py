"""CLI da auditoria semântica das quatro fontes complementares."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.complementary_semantic_audit import audit_complementary_semantics


def main() -> None:
    audit_id = f"complementary-semantic-audit-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = audit_complementary_semantics(
        values_path=Path(
            ".data/curated/base_territorial/complementary_source_values/"
            "complementary-source-values-20260729-220618/complementary_values.csv"
        ),
        sebrae_inventory_path=Path(
            ".data/audit/base_territorial/complementary_sources/"
            "complementary-source-inventory-20260729-204156/"
            "candidate_query_inventory.csv"
        ),
        ips_baseline_path=Path(
            ".data/curated/base_territorial/social/ips/published_2024_2026/"
            "ips_published_summary_2024_2026.csv"
        ),
        output_root=Path(
            ".data/audit/base_territorial/complementary_semantic_audit"
        ),
        audit_id=audit_id,
    )
    print(f"audit_id={audit_id}")
    print(f"contracts={len(result.register)}")
    print(f"conflicts={int(result.register.classification.eq('CONFLICT').sum())}")
    print("canonical_rows_promoted=0")
    print("drive_operations=0")
    print(f"output={result.output_path}")


if __name__ == "__main__":
    main()
