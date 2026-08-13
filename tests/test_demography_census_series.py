import json
from pathlib import Path

import pytest

from sbmi.demography_census_series import collect_demography_census_series


class Response:
    status_code = 200
    headers = {"Content-Type": "application/json"}

    def __init__(self, url, payload):
        self.url, self.content = url, json.dumps(payload).encode()

    def raise_for_status(self):
        pass


class Session:
    def get(self, url, **_kwargs):
        header = {
            "NC": "Nível",
            "MC": "Unidade",
            "MN": "Unidade",
            "V": "Valor",
            "D1C": "Município (Código)",
            "D2C": "Ano (Código)",
            "D3C": "Variável (Código)",
            "D4C": "Sexo (Código)",
            "D4N": "Sexo",
        }
        row = {
            "NC": "6",
            "MC": "1020",
            "MN": "Pessoas",
            "V": "10",
            "D1C": "4318002",
            "D1N": "São Borja (RS)",
            "D2C": "1991",
            "D3C": "93",
            "D3N": "População",
            "D4C": "4",
            "D4N": "Homens",
        }
        return Response(url, [header, row])


def inputs(tmp_path):
    query = (
        {
            "query_id": "q",
            "table_id": "1",
            "years": ("1991",),
            "variable_ids": ("93",),
            "expected_rows": 1,
            "url": "https://apisidra.ibge.gov.br/values/t/1/n6/4318002/p/1991/v/93/c2/4",
            "comparability_note": "nota",
        },
    )
    return query, {
        name: tmp_path / name for name in ("raw", "staging", "curated", "exports", "audit")
    }


def test_collects_and_refuses_overwrite(tmp_path: Path):
    query, roots = inputs(tmp_path)
    result = collect_demography_census_series(
        Session(), queries=query, roots=roots, execution_id="run"
    )
    assert result.values.iloc[0].category_key == "Sexo=Homens"
    assert result.values.iloc[0].numeric_value == 10
    with pytest.raises(FileExistsError):
        collect_demography_census_series(Session(), queries=query, roots=roots, execution_id="run")


def test_rejects_wrong_geography(tmp_path: Path):
    class Bad(Session):
        def get(self, url, **kwargs):
            response = super().get(url, **kwargs)
            payload = json.loads(response.content)
            payload[1]["D1C"] = "0"
            return Response(url, payload)

    query, roots = inputs(tmp_path)
    with pytest.raises(ValueError, match="Geografia"):
        collect_demography_census_series(Bad(), queries=query, roots=roots, execution_id="run")
