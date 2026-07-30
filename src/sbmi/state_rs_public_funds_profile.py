"""Perfil seguro e agregado dos recursos públicos estaduais capturados."""

from __future__ import annotations

import csv
import hashlib
import io
import shutil
import unicodedata
import zipfile
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MUNICIPALITY_COLUMNS = ("MunicipioConvenente", "Municipio")
YEAR_COLUMNS = (
    "ExercicioConvenio",
    "ExercicioParceria",
    "Exercicio",
)
SENSITIVE_COLUMN_TOKENS = (
    "cnpj",
    "cpf",
    "credor",
    "favorecido",
    "beneficiario",
    "ordenador",
    "historico",
    "objeto",
    "justificativa",
    "banco",
    "agencia",
)


@dataclass(frozen=True)
class StateFundsProfileResult:
    output_path: Path
    schema_profile: pd.DataFrame
    temporal_counts: pd.DataFrame
    territorial_summary: pd.DataFrame
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


def _year(value: str) -> int | None:
    cleaned = value.strip()
    if len(cleaned) >= 4 and cleaned[:4].isdigit():
        result = int(cleaned[:4])
        if 1900 <= result <= 2100:
            return result
    return None


def profile_state_rs_public_funds(
    *,
    snapshot_path: Path,
    output_root: Path,
    run_id: str,
    municipality: str = "São Borja",
) -> StateFundsProfileResult:
    """Lê CSVs em fluxo e publica somente esquema e contagens agregadas."""
    source = snapshot_path.resolve()
    if not source.is_dir():
        raise FileNotFoundError(f"Snapshot não encontrado: {source}")
    if not run_id or Path(run_id).name != run_id:
        raise ValueError("run_id deve ser um identificador simples")
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError("Execução existente ou incompleta")
    partial.mkdir(parents=True)
    schema_rows: list[dict[str, object]] = []
    temporal_rows: list[dict[str, object]] = []
    territorial_rows: list[dict[str, object]] = []
    target_name = _normalize(municipality)
    try:
        for archive_path in sorted(source.glob("*.zip")):
            with zipfile.ZipFile(archive_path) as archive:
                csv_members = [
                    member
                    for member in archive.infolist()
                    if not member.is_dir()
                    and Path(member.filename).suffix.lower() == ".csv"
                ]
                for member in csv_members:
                    with archive.open(member) as binary:
                        text = io.TextIOWrapper(
                            binary, encoding="utf-8-sig", errors="replace", newline=""
                        )
                        reader = csv.reader(text, delimiter=";")
                        header = next(reader)
                        municipality_indices = [
                            header.index(name)
                            for name in MUNICIPALITY_COLUMNS
                            if name in header
                        ]
                        year_indices = [
                            header.index(name) for name in YEAR_COLUMNS if name in header
                        ]
                        sensitive_columns = [
                            name
                            for name in header
                            if any(
                                token in _normalize(name).lower()
                                for token in SENSITIVE_COLUMN_TOKENS
                            )
                        ]
                        total_by_year: Counter[int] = Counter()
                        matched_by_year: Counter[int] = Counter()
                        rows_scanned = 0
                        malformed_rows = 0
                        matched_rows = 0
                        for row in reader:
                            rows_scanned += 1
                            if len(row) != len(header):
                                malformed_rows += 1
                                continue
                            year = next(
                                (
                                    parsed
                                    for index in year_indices
                                    if (parsed := _year(row[index])) is not None
                                ),
                                None,
                            )
                            if year is not None:
                                total_by_year[year] += 1
                            is_match = any(
                                _normalize(row[index]) == target_name
                                for index in municipality_indices
                            )
                            if is_match:
                                matched_rows += 1
                                if year is not None:
                                    matched_by_year[year] += 1
                        resource_id = archive_path.stem
                        schema_rows.append({
                            "resource_id": resource_id,
                            "archive_sha256": _sha256(archive_path),
                            "member_name": member.filename,
                            "encoding": "utf-8-sig_with_replacement",
                            "delimiter": ";",
                            "column_count": len(header),
                            "column_names": "|".join(header),
                            "municipality_columns": "|".join(
                                header[index] for index in municipality_indices
                            ),
                            "year_columns": "|".join(
                                header[index] for index in year_indices
                            ),
                            "sensitive_fields_present": bool(sensitive_columns),
                            "sensitive_column_names": "|".join(sensitive_columns),
                            "sensitive_values_persisted": False,
                            "rows_scanned": rows_scanned,
                            "malformed_rows": malformed_rows,
                            "nature": "observed_schema_and_calculated_counts",
                        })
                        all_years = sorted(total_by_year)
                        match_years = sorted(matched_by_year)
                        territorial_rows.append({
                            "resource_id": resource_id,
                            "municipality": municipality,
                            "match_rule": "EXACT_NORMALIZED_MUNICIPALITY_NAME",
                            "rows_scanned": rows_scanned,
                            "matched_rows": matched_rows,
                            "match_share": (
                                matched_rows / rows_scanned if rows_scanned else 0
                            ),
                            "minimum_year": all_years[0] if all_years else None,
                            "maximum_year": all_years[-1] if all_years else None,
                            "matched_minimum_year": (
                                match_years[0] if match_years else None
                            ),
                            "matched_maximum_year": (
                                match_years[-1] if match_years else None
                            ),
                            "values_persisted": False,
                            "integration_status": "NOT_INTEGRATED",
                            "nature": "calculated_aggregate",
                        })
                        for year in sorted(set(total_by_year) | set(matched_by_year)):
                            temporal_rows.append({
                                "resource_id": resource_id,
                                "year": year,
                                "rows": total_by_year[year],
                                "municipality_matched_rows": matched_by_year[year],
                                "nature": "calculated_aggregate",
                            })
        schema = pd.DataFrame(schema_rows)
        temporal = pd.DataFrame(temporal_rows)
        territorial = pd.DataFrame(territorial_rows)
        validation = pd.DataFrame(
            [
                ("csv_members_profiled", len(schema), "calculated", "PASS"),
                (
                    "malformed_rows_quarantined",
                    int(schema.malformed_rows.sum()) if not schema.empty else 0,
                    "calculated",
                    "PASS" if schema.empty or not schema.malformed_rows.any() else "WARN",
                ),
                ("sensitive_values_persisted", 0, "calculated", "PASS"),
                ("row_level_values_persisted", 0, "calculated", "PASS"),
                ("canonical_rows_promoted", 0, "calculated", "PASS"),
            ],
            columns=["indicator", "value", "nature", "status"],
        )
        if schema.empty or validation.status.eq("FAIL").any():
            raise ValueError("Validação do perfil estadual falhou")
        schema.to_csv(partial / "schema_profile.csv", index=False)
        temporal.to_csv(partial / "temporal_counts.csv", index=False)
        territorial.to_csv(partial / "territorial_summary.csv", index=False)
        validation.to_csv(partial / "validation.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return StateFundsProfileResult(target, schema, temporal, territorial, validation)
