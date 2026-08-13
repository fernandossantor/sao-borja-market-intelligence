"""Testes da série oficial DCA."""

import hashlib
import json

import pandas as pd
import pytest

from sbmi.siconfi_dca_series import (
    EXPENSE_ACCOUNTS,
    EXPENSE_MEASURES,
    REVENUE_ACCOUNTS,
    REVENUE_MEASURES,
    curate_siconfi_dca_series,
)


def test_curates_only_observed_values_and_marks_missing(tmp_path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot.mkdir()
    manifests = []
    for year in range(2019, 2026):
        items = []
        for code, label in REVENUE_ACCOUNTS.items():
            items.append(
                {
                    "exercicio": year,
                    "cod_conta": code,
                    "conta": label,
                    "coluna": REVENUE_MEASURES[0],
                    "valor": 1,
                }
            )
        for code, label in EXPENSE_ACCOUNTS.items():
            for measure in EXPENSE_MEASURES:
                items.append(
                    {
                        "exercicio": year,
                        "cod_conta": code,
                        "conta": label,
                        "coluna": measure,
                        "valor": 2,
                    }
                )
        content = json.dumps({"items": items}).encode()
        filename = f"{year}.json"
        (snapshot / filename).write_bytes(content)
        manifests.append(
            {
                "reference_year": year,
                "file": filename,
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
            }
        )
    pd.DataFrame(manifests).to_csv(snapshot / "manifest.csv", index=False)
    roots = {layer: tmp_path / layer for layer in ("staging", "curated", "exports", "audit")}
    result = curate_siconfi_dca_series(snapshot, roots=roots, execution_id="run")
    assert result.values.account_code.nunique() == 18
    assert (result.coverage.status == "MISSING").sum() == 154
    with pytest.raises(FileExistsError):
        curate_siconfi_dca_series(snapshot, roots=roots, execution_id="run")


def test_rejects_snapshot_hash_divergence(tmp_path) -> None:
    snapshot = tmp_path / "snapshot"
    snapshot.mkdir()
    content = json.dumps({"items": []}).encode()
    (snapshot / "2019.json").write_bytes(content + b" ")
    pd.DataFrame(
        [
            {
                "reference_year": year,
                "file": "2019.json",
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
            }
            for year in range(2019, 2026)
        ]
    ).to_csv(snapshot / "manifest.csv", index=False)
    with pytest.raises(ValueError, match="Integridade DCA divergente"):
        curate_siconfi_dca_series(
            snapshot,
            roots={layer: tmp_path / layer for layer in ("staging", "curated", "exports", "audit")},
            execution_id="run",
        )
