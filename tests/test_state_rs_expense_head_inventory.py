import pytest

from sbmi.state_rs_expense_head_inventory import (
    inventory_state_rs_expense_heads,
)


class Response:
    def __init__(
        self,
        *,
        payload=None,
        status_code=200,
        headers=None,
        url="https://dados.rs.gov.br/file.zip",
    ):
        self.payload = payload
        self.status_code = status_code
        self.headers = headers or {}
        self.url = url

    def raise_for_status(self):
        return None

    def json(self):
        return self.payload

    def close(self):
        return None


class Session:
    def __init__(self):
        self.get_calls = 0
        self.head_calls = []

    def get(self, url, params, timeout):
        self.get_calls += 1
        assert params == {"q": "organization:cage", "rows": 100}
        return Response(payload={
            "success": True,
            "result": {
                "results": [
                    {
                        "id": "package",
                        "name": "2026-despesa-do-estado",
                        "title": "2026 - Despesa do Estado",
                        "resources": [
                            {
                                "id": "jan",
                                "name": "Janeiro",
                                "format": "zip/csv",
                                "size": None,
                                "last_modified": None,
                                "url": (
                                    "https://dados.rs.gov.br/resource/"
                                    "despesas-202601.zip"
                                ),
                            },
                            {
                                "id": "feb",
                                "name": "Fevereiro",
                                "format": "zip/csv",
                                "size": None,
                                "last_modified": None,
                                "url": (
                                    "https://dados.rs.gov.br/resource/"
                                    "despesas-202602.zip"
                                ),
                            },
                        ],
                    }
                ]
            },
        })

    def head(self, url, timeout, allow_redirects):
        self.head_calls.append(url)
        assert timeout > 0 and not allow_redirects
        if "/resource/" in url and url.endswith("202601.zip"):
            return Response(
                status_code=302,
                headers={"Location": "/download/202601.zip"},
                url=url,
            )
        size = "100" if "202601" in url else "200"
        return Response(
            headers={
                "Content-Length": size,
                "Content-Type": "application/zip",
            },
            url=url,
        )


def test_inventories_heads_without_getting_bodies(tmp_path):
    session = Session()
    result = inventory_state_rs_expense_heads(
        output_root=tmp_path,
        run_id="run",
        session=session,
        max_workers=2,
    )
    assert session.get_calls == 1
    assert len(session.head_calls) == 3
    assert len(result.inventory) == 2
    assert result.inventory.content_length.sum() == 300
    assert result.inventory.catalog_filename_period_matches.all()
    assert not result.inventory.body_downloaded.any()
    assert result.validation.status.ne("FAIL").all()


def test_refuses_overwrite(tmp_path):
    session = Session()
    kwargs = {
        "output_root": tmp_path,
        "run_id": "run",
        "session": session,
    }
    inventory_state_rs_expense_heads(**kwargs)
    with pytest.raises(FileExistsError):
        inventory_state_rs_expense_heads(**kwargs)


def test_rejects_redirect_outside_allowed_host(tmp_path):
    class UnsafeSession(Session):
        def head(self, url, timeout, allow_redirects):
            return Response(
                status_code=302,
                headers={"Location": "https://example.com/file.zip"},
                url=url,
            )

    result = inventory_state_rs_expense_heads(
        output_root=tmp_path,
        run_id="run",
        session=UnsafeSession(),
    )
    assert result.inventory.head_error.str.contains("não autorizado").all()
    assert not result.inventory.body_downloaded.any()
