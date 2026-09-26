from __future__ import annotations

import pandas as pd

from sbmi.public_market_series_analysis import (
    build_dfe_monthly_panel,
    build_taxonomy_gap_prefix,
)


def test_dfe_monthly_panel_marks_partial_month_and_yoy() -> None:
    rows = []
    for year in [2024, 2025, 2026]:
        for month in [1, 2]:
            rows.append(
                {
                    "ano_mes": f"{year}-{month:02d}",
                    "modelo_dfe": "NFC-e",
                    "qtde_dfe": 100 * (year - 2023),
                    "vlr_total_dfe": 1000.0 * (year - 2023),
                    "periodo_parcial": False,
                }
            )
    rows.append(
        {
            "ano_mes": "2026-09",
            "modelo_dfe": "NFC-e",
            "qtde_dfe": 50,
            "vlr_total_dfe": 500.0,
            "periodo_parcial": True,
        }
    )
    frame = pd.DataFrame(rows)
    panel = build_dfe_monthly_panel(frame)
    jan_2026 = panel.loc[panel["ano_mes"].eq("2026-01")].iloc[0]
    assert round(jan_2026["qtde_yoy_pct"], 6) == 50.0
    sep_2026 = panel.loc[panel["ano_mes"].eq("2026-09")].iloc[0]
    assert sep_2026["status_comparabilidade"] == "mes_parcial"
    assert pd.isna(sep_2026["qtde_yoy_pct"])
    assert pd.isna(sep_2026["indice_qtde_base_media_2024"])


def test_taxonomy_gap_prefix_does_not_impute_groups() -> None:
    frame = pd.DataFrame(
        {
            "series": ["radar_composicao_mercado"] * 3,
            "ncm8": ["29000001", "29000002", "61000001"],
            "rows": [10, 20, 5],
            "valor_publicado": [100.0, 200.0, 10.0],
        }
    )
    summary, meta = build_taxonomy_gap_prefix(frame)
    row29 = summary.loc[summary["prefixo2"].eq("29")].iloc[0]
    assert row29["ncm8_unicos"] == 2
    assert round(meta["composition_prefix29_pct_unmapped_value"], 6) == round(300 / 310 * 100, 6)