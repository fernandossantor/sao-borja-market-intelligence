from sbmi.demography_historical_values_cli import QUERIES


def test_demography_plan_is_small_and_scoped():
    assert {row["table_id"] for row in QUERIES} == {"156", "6579"}
    assert {row["municipality_code"] for row in QUERIES} == {"4318002"}
    assert all(row["classification_id"] == "" for row in QUERIES)
    assert all(row["category_ids"] == "" for row in QUERIES)
    assert all(row["url"].startswith("https://apisidra.ibge.gov.br/values/") for row in QUERIES)
    intervals = {row["table_id"]: (row["period_start"], row["period_end"]) for row in QUERIES}
    assert intervals == {"156": ("1991", "2010"), "6579": ("2001", "2025")}
