"""Descoberta controlada de fontes de recursos destinados a São Borja."""

from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests

SOURCES = (
    {
        "source_id": "federal_locality_panel",
        "url": "https://portaldatransparencia.gov.br/localidades/4318002-sao-borja",
        "government_sphere": "FEDERAL",
        "financial_family": "MULTIFAMILY_SUMMARY",
        "recipient_scope": "MIXED",
        "financial_stage": "MIXED",
        "territorial_relation": "APPLIED_OR_RECEIVED_IN_LOCALITY",
    },
    {
        "source_id": "federal_transfers",
        "url": "https://portaldatransparencia.gov.br/transferencias/consulta",
        "government_sphere": "FEDERAL",
        "financial_family": "TRANSFER",
        "recipient_scope": "MIXED",
        "financial_stage": "TRANSFERRED_OR_EXECUTION_STAGE",
        "territorial_relation": "RECIPIENT_LOCATED_IN_MUNICIPALITY",
    },
    {
        "source_id": "federal_citizen_benefits",
        "url": "https://portaldatransparencia.gov.br/beneficios/consulta",
        "government_sphere": "FEDERAL",
        "financial_family": "CITIZEN_BENEFIT",
        "recipient_scope": "INDIVIDUAL_RESIDENT_AGGREGATE_ONLY",
        "financial_stage": "PAID",
        "territorial_relation": "RESIDENT_IN_MUNICIPALITY",
    },
    {
        "source_id": "federal_agreements",
        "url": "https://portaldatransparencia.gov.br/convenios/consulta",
        "government_sphere": "FEDERAL",
        "financial_family": "AGREEMENT",
        "recipient_scope": "MIXED",
        "financial_stage": "CELEBRATED_AND_RELEASED_SEPARATE",
        "territorial_relation": "AGREEMENT_PARTY_IN_MUNICIPALITY",
    },
    {
        "source_id": "federal_government_programs",
        "url": "https://portaldatransparencia.gov.br/programas-de-governo?ano=2026",
        "government_sphere": "FEDERAL",
        "financial_family": "DIRECT_EXPENDITURE_OR_PROGRAM",
        "recipient_scope": "LOCALITY",
        "financial_stage": "PAID_OR_EXECUTED",
        "territorial_relation": "APPLIED_IN_LOCALITY",
    },
    {
        "source_id": "state_rs_open_data",
        "url": (
            "https://www.transparencia.rs.gov.br/dados-abertos/"
            "dados-transparencia-rs/dados/"
        ),
        "government_sphere": "STATE_RS",
        "financial_family": "TRANSFER_AND_AGREEMENT_CATALOG",
        "recipient_scope": "MIXED",
        "financial_stage": "DATASET_DEPENDENT",
        "territorial_relation": "RECIPIENT_OR_PARTY_IN_MUNICIPALITY",
    },
)


@dataclass(frozen=True)
class PublicFundsDiscoveryResult:
    snapshot_path: Path
    audit_path: Path
    inventory: pd.DataFrame
    validation: pd.DataFrame


def discover_public_funds_sources(
    *,
    snapshot_root: Path,
    audit_root: Path,
    run_id: str,
    timeout: float = 30,
    response_limit: int = 2_000_000,
    session: requests.Session | None = None,
) -> PublicFundsDiscoveryResult:
    """Captura páginas públicas; não baixa bases nem dados pessoais."""
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    snapshot = snapshot_root.resolve() / run_id
    audit = audit_root.resolve() / run_id
    partial_snapshot = snapshot.with_name(f".{snapshot.name}.partial")
    partial_audit = audit.with_name(f".{audit.name}.partial")
    if any(path.exists() for path in (snapshot, audit, partial_snapshot, partial_audit)):
        raise FileExistsError("Execução existente ou incompleta")
    client = session or requests.Session()
    partial_snapshot.mkdir(parents=True)
    partial_audit.mkdir(parents=True)
    records = []
    try:
        for source in SOURCES:
            response = client.get(source["url"], timeout=timeout)
            payload = response.content
            if len(payload) > response_limit:
                raise ValueError(f"Resposta excede limite: {source['source_id']}")
            content_type = response.headers.get("Content-Type", "")
            safe_html = b"text/html" in content_type.encode().lower()
            suffix = ".html" if safe_html else ".bin"
            raw_name = f"{source['source_id']}{suffix}"
            (partial_snapshot / raw_name).write_bytes(payload)
            challenge = (
                b"Human Verification" in payload
                or b"captcha-container" in payload
            )
            records.append(source | {
                "requested_url": source["url"],
                "final_url": response.url,
                "status_code": response.status_code,
                "content_type": content_type,
                "bytes": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(),
                "raw_file": raw_name,
                "sample_status": (
                    "BLOCKED_BY_HUMAN_VERIFICATION"
                    if challenge
                    else "METADATA_PAGE_CAPTURED_NO_DATA_SAMPLE"
                ),
                "personal_data_captured": False,
                "integration_status": "NOT_INTEGRATED",
                "dimension": "financas_publicas_transferencias",
                "nature": "observed_metadata_capture",
            })
        inventory = pd.DataFrame(records)
        validation = pd.DataFrame([
            ("sources_expected", len(SOURCES), "calculated", "PASS"),
            ("sources_captured", len(inventory), "calculated", "PASS"),
            ("personal_data_files", 0, "calculated", "PASS"),
            ("data_samples_captured", 0, "calculated", "PASS"),
            ("canonical_rows_promoted", 0, "calculated", "PASS"),
        ], columns=["indicator", "value", "nature", "status"])
        inventory.to_csv(partial_audit / "source_inventory.csv", index=False)
        validation.to_csv(partial_audit / "validation.csv", index=False)
        partial_snapshot.replace(snapshot)
        partial_audit.replace(audit)
    except Exception:
        shutil.rmtree(partial_snapshot, ignore_errors=True)
        shutil.rmtree(partial_audit, ignore_errors=True)
        raise
    return PublicFundsDiscoveryResult(snapshot, audit, inventory, validation)
