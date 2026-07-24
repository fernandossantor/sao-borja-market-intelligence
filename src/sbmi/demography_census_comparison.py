"""Comparação entre planilhas brutas e produtos parquet do Censo 2022."""

from __future__ import annotations

import hashlib
import json
import math
import re
import shutil
import unicodedata
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal, InvalidOperation
from pathlib import Path, PurePosixPath

import pandas as pd

LINEAGE_REQUIRED_COLUMNS = {
    "dataset_identity",
    "raw_source_count",
    "processed_product_count",
    "raw_source_paths",
    "processed_product_paths",
    "lineage_match_status",
}
MATCHED_STATUS = "MATCHED_ONE_TO_ONE_BY_NAME"
NUMERIC_SIMPLE = re.compile(r"^[+-]?\d+(?:[.,]\d+)?$")
NUMERIC_BR = re.compile(r"^[+-]?\d{1,3}(?:\.\d{3})+(?:,\d+)?$")


@dataclass(frozen=True)
class CensusContentComparisonResult:
    datasets: pd.DataFrame
    columns: pd.DataFrame
    differences: pd.DataFrame
    summary: pd.DataFrame


def normalize_header(value: object) -> str:
    """Normaliza cabeçalhos sem alterar os valores analíticos."""
    decomposed = unicodedata.normalize("NFKD", str(value or ""))
    ascii_text = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return re.sub(r"[^a-z0-9]+", "_", ascii_text.casefold()).strip("_")


def _is_missing(value: object) -> bool:
    if value is None:
        return True
    try:
        result = pd.isna(value)
    except (TypeError, ValueError):
        return False
    return bool(result) if not hasattr(result, "__len__") else False


def _decimal_text(value: Decimal) -> str:
    if value == value.to_integral_value():
        return str(value.quantize(Decimal(1)))
    normalized = value.normalize()
    text = format(normalized, "f")
    return text.rstrip("0").rstrip(".") if "." in text else text


def _parse_numeric_text(value: str) -> Decimal | None:
    text = value.strip()
    if not text:
        return None
    if NUMERIC_BR.fullmatch(text):
        text = text.replace(".", "").replace(",", ".")
    elif NUMERIC_SIMPLE.fullmatch(text):
        if text.count(",") == 1:
            text = text.replace(",", ".")
    else:
        return None
    digits = text.lstrip("+-")
    integer_part = digits.split(".", maxsplit=1)[0]
    if len(integer_part) > 1 and integer_part.startswith("0"):
        return None
    try:
        return Decimal(text)
    except InvalidOperation:
        return None


def canonical_value(value: object) -> tuple[str, str]:
    """Converte valores para comparação sem esconder diferenças textuais."""
    if _is_missing(value):
        return "missing", ""
    if isinstance(value, bool):
        return "boolean", "true" if value else "false"
    if isinstance(value, (datetime, date)):
        return "date", value.isoformat()
    if isinstance(value, int):
        return "number", str(value)
    if isinstance(value, float):
        if math.isnan(value):
            return "missing", ""
        return "number", _decimal_text(Decimal(str(value)))
    if isinstance(value, Decimal):
        return "number", _decimal_text(value)
    text = " ".join(str(value).strip().split())
    numeric = _parse_numeric_text(text)
    if numeric is not None:
        return "number", _decimal_text(numeric)
    return "text", unicodedata.normalize("NFC", text)


def _canonical_frame(frame: pd.DataFrame) -> tuple[pd.DataFrame, list[str]]:
    normalized_headers = [normalize_header(column) for column in frame.columns]
    if any(not header for header in normalized_headers):
        raise ValueError("Cabeçalho vazio após normalização.")
    if len(set(normalized_headers)) != len(normalized_headers):
        duplicates = sorted(
            header
            for header, count in Counter(normalized_headers).items()
            if count > 1
        )
        raise ValueError(f"Cabeçalhos duplicados após normalização: {duplicates}")
    canonical = pd.DataFrame(index=range(len(frame)))
    for source_column, normalized in zip(frame.columns, normalized_headers, strict=True):
        canonical[normalized] = frame[source_column].map(canonical_value)
    return canonical, normalized_headers


