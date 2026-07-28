"""Comando para revisar a qualidade dos produtos censitários processados."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.demography_census_quality_review import (
    review_census_quality,
    write_census_quality_review,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Classifica equivalências e anomalias dos produtos processados do "
            "Censo 2022 sem validar a autoridade da fonte."
        )
    )
    parser.add_argument("--comparison-path", type=Path)
    parser.add_argument(
        "--comparison-root",
        type=Path,
        default=Path(
            ".data/audit/base_territorial/demography_census_comparison"
        ),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--replace", action="store_true")
    return parser


def _latest_directory(root: Path, required_file: str) -> Path:
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Diretório não encontrado: {resolved}")
    candidates = sorted(
        path
        for path in resolved.iterdir()
        if path.is_dir() and (path / required_file).is_file()
    )
    if not candidates:
        raise FileNotFoundError(
            f"Nenhuma execução válida em {resolved} com {required_file}."
        )
    return candidates[-1]


def _resolve_comparison_path(args: argparse.Namespace) -> Path:
    if args.comparison_path is not None:
        path = args.comparison_path.expanduser().resolve()
        required = path / "demography_census_dataset_comparison.csv"
        if not required.is_file():
            raise FileNotFoundError(f"Comparação inválida: {path}")
        return path
    return _latest_directory(
        args.comparison_root,
        "demography_census_dataset_comparison.csv",
    )


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    comparison_path = _resolve_comparison_path(args)
    datasets = pd.read_csv(
        comparison_path / "demography_census_dataset_comparison.csv"
    )
    differences_path = (
        comparison_path / "demography_census_cell_differences.csv"
    )
    differences = (
        pd.read_csv(differences_path)
        if differences_path.is_file()
        else pd.DataFrame()
    )
    result = review_census_quality(datasets, differences)
    run_id = args.run_id or datetime.now(UTC).strftime(
        "demography-census-quality-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/base_territorial/demography_census_quality")
        / run_id
    )
    target = write_census_quality_review(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.summary)

    print(f"comparison_path={comparison_path}")
    for name in (
        "datasets_reviewed",
        "content_equivalent_datasets",
        "datasets_quarantined",
        "systematic_decimal_scale_errors",
        "affected_cells",
        "source_authority_reviews_completed",
        "conceptually_validated_datasets",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== REGISTRO DE QUALIDADE ===")
    columns = [
        "dataset_identity",
        "content_equivalence_status",
        "quality_class",
        "affected_cells",
        "affected_columns",
        "observed_scale_factors",
        "processed_reuse_status",
        "recommended_action",
    ]
    print(result.datasets[columns].to_string(index=False))

    print("\n=== PRODUTOS EM QUARENTENA ===")
    if result.anomalies.empty:
        print("nenhum produto em quarentena")
    else:
        print(result.anomalies[columns].to_string(index=False))

    print(f"\noutput_dir={target}")
    print("historical_processed_files_modified=0")
    print("corrected_products_built=0")
    print("source_authority_claimed=0")
    print("conceptual_validation_claimed=0")
    print("status=ok")


if __name__ == "__main__":
    main()
