import pandas as pd
import pytest

from sbmi.demography_census_sources import (
    census_topic_key,
    select_census_source_files,
    selected_source_paths,
)


def _inventory() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "relative_path": (
                    "raw/social/Censo 2022 - População por sexo - "
                    "São Borja (RS).xlsx"
                ),
                "file_name": (
                    "Censo 2022 - População por sexo - São Borja (RS).xlsx"
                ),
                "extension": "xlsx",
                "is_folder": False,
                "size_bytes": 15050,
                "drive_file_id": "raw-sex",
                "sha256_checksum": "abc",
            },
            {
                "relative_path": (
                    "processed/social/Censo 2022 - População por sexo - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "file_name": (
                    "Censo 2022 - População por sexo - "
                    "São Borja (RS)_Sheet1.parquet"
                ),
                "extension": "parquet",
                "is_folder": False,
                "size_bytes": 1000,
                "drive_file_id": "processed-sex",
                "sha256_checksum": "def",
            },
            {
                "relative_path": "raw/social/outro.xlsx",
                "file_name": "outro.xlsx",
                "extension": "xlsx",
                "is_folder": False,
                "size_bytes": 100,
                "drive_file_id": "other",
                "sha256_checksum": "ghi",
            },
        ]
    )


def test_topic_key_normalizes_source_and_processed_names() -> None:
    raw = "Censo 2022 - População por sexo - São Borja (RS).xlsx"
    processed = (
        "Censo 2022 - População por sexo - São Borja (RS)_Sheet1.parquet"
    )

    assert census_topic_key(raw) == "populacao por sexo"
    assert census_topic_key(raw) == census_topic_key(processed)


def test_selects_only_dedicated_raw_xlsx_sources() -> None:
    selected = select_census_source_files(_inventory())

    assert len(selected) == 1
    assert selected.iloc[0]["topic_key"] == "populacao por sexo"
    assert selected.iloc[0]["source_role"] == "DEDICATED_CENSUS_SOURCE"
    assert selected_source_paths(selected) == (
        "raw/social/Censo 2022 - População por sexo - São Borja (RS).xlsx",
    )


def test_rejects_duplicate_topic_keys() -> None:
    inventory = pd.concat(
        [
            _inventory(),
            pd.DataFrame(
                [
                    {
                        "relative_path": (
                            "raw/copy/Censo 2022 - População por sexo - "
                            "São Borja (RS).xlsx"
                        ),
                        "file_name": (
                            "Censo 2022 - População por sexo - "
                            "São Borja (RS).xlsx"
                        ),
                        "extension": "xlsx",
                        "is_folder": False,
                        "size_bytes": 15050,
                        "drive_file_id": "raw-sex-copy",
                        "sha256_checksum": "abc",
                    }
                ]
            ),
        ],
        ignore_index=True,
    )

    with pytest.raises(ValueError, match="Chaves temáticas censitárias duplicadas"):
        select_census_source_files(inventory)
