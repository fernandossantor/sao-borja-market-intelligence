import zipfile

import pytest

from sbmi.state_rs_public_funds_profile import profile_state_rs_public_funds


def _snapshot(root):
    root.mkdir()
    with zipfile.ZipFile(root / "agreements.zip", "w") as archive:
        archive.writestr(
            "data.csv",
            "ExercicioConvenio;MunicipioConvenente;cnpj_convenente;ValorPago\n"
            "2020;São Borja;secret;10\n"
            "2021;Outra;secret;20\n"
            "2022;SAO BORJA;secret;30\n",
        )
    return root


def test_profiles_only_aggregates_and_exact_territory(tmp_path):
    result = profile_state_rs_public_funds(
        snapshot_path=_snapshot(tmp_path / "snapshot"),
        output_root=tmp_path / "audit",
        run_id="run",
    )
    summary = result.territorial_summary.iloc[0]
    assert summary["rows_scanned"] == 3
    assert summary["matched_rows"] == 2
    assert not result.schema_profile.sensitive_values_persisted.any()
    assert set(result.temporal_counts.year) == {2020, 2021, 2022}
    assert result.validation.status.eq("PASS").all()
    assert "secret" not in (result.output_path / "schema_profile.csv").read_text()


def test_refuses_overwrite(tmp_path):
    snapshot = _snapshot(tmp_path / "snapshot")
    kwargs = {
        "snapshot_path": snapshot,
        "output_root": tmp_path / "audit",
        "run_id": "run",
    }
    profile_state_rs_public_funds(**kwargs)
    with pytest.raises(FileExistsError):
        profile_state_rs_public_funds(**kwargs)


def test_quarantines_malformed_rows(tmp_path):
    snapshot = tmp_path / "snapshot"
    snapshot.mkdir()
    with zipfile.ZipFile(snapshot / "bad.zip", "w") as archive:
        archive.writestr(
            "bad.csv",
            "Exercicio;Municipio\n2026;São Borja;unexpected\n",
        )
    result = profile_state_rs_public_funds(
        snapshot_path=snapshot,
        output_root=tmp_path / "audit",
        run_id="run",
    )
    assert result.schema_profile.malformed_rows.iloc[0] == 1
    malformed = result.validation[
        result.validation.indicator == "malformed_rows_quarantined"
    ].iloc[0]
    assert malformed["status"] == "WARN"