def _frame_hash(columns: list[str], rows: list[tuple[object, ...]]) -> str:
    payload = {
        "columns": columns,
        "rows": rows,
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
        default=str,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _read_raw_xlsx(path: Path) -> tuple[pd.DataFrame, str, int]:
    workbook = pd.ExcelFile(path)
    if not workbook.sheet_names:
        raise ValueError("Planilha sem abas.")
    if len(workbook.sheet_names) != 1:
        raise ValueError(
            "Quantidade de abas inesperada para o par nominal: "
            f"{len(workbook.sheet_names)}"
        )
    sheet = workbook.sheet_names[0]
    frame = pd.read_excel(path, sheet_name=sheet)
    frame = frame.dropna(axis=0, how="all").dropna(axis=1, how="all")
    return frame.reset_index(drop=True), sheet, len(workbook.sheet_names)


def _read_processed_parquet(path: Path) -> pd.DataFrame:
    frame = pd.read_parquet(path)
    return frame.dropna(axis=0, how="all").dropna(axis=1, how="all").reset_index(
        drop=True
    )


def _resolve_snapshot_file(root: Path, relative_path: str) -> Path:
    normalized = PurePosixPath(str(relative_path).strip("/"))
    candidate = root.joinpath(*normalized.parts).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f"Caminho fora da captura: {relative_path}") from exc
    if not candidate.is_file():
        raise FileNotFoundError(f"Arquivo da captura não encontrado: {candidate}")
    return candidate


def _split_single_path(value: object, expected_count: object, label: str) -> str:
    count = int(expected_count)
    paths = [part for part in str(value or "").split("|") if part]
    if count != 1 or len(paths) != 1:
        raise ValueError(f"{label} não é um caminho único: count={count}, paths={paths}")
    return paths[0]


