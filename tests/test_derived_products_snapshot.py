import hashlib
from pathlib import Path

import pandas as pd
import pytest

from sbmi.derived_products_snapshot import (
    select_derived_files,
    snapshot_derived_products,
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


def _inventory(payloads: dict[str, bytes]) -> pd.DataFrame:
    rows = []
    for file_id, (path, content) in enumerate(payloads.items(), start=1):
        rows.append(
            {
                "drive_file_id": str(file_id),
                "relative_path": path,
                "is_folder": False,
                "size_bytes": len(content),
                "sha256_checksum": hashlib.sha256(content).hexdigest(),
            }
        )
    rows.append(
        {
            "drive_file_id": "folder",
            "relative_path": "processed/agro",
            "is_folder": True,
            "size_bytes": None,
            "sha256_checksum": "",
        }
    )
    return pd.DataFrame(rows)


def test_selects_only_requested_derived_scopes() -> None:
    payloads = {
        "processed/agro/a.parquet": b"a",
        "exports/a.csv": b"b",
        "warehouse/a.duckdb": b"c",
        "raw/source.xlsx": b"d",
    }
    selected = select_derived_files(_inventory(payloads))
    assert list(selected["relative_path"]) == [
        "exports/a.csv",
        "processed/agro/a.parquet",
        "warehouse/a.duckdb",
    ]


def test_snapshot_downloads_and_verifies_all_scopes(tmp_path: Path) -> None:
    paths = {
        "processed/agro/a.parquet": b"alpha",
        "exports/a.csv": b"beta",
        "warehouse/a.duckdb": b"gamma",
    }
    inventory = _inventory(paths)
    session_payloads = {
        str(index): content
        for index, content in enumerate(paths.values(), start=1)
    }
    result = snapshot_derived_products(
        session=FakeSession(session_payloads),
        inventory=inventory,
        snapshots_root=tmp_path,
        snapshot_id="derived-test",
        max_total_bytes=100,
    )

    assert result.files == 3
    assert result.bytes == sum(len(value) for value in paths.values())
    manifest = pd.read_csv(result.snapshot_path / "snapshot_manifest.csv")
    assert set(manifest["verification_status"]) == {"VERIFIED"}
    for relative_path, content in paths.items():
        assert (result.snapshot_path / relative_path).read_bytes() == content


def test_snapshot_blocks_volume_over_limit(tmp_path: Path) -> None:
    inventory = _inventory({"processed/a.parquet": b"12345"})
    with pytest.raises(ValueError, match="Captura bloqueada"):
        snapshot_derived_products(
            session=FakeSession({"1": b"12345"}),
            inventory=inventory,
            snapshots_root=tmp_path,
            snapshot_id="derived-test",
            max_total_bytes=4,
        )
