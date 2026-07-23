"""Auditoria da caixa de entrada ``raw/new_files`` por metadados do Drive."""

from __future__ import annotations

from pathlib import PurePosixPath

import pandas as pd

DEFAULT_INBOX_PREFIX = "raw/new_files"

REQUIRED_COLUMNS = {
    "relative_path",
    "is_folder",
    "size_bytes",
    "sha256_checksum",
}

CLASS_UNIQUE = "UNIQUE_BY_SHA256"
CLASS_MISSING = "MISSING_SHA256"
CLASS_OUTSIDE = "EXACT_DUPLICATE_OUTSIDE_INBOX"
CLASS_WITHIN = "EXACT_DUPLICATE_WITHIN_INBOX"


def validate_inventory(inventory: pd.DataFrame) -> None:
    """Valida as colunas mínimas necessárias para a auditoria da caixa de entrada."""
    missing = REQUIRED_COLUMNS.difference(inventory.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")


def _folder_mask(series: pd.Series) -> pd.Series:
    """Converte valores booleanos ou textuais de ``is_folder`` com segurança."""
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False).astype(bool)

    normalized = series.fillna(False).astype(str).str.strip().str.lower()
    truthy = {"true", "1", "yes", "sim"}
    falsy = {"false", "0", "no", "não", "nao", "", "none", "nan"}
    unknown = set(normalized.unique()).difference(truthy | falsy)
    if unknown:
        raise ValueError(f"Valores inválidos em is_folder: {sorted(unknown)}")
    return normalized.isin(truthy)


def _normalized_prefix(prefix: str) -> str:
    value = prefix.strip().strip("/")
    if not value:
        raise ValueError("O prefixo da caixa de entrada não pode estar vazio.")
    if any(part in {".", ".."} for part in PurePosixPath(value).parts):
        raise ValueError("O prefixo da caixa de entrada não pode conter '.' ou '..'.")
    return PurePosixPath(value).as_posix()


def _inbox_mask(paths: pd.Series, prefix: str) -> pd.Series:
    normalized = _normalized_prefix(prefix)
    text = paths.fillna("").astype(str).str.strip("/")
    return text.eq(normalized) | text.str.startswith(f"{normalized}/")


def _source_from_path(path: object, prefix: str) -> str:
    normalized = _normalized_prefix(prefix)
    value = str(path or "").strip("/")
    if value == normalized:
        return "(raiz)"
    remainder = value.removeprefix(f"{normalized}/")
    if not remainder or remainder == value:
        return "(fora da caixa)"
    return PurePosixPath(remainder).parts[0]


def classify_inbox_files(
    inventory: pd.DataFrame,
    inbox_prefix: str = DEFAULT_INBOX_PREFIX,
) -> pd.DataFrame:
    """Classifica arquivos da caixa de entrada sem inferir duplicidade conceitual."""
    validate_inventory(inventory)
    prefix = _normalized_prefix(inbox_prefix)

    frame = inventory.copy()
    folder_mask = _folder_mask(frame["is_folder"])
    frame = frame.loc[~folder_mask].copy()
    frame["relative_path"] = frame["relative_path"].fillna("").astype(str)
    frame["sha256_checksum"] = (
        frame["sha256_checksum"].fillna("").astype(str).str.strip()
    )
    frame["size_bytes"] = pd.to_numeric(frame["size_bytes"], errors="coerce")
    frame["is_inbox"] = _inbox_mask(frame["relative_path"], prefix)

    inbox = frame.loc[frame["is_inbox"]].copy()
    output_columns = [
        "relative_path",
        "inbox_source",
        "size_bytes",
        "sha256_checksum",
        "global_group_size",
        "inbox_group_size",
        "outside_group_size",
        "audit_class",
    ]
    if inbox.empty:
        return pd.DataFrame(columns=output_columns)

    checksummed = frame.loc[frame["sha256_checksum"].ne("")].copy()
    global_counts = checksummed.groupby("sha256_checksum")["relative_path"].size()
    inbox_counts = (
        checksummed.loc[checksummed["is_inbox"]]
        .groupby("sha256_checksum")["relative_path"]
        .size()
    )

    inbox["inbox_source"] = inbox["relative_path"].map(
        lambda value: _source_from_path(value, prefix)
    )
    inbox["global_group_size"] = (
        inbox["sha256_checksum"].map(global_counts).fillna(0).astype(int)
    )
    inbox["inbox_group_size"] = (
        inbox["sha256_checksum"].map(inbox_counts).fillna(0).astype(int)
    )
    inbox["outside_group_size"] = (
        inbox["global_group_size"] - inbox["inbox_group_size"]
    )

    inbox["audit_class"] = CLASS_UNIQUE
    inbox.loc[inbox["sha256_checksum"].eq(""), "audit_class"] = CLASS_MISSING
    inbox.loc[inbox["outside_group_size"].gt(0), "audit_class"] = CLASS_OUTSIDE
    inbox.loc[
        inbox["outside_group_size"].eq(0)
        & inbox["inbox_group_size"].gt(1)
        & inbox["sha256_checksum"].ne(""),
        "audit_class",
    ] = CLASS_WITHIN

    return inbox[output_columns].sort_values(
        ["audit_class", "inbox_source", "relative_path"]
    ).reset_index(drop=True)


