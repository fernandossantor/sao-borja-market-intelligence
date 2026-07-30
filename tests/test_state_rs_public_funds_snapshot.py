import io
import zipfile

import pytest

from sbmi.state_rs_public_funds_snapshot import (
    RESOURCES,
    snapshot_state_rs_public_funds,
)


def _zip_bytes(value: str = "example") -> bytes:
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        archive.writestr("dados.csv", f"resource;valor\n{value};1\n")
    return output.getvalue()


class Response:
    url = "https://dados.rs.gov.br/final.zip"
    status_code = 200
    headers = {"Content-Type": "application/zip"}

    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self):
        return None

    def iter_content(self, chunk_size):
        yield self.payload


class Session:
    def get(self, url, timeout, stream):
        assert timeout > 0 and stream
        assert url.startswith("https://dados.rs.gov.br/")
        return Response(_zip_bytes(url))


def test_snapshot_is_immutable_and_does_not_extract(tmp_path):
    result = snapshot_state_rs_public_funds(
        snapshot_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        run_id="run",
        session=Session(),
    )
    assert len(result.manifest) == len(RESOURCES)
    assert len(result.archive_inventory) == len(RESOURCES)
    assert not result.archive_inventory.extracted.any()
    assert not result.manifest.personal_data_inspected.any()
    assert result.validation.status.eq("PASS").all()


def test_refuses_overwrite(tmp_path):
    kwargs = {
        "snapshot_root": tmp_path / "snapshots",
        "audit_root": tmp_path / "audit",
        "run_id": "run",
        "session": Session(),
    }
    snapshot_state_rs_public_funds(**kwargs)
    with pytest.raises(FileExistsError):
        snapshot_state_rs_public_funds(**kwargs)


def test_enforces_total_limit(tmp_path):
    with pytest.raises(ValueError, match="Limite"):
        snapshot_state_rs_public_funds(
            snapshot_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            run_id="run",
            session=Session(),
            total_limit=10,
        )
