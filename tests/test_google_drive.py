import base64
import json
from typing import Any

from sbmi.google_drive import (
    FOLDER_MIME_TYPE,
    build_drive_inventory,
    decode_service_account_info,
)


def service_account_payload() -> dict[str, str]:
    return {
        "type": "service_account",
        "project_id": "sbmi-test",
        "private_key_id": "key-id",
        "private_key": "-----BEGIN PRIVATE KEY-----\ntest\n-----END PRIVATE KEY-----\n",
        "client_email": "reader@sbmi-test.iam.gserviceaccount.com",
        "client_id": "123456789",
        "token_uri": "https://oauth2.googleapis.com/token",
    }


def encode_payload(payload: object) -> str:
    raw = json.dumps(payload).encode("utf-8")
    return base64.b64encode(raw).decode("ascii")


def test_decode_service_account_info() -> None:
    payload = service_account_payload()
    decoded = decode_service_account_info(encode_payload(payload))
    assert decoded["client_email"] == payload["client_email"]
    assert decoded["type"] == "service_account"


def test_decode_service_account_rejects_invalid_payload() -> None:
    try:
        decode_service_account_info("não-é-base64")
    except ValueError as exc:
        assert "Base64 válido" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError")


def test_decode_service_account_requires_expected_fields() -> None:
    try:
        decode_service_account_info(encode_payload({"type": "service_account"}))
    except ValueError as exc:
        assert "Campos obrigatórios ausentes" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError")


class FakeResponse:
    def __init__(self, payload: dict[str, Any]) -> None:
        self.payload = payload

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return self.payload


class FakeSession:
    def get(
        self,
        url: str,
        params: dict[str, Any],
        timeout: int,
    ) -> FakeResponse:
        assert timeout == 60

        if url.endswith("/root-folder"):
            return FakeResponse(
                {
                    "id": "root-folder",
                    "name": "_sao_borja",
                    "mimeType": FOLDER_MIME_TYPE,
                }
            )

        query = str(params.get("q", ""))
        page_token = params.get("pageToken")

        if "'root-folder' in parents" in query and page_token is None:
            return FakeResponse(
                {
                    "files": [
                        {
                            "id": "raw-folder",
                            "name": "raw",
                            "mimeType": FOLDER_MIME_TYPE,
                            "createdTime": "2026-01-01T00:00:00Z",
                            "modifiedTime": "2026-07-01T00:00:00Z",
                            "parents": ["root-folder"],
                        }
                    ],
                    "nextPageToken": "page-2",
                }
            )

        if "'root-folder' in parents" in query and page_token == "page-2":
            return FakeResponse(
                {
                    "files": [
                        {
                            "id": "root-file",
                            "name": "readme.txt",
                            "mimeType": "text/plain",
                            "size": "10",
                            "fullFileExtension": "txt",
                            "sha256Checksum": "abc",
                            "parents": ["root-folder"],
                        }
                    ]
                }
            )

        if "'raw-folder' in parents" in query:
            return FakeResponse(
                {
                    "files": [
                        {
                            "id": "nested-file",
                            "name": "dados.xlsx",
                            "mimeType": (
                                "application/vnd.openxmlformats-officedocument."
                                "spreadsheetml.sheet"
                            ),
                            "size": "25",
                            "fullFileExtension": "xlsx",
                            "md5Checksum": "md5",
                            "sha1Checksum": "sha1",
                            "sha256Checksum": "sha256",
                            "parents": ["raw-folder"],
                        }
                    ]
                }
            )

        raise AssertionError(f"Chamada não esperada: {url} {params}")


def test_build_drive_inventory_is_recursive_and_paginated() -> None:
    inventory = build_drive_inventory(FakeSession(), "root-folder")  # type: ignore[arg-type]

    assert len(inventory) == 3
    assert inventory["relative_path"].tolist() == [
        "raw",
        "readme.txt",
        "raw/dados.xlsx",
    ]
    assert inventory.loc[inventory["drive_file_id"] == "nested-file", "size_bytes"].item() == 25
    assert inventory.loc[
        inventory["drive_file_id"] == "nested-file", "sha256_checksum"
    ].item() == "sha256"
    assert set(inventory["audit_status"]) == {"PENDING_AUDIT"}
