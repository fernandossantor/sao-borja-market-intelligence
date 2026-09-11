from __future__ import annotations

import zipfile
from pathlib import Path

import pandas as pd
import pytest

from sbmi.cnpj_territorial_control import (
    COMPANY_COLUMNS,
    ESTABLISHMENT_COLUMNS,
    curate_cnpj_territorial_control,
)


def _zip_rows(path: Path, member: str, rows: list[list[str]]) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zf:
        text = "\n".join(";".join(row) for row in rows) + "\n"
        zf.writestr(member, text.encode("latin1"))


def _est(
    root: str,
    order: str,
    dv: str,
    matrix_branch: str,
    status: str,
    municipality: str,
    *,
    fantasy: str,
    cnae: str,
    uf: str = "RS",
) -> list[str]:
    values = {column: "" for column in ESTABLISHMENT_COLUMNS}
    values.update(
        {
            "cnpj_basico": root,
            "cnpj_ordem": order,
            "cnpj_dv": dv,
            "identificador_matriz_filial": matrix_branch,
            "nome_fantasia": fantasy,
            "situacao_cadastral": status,
            "data_inicio_atividade": "20200101",
            "cnae_fiscal_principal": cnae,
            "uf": uf,
            "municipio": municipality,
        }
    )
    return [values[c] for c in ESTABLISHMENT_COLUMNS]


def _company(root: str, name: str, size: str) -> list[str]:
    values = {column: "" for column in COMPANY_COLUMNS}
    values.update(
        {
            "cnpj_basico": root,
            "razao_social": name,
            "natureza_juridica": "2062",
            "capital_social": "100000,00",
            "porte_empresa": size,
        }
    )
    return [values[c] for c in COMPANY_COLUMNS]


