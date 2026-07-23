import pandas as pd

from sbmi.inbox_structure_triage import (
    build_schema_summary,
    build_similarity_candidates,
    build_source_summary,
    build_table_registry,
    source_from_path,
)


def sample_profiles() -> tuple[pd.DataFrame, pd.DataFrame]:
    sheets = pd.DataFrame(
        [
            {
                "relative_path": "raw/new_files/Federal/a.xlsx",
                "sheet_name": "dados",
                "sheet_index": 1,
                "schema_signature_sha256": "sig-a",
                "observed_nonempty_rows": 10,
                "observed_max_column": 3,
                "header_confidence_estimate": "HIGH",
                "year_min_observed": 2020,
                "year_max_observed": 2020,
            },
            {
                "relative_path": "raw/new_files/Federal/b.xlsx",
                "sheet_name": "dados",
                "sheet_index": 1,
                "schema_signature_sha256": "sig-a",
                "observed_nonempty_rows": 12,
                "observed_max_column": 3,
                "header_confidence_estimate": "HIGH",
                "year_min_observed": 2021,
                "year_max_observed": 2021,
            },
            {
                "relative_path": "raw/new_files/Municipal/c.xlsx",
                "sheet_name": "base",
                "sheet_index": 1,
                "schema_signature_sha256": "sig-c",
                "observed_nonempty_rows": 8,
                "observed_max_column": 4,
                "header_confidence_estimate": "MEDIUM",
                "year_min_observed": 2022,
                "year_max_observed": 2022,
            },
            {
                "relative_path": "raw/new_files/Estadual/d.xlsx",
                "sheet_name": "base",
                "sheet_index": 1,
                "schema_signature_sha256": "sig-d",
                "observed_nonempty_rows": 7,
                "observed_max_column": 2,
                "header_confidence_estimate": "HIGH",
                "year_min_observed": None,
                "year_max_observed": None,
            },
        ]
    )
    headers = {
        ("raw/new_files/Federal/a.xlsx", "dados", 1): ["ano", "municipio", "valor"],
        ("raw/new_files/Federal/b.xlsx", "dados", 1): ["ano", "municipio", "valor"],
        ("raw/new_files/Municipal/c.xlsx", "base", 1): [
            "ano",
            "municipio",
            "valor",
            "unidade",
        ],
        ("raw/new_files/Estadual/d.xlsx", "base", 1): ["codigo", "descricao"],
    }
    rows: list[dict[str, object]] = []
    for key, values in headers.items():
        relative_path, sheet_name, sheet_index = key
        for column_index, header in enumerate(values, start=1):
            rows.append(
                {
                    "relative_path": relative_path,
                    "sheet_name": sheet_name,
                    "sheet_index": sheet_index,
                    "column_index": column_index,
                    "header_normalized": header,
                }
            )
    return sheets, pd.DataFrame(rows)


def test_source_from_path() -> None:
    assert source_from_path("raw/new_files/Federal/a.xlsx") == "Federal"
    assert source_from_path("raw/fiscal/a.xlsx") == "(não identificada)"


def test_registry_classifies_exact_groups() -> None:
    sheets, columns = sample_profiles()
    registry = build_table_registry(sheets, columns)
    indexed = registry.set_index("relative_path")

    assert indexed.loc["raw/new_files/Federal/a.xlsx", "exact_schema_group_size"] == 2
    assert indexed.loc["raw/new_files/Federal/a.xlsx", "schema_status"] == "REPEATED_EXACT"
    assert indexed.loc["raw/new_files/Municipal/c.xlsx", "schema_status"] == "SINGLETON"
    assert indexed.loc["raw/new_files/Municipal/c.xlsx", "header_token_count"] == 4


def test_schema_and_source_summaries() -> None:
    sheets, columns = sample_profiles()
    registry = build_table_registry(sheets, columns)
    schemas = build_schema_summary(registry).set_index("schema_signature_sha256")
    sources = build_source_summary(registry).set_index("source_declared")

    assert schemas.loc["sig-a", "group_size"] == 2
    assert schemas.loc["sig-a", "sources"] == "Federal"
    assert schemas.loc["sig-a", "year_min_observed"] == 2020
    assert schemas.loc["sig-a", "year_max_observed"] == 2021
    assert sources.loc["Federal", "tables"] == 2
    assert sources.loc["Federal", "repeated_exact_tables"] == 2
    assert sources.loc["Municipal", "singleton_tables"] == 1


def test_similarity_candidates_exclude_exact_and_capture_partial() -> None:
    sheets, columns = sample_profiles()
    registry = build_table_registry(sheets, columns)
    candidates = build_similarity_candidates(registry)

    assert len(candidates) == 2
    pairs = {
        (row.left_path, row.right_path)
        for row in candidates.itertuples(index=False)
    }
    assert (
        "raw/new_files/Federal/a.xlsx",
        "raw/new_files/Municipal/c.xlsx",
    ) in pairs
    assert (
        "raw/new_files/Federal/b.xlsx",
        "raw/new_files/Municipal/c.xlsx",
    ) in pairs
    assert set(candidates["candidate_class"]) == {"PARTIAL_SCHEMA"}
