"""Comando para construir o mapa de cobertura da Base Territorial Comum."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.base_territorial_coverage import (
    build_coverage_map,
    detect_local_module_evidence,
    write_coverage_map,
)
from sbmi.base_territorial_coverage_refinement import refine_coverage_map
from sbmi.inbox_staging_validation_cli import latest_staging


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Mapeia a cobertura técnica da Base Territorial Comum usando o "
            "inventário do Drive e auditorias locais já existentes."
        )
    )
    parser.add_argument(
        "--inventory-path",
        type=Path,
        default=Path(".data/manifests/google_drive_inventory.csv"),
    )
    parser.add_argument("--staging-path", type=Path)
    parser.add_argument(
        "--staging-root",
        type=Path,
        default=Path(".data/staging/new_files"),
    )
    parser.add_argument("--staging-validation-path", type=Path)
    parser.add_argument(
        "--staging-validation-root",
        type=Path,
        default=Path(".data/audit/new_files/staging_validation"),
    )
    parser.add_argument(
        "--derived-audit-path",
        type=Path,
        default=Path(
            ".data/audit/derived_products/derived-products-20260723"
        ),
    )
    parser.add_argument(
        "--curated-root",
        type=Path,
        default=Path(".data/curated/base_territorial"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--replace", action="store_true")
    return parser


def _optional_csv(path: Path) -> pd.DataFrame | None:
    resolved = path.expanduser().resolve()
    return pd.read_csv(resolved) if resolved.is_file() else None


def _resolve_staging(args: argparse.Namespace) -> Path | None:
    if args.staging_path is not None:
        resolved = args.staging_path.expanduser().resolve()
        if not resolved.is_dir():
            raise FileNotFoundError(f"Staging não encontrado: {resolved}")
        return resolved
    root = args.staging_root.expanduser().resolve()
    return latest_staging(root) if root.is_dir() else None


def _validation_path(
    args: argparse.Namespace,
    staging_path: Path | None,
) -> Path | None:
    if args.staging_validation_path is not None:
        return args.staging_validation_path.expanduser().resolve()
    if staging_path is None:
        return None
    return (
        args.staging_validation_root.expanduser().resolve()
        / staging_path.name
    )


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    inventory_path = args.inventory_path.expanduser().resolve()
    if not inventory_path.is_file():
        raise FileNotFoundError(
            f"Inventário do Drive não encontrado: {inventory_path}"
        )

    inventory = pd.read_csv(inventory_path)
    staging_path = _resolve_staging(args)
    manifest = (
        _optional_csv(staging_path / "source_manifest.csv")
        if staging_path is not None
        else None
    )
    validation_path = _validation_path(args, staging_path)
    dataset_validation = (
        _optional_csv(validation_path / "dataset_validation_summary.csv")
        if validation_path is not None
        else None
    )
    derived_families = _optional_csv(
        args.derived_audit_path.expanduser().resolve()
        / "derived_family_summary.csv"
    )
    local_modules = detect_local_module_evidence(args.curated_root)

    result = build_coverage_map(
        inventory,
        manifest=manifest,
        dataset_validation=dataset_validation,
        derived_families=derived_families,
        local_modules=local_modules,
    )
    result = refine_coverage_map(result, inventory)
    run_id = args.run_id or datetime.now(UTC).strftime(
        "coverage-map-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/base_territorial/coverage_map") / run_id
    )
    target = write_coverage_map(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.summary)

    print(f"inventory_path={inventory_path}")
    print(f"staging_path={staging_path or '-'}")
    print(f"staging_validation_path={validation_path or '-'}")
    print(
        "derived_audit_path="
        f"{args.derived_audit_path.expanduser().resolve()}"
    )
    print(f"curated_root={args.curated_root.expanduser().resolve()}")
    for name in (
        "inventory_entries",
        "inventory_folders",
        "inventory_files",
        "analytical_candidate_files",
        "classified_candidate_files",
        "unclassified_candidate_files",
        "source_family_rows",
        "evidence_register_rows",
        "blocks_with_curated_modules",
        "blocks_with_validated_staging",
        "blocks_without_candidates",
    ):
        print(f"{name}={indicators[name]}")
    for row in result.block_summary.itertuples(index=False):
        print(
            f"block={row.block}"
            f"\tfiles={row.candidate_files}"
            f"\traw={row.raw_files}"
            f"\tstaging={row.staging_datasets}"
            f"\tcurated={row.curated_modules}"
            f"\tderived={row.audited_derived_families}"
            f"\tstatus={row.coverage_status}"
        )
    print(f"output_dir={target}")
    print("classification_calibration=applied")
    print("external_sources_collected=0")
    print("raw_files_modified=0")
    print("drive_write_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
