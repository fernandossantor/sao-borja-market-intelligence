import io
import json
import zipfile
from pathlib import Path

import pytest

from sbmi.economy_gdp_series import collect_economy_gdp_series


class Response:
    status_code = 200

    def __init__(self, url, content):
        self.url, self.content = url, content
        self.headers = {
            "Content-Type": "application/zip" if "ftp.ibge" in url else "application/json"
        }

    def raise_for_status(self):
        pass


def old_zip():
    lines = []
    for year in (1999, 2000, 2001):
        line = list(" " * 340)
        line[0:4], line[34:41] = str(year), "4318002"
        spans = ((223, 241), (242, 260), (261, 279), (280, 298), (299, 317), (318, 336))
        for (start, end), value in zip(spans, (10, 20, 30, 5, 4, 64), strict=True):
            line[start:end] = f"{value:18.2f}"
        lines.append("".join(line))
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        archive.writestr("base.txt", "\n".join(lines).encode("latin-1"))
    return buffer.getvalue()


def sidra_payload():
    header = {key: key for key in ("NC", "MC", "MN", "V", "D1C", "D2C", "D3C")}
    variables = {
        "37": 64,
        "543": 4,
        "498": 60,
        "513": 10,
        "516": 16.666667,
        "517": 20,
        "520": 33.333333,
        "6575": 25,
        "6574": 41.666667,
        "525": 5,
        "528": 8.333333,
    }
    rows = [
        {"NC": "6", "D1C": "4318002", "D2C": str(year), "D3C": variable, "V": str(value)}
        for year in range(2002, 2022)
        for variable, value in variables.items()
    ]
    return json.dumps([header, *rows]).encode()


class Session:
    def get(self, url, **_kwargs):
        return Response(url, old_zip() if "ftp.ibge" in url else sidra_payload())


def roots(tmp_path):
    return {layer: tmp_path / layer for layer in ("raw", "staging", "curated", "exports", "audit")}


def test_collects_validates_and_refuses_overwrite(tmp_path: Path):
    kwargs = {
        "session": Session(),
        "old_url": "https://ftp.ibge.gov.br/a.zip",
        "sidra_url": "https://apisidra.ibge.gov.br/values/t/5938",
        "roots": roots(tmp_path),
        "execution_id": "run",
    }
    result = collect_economy_gdp_series(**kwargs)
    assert set(result.values.methodology_series) == {"old_1999_2001", "current_2002_onward"}
    assert set(result.validation.status) <= {"PASS", "INFORMATIONAL"}
    with pytest.raises(FileExistsError):
        collect_economy_gdp_series(**kwargs)


def test_rejects_external_host(tmp_path: Path):
    with pytest.raises(ValueError, match="domínio"):
        collect_economy_gdp_series(
            Session(),
            old_url="https://example.com/a.zip",
            sidra_url="https://apisidra.ibge.gov.br/values/t/5938",
            roots=roots(tmp_path),
            execution_id="run",
        )


class UnexpectedResponseSession(Session):
    def __init__(self, *, content_type=None, final_url=None):
        self.content_type = content_type
        self.final_url = final_url

    def get(self, url, **kwargs):
        response = super().get(url, **kwargs)
        if self.content_type:
            response.headers["Content-Type"] = self.content_type
        if self.final_url:
            response.url = self.final_url
        return response


@pytest.mark.parametrize(
    ("session", "message"),
    [
        (UnexpectedResponseSession(content_type="text/html"), "Tipo de conteúdo"),
        (
            UnexpectedResponseSession(final_url="http://ftp.ibge.gov.br/a.zip"),
            "Redirecionamento",
        ),
    ],
)
def test_rejects_unexpected_response(tmp_path, session, message):
    with pytest.raises(ValueError, match=message):
        collect_economy_gdp_series(
            session,
            old_url="https://ftp.ibge.gov.br/a.zip",
            sidra_url="https://apisidra.ibge.gov.br/values/t/5938",
            roots=roots(tmp_path),
            execution_id="run",
        )
