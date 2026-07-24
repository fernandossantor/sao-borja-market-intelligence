import hashlib
from pathlib import Path

import pandas as pd
import pytest

from sbmi.source_snapshot import (
    select_exact_source_files,
    snapshot_source_files,
)


class FakeResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def raise_for_status(self) -> None:
        return None

    def iter_content(self, chunk_size: int):
        for index in range(0, len(self.content), chunk_size):
            yield self.content[index : index + chunk_size]


class FakeSession:
    def __init__(self, payloads: dict[str, bytes]) -> None:
        self.payloads = payloads

    def get(self, url: str, **_kwargs):
        file_id = url.rsplit("/", 1)[-1]
        return FakeResponse(self.payloads[file_id])


def _inventory(path: str, content: bytes) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "drive_file_id": "file-1",
                "relative_path": path,
                "is_folder": False,
                "size_bytes": len(content),
                "sha256_checksum": hashlib.sha256(content).hexdigest(),
            },
            {
                "drive_file_id": "folder-1",
                "relative_path": "raw/social",
                "is_folder": True,
                "size_bytes": None,
                "sha256_checksum": "",
            },
        ]
    )


def test_selects_exact_requested_source() -> None:
    path = "raw/social/source.xlsx"
    selected = select_exact_source_files(_inventory(path, b"abc"), [path])
    assert list(selected["relative_path"]) == [path]


def test_rejects_missing_requested_source() -> None:
    with pytest.raises(ValueError, match="Fontes não encontradas"):
        select_exact_source_files(
            _inventory("raw/social/source.xlsx", b"abc"),
            ["raw/social/missing.xlsx"],
        )


def test_snapshot_downloads_and_verifies_source(tmp_path: Path) -> None:
    path = "raw/social/source.xlsx"
    content = b"source-content"
    result = snapshot_source_files(
        session=FakeSession({"file-1": content}),
        inventory=_inventory(path, content),
        snapshots_root=tmp_path,
        relative_paths=(path,),
        snapshot_id="source-test",
        max_total_bytes=100,
    )

    assert result.files == 1
    assert result.bytes == len(content)
    assert (result.snapshot_path / path).read_bytes() == content
    manifest = pd.read_csv(result.snapshot_path / "source_manifest.csv")
    assert manifest.loc[0, "verification_status"] == "VERIFIED"
