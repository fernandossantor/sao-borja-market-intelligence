from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd
import pytest

from sbmi.ips_web_snapshot import (
    extract_table_ibge_codes,
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
    def __init__(self, page_factory) -> None:
        self.page_factory = page_factory
        self.urls: list[str] = []

    def get(self, url: str, **_kwargs: object) -> FakeResponse:
        self.urls.append(url)
        query = parse_qs(urlparse(url).query)
        year = int(query["year"][0])
        page = int(query["page"][0])
        return FakeResponse(self.page_factory(year, page), url)


def _html(year: int, codes: list[int]) -> bytes:
    rows = []
    for code in codes:
        municipality = "São Borja (RS)" if code == 4318002 else f"Município {code}"
        rows.append(
            f"<tr><td>{code}</td><td>{municipality}</td><td>RS</td>"
            f"<td>{60 + year % 10},50</td></tr>"
        )
    return (
        "<html><body><table>"
        "<tr><th>Código IBGE</th><th>Município</th><th>UF</th>"
        "<th>Índice de Progresso Social</th></tr>"
        + "".join(rows)
        + "</table></body></html>"
    ).encode()


def _monotonic_page(year: int, page: int, *, include_target: bool = True) -> bytes:
    if page < 5:
        codes = [1_000_000 + page * 10 + offset for offset in range(3)]
    elif page > 5:
        codes = [5_000_000 + page * 10 + offset for offset in range(3)]
    elif include_target:
        codes = [4_317_999, 4_318_002, 4_318_003]
    else:
        codes = [4_318_000, 4_318_001, 4_318_003]
    return _html(year, codes)


def test_published_data_url_is_explicit() -> None:
    url = published_data_url(2026, page=499, per_page=10)
    assert "page=499" in url
    assert "per_page=10" in url
    assert "sort_by=code" in url
    assert "year=2026" in url


def test_extracts_only_codes_from_the_municipal_table() -> None:
    html = _html(2026, [4_317_999, 4_318_002, 4_318_003]).decode()
    assert extract_table_ibge_codes(html) == (4_317_999, 4_318_002, 4_318_003)


def test_snapshot_captures_three_verified_pages(tmp_path: Path) -> None:
    contents = {
        year: _html(year, [4_317_999, 4_318_002, 4_318_003])
        for year in (2024, 2025, 2026)
    }
    session = FakeSession(lambda year, _page: contents[year])
    result = snapshot_published_ips_pages(
        tmp_path,
        snapshot_id="ips-test",
        session=session,
    )

    assert result.pages == 3
    assert result.requests == 3
    assert result.bytes == sum(len(content) for content in contents.values())
    assert result.transferred_bytes == result.bytes
    manifest = pd.read_csv(result.snapshot_path / "web_manifest.csv")
    assert list(manifest["reference_year"]) == [2024, 2025, 2026]
    assert list(manifest["page_found"]) == [499, 499, 499]
    assert manifest["ibge_code_present"].all()
    assert all((result.snapshot_path / name).is_file() for name in manifest["local_file"])


def test_snapshot_finds_page_by_binary_search(tmp_path: Path) -> None:
    session = FakeSession(lambda year, page: _monotonic_page(year, page))
    result = snapshot_published_ips_pages(
        tmp_path,
        snapshot_id="ips-test",
        years=(2024,),
        initial_page=9,
        max_page=10,
        session=session,
    )

    assert result.requests == 2
    manifest = pd.read_csv(result.snapshot_path / "web_manifest.csv")
    assert int(manifest.loc[0, "page_found"]) == 5
    assert int(manifest.loc[0, "search_requests"]) == 2


def test_snapshot_refuses_search_without_municipality(tmp_path: Path) -> None:
    session = FakeSession(
        lambda year, page: _monotonic_page(year, page, include_target=False)
    )
    with pytest.raises(ValueError, match="não foi encontrado"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            initial_page=9,
            max_page=10,
            session=session,
        )
    assert not (tmp_path / ".ips-test.partial").exists()
