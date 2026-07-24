"""Comando para comparar fontes XLSX e produtos parquet do Censo 2022."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.demography_census_comparison import (
    compare_census_lineage,
    write_census_comparison,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Compara os pares nominais XLSX e parquet do Censo 2022, sem "
            "atribuir validade conceitual ou autoridade à fonte capturada."
        )
    )
    parser.add_argument("--lineage-path", type=Path)
    parser.add_argument(
        "--lineage-root",
        type=Path,
        default=Path(".data/audit/base_territorial/demography_lineage"),
    )
    parser.add_argument("--raw-snapshot-path", type=Path)
    parser.add_argument(
        "--raw-snapshot-root",
        type=Path,
        default=Path(".data/snapshots/sources/demography_census"),
    )
    parser.add_argument("--derived-snapshot-path", type=Path)
    parser.add_argument(
        "--derived-snapshot-root",
        type=Path,
        default=Path(".data/snapshots/derived_products"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--difference-limit", type=int, default=100)
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


def _resolve_optional_or_latest(
    explicit: Path | None,
    root: Path,
    required_file: str,
) -> Path:
    if explicit is not None:
        resolved = explicit.expanduser().resolve()
        if not (resolved / required_file).is_file():
            raise FileNotFoundError(
                f"Diretório inválido: {resolved}; ausente {required_file}."
            )
        return resolved
    return _latest_directory(root, required_file)


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    if args.difference_limit <= 0:
        raise ValueError("difference-limit deve ser maior que zero.")
    lineage_path = _resolve_optional_or_latest(
        args.lineage_path,
        args.lineage_root,
        "demography_lineage_register.csv",
    )
    raw_snapshot_path = _resolve_optional_or_latest(
        args.raw_snapshot_path,
        args.raw_snapshot_root,
        "source_manifest.csv",
    )
    derived_snapshot_path = _resolve_optional_or_latest(
        args.derived_snapshot_path,
        args.derived_snapshot_root,
        "source_manifest.csv",
    )
    lineage = pd.read_csv(lineage_path / "demography_lineage_register.csv")
    result = compare_census_lineage(
        lineage,
        raw_snapshot_root=raw_snapshot_path,
        derived_snapshot_root=derived_snapshot_path,
        difference_limit_per_dataset=args.difference_limit,
    )
    run_id = args.run_id or datetime.now(UTC).strftime(
        "demography-census-comparison-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/base_territorial/demography_census_comparison")
        / run_id
    )
    target = write_census_comparison(result, output_dir, replace=args.replace)
    indicators = _indicator_map(result.summary)

    print(f"lineage_path={lineage_path}")
    print(f"raw_snapshot_path={raw_snapshot_path}")
    print(f"derived_snapshot_path={derived_snapshot_path}")
    for name in (
        "lineage_pairs_compared",
        "exact_after_canonicalization",
        "row_order_only_differences",
        "schema_mismatches",
        "row_count_mismatches",
        "cell_value_mismatches",
        "read_errors",
        "difference_cells_observed",
        "content_equivalence_tests_completed",
        "source_authority_reviews_completed",
        "conceptually_validated_datasets",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== COMPARAÇÃO POR DATASET ===")
    columns = [
        "dataset_identity",
        "raw_rows",
        "processed_rows",
        "raw_columns",
        "processed_columns",
        "header_set_match",
        "column_order_match",
        "row_count_match",
        "missing_values_match",
        "content_equivalence_status",
    ]
    print(result.datasets[columns].to_string(index=False))

    print("\n=== DIFERENÇAS DE CÉLULAS OBSERVADAS ===")
    if result.differences.empty:
        print("nenhuma diferença observada")
    else:
        print(result.differences.to_string(index=False))

    print(f"\noutput_dir={target}")
    print("comparison_basis=canonical_headers_and_semantic_cell_values")
    print("row_order_preserved_and_tested=1")
    print("source_authority_claimed=0")
    print("conceptual_validation_claimed=0")
    print("new_external_sources_collected=0")
    print("raw_files_modified=0")
    print("drive_write_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
