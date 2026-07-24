"""Mapeamento de candidatos para integrar o staging ao acervo histórico."""

from __future__ import annotations

import re
import shutil
import unicodedata
from collections.abc import Iterable
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path, PurePosixPath

import pandas as pd

from sbmi.inbox_audit import _folder_mask

TARGET_SCOPES = ("processed", "warehouse", "exports")
DATA_EXTENSIONS = {
    "csv",
    "tsv",
    "xlsx",
    "xls",
    "xlsm",
    "ods",
    "parquet",
    "feather",
    "json",
    "jsonl",
    "duckdb",
    "db",
    "sqlite",
    "sqlite3",
}
INVENTORY_REQUIRED_COLUMNS = {
    "relative_path",
    "file_name",
    "extension",
    "is_folder",
    "size_bytes",
    "sha256_checksum",
}
MANIFEST_REQUIRED_COLUMNS = {
    "relative_path",
    "dataset",
    "disposition",
}
COPY_SUFFIX_PATTERN = re.compile(
    r"(?:\s|_|-)*(?:\(\d+\)|copia|copy)$",
    re.IGNORECASE,
)
NON_ALNUM_PATTERN = re.compile(r"[^a-z0-9]+")


@dataclass(frozen=True)
class HistoricalIntegrationMapResult:
    scope_summary: pd.DataFrame
    source_summary: pd.DataFrame
    candidates: pd.DataFrame
    mapping_summary: pd.DataFrame


def _extension(value: object) -> str:
    return str(value or "").strip().lower().lstrip(".")


def _top_level(path: object) -> str:
    parts = PurePosixPath(str(path or "").strip("/")).parts
    return parts[0] if parts else ""


def normalize_file_stem(value: object) -> str:
    """Normaliza o nome sem extensão para comparação lexical heurística."""
    stem = PurePosixPath(str(value or "")).stem.strip()
    stem = COPY_SUFFIX_PATTERN.sub("", stem).strip()
    decomposed = unicodedata.normalize("NFKD", stem)
    ascii_text = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    normalized = NON_ALNUM_PATTERN.sub(" ", ascii_text.casefold()).strip()
    return re.sub(r"\s+", " ", normalized)


def _tokens(value: str) -> set[str]:
    return {token for token in value.split() if token}


def name_similarity(left: object, right: object) -> dict[str, float]:
    """Calcula similaridades lexicais sem inferir equivalência conceitual."""
    left_name = normalize_file_stem(left)
    right_name = normalize_file_stem(right)
    if not left_name or not right_name:
        return {
            "jaccard": 0.0,
            "containment": 0.0,
            "sequence": 0.0,
            "score": 0.0,
        }

    left_tokens = _tokens(left_name)
    right_tokens = _tokens(right_name)
    union = left_tokens | right_tokens
    intersection = left_tokens & right_tokens
    jaccard = len(intersection) / len(union) if union else 0.0
    smaller = min(len(left_tokens), len(right_tokens))
    containment = len(intersection) / smaller if smaller else 0.0
    sequence = SequenceMatcher(None, left_name, right_name).ratio()
    score = max(jaccard, sequence, containment * 0.9)
    return {
        "jaccard": round(jaccard, 6),
        "containment": round(containment, 6),
        "sequence": round(sequence, 6),
        "score": round(score, 6),
    }


def classify_candidate(
    *,
    source_sha256: str,
    historical_sha256: str,
    source_name: object,
    historical_name: object,
    similarities: dict[str, float],
) -> str | None:
    """Classifica somente a força do indício de correspondência."""
    if source_sha256 and source_sha256 == historical_sha256:
        return "EXACT_SHA256"
    if normalize_file_stem(source_name) == normalize_file_stem(historical_name):
        return "EXACT_NORMALIZED_NAME"

    token_count = min(
        len(_tokens(normalize_file_stem(source_name))),
        len(_tokens(normalize_file_stem(historical_name))),
    )
    if similarities["score"] >= 0.8 or (
        token_count >= 2 and similarities["containment"] >= 0.9
    ):
        return "STRONG_NAME_MATCH"
    if (
        similarities["score"] >= 0.6
        or similarities["jaccard"] >= 0.4
        or similarities["containment"] >= 0.7
    ):
        return "POSSIBLE_NAME_MATCH"
    return None


def _validate_inputs(inventory: pd.DataFrame, manifest: pd.DataFrame) -> None:
    inventory_missing = INVENTORY_REQUIRED_COLUMNS.difference(inventory.columns)
    if inventory_missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no inventário: "
            f"{sorted(inventory_missing)}"
        )
    manifest_missing = MANIFEST_REQUIRED_COLUMNS.difference(manifest.columns)
    if manifest_missing:
        raise ValueError(
            "Colunas obrigatórias ausentes no manifesto: "
            f"{sorted(manifest_missing)}"
        )


