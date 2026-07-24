"""Comando para construir os produtos IDSC da Base Territorial Comum."""

from __future__ import annotations

import argparse
from pathlib import Path

from sbmi.social_idsc import build_idsc, write_idsc_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Constrói resumo e factsheet do IDSC-BR 2025 e compara os resultados "
            "com as exportações históricas, sem substituí-las."
        )
    )
    parser.add_argument(
        "--source-path",
        type=Path,
        default=Path(
            ".data/snapshots/sources/social_idsc/idsc-br-2025/"
            "raw/social/Base_de_Dados_IDSC-BR_2025.xlsx"
        ),
    )
    parser.add_argument(
        "--historical-exports-dir",
        type=Path,
        default=Path(
            ".data/snapshots/derived_products/derived-products-20260723/exports"
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(
            ".data/curated/base_territorial/social/idsc/2025"
        ),
    )
    parser.add_argument("--municipality", default="São Borja")
    parser.add_argument("--sheet-name", default="Todos os Dados")
    parser.add_argument("--replace", action="store_true")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    result = build_idsc(
        args.source_path,
        municipality=args.municipality,
        sheet_name=args.sheet_name,
        historical_exports_dir=args.historical_exports_dir,
    )
    output_dir = write_idsc_result(
        result,
        args.output_dir,
        replace=args.replace,
    )

    print(f"source_path={args.source_path.expanduser().resolve()}")
    print(f"municipality={args.municipality}")
    print(f"reference_year={result.metadata['reference_year']}")
    print(f"source_rows_observed={result.metadata['source_rows_observed']}")
    print(f"source_columns_observed={result.metadata['source_columns_observed']}")
    print(f"ods_scores_observed={len(result.summary)}")
    print(f"factsheet_indicators={len(result.factsheet)}")
    print(
        "classification_nature="
        f"{result.metadata['classification_nature']}"
    )
    if result.comparison.empty:
        print("historical_comparison=NOT_REQUESTED")
    else:
        for row in result.comparison.itertuples(index=False):
            print(
                f"comparison={row.dataset}"
                f"\tstatus={row.status}"
                f"\trows_current={row.rows_current}"
                f"\trows_historical={row.rows_historical}"
                f"\tmismatched_cells={row.mismatched_cells}"
            )
    print(f"output_dir={output_dir}")
    print("historical_outputs_modified=0")
    print("drive_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
