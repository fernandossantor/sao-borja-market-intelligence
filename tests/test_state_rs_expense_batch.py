import io
import zipfile

import pandas as pd
import pytest

from sbmi.state_rs_expense_batch import build_state_rs_expense_batch

HEADER = (
    "Exercicio;Mes;FaseGasto;TipoGasto;Orgao;Data;Valor;Municipio;"
    "CNPJ;Favorecido;Historico\n"
)


def _zip_bytes(month):
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w") as archive:
        content = (
            HEADER
            + f"2026;{month};Liquidação;T;O;2026-01-01;1.234,50;"
            "São Borja;x;y;z\n"
            + f"2026;{month};Liquidação;T;O;2026-01-01;10,00;"
            "Outra;x;y;z\n"
        )
        archive.writestr(
            f"Gasto-RS-2026{month:02d}.csv",
            content.encode("cp1252"),
        )
    return output.getvalue()


class Response:
    status_code = 200
    headers = {"Content-Type": "application/zip"}

    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    def raise_for_status(self):
        return None

    def iter_content(self, chunk_size):
        yield self.payload


class Session:
    def get(self, url, timeout, stream):
        month = int(url[-6:-4])
        return Response(url, _zip_bytes(month))


def _inventory(path):
    rows = []
    for month in (1, 2, 3, 4):
        payload = _zip_bytes(month)
        rows.append({
            "catalog_year": 2026,
            "resource_name_month": month,
            "resource_id": f"id-{month}",
            "source_url": f"https://dados.rs.gov.br/file-2026{month:02d}.zip",
            "head_status": 200,
            "content_length": len(payload),
            "obtained_at_utc": "2026-07-30T00:00:00+00:00",
        })
    pd.DataFrame(rows).to_csv(path, index=False)
    return path


def test_downloads_and_filters_minimal_staging(tmp_path):
    result = build_state_rs_expense_batch(
        inventory_path=_inventory(tmp_path / "inventory.csv"),
        snapshot_root=tmp_path / "raw",
        staging_root=tmp_path / "staging",
        audit_root=tmp_path / "audit",
        run_id="run",
        session=Session(),
    )
    assert len(result.manifest) == 4
    assert len(result.staging) == 4
    assert set(result.staging.Valor) == {"1234.50"}
    assert set(result.staging.FaseGasto) == {"Liquidação"}
    text = (result.staging_path / "state_expense_staging.csv").read_text()
    assert "Favorecido" not in text
    assert "Historico" not in text
    assert "CNPJ" not in text
    assert result.validation.status.ne("FAIL").all()


def test_refuses_overwrite(tmp_path):
    inventory = _inventory(tmp_path / "inventory.csv")
    kwargs = {
        "inventory_path": inventory,
        "snapshot_root": tmp_path / "raw",
        "staging_root": tmp_path / "staging",
        "audit_root": tmp_path / "audit",
        "run_id": "run",
        "session": Session(),
    }
    build_state_rs_expense_batch(**kwargs)
    with pytest.raises(FileExistsError):
        build_state_rs_expense_batch(**kwargs)