def test_cnpj_territorial_control_classifies_local_and_external_matrices(
    tmp_path: Path,
) -> None:
    est_dir = tmp_path / "est"
    emp_dir = tmp_path / "emp"
    est_dir.mkdir()
    emp_dir.mkdir()

    # A ordem do estabelecimento foi escolhida de propósito para provar que
    # o pipeline usa o identificador oficial matriz/filial, e não /0001.
    est_rows = [
        _est(
            "11111111",
            "0100",
            "10",
            "1",
            "02",
            "8863",
            fantasy="Matriz local",
            cnae="4711302",
        ),
        _est(
            "11111111",
            "0101",
            "91",
            "2",
            "02",
            "8863",
            fantasy="Filial local",
            cnae="4711302",
        ),
        _est(
            "22222222",
            "0200",
            "20",
            "1",
            "02",
            "8841",
            fantasy="Matriz externa",
            cnae="4771701",
        ),
        _est(
            "22222222",
            "0201",
            "00",
            "2",
            "02",
            "8863",
            fantasy="Filial externa",
            cnae="4771701",
        ),
        _est(
            "33333333",
            "0001",
            "30",
            "1",
            "08",
            "8863",
            fantasy="Baixada",
            cnae="4781400",
        ),
    ]
    _zip_rows(est_dir / "Estabelecimentos0.zip", "ESTABELE0.CSV", est_rows)

    company_rows = [
        _company("11111111", "Empresa Local Ltda", "03"),
        _company("22222222", "Rede Externa S.A.", "05"),
        _company("33333333", "Baixada Ltda", "01"),
    ]
    _zip_rows(emp_dir / "Empresas0.zip", "EMPRE0.CSV", company_rows)
    _zip_rows(
        tmp_path / "Municipios.zip",
        "MUNIC.CSV",
        [["8863", "SAO BORJA"], ["8841", "SANTA MARIA"]],
    )

    roots = {
        layer: tmp_path / layer
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_cnpj_territorial_control(
        establishments=est_dir,
        companies=emp_dir,
        municipalities_zip=tmp_path / "Municipios.zip",
        roots=roots,
        execution_id="run",
        chunksize=2,
    )

    assert len(result.establishments) == 3
    statuses = result.establishments["territorial_control_status"].value_counts().to_dict()
    assert statuses == {
        "MATRIZ_LOCAL": 1,
        "FILIAL_DE_MATRIZ_LOCAL": 1,
        "FILIAL_DE_MATRIZ_EXTERNA": 1,
    }
    external = result.establishments.query(
        "territorial_control_status == 'FILIAL_DE_MATRIZ_EXTERNA'"
    ).iloc[0]
    assert external["matrix_municipality_name"] == "SANTA MARIA"
    assert external["matrix_cnpj"].startswith("22222222")
    assert external["natureza_juridica"] == "2062"

    assert set(result.by_division["cnae_division"]) == {"47"}
    assert result.validation.query("indicator == 'duplicate_cnpjs'").iloc[0]["status"] == "PASS"
    assert (result.paths["curated"] / "cnpj_territorial_control.csv").exists()
    assert (result.paths["exports"] / "cnpj_territorial_control_by_division.csv").exists()

    persisted = pd.read_csv(
        result.paths["curated"] / "cnpj_territorial_control.csv", dtype=str
    )
    assert len(persisted) == 3
    assert set(persisted["natureza_juridica"]) == {"2062"}


def test_cnpj_territorial_control_accepts_alphanumeric_cnpj(tmp_path: Path) -> None:
    est_dir = tmp_path / "est"
    emp_dir = tmp_path / "emp"
    est_dir.mkdir()
    emp_dir.mkdir()

    # Desde julho de 2026 novas inscrições podem usar letras nas 12 primeiras
    # posições do CNPJ. O parser deve preservar raiz e ordem como texto.
    root = "A1B2C3D4"
    order = "E08G"
    _zip_rows(
        est_dir / "Estabelecimentos0.zip",
        "ESTABELE0.CSV",
        [
            _est(
                root,
                order,
                "12",
                "1",
                "02",
                "8863",
                fantasy="Matriz alfanumerica",
                cnae="6201501",
            )
        ],
    )
    _zip_rows(
        emp_dir / "Empresas0.zip",
        "EMPRE0.CSV",
        [_company(root, "Empresa Alfa Ltda", "03")],
    )
    _zip_rows(tmp_path / "Municipios.zip", "MUNIC.CSV", [["8863", "SAO BORJA"]])

    roots = {
        layer: tmp_path / layer
        for layer in ("staging", "curated", "exports", "audit")
    }
    result = curate_cnpj_territorial_control(
        establishments=est_dir,
        companies=emp_dir,
        municipalities_zip=tmp_path / "Municipios.zip",
        roots=roots,
        execution_id="alpha",
        chunksize=1,
    )

    row = result.establishments.iloc[0]
    assert row["cnpj"] == "A1B2C3D4E08G12"
    assert row["cnpj_basico"] == root
    assert row["cnpj_ordem"] == order
    assert row["territorial_control_status"] == "MATRIZ_LOCAL"


def test_cnpj_territorial_control_refuses_overwrite(tmp_path: Path) -> None:
    est_dir = tmp_path / "est"
    emp_dir = tmp_path / "emp"
    est_dir.mkdir()
    emp_dir.mkdir()
    _zip_rows(
        est_dir / "Estabelecimentos0.zip",
        "ESTABELE0.CSV",
        [
            _est(
                "11111111",
                "0100",
                "10",
                "1",
                "02",
                "8863",
                fantasy="Matriz",
                cnae="4711302",
            )
        ],
    )
    _zip_rows(
        emp_dir / "Empresas0.zip",
        "EMPRE0.CSV",
        [_company("11111111", "Empresa", "03")],
    )
    _zip_rows(tmp_path / "Municipios.zip", "MUNIC.CSV", [["8863", "SAO BORJA"]])

    roots = {
        layer: tmp_path / layer
        for layer in ("staging", "curated", "exports", "audit")
    }
    kwargs = dict(
        establishments=est_dir,
        companies=emp_dir,
        municipalities_zip=tmp_path / "Municipios.zip",
        roots=roots,
        execution_id="run",
        chunksize=1,
    )
    curate_cnpj_territorial_control(**kwargs)
    with pytest.raises(FileExistsError):
        curate_cnpj_territorial_control(**kwargs)
