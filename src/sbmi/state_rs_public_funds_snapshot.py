"""Snapshot piloto de recursos públicos estaduais destinados ao território."""

from __future__ import annotations

import hashlib
import shutil
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

import pandas as pd
import requests

RESOURCES = (
    (
        "agreements_revenue",
        "AGREEMENT",
        "https://dados.rs.gov.br/dataset/0627e630-e05b-4eaa-bf54-a0b26d9b96b7/"
        "resource/a1eedd0a-fc88-4269-b91d-899c975653fe/download/"
        "convenios-de-receita.zip",
    ),
    (
        "agreements_expense",
        "AGREEMENT",
        "https://dados.rs.gov.br/dataset/0627e630-e05b-4eaa-bf54-a0b26d9b96b7/"
        "resource/7e2bf92c-056c-48b1-ac4d-11a01e07e447/download/"
        "convenios-de-despesa.zip",
    ),
    (
        "agreements_layout",
        "LAYOUT",
        "https://dados.rs.gov.br/dataset/0627e630-e05b-4eaa-bf54-a0b26d9b96b7/"
        "resource/32c0a2be-cea4-4d22-a91e-1b434f9754df/download/"
        "convenios-rs.zip",
    ),
    (
        "partnerships",
        "AGREEMENT",
        "https://dados.rs.gov.br/dataset/0627e630-e05b-4eaa-bf54-a0b26d9b96b7/"
        "resource/b3379b65-1ac0-430c-95eb-67f903ba2e36/download/"
        "parcerias-rs.zip",
    ),
    (
        "partnerships_layout",
        "LAYOUT",
        "https://dados.rs.gov.br/dataset/0627e630-e05b-4eaa-bf54-a0b26d9b96b7/"
        "resource/b4e9d126-f92f-4e60-b804-ac2cc95904be/download/"
        "layout-parcerias.pdf",
    ),
    (
        "state_expense_2026_05",
        "DIRECT_EXPENDITURE_OR_TRANSFER",
        "https://dados.rs.gov.br/dataset/6d9e3f69-a795-4122-bca2-0924fbf7ede9/"
        "resource/3e68adb7-0be7-4bc0-89a1-f8dfbfff4f06/download/"
        "despesas-do-estado-202605.zip",
    ),
)
ALLOWED_HOST = "dados.rs.gov.br"


@dataclass(frozen=True)
class StateFundsSnapshotResult:
    snapshot_path: Path
    audit_path: Path
    manifest: pd.DataFrame
    archive_inventory: pd.DataFrame
    validation: pd.DataFrame


def _safe_archive_name(name: str) -> bool:
    path = PurePosixPath(name.replace("\\", "/"))
    return not path.is_absolute() and ".." not in path.parts


def snapshot_state_rs_public_funds(
    *,
    snapshot_root: Path,
    audit_root: Path,
    run_id: str,
    session: requests.Session | None = None,
    timeout: float = 60,
    per_file_limit: int = 25_000_000,
    total_limit: int = 60_000_000,
) -> StateFundsSnapshotResult:
    """Baixa seis recursos oficiais sem extrair ou normalizar seu conteúdo."""
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    target = snapshot_root.resolve() / run_id
    audit = audit_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    partial_audit = audit.with_name(f".{audit.name}.partial")
    if any(path.exists() for path in (target, audit, partial, partial_audit)):
        raise FileExistsError("Execução existente ou incompleta")
    client = session or requests.Session()
    partial.mkdir(parents=True)
    partial_audit.mkdir(parents=True)
    manifest_rows = []
    archive_rows = []
    total_bytes = 0
    try:
        for resource_id, family, url in RESOURCES:
            if urlparse(url).hostname != ALLOWED_HOST:
                raise ValueError(f"Domínio não autorizado: {url}")
            response = client.get(url, timeout=timeout, stream=True)
            response.raise_for_status()
            suffix = Path(urlparse(url).path).suffix.lower()
            filename = f"{resource_id}{suffix}"
            path = partial / filename
            digest = hashlib.sha256()
            size = 0
            with path.open("xb") as output:
                for chunk in response.iter_content(chunk_size=64 * 1024):
                    if not chunk:
                        continue
                    size += len(chunk)
                    total_bytes += len(chunk)
                    if size > per_file_limit or total_bytes > total_limit:
                        raise ValueError("Limite de download excedido")
                    digest.update(chunk)
                    output.write(chunk)
            is_zip = zipfile.is_zipfile(path)
            if suffix == ".zip" and not is_zip:
                raise ValueError(f"ZIP inválido: {filename}")
            if is_zip:
                with zipfile.ZipFile(path) as archive:
                    for member in archive.infolist():
                        if not _safe_archive_name(member.filename):
                            raise ValueError(
                                f"Membro ZIP inseguro: {member.filename}"
                            )
                        archive_rows.append({
                            "resource_id": resource_id,
                            "archive_file": filename,
                            "member_name": member.filename,
                            "compressed_bytes": member.compress_size,
                            "uncompressed_bytes": member.file_size,
                            "is_directory": member.is_dir(),
                            "member_suffix": Path(member.filename).suffix.lower(),
                            "extracted": False,
                            "nature": "observed_archive_metadata",
                        })
            manifest_rows.append({
                "resource_id": resource_id,
                "government_sphere": "STATE_RS",
                "dimension": "financas_publicas_transferencias",
                "financial_family": family,
                "territorial_filter_status": "NOT_YET_FILTERED",
                "source_url": url,
                "final_url": response.url,
                "status_code": response.status_code,
                "content_type": response.headers.get("Content-Type", ""),
                "bytes": size,
                "sha256": digest.hexdigest(),
                "raw_file": filename,
                "is_zip": is_zip,
                "personal_data_inspected": False,
                "integration_status": "NOT_INTEGRATED",
                "nature": "observed_raw_capture",
            })
        manifest = pd.DataFrame(manifest_rows)
        archive_inventory = pd.DataFrame(archive_rows)
        duplicate_hashes = int(manifest.sha256.duplicated().sum())
        validation = pd.DataFrame([
            ("resources_expected", len(RESOURCES), "calculated", "PASS"),
            ("resources_captured", len(manifest), "calculated", "PASS"),
            ("total_bytes", total_bytes, "calculated", "PASS"),
            ("duplicate_hashes", duplicate_hashes, "calculated",
             "PASS" if duplicate_hashes == 0 else "FAIL"),
            ("archives_extracted", 0, "calculated", "PASS"),
            ("personal_data_inspected", 0, "calculated", "PASS"),
            ("canonical_rows_promoted", 0, "calculated", "PASS"),
        ], columns=["indicator", "value", "nature", "status"])
        if validation.status.eq("FAIL").any():
            raise ValueError("Validação do snapshot falhou")
        manifest.to_csv(partial_audit / "source_manifest.csv", index=False)
        archive_inventory.to_csv(
            partial_audit / "archive_inventory.csv", index=False
        )
        validation.to_csv(partial_audit / "validation.csv", index=False)
        partial.replace(target)
        partial_audit.replace(audit)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        shutil.rmtree(partial_audit, ignore_errors=True)
        raise
    return StateFundsSnapshotResult(
        target, audit, manifest, archive_inventory, validation
    )
