"""Construção local da camada de staging para ``raw/new_files``."""

from __future__ import annotations

import hashlib
import re
import shutil
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath
from typing import Iterable

import pandas as pd

from sbmi.inbox_anomaly_review import DATE_HEADERS, _table_rows, parse_date_observation
from sbmi.inbox_content_audit import canonical_value
from sbmi.inbox_profile import normalize_label
from sbmi.inbox_structure_triage import source_from_path

FEDERAL_HEADERS = (
    "mes_ano",
    "tipo",
    "tipo_de_favorecido",
    "uf",
    "nome_do_favorecido",
    "cpf_cnpj",
    "municipio",
    "funcao",
    "programa_orcamentario",
    "acao_orcamentaria",
    "linguagem_cidada",
    "valor_transferido",
)
ESTADUAL_ICMS_HEADERS = (
    "data",
    "codmunicipio",
    "nomemunicipio",
    "valor",
    "valorcoeficiente",
    "rubrica",
    "descricao",
    "iniciativa",
    "convenio",
)
ESTADUAL_TRANSFERENCIAS_HEADERS = (
    "data",
    "valor",
    "rubrica",
    "iniciativa",
    "municipio",
    "credor",
    "orgao",
    "fase_gasto",
    "empenho",
    "processo",
    "unidade_orcamentaria",
    "funcao",
    "subfuncao",
    "acao_porgramatica",
    "projeto",
    "subprojeto",
)
MUNICIPAL_DESPESAS_INSTITUICAO_HEADERS = (
    "instituicao",
    "empenhado",
    "anulado",
    "liquidado",
    "pago",
)
MUNICIPAL_DESPESAS_ELEMENTO_HEADERS = (
    "grupo_de_despesa",
    "elemento_da_despesa",
    "empenhado",
    "anulado",
    "liquidado",
    "pago",
)
MUNICIPAL_RECEITA_ELEMENTO_HEADERS = (
    "instituicao",
    "previsao_inicial",
    "previsao_adicional",
    "arrecadado",
    "acumulado",
    "diferenca",
)

DATASET_CONTRACTS = {
    ("Federal", FEDERAL_HEADERS): "federal_transferencias",
    ("Estadual", ESTADUAL_ICMS_HEADERS): "estadual_icms",
    ("Estadual", ESTADUAL_TRANSFERENCIAS_HEADERS): "estadual_transferencias",
    (
        "Municipal",
        MUNICIPAL_DESPESAS_INSTITUICAO_HEADERS,
    ): "municipal_despesas_instituicao",
    ("Municipal", MUNICIPAL_DESPESAS_ELEMENTO_HEADERS): "municipal_despesas_elemento",
    ("Municipal", MUNICIPAL_RECEITA_ELEMENTO_HEADERS): "municipal_receita_elemento",
}

NUMERIC_HEADERS = {
    "valor_transferido",
    "valor",
    "valorcoeficiente",
    "empenhado",
    "anulado",
    "liquidado",
    "pago",
    "previsao_inicial",
    "previsao_adicional",
    "arrecadado",
    "acumulado",
    "diferenca",
}
COPY_YEAR_PATTERN = re.compile(r"(?<!\d)(?:19|20|21)\d{2}(?!\d)")


@dataclass(frozen=True)
class StagingResult:
    datasets: dict[str, pd.DataFrame]
    source_manifest: pd.DataFrame
    quality_summary: pd.DataFrame


def parse_decimal_value(value: object) -> Decimal | None:
    """Converte número observado em ``Decimal`` sem arredondamento imposto."""
    if value is None:
        return None
    if isinstance(value, bool):
        raise ValueError("Valor booleano não pode ser convertido em medida numérica.")
    if isinstance(value, Decimal):
        return value
    if isinstance(value, (int, float)):
        text = canonical_value(value)
    else:
        text = re.sub(r"\s+", "", str(value)).replace("R$", "").strip()
    if not text:
        return None

    if "," in text and "." in text:
        if text.rfind(",") > text.rfind("."):
            text = text.replace(".", "").replace(",", ".")
        else:
            text = text.replace(",", "")
    elif "," in text:
        text = text.replace(".", "").replace(",", ".")

    try:
        return Decimal(text)
    except InvalidOperation as exc:
        raise ValueError(f"Valor numérico inválido: {value!r}") from exc


