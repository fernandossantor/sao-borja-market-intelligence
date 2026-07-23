"""Triagem estrutural dos perfis produzidos para ``raw/new_files``."""

from __future__ import annotations

from dataclasses import dataclass
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import PurePosixPath

import pandas as pd

TABLE_KEY = ["relative_path", "sheet_name", "sheet_index"]
REQUIRED_SHEET_COLUMNS = {
    "relative_path",
    "sheet_name",
    "sheet_index",
    "schema_signature_sha256",
    "observed_nonempty_rows",
    "observed_max_column",
    "header_confidence_estimate",
    "year_min_observed",
    "year_max_observed",
}
REQUIRED_COLUMN_COLUMNS = {
    "relative_path",
    "sheet_name",
    "sheet_index",
    "column_index",
    "header_normalized",
}


@dataclass(frozen=True)
class StructureTriageResult:
    table_registry: pd.DataFrame
    schema_summary: pd.DataFrame
    source_summary: pd.DataFrame
    similarity_candidates: pd.DataFrame


def _validate_columns(frame: pd.DataFrame, required: set[str], name: str) -> None:
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes em {name}: {sorted(missing)}")


def source_from_path(value: object) -> str:
    """Extrai a origem declarada logo abaixo de ``raw/new_files``."""
    parts = PurePosixPath(str(value or "").strip("/")).parts
    if len(parts) >= 3 and parts[0:2] == ("raw", "new_files"):
        return parts[2]
    return "(não identificada)"


def _header_sequences(columns: pd.DataFrame) -> dict[tuple[object, ...], tuple[str, ...]]:
    ordered = columns.copy()
    ordered["column_index"] = pd.to_numeric(ordered["column_index"], errors="raise")
    ordered["header_normalized"] = (
        ordered["header_normalized"].fillna("").astype(str).str.strip()
    )
    ordered = ordered.sort_values(TABLE_KEY + ["column_index"])

    result: dict[tuple[object, ...], tuple[str, ...]] = {}
    for key, group in ordered.groupby(TABLE_KEY, dropna=False, sort=False):
        normalized_key = key if isinstance(key, tuple) else (key,)
        result[normalized_key] = tuple(group["header_normalized"].tolist())
    return result


def build_table_registry(sheets: pd.DataFrame, columns: pd.DataFrame) -> pd.DataFrame:
    """Constrói um registro por tabela com grupo estrutural e origem declarada."""
    _validate_columns(sheets, REQUIRED_SHEET_COLUMNS, "sheet_profile")
    _validate_columns(columns, REQUIRED_COLUMN_COLUMNS, "column_profile")

    registry = sheets.copy()
    registry["source_declared"] = registry["relative_path"].map(source_from_path)
    registry["schema_signature_sha256"] = (
        registry["schema_signature_sha256"].fillna("").astype(str).str.strip()
    )

    nonempty_signatures = registry.loc[
        registry["schema_signature_sha256"].ne(""), "schema_signature_sha256"
    ]
    counts = nonempty_signatures.value_counts()
    registry["exact_schema_group_size"] = (
        registry["schema_signature_sha256"].map(counts).fillna(0).astype(int)
    )
    registry["schema_status"] = "NO_SIGNATURE"
    registry.loc[registry["exact_schema_group_size"].eq(1), "schema_status"] = "SINGLETON"
    registry.loc[registry["exact_schema_group_size"].gt(1), "schema_status"] = (
        "REPEATED_EXACT"
    )

    sequences = _header_sequences(columns)
    registry["header_sequence"] = [
        "|".join(sequences.get(tuple(row), ()))
        for row in registry[TABLE_KEY].itertuples(index=False, name=None)
    ]
    registry["header_token_count"] = registry["header_sequence"].map(
        lambda value: sum(bool(token) for token in str(value).split("|"))
    )

    selected = [
        "relative_path",
        "source_declared",
        "sheet_name",
        "sheet_index",
        "observed_nonempty_rows",
        "observed_max_column",
        "header_confidence_estimate",
        "year_min_observed",
        "year_max_observed",
        "schema_signature_sha256",
        "exact_schema_group_size",
        "schema_status",
        "header_token_count",
        "header_sequence",
    ]
    return registry[selected].sort_values(
        ["exact_schema_group_size", "source_declared", "relative_path", "sheet_index"],
        ascending=[False, True, True, True],
    ).reset_index(drop=True)


