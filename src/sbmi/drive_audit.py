"""Auditoria agregada do inventário de metadados do Google Drive."""

from __future__ import annotations

from pathlib import PurePosixPath

import pandas as pd

REQUIRED_COLUMNS = {
    "relative_path",
    "extension",
    "is_folder",
    "size_bytes",
    "sha256_checksum",
}


def validate_drive_inventory(inventory: pd.DataFrame) -> None:
    """Valida o esquema mínimo necessário para a auditoria."""
    missing = REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")


def _top_level(path: object) -> str:
    value = str(path or "").strip("/")
    if not value:
        return "(raiz)"
    return PurePosixPath(value).parts[0]


def exact_duplicate_candidates(inventory: pd.DataFrame) -> pd.DataFrame:
    """Lista arquivos com SHA-256 repetido sem recomendar exclusão."""
    validate_drive_inventory(inventory)
    files = inventory.loc[~inventory["is_folder"].astype(bool)].copy()
    checksum = files["sha256_checksum"].fillna("").astype(str).str.strip()
    files = files.loc[checksum.ne("")].copy()
    files["sha256_checksum"] = checksum.loc[files.index]

    duplicated = files.loc[
        files.duplicated("sha256_checksum", keep=False),
        ["sha256_checksum", "relative_path", "size_bytes"],
    ].copy()

    if duplicated.empty:
        return pd.DataFrame(
            columns=[
                "sha256_checksum",
                "group_size",
                "relative_path",
                "size_bytes",
                "duplicate_class",
            ]
        )

    group_sizes = duplicated.groupby("sha256_checksum")["relative_path"].transform("size")
    duplicated.insert(1, "group_size", group_sizes.astype(int))
    duplicated["duplicate_class"] = "EXACT_DUPLICATE"
    return duplicated.sort_values(["sha256_checksum", "relative_path"]).reset_index(drop=True)


def inventory_summary(inventory: pd.DataFrame) -> pd.DataFrame:
    """Produz indicadores observados e calculados do inventário."""
    validate_drive_inventory(inventory)
    is_folder = inventory["is_folder"].astype(bool)
    files = inventory.loc[~is_folder]
    checksum_available = files["sha256_checksum"].fillna("").astype(str).str.strip().ne("")
    duplicates = exact_duplicate_candidates(inventory)

    duplicate_groups = (
        int(duplicates["sha256_checksum"].nunique()) if not duplicates.empty else 0
    )

    records = [
        ("entries", int(len(inventory)), "observed"),
        ("folders", int(is_folder.sum()), "observed"),
        ("files", int((~is_folder).sum()), "observed"),
        ("known_bytes", int(inventory["size_bytes"].fillna(0).sum()), "calculated"),
        ("missing_size", int(inventory["size_bytes"].isna().sum()), "observed"),
        ("files_with_sha256", int(checksum_available.sum()), "observed"),
        ("files_without_sha256", int((~checksum_available).sum()), "calculated"),
        ("exact_duplicate_groups", duplicate_groups, "calculated"),
        ("exact_duplicate_rows", int(len(duplicates)), "calculated"),
    ]
    return pd.DataFrame(records, columns=["indicator", "value", "measurement_type"])


def top_level_summary(inventory: pd.DataFrame) -> pd.DataFrame:
    """Resume quantidade e volume por pasta de primeiro nível."""
    validate_drive_inventory(inventory)
    frame = inventory.copy()
    frame["top_level"] = frame["relative_path"].map(_top_level)
    frame["is_file"] = ~frame["is_folder"].astype(bool)
    frame["known_bytes"] = frame["size_bytes"].fillna(0)

    result = (
        frame.groupby("top_level", dropna=False)
        .agg(
            entries=("relative_path", "size"),
            folders=("is_folder", "sum"),
            files=("is_file", "sum"),
            known_bytes=("known_bytes", "sum"),
            missing_size=("size_bytes", lambda series: int(series.isna().sum())),
        )
        .reset_index()
        .sort_values(["known_bytes", "entries"], ascending=[False, False])
    )

    for column in ["entries", "folders", "files", "known_bytes", "missing_size"]:
        result[column] = result[column].astype(int)
    return result.reset_index(drop=True)


def extension_summary(inventory: pd.DataFrame) -> pd.DataFrame:
    """Resume quantidade e volume dos arquivos por extensão."""
    validate_drive_inventory(inventory)
    files = inventory.loc[~inventory["is_folder"].astype(bool)].copy()
    normalized = files["extension"].fillna("").astype(str).str.lower().str.strip().str.lstrip(".")
    files["extension_group"] = normalized.mask(normalized.eq(""), "(sem extensão)")
    files["known_bytes"] = files["size_bytes"].fillna(0)

    result = (
        files.groupby("extension_group", dropna=False)
        .agg(
            files=("relative_path", "size"),
            known_bytes=("known_bytes", "sum"),
            missing_size=("size_bytes", lambda series: int(series.isna().sum())),
        )
        .reset_index()
        .sort_values(["files", "known_bytes"], ascending=[False, False])
    )

    for column in ["files", "known_bytes", "missing_size"]:
        result[column] = result[column].astype(int)
    return result.reset_index(drop=True)
