"""Auditoria conservadora dos arquivos oficiais de IPM definitivo do RS."""

from __future__ import annotations

import hashlib
import unicodedata
import zipfile
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class IpmArchiveAuditResult:
    """Resultado mínimo da inspeção de um arquivo definitivo de IPM."""

    distribution_year: int
    archive_path: Path
    archive_bytes: int
    archive_sha256: str
    import_member: str
    encoding: str
    matched_lines: tuple[str, ...]


def _normalize(value: str) -> str:
    decomposed = unicodedata.normalize("NFKD", value)
    return " ".join(
        "".join(ch for ch in decomposed if not unicodedata.combining(ch))
        .upper()
        .split()
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _decode(payload: bytes) -> tuple[str, str]:
    for encoding in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return payload.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("unknown", payload, 0, 1, "unsupported text encoding")


def _select_import_member(archive: zipfile.ZipFile) -> zipfile.ZipInfo:
    candidates = [
        member
        for member in archive.infolist()
        if not member.is_dir()
        and Path(member.filename).name.upper().startswith("DAIM545X")
    ]
    if len(candidates) != 1:
        names = [member.filename for member in candidates]
        raise ValueError(
            "Esperado exatamente um membro DAIM545X no ZIP; "
            f"encontrados={len(candidates)} nomes={names}"
        )
    return candidates[0]


def audit_ipm_archive(
    archive_path: Path,
    *,
    distribution_year: int,
    municipality: str = "São Borja",
) -> IpmArchiveAuditResult:
    """Inspeciona DAIM545X sem inferir ainda o layout numérico."""
    path = Path(archive_path).resolve()
    if not path.is_file():
        raise FileNotFoundError(path)
    if not 1900 <= int(distribution_year) <= 2200:
        raise ValueError("Ano de distribuição inválido")

    with zipfile.ZipFile(path) as archive:
        member = _select_import_member(archive)
        text, encoding = _decode(archive.read(member))

    target = _normalize(municipality)
    matches = tuple(
        line.rstrip("\r\n")
        for line in text.splitlines()
        if target in _normalize(line)
    )
    if not matches:
        raise ValueError(f"Município não localizado no DAIM545X: {municipality}")

    return IpmArchiveAuditResult(
        distribution_year=int(distribution_year),
        archive_path=path,
        archive_bytes=path.stat().st_size,
        archive_sha256=_sha256(path),
        import_member=member.filename,
        encoding=encoding,
        matched_lines=matches,
    )


def audit_results_table(results: list[IpmArchiveAuditResult]) -> pd.DataFrame:
    """Publica apenas metadados e linhas municipais para auditoria de layout."""
    rows: list[dict[str, object]] = []
    for result in results:
        for position, line in enumerate(result.matched_lines, start=1):
            rows.append(
                {
                    "distribution_year": result.distribution_year,
                    "archive_file": result.archive_path.name,
                    "archive_bytes": result.archive_bytes,
                    "archive_sha256": result.archive_sha256,
                    "import_member": result.import_member,
                    "encoding": result.encoding,
                    "municipality_match_position": position,
                    "raw_municipality_line": line,
                    "nature": "observed_official_archive_layout",
                }
            )
    return pd.DataFrame(rows).sort_values(
        ["distribution_year", "municipality_match_position"]
    )
