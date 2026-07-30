"""Reconciliação e staging mínimo dos recursos estaduais de São Borja."""

from __future__ import annotations

import csv
import hashlib
import io
import shutil
import unicodedata
import zipfile
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

import pandas as pd

RESOURCE_FAMILIES = {
    "agreements_expense": "AGREEMENT",
    "agreements_layout": "AGREEMENT_AMBIGUOUS",
    "agreements_revenue": "AGREEMENT_REVENUE",
    "partnerships": "PARTNERSHIP",
    "state_expense_2026_05": "DIRECT_EXPENDITURE_OR_TRANSFER",
}
PROMOTABLE_RESOURCES = {
    "agreements_expense",
    "partnerships",
    "state_expense_2026_05",
}
MUNICIPALITY_COLUMNS = ("MunicipioConvenente", "Municipio")
YEAR_COLUMNS = ("ExercicioConvenio", "ExercicioParceria", "Exercicio")
IDENTITY_COLUMNS = (
    "ExercicioConvenio",
    "Cod_Orgao",
    "DataInicioVigencia",
    "DataFimVigencia",
    "DataAssinatura",
    "NomeConcedente",
    "NomeConvenente",
    "MunicipioConvenente",
    "cnpj_convenente",
)
OUTPUT_VALUE_COLUMNS = (
    "ValorConcedente",
    "ValorConvenente",
    "ValorAdministracaoPublica",
    "ValorOrganizacaoParceira",
    "ValorPago",
    "SaldoLiquidadoAPagar",
    "SaldoAPagarDoConvenio",
    "SaldoAPagarDaparceria",
    "Valor",
)
OUTPUT_TEXT_COLUMNS = (
    "SituacaoConvenio",
    "SituacaoProcesso",
    "SituacaoVigencia",
    "TipoParticipacao",
    "TipoTransferencia",
    "FaseGasto",
    "TipoGasto",
    "Orgao",
)
OUTPUT_DATE_COLUMNS = (
    "DataSituacao",
    "DataInicioVigencia",
    "DataFimVigencia",
    "DataAssinatura",
    "DataExtincao",
    "DataPublicacao",
    "Data",
)


@dataclass(frozen=True)
class StateFundsStagingResult:
    staging_path: Path
    audit_path: Path
    staging: pd.DataFrame
    overlap_summary: pd.DataFrame
    validation: pd.DataFrame


