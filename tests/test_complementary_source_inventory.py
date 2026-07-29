import hashlib

import pytest

from sbmi.complementary_source_inventory import (
    PAGE_SPECS,
    build_complementary_source_inventory,
)


class Response:
    status_code = 200
    headers = {"Content-Type": "text/html; charset=utf-8"}

    def __init__(self, url, content):
        self.url = url
        self.content = content

    def raise_for_status(self):
        pass


class Session:
    def __init__(self):
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(url)
        content = b"<html>official page</html>"
        if "observatorio" in url:
            content = (
                b'<script>"https://apiv2-observatorio.sebrae.com.br/tesseract/'
                b'data.jsonrecords?cube=RAIS_workers\\u0026drilldowns=Year'
                b'\\u0026measures=Workers\\u0026Municipality=4318002"</script>'
                b'<script>"https://apiv2-observatorio.sebrae.com.br/tesseract/'
                b'data.jsonrecords?cube=IBGE\\u0026drilldowns=Year'
                b'\\u0026measures=Population\\u0026Municipality=4318002"</script>'
            )
        return Response(url, content)


def _run(tmp_path, session=None):
    return build_complementary_source_inventory(
        session or Session(),
        snapshot_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        execution_id="execution",
    )


def test_captures_pages_but_does_not_execute_candidate_queries(tmp_path):
    session = Session()
    result = _run(tmp_path, session)
    assert session.calls == [spec[0] for spec in PAGE_SPECS.values()]
    assert len(result.queries) == 2
    assert set(result.queries.execution_status) == {"PREPARED_NOT_EXECUTED"}
    assert set(result.queries.dimension) == {
        "demografia", "renda_emprego_trabalho",
    }
    assert set(result.queries.primary_source_declared) == {
        "IBGE", "Ministério do Trabalho/RAIS",
    }
    assert not any("apiv2-observatorio" in call for call in session.calls)


def test_preserves_page_hashes_and_refuses_overwrite(tmp_path):
    result = _run(tmp_path)
    for row in result.pages.itertuples(index=False):
        path = result.snapshot_path / row.local_file
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row.sha256
    with pytest.raises(FileExistsError):
        _run(tmp_path)


def test_rejects_unsafe_execution_id_before_access(tmp_path):
    session = Session()
    with pytest.raises(ValueError, match="nome simples"):
        build_complementary_source_inventory(
            session,
            snapshot_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            execution_id="../unsafe",
        )
    assert session.calls == []
