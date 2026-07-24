"""Comando para auditar os candidatos do bloco demográfico."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.demography_audit import (
    audit_demography_candidates,
    write_demography_audit,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Audita os candidatos demográficos já identificados no mapa de "
            "cobertura, sem coletar novas fontes."
        )
    )
    parser.add_argument("--coverage-path", type=Path)
    parser.add_argument(
        "--coverage-root",
        type=Path,
        default=Path(".data/audit/base_territorial/coverage_map"),
    )
    parser.add_argument("--derived-audit-path", type=Path)
    parser.add_argument(
        "--derived-audit-root",
        type=Path,
        default=Path(".data/audit/derived_products"),
    )
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--run-id")
    parser.add_argument("--primary-only", action="store_true")
    parser.add_argument("--replace", action="store_true")
    return parser


def _latest_directory(root: Path, required_file: str) -> Path:
    resolved = root.expanduser().resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Diretório de auditoria não encontrado: {resolved}")
    candidates = sorted(
        path
        for path in resolved.iterdir()
        if path.is_dir() and (path / required_file).is_file()
    )
    if not candidates:
        raise FileNotFoundError(
            f"Nenhuma execução válida encontrada em {resolved} com {required_file}."
        )
    return candidates[-1]


def _resolve_coverage_path(args: argparse.Namespace) -> Path:
    if args.coverage_path is not None:
        path = args.coverage_path.expanduser().resolve()
        if not (path / "coverage_file_inventory.csv").is_file():
            raise FileNotFoundError(f"Mapa de cobertura inválido: {path}")
        return path
    return _latest_directory(
        args.coverage_root,
        "coverage_file_inventory.csv",
    )


def _resolve_derived_audit_path(args: argparse.Namespace) -> Path | None:
    if args.derived_audit_path is not None:
        path = args.derived_audit_path.expanduser().resolve()
        if not path.is_dir():
            raise FileNotFoundError(f"Auditoria de derivados não encontrada: {path}")
        return path
    root = args.derived_audit_root.expanduser().resolve()
    if not root.is_dir():
        return None
    candidates = sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and (path / "derived_file_profile.csv").is_file()
    )
    return candidates[-1] if candidates else None


def _optional_csv(path: Path | None, file_name: str) -> pd.DataFrame | None:
    if path is None:
        return None
    candidate = path / file_name
    return pd.read_csv(candidate) if candidate.is_file() else None


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    coverage_path = _resolve_coverage_path(args)
    derived_audit_path = _resolve_derived_audit_path(args)
    coverage_files = pd.read_csv(coverage_path / "coverage_file_inventory.csv")
    file_profiles = _optional_csv(
        derived_audit_path,
        "derived_file_profile.csv",
    )
    table_profiles = _optional_csv(
        derived_audit_path,
        "derived_table_profile.csv",
    )

    result = audit_demography_candidates(
        coverage_files,
        file_profiles=file_profiles,
        table_profiles=table_profiles,
        include_secondary=not args.primary_only,
    )
    run_id = args.run_id or datetime.now(UTC).strftime(
        "demography-audit-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(".data/audit/base_territorial/demography") / run_id
    )
    target = write_demography_audit(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.summary)

    print(f"coverage_path={coverage_path}")
    print(f"derived_audit_path={derived_audit_path or '-'}")
    for name in (
        "demography_candidates",
        "primary_candidates",
        "secondary_candidates",
        "raw_candidates",
        "processed_candidates",
        "warehouse_candidates",
        "export_candidates",
        "profiled_candidates",
        "profile_error_candidates",
        "tables_observed",
        "rows_observed",
        "tables_with_core_signals",
        "source_families",
        "conceptually_validated_candidates",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== CANDIDATOS DEMOGRÁFICOS ===")
    display_columns = [
        "demography_relation",
        "source_stage",
        "candidate_role",
        "read_status",
        "tables_observed",
        "rows_observed",
        "relative_path",
    ]
    print(result.candidates[display_columns].to_string(index=False))

    print("\n=== TABELAS E SINAIS ESTRUTURAIS ===")
    table_columns = [
        "demography_relation",
        "source_stage",
        "relative_path",
        "table_name",
        "rows_observed",
        "columns_observed",
        "structural_signal_status",
        "utility_estimate",
        "headers",
    ]
    if result.tables.empty:
        print("nenhuma tabela perfilada")
    else:
        print(result.tables[table_columns].to_string(index=False))

    print("\n=== FAMÍLIAS ===")
    print(result.families.to_string(index=False))
    print(f"\noutput_dir={target}")
    print("new_external_sources_collected=0")
    print("raw_files_modified=0")
    print("drive_write_operations=0")
    print("curated_demography_built=0")
    print("status=ok")


if __name__ == "__main__":
    main()