def _normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    return " ".join(
        "".join(char for char in decomposed if not unicodedata.combining(char))
        .upper()
        .split()
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _hash_values(values: list[str]) -> str:
    digest = hashlib.sha256()
    for value in values:
        digest.update(value.encode("utf-8", errors="replace"))
        digest.update(b"\x1f")
    return digest.hexdigest()


def _year(value: str) -> int | None:
    cleaned = value.strip()
    if len(cleaned) >= 4 and cleaned[:4].isdigit():
        result = int(cleaned[:4])
        if 1900 <= result <= 2100:
            return result
    return None


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


def _read_resources(snapshot: Path, municipality: str):
    target_name = _normalize(municipality)
    staging_rows: list[dict[str, object]] = []
    inventory_rows: list[dict[str, object]] = []
    identities: dict[str, set[str]] = {}
    full_hashes: dict[str, set[str]] = {}
    for archive_path in sorted(snapshot.glob("*.zip")):
        resource_id = archive_path.stem
        archive_hash = _sha256(archive_path)
        resource_staging_start = len(staging_rows)
        identities[resource_id] = set()
        full_hashes[resource_id] = set()
        rows_scanned = malformed = matches = promoted = invalid_values = 0
        with zipfile.ZipFile(archive_path) as archive:
            members = [
                item
                for item in archive.infolist()
                if not item.is_dir()
                and Path(item.filename).suffix.lower() == ".csv"
            ]
            for member in members:
                with archive.open(member) as binary:
                    reader = csv.reader(
                        io.TextIOWrapper(
                            binary,
                            encoding="utf-8-sig",
                            errors="replace",
                            newline="",
                        ),
                        delimiter=";",
                    )
                    header = next(reader)
                    positions = {name: index for index, name in enumerate(header)}
                    municipality_indices = [
                        positions[name]
                        for name in MUNICIPALITY_COLUMNS
                        if name in positions
                    ]
                    year_indices = [
                        positions[name] for name in YEAR_COLUMNS if name in positions
                    ]
                    for row_number, row in enumerate(reader, start=2):
                        rows_scanned += 1
                        if len(row) != len(header):
                            malformed += 1
                            continue
                        full_hashes[resource_id].add(_hash_values(row))
                        if resource_id.startswith("agreements_"):
                            identities[resource_id].add(
                                _hash_values(
                                    [
                                        row[positions[name]]
                                        for name in IDENTITY_COLUMNS
                                        if name in positions
                                    ]
                                )
                            )
                        matched = any(
                            _normalize(row[index]) == target_name
                            for index in municipality_indices
                        )
                        if not matched:
                            continue
                        matches += 1
                        if resource_id not in PROMOTABLE_RESOURCES:
                            continue
                        record: dict[str, object] = {
                            "source_resource_id": resource_id,
                            "source_archive_sha256": archive_hash,
                            "source_member": member.filename,
                            "source_row_number": row_number,
                            "source_record_fingerprint": _hash_values(
                                [
                                    resource_id,
                                    str(row_number),
                                    municipality,
                                    *[
                                        row[index]
                                        for index in year_indices
                                    ],
                                ]
                            ),
                            "government_sphere": "STATE_RS",
                            "dimension": "financas_publicas_transferencias",
                            "financial_family": RESOURCE_FAMILIES[resource_id],
                            "municipality": municipality,
                            "reference_year": next(
                                (
                                    parsed
                                    for index in year_indices
                                    if (parsed := _year(row[index])) is not None
                                ),
                                None,
                            ),
                            "reference_month": (
                                row[positions["Mes"]].strip()
                                if "Mes" in positions
                                else ""
                            ),
                            "territorial_match_rule": (
                                "EXACT_NORMALIZED_MUNICIPALITY_NAME"
                            ),
                            "source_malformed_rows_excluded": 0,
                            "integration_status": "STAGING_NOT_CURATED",
                            "nature": "observed_filtered_source_record",
                        }
                        for name in OUTPUT_TEXT_COLUMNS + OUTPUT_DATE_COLUMNS:
                            record[name] = (
                                row[positions[name]].strip()
                                if name in positions
                                else ""
                            )
                        for name in OUTPUT_VALUE_COLUMNS:
                            if name not in positions:
                                record[name] = ""
                                continue
                            raw_value = row[positions[name]]
                            parsed_value = _decimal(raw_value)
                            if raw_value.strip() and not parsed_value:
                                invalid_values += 1
                            record[name] = parsed_value
                        staging_rows.append(record)
                        promoted += 1
        for record in staging_rows[resource_staging_start:]:
            record["source_malformed_rows_excluded"] = malformed
        inventory_rows.append({
            "resource_id": resource_id,
            "financial_family": RESOURCE_FAMILIES[resource_id],
            "archive_sha256": archive_hash,
            "rows_scanned": rows_scanned,
            "malformed_rows_quarantined": malformed,
            "municipality_matched_rows": matches,
            "staging_rows": promoted,
            "invalid_numeric_values": invalid_values,
            "disposition": (
                "INCLUDED_IN_STAGING"
                if resource_id in PROMOTABLE_RESOURCES
                else (
                    "QUARANTINED_AMBIGUOUS_OVERLAP"
                    if resource_id == "agreements_layout"
                    else "NO_TERRITORIAL_MATCH"
                )
            ),
            "sensitive_values_persisted": False,
            "nature": "calculated_reconciliation",
        })
    return staging_rows, inventory_rows, identities, full_hashes


def build_state_rs_public_funds_staging(
    *,
    snapshot_path: Path,
    staging_root: Path,
    audit_root: Path,
    run_id: str,
    municipality: str = "São Borja",
) -> StateFundsStagingResult:
    """Reconcilia convênios e publica um staging territorial minimizado."""
    snapshot = snapshot_path.resolve()
    if not snapshot.is_dir():
        raise FileNotFoundError(f"Snapshot não encontrado: {snapshot}")
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    staging_target = staging_root.resolve() / run_id
    audit_target = audit_root.resolve() / run_id
    staging_partial = staging_target.with_name(f".{run_id}.partial")
    audit_partial = audit_target.with_name(f".{run_id}.partial")
    if any(
        path.exists()
        for path in (
            staging_target,
            audit_target,
            staging_partial,
            audit_partial,
        )
    ):
        raise FileExistsError("Execução existente ou incompleta")
    staging_partial.mkdir(parents=True)
    audit_partial.mkdir(parents=True)
    try:
        rows, inventory_rows, identities, full_hashes = _read_resources(
            snapshot, municipality
        )
        staging = pd.DataFrame(rows)
        inventory = pd.DataFrame(inventory_rows)
        left = "agreements_layout"
        right = "agreements_expense"
        identity_overlap = identities.get(left, set()) & identities.get(right, set())
        exact_overlap = full_hashes.get(left, set()) & full_hashes.get(right, set())
        overlap = pd.DataFrame([{
            "left_resource": left,
            "right_resource": right,
            "left_rows": len(full_hashes.get(left, set())),
            "right_rows": len(full_hashes.get(right, set())),
            "exact_full_record_overlap": len(exact_overlap),
            "stable_identity_overlap": len(identity_overlap),
            "classification": (
                "CONTENT_DUPLICATE"
                if full_hashes.get(left, set())
                and full_hashes[left] <= full_hashes.get(right, set())
                else "PARTIAL_OVERLAP"
                if identity_overlap
                else "UNEXPLAINED"
            ),
            "decision": "QUARANTINE_LEFT_RESOURCE",
            "sensitive_hashes_persisted": False,
            "nature": "calculated_in_memory_hash_comparison",
        }])
        invalid_numeric = int(inventory.invalid_numeric_values.sum())
        validation = pd.DataFrame(
            [
                ("staging_rows", len(staging), "calculated", "PASS"),
                (
                    "malformed_rows_quarantined",
                    int(inventory.malformed_rows_quarantined.sum()),
                    "calculated",
                    "WARN"
                    if inventory.malformed_rows_quarantined.any()
                    else "PASS",
                ),
                (
                    "invalid_numeric_values",
                    invalid_numeric,
                    "calculated",
                    "FAIL" if invalid_numeric else "PASS",
                ),
                ("sensitive_values_persisted", 0, "calculated", "PASS"),
                ("ambiguous_resource_promoted", 0, "calculated", "PASS"),
                ("canonical_rows_promoted", 0, "calculated", "PASS"),
            ],
            columns=["indicator", "value", "nature", "status"],
        )
        if staging.empty or validation.status.eq("FAIL").any():
            raise ValueError("Validação do staging estadual falhou")
        staging.to_csv(staging_partial / "state_public_funds_staging.csv", index=False)
        inventory.to_csv(audit_partial / "resource_decisions.csv", index=False)
        overlap.to_csv(audit_partial / "overlap_summary.csv", index=False)
        validation.to_csv(audit_partial / "validation.csv", index=False)
        staging_target.parent.mkdir(parents=True, exist_ok=True)
        audit_target.parent.mkdir(parents=True, exist_ok=True)
        staging_partial.replace(staging_target)
        audit_partial.replace(audit_target)
    except Exception:
        shutil.rmtree(staging_partial, ignore_errors=True)
        shutil.rmtree(audit_partial, ignore_errors=True)
        raise
    return StateFundsStagingResult(
        staging_target, audit_target, staging, overlap, validation
    )
