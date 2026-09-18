"""CLI para auditoria exploratória dos CSVs do Radar de Mercado."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.radar_open_data import audit_radar_open_data


def _load_basket(path: Path) -> dict[str, str]:
    frame = pd.read_csv(path, dtype=str)
    required = {"ncm", "descricao"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(
            f"Arquivo da cesta deve conter as colunas ncm,descricao; faltam: {sorted(missing)}"
        )
    return {
        str(row.ncm).strip(): str(row.descricao).strip()
        for row in frame[["ncm", "descricao"]].itertuples(index=False)
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Audita CSVs públicos do Radar de Mercado sem promoção canônica. "
            "Sem cesta explícita, usa o piloto de arroz."
        )
    )
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(".data/audit/receita_rs/radar_open_data"),
    )
    parser.add_argument("--execution-id")
    parser.add_argument(
        "--basket-file",
        type=Path,
        help="CSV com colunas ncm,descricao para uma cesta auditável de produtos.",
    )
    parser.add_argument(
        "--basket-name",
        default="rice_default",
        help="Nome de controle da cesta usada na execução.",
    )
    args = parser.parse_args()

    basket = _load_basket(args.basket_file) if args.basket_file else None
    execution_id = args.execution_id or (
        f"radar-open-data-{datetime.now(UTC):%Y%m%d-%H%M%S}"
    )
    result = audit_radar_open_data(
        source_dir=args.source_dir,
        output_root=args.output_root,
        execution_id=execution_id,
        ncm_basket=basket,
        basket_name=args.basket_name,
    )
    print(f"execution_id={execution_id}")
    print(f"csv_files={len(result.schema_inventory)}")
    print(f"ncm_rows={len(result.ncm_matches)}")
    print(f"composition_rows={len(result.composition_summary)}")
    print("canonical_rows_promoted=0")
    print(f"output={result.output_path}")


if __name__ == "__main__":
    main()
