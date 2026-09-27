import hashlib
from pathlib import Path
from typing import Any

import pytest

import sbmi.drive_staging as drive_staging
from sbmi.drive_staging import stage_drive_file


class FakeDownloadResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def raise_for_status(self) -> None:
        return None

    def iter_content(self, chunk_size: int):  # type: ignore[no-untyped-def]
        assert chunk_size > 0
        yield self.content[:3]
        yield self.content[3:]


class FakeSession:
    def __init__(self, content: bytes) -> None:
        self.content = content
        self.media_calls = 0

    def get(self, url: str, **kwargs: Any) -> FakeDownloadResponse:
        assert url.endswith("/drive-file")
        assert kwargs["params"]["alt"] == "media"
        assert kwargs["stream"] is True
        self.media_calls += 1
        return FakeDownloadResponse(self.content)


def test_stage_drive_file_downloads_validates_and_reuses(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    content = b"sbmi-drive-master"
    sha256 = hashlib.sha256(content).hexdigest()
    metadata = {
        "id": "drive-file",
        "name": "input.bin",
        "mimeType": "application/octet-stream",
        "size": str(len(content)),
        "sha256Checksum": sha256,
    }
    monkeypatch.setattr(drive_staging, "get_file_metadata", lambda session, file_id: metadata)
    session = FakeSession(content)
    target = tmp_path / "input.bin"

    first = stage_drive_file(
        session,  # type: ignore[arg-type]
        file_id="drive-file",
        target=target,
        expected_size=len(content),
        expected_sha256=sha256,
    )
    assert target.read_bytes() == content
    assert first.reused_existing is False
    assert first.sha256 == sha256
    assert session.media_calls == 1

    second = stage_drive_file(
        session,  # type: ignore[arg-type]
        file_id="drive-file",
        target=target,
        expected_size=len(content),
        expected_sha256=sha256,
    )
    assert second.reused_existing is True
    assert session.media_calls == 1


def test_stage_drive_file_rejects_divergent_existing_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    expected = b"expected"
    expected_sha = hashlib.sha256(expected).hexdigest()
    metadata = {
        "id": "drive-file",
        "name": "input.bin",
        "mimeType": "application/octet-stream",
        "size": str(len(expected)),
    }
    monkeypatch.setattr(drive_staging, "get_file_metadata", lambda session, file_id: metadata)
    target = tmp_path / "input.bin"
    target.write_bytes(b"wrong!!!")

    with pytest.raises(ValueError, match="SHA-256 local divergente"):
        stage_drive_file(
            FakeSession(expected),  # type: ignore[arg-type]
            file_id="drive-file",
            target=target,
            expected_size=len(expected),
            expected_sha256=expected_sha,
        )
