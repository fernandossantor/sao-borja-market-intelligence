from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pandas as pd
import pytest

from sbmi.ips_web_snapshot import (
    SUMMARY_LABELS,
    RenderedScorecard,
    scorecard_diagnostics,
    scorecard_url,
    snapshot_published_ips_pages,
    validate_rendered_scorecard,
)


class FakeRenderer:
    def __init__(self, pages: dict[int, RenderedScorecard]) -> None:
        self.pages = pages
        self.urls: list[str] = []
        self.closed = False

    def render(
        self,
        url: str,
        *,
        year: int,
        ibge_code: str,
        municipality: str,
        timeout_seconds: int,
    ) -> RenderedScorecard:
        del ibge_code, municipality, timeout_seconds
        self.urls.append(url)
        observed_year = int(parse_qs(urlparse(url).query)["year"][0])
        assert observed_year == year
        return self.pages[year]

    def close(self) -> None:
        self.closed = True


def _rendered(
    year: int,
    *,
    municipality: str = "São Borja",
    include_scores: bool = True,
) -> RenderedScorecard:
    index_score = "62,40" if include_scores else ""
    sections = " ".join(
        f"{label} {61 + position},{position % 10}"
        if include_scores
        else label
        for position, label in enumerate(SUMMARY_LABELS, start=1)
    )
    text = f"{municipality} IPS BRASIL {year} {index_score} {sections}"
    html = (
        "<html><body>"
        f"<a href='/explore/scorecard/4318002?year={year}'>fonte</a>"
        f"<main>{text}</main></body></html>"
    )
    return RenderedScorecard(
        html=html,
        text=text,
        final_url=f"https://example.test/scorecard/4318002?year={year}",
        status_code=200,
    )


def test_scorecard_url_is_explicit() -> None:
    url = scorecard_url(2026, ibge_code="4318002")
    assert "/explore/scorecard/4318002" in url
    assert "year=2026" in url


def test_diagnostics_require_rendered_scores() -> None:
    incomplete = scorecard_diagnostics(
        _rendered(2026, include_scores=False).text,
        year=2026,
        municipality="São Borja",
    )
    complete = scorecard_diagnostics(
        _rendered(2026).text,
        year=2026,
        municipality="São Borja",
    )

    assert incomplete.labels_present == 15
    assert incomplete.labels_with_score == 0
    assert incomplete.ready is False
    assert complete.labels_with_score == 15
    assert complete.score_candidates >= 16
    assert complete.ready is True


def test_validates_rendered_contract() -> None:
    diagnostics = validate_rendered_scorecard(
        _rendered(2026),
        year=2026,
        ibge_code="4318002",
        municipality="São Borja",
    )
    assert diagnostics.labels_present == 15
    assert diagnostics.labels_with_score == 15


def test_snapshot_captures_three_rendered_scorecards(tmp_path: Path) -> None:
    renderer = FakeRenderer({year: _rendered(year) for year in (2024, 2025, 2026)})
    result = snapshot_published_ips_pages(
        tmp_path,
        snapshot_id="ips-test",
        renderer=renderer,
    )

    assert result.pages == 3
    assert result.browser_navigations == 3
    assert result.stored_bytes > 0
    assert renderer.closed is False
    manifest = pd.read_csv(result.snapshot_path / "web_manifest.csv")
    assert list(manifest["reference_year"]) == [2024, 2025, 2026]
    assert set(manifest["capture_mode"]) == {"PLAYWRIGHT_RENDERED_LIVEVIEW_DOM"}
    assert set(manifest["summary_labels_with_score"]) == {15}
    assert all(
        (result.snapshot_path / filename).is_file()
        for filename in manifest["local_html_file"]
    )
    assert all(
        (result.snapshot_path / filename).is_file()
        for filename in manifest["local_text_file"]
    )


def test_snapshot_refuses_wrong_edition(tmp_path: Path) -> None:
    renderer = FakeRenderer({2024: _rendered(2025)})
    with pytest.raises(ValueError, match="contrato numérico completo"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            renderer=renderer,
        )
    assert not (tmp_path / ".ips-test.partial").exists()


def test_snapshot_refuses_static_structure_without_scores(tmp_path: Path) -> None:
    renderer = FakeRenderer({2024: _rendered(2024, include_scores=False)})
    with pytest.raises(ValueError, match="contrato numérico completo"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            renderer=renderer,
        )
    assert not (tmp_path / ".ips-test.partial").exists()


def test_snapshot_refuses_missing_municipality(tmp_path: Path) -> None:
    renderer = FakeRenderer({2024: _rendered(2024, municipality="Outro Município")})
    with pytest.raises(ValueError, match="contrato numérico completo"):
        snapshot_published_ips_pages(
            tmp_path,
            snapshot_id="ips-test",
            years=(2024,),
            renderer=renderer,
        )
    assert not (tmp_path / ".ips-test.partial").exists()