def _column_register(
    dataset_identity: str,
    raw: pd.DataFrame,
    processed: pd.DataFrame,
    raw_columns: list[str],
    processed_columns: list[str],
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    all_columns = sorted(set(raw_columns) | set(processed_columns))
    for column in all_columns:
        raw_present = column in raw.columns
        processed_present = column in processed.columns
        raw_values = raw[column].tolist() if raw_present else []
        processed_values = processed[column].tolist() if processed_present else []
        records.append(
            {
                "dataset_identity": dataset_identity,
                "column": column,
                "raw_present": raw_present,
                "processed_present": processed_present,
                "raw_nonmissing": sum(kind != "missing" for kind, _ in raw_values),
                "processed_nonmissing": sum(
                    kind != "missing" for kind, _ in processed_values
                ),
                "raw_semantic_types": "|".join(
                    sorted({kind for kind, _ in raw_values})
                ),
                "processed_semantic_types": "|".join(
                    sorted({kind for kind, _ in processed_values})
                ),
                "column_values_match": raw_present
                and processed_present
                and raw_values == processed_values,
                "nature": "observed_and_calculated",
            }
        )
    return records


def _difference_register(
    dataset_identity: str,
    raw: pd.DataFrame,
    processed: pd.DataFrame,
    common_columns: list[str],
    *,
    limit: int,
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    maximum_rows = max(len(raw), len(processed))
    for row_index in range(maximum_rows):
        for column in common_columns:
            raw_value = raw.at[row_index, column] if row_index < len(raw) else None
            processed_value = (
                processed.at[row_index, column]
                if row_index < len(processed)
                else None
            )
            if raw_value == processed_value:
                continue
            raw_kind, raw_text = raw_value or ("missing", "")
            processed_kind, processed_text = processed_value or ("missing", "")
            records.append(
                {
                    "dataset_identity": dataset_identity,
                    "row_number_1_based": row_index + 1,
                    "column": column,
                    "raw_kind": raw_kind,
                    "raw_value": raw_text,
                    "processed_kind": processed_kind,
                    "processed_value": processed_text,
                    "nature": "observed",
                }
            )
            if len(records) >= limit:
                return records
    return records


def compare_dataset_pair(
    *,
    dataset_identity: str,
    raw_path: Path,
    processed_path: Path,
    raw_relative_path: str,
    processed_relative_path: str,
    difference_limit: int = 100,
) -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]]]:
    """Compara um par, distinguindo equivalência de conteúdo de validade conceitual."""
    try:
        raw_frame, raw_sheet, raw_sheet_count = _read_raw_xlsx(raw_path)
        processed_frame = _read_processed_parquet(processed_path)
        raw, raw_columns = _canonical_frame(raw_frame)
        processed, processed_columns = _canonical_frame(processed_frame)
    except Exception as exc:  # noqa: BLE001
        record = {
            "dataset_identity": dataset_identity,
            "raw_relative_path": raw_relative_path,
            "processed_relative_path": processed_relative_path,
            "raw_sheet": "",
            "raw_sheet_count": 0,
            "raw_rows": 0,
            "processed_rows": 0,
            "raw_columns": 0,
            "processed_columns": 0,
            "header_set_match": False,
            "column_order_match": False,
            "row_count_match": False,
            "missing_values_match": False,
            "canonical_sequence_match": False,
            "canonical_row_multiset_match": False,
            "raw_canonical_sha256": "",
            "processed_canonical_sha256": "",
            "difference_cells_observed": 0,
            "content_equivalence_status": "READ_ERROR",
            "error_type": type(exc).__name__,
            "error_message": str(exc)[:500],
            "source_authority_status": "NOT_ASSESSED",
            "conceptual_validation_status": "NOT_VALIDATED",
            "nature": "observed_and_calculated",
        }
        return record, [], []

    header_set_match = set(raw_columns) == set(processed_columns)
    column_order_match = raw_columns == processed_columns
    row_count_match = len(raw) == len(processed)
    common_columns = [column for column in raw_columns if column in processed.columns]
    raw_aligned = raw[common_columns]
    processed_aligned = processed[common_columns]
    raw_rows = [tuple(row) for row in raw_aligned.itertuples(index=False, name=None)]
    processed_rows = [
        tuple(row) for row in processed_aligned.itertuples(index=False, name=None)
    ]
    sequence_match = header_set_match and row_count_match and raw_rows == processed_rows
    multiset_match = header_set_match and Counter(raw_rows) == Counter(processed_rows)
    raw_missing = sum(
        kind == "missing" for row in raw_rows for kind, _ in row
    )
    processed_missing = sum(
        kind == "missing" for row in processed_rows for kind, _ in row
    )
    missing_match = header_set_match and raw_missing == processed_missing
    differences = _difference_register(
        dataset_identity,
        raw_aligned,
        processed_aligned,
        common_columns,
        limit=difference_limit,
    )
    columns = _column_register(
        dataset_identity,
        raw_aligned,
        processed_aligned,
        raw_columns,
        processed_columns,
    )

    if sequence_match:
        status = "EXACT_AFTER_CANONICALIZATION"
    elif multiset_match:
        status = "ROW_ORDER_DIFFERS_ONLY"
    elif not header_set_match:
        status = "SCHEMA_MISMATCH"
    elif not row_count_match:
        status = "ROW_COUNT_MISMATCH"
    else:
        status = "CELL_VALUE_MISMATCH"

    record = {
        "dataset_identity": dataset_identity,
        "raw_relative_path": raw_relative_path,
        "processed_relative_path": processed_relative_path,
        "raw_sheet": raw_sheet,
        "raw_sheet_count": raw_sheet_count,
        "raw_rows": len(raw),
        "processed_rows": len(processed),
        "raw_columns": len(raw_columns),
        "processed_columns": len(processed_columns),
        "header_set_match": header_set_match,
        "column_order_match": column_order_match,
        "row_count_match": row_count_match,
        "missing_values_match": missing_match,
        "canonical_sequence_match": sequence_match,
        "canonical_row_multiset_match": multiset_match,
        "raw_canonical_sha256": _frame_hash(common_columns, raw_rows),
        "processed_canonical_sha256": _frame_hash(common_columns, processed_rows),
        "difference_cells_observed": len(differences),
        "content_equivalence_status": status,
        "error_type": "",
        "error_message": "",
        "source_authority_status": "PENDING_SOURCE_METADATA_REVIEW",
        "conceptual_validation_status": "NOT_VALIDATED",
        "nature": "observed_and_calculated",
    }
    return record, columns, differences


