"""Run the territorial wage pipeline from the project master copies on Google Drive."""

from __future__ import annotations

import argparse
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

from sbmi.drive_staging import StagedDriveFile, stage_drive_file
from sbmi.google_drive import build_authorized_session, service_account_info_from_environment
from sbmi.rais_workers_extract import extract_municipality_from_7z_csv
from sbmi.territorial_wage_estimation import (
    estimate_territorial_wages,
    write_wage_outputs,
)

RAIS_VINC_SUL_2025_DRIVE_ID = "16NgcdvbvKLwlNoUmBpfXoeVXqGr5kOhn"
RAIS_VINC_SUL_2025_SIZE = 704_888_712
RAIS_VINC_SUL_2025_SHA256 = "c537caaaa8318b04e6f4cbbc7e59b130988668b7ea58ce67a0ab2caebf2f5bd0"
RAIS_VINC_MEMBER = "RAIS_VINC_PUB_SUL.COMT"

RFB_CELLS_DRIVE_ID = "10Frn6bcdixiMiXNQpe_5ycKjDHOrmyCd"
RFB_CELLS_SIZE = 30_429
RFB_CELLS_SHA256 = "73d53f372abda611f448970a5ea5a362f4183aee09e14b4c355c74ff7b585497"


def _source_manifest(
    rais_archive: StagedDriveFile,
    rais_extract_path: Path,
    rais_extract_sha256: str,
    rfb_cells: StagedDriveFile,
) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "role": "rais_workers_archive_drive_master",
                "source_file": rais_archive.drive_file_name,
                "bytes": rais_archive.size_bytes,
                "sha256": rais_archive.sha256,
                "nature": "observed_input",
                "drive_file_id": rais_archive.drive_file_id,
            },
            {
                "role": "rais_workers_extract_sao_borja",
                "source_file": rais_extract_path.name,
                "bytes": rais_extract_path.stat().st_size,
                "sha256": rais_extract_sha256,
                "nature": "calculated_extract",
                "drive_file_id": "",
            },
            {
                "role": "rfb_cnae_nature_territorial_cells_drive_master",
                "source_file": rfb_cells.drive_file_name,
                "bytes": rfb_cells.size_bytes,
                "sha256": rfb_cells.sha256,
                "nature": "calculated_audited_input",
                "drive_file_id": rfb_cells.drive_file_id,
            },
        ]
    )


