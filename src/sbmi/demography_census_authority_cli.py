"""Comando para verificar a autoridade externa das fontes censitárias."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd
import requests

from sbmi.demography_census_authority import audit_census_authority


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Captura páginas oficiais do IBGE e verifica temas, produtos e datas "
            "associados às 17 tabelas locais do Censo 2022."
        )
    )
    parser.add_argument("--quality-path", type=Path)
    parser.add_argument(
        "--quality-root",
        type=Path,
        default=Path(
            ".data/audit/base_territorial/demography_census_quality"
        ),
    )
    parser.add_argument("--provenance-path", type=Path)
    parser.add_argument(
        "--provenance-root",
        type=Path,
        default=Path(
            ".data/audit/base_territorial/demography_census_provenance"
        ),
    )
    parser.add_argument(
        "--snapshots-root",
        type=Path,
        default=Path(
            ".data/snapshots/web/demography_census_authority"
        ),
    )
    parser.add_argument(
        "--audit-root",
        type=Path,
        default=Path(
            ".data/audit/base_territorial/demography_census_authority"
        ),
    )
    parser.add_argument("--snapshot-id")
    parser.add_argument("--run-id")
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    parser.add_argument("--max-page-bytes", type=int, default=5_000_000)
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


def _resolve(
    explicit: Path | None,
    root: Path,
    required_file: str,
) -> Path:
    if explicit is not None:
        resolved = explicit.expanduser().resolve()
        if not (resolved / required_file).is_file():
            raise FileNotFoundError(f"Execução inválida: {resolved}")
        return resolved
    return _latest_directory(root, required_file)


def _indicator_map(summary: pd.DataFrame) -> dict[str, int]:
    return {
        str(row.indicator): int(row.value)
        for row in summary.itertuples(index=False)
    }


def main() -> None:
    args = build_parser().parse_args()
    quality_path = _resolve(
        args.quality_path,
        args.quality_root,
        "demography_census_quality_register.csv",
    )
    provenance_path = _resolve(
        args.provenance_path,
        args.provenance_root,
        "demography_census_workbook_provenance.csv",
    )
    date_stamp = datetime.now(UTC).strftime("%Y%m%d")
    snapshot_id = args.snapshot_id or f"census-authority-{date_stamp}"
    run_id = args.run_id or f"demography-census-authority-{date_stamp}"
    quality = pd.read_csv(
        quality_path / "demography_census_quality_register.csv"
    )
    provenance = pd.read_csv(
        provenance_path / "demography_census_workbook_provenance.csv"
    )

    with requests.Session() as session:
        result = audit_census_authority(
            session,
            quality,
            provenance,
            snapshots_root=args.snapshots_root,
            audit_root=args.audit_root,
            snapshot_id=snapshot_id,
            run_id=run_id,
            replace=args.replace,
            timeout_seconds=args.timeout_seconds,
            max_page_bytes=args.max_page_bytes,
        )
    indicators = _indicator_map(result.summary)

    print(f"quality_path={quality_path}")
    print(f"provenance_path={provenance_path}")
    print(f"official_snapshot_path={result.snapshot_path}")
    for name in (
        "datasets_registered",
        "official_topics_confirmed",
        "official_products_confirmed",
        "official_release_dates_confirmed",
        "official_authority_confirmed_datasets",
        "local_file_origin_established_datasets",
        "official_rebuild_required_datasets",
        "conceptually_validated_datasets",
    ):
        print(f"{name}={indicators[name]}")

    print("\n=== VERIFICAÇÃO OFICIAL POR DATASET ===")
    columns = [
        "dataset_identity",
        "official_result_basis",
        "official_release_date",
        "panorama_topic_present",
        "official_product_present",
        "official_release_date_present",
        "external_authority_status",
        "local_file_origin_linkage_status",
        "processed_reuse_status",
        "recommended_next_action",
    ]
    print(result.verification[columns].to_string(index=False))

    print("\n=== PÁGINAS OFICIAIS CAPTURADAS ===")
    print(result.pages.to_string(index=False))
    print(f"\noutput_dir={result.output_path}")
    print("official_institution=IBGE")
    print("official_locality_code=4318002")
    print("local_file_origin_claimed=0")
    print("conceptual_validation_claimed=0")
    print("historical_processed_files_modified=0")
    print("drive_write_operations=0")
    print("status=ok")


if __name__ == "__main__":
    main()
