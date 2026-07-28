from pathlib import Path

import pandas as pd
import pytest

from sbmi.demography_census_comparison import (
    CensusContentComparisonResult,
    compare_census_lineage,
    compare_dataset_pair,
    write_census_comparison,
)


def _write_pair(
    tmp_path: Path,
    raw: pd.DataFrame,
    processed: pd.DataFrame,
) -> tuple[Path, Path]:
    raw_path = tmp_path / "raw.xlsx"
    processed_path = tmp_path / "processed.parquet"
    raw.to_excel(raw_path, index=False)
    processed.to_parquet(processed_path, index=False)
    return raw_path, processed_path


def test_exact_after_header_and_numeric_canonicalization(tmp_path: Path) -> None:
    raw_path, processed_path = _write_pair(
        tmp_path,
        pd.DataFrame(
            {
                "Característica": ["Rede de água", "Coleta de lixo"],
                "Possui(%)": ["86,64", "91,39"],
                "Código do Município": [4318002, 4318002],
            }
        ),
        pd.DataFrame(
            {
                "caracteristica": ["Rede de água", "Coleta de lixo"],
                "possui": [86.64, 91.39],
                "codigo_do_municipio": [4318002, 4318002],
            }
        ),
    )

    dataset, columns, differences = compare_dataset_pair(
        dataset_identity="domicilios",
        raw_path=raw_path,
        processed_path=processed_path,
        raw_relative_path="raw/social/domicilios.xlsx",
        processed_relative_path="processed/social/domicilios.parquet",
    )

    assert dataset["content_equivalence_status"] == "EXACT_AFTER_CANONICALIZATION"
    assert dataset["header_set_match"]
    assert dataset["row_count_match"]
    assert not differences
    assert all(record["column_values_match"] for record in columns)


def test_row_order_difference_is_not_reported_as_exact(tmp_path: Path) -> None:
    raw = pd.DataFrame({"categoria": ["A", "B"], "pessoas": [10, 20]})
    processed = raw.iloc[::-1].reset_index(drop=True)
    raw_path, processed_path = _write_pair(tmp_path, raw, processed)

    dataset, _, differences = compare_dataset_pair(
        dataset_identity="ordem",
        raw_path=raw_path,
        processed_path=processed_path,
        raw_relative_path="raw/social/ordem.xlsx",
        processed_relative_path="processed/social/ordem.parquet",
    )

    assert dataset["content_equivalence_status"] == "ROW_ORDER_DIFFERS_ONLY"
    assert dataset["canonical_row_multiset_match"]
    assert not dataset["canonical_sequence_match"]
    assert differences


def test_schema_mismatch_remains_explicit(tmp_path: Path) -> None:
    raw_path, processed_path = _write_pair(
        tmp_path,
        pd.DataFrame({"categoria": ["A"], "pessoas": [10]}),
        pd.DataFrame({"categoria": ["A"], "percentual": [10]}),
    )

    dataset, columns, _ = compare_dataset_pair(
        dataset_identity="schema",
        raw_path=raw_path,
        processed_path=processed_path,
        raw_relative_path="raw/social/schema.xlsx",
        processed_relative_path="processed/social/schema.parquet",
    )

    assert dataset["content_equivalence_status"] == "SCHEMA_MISMATCH"
    assert not dataset["header_set_match"]
    by_name = {record["column"]: record for record in columns}
    assert by_name["pessoas"]["raw_present"]
    assert not by_name["pessoas"]["processed_present"]


def test_compare_lineage_uses_snapshot_paths(tmp_path: Path) -> None:
    raw_root = tmp_path / "raw_snapshot"
    derived_root = tmp_path / "derived_snapshot"
    raw_file = raw_root / "raw" / "social" / "Censo 2022 - Sexo.xlsx"
    processed_file = (
        derived_root / "processed" / "social" / "Censo 2022 - Sexo_Sheet1.parquet"
    )
    raw_file.parent.mkdir(parents=True)
    processed_file.parent.mkdir(parents=True)
    frame = pd.DataFrame({"Sexo": ["Mulheres", "Homens"], "Pessoas": [30, 29]})
    frame.to_excel(raw_file, index=False)
    frame.rename(columns={"Sexo": "sexo", "Pessoas": "pessoas"}).to_parquet(
        processed_file,
        index=False,
    )
    lineage = pd.DataFrame(
        [
            {
                "dataset_identity": "sexo",
                "raw_source_count": 1,
                "processed_product_count": 1,
                "raw_source_paths": "raw/social/Censo 2022 - Sexo.xlsx",
                "processed_product_paths": (
                    "processed/social/Censo 2022 - Sexo_Sheet1.parquet"
                ),
                "lineage_match_status": "MATCHED_ONE_TO_ONE_BY_NAME",
            }
        ]
    )

    result = compare_census_lineage(
        lineage,
        raw_snapshot_root=raw_root,
        derived_snapshot_root=derived_root,
    )
    summary = result.summary.set_index("indicator")

    assert len(result.datasets) == 1
    assert int(summary.loc["exact_after_canonicalization", "value"]) == 1
    assert int(summary.loc["conceptually_validated_datasets", "value"]) == 0


def test_write_comparison_is_atomic_and_refuses_overwrite(tmp_path: Path) -> None:
    result = CensusContentComparisonResult(
        datasets=pd.DataFrame([{"dataset_identity": "sexo"}]),
        columns=pd.DataFrame([{"dataset_identity": "sexo", "column": "sexo"}]),
        differences=pd.DataFrame(),
        summary=pd.DataFrame(
            [("lineage_pairs_compared", 1, "calculated")],
            columns=["indicator", "value", "nature"],
        ),
    )
    target = tmp_path / "comparison"

    written = write_census_comparison(result, target)

    assert written == target.resolve()
    assert (target / "demography_census_dataset_comparison.csv").is_file()
    assert (target / "demography_census_column_comparison.csv").is_file()
    assert (target / "demography_census_cell_differences.csv").is_file()
    assert (target / "demography_census_comparison_summary.csv").is_file()
    with pytest.raises(FileExistsError):
        write_census_comparison(result, target)