def _prepare_inventory(inventory: pd.DataFrame) -> pd.DataFrame:
    frame = inventory.copy()
    frame = frame.loc[~_folder_mask(frame["is_folder"])].copy()
    frame["relative_path"] = frame["relative_path"].fillna("").astype(str)
    frame["file_name"] = frame["file_name"].fillna("").astype(str)
    frame["extension"] = frame["extension"].map(_extension)
    frame["size_bytes"] = pd.to_numeric(frame["size_bytes"], errors="coerce")
    frame["sha256_checksum"] = (
        frame["sha256_checksum"].fillna("").astype(str).str.strip().str.lower()
    )
    frame["scope"] = frame["relative_path"].map(_top_level)
    frame["is_data_like"] = frame["extension"].isin(DATA_EXTENSIONS)
    return frame


def _active_sources(
    manifest: pd.DataFrame,
    inventory: pd.DataFrame,
) -> pd.DataFrame:
    included = manifest.loc[
        manifest["disposition"].eq("INCLUDED_IN_STAGING"),
        ["relative_path", "dataset"],
    ].drop_duplicates()
    source_metadata = inventory[
        [
            "relative_path",
            "file_name",
            "extension",
            "size_bytes",
            "sha256_checksum",
        ]
    ]
    sources = included.merge(
        source_metadata,
        on="relative_path",
        how="left",
        validate="one_to_one",
    )
    if sources["file_name"].isna().any():
        missing = sorted(
            sources.loc[
                sources["file_name"].isna(),
                "relative_path",
            ].astype(str)
        )
        raise ValueError(f"Fontes do staging ausentes no inventário: {missing}")
    return sources.sort_values(["dataset", "relative_path"]).reset_index(drop=True)


def _scope_summary(
    historical: pd.DataFrame,
    scopes: Iterable[str],
) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for scope in scopes:
        group = historical.loc[historical["scope"].eq(scope)]
        extensions = sorted(
            set(group.loc[group["extension"].ne(""), "extension"])
        )
        records.append(
            {
                "scope": scope,
                "files": len(group),
                "data_like_files": int(group["is_data_like"].sum()),
                "known_bytes": int(group["size_bytes"].fillna(0).sum()),
                "files_with_sha256": int(
                    group["sha256_checksum"].ne("").sum()
                ),
                "extensions": "|".join(extensions),
            }
        )
    return pd.DataFrame(records)


def _candidate_records(
    sources: pd.DataFrame,
    historical: pd.DataFrame,
    *,
    top_n: int,
) -> pd.DataFrame:
    if top_n < 1:
        raise ValueError("top_n deve ser maior ou igual a 1.")

    records: list[dict[str, object]] = []
    historical_data = historical.loc[historical["is_data_like"]].copy()
    for source in sources.itertuples(index=False):
        source_records: list[dict[str, object]] = []
        for candidate in historical_data.itertuples(index=False):
            similarities = name_similarity(source.file_name, candidate.file_name)
            candidate_class = classify_candidate(
                source_sha256=str(source.sha256_checksum or ""),
                historical_sha256=str(candidate.sha256_checksum or ""),
                source_name=source.file_name,
                historical_name=candidate.file_name,
                similarities=similarities,
            )
            if candidate_class is None:
                continue
            priority = {
                "EXACT_SHA256": 4,
                "EXACT_NORMALIZED_NAME": 3,
                "STRONG_NAME_MATCH": 2,
                "POSSIBLE_NAME_MATCH": 1,
            }[candidate_class]
            source_records.append(
                {
                    "source_relative_path": source.relative_path,
                    "source_dataset": source.dataset,
                    "source_file_name": source.file_name,
                    "source_extension": source.extension,
                    "source_size_bytes": source.size_bytes,
                    "source_sha256": source.sha256_checksum,
                    "historical_scope": candidate.scope,
                    "historical_relative_path": candidate.relative_path,
                    "historical_file_name": candidate.file_name,
                    "historical_extension": candidate.extension,
                    "historical_size_bytes": candidate.size_bytes,
                    "historical_sha256": candidate.sha256_checksum,
                    "candidate_class": candidate_class,
                    "candidate_priority": priority,
                    "name_jaccard": similarities["jaccard"],
                    "name_containment": similarities["containment"],
                    "name_sequence": similarities["sequence"],
                    "name_score": similarities["score"],
                }
            )
        source_records.sort(
            key=lambda row: (
                -int(row["candidate_priority"]),
                -float(row["name_score"]),
                str(row["historical_relative_path"]),
            )
        )
        for rank, record in enumerate(source_records[:top_n], start=1):
            record["candidate_rank_for_source"] = rank
            records.append(record)

    columns = [
        "source_relative_path",
        "source_dataset",
        "source_file_name",
        "source_extension",
        "source_size_bytes",
        "source_sha256",
        "historical_scope",
        "historical_relative_path",
        "historical_file_name",
        "historical_extension",
        "historical_size_bytes",
        "historical_sha256",
        "candidate_class",
        "candidate_priority",
        "candidate_rank_for_source",
        "name_jaccard",
        "name_containment",
        "name_sequence",
        "name_score",
    ]
    return pd.DataFrame(records, columns=columns)


