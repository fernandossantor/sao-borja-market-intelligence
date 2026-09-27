"""Verified promotion of small audited derivatives to Google Drive."""

from __future__ import annotations

import hashlib
import json
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

from sbmi.drive import remote_spec, run_rclone
from sbmi.google_drive import FOLDER_MIME_TYPE, get_file_metadata, list_children

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
    """Create a Drive write session for shared-drive/service-account use cases."""
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
    if not response.ok:
        detail = response.text.strip()
        raise RuntimeError(
            f"Falha no upload Drive de {path.name}: HTTP {response.status_code}: {detail}"
        )
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
    """Promote audited derivatives with a Drive API session.

    This backend is suitable for a human OAuth session or a service account writing
    to a Shared Drive. Service accounts cannot own files in a user's My Drive.
    """
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


def _configured_rclone_remotes() -> set[str]:
    result = run_rclone(["listremotes"])
    return {line.strip().removesuffix(":") for line in result.stdout.splitlines() if line.strip()}


def _rclone_list_files(remote: str, remote_folder_path: str) -> dict[str, list[dict[str, Any]]]:
    result = run_rclone(
        [
            "lsjson",
            remote_spec(remote, remote_folder_path),
            "--files-only",
            "--max-depth",
            "1",
        ]
    )
    payload = json.loads(result.stdout or "[]")
    if not isinstance(payload, list):
        raise RuntimeError("Resposta inesperada do rclone lsjson")
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in payload:
        if not isinstance(item, dict):
            continue
        name = str(item.get("Name") or item.get("Path") or "").strip()
        if name:
            grouped.setdefault(name, []).append(item)
    return grouped


def _verify_remote_rclone_file(
    remote: str,
    remote_file_path: str,
    expected: ExpectedDerivative,
) -> None:
    with tempfile.TemporaryDirectory(prefix="sbmi-drive-verify-") as temp_dir:
        local_copy = Path(temp_dir) / expected.name
        run_rclone(["copyto", remote_spec(remote, remote_file_path), str(local_copy)])
        observed_size = local_copy.stat().st_size
        observed_sha256 = sha256_file(local_copy)
        if observed_size != expected.size_bytes or observed_sha256 != expected.sha256.lower():
            raise ValueError(
                f"Cópia remota divergente para {expected.name}: "
                f"size={observed_size}, sha256={observed_sha256}"
            )


def promote_derivatives_rclone(
    *,
    output_dir: Path,
    remote: str,
    remote_folder_path: str,
    expected: list[ExpectedDerivative],
) -> list[PromotedDerivative]:
    """Promote audited derivatives using a human-OAuth rclone remote.

    The write remote is intentionally separate from the project's read-only remote.
    Every local file is validated before upload and every remote file is downloaded
    back after upload/reuse so SHA-256 can be checked independently of Drive metadata.
    """
    configured = _configured_rclone_remotes()
    normalized_remote = remote.strip().removesuffix(":")
    if normalized_remote not in configured:
        raise RuntimeError(
            f"Remote rclone de escrita '{normalized_remote}' não configurado. "
            "Configure um remote OAuth humano separado antes da promoção."
        )

    local = validate_local_derivatives(output_dir, expected)
    remote_files = _rclone_list_files(normalized_remote, remote_folder_path)
    results: list[PromotedDerivative] = []

    for item in expected:
        matches = remote_files.get(item.name, [])
        if len(matches) > 1:
            raise ValueError(f"Mais de um arquivo remoto com nome {item.name} no destino")

        remote_file_path = f"{remote_folder_path.rstrip('/')}/{item.name}"
        reused = bool(matches)
        if reused:
            _verify_remote_rclone_file(normalized_remote, remote_file_path, item)
        else:
            run_rclone(
                [
                    "copyto",
                    str(local[item.name]),
                    remote_spec(normalized_remote, remote_file_path),
                ]
            )
            _verify_remote_rclone_file(normalized_remote, remote_file_path, item)

        refreshed = _rclone_list_files(normalized_remote, remote_folder_path).get(item.name, [])
        if len(refreshed) != 1:
            raise RuntimeError(
                f"Não foi possível identificar univocamente {item.name} após promoção"
            )
        drive_file_id = str(refreshed[0].get("ID", ""))
        results.append(
            PromotedDerivative(
                item.name,
                drive_file_id,
                item.size_bytes,
                item.sha256.lower(),
                reused,
            )
        )
        remote_files[item.name] = refreshed

    return results