def inbox_summary(classified: pd.DataFrame) -> pd.DataFrame:
    """Produz indicadores observados e calculados da caixa de entrada."""
    required = {
        "relative_path",
        "size_bytes",
        "sha256_checksum",
        "audit_class",
    }
    missing = required.difference(classified.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    checksum = classified["sha256_checksum"].fillna("").astype(str).str.strip()
    outside = classified.loc[classified["audit_class"].eq(CLASS_OUTSIDE)]
    within = classified.loc[classified["audit_class"].eq(CLASS_WITHIN)]

    records = [
        ("inbox_files", int(len(classified)), "observed"),
        (
            "inbox_known_bytes",
            int(pd.to_numeric(classified["size_bytes"], errors="coerce").fillna(0).sum()),
            "calculated",
        ),
        ("inbox_files_with_sha256", int(checksum.ne("").sum()), "observed"),
        ("inbox_files_without_sha256", int(checksum.eq("").sum()), "calculated"),
        (
            "unique_by_sha256_rows",
            int(classified["audit_class"].eq(CLASS_UNIQUE).sum()),
            "calculated",
        ),
        ("exact_duplicate_outside_rows", int(len(outside)), "calculated"),
        (
            "exact_duplicate_outside_groups",
            int(outside["sha256_checksum"].nunique()) if not outside.empty else 0,
            "calculated",
        ),
        ("exact_duplicate_within_rows", int(len(within)), "calculated"),
        (
            "exact_duplicate_within_groups",
            int(within["sha256_checksum"].nunique()) if not within.empty else 0,
            "calculated",
        ),
    ]
    return pd.DataFrame(records, columns=["indicator", "value", "measurement_type"])


def inbox_source_summary(classified: pd.DataFrame) -> pd.DataFrame:
    """Resume volume e classes de auditoria por origem declarada no caminho."""
    required = {"inbox_source", "relative_path", "size_bytes", "audit_class"}
    missing = required.difference(classified.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {sorted(missing)}")

    if classified.empty:
        return pd.DataFrame(
            columns=[
                "inbox_source",
                "files",
                "known_bytes",
                "unique_by_sha256_rows",
                "exact_duplicate_outside_rows",
                "exact_duplicate_within_rows",
                "missing_sha256_rows",
            ]
        )

    frame = classified.copy()
    frame["known_bytes"] = pd.to_numeric(frame["size_bytes"], errors="coerce").fillna(0)
    frame["unique_by_sha256_rows"] = frame["audit_class"].eq(CLASS_UNIQUE).astype(int)
    frame["exact_duplicate_outside_rows"] = frame["audit_class"].eq(CLASS_OUTSIDE).astype(int)
    frame["exact_duplicate_within_rows"] = frame["audit_class"].eq(CLASS_WITHIN).astype(int)
    frame["missing_sha256_rows"] = frame["audit_class"].eq(CLASS_MISSING).astype(int)

    result = (
        frame.groupby("inbox_source", dropna=False)
        .agg(
            files=("relative_path", "size"),
            known_bytes=("known_bytes", "sum"),
            unique_by_sha256_rows=("unique_by_sha256_rows", "sum"),
            exact_duplicate_outside_rows=("exact_duplicate_outside_rows", "sum"),
            exact_duplicate_within_rows=("exact_duplicate_within_rows", "sum"),
            missing_sha256_rows=("missing_sha256_rows", "sum"),
        )
        .reset_index()
        .sort_values(["files", "known_bytes"], ascending=[False, False])
    )

    numeric_columns = [column for column in result.columns if column != "inbox_source"]
    for column in numeric_columns:
        result[column] = result[column].astype(int)
    return result.reset_index(drop=True)
