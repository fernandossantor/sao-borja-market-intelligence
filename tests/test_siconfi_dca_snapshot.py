"""Testes da captura oficial DCA/SICONFI."""

import json

import pandas as pd
import pytest

from sbmi.siconfi_dca_snapshot import snapshot_siconfi_dca


class FakeResponse:
    def __init__(self, payload: dict, *, content_type: str = "application/json") -> None:
        self.content = json.dumps(payload).encode()
        self.headers = {"Content-Type": content_type}
        self.url = "https://apidatalake.tesouro.gov.br/ords/siconfi/tt/dca"

    def raise_for_status(self) -> None:
        return None


class FakeSession:
    def get(self, _url: str, **kwargs) -> FakeResponse:
        year = kwargs["params"]["an_exercicio"]
        return FakeResponse(
            {
                "items": [{"exercicio": year, "cod_ibge": 4318002}],
                "hasMore": False,
            }
        )


def test_snapshot_is_atomic_and_refuses_collision(tmp_path) -> None:
    result = snapshot_siconfi_dca(FakeSession(), tmp_path, snapshot_id="run", years=(2021, 2022))
    assert result.files == 2
    assert result.rows == 2
    manifest = pd.read_csv(result.snapshot_path / "manifest.csv")
    assert list(manifest["reference_year"]) == [2021, 2022]
    assert set(manifest["audit_status"]) == {"VERIFIED"}
    with pytest.raises(FileExistsError):
        snapshot_siconfi_dca(FakeSession(), tmp_path, snapshot_id="run", years=(2022,))


class InvalidResponseSession(FakeSession):
    def __init__(self, *, content_type="application/json", url=None) -> None:
        self.content_type = content_type
        self.url = url

    def get(self, _url: str, **kwargs) -> FakeResponse:
        response = super().get(_url, **kwargs)
        response.headers = {"Content-Type": self.content_type}
        if self.url:
            response.url = self.url
        return response


@pytest.mark.parametrize(
    ("session", "message"),
    [
        (InvalidResponseSession(content_type="text/html"), "Tipo de conteúdo"),
        (InvalidResponseSession(url="https://example.com/dca"), "URL final"),
        (
            InvalidResponseSession(
                url="https://apidatalake.tesouro.gov.br/ords/siconfi/tt/outro"
            ),
            "URL final",
        ),
    ],
)
def test_rejects_unexpected_http_response(tmp_path, session, message) -> None:
    with pytest.raises(ValueError, match=message):
        snapshot_siconfi_dca(session, tmp_path, snapshot_id="run", years=(2021,))
    assert not (tmp_path / "run").exists()
    assert not (tmp_path / ".run.partial").exists()
