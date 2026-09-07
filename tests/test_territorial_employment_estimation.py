from pathlib import Path

import pandas as pd
import pytest

from sbmi.territorial_employment_estimation import (
    estimate_territorial_employment,
    write_estimation_outputs,
)


def _rais_row(cnae: str, nature: str, links: int) -> dict[str, str]:
    return {
        "CNAE 2.0 Subclasse - Codigo": cnae,
        "Município - Código": "431800",
        "Natureza Jurídica - Código": nature,
        "Qtd Vínculos Ativos": str(links),
        "Tipo Estabelecimento - Código": "1",
    }


def _rfb_row(cnae: str, nature: str, status: str, n: int) -> dict[str, str]:
    return {
        "cnae_subclass": cnae,
        "natureza_juridica": nature,
        "territorial_control_status": status,
        "estabelecimentos": str(n),
    }


def test_estimation_uses_hierarchical_matches_and_reconciles_links() -> None:
    rais = pd.DataFrame(
        [
            _rais_row("4711302", "2062", 30),
            _rais_row("4721102", "2062", 10),
            _rais_row("4711303", "2054", 4),
            _rais_row("4711401", "2054", 2),
            _rais_row("4789001", "2054", 1),
            _rais_row("6201501", "2062", 0),
        ]
    )
    rfb = pd.DataFrame(
        [
            _rfb_row("4711302", "2062", "MATRIZ_LOCAL", 3),
            _rfb_row("4711302", "2062", "FILIAL_DE_MATRIZ_EXTERNA", 1),
            _rfb_row("4721102", "2054", "MATRIZ_LOCAL", 1),
            _rfb_row("4711302", "2054", "FILIAL_DE_MATRIZ_EXTERNA", 1),
            _rfb_row("4711499", "2062", "MATRIZ_LOCAL", 1),
            _rfb_row("4790101", "2062", "FILIAL_DE_MATRIZ_EXTERNA", 1),
        ]
    )

    result = estimate_territorial_employment(rais, rfb)
    levels = result.cells.set_index("cnae_subclass")["match_level"].to_dict()

    assert levels["4711302"] == "subclass_nature"
    assert levels["4721102"] == "subclass"
    assert levels["4711303"] == "class_nature"
    assert levels["4711401"] == "class"
    assert levels["4789001"] == "division"
    assert levels["6201501"] == "unmatched"

    total = result.summary.set_index("indicator")["value"]
    assert total["rais_business_active_links"] == 47
    assert total["estimated_external_branch_links"] == pytest.approx(11.875)
    assert result.validation.query("indicator == 'estimated_links_reconcile'").iloc[0][
        "status"
    ] == "PASS"


def test_write_outputs_refuses_overwrite(tmp_path: Path) -> None:
    rais = pd.DataFrame([_rais_row("4711302", "2062", 10)])
    rfb = pd.DataFrame(
        [_rfb_row("4711302", "2062", "FILIAL_DE_MATRIZ_EXTERNA", 1)]
    )
    result = estimate_territorial_employment(rais, rfb)
    destination = tmp_path / "run"
    write_estimation_outputs(result, destination)

    assert (destination / "territorial_employment_summary.csv").exists()
    with pytest.raises(FileExistsError):
        write_estimation_outputs(result, destination)
