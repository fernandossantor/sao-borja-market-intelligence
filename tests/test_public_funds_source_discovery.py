
import pytest

from sbmi.public_funds_source_discovery import (
    SOURCES,
    discover_public_funds_sources,
)


class Response:
    content = b"<html>metadata only</html>"
    url = "https://example.invalid/final"
    status_code = 200
    headers = {"Content-Type": "text/html; charset=utf-8"}


class Session:
    def get(self, url, timeout):
        assert timeout > 0
        assert url.startswith("https://")
        return Response()


def test_captures_metadata_with_required_tags_and_no_personal_data(tmp_path):
    result = discover_public_funds_sources(
        snapshot_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        run_id="run",
        session=Session(),
    )
    assert len(result.inventory) == len(SOURCES)
    assert result.inventory.dimension.eq(
        "financas_publicas_transferencias"
    ).all()
    assert not result.inventory.personal_data_captured.any()
    assert result.inventory.integration_status.eq("NOT_INTEGRATED").all()
    assert result.validation.status.eq("PASS").all()


def test_refuses_overwrite(tmp_path):
    kwargs = {
        "snapshot_root": tmp_path / "snapshots",
        "audit_root": tmp_path / "audit",
        "run_id": "run",
        "session": Session(),
    }
    discover_public_funds_sources(**kwargs)
    with pytest.raises(FileExistsError):
        discover_public_funds_sources(**kwargs)


def test_rejects_oversized_response(tmp_path):
    with pytest.raises(ValueError, match="excede limite"):
        discover_public_funds_sources(
            snapshot_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            run_id="run",
            response_limit=5,
            session=Session(),
        )
