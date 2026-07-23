"""Acesso somente leitura ao Google Drive por conta de serviço."""

from __future__ import annotations

import base64
import binascii
import json
import os
from collections import deque
from pathlib import PurePosixPath
from typing import Any

import pandas as pd
from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account

DRIVE_READONLY_SCOPE = "https://www.googleapis.com/auth/drive.readonly"
DRIVE_API_BASE = "https://www.googleapis.com/drive/v3/files"
FOLDER_MIME_TYPE = "application/vnd.google-apps.folder"

INVENTORY_COLUMNS = [
    "drive_file_id",
    "relative_path",
    "file_name",
    "extension",
    "mime_type",
    "is_folder",
    "size_bytes",
    "created_at_utc",
    "modified_at_utc",
    "md5_checksum",
    "sha1_checksum",
    "sha256_checksum",
    "parent_drive_file_id",
    "audit_status",
]

REQUIRED_SERVICE_ACCOUNT_FIELDS = {
    "type",
    "project_id",
    "private_key_id",
    "private_key",
    "client_email",
    "client_id",
    "token_uri",
}

FILE_FIELDS = (
    "id,name,mimeType,size,createdTime,modifiedTime,md5Checksum,"
    "sha1Checksum,sha256Checksum,parents,fullFileExtension"
)


def decode_service_account_info(encoded_secret: str) -> dict[str, Any]:
    """Decodifica e valida a credencial JSON armazenada em Base64."""
    compact = "".join(encoded_secret.split())
    if not compact:
        raise ValueError("A credencial Base64 está vazia.")

    try:
        raw = base64.b64decode(compact, validate=True)
        payload = json.loads(raw.decode("utf-8"))
    except (binascii.Error, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("A credencial não é um JSON Base64 válido.") from exc

    if not isinstance(payload, dict):
        raise ValueError("A credencial decodificada deve ser um objeto JSON.")

    missing = REQUIRED_SERVICE_ACCOUNT_FIELDS.difference(payload)
    if missing:
        raise ValueError(f"Campos obrigatórios ausentes na conta de serviço: {sorted(missing)}")

    if payload.get("type") != "service_account":
        raise ValueError("A credencial não pertence a uma conta de serviço.")

    return payload


def service_account_info_from_environment(
    env_name: str = "SBMI_GDRIVE_SA_B64",
) -> dict[str, Any]:
    """Lê a credencial da variável de ambiente sem gravá-la em disco."""
    encoded = os.getenv(env_name)
    if encoded is None:
        raise RuntimeError(
            f"Segredo {env_name} não encontrado no ambiente do Codespace."
        )
    return decode_service_account_info(encoded)


def build_authorized_session(info: dict[str, Any]) -> AuthorizedSession:
    """Cria sessão autenticada exclusivamente com escopo de leitura."""
    credentials = service_account.Credentials.from_service_account_info(
        info,
        scopes=[DRIVE_READONLY_SCOPE],
    )
    return AuthorizedSession(credentials)


def get_file_metadata(session: AuthorizedSession, file_id: str) -> dict[str, Any]:
    """Obtém metadados de um arquivo ou pasta por ID."""
    response = session.get(
        f"{DRIVE_API_BASE}/{file_id}",
        params={
            "fields": FILE_FIELDS,
            "supportsAllDrives": "true",
        },
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise RuntimeError("Resposta inesperada da API do Google Drive.")
    return payload


def list_children(session: AuthorizedSession, parent_id: str) -> list[dict[str, Any]]:
    """Lista todos os filhos diretos de uma pasta, com paginação."""
    items: list[dict[str, Any]] = []
    page_token: str | None = None

    while True:
        params = {
            "q": f"'{parent_id}' in parents and trashed = false",
            "fields": f"nextPageToken,files({FILE_FIELDS})",
            "pageSize": 1000,
            "spaces": "drive",
            "supportsAllDrives": "true",
            "includeItemsFromAllDrives": "true",
        }
        if page_token:
            params["pageToken"] = page_token

        response = session.get(DRIVE_API_BASE, params=params, timeout=60)
        response.raise_for_status()
        payload = response.json()
        if not isinstance(payload, dict):
            raise RuntimeError("Resposta inesperada da API do Google Drive.")

        page_items = payload.get("files", [])
        if not isinstance(page_items, list):
            raise RuntimeError("Lista de arquivos inválida na resposta do Google Drive.")
        items.extend(item for item in page_items if isinstance(item, dict))

        page_token = payload.get("nextPageToken")
        if not page_token:
            break

    return items


def check_root_folder(
    session: AuthorizedSession,
    root_folder_id: str,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Confirma que a raiz é uma pasta acessível e lista seu primeiro nível."""
    root = get_file_metadata(session, root_folder_id)
    if root.get("mimeType") != FOLDER_MIME_TYPE:
        raise ValueError("O ID informado não corresponde a uma pasta do Google Drive.")
    return root, list_children(session, root_folder_id)


def _relative_path(parent_path: str, file_name: str) -> str:
    if parent_path:
        return (PurePosixPath(parent_path) / file_name).as_posix()
    return PurePosixPath(file_name).as_posix()


def build_drive_inventory(
    session: AuthorizedSession,
    root_folder_id: str,
) -> pd.DataFrame:
    """Gera inventário recursivo de metadados sem baixar conteúdos."""
    root, first_level = check_root_folder(session, root_folder_id)
    queue: deque[tuple[str, str, list[dict[str, Any]] | None]] = deque(
        [(str(root["id"]), "", first_level)]
    )
    visited_folders = {str(root["id"])}
    records: list[dict[str, object]] = []

    while queue:
        parent_id, parent_path, prefetched = queue.popleft()
        children = prefetched if prefetched is not None else list_children(session, parent_id)

        for item in children:
            item_id = str(item.get("id", ""))
            file_name = str(item.get("name", ""))
            mime_type = str(item.get("mimeType", ""))
            is_folder = mime_type == FOLDER_MIME_TYPE
            relative_path = _relative_path(parent_path, file_name)
            size = item.get("size")

            records.append(
                {
                    "drive_file_id": item_id,
                    "relative_path": relative_path,
                    "file_name": file_name,
                    "extension": str(item.get("fullFileExtension", "")),
                    "mime_type": mime_type,
                    "is_folder": is_folder,
                    "size_bytes": int(size) if size not in {None, ""} else None,
                    "created_at_utc": item.get("createdTime"),
                    "modified_at_utc": item.get("modifiedTime"),
                    "md5_checksum": item.get("md5Checksum"),
                    "sha1_checksum": item.get("sha1Checksum"),
                    "sha256_checksum": item.get("sha256Checksum"),
                    "parent_drive_file_id": parent_id,
                    "audit_status": "PENDING_AUDIT",
                }
            )

            if is_folder and item_id and item_id not in visited_folders:
                visited_folders.add(item_id)
                queue.append((item_id, relative_path, None))

    return pd.DataFrame(records, columns=INVENTORY_COLUMNS)
