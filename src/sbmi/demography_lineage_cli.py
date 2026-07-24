"""Comando para revisar a linhagem dos produtos censitários."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.demography_lineage import (
    audit_demography_lineage,
    write_demography_lineage,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Relaciona fontes brutas do Censo 2022 e produtos processados por "
            "identidade nominal, sem afirmar equivalência de conteúdo."
        )
    )
    parser.add_argument("--coverage-path", type=Path)
    parser.add_argument(
        "--coverage-root",
        type=Path,
        default=Path(".data/audit/base_territorial/coverage_map"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--replace", action="store_true")
    return parser


def _latest_coverage(root: Path) -> Path:
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Raiz do mapa de cobertura não encontrada: {resolved}")
    candidates = sorted(
        path
        for path in resolved.iterdir()
        if path.is_dir() and (path / "coverage_file_inventory.csv").is_file()
    )
    if not candidates:
        raise FileNotFoundError(
            f"Nenhum mapa de cobertura válido encontrado em {resolved}."
        )
    return candidates[-1]


def _resolve_coverage(args: argparse.Namespace) -> Path:
    if args.coverage_path is not None:
        path = args.coverage_path.expanduser().resolve()
        if not (path / "coverage_file_inventory.csv").is_file():
            raise FileNotFoundError(f"Mapa de cobertura inválido: {path}")
        return path
    return _latest_coverage(args.coverage_root)


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    coverage_path = _resolve_coverage(args)
    coverage_files = pd.read_csv(coverage_path / "coverage_file_inventory.csv")
    result = audit_demography_lineage(coverage_files)

    run_id = args.run_id or datetime.now(UTC).strftime(
        "demography-lineage-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/base_territorial/demography_lineage") / run_id
    )
    target = write_demography_lineage(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.summary)

    print(f"coverage_path={coverage_path}")
    for name in (
        "lineage_candidates",
        "raw_census_sources",
        "processed_census_products",
        "technical_census_profiles",
        "dataset_identities",
        "matched_one_to_one_by_name",
        "raw_only",
        "processed_only",
        "ambiguous_lineage",
        "proposed_classification_corrections",
        "classification_reviews_already_applied",
        "content_equivalence_tests_completed",
        "conceptually_validated_datasets",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== REGISTRO DE LINHAGEM ===")
    print(
        result.lineage_register[
            [
                "dataset_identity",
                "raw_source_count",
                "processed_product_count",
                "lineage_match_status",
                "content_equivalence_status",
                "next_action",
            ]
        ].to_string(index=False)
    )

    print("\n=== CORREÇÕES PROPOSTAS AO MAPA ===")
    corrections = result.classification_corrections
    changed = corrections.loc[
        corrections["application_status"].eq("PROPOSED_NOT_APPLIED")
    ]
    if changed.empty:
        print("nenhuma correção temática pendente")
    else:
        print(
            changed[
                [
                    "relative_path",
                    "candidate_kind",
                    "current_primary_block",
                    "proposed_primary_block",
                    "current_analytical_candidate",
                    "proposed_analytical_candidate",
                    "correction_reason",
                ]
            ].to_string(index=False)
        )

    print(f"\noutput_dir={target}")
    print("lineage_evidence=normalized_filename_and_stage")
    print("census_topic_review=explicit")
    print("content_equivalence_claimed=0")
    print("new_external_sources_collected=0")
    print("raw_files_modified=0")
    print("drive_write_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