def compare_census_lineage(
    lineage_register: pd.DataFrame,
    *,
    raw_snapshot_root: Path,
    derived_snapshot_root: Path,
    difference_limit_per_dataset: int = 100,
) -> CensusContentComparisonResult:
    """Compara todos os pares nominais um-para-um registrados na linhagem."""
    missing = LINEAGE_REQUIRED_COLUMNS.difference(lineage_register.columns)
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes na linhagem: {sorted(missing)}")
    raw_root = raw_snapshot_root.expanduser().resolve()
    derived_root = derived_snapshot_root.expanduser().resolve()
    dataset_records: list[dict[str, object]] = []
    column_records: list[dict[str, object]] = []
    difference_records: list[dict[str, object]] = []

    matched = lineage_register.loc[
        lineage_register["lineage_match_status"].eq(MATCHED_STATUS)
    ].copy()
    for row in matched.itertuples(index=False):
        raw_relative = _split_single_path(
            row.raw_source_paths,
            row.raw_source_count,
            "Fonte bruta",
        )
        processed_relative = _split_single_path(
            row.processed_product_paths,
            row.processed_product_count,
            "Produto processado",
        )
        raw_path = _resolve_snapshot_file(raw_root, raw_relative)
        processed_path = _resolve_snapshot_file(derived_root, processed_relative)
        dataset, columns, differences = compare_dataset_pair(
            dataset_identity=str(row.dataset_identity),
            raw_path=raw_path,
            processed_path=processed_path,
            raw_relative_path=raw_relative,
            processed_relative_path=processed_relative,
            difference_limit=difference_limit_per_dataset,
        )
        dataset_records.append(dataset)
        column_records.extend(columns)
        difference_records.extend(differences)

    datasets = pd.DataFrame(dataset_records)
    columns = pd.DataFrame(column_records)
    differences = pd.DataFrame(difference_records)
    if differences.empty:
        differences = pd.DataFrame(
            columns=[
                "dataset_identity",
                "row_number_1_based",
                "column",
                "raw_kind",
                "raw_value",
                "processed_kind",
                "processed_value",
                "nature",
            ]
        )
    statuses = datasets["content_equivalence_status"] if not datasets.empty else pd.Series()
    summary = pd.DataFrame(
        [
            ("lineage_pairs_compared", len(datasets), "calculated"),
            (
                "exact_after_canonicalization",
                int(statuses.eq("EXACT_AFTER_CANONICALIZATION").sum()),
                "calculated",
            ),
            (
                "row_order_only_differences",
                int(statuses.eq("ROW_ORDER_DIFFERS_ONLY").sum()),
                "calculated",
            ),
            (
                "schema_mismatches",
                int(statuses.eq("SCHEMA_MISMATCH").sum()),
                "calculated",
            ),
            (
                "row_count_mismatches",
                int(statuses.eq("ROW_COUNT_MISMATCH").sum()),
                "calculated",
            ),
            (
                "cell_value_mismatches",
                int(statuses.eq("CELL_VALUE_MISMATCH").sum()),
                "calculated",
            ),
            ("read_errors", int(statuses.eq("READ_ERROR").sum()), "observed"),
            ("difference_cells_observed", len(differences), "observed"),
            (
                "content_equivalence_tests_completed",
                int(statuses.ne("READ_ERROR").sum()),
                "calculated",
            ),
            ("source_authority_reviews_completed", 0, "observed"),
            ("conceptually_validated_datasets", 0, "observed"),
        ],
        columns=["indicator", "value", "nature"],
    )
    return CensusContentComparisonResult(
        datasets=datasets,
        columns=columns,
        differences=differences,
        summary=summary,
    )


def write_census_comparison(
    result: CensusContentComparisonResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica a comparação local de forma atômica."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino da comparação já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    outputs = {
        "demography_census_dataset_comparison.csv": result.datasets,
        "demography_census_column_comparison.csv": result.columns,
        "demography_census_cell_differences.csv": result.differences,
        "demography_census_comparison_summary.csv": result.summary,
    }
    try:
        for file_name, frame in outputs.items():
            frame.to_csv(partial / file_name, index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
