import hashlib
from pathlib import Path

import pytest

from sbmi.demography_census_official_discovery import (
    HOUSEHOLD_COMPOSITION_URL,
    POPULATION_HOUSEHOLDS_URL,
    discover_official_census_products,
)


class FakeResponse:
    def __init__(
        self,
        content: bytes,
        *,
        url: str,
        content_type: str = "text/html; charset=utf-8",
        status_code: int = 200,
        challenge: bool = False,
    ) -> None:
        self.content = content
        self.url = url
        self.status_code = status_code
        self.headers = {"Content-Type": content_type}
        if challenge:
            self.headers["cf-mitigated"] = "challenge"


class FakeSession:
    def __init__(self, pages: dict[str, bytes]) -> None:
        self.pages = pages
        self.calls: list[str] = []

    def get(self, url: str, **_: object) -> FakeResponse:
        self.calls.append(url)
        return FakeResponse(self.pages[url], url=url)


def _pages() -> dict[str, bytes]:
    return {
        HOUSEHOLD_COMPOSITION_URL: b"""
            <html><a href='https://sidra.ibge.gov.br/tabela/1'>Tabela SIDRA</a>
            <a href='https://example.org/file.xlsx'>Externo</a></html>
        """,
        POPULATION_HOUSEHOLDS_URL: b"""
            <html><a href='/downloads/resultados.zip'>Download</a>
            <a href='https://www.ibge.gov.br/publicacao'>Publicacao</a></html>
        """,
    }


def _run(tmp_path: Path, session: FakeSession | None = None):
    return discover_official_census_products(
        session or FakeSession(_pages()),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="discovery-test",
        run_id="audit-test",
    )


def test_captures_exact_two_pages_and_hashes(tmp_path: Path) -> None:
    session = FakeSession(_pages())
    result = _run(tmp_path, session)

    assert session.calls == [HOUSEHOLD_COMPOSITION_URL, POPULATION_HOUSEHOLDS_URL]
    assert len(result.pages) == 2
    for row in result.pages.itertuples(index=False):
        content = (result.snapshot_path / row.local_file).read_bytes()
        assert row.sha256 == hashlib.sha256(content).hexdigest()
    assert (result.snapshot_path / "official_product_page_manifest.csv").is_file()


def test_registers_candidates_without_claiming_equivalence(tmp_path: Path) -> None:
    result = _run(tmp_path)

    assert set(result.candidates["candidate_kind"]) == {
        "DIRECT_FILE_LINK",
        "SIDRA_LINK",
    }
    assert set(result.candidates["conceptual_equivalence_status"]) == {"NOT_ASSESSED"}
    external = result.links[result.links["domain"].eq("example.org")].iloc[0]
    assert not bool(external["is_official_ibge_domain"])
    assert external["candidate_kind"] == "NON_OFFICIAL_LINK"


def test_rejects_non_html_response(tmp_path: Path) -> None:
    class NonHtmlSession(FakeSession):
        def get(self, url: str, **_: object) -> FakeResponse:
            return FakeResponse(b"{}", url=url, content_type="application/json")

    with pytest.raises(ValueError, match="Tipo de conteúdo inesperado"):
        _run(tmp_path, NonHtmlSession(_pages()))


def test_rejects_empty_or_oversized_response(tmp_path: Path) -> None:
    pages = _pages()
    pages[HOUSEHOLD_COMPOSITION_URL] = b""
    with pytest.raises(ValueError, match="Página oficial vazia"):
        _run(tmp_path, FakeSession(pages))

    with pytest.raises(ValueError, match="excede o limite"):
        discover_official_census_products(
            FakeSession(_pages()),
            snapshots_root=tmp_path / "snapshots-2",
            audit_root=tmp_path / "audit-2",
            snapshot_id="discovery-test",
            run_id="audit-test",
            max_page_bytes=5,
        )


def test_outputs_are_atomic_and_refuse_overwrite(tmp_path: Path) -> None:
    result = _run(tmp_path)

    assert (result.output_path / "official_product_link_register.csv").is_file()
    assert (result.output_path / "official_download_candidate_register.csv").is_file()
    assert (result.output_path / "official_discovery_summary.csv").is_file()
    assert not (tmp_path / "snapshots" / ".discovery-test.partial").exists()

    with pytest.raises(FileExistsError):
        _run(tmp_path)


def test_http_403_challenge_is_preserved_without_link_inference(
    tmp_path: Path,
) -> None:
    class ChallengeSession(FakeSession):
        def get(self, url: str, **_: object) -> FakeResponse:
            self.calls.append(url)
            return FakeResponse(
                b"<html>challenges.cloudflare.com</html>",
                url=url,
                status_code=403,
                challenge=True,
            )

    result = _run(tmp_path, ChallengeSession(_pages()))
    summary = result.summary.set_index("indicator")

    assert set(result.pages["status_code"]) == {403}
    assert set(result.pages["fetch_status"]) == {"HTTP_ERROR"}
    assert result.pages["challenge_detected"].all()
    assert result.links.empty
    assert int(summary.loc["pages_http_error", "value"]) == 2
    assert int(summary.loc["cloudflare_challenges", "value"]) == 2


def test_page_without_candidate_is_recorded_without_inference(tmp_path: Path) -> None:
    pages = {
        HOUSEHOLD_COMPOSITION_URL: b"<html><p>Sem links</p></html>",
        POPULATION_HOUSEHOLDS_URL: b"<html><p>Sem links</p></html>",
    }
    result = _run(tmp_path, FakeSession(pages))
    summary = result.summary.set_index("indicator")

    assert result.candidates.empty
    assert int(summary.loc["download_candidates", "value"]) == 0
    assert int(summary.loc["conceptually_validated_candidates", "value"]) == 0


@pytest.mark.parametrize("identifier", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_identifiers_before_fetch(tmp_path: Path, identifier):
    session = FakeSession(_pages())
    with pytest.raises(ValueError, match="identificador|nome simples"):
        discover_official_census_products(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id=identifier,
            run_id="audit-test",
        )
    assert session.calls == []


def test_audit_collision_prevents_fetch_and_snapshot(tmp_path: Path):
    session = FakeSession(_pages())
    (tmp_path / "audit" / "audit-test").mkdir(parents=True)
    with pytest.raises(FileExistsError):
        discover_official_census_products(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id="discovery-test",
            run_id="audit-test",
        )
    assert session.calls == []
    assert not (tmp_path / "snapshots" / "discovery-test").exists()
