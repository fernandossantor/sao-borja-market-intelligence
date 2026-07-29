import hashlib
import json
from pathlib import Path

import pandas as pd
import pytest

from sbmi.sidra_historical_values import collect_sidra_historical_values


class Response:
    status_code = 200
    headers = {"Content-Type": "application/json"}

    def __init__(self, url):
        self.url = url
        self.content = json.dumps(
            [
                {
                    "NC": "nível",
                    "MC": "unidade",
                    "MN": "unidade",
                    "V": "valor",
                    "D1C": "município",
                    "D2C": "ano",
                    "D3C": "variável",
                    "D4C": "categoria",
                },
                {
                    "NC": "6",
                    "MC": "1",
                    "MN": "Unidade",
                    "V": "10",
                    "D1C": "4318002",
                    "D1N": "São Borja (RS)",
                    "D2C": "1996",
                    "D3C": "105",
                    "D3N": "Variável",
                    "D4C": "2670",
                    "D4N": "Categoria",
                },
            ]
        ).encode()

    def raise_for_status(self):
        pass


class Session:
    def get(self, url, **kwargs):
        return Response(url)


def _plan(path: Path):
    pd.DataFrame(
        [
            {
                "query_id": "agro_3939_1996_2025",
                "table_id": "3939",
                "municipality_code": "4318002",
                "variable_ids": "105",
                "classification_id": "79",
                "category_ids": "2670",
                "url": (
                    "https://apisidra.ibge.gov.br/values/t/3939/n6/4318002/"
                    "p/1996/v/105/c79/2670"
                ),
                "execution_status": "PREPARED_NOT_EXECUTED",
            }
        ]
    ).to_csv(path, index=False)


def _run_with_plan(tmp_path, plan):
    return collect_sidra_historical_values(
        Session(),
        query_plan_path=plan,
        snapshot_root=tmp_path / "raw",
        staging_root=tmp_path / "staging",
        curated_root=tmp_path / "curated",
        export_root=tmp_path / "exports",
        audit_root=tmp_path / "audit",
        execution_id="execution",
    )


def _run(tmp_path):
    plan = tmp_path / "plan.csv"
    _plan(plan)
    return _run_with_plan(tmp_path, plan)


def test_collects_all_layers_and_preserves_hash(tmp_path):
    result = _run(tmp_path)
    assert len(result.curated) == 1
    assert result.curated.iloc[0].numeric_value == 10
    raw = result.snapshot_path / "sidra_values_3939.json"
    assert hashlib.sha256(raw.read_bytes()).hexdigest() == result.manifest.iloc[0].sha256
    for path in (
        result.staging_path,
        result.curated_path,
        result.export_path,
        result.audit_path,
    ):
        assert path.is_dir()


def test_refuses_overwrite(tmp_path):
    _run(tmp_path)
    with pytest.raises(FileExistsError):
        _run(tmp_path)


def test_rejects_wrong_municipality_before_request(tmp_path):
    plan = tmp_path / "plan.csv"
    _plan(plan)
    frame = pd.read_csv(plan, dtype=str)
    frame["municipality_code"] = "4300000"
    frame.to_csv(plan, index=False)
    with pytest.raises(ValueError, match="município"):
        _run_with_plan(tmp_path, plan)


def test_rejects_unsafe_url(tmp_path):
    plan = tmp_path / "plan.csv"
    _plan(plan)
    frame = pd.read_csv(plan, dtype=str)
    frame["url"] = "https://example.com/values"
    frame.to_csv(plan, index=False)
    with pytest.raises(ValueError, match="endpoint permitido"):
        _run_with_plan(tmp_path, plan)
