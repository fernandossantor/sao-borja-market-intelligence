from __future__ import annotations

from pathlib import Path

import pandas as pd

from sbmi.public_market_series_curated import (
    _normalize_ncm,
    _numeric_decimal_comma,
    _period_from_radar_filename,
    _radar_numeric_value,
    parse_crosswalk_markdown,
)


def test_period_from_radar_filename_uses_filename_not_anomes() -> None:
    assert _period_from_radar_filename(Path("Composicao_de_Mercado_01_2026.csv")) == "2026-01"
    assert _period_from_radar_filename(Path("Exportacoes_NCM_12_2025.csv")) == "2025-12"


def test_normalize_ncm_preserves_leading_zeroes() -> None:
    result = _normalize_ncm(pd.Series(["7039090", "07039090", "84211210.0"]))
    assert result.tolist() == ["07039090", "07039090", "84211210"]


def test_numeric_decimal_comma_handles_brazilian_values() -> None:
    result = _numeric_decimal_comma(pd.Series(["303079,16", "1.234,56", "0,00"]))
    assert result.tolist() == [303079.16, 1234.56, 0.0]


def test_radar_numeric_value_handles_2026_thousands_separator() -> None:
    source_2026 = pd.Series(["129.639", "3.020.306", "9", "0"])
    assert _radar_numeric_value(source_2026, "2026-07").tolist() == [
        129639,
        3020306,
        9,
        0,
    ]
    source_2025 = pd.Series(["129639", "3020306", "9"])
    assert _radar_numeric_value(source_2025, "2025-07").tolist() == [
        129639,
        3020306,
        9,
    ]


def test_parse_crosswalk_markdown_extracts_rows(tmp_path: Path) -> None:
    path = tmp_path / "crosswalk.md"
    path.write_text(
        "\n".join(
            [
                "| Grupo de afinidade Radar | Setor principal SBMI | Módulo | Status | Relação POF | Prioridade | Justificativa |",
                "|---|---|---|---|---|---|---|",
                "| Café | Bens Essenciais | Alimentação no domicílio | CORE | sim/alta | ALTA | exemplo |",
                "| Calçados | Bens Não Essenciais | Vestuário e calçados | CORE | parcial/alta | ALTA | exemplo |",
            ]
        ),
        encoding="utf-8",
    )
    frame = parse_crosswalk_markdown(path)
    assert frame["grupo_afinidade_final"].tolist() == ["Café", "Calçados"]
    assert frame["status_sbmi"].tolist() == ["CORE", "CORE"]