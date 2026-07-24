"""Comando da auditoria de proveniência das planilhas do Censo 2022."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.demography_census_provenance import (
    audit_census_provenance,
    write_census_provenance_audit,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Extrai metadados, URLs, rótulos de fonte, período, unidade e "
            "abrangência das planilhas capturadas, sem atribuir autoridade."
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


def _resolve_path(
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
    lineage_path = _resolve_path(
        args.lineage_path,
        args.lineage_root,
        "demography_lineage_register.csv",
    )
    raw_snapshot_path = _resolve_path(
        args.raw_snapshot_path,
        args.raw_snapshot_root,
        "source_manifest.csv",
    )
    lineage = pd.read_csv(lineage_path / "demography_lineage_register.csv")
    manifest = pd.read_csv(raw_snapshot_path / "source_manifest.csv")
    result = audit_census_provenance(
        lineage,
        manifest,
        raw_snapshot_root=raw_snapshot_path,
    )
    run_id = args.run_id or datetime.now(UTC).strftime(
        "demography-census-provenance-%Y%m%d"
    )
    output_dir = (
        args.output_dir.expanduser().resolve()
        if args.output_dir is not None
        else Path(
            ".data/audit/base_territorial/demography_census_provenance"
        )
        / run_id
    )
    target = write_census_provenance_audit(
        result,
        output_dir,
        replace=args.replace,
    )
    indicators = _indicator_map(result.summary)

    print(f"lineage_path={lineage_path}")
    print(f"raw_snapshot_path={raw_snapshot_path}")
    for name in (
        "workbooks_reviewed",
        "manifest_verified_workbooks",
        "sheets_reviewed",
        "columns_profiled",
        "evidence_records",
        "workbooks_with_embedded_domains",
        "unique_detected_domains",
        "workbooks_with_source_labels",
        "workbooks_with_document_creator",
        "workbooks_without_embedded_provenance",
        "source_authority_reviews_completed",
        "conceptually_validated_datasets",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== PROVENIÊNCIA POR PLANILHA ===")
    workbook_columns = [
        "dataset_identity",
        "creator",
        "last_modified_by",
        "created_at",
        "modified_at",
        "detected_domains",
        "source_label_occurrences",
        "institution_label_occurrences",
        "period_label_occurrences",
        "unit_label_occurrences",
        "geography_label_occurrences",
        "provenance_status",
        "source_authority_status",
    ]
    print(result.workbooks[workbook_columns].to_string(index=False))

    print("\n=== EVIDÊNCIAS DE FONTE, INSTITUIÇÃO E URL ===")
    authority_kinds = {
        "CELL_URL",
        "HYPERLINK_TARGET",
        "SOURCE_LABEL",
        "INSTITUTION_LABEL",
    }
    authority_evidence = result.evidence.loc[
        result.evidence["evidence_kind"].isin(authority_kinds)
    ]
    if authority_evidence.empty:
        print("nenhuma evidência embutida de fonte, instituição ou URL")
    else:
        evidence_columns = [
            "dataset_identity",
            "sheet_name",
            "cell_coordinate",
            "evidence_kind",
            "evidence_text",
            "detected_domain",
            "occurrence_count",
            "authority_implication",
        ]
        print(authority_evidence[evidence_columns].to_string(index=False))

    print("\n=== PISTAS DE UNIDADE POR COLUNA ===")
    unit_columns = result.columns.loc[
        result.columns["unit_hint"].ne("UNSPECIFIED")
    ]
    if unit_columns.empty:
        print("nenhuma pista de unidade identificada nos cabeçalhos")
    else:
        display_columns = [
            "dataset_identity",
            "header_raw",
            "unit_hint",
            "semantic_types",
            "excel_number_formats_json",
            "percent_style_cells",
        ]
        print(unit_columns[display_columns].to_string(index=False))

    print(f"\noutput_dir={target}")
    print("authority_assignment=NONE")
    print("external_verification_completed=0")
    print("conceptual_validation_claimed=0")
    print("raw_files_modified=0")
    print("drive_write_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
