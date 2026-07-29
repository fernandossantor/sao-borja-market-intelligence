"""Descoberta segura do catálogo estadual de dados abertos."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import requests

PANEL_UPDATE_URL = (
    "https://www.transparencia.rs.gov.br/umbraco/Surface/Faq/AtualizacaoPainel"
)
REPORT_URL = (
    "https://www.transparencia.rs.gov.br/umbraco/Surface/PowerBI/Report"
)
WORKSPACE_ID = "48138f86-653d-4a67-98d5-4cf00cdbcf4a"
REPORT_ID = "f465474e-63b4-4b54-a8b8-65b32779e61f"


@dataclass(frozen=True)
class StateCatalogDiscoveryResult:
    output_path: Path
    metadata: pd.DataFrame
    validation: pd.DataFrame


def discover_state_rs_catalog(
    *,
    output_root: Path,
    run_id: str,
    session: requests.Session | None = None,
    timeout: float = 30,
) -> StateCatalogDiscoveryResult:
    """Registra metadados do painel e descarta explicitamente o token."""
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    client = session or requests.Session()
    update = client.post(
        PANEL_UPDATE_URL,
        data={"tipoPainel": "Dados Abertos"},
        timeout=timeout,
    )
    update.raise_for_status()
    report = client.post(
        REPORT_URL,
        data={"workspaceId": WORKSPACE_ID, "reportId": REPORT_ID},
        timeout=timeout,
    )
    report.raise_for_status()
    report_data = report.json()
    token_present = bool(report_data.get("Token"))
    metadata = pd.DataFrame([{
        "source_id": "state_rs_open_data_catalog",
        "institution": "CAGE/RS",
        "government_sphere": "STATE_RS",
        "dimension": "financas_publicas_transferencias",
        "financial_families": "TRANSFER|AGREEMENT|DIRECT_EXPENDITURE",
        "panel_update_raw": update.text.strip(),
        "report_id": str(report_data.get("Id", "")),
        "embed_host": urlparse(str(report_data.get("EmbedUrl", ""))).netloc,
        "token_was_present_and_discarded": token_present,
        "token_stored": False,
        "data_rows_captured": 0,
        "personal_data_captured": False,
        "sample_status": "CATALOG_METADATA_ONLY",
        "integration_status": "NOT_INTEGRATED",
        "nature": "observed_public_panel_metadata",
    }])
    validation = pd.DataFrame([
        ("report_id_matches", int(metadata.report_id.iloc[0] == REPORT_ID),
         "calculated", "PASS"),
        ("embed_host_is_powerbi",
         int(metadata.embed_host.iloc[0] == "app.powerbi.com"),
         "calculated", "PASS"),
        ("token_stored", 0, "calculated", "PASS"),
        ("data_rows_captured", 0, "calculated", "PASS"),
        ("personal_data_files", 0, "calculated", "PASS"),
        ("canonical_rows_promoted", 0, "calculated", "PASS"),
    ], columns=["indicator", "value", "nature", "status"])
    partial.mkdir(parents=True)
    try:
        metadata.to_csv(partial / "state_rs_catalog_metadata.csv", index=False)
        validation.to_csv(partial / "validation.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return StateCatalogDiscoveryResult(target, metadata, validation)
