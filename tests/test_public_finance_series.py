import json

import pytest

from sbmi.public_finance_series import curate_public_finance_series


def _write(p, table, rows):
    p.write_text(
        json.dumps({"annotations": {"source_name": "SICONFI", "table": table}, "data": rows}),
        encoding="utf-8",
    )


def test_curates_without_hierarchy_sum(tmp_path):
    s = tmp_path / "s"
    s.mkdir()
    _write(
        s / "r.json",
        "Receitas",
        [
            {"Municipality ID": 4318002, "Year": 2019, "Revenue Value": 10},
            {"Municipality ID": 4318002, "Year": 2020, "Revenue Value": 11},
            {"Municipality ID": 4318002, "Year": 2021, "Revenue Value": 12},
            {"Municipality ID": 4318002, "Year": 2023, "Revenue Value": 13},
            {"Municipality ID": 4318002, "Year": 2024, "Revenue Value": 14},
            {"Municipality ID": 4318002, "Year": 2025, "Revenue Value": 15},
        ],
    )
    _write(
        s / "c.json",
        "Despesas",
        [
            {"Expense ID": "DO4.4.00.00.00.00", "Expense Value": 1, "Year": 2025},
            {"Expense ID": "DO4.6.00.00.00.00", "Expense Value": 2, "Year": 2025},
        ],
    )
    _write(
        s / "d.json",
        "Despesas",
        [
            {"Expense ID": c, "Expense Value": 1, "Year": 2025}
            for c in [
                "DO3.0.00.00.00.00",
                "DO3.1.00.00.00.00",
                "DO3.2.00.00.00.00",
                "DO3.3.00.00.00.00",
            ]
        ],
    )
    _write(
        s / "rc.json",
        "Receitas",
        [
            {"Revenue ID": c, "Revenue Value": 1, "Year": 2025}
            for c in ["RO1.0.0.0.00.0.0", "RO1.7.0.0.00.0.0", "RO1.9.0.0.00.0.0"]
        ],
    )
    _write(
        s / "t.json",
        "Receitas",
        [
            {"Revenue ID": c, "Revenue Value": 1, "Year": 2025}
            for c in [
                "RO1.7.1.0.00.0.0",
                "RO1.7.2.4.00.0.0",
                "RO1.7.5.0.00.0.0",
                "RO2.4.1.0.00.0.0",
                "RO2.4.2.2.00.0.0",
            ]
        ],
    )
    sources = dict(
        zip(
            [
                "revenue_total",
                "capital_expense",
                "current_expense",
                "revenue_categories",
                "transfer_categories",
            ],
            [s / "r.json", s / "c.json", s / "d.json", s / "rc.json", s / "t.json"],
            strict=True,
        )
    )
    roots = {x: tmp_path / x for x in ("staging", "curated", "exports", "audit")}
    result = curate_public_finance_series(sources=sources, roots=roots, execution_id="run")
    assert len(result.values) == 20
    assert result.values.indicator_id.nunique() == 15
    with pytest.raises(FileExistsError):
        curate_public_finance_series(sources=sources, roots=roots, execution_id="run")
