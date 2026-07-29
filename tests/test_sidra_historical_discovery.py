import hashlib
import json
from pathlib import Path

import pytest

from sbmi.sidra_historical_discovery import (
    ALLOWED_DIMENSIONS,
    QUERY_SPECS,
    TABLE_SPECS,
    discover_sidra_historical_metadata,
)


class Response:
    def __init__(self, content, url):
        self.content = content
        self.url = url
        self.status_code = 200
        self.headers = {"Content-Type": "application/json"}

    def raise_for_status(self):
        pass


class Session:
    def __init__(self):
        self.calls = []

    def get(self, url, **kwargs):
        self.calls.append(url)
        table_id = url.rsplit("/", 1)[-1]
        availability = {
            "156": "1991, 2000, 2010",
            "289": "1986 a 2025",
            "291": "1986 a 2025",
            "3939": "1974 a 2025",
            "5457": "1974 a 2025",
            "5938": "2002 a 2023",
            "6449": "2006 a 2021",
            "6450": "2006 a 2021",
            "6579": "2001 a 2006, 2008 a 2009, 2011 a 2021, 2024 a 2025",
            "9514": "2022",
        }[table_id]
        query_spec = QUERY_SPECS.get(table_id)
        variable_ids = query_spec["variable_ids"] if query_spec else (table_id,)
        classification_id = query_spec["classification_id"] if query_spec else "1"
        category_ids = query_spec["category_ids"] if query_spec else ("0",)
        document = {
            "Id": int(table_id),
            "Nome": f"Tabela {table_id}",
            "Pesquisa": TABLE_SPECS[table_id][1],
            "Disponibilidade": availability,
            "TipoPeriodo": "Ano",
            "NiveisTerritoriais": [{"Nome": "Brasil"}, {"Nome": "Município"}],
            "Variaveis": [
                {
                    "Id": int(variable_id),
                    "Nome": "Variável",
                    "UnidadeDeMedida": [{"Unidade": "Unidade", "Periodo": availability}],
                    "VariaveisDerivadas": [],
                }
                for variable_id in variable_ids
            ],
            "Classificacoes": [
                {
                    "Id": int(classification_id),
                    "Nome": "Classe",
                    "IndiceTotal": 0,
                    "AdmiteTotal": True,
                    "Categorias": [
                        {
                            "Id": int(category_id),
                            "Nome": "Categoria",
                            "Disponibilidade": availability,
                        }
                        for category_id in category_ids
                    ],
                }
            ],
        }
        return Response(json.dumps(document).encode(), url)


def run(tmp_path, session=None):
    return discover_sidra_historical_metadata(
        session or Session(),
        snapshots_root=tmp_path / "snapshots",
        audit_root=tmp_path / "audit",
        snapshot_id="snapshot",
        run_id="run",
    )


def test_metadata_only_and_hashes(tmp_path: Path):
    session = Session()
    result = run(tmp_path, session)
    assert len(session.calls) == 10
    assert all("/values" not in url for url in session.calls)
    assert set(result.tables.table_id) == set(TABLE_SPECS)
    for row in result.manifest.itertuples(index=False):
        path = result.snapshot_path / row.local_file
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row.sha256


def test_period_expansion_is_limited_to_target_interval(tmp_path: Path):
    result = run(tmp_path)
    years = result.periods.groupby("table_id").reference_year.agg(["min", "max", "count"])
    assert tuple(years.loc["291"]) == (1996, 2025, 30)
    assert tuple(years.loc["5457"]) == (1996, 2025, 30)
    assert tuple(years.loc["5938"]) == (2002, 2023, 22)
    assert tuple(years.loc["6579"]) == (2001, 2025, 21)
    assert tuple(years.loc["156"]) == (2000, 2010, 2)
    assert result.periods.reference_year.max() == 2025


def test_only_existing_dimensions_and_no_conceptual_claim(tmp_path: Path):
    result = run(tmp_path)
    dimensions = {
        dimension for value in result.tables.mapped_dimensions for dimension in value.split("|")
    }
    assert dimensions <= ALLOWED_DIMENSIONS
    assert set(result.tables.conceptual_equivalence_status) == {"NOT_ASSESSED"}
    summary = result.summary.set_index("indicator").value
    assert int(summary["values_requests"]) == 0
    assert int(summary["conceptually_validated_tables"]) == 0
    assert int(summary["queries_prepared"]) == 3
    assert int(summary["planned_max_value_rows"]) == 2580
    assert set(result.query_plans.execution_status) == {"PREPARED_NOT_EXECUTED"}
    assert set(result.query_plans.table_id) == set(QUERY_SPECS)


def test_outputs_are_atomic_and_refuse_overwrite(tmp_path: Path):
    result = run(tmp_path)
    assert (result.output_path / "sidra_historical_table_register.csv").is_file()
    assert (result.output_path / "sidra_historical_limitation_register.csv").is_file()
    assert (result.output_path / "sidra_historical_query_plan.csv").is_file()
    with pytest.raises(FileExistsError):
        run(tmp_path)


@pytest.mark.parametrize("identifier", ["", ".", "..", "nested/name"])
def test_rejects_unsafe_identifier_before_fetch(tmp_path: Path, identifier):
    session = Session()
    with pytest.raises(ValueError, match="identificador|nome simples"):
        discover_sidra_historical_metadata(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id=identifier,
            run_id="run",
        )
    assert session.calls == []


def test_rejects_non_municipal_descriptor(tmp_path: Path):
    class NonMunicipalSession(Session):
        def get(self, url, **kwargs):
            response = super().get(url, **kwargs)
            document = json.loads(response.content)
            document["NiveisTerritoriais"] = [{"Nome": "Brasil"}]
            return Response(json.dumps(document).encode(), url)

    with pytest.raises(ValueError, match="sem nível municipal"):
        run(tmp_path, NonMunicipalSession())


def test_invalid_limit_before_fetch(tmp_path: Path):
    session = Session()
    with pytest.raises(ValueError, match="positivos"):
        discover_sidra_historical_metadata(
            session,
            snapshots_root=tmp_path / "snapshots",
            audit_root=tmp_path / "audit",
            snapshot_id="snapshot",
            run_id="run",
            max_descriptor_bytes=0,
        )
    assert session.calls == []
