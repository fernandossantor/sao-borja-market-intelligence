"""Download e staging em fluxo de um lote mensal de despesas estaduais."""

from __future__ import annotations

import csv
import hashlib
import io
import shutil
import unicodedata
import zipfile
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath
from urllib.parse import urlparse

import pandas as pd
import requests

ALLOWED_HOST = "dados.rs.gov.br"
OUTPUT_COLUMNS = ("FaseGasto", "TipoGasto", "Orgao", "Data", "Valor")


@dataclass(frozen=True)
class StateExpenseBatchResult:
    snapshot_path: Path
    staging_path: Path
    audit_path: Path
    manifest: pd.DataFrame
    staging: pd.DataFrame
    resource_summary: pd.DataFrame
    validation: pd.DataFrame


def _normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    return " ".join(
        "".join(char for char in decomposed if not unicodedata.combining(char))
        .upper()
        .split()
    )


def _decimal(value: str) -> str:
    cleaned = value.strip().replace("R$", "").replace(" ", "")
    if not cleaned:
        return ""
    if "," in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    try:
        return format(Decimal(cleaned), "f")
    except InvalidOperation:
        return ""


def _hash_values(values: list[str]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(value.encode("utf-8", errors="replace"))
        digest.update(b"\x1f")
    return digest.hexdigest()


def _safe_member(name: str) -> bool:
    path = PurePosixPath(name.replace("\\", "/"))
    return not path.is_absolute() and ".." not in path.parts


def _selected_resources(
    inventory_path: Path,
    *,
    year: int,
    months: tuple[int, ...],
) -> list[dict[str, object]]:
    inventory = pd.read_csv(inventory_path)
    selected = inventory[
        inventory.catalog_year.eq(year)
        & inventory.resource_name_month.isin(months)
    ].copy()
    if len(selected) != len(months):
        raise ValueError("Inventário não contém exatamente os meses solicitados")
    if set(selected.resource_name_month.astype(int)) != set(months):
        raise ValueError("Meses duplicados ou ausentes no inventário")
    if not selected.head_status.eq(200).all():
        raise ValueError("Recurso sem HEAD 200")
    if selected.content_length.isna().any():
        raise ValueError("Recurso sem tamanho observado")
    rows = []
    for row in selected.sort_values("resource_name_month").to_dict("records"):
        rows.append({
            "resource_id": str(row["resource_id"]),
            "year": year,
            "month": int(row["resource_name_month"]),
            "url": str(row["source_url"]),
            "expected_bytes": int(row["content_length"]),
            "head_obtained_at_utc": str(row["obtained_at_utc"]),
        })
    return rows


def _download(
    session: requests.Session,
    resource: dict[str, object],
    path: Path,
    *,
    timeout: float,
    per_file_limit: int,
    total_so_far: int,
    total_limit: int,
) -> tuple[dict[str, object], int]:
    url = str(resource["url"])
    if urlparse(url).hostname != ALLOWED_HOST:
        raise ValueError(f"Domínio não autorizado: {url}")
    response = session.get(url, timeout=timeout, stream=True)
    response.raise_for_status()
    if urlparse(response.url).hostname != ALLOWED_HOST:
        raise ValueError(f"Domínio final não autorizado: {response.url}")
    digest = hashlib.sha256()
    size = 0
    with path.open("xb") as output:
        for chunk in response.iter_content(chunk_size=64 * 1024):
            if not chunk:
                continue
            size += len(chunk)
            if size > per_file_limit or total_so_far + size > total_limit:
                raise ValueError("Limite de download excedido")
            digest.update(chunk)
            output.write(chunk)
    if size != int(resource["expected_bytes"]):
        raise ValueError("Tamanho baixado difere do inventário HEAD")
    if not zipfile.is_zipfile(path):
        raise ValueError("Recurso baixado não é ZIP válido")
    return {
        **resource,
        "final_url": response.url,
        "status_code": response.status_code,
        "content_type": response.headers.get("Content-Type", ""),
        "actual_bytes": size,
        "sha256": digest.hexdigest(),
        "raw_file": path.name,
        "body_downloaded": True,
        "nature": "observed_raw_capture",
    }, total_so_far + size


def _profile_and_filter(
    path: Path,
    manifest: dict[str, object],
    *,
    municipality: str,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    members_seen = []
    staging_rows = []
    rows_scanned = malformed = matched = invalid_numeric = period_mismatch = 0
    with zipfile.ZipFile(path) as archive:
        members = [
            member
            for member in archive.infolist()
            if not member.is_dir()
            and Path(member.filename).suffix.lower() == ".csv"
        ]
        if len(members) != 1 or not _safe_member(members[0].filename):
            raise ValueError("ZIP deve conter exatamente um CSV seguro")
        member = members[0]
        members_seen.append(member.filename)
        with archive.open(member) as binary:
            reader = csv.reader(
                io.TextIOWrapper(
                    binary, encoding="cp1252", errors="strict", newline=""
                ),
                delimiter=";",
            )
            header = next(reader)
            positions = {name: index for index, name in enumerate(header)}
            required = {"Exercicio", "Mes", "Municipio", *OUTPUT_COLUMNS}
            if not required <= positions.keys():
                raise ValueError("Esquema mensal obrigatório ausente")
            for row_number, row in enumerate(reader, start=2):
                rows_scanned += 1
                if len(row) != len(header):
                    malformed += 1
                    continue
                try:
                    row_year = int(row[positions["Exercicio"]])
                    row_month = int(row[positions["Mes"]])
                except ValueError:
                    period_mismatch += 1
                    continue
                if (
                    row_year != int(manifest["year"])
                    or row_month != int(manifest["month"])
                ):
                    period_mismatch += 1
                    continue
                if _normalize(row[positions["Municipio"]]) != _normalize(
                    municipality
                ):
                    continue
                matched += 1
                value = _decimal(row[positions["Valor"]])
                if row[positions["Valor"]].strip() and not value:
                    invalid_numeric += 1
                    continue
                staging_rows.append({
                    "source_resource_id": manifest["resource_id"],
                    "source_archive_sha256": manifest["sha256"],
                    "source_member": member.filename,
                    "source_row_number": row_number,
                    "source_record_fingerprint": _hash_values([
                        str(manifest["resource_id"]),
                        str(row_number),
                        municipality,
                        str(row_year),
                        str(row_month),
                        value,
                    ]),
                    "government_sphere": "STATE_RS",
                    "dimension": "financas_publicas_transferencias",
                    "financial_family": "DIRECT_EXPENDITURE_OR_TRANSFER",
                    "municipality": municipality,
                    "reference_year": row_year,
                    "reference_month": row_month,
                    "territorial_match_rule": (
                        "EXACT_NORMALIZED_MUNICIPALITY_NAME"
                    ),
                    "FaseGasto": row[positions["FaseGasto"]].strip(),
                    "TipoGasto": row[positions["TipoGasto"]].strip(),
                    "Orgao": row[positions["Orgao"]].strip(),
                    "Data": row[positions["Data"]].strip(),
                    "Valor": value,
                    "source_malformed_rows_excluded": malformed,
                    "integration_status": "STAGING_NOT_CURATED",
                    "nature": "observed_filtered_source_record",
                })
    for record in staging_rows:
        record["source_malformed_rows_excluded"] = malformed
    return staging_rows, {
        "resource_id": manifest["resource_id"],
        "year": manifest["year"],
        "month": manifest["month"],
        "archive_sha256": manifest["sha256"],
        "member_names": "|".join(members_seen),
        "source_encoding": "cp1252",
        "rows_scanned": rows_scanned,
        "malformed_rows_quarantined": malformed,
        "period_mismatch_rows": period_mismatch,
        "municipality_matched_rows": matched,
        "staging_rows": len(staging_rows),
        "invalid_numeric_values": invalid_numeric,
        "sensitive_values_persisted": False,
        "nature": "calculated_streaming_profile",
    }


def build_state_rs_expense_batch(
    *,
    inventory_path: Path,
    snapshot_root: Path,
    staging_root: Path,
    audit_root: Path,
    run_id: str,
    year: int = 2026,
    months: tuple[int, ...] = (1, 2, 3, 4),
    municipality: str = "São Borja",
    session: requests.Session | None = None,
    timeout: float = 60,
    per_file_limit: int = 20_000_000,
    total_limit: int = 60_000_000,
) -> StateExpenseBatchResult:
    """Baixa e filtra um lote mensal sem extrair os CSVs para disco."""
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    resources = _selected_resources(inventory_path, year=year, months=months)
    expected_total = sum(int(row["expected_bytes"]) for row in resources)
    if expected_total > total_limit:
        raise ValueError("Inventário excede o limite total")
    targets = [
        snapshot_root.resolve() / run_id,
        staging_root.resolve() / run_id,
        audit_root.resolve() / run_id,
    ]
    partials = [
        target.with_name(f".{target.name}.partial") for target in targets
    ]
    if any(path.exists() for path in [*targets, *partials]):
        raise FileExistsError("Execução existente ou incompleta")
    for partial in partials:
        partial.mkdir(parents=True)
    client = session or requests.Session()
    manifest_rows = []
    staging_rows = []
    summary_rows = []
    total_bytes = 0
    try:
        for resource in resources:
            filename = (
                f"state_expense_{resource['year']}_{resource['month']:02d}.zip"
            )
            manifest, total_bytes = _download(
                client,
                resource,
                partials[0] / filename,
                timeout=timeout,
                per_file_limit=per_file_limit,
                total_so_far=total_bytes,
                total_limit=total_limit,
            )
            rows, summary = _profile_and_filter(
                partials[0] / filename,
                manifest,
                municipality=municipality,
            )
            manifest_rows.append(manifest)
            staging_rows.extend(rows)
            summary_rows.append(summary)
        manifest_frame = pd.DataFrame(manifest_rows)
        staging_frame = pd.DataFrame(staging_rows)
        summary_frame = pd.DataFrame(summary_rows)
        invalid = int(summary_frame.invalid_numeric_values.sum())
        period_mismatch = int(summary_frame.period_mismatch_rows.sum())
        validation = pd.DataFrame([
            ("resources_expected", len(months), "calculated", "PASS"),
            ("resources_captured", len(manifest_frame), "calculated", "PASS"),
            ("expected_bytes", expected_total, "calculated", "PASS"),
            ("actual_bytes", total_bytes, "calculated", "PASS"),
            (
                "malformed_rows_quarantined",
                int(summary_frame.malformed_rows_quarantined.sum()),
                "calculated",
                "WARN"
                if summary_frame.malformed_rows_quarantined.any()
                else "PASS",
            ),
            (
                "period_mismatch_rows",
                period_mismatch,
                "calculated",
                "FAIL" if period_mismatch else "PASS",
            ),
            (
                "invalid_numeric_values",
                invalid,
                "calculated",
                "FAIL" if invalid else "PASS",
            ),
            ("sensitive_values_persisted", 0, "calculated", "PASS"),
            ("canonical_rows_promoted", 0, "calculated", "PASS"),
        ], columns=["indicator", "value", "nature", "status"])
        if staging_frame.empty or validation.status.eq("FAIL").any():
            raise ValueError("Validação do lote estadual falhou")
        staging_frame.to_csv(
            partials[1] / "state_expense_staging.csv", index=False
        )
        manifest_frame.to_csv(
            partials[2] / "source_manifest.csv", index=False
        )
        summary_frame.to_csv(
            partials[2] / "resource_summary.csv", index=False
        )
        validation.to_csv(partials[2] / "validation.csv", index=False)
        for target in targets:
            target.parent.mkdir(parents=True, exist_ok=True)
        for partial, target in zip(partials, targets, strict=True):
            partial.replace(target)
    except Exception:
        for partial in partials:
            shutil.rmtree(partial, ignore_errors=True)
        raise
    return StateExpenseBatchResult(
        targets[0],
        targets[1],
        targets[2],
        manifest_frame,
        staging_frame,
        summary_frame,
        validation,
    )