def classify_dataset(source_declared: str, headers: Iterable[str]) -> str:
    """Classifica uma tabela apenas quando ela corresponde a contrato explícito."""
    normalized = tuple(normalize_label(value) for value in headers)
    key = (source_declared, normalized)
    if key not in DATASET_CONTRACTS:
        raise ValueError(
            "Estrutura sem contrato de staging: "
            f"origem={source_declared!r}, cabeçalhos={normalized!r}"
        )
    return DATASET_CONTRACTS[key]


def _normalized_row_hash(values: Iterable[object]) -> str:
    payload = "\x1f".join(
        re.sub(r"\s+", " ", canonical_value(value)).casefold().strip()
        for value in values
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _excluded_paths(content_duplicates: pd.DataFrame) -> set[str]:
    if content_duplicates.empty:
        return set()
    required = {
        "suggested_duplicate_path",
        "suggestion_basis",
        "duplicate_class",
    }
    missing = required.difference(content_duplicates.columns)
    if missing:
        raise ValueError(f"Colunas ausentes em content_duplicate_pairs: {sorted(missing)}")
    eligible = content_duplicates.loc[
        content_duplicates["suggested_duplicate_path"].fillna("").astype(str).str.strip().ne("")
        & content_duplicates["suggestion_basis"].eq("COPY_SUFFIX_HEURISTIC")
        & content_duplicates["duplicate_class"].isin(
            ["CONTENT_DUPLICATE", "EXACT_DUPLICATE"]
        )
    ]
    return set(eligible["suggested_duplicate_path"].astype(str))


def _duplicate_row_lookup(duplicate_rows: pd.DataFrame) -> dict[tuple[str, int], dict[str, object]]:
    if duplicate_rows.empty:
        return {}
    required = {
        "relative_path",
        "normalized_row_hash",
        "occurrence_count",
        "source_row_numbers",
        "duplicate_class",
        "review_status",
    }
    missing = required.difference(duplicate_rows.columns)
    if missing:
        raise ValueError(f"Colunas ausentes em duplicate_row_groups: {sorted(missing)}")

    lookup: dict[tuple[str, int], dict[str, object]] = {}
    for group_index, row in enumerate(duplicate_rows.itertuples(index=False), start=1):
        path = str(row.relative_path)
        group_id = f"duplicate-group-{group_index:04d}"
        for raw_number in str(row.source_row_numbers).split("|"):
            source_row_number = int(raw_number)
            lookup[(path, source_row_number)] = {
                "_duplicate_group_id": group_id,
                "_duplicate_occurrence_count": int(row.occurrence_count),
                "_duplicate_class": str(row.duplicate_class),
                "_duplicate_review_status": str(row.review_status),
                "_duplicate_row_hash": str(row.normalized_row_hash),
            }
    return lookup


def _reference_year_from_filename(relative_path: str) -> int | None:
    years = COPY_YEAR_PATTERN.findall(PurePosixPath(relative_path).stem)
    return int(years[-1]) if years else None


def _transform_value(header: str, value: object) -> object:
    if header in DATE_HEADERS:
        parsed = parse_date_observation(value)
        if parsed["parsed_date"] is None:
            raise ValueError(f"Data não interpretada no campo {header}: {value!r}")
        if parsed["ambiguous"]:
            raise ValueError(f"Data ambígua no campo {header}: {value!r}")
        return parsed["parsed_date"]
    if header in NUMERIC_HEADERS:
        return parse_decimal_value(value)
    return canonical_value(value) or None


def _source_table_records(
    snapshot_path: Path,
    profile_row: object,
    *,
    snapshot_id: str,
    duplicate_lookup: dict[tuple[str, int], dict[str, object]],
) -> tuple[str, list[dict[str, object]]]:
    relative_path = str(profile_row.relative_path)
    source_declared = source_from_path(relative_path)
    headers, observations = _table_rows(snapshot_path, profile_row)
    normalized_headers = tuple(normalize_label(value) for value in headers)
    dataset = classify_dataset(source_declared, headers)

    records: list[dict[str, object]] = []
    for observation in observations:
        transformed = {
            header: _transform_value(header, value)
            for header, value in zip(
                normalized_headers,
                observation.values,
                strict=False,
            )
        }
        transformed.update(
            {
                "_source_level": source_declared,
                "_source_path": relative_path,
                "_source_file": PurePosixPath(relative_path).name,
                "_source_sheet": str(profile_row.sheet_name),
                "_source_row": int(observation.source_row_number),
                "_snapshot_id": snapshot_id,
                "_reference_year_filename": _reference_year_from_filename(relative_path),
                "_row_sha256": _normalized_row_hash(observation.values),
                "_duplicate_group_id": None,
                "_duplicate_occurrence_count": 0,
                "_duplicate_class": None,
                "_duplicate_review_status": None,
                "_duplicate_row_hash": None,
            }
        )
        transformed.update(
            duplicate_lookup.get((relative_path, observation.source_row_number), {})
        )
        records.append(transformed)
    return dataset, records


def build_staging(
    snapshot_path: Path,
    sheet_profile: pd.DataFrame,
    content_duplicates: pd.DataFrame,
    duplicate_rows: pd.DataFrame,
    *,
    snapshot_id: str,
) -> StagingResult:
    """Constrói dataframes de staging sem alterar arquivos de origem."""
    excluded = _excluded_paths(content_duplicates)
    duplicate_lookup = _duplicate_row_lookup(duplicate_rows)
    grouped_records: dict[str, list[dict[str, object]]] = {
        name: [] for name in sorted(set(DATASET_CONTRACTS.values()))
    }
    manifest_records: list[dict[str, object]] = []

    for profile_row in sheet_profile.itertuples(index=False):
        relative_path = str(profile_row.relative_path)
        headers, observations = _table_rows(snapshot_path, profile_row)
        source_declared = source_from_path(relative_path)
        dataset = classify_dataset(source_declared, headers)
        input_rows = len(observations)

        if relative_path in excluded:
            manifest_records.append(
                {
                    "relative_path": relative_path,
                    "source_declared": source_declared,
                    "dataset": dataset,
                    "input_rows": input_rows,
                    "output_rows": 0,
                    "disposition": "EXCLUDED_CONTENT_DUPLICATE_FROM_STAGING",
                    "basis": "COPY_SUFFIX_HEURISTIC",
                }
            )
            continue

        _, records = _source_table_records(
            snapshot_path,
            profile_row,
            snapshot_id=snapshot_id,
            duplicate_lookup=duplicate_lookup,
        )
        grouped_records[dataset].extend(records)
        manifest_records.append(
            {
                "relative_path": relative_path,
                "source_declared": source_declared,
                "dataset": dataset,
                "input_rows": input_rows,
                "output_rows": len(records),
                "disposition": "INCLUDED_IN_STAGING",
                "basis": "EXPLICIT_DATA_CONTRACT",
            }
        )

    datasets = {
        name: pd.DataFrame(records)
        for name, records in grouped_records.items()
    }
    manifest = pd.DataFrame(manifest_records).sort_values(
        ["source_declared", "dataset", "relative_path"]
    ).reset_index(drop=True)

    duplicate_flagged_rows = sum(
        int(frame["_duplicate_group_id"].notna().sum())
        for frame in datasets.values()
        if "_duplicate_group_id" in frame.columns
    )
    indicators = [
        ("source_tables_observed", len(manifest), "observed"),
        ("source_rows_observed", int(manifest["input_rows"].sum()), "observed"),
        (
            "source_files_excluded_from_staging",
            int(manifest["disposition"].ne("INCLUDED_IN_STAGING").sum()),
            "calculated",
        ),
        (
            "source_rows_excluded_from_staging",
            int((manifest["input_rows"] - manifest["output_rows"]).sum()),
            "calculated",
        ),
        ("staging_datasets", len(datasets), "observed"),
        (
            "staging_rows",
            sum(len(frame) for frame in datasets.values()),
            "calculated",
        ),
        (
            "federal_source_files_included",
            int(
                manifest.loc[
                    manifest["dataset"].eq("federal_transferencias")
                    & manifest["disposition"].eq("INCLUDED_IN_STAGING")
                ].shape[0]
            ),
            "calculated",
        ),
        (
            "federal_rows",
            len(datasets["federal_transferencias"]),
            "calculated",
        ),
        ("icms_rows_retained", len(datasets["estadual_icms"]), "calculated"),
        ("icms_duplicate_rows_flagged", duplicate_flagged_rows, "calculated"),
    ]
    quality_summary = pd.DataFrame(indicators, columns=["indicator", "value", "nature"])
    return StagingResult(
        datasets=datasets,
        source_manifest=manifest,
        quality_summary=quality_summary,
    )


def write_staging_output(result: StagingResult, output_dir: Path) -> Path:
    """Publica o staging local de modo atômico e recusa sobrescrita."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        raise FileExistsError(f"Destino de staging já existe: {target}")
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        for name, frame in result.datasets.items():
            frame.to_parquet(partial / f"{name}.parquet", index=False)
        result.source_manifest.to_csv(partial / "source_manifest.csv", index=False)
        result.quality_summary.to_csv(partial / "staging_quality_summary.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
