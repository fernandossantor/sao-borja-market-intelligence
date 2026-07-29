import pytest

from sbmi.state_rs_catalog_discovery import (
    REPORT_ID,
    discover_state_rs_catalog,
)


class Response:
    def __init__(self, *, text="", payload=None):
        self.text = text
        self.payload = payload

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload


class Session:
    def post(self, url, data, timeout):
        assert timeout > 0
        if "AtualizacaoPainel" in url:
            return Response(text="2026-07-29")
        assert set(data) == {"workspaceId", "reportId"}
        return Response(payload={
            "Id": REPORT_ID,
            "EmbedUrl": "https://app.powerbi.com/reportEmbed",
            "Token": "must-not-be-stored",
        })


def test_records_only_sanitized_catalog_metadata(tmp_path):
    result = discover_state_rs_catalog(
        output_root=tmp_path,
        run_id="run",
        session=Session(),
    )
    row = result.metadata.iloc[0]
    assert row.token_was_present_and_discarded
    assert not row.token_stored
    assert row.data_rows_captured == 0
    assert "Token" not in result.metadata.columns
    assert result.validation.status.eq("PASS").all()


def test_refuses_overwrite(tmp_path):
    kwargs = {"output_root": tmp_path, "run_id": "run", "session": Session()}
    discover_state_rs_catalog(**kwargs)
    with pytest.raises(FileExistsError):
        discover_state_rs_catalog(**kwargs)
