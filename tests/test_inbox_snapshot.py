import hashlib
from pathlib import Path
from typing import Any

import pandas as pd

from sbmi.inbox_snapshot import planned_bytes, select_inbox_files, snapshot_inbox


class FakeResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def raise_for_status(self) -> None:
        return None

    def iter_content(self, chunk_size: int) -> list[bytes]:
        return [
            self.content[index : index + chunk_size]
            for index in range(0, len(self.content), chunk_size)
        ]


class FakeSession:
    def __init__(self, files: dict[str, bytes]) -> None:
        self.files = files

    def get(
        self,
        url: str,
        params: dict[str, Any],
        stream: bool,
        timeout: int,
    ) -> FakeResponse:
        assert params == {"alt": "media", "supportsAllDrives": "true"}
        assert stream is True
        assert timeout == 120
        file_id = url.rsplit("/", maxsplit=1)[-1]
        return FakeResponse(self.files[file_id])


def inventory_frame() -> pd.DataFrame:
    content_a = b"arquivo-a"
    content_b = b"arquivo-b"
    return pd.DataFrame(
        [
            {
                "drive_file_id": "file-a",
                "relative_path": "raw/new_files/Federal/a.xlsx",
                "is_folder": False,
                "size_bytes": len(content_a),
                "sha256_checksum": hashlib.sha256(content_a).hexdigest(),
            },
            {
                "drive_file_id": "file-b",
                "relative_path": "raw/new_files/Municipal/b.xlsx",
                "is_folder": "False",
                "size_bytes": len(content_b),
                "sha256_checksum": hashlib.sha256(content_b).hexdigest(),
            },
            {
                "drive_file_id": "folder",
                "relative_path": "raw/new_files/Municipal",
                "is_folder": True,
                "size_bytes": None,
                "sha256_checksum": None,
            },
            {
                "drive_file_id": "outside",
                "relative_path": "raw/fiscal/outside.xlsx",
                "is_folder": False,
                "size_bytes": 100,
                "sha256_checksum": "outside-hash",
            },
        ]
    )


def test_select_inbox_files_and_planned_bytes() -> None:
    selected = select_inbox_files(inventory_frame())

    assert selected["drive_file_id"].tolist() == ["file-a", "file-b"]
    assert planned_bytes(selected) == len(b"arquivo-a") + len(b"arquivo-b")


def test_snapshot_inbox_downloads_and_verifies_files(tmp_path: Path) -> None:
    files = {"file-a": b"arquivo-a", "file-b": b"arquivo-b"}
    result = snapshot_inbox(
        session=FakeSession(files),  # type: ignore[arg-type]
        inventory=inventory_frame(),
        snapshots_root=tmp_path,
        snapshot_id="snapshot-001",
        max_total_bytes=1_000,
    )

    assert result.files == 2
    assert result.bytes == len(b"arquivo-a") + len(b"arquivo-b")
    assert (result.snapshot_path / "raw/new_files/Federal/a.xlsx").read_bytes() == b"arquivo-a"
    assert (result.snapshot_path / "raw/new_files/Municipal/b.xlsx").read_bytes() == b"arquivo-b"

    manifest = pd.read_csv(result.snapshot_path / "snapshot_manifest.csv")
    assert set(manifest["verification_status"]) == {"VERIFIED"}
    assert manifest["expected_sha256"].equals(manifest["local_sha256"])


def test_snapshot_inbox_blocks_volume_above_limit(tmp_path: Path) -> None:
    try:
        snapshot_inbox(
            session=FakeSession({}),  # type: ignore[arg-type]
            inventory=inventory_frame(),
            snapshots_root=tmp_path,
            snapshot_id="snapshot-002",
            max_total_bytes=1,
        )
    except ValueError as exc:
        assert "Captura bloqueada pelo limite" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError")


def test_snapshot_inbox_rejects_checksum_mismatch_and_cleans_partial(
    tmp_path: Path,
) -> None:
    files = {"file-a": b"conteudo-divergente", "file-b": b"arquivo-b"}

    try:
        snapshot_inbox(
            session=FakeSession(files),  # type: ignore[arg-type]
            inventory=inventory_frame(),
            snapshots_root=tmp_path,
            snapshot_id="snapshot-003",
            max_total_bytes=1_000,
        )
    except ValueError as exc:
        assert "divergente" in str(exc)
    else:
        raise AssertionError("Era esperado ValueError")

    assert not (tmp_path / "snapshot-003").exists()
    assert not (tmp_path / ".snapshot-003.partial").exists()
