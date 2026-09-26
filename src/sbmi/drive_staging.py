"""Stage immutable project inputs from the Google Drive master copy."""

from __future__ import annotations

import hashlib
import os
from dataclasses import dataclass
from pathlib import Path

from google.auth.transport.requests import AuthorizedSession

from sbmi.google_drive import DRIVE_API_BASE, FOLDER_MIME_TYPE, get_file_metadata


@dataclass(frozen=True)
class StagedDriveFile:
    """Result of a verified Drive-to-local staging operation."""

    drive_file_id: str
    drive_file_name: str
    local_path: Path
    size_bytes: int
    sha256: str
    reused_existing: bool


def sha256_file(path: Path, *, chunk_size: int = 8 * 1024 * 1024) -> str:
    """Calculate SHA-256 without loading the whole file into memory."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _validate_local_file(
    path: Path,
    *,
    expected_size: int | None,
    expected_sha256: str | None,
) -> tuple[int, str]:
    size = path.stat().st_size
    sha256 = sha256_file(path)
    if expected_size is not None and size != expected_size:
        raise ValueError(
            f"Tamanho local divergente para {path}: observado={size}, "
            f"esperado={expected_size}"
        )
    if expected_sha256 is not None and sha256 != expected_sha256.lower():
        raise ValueError(
            f"SHA-256 local divergente para {path}: observado={sha256}, "
            f"esperado={expected_sha256}"
        )
    return size, sha256


def stage_drive_file(
    session: AuthorizedSession,
    *,
    file_id: str,
    target: Path,
    expected_size: int | None = None,
    expected_sha256: str | None = None,
    chunk_size: int = 8 * 1024 * 1024,
) -> StagedDriveFile:
    """Copy one Drive file to local staging and validate it before promotion.

    Existing validated targets are reused. Existing divergent targets are never
    overwritten. New transfers are written to ``.partial`` and atomically
    promoted only after size and SHA-256 validation.
    """
    target = Path(target)
    metadata = get_file_metadata(session, file_id)
    if metadata.get("mimeType") == FOLDER_MIME_TYPE:
        raise ValueError(f"O ID {file_id} corresponde a uma pasta, não a um arquivo")

    drive_name = str(metadata.get("name", file_id))
    metadata_size_raw = metadata.get("size")
    if expected_size is not None and metadata_size_raw not in {None, ""}:
        metadata_size = int(metadata_size_raw)
        if metadata_size != expected_size:
            raise ValueError(
                "Tamanho informado pelo Drive diverge do esperado para "
                f"{drive_name}: observado={metadata_size}, esperado={expected_size}"
            )

    metadata_sha256 = str(metadata.get("sha256Checksum", "")).strip().lower()
    if expected_sha256 is not None and metadata_sha256:
        if metadata_sha256 != expected_sha256.lower():
            raise ValueError(
                "SHA-256 informado pelo Drive diverge do esperado para "
                f"{drive_name}: observado={metadata_sha256}, esperado={expected_sha256}"
            )

    if target.exists():
        size, sha256 = _validate_local_file(
            target,
            expected_size=expected_size,
            expected_sha256=expected_sha256,
        )
        return StagedDriveFile(file_id, drive_name, target, size, sha256, True)

    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_name(f"{target.name}.partial")
    if partial.exists():
        raise FileExistsError(
            f"Arquivo parcial já existe; revise antes de nova tentativa: {partial}"
        )

    response = session.get(
        f"{DRIVE_API_BASE}/{file_id}",
        params={"alt": "media", "supportsAllDrives": "true"},
        stream=True,
        timeout=300,
    )
    response.raise_for_status()

    digest = hashlib.sha256()
    size = 0
    with partial.open("wb") as handle:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if not chunk:
                continue
            handle.write(chunk)
            digest.update(chunk)
            size += len(chunk)

    sha256 = digest.hexdigest()
    if expected_size is not None and size != expected_size:
        raise ValueError(
            "Tamanho transferido divergente para "
            f"{drive_name}: observado={size}, esperado={expected_size}; "
            f"arquivo parcial preservado em {partial}"
        )
    if expected_sha256 is not None and sha256 != expected_sha256.lower():
        raise ValueError(
            "SHA-256 transferido divergente para "
            f"{drive_name}: observado={sha256}, esperado={expected_sha256}; "
            f"arquivo parcial preservado em {partial}"
        )

    os.replace(partial, target)
    return StagedDriveFile(file_id, drive_name, target, size, sha256, False)
