from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_census_authority import (
    DOWNLOADS_URL,
    MUNICIPALITY_API_URL,
    PANORAMA_URL,
    SOURCE_REGISTRY,
    audit_census_authority,
    build_source_registry,
)


class FakeResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content
        self.status_code = 200
        self.headers = {"Content-Type": "text/html; charset=utf-8"}

    def raise_for_status(self) -> None:
        return None


class FakeSession:
    def __init__(self, pages: dict[str, bytes]) -> None:
        self.pages = pages
        self.calls: list[str] = []

    def get(self, url: str, **_: object) -> FakeResponse:
        self.calls.append(url)
        return FakeResponse(self.pages[url])


def _quality() -> pd.DataFrame:
    rows = []
    for index, row in enumerate(SOURCE_REGISTRY):
        identity = row[0]
        quarantined = index in {3, 16}
        rows.append(
            {
                "dataset_identity": identity,
                "quality_class": (
                    "SYSTEMATIC_DECIMAL_SCALE_ERROR"
                    if quarantined
                    else "NO_CONTENT_ANOMALY_DETECTED"
                ),
                "processed_reuse_status": (
                    "QUARANTINE_PROCESSED_PRODUCT"
                    if quarantined
                    else "CONTENT_EQUIVALENT_SOURCE_NOT_VALIDATED"
                ),
            }
        )
    return pd.DataFrame(rows)


def _provenance() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "dataset_identity": row[0],
                "source_authority_status": "NOT_ESTABLISHED",
                "provenance_status": "DOCUMENT_METADATA_ONLY",
            }
            for row in SOURCE_REGISTRY
        ]
    )


def _pages() -> dict[str, bytes]:
    panorama_topics = " ".join(row[1] for row in SOURCE_REGISTRY)
    download_products = " ".join(
        f"{pd.Timestamp(row[3]).strftime('%d/%m/%Y')} {row[2]}"
        for row in SOURCE_REGISTRY
    )
    return {
        PANORAMA_URL: f"<html>{panorama_topics}</html>".encode(),
        DOWNLOADS_URL: f"<html>{download_products}</html>".encode(),
        MUNICIPALITY_API_URL: (
            b'{"id":4318002,"nome":"Sao Borja","regiao-imediata":'
            b'{"regiao-intermediaria":{"UF":{"id":43,"sigla":"RS",'
            b'"nome":"Rio Grande do Sul"}}}}'
        ),
    }


def test_registry_contains_all_seventeen_topics() -> None:
    registry = build_source_registry()

    assert len(registry) == 17
    assert registry["dataset_identity"].is_unique
    assert set(registry["official_result_basis"]) == {
        "UNIVERSE",
        "SAMPLE_PRELIMINARY",
    }


def test_authority_verification_preserves_local_origin_uncertainty(
    tmp_path: Path,
) -> None:
    session = FakeSession(_pages())

    result = audit_census_authority(
        session,
        _quality(),
        _provenance(),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="authority-test",
        run_id="audit-test",
    )
    summary = result.summary.set_index("indicator")

    assert int(summary.loc["official_authority_confirmed_datasets", "value"]) == 17
    assert int(summary.loc["local_file_origin_established_datasets", "value"]) == 0
    assert int(summary.loc["official_rebuild_required_datasets", "value"]) == 2
    assert set(result.verification["local_file_origin_linkage_status"]) == {
        "LOCAL_FILE_ORIGIN_NOT_ESTABLISHED"
    }
    assert len(session.calls) == 3


def test_authority_snapshot_and_outputs_are_written(tmp_path: Path) -> None:
    result = audit_census_authority(
        FakeSession(_pages()),
        _quality(),
        _provenance(),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="authority-test",
        run_id="audit-test",
    )

    assert (result.snapshot_path / "panorama.html").is_file()
    assert (result.snapshot_path / "downloads.html").is_file()
    assert (result.snapshot_path / "municipality.json").is_file()
    assert (result.snapshot_path / "official_page_manifest.csv").is_file()
    assert (
        result.output_path / "demography_census_authority_verification.csv"
    ).is_file()
    assert (
        result.output_path / "demography_census_authority_summary.csv"
    ).is_file()


def test_incomplete_official_page_is_not_confirmed(tmp_path: Path) -> None:
    pages = _pages()
    pages[DOWNLOADS_URL] = b"<html>catalogo incompleto</html>"

    result = audit_census_authority(
        FakeSession(pages),
        _quality(),
        _provenance(),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="authority-test",
        run_id="audit-test",
    )

    assert set(result.verification["external_authority_status"]) == {
        "OFFICIAL_VERIFICATION_INCOMPLETE"
    }


def test_inconsistent_official_municipality_is_not_confirmed(
    tmp_path: Path,
) -> None:
    pages = _pages()
    pages[MUNICIPALITY_API_URL] = pages[MUNICIPALITY_API_URL].replace(
        b"4318002", b"4318101"
    )

    result = audit_census_authority(
        FakeSession(pages),
        _quality(),
        _provenance(),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="authority-test",
        run_id="audit-test",
    )

    assert not result.verification["official_municipality_code_confirmed"].any()
    assert set(result.verification["external_authority_status"]) == {
        "OFFICIAL_VERIFICATION_INCOMPLETE"
    }


def test_existing_run_is_not_overwritten_without_replace(tmp_path: Path) -> None:
    session = FakeSession(_pages())
    kwargs = {
        "snapshots_root": tmp_path / "snapshots",
        "audit_root": tmp_path / "audit",
        "snapshot_id": "authority-test",
        "run_id": "audit-test",
    }
    audit_census_authority(session, _quality(), _provenance(), **kwargs)

    with pytest.raises(FileExistsError):
        audit_census_authority(
            FakeSession(_pages()),
            _quality(),
            _provenance(),
            **kwargs,
        )
