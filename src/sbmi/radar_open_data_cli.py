"""CLI para auditoria exploratória dos CSVs do Radar de Mercado."""
from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

from sbmi.radar_open_data import audit_radar_open_data


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audita CSVs públicos do Radar de Mercado sem promoção canônica."
    )
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(".data/audit/receita_rs/radar_open_data"),
    )
    parser.add_argument("--execution-id")
    args = parser.parse_args()
    execution_id = args.execution_id or (
        f"radar-open-data-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    )
    result = audit_radar_open_data(
        source_dir=args.source_dir,
        output_root=args.output_root,
        execution_id=execution_id,
    )
    print(f"execution_id={execution_id}")
    print(f"csv_files={len(result.schema_inventory)}")
    print(f"rice_rows={len(result.ncm_matches)}")
    print(f"rice_composition_rows={len(result.composition_summary)}")
    print("canonical_rows_promoted=0")
    print(f"output={result.output_path}")


if __name__ == "__main__":
    main()
