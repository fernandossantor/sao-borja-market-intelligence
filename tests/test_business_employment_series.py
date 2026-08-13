import json
from pathlib import Path

import pytest

from sbmi.business_employment_series import curate_business_employment_series


def inputs(tmp_path):
    est = {"annotations": {"table": "Estabelecimentos"}, "data": []}
    workers = {"annotations": {"table": "Vinculos"}, "data": []}
    for year in range(2016, 2026):
        common = {"Municipality ID": 4318002, "Municipality": "São Borja", "Year": year}
        est["data"].append(common | {"Establishments": year})
        workers["data"].append(common | {"Workers": year, "Remuneration Avg Nominal": year + 0.5})
    ep, wp = tmp_path / "est.json", tmp_path / "workers.json"
    ep.write_text(json.dumps(est))
    wp.write_text(json.dumps(workers))
    roots = {layer: tmp_path / layer for layer in ("staging", "curated", "exports", "audit")}
    return ep, wp, roots


def test_curates_three_complete_series_and_refuses_overwrite(tmp_path: Path):
    ep, wp, roots = inputs(tmp_path)
    kwargs = dict(establishments_path=ep, workers_path=wp, roots=roots, execution_id="run")
    result = curate_business_employment_series(**kwargs)
    assert len(result.values) == 30
    assert set(result.validation.status) == {"PASS"}
    with pytest.raises(FileExistsError):
        curate_business_employment_series(**kwargs)


def test_rejects_wrong_municipality(tmp_path: Path):
    ep, wp, roots = inputs(tmp_path)
    payload = json.loads(ep.read_text())
    payload["data"][0]["Municipality ID"] = 0
    ep.write_text(json.dumps(payload))
    with pytest.raises(ValueError, match="Validação"):
        curate_business_employment_series(
            establishments_path=ep, workers_path=wp, roots=roots, execution_id="run"
        )
