import hashlib
import json
from pathlib import Path

import pytest

from sbmi.demography_census_sidra_discovery import (
    API_HELP_URL,
    COMPOSITION_CATALOG_URL,
    DESCRIPTOR_URLS,
    discover_sidra_metadata,
)


class Resp:
    def __init__(self, c, u, ctype):
        self.content = c
        self.url = u
        self.status_code = 200
        self.headers = {"Content-Type": ctype}

    def raise_for_status(self):
        pass


class Session:
    def __init__(self):
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(url)
        if url == API_HELP_URL:
            return Resp(b"<html>API</html>", url, "text/html")
        if url in DESCRIPTOR_URLS.values():
            tid = next(key for key, value in DESCRIPTOR_URLS.items() if value == url)
            doc = {
                "Id": int(tid),
                "Notas": "nota",
                "Variaveis": [
                    {
                        "Id": 6318 if tid == "4714" else 800,
                        "Nome": "Area" if tid == "4714" else "Domicilios",
                        "DecimaisArmazenamento": 3 if tid == "4714" else 0,
                        "DecimaisApresentacao": 3 if tid == "4714" else 0,
                        "UnidadeDeMedida": [
                            {"Unidade": "Quilômetros quadrados" if tid == "4714" else "Domicílios"}
                        ],
                        "VariaveisDerivadas": [],
                    }
                ],
                "Classificacoes": []
                if tid == "4714"
                else [
                    {
                        "Id": 460,
                        "Nome": "Espécie",
                        "IndiceTotal": 45902,
                        "AdmiteTotal": True,
                        "Categorias": [
                            {"Id": 45902, "Nome": "Total", "Disponibilidade": "2022"},
                            {"Id": 12076, "Nome": "Unipessoal", "Disponibilidade": "2022"},
                        ],
                    }
                ],
            }
            return Resp(json.dumps(doc).encode(), url, "application/json")
        tid, title = (
            ("9879", "Domicilios") if url == COMPOSITION_CATALOG_URL else ("4714", "Territorio")
        )
        html = (
            f"<table><tr><th></th><th>N</th><th>Nome</th><th>P</th>"
            f"<th>T</th></tr><tr><td></td><td>{tid}</td><td>{title}</td>"
            "<td>2022</td><td>MU</td></tr></table>"
        )
        return Resp(html.encode(), url, "text/html")


def run(tmp_path, s=None):
    return discover_sidra_metadata(
        s or Session(),
        snapshots_root=tmp_path / "snap",
        audit_root=tmp_path / "audit",
        snapshot_id="s",
        run_id="r",
    )


def test_metadata_only_hashes_and_descriptors(tmp_path: Path):
    s = Session()
    r = run(tmp_path, s)
    assert len(s.calls) == 5
    assert all("/values" not in url for url in s.calls)
    assert set(r.variables.table_id) == {"4714", "9879"}
    for row in r.pages.itertuples(index=False):
        assert (
            row.sha256
            == hashlib.sha256((r.snapshot_path / row.local_file).read_bytes()).hexdigest()
        )


def test_query_plans_are_not_executed_and_filters_are_explicit(tmp_path: Path):
    r = run(tmp_path)
    assert set(r.queries.execution_status) == {"PREPARED_NOT_EXECUTED"}
    assert set(r.queries.municipality_code) == {"4318002"}
    q = r.queries.set_index("table_id").loc["9879"]
    assert "c460/12076,12077,12078,12079" in q.url
    assert "c68/9902" in q.url
    assert int(r.summary.set_index("indicator").loc["values_requests", "value"]) == 0


def test_classification_and_natures(tmp_path: Path):
    r = run(tmp_path)
    assert set(r.classifications.classification_id) == {"460"}
    assert bool(r.categories.set_index("category_id").loc["45902", "is_total"])
    assert set(r.tables.conceptual_equivalence_status) == {"NOT_ASSESSED"}


def test_atomic_no_overwrite(tmp_path: Path):
    r = run(tmp_path)
    assert (r.output_path / "sidra_query_plan.csv").is_file()
    with pytest.raises(FileExistsError):
        run(tmp_path)


def test_invalid_limit(tmp_path: Path):
    with pytest.raises(ValueError, match="positivos"):
        discover_sidra_metadata(
            Session(),
            snapshots_root=tmp_path / "s",
            audit_root=tmp_path / "a",
            snapshot_id="s",
            run_id="r",
            max_page_bytes=0,
        )


@pytest.mark.parametrize("identifier", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_identifiers_before_fetch(tmp_path: Path, identifier):
    session = Session()
    with pytest.raises(ValueError, match="identificador|nome simples"):
        discover_sidra_metadata(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id=identifier,
            run_id="audit-test",
        )
    assert session.calls == []


def test_audit_collision_prevents_fetch_and_snapshot(tmp_path: Path):
    session = Session()
    (tmp_path / "audit" / "audit-test").mkdir(parents=True)
    with pytest.raises(FileExistsError):
        discover_sidra_metadata(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id="discovery-test",
            run_id="audit-test",
        )
    assert session.calls == []
    assert not (tmp_path / "snapshots" / "discovery-test").exists()