def build_schema_summary(registry: pd.DataFrame) -> pd.DataFrame:
    """Resume cada assinatura estrutural observada."""
    eligible = registry.loc[registry["schema_signature_sha256"].ne("")].copy()
    if eligible.empty:
        return pd.DataFrame(
            columns=[
                "schema_signature_sha256",
                "group_size",
                "sources_count",
                "sources",
                "rows_min_observed",
                "rows_max_observed",
                "columns_min_observed",
                "columns_max_observed",
                "year_min_observed",
                "year_max_observed",
            ]
        )

    records: list[dict[str, object]] = []
    for signature, group in eligible.groupby("schema_signature_sha256", sort=False):
        sources = sorted(set(group["source_declared"].astype(str)))
        year_min = pd.to_numeric(group["year_min_observed"], errors="coerce")
        year_max = pd.to_numeric(group["year_max_observed"], errors="coerce")
        records.append(
            {
                "schema_signature_sha256": signature,
                "group_size": int(len(group)),
                "sources_count": len(sources),
                "sources": "|".join(sources),
                "rows_min_observed": int(group["observed_nonempty_rows"].min()),
                "rows_max_observed": int(group["observed_nonempty_rows"].max()),
                "columns_min_observed": int(group["observed_max_column"].min()),
                "columns_max_observed": int(group["observed_max_column"].max()),
                "year_min_observed": int(year_min.min()) if year_min.notna().any() else None,
                "year_max_observed": int(year_max.max()) if year_max.notna().any() else None,
            }
        )
    return pd.DataFrame(records).sort_values(
        ["group_size", "sources", "schema_signature_sha256"],
        ascending=[False, True, True],
    ).reset_index(drop=True)


def build_source_summary(registry: pd.DataFrame) -> pd.DataFrame:
    """Resume tabelas e assinaturas por origem declarada."""
    frame = registry.copy()
    frame["is_repeated"] = frame["schema_status"].eq("REPEATED_EXACT").astype(int)
    frame["is_singleton"] = frame["schema_status"].eq("SINGLETON").astype(int)
    return (
        frame.groupby("source_declared", dropna=False)
        .agg(
            tables=("relative_path", "size"),
            files=("relative_path", "nunique"),
            exact_schema_signatures=("schema_signature_sha256", "nunique"),
            repeated_exact_tables=("is_repeated", "sum"),
            singleton_tables=("is_singleton", "sum"),
            rows_observed=("observed_nonempty_rows", "sum"),
        )
        .reset_index()
        .sort_values(["tables", "source_declared"], ascending=[False, True])
        .reset_index(drop=True)
    )


def _tokens(sequence: object) -> tuple[str, ...]:
    return tuple(token for token in str(sequence or "").split("|") if token)


def build_similarity_candidates(
    registry: pd.DataFrame,
    *,
    minimum_jaccard: float = 0.60,
    minimum_containment: float = 0.80,
) -> pd.DataFrame:
    """Calcula candidatos de sobreposição estrutural parcial entre tabelas não idênticas."""
    if not 0 <= minimum_jaccard <= 1 or not 0 <= minimum_containment <= 1:
        raise ValueError("Os limiares de similaridade devem estar entre 0 e 1.")

    records: list[dict[str, object]] = []
    rows = list(registry.itertuples(index=False))
    for left, right in combinations(rows, 2):
        if (
            left.schema_signature_sha256
            and left.schema_signature_sha256 == right.schema_signature_sha256
        ):
            continue

        left_sequence = _tokens(left.header_sequence)
        right_sequence = _tokens(right.header_sequence)
        left_set = set(left_sequence)
        right_set = set(right_sequence)
        if not left_set or not right_set:
            continue

        intersection = len(left_set & right_set)
        union = len(left_set | right_set)
        jaccard = intersection / union if union else 0.0
        containment = intersection / min(len(left_set), len(right_set))
        sequence_ratio = SequenceMatcher(None, left_sequence, right_sequence).ratio()
        if jaccard < minimum_jaccard and containment < minimum_containment:
            continue

        records.append(
            {
                "left_path": left.relative_path,
                "left_sheet": left.sheet_name,
                "left_source": left.source_declared,
                "right_path": right.relative_path,
                "right_sheet": right.sheet_name,
                "right_source": right.source_declared,
                "headers_left": len(left_set),
                "headers_right": len(right_set),
                "headers_intersection": intersection,
                "jaccard_similarity_estimate": round(jaccard, 6),
                "containment_similarity_estimate": round(containment, 6),
                "sequence_similarity_estimate": round(sequence_ratio, 6),
                "candidate_class": "NEAR_SCHEMA"
                if jaccard >= 0.80
                else "PARTIAL_SCHEMA",
            }
        )

    if not records:
        return pd.DataFrame(
            columns=[
                "left_path",
                "left_sheet",
                "left_source",
                "right_path",
                "right_sheet",
                "right_source",
                "headers_left",
                "headers_right",
                "headers_intersection",
                "jaccard_similarity_estimate",
                "containment_similarity_estimate",
                "sequence_similarity_estimate",
                "candidate_class",
            ]
        )
    return pd.DataFrame(records).sort_values(
        [
            "jaccard_similarity_estimate",
            "containment_similarity_estimate",
            "sequence_similarity_estimate",
            "left_path",
            "right_path",
        ],
        ascending=[False, False, False, True, True],
    ).reset_index(drop=True)


def triage_structure(sheets: pd.DataFrame, columns: pd.DataFrame) -> StructureTriageResult:
    """Executa a triagem estrutural sem inferir equivalência conceitual."""
    registry = build_table_registry(sheets, columns)
    return StructureTriageResult(
        table_registry=registry,
        schema_summary=build_schema_summary(registry),
        source_summary=build_source_summary(registry),
        similarity_candidates=build_similarity_candidates(registry),
    )
