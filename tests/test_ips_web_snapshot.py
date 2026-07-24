from pathlib import Path

import pandas as pd
import pytest

from sbmi.ips_web_snapshot import (
    published_data_url,
    snapshot_published_ips_pages,
)


class FakeResponse:
    def __init__(self, content: bytes, url: str, status_code: int = 200) -> None:
        self.content = content
        self.url = url
        self.status_code = status_code
        self.headers = {"content-type": "text/html; charset=utf-8"}

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError(f"HTTP {self.status_code}")


class FakeSession:
    def __init__(self, contents: dict[int, bytes]) -> None:
        self.contents = contents

    def get(self, url: str, **_kwargs: object) -> FakeResponse:
        year = int(url.rsplit("year=", 1)[-1])
        return FakeResponse(self.contents[year], url)


def _html(year: int, code: str = "4318002") -> bytes:
    return (
        "<html><body><table>"
        "<tr><th>Código IBGE</th><th>Município</th><th>UF</th>"
        "<th>Índice de Progresso Social</th></tr>"
        f"<tr><td>{code}</td><td>São Borja (RS)</td><td>RS</td>"
        f"<td>{60 + year % 10},50</td></tr>"
        "</table></body></html>"
    ).encode()


def test_published_data_url_is_explicit() -> None:
    url = published_data_url(2026, page=499, per_page=10)
    assert "page=499" in url
    assert "per_page=10" in url
    assert "sort_by=code" in url
    assert "year=2026" in url


def test_snapshot_captures_three_verified_pages(tmp_path: Path) -> None:
    contents = {year: _html(year) for year in (2024, 2025, 2026)}
    result = snapshot_published_ips_pages(
        tmp_path,
        snapshot_id="ips-test",
        session=FakeSession(contents),
    )

    assert result.pages == 3
    assert result.bytes == sum(len(content) for content in contents.values())
    manifest = pd.read_csv(result.snapshot_path / "web_manifest.csv")
    assert list(manifest["reference_year"]) == [2024, 2025, 2026]
    assert manifest["ibge_code_present"].all()
    assert all((result.snapshot_path / name).is_file() for name in manifest["local_file"])


def test_snapshot_refuses_page_without_municipality(tmp_path: Path) -> None:
    contents = {year: _html(year, code="9999999") for year in (2024, 2025, 2026)}
    with pytest.raises(ValueError, match="não foi encontrado"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            session=FakeSession(contents),
        )
    assert not (tmp_path / ".ips-test.partial").exists()
