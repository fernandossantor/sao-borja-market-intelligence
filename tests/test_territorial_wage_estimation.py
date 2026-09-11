from pathlib import Path

import pandas as pd
import pytest

from sbmi.territorial_wage_estimation import (
    estimate_territorial_wages,
    write_wage_outputs,
)


def _worker_row(
    cnae: str,
    nature: str,
    *,
    dec: str = "100",
    avg: str = "100",
    active: str = "1",
    abandoned: str = "0",
    establishment_type: str = "1",
) -> dict[str, str]:
    return {
        "CNAE 2.0 Subclasse - Codigo": cnae,
        "Município - Código": "431800",
        "Natureza Jurídica - Código": nature,
        "Ind Vínculo Ativo 31/12 - Código": active,
        "Ind Vínculo Abandonado - Código": abandoned,
        "Tipo Estabelecimento - Código": establishment_type,
        "Vl Rem Dezembro Nom": dec,
        "Vl Rem Média Nom": avg,
    }


def _rfb_row(cnae: str, nature: str, status: str, n: int) -> dict[str, str]:
    return {
        "cnae_subclass": cnae,
        "natureza_juridica": nature,
        "territorial_control_status": status,
        "estabelecimentos": str(n),
    }


def _frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    rais = pd.DataFrame(
        [
            _worker_row("4711302", "2062", dec="100", avg="100"),
            _worker_row("4711302", "2062", dec="200", avg="200"),
            _worker_row("4711302", "2062", dec="300", avg="300"),
            _worker_row("4711302", "2062", dec="", avg="400"),
            _worker_row("4721102", "2062", dec="500", avg="500"),
            _worker_row("4721102", "2062", dec="600", avg="600"),
            _worker_row("4711302", "2062", abandoned="1", dec="", avg="0"),
            _worker_row("4711302", "2062", active="0", dec="700", avg="700"),
            _worker_row("4711302", "1031", dec="800", avg="800"),
        ]
    )
    rfb = pd.DataFrame(
        [
            _rfb_row("4711302", "2062", "MATRIZ_LOCAL", 3),
            _rfb_row("4711302", "2062", "FILIAL_DE_MATRIZ_EXTERNA", 1),
            _rfb_row("4721102", "2054", "FILIAL_DE_MATRIZ_EXTERNA", 1),
        ]
    )
    return rais, rfb


def test_wage_estimation_filters_abandoned_and_reconciles_metrics() -> None:
    rais, rfb = _frames()
    result = estimate_territorial_wages(rais, rfb, expected_business_active_links=6)
    summary = result.summary.set_index("indicator")["value"]
    levels = result.cells.set_index("cnae_subclass")["match_level"].to_dict()

    assert levels["4711302"] == "subclass_nature"
    assert levels["4721102"] == "subclass"
    assert summary["rais_business_active_links"] == 6
    assert summary["rais_dec_valid_links"] == 5
    assert summary["rais_dec_missing_links"] == 1
    assert summary["rais_dec_mass_informed"] == 1700
    assert summary["rais_avg_rem_sum"] == 2100
    assert summary["estimated_external_active_links"] == pytest.approx(3)
    assert summary["estimated_external_dec_mass"] == pytest.approx(1250)
    assert summary["estimated_external_avg_rem_sum"] == pytest.approx(1350)
    assert set(result.validation["status"]) == {"PASS", "REVIEW"}
    assert "FAIL" not in set(result.validation["status"])


def test_write_wage_outputs_refuses_overwrite(tmp_path: Path) -> None:
    rais, rfb = _frames()
    result = estimate_territorial_wages(rais, rfb)
    destination = tmp_path / "run"
    write_wage_outputs(result, destination)

    assert (destination / "territorial_wage_summary.csv").exists()
    assert (destination / "territorial_wage_cells.csv").exists()
    with pytest.raises(FileExistsError):
        write_wage_outputs(result, destination)
