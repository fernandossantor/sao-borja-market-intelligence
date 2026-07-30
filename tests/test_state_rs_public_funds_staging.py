import zipfile

import pandas as pd
import pytest

from sbmi.state_rs_public_funds_staging import (
    build_state_rs_public_funds_staging,
)

HEADER = (
    "ExercicioConvenio;Cod_Orgao;DataInicioVigencia;DataFimVigencia;"
    "DataAssinatura;NomeConcedente;NomeConvenente;MunicipioConvenente;"
    "cnpj_convenente;ValorPago;TipoTransferencia\n"
)


def _archive(path, member, rows):
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr(member, HEADER + "".join(rows))


def _snapshot(root):
    root.mkdir()
    common = "2020;1;a;b;c;X;Y;São Borja;secret;1.234,50;TIPO\n"
    _archive(root / "agreements_layout.zip", "old.csv", [common])
    _archive(
        root / "agreements_expense.zip",
        "current.csv",
        [common, "2021;1;a;b;c;X;Y;Outra;secret;10,00;TIPO\n"],
    )
    _archive(
        root / "agreements_revenue.zip",
        "revenue.csv",
        ["2020;1;a;b;c;X;Y;Outra;secret;10,00;TIPO\n"],
    )
    return root


def test_reconciles_overlap_and_minimizes_staging(tmp_path):
    result = build_state_rs_public_funds_staging(
        snapshot_path=_snapshot(tmp_path / "snapshot"),
        staging_root=tmp_path / "staging",
        audit_root=tmp_path / "audit",
        run_id="run",
    )
    assert len(result.staging) == 1
    assert result.staging.ValorPago.iloc[0] == "1234.50"
    assert result.staging.source_malformed_rows_excluded.iloc[0] == 0
    assert result.overlap_summary.classification.iloc[0] == "CONTENT_DUPLICATE"
    text = (result.staging_path / "state_public_funds_staging.csv").read_text()
    assert "secret" not in text
    decisions = pd.read_csv(result.audit_path / "resource_decisions.csv")
    layout = decisions[decisions.resource_id == "agreements_layout"].iloc[0]
    assert layout.disposition == "QUARANTINED_AMBIGUOUS_OVERLAP"
    assert result.validation.status.ne("FAIL").all()


def test_refuses_overwrite(tmp_path):
    snapshot = _snapshot(tmp_path / "snapshot")
    kwargs = {
        "snapshot_path": snapshot,
        "staging_root": tmp_path / "staging",
        "audit_root": tmp_path / "audit",
        "run_id": "run",
    }
    build_state_rs_public_funds_staging(**kwargs)
    with pytest.raises(FileExistsError):
        build_state_rs_public_funds_staging(**kwargs)