def _run_metadata(*, execution_id: str) -> pd.DataFrame:
    return pd.DataFrame(
        [
            ("execution_id", execution_id, "parameter"),
            ("municipality_code", "431800", "parameter"),
            ("geography", "São Borja/RS", "parameter"),
            ("rais_reference_year", "2025", "observed_source_period"),
            ("rfb_competence", "2026-08", "observed_source_period"),
            (
                "operational_source",
                "Google Drive project master copies; no external source reacquisition in this run",
                "method",
            ),
            (
                "rais_active_link_rule",
                "Ind Vínculo Ativo 31/12 - Código = 1",
                "method",
            ),
            (
                "rais_abandoned_link_rule",
                "Ind Vínculo Abandonado - Código = 0",
                "method",
            ),
            (
                "business_universe",
                "Tipo Estabelecimento - Código = 1 (CNPJ) and Natureza Jurídica group 2",
                "method",
            ),
            (
                "primary_wage_metric",
                "sum of Vl Rem Média Nom across active non-abandoned business links; not annual payroll",
                "method",
            ),
            (
                "december_metric",
                "sum of Vl Rem Dezembro Nom where informed; not annual payroll",
                "method",
            ),
            (
                "estimation_rule",
                "RAIS employment and remuneration allocated by RFB establishment shares within hierarchical CNAE/nature cells",
                "method",
            ),
            (
                "temporal_comparability",
                "RAIS stock/reference 2025 versus RFB 2026-08; estimates are not same-period observations",
                "limitation",
            ),
        ],
        columns=["field", "value", "nature"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--execution-id",
        default=f"territorial-wage-rais2025-rfb2026-08-drive-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}",
    )
    parser.add_argument("--secret-env", default="SBMI_GDRIVE_SA_B64")
    parser.add_argument("--rais-drive-file-id", default=RAIS_VINC_SUL_2025_DRIVE_ID)
    parser.add_argument("--rfb-cells-drive-file-id", default=RFB_CELLS_DRIVE_ID)
    parser.add_argument(
        "--rais-local-path",
        type=Path,
        default=Path(".data/raw/rais/2025/RAIS_VINC_PUB_SUL.7z"),
    )
    parser.add_argument(
        "--rais-extract-path",
        type=Path,
        default=Path(".data/staging/rais/2025/rais_vinc_2025_sao_borja_extract_v001.csv"),
    )
    parser.add_argument(
        "--rfb-cells-local-path",
        type=Path,
        default=Path(
            ".data/staging/base_territorial/rais2025_wage/"
            "rfb_cnae_nature_territorial_cells_v001.csv"
        ),
    )
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(".data/exports/base_territorial/territorial_wage_estimation"),
    )
    args = parser.parse_args()

    info = service_account_info_from_environment(args.secret_env)
    session = build_authorized_session(info)

    rais_archive = stage_drive_file(
        session,
        file_id=args.rais_drive_file_id,
        target=args.rais_local_path,
        expected_size=RAIS_VINC_SUL_2025_SIZE,
        expected_sha256=RAIS_VINC_SUL_2025_SHA256,
    )
    rfb_cells = stage_drive_file(
        session,
        file_id=args.rfb_cells_drive_file_id,
        target=args.rfb_cells_local_path,
        expected_size=RFB_CELLS_SIZE,
        expected_sha256=RFB_CELLS_SHA256,
    )

    extract = extract_municipality_from_7z_csv(
        rais_archive.local_path,
        member=RAIS_VINC_MEMBER,
        output=args.rais_extract_path,
        municipality_column="Município - Código",
        municipality_code="431800",
        expected_columns=62,
        expected_rows=19_960,
    )

    rais = pd.read_csv(
        extract.output_path,
        encoding="utf-8",
        dtype=str,
        keep_default_na=False,
    )
    rfb = pd.read_csv(rfb_cells.local_path, dtype=str)
    result = estimate_territorial_wages(
        rais,
        rfb,
        municipality_code="431800",
        expected_business_active_links=8_595,
    )

    output_dir = args.output_root / args.execution_id
    manifest = _source_manifest(
        rais_archive,
        extract.output_path,
        extract.sha256,
        rfb_cells,
    )
    write_wage_outputs(
        result,
        output_dir,
        source_manifest=manifest,
        run_metadata=_run_metadata(execution_id=args.execution_id),
    )

    summary = result.summary.set_index("indicator")["value"]
    print(f"execution_id={args.execution_id}")
    print(f"rais_drive_reused_local={str(rais_archive.reused_existing).lower()}")
    print(f"rfb_drive_reused_local={str(rfb_cells.reused_existing).lower()}")
    print(f"rais_extract_reused_local={str(extract.reused_existing).lower()}")
    print(f"rais_extract_rows={extract.rows_selected}")
    print(f"rais_business_active_links={summary['rais_business_active_links']:.0f}")
    print(
        "estimated_external_active_links_share_pct="
        f"{summary['estimated_external_active_links_share_pct']:.6f}"
    )
    print(
        "estimated_external_avg_rem_sum_share_pct="
        f"{summary['estimated_external_avg_rem_sum_share_pct']:.6f}"
    )
    print(
        "estimated_external_dec_mass_share_pct="
        f"{summary['estimated_external_dec_mass_share_pct']:.6f}"
    )
    print(f"output_dir={output_dir}")
    print("STATUS=TERRITORIAL_WAGE_DRIVE_PIPELINE_OK")


if __name__ == "__main__":
    main()
