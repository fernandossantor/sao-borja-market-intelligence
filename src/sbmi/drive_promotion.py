"""Verified promotion of small audited derivatives to Google Drive."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

from sbmi.google_drive import DRIVE_API_BASE, FOLDER_MIME_TYPE, get_file_metadata, list_children

DRIVE_WRITE_SCOPE = "https://www.googleapis.com/auth/drive"
DRIVE_UPLOAD_BASE = "https://www.googleapis.com/upload/drive/v3/files"


@dataclass(frozen=True)
class ExpectedDerivative:
    """Expected immutable properties of one promoted derivative."""

    name: str
    size_bytes: int
    sha256: str


@dataclass(frozen=True)
class PromotedDerivative:
    """Drive result for one promoted or safely reused derivative."""

    name: str
    drive_file_id: str
    size_bytes: int
    sha256: str
    reused_existing: bool


def build_authorized_write_session(info: dict[str, Any]) -> AuthorizedSession:
    """Create a Drive write session without changing the read-only default helper."""
    credentials = service_account.Credentials.from_service_account_info(
        info,
        scopes=[DRIVE_WRITE_SCOPE],
    )
    return AuthorizedSession(credentials)


def sha256_file(path: Path, *, chunk_size: int = 8 * 1024 * 1024) -> str:
    """Hash one local derivative without loading it all into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_local_derivatives(
    output_dir: Path,
    expected: list[ExpectedDerivative],
) -> dict[str, Path]:
    """Validate exact filename, size and SHA-256 before any external write."""
    output_dir = Path(output_dir)
    validated: dict[str, Path] = {}
    for item in expected:
        path = output_dir / item.name
        if not path.is_file():
            raise FileNotFoundError(path)
        size = path.stat().st_size
        if size != item.size_bytes:
            raise ValueError(
                f"Tamanho divergente para {item.name}: observado={size}, esperado={item.size_bytes}"
            )
        sha256 = sha256_file(path)
        if sha256 != item.sha256.lower():
            raise ValueError(
                f"SHA-256 divergente para {item.name}: observado={sha256}, esperado={item.sha256}"
            )
        validated[item.name] = path
    return validated


def _metadata_integrity(metadata: dict[str, Any]) -> tuple[int, str]:
    size_raw = metadata.get("size")
    sha256 = str(metadata.get("sha256Checksum", "")).strip().lower()
    if size_raw in {None, ""} or not sha256:
        raise ValueError("Metadados do Drive não contêm size/sha256Checksum para validação")
    return int(size_raw), sha256


def _find_existing_by_name(
    session: AuthorizedSession,
    parent_folder_id: str,
    name: str,
) -> list[dict[str, Any]]:
    return [item for item in list_children(session, parent_folder_id) if item.get("name") == name]


def _upload_one(
    session: AuthorizedSession,
    path: Path,
    parent_folder_id: str,
) -> dict[str, Any]:
    metadata = {"name": path.name, "parents": [parent_folder_id]}
    with path.open("rb") as handle:
        files = {
            "metadata": (
                "metadata",
                json.dumps(metadata, ensure_ascii=False),
                "application/json; charset=UTF-8",
            ),
            "file": (path.name, handle, "text/csv"),
        }
        response = session.post(
            DRIVE_UPLOAD_BASE,
            params={
                "uploadType": "multipart",
                "supportsAllDrives": "true",
                "fields": "id,name,size,sha256Checksum,parents",
            },
            files=files,
            timeout=300,
        )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict) or not payload.get("id"):
        raise RuntimeError(f"Resposta de upload inválida para {path.name}")
    return payload


def promote_derivatives(
    session: AuthorizedSession,
    *,
    output_dir: Path,
    parent_folder_id: str,
    expected: list[ExpectedDerivative],
) -> list[PromotedDerivative]:
    """Promote audited derivatives idempotently, refusing divergent collisions."""
    folder = get_file_metadata(session, parent_folder_id)
    if folder.get("mimeType") != FOLDER_MIME_TYPE:
        raise ValueError(f"Destino {parent_folder_id} não é uma pasta do Google Drive")

    local = validate_local_derivatives(output_dir, expected)
    results: list[PromotedDerivative] = []

    for item in expected:
        matches = _find_existing_by_name(session, parent_folder_id, item.name)
        if len(matches) > 1:
            raise ValueError(f"Mais de um arquivo existente com nome {item.name} no destino")
        if matches:
            existing = matches[0]
            size, sha256 = _metadata_integrity(existing)
            if size != item.size_bytes or sha256 != item.sha256.lower():
                raise ValueError(
                    f"Colisão divergente no Drive para {item.name}: size={size}, sha256={sha256}"
                )
            results.append(
                PromotedDerivative(item.name, str(existing["id"]), size, sha256, True)
            )
            continue

        uploaded = _upload_one(session, local[item.name], parent_folder_id)
        uploaded_id = str(uploaded["id"])
        verified = get_file_metadata(session, uploaded_id)
        size, sha256 = _metadata_integrity(verified)
        if size != item.size_bytes or sha256 != item.sha256.lower():
            raise ValueError(
                f"Upload divergente para {item.name}: size={size}, sha256={sha256}"
            )
        results.append(PromotedDerivative(item.name, uploaded_id, size, sha256, False))

    return results
