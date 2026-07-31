import pytest

from sbmi.transparencia_api import (
    fetch_transparencia_api_json,
    transparencia_api_headers,
)


class Response:
    def raise_for_status(self):
        return None

    def json(self):
        return {"ok": True}


class Session:
    def get(self, url, *, params, headers, timeout):
        assert url.startswith("https://api.portaldatransparencia.gov.br/")
        assert params == {"pagina": 1}
        assert headers == {
            "Accept": "application/json",
            "chave-api-dados": "test-key",
        }
        assert timeout == 5
        return Response()


def test_headers_use_explicit_key_without_exposing_it():
    assert transparencia_api_headers(" test-key ") == {
        "Accept": "application/json",
        "chave-api-dados": "test-key",
    }


def test_headers_require_key(monkeypatch):
    monkeypatch.delenv("TRANSPARENCIA_API_KEY", raising=False)
    with pytest.raises(RuntimeError, match="TRANSPARENCIA_API_KEY"):
        transparencia_api_headers()


def test_fetches_relative_endpoint_with_authentication():
    assert fetch_transparencia_api_json(
        "orgaos-siafi",
        params={"pagina": 1},
        timeout=5,
        session=Session(),
        api_key="test-key",
    ) == {"ok": True}


@pytest.mark.parametrize("endpoint", ["https://example.invalid", "http://example.invalid"])
def test_rejects_absolute_endpoint(endpoint):
    with pytest.raises(ValueError, match="relativo"):
        fetch_transparencia_api_json(endpoint, api_key="test-key")
