"""CLI do diagnóstico temporal das dimensões existentes."""

from datetime import UTC, datetime
from pathlib import Path

from sbmi.temporal_dimension_audit import audit_temporal_dimensions


def main() -> None:
    canonical_root = Path(".data/curated/base_territorial/canonical_extended")
    candidates = sorted(path for path in canonical_root.iterdir() if path.is_dir())
    if not candidates:
        raise FileNotFoundError("Execução canônica estendida ausente")
    run_id = f"temporal-dimension-audit-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    result = audit_temporal_dimensions(
        candidates[-1],
        Path(".data/audit/base_territorial/temporal_dimension"),
        run_id,
    )
    print(f"run_id={run_id}")
    print(f"output_path={result.output_path}")
    print(
        "dimensions_with_evidence="
        f"{int(result.coverage['years_covered'].gt(0).sum())}"
    )


if __name__ == "__main__":
    main()
