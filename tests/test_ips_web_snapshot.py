from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd
import pytest

from sbmi.ips_web_snapshot import (
    SUMMARY_LABELS,
    scorecard_url,
    snapshot_published_ips_pages,
    validate_scorecard_html,
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
        self.urls: list[str] = []

    def get(self, url: str, **_kwargs: object) -> FakeResponse:
        self.urls.append(url)
        year = int(parse_qs(urlparse(url).query)["year"][0])
        return FakeResponse(self.contents[year], url)


def _html(year: int, *, municipality: str = "São Borja") -> bytes:
    sections = "".join(
        f"<section><h2>{label}</h2><div class='score'>61,25</div></section>"
        for label in SUMMARY_LABELS
    )
    return (
        "<html><body>"
        f"<a href='/explore/scorecard/4318002?year={year}'>fonte</a>"
        f"<h1>{municipality}</h1><div>IPS BRASIL {year}</div>"
        "<strong>62,40 / 100</strong>"
        f"{sections}</body></html>"
    ).encode()


def test_scorecard_url_is_explicit() -> None:
    url = scorecard_url(2026, ibge_code="4318002")
    assert "/explore/scorecard/4318002" in url
    assert "year=2026" in url


def test_validates_year_municipality_and_aggregates() -> None:
    source = _html(2026).decode()
    labels = validate_scorecard_html(
        source,
        year=2026,
        ibge_code="4318002",
        municipality="São Borja",
    )
    assert labels == 15


def test_snapshot_captures_three_verified_scorecards(tmp_path: Path) -> None:
    contents = {year: _html(year) for year in (2024, 2025, 2026)}
    result = snapshot_published_ips_pages(
        tmp_path,
        snapshot_id="ips-test",
        session=FakeSession(contents),
    )

    assert result.pages == 3
    assert result.requests == 3
    assert result.bytes == sum(len(content) for content in contents.values())
    assert result.transferred_bytes == result.bytes
    manifest = pd.read_csv(result.snapshot_path / "web_manifest.csv")
    assert list(manifest["reference_year"]) == [2024, 2025, 2026]
    assert set(manifest["summary_labels_observed"]) == {15}
    assert manifest["year_marker_confirmed"].all()
    assert all((result.snapshot_path / name).is_file() for name in manifest["local_file"])


def test_snapshot_refuses_wrong_edition(tmp_path: Path) -> None:
    contents = {2024: _html(2025)}
    with pytest.raises(ValueError, match="não foi confirmada"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            session=FakeSession(contents),
        )
    assert not (tmp_path / ".ips-test.partial").exists()


def test_snapshot_refuses_missing_municipality(tmp_path: Path) -> None:
    contents = {2024: _html(2024, municipality="Outro Município")}
    with pytest.raises(ValueError, match="Município ausente"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            session=FakeSession(contents),
        )
    assert not (tmp_path / ".ips-test.partial").exists()
