"""Seleção e identificação das fontes brutas do Censo 2022 de São Borja."""

from __future__ import annotations

from pathlib import PurePosixPath

import pandas as pd

from sbmi.base_territorial_coverage import normalize_text

REQUIRED_COLUMNS = {
    "relative_path",
    "file_name",
    "extension",
    "is_folder",
    "size_bytes",
    "drive_file_id",
    "sha256_checksum",
}
EXPECTED_CENSUS_SOURCE_FILES = 17


def _truthy(value: object) -> bool:
    return value is True or str(value).strip().casefold() in {
        "true",
        "1",
        "yes",
    }


def census_topic_key(value: object) -> str:
    """Extrai uma chave temática estável de fonte ou produto censitário."""
    normalized = normalize_text(value)
    removable = (
        "censo 2022",
        "sao borja rs",
        "sheet1",
        "xlsx",
        "parquet",
        "csv",
    )
    for token in removable:
        normalized = normalized.replace(token, " ")
    return " ".join(normalized.split())


def select_census_source_files(inventory: pd.DataFrame) -> pd.DataFrame:
    """Seleciona as planilhas brutas dedicadas ao Censo 2022 municipal."""
    missing = REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no inventário: " f"{sorted(missing)}"
        )

    frame = inventory.copy()
    frame["relative_path"] = frame["relative_path"].fillna("").astype(str)
    frame["file_name"] = frame["file_name"].fillna("").astype(str)
    frame["extension"] = (
        frame["extension"].fillna("").astype(str).str.lower().str.lstrip(".")
    )
    frame["is_folder_normalized"] = frame["is_folder"].map(_truthy)
    normalized_names = frame["file_name"].map(normalize_text)
    raw_path = frame["relative_path"].str.startswith("raw/")
    dedicated_name = (
        normalized_names.str.contains("censo 2022", regex=False)
        & normalized_names.str.contains("sao borja rs", regex=False)
    )
    selected = frame.loc[
        raw_path
        & dedicated_name
        & frame["extension"].eq("xlsx")
        & ~frame["is_folder_normalized"]
    ].copy()
    if selected.empty:
        raise ValueError("Nenhuma fonte bruta do Censo 2022 foi localizada.")
    if selected["relative_path"].duplicated().any():
        duplicated = sorted(
            selected.loc[
                selected["relative_path"].duplicated(False),
                "relative_path",
            ].unique()
        )
        raise ValueError(f"Caminhos censitários duplicados: {duplicated}")

    selected["topic_key"] = selected["file_name"].map(census_topic_key)
    if selected["topic_key"].duplicated().any():
        duplicated = sorted(
            selected.loc[
                selected["topic_key"].duplicated(False),
                "topic_key",
            ].unique()
        )
        raise ValueError(f"Chaves temáticas censitárias duplicadas: {duplicated}")
    selected["source_stage"] = "raw"
    selected["source_role"] = "DEDICATED_CENSUS_SOURCE"
    selected["nature"] = "observed_and_calculated"
    columns = [
        "topic_key",
        "relative_path",
        "file_name",
        "extension",
        "size_bytes",
        "drive_file_id",
        "sha256_checksum",
        "source_stage",
        "source_role",
        "nature",
    ]
    return selected[columns].sort_values("topic_key").reset_index(drop=True)


def selected_source_paths(selected: pd.DataFrame) -> tuple[str, ...]:
    """Converte a seleção validada em caminhos exatos para captura."""
    if "relative_path" not in selected.columns or selected.empty:
        raise ValueError("Seleção censitária vazia ou sem relative_path.")
    return tuple(
        PurePosixPath(str(value).strip("/")).as_posix()
        for value in selected["relative_path"]
    )