def _source_summary(
    sources: pd.DataFrame,
    candidates: pd.DataFrame,
) -> pd.DataFrame:
    records: list[dict[str, object]] = []
    for source in sources.itertuples(index=False):
        matches = candidates.loc[
            candidates["source_relative_path"].eq(source.relative_path)
        ].sort_values("candidate_rank_for_source")
        best = matches.iloc[0] if not matches.empty else None
        records.append(
            {
                "source_relative_path": source.relative_path,
                "source_dataset": source.dataset,
                "source_file_name": source.file_name,
                "source_extension": source.extension,
                "source_size_bytes": source.size_bytes,
                "source_sha256": source.sha256_checksum,
                "candidate_count_retained": len(matches),
                "best_candidate_class": (
                    "" if best is None else best["candidate_class"]
                ),
                "best_candidate_score": (
                    None if best is None else best["name_score"]
                ),
                "best_historical_scope": (
                    "" if best is None else best["historical_scope"]
                ),
                "best_historical_path": (
                    "" if best is None else best["historical_relative_path"]
                ),
                "mapping_status": (
                    "CANDIDATE_FOUND"
                    if best is not None
                    else "NO_METADATA_CANDIDATE"
                ),
            }
        )
    return pd.DataFrame(records)


def _mapping_summary(
    sources: pd.DataFrame,
    historical: pd.DataFrame,
    candidates: pd.DataFrame,
    source_summary: pd.DataFrame,
) -> pd.DataFrame:
    indicators = [
        ("active_staging_source_files", len(sources), "observed"),
        ("historical_target_files", len(historical), "observed"),
        (
            "historical_data_like_files",
            int(historical["is_data_like"].sum()),
            "calculated",
        ),
        ("candidate_pairs_retained", len(candidates), "calculated"),
        (
            "sources_with_candidates",
            int(source_summary["mapping_status"].eq("CANDIDATE_FOUND").sum()),
            "calculated",
        ),
        (
            "sources_without_candidates",
            int(
                source_summary["mapping_status"]
                .eq("NO_METADATA_CANDIDATE")
                .sum()
            ),
            "calculated",
        ),
    ]
    for candidate_class in (
        "EXACT_SHA256",
        "EXACT_NORMALIZED_NAME",
        "STRONG_NAME_MATCH",
        "POSSIBLE_NAME_MATCH",
    ):
        indicators.append(
            (
                candidate_class.lower() + "_pairs",
                int(candidates["candidate_class"].eq(candidate_class).sum()),
                "calculated",
            )
        )
    return pd.DataFrame(
        indicators,
        columns=["indicator", "value", "nature"],
    )


def build_historical_integration_map(
    inventory: pd.DataFrame,
    manifest: pd.DataFrame,
    *,
    scopes: Iterable[str] = TARGET_SCOPES,
    top_n: int = 5,
) -> HistoricalIntegrationMapResult:
    """Mapeia candidatos por metadados, sem baixar ou alterar arquivos históricos."""
    _validate_inputs(inventory, manifest)
    normalized_scopes = tuple(
        dict.fromkeys(
            str(scope).strip("/")
            for scope in scopes
            if str(scope).strip("/")
        )
    )
    if not normalized_scopes:
        raise ValueError("Ao menos um escopo histórico deve ser informado.")

    prepared = _prepare_inventory(inventory)
    sources = _active_sources(manifest, prepared)
    historical = prepared.loc[
        prepared["scope"].isin(normalized_scopes)
    ].copy()
    candidates = _candidate_records(sources, historical, top_n=top_n)
    source_summary = _source_summary(sources, candidates)
    return HistoricalIntegrationMapResult(
        scope_summary=_scope_summary(historical, normalized_scopes),
        source_summary=source_summary,
        candidates=candidates,
        mapping_summary=_mapping_summary(
            sources,
            historical,
            candidates,
            source_summary,
        ),
    )


def write_historical_integration_map(
    result: HistoricalIntegrationMapResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica relatórios locais de modo atômico e sem sobrescrever por padrão."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino do mapeamento já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        result.scope_summary.to_csv(
            partial / "historical_scope_summary.csv",
            index=False,
        )
        result.source_summary.to_csv(
            partial / "staging_source_mapping_summary.csv",
            index=False,
        )
        result.candidates.to_csv(
            partial / "historical_integration_candidates.csv",
            index=False,
        )
        result.mapping_summary.to_csv(
            partial / "historical_integration_summary.csv",
            index=False,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
