import json
from pathlib import Path

import pandas as pd
import pytest

from sbmi.complementary_source_values import (
    CENSO_INDICATOR_GROUPS,
    IPS_EDITIONS,
    _query_plan,
    collect_complementary_source_values,
)


class FakeResponse:
    def __init__(self, url: str, content: bytes, content_type: str) -> None:
        self.url = url
        self.content = content
        self.status_code = 200
        self.headers = {"Content-Type": content_type}

    def raise_for_status(self) -> None:
        return None


class FakeSession:
    def __init__(self) -> None:
        self.urls: list[str] = []

    def get(self, url: str, **_kwargs) -> FakeResponse:
        self.urls.append(url)
        if "ipsbrasil.org.br" in url:
            content = (
                "Município,UF,Índice de Progresso Social\n"
                "São Borja,RS,\"63,50\"\n"
                "Outro,RS,\"50,00\"\n"
            ).encode()
            return FakeResponse(url, content, "text/csv; charset=utf-8")
        if "observatorio.sebrae" in url:
            payload = {"data": [{"Year": "2000", "Gini": "0.51"}]}
            return FakeResponse(url, json.dumps(payload).encode(), "application/json")
        locality = "4318002" if url.endswith("/4318002") else "431800"
        payload = [{
            "id": 96385,
            "res": [{"localidade": locality, "res": {"2010": "61671", "2022": "59676"}}],
        }]
        return FakeResponse(url, json.dumps(payload).encode(), "application/json")


def _sebrae_plan(path: Path) -> Path:
    target = path / "candidate_query_inventory.csv"
    pd.DataFrame([{
        "query_id": "sebrae_candidate_001",
        "dimension": "ambiente_sociocultural_territorial",
        "query_url": (
            "https://apiv2-observatorio.sebrae.com.br/tesseract/data.jsonrecords"
            "?Municipality=4318002&Year=2000&cube=PNUD_Atlas_IDHM"
            "&drilldowns=Year&measures=Gini"
        ),
        "execution_status": "PREPARED_NOT_EXECUTED",
        "primary_source_declared": "PNUD/Ipea/FJP",
    }]).to_csv(target, index=False)
    return target


def test_query_plan_contains_four_sources_and_available_periods(tmp_path: Path) -> None:
    plan = _query_plan(_sebrae_plan(tmp_path))

    assert set(plan.source_id) == {
        "ibge_censo_2022_panorama",
        "ibge_cidades_panorama",
        "sebrae_observatorio_profile",
        "ips_brasil_explorer",
    }
    assert len(plan) == len(CENSO_INDICATOR_GROUPS) + 1 + 1 + len(IPS_EDITIONS)
    assert set(plan.loc[plan.source_id.eq("ips_brasil_explorer"), "reference_period"]) == {
        "2024", "2025", "2026",
    }
    assert set(
        plan.loc[plan.source_id.eq("sebrae_observatorio_profile"), "declared_author"]
    ) == {"PNUD/Ipea/FJP"}


def test_collection_publishes_five_immutable_layers(tmp_path: Path) -> None:
    roots = [tmp_path / name for name in ("raw", "staging", "curated", "exports", "audit")]
    session = FakeSession()
    result = collect_complementary_source_values(
        session,
        sebrae_plan_path=_sebrae_plan(tmp_path),
        snapshot_root=roots[0],
        staging_root=roots[1],
        curated_root=roots[2],
        export_root=roots[3],
        audit_root=roots[4],
        execution_id="run-001",
    )

    assert result.manifest.source_id.nunique() == 4
    assert len(session.urls) == len(CENSO_INDICATOR_GROUPS) + 5
    assert set(result.values.source_id) == set(result.manifest.source_id)
    assert result.values.reference_year.dropna().between(1996, 2026).all()
    ips = result.values.loc[result.values.source_id.eq("ips_brasil_explorer")]
    assert not ips.raw_value.astype(str).str.contains("Outro").any()
    assert (result.snapshot_path / "manifest.csv").is_file()
    assert (result.staging_path / "complementary_values_staging.csv").is_file()
    assert (result.curated_path / "complementary_values.csv").is_file()
    assert (result.export_path / "complementary_values.csv").is_file()
    assert (result.audit_path / "source_manifest.csv").is_file()
    assert set(result.validation.status) == {"PASS"}

    with pytest.raises(FileExistsError):
        collect_complementary_source_values(
            FakeSession(),
            sebrae_plan_path=_sebrae_plan(tmp_path),
            snapshot_root=roots[0],
            staging_root=roots[1],
            curated_root=roots[2],
            export_root=roots[3],
            audit_root=roots[4],
            execution_id="run-001",
        )


def test_collection_rejects_unapproved_sebrae_host(tmp_path: Path) -> None:
    plan = _sebrae_plan(tmp_path)
    frame = pd.read_csv(plan)
    frame.loc[0, "query_url"] = "https://example.com/data.json"
    frame.to_csv(plan, index=False)

    with pytest.raises(ValueError, match="fora do escopo"):
        _query_plan(plan)
