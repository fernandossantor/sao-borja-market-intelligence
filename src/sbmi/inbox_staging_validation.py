"""Validação da camada local de staging de ``raw/new_files``."""

from __future__ import annotations

import re
import shutil
from collections.abc import Mapping
from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from pathlib import Path, PurePosixPath

import pandas as pd

from sbmi.inbox_staging import DATASET_CONTRACTS, NUMERIC_HEADERS

PROVENANCE_COLUMNS = (
    "_source_level",
    "_source_path",
    "_source_file",
    "_source_sheet",
    "_source_row",
    "_snapshot_id",
    "_reference_year_filename",
    "_row_sha256",
    "_duplicate_group_id",
    "_duplicate_occurrence_count",
    "_duplicate_class",
    "_duplicate_review_status",
    "_duplicate_row_hash",
)
REQUIRED_PROVENANCE_COLUMNS = (
    "_source_level",
    "_source_path",
    "_source_file",
    "_source_sheet",
    "_source_row",
    "_snapshot_id",
    "_row_sha256",
)
DATE_COLUMNS_BY_DATASET = {
    "federal_transferencias": ("mes_ano",),
    "estadual_icms": ("data",),
    "estadual_transferencias": ("data",),
    "municipal_despesas_instituicao": (),
    "municipal_despesas_elemento": (),
    "municipal_receita_elemento": (),
}
SOURCE_LEVEL_BY_DATASET = {
    "federal_transferencias": "Federal",
    "estadual_icms": "Estadual",
    "estadual_transferencias": "Estadual",
    "municipal_despesas_instituicao": "Municipal",
    "municipal_despesas_elemento": "Municipal",
    "municipal_receita_elemento": "Municipal",
}
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
SNAPSHOT_DATE_PATTERN = re.compile(r"(\d{8})$")

BASE_COLUMNS_BY_DATASET = {
    dataset: tuple(headers)
    for (_, headers), dataset in DATASET_CONTRACTS.items()
}
EXPECTED_DATASETS = tuple(sorted(BASE_COLUMNS_BY_DATASET))


@dataclass(frozen=True)
class StagingValidationResult:
    dataset_summary: pd.DataFrame
    manifest_reconciliation: pd.DataFrame
    quality_reconciliation: pd.DataFrame
    validation_issues: pd.DataFrame
    validation_summary: pd.DataFrame


def snapshot_date_from_id(snapshot_id: str) -> date:
    """Extrai a data de uma captura cujo identificador termina em AAAAMMDD."""
    match = SNAPSHOT_DATE_PATTERN.search(snapshot_id)
    if not match:
        raise ValueError(
            "Não foi possível inferir a data do staging. "
            "O identificador deve terminar em AAAAMMDD."
        )
    return datetime.strptime(match.group(1), "%Y%m%d").date()


def required_columns(dataset: str) -> tuple[str, ...]:
    """Retorna o contrato completo esperado para um dataset de staging."""
    if dataset not in BASE_COLUMNS_BY_DATASET:
        raise ValueError(f"Dataset de staging desconhecido: {dataset}")
    return (*BASE_COLUMNS_BY_DATASET[dataset], *PROVENANCE_COLUMNS)


def _issue(
    records: list[dict[str, object]],
    *,
    severity: str,
    issue_class: str,
    dataset: str = "",
    column: str = "",
    count: int = 1,
    details: str = "",
) -> None:
    records.append(
        {
            "severity": severity,
            "issue_class": issue_class,
            "dataset": dataset,
            "column": column,
            "count": int(count),
            "details": details,
        }
    )


def _numeric_type_failures(series: pd.Series) -> int:
    failures = 0
    for value in series.dropna():
        if isinstance(value, bool):
            failures += 1
        elif not isinstance(value, (int, float, Decimal)):
            failures += 1
    return failures


def _date_metrics(series: pd.Series, snapshot_date: date) -> dict[str, object]:
    null_values = int(series.isna().sum())
    non_null = series.dropna()
    parsed = pd.to_datetime(non_null, errors="coerce")
    failures = int(parsed.isna().sum())
    valid = parsed.dropna()
    future = int((valid.dt.date > snapshot_date).sum()) if not valid.empty else 0
    return {
        "date_null_values": null_values,
        "date_parse_failures": failures,
        "future_date_values": future,
        "date_min": valid.min().date().isoformat() if not valid.empty else "",
        "date_max": valid.max().date().isoformat() if not valid.empty else "",
    }


def _duplicate_metrics(frame: pd.DataFrame) -> dict[str, int]:
    if "_duplicate_group_id" not in frame.columns:
        return {
            "duplicate_flagged_rows": 0,
            "duplicate_groups": 0,
            "duplicate_excess": 0,
            "duplicate_flag_inconsistencies": 0,
        }

    group_id = frame["_duplicate_group_id"]
    flagged = group_id.notna()
    fallback = pd.Series(index=frame.index, dtype=float)
    occurrence = pd.to_numeric(
        frame.get("_duplicate_occurrence_count", fallback),
        errors="coerce",
    ).fillna(0)
    companion_columns = (
        "_duplicate_class",
        "_duplicate_review_status",
        "_duplicate_row_hash",
    )
    inconsistent = int(
        ((flagged & occurrence.le(1)) | (~flagged & occurrence.ne(0))).sum()
    )
    for column in companion_columns:
        if column in frame.columns:
            companion_present = frame[column].notna()
            inconsistent += int((flagged ^ companion_present).sum())

    duplicate_groups = int(group_id.dropna().nunique())
    duplicate_excess = 0
    for _, group in frame.loc[flagged].groupby("_duplicate_group_id", dropna=False):
        size = len(group)
        expected = pd.to_numeric(
            group["_duplicate_occurrence_count"],
            errors="coerce",
        )
        if expected.isna().any() or not expected.eq(size).all():
            inconsistent += size
        duplicate_excess += max(size - 1, 0)

    return {
        "duplicate_flagged_rows": int(flagged.sum()),
        "duplicate_groups": duplicate_groups,
        "duplicate_excess": duplicate_excess,
        "duplicate_flag_inconsistencies": inconsistent,
    }


def validate_dataset_frame(
    dataset: str,
    frame: pd.DataFrame,
    *,
    snapshot_id: str,
    snapshot_date: date,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    """Valida contrato, proveniência, tipos e sinalizadores de um dataset."""
    issues: list[dict[str, object]] = []
    expected = required_columns(dataset)
    missing = sorted(set(expected).difference(frame.columns))
    unexpected = sorted(set(frame.columns).difference(expected))
    column_order_mismatch = int(tuple(frame.columns) != expected)
    if missing:
        _issue(
            issues,
            severity="ERROR",
            issue_class="MISSING_REQUIRED_COLUMNS",
            dataset=dataset,
            count=len(missing),
            details="|".join(missing),
        )
    if unexpected:
        _issue(
            issues,
            severity="WARNING",
            issue_class="UNEXPECTED_COLUMNS",
            dataset=dataset,
            count=len(unexpected),
            details="|".join(unexpected),
        )
    if column_order_mismatch and not missing and not unexpected:
        _issue(
            issues,
            severity="WARNING",
            issue_class="COLUMN_ORDER_MISMATCH",
            dataset=dataset,
        )

    provenance_null_values = 0
    for column in REQUIRED_PROVENANCE_COLUMNS:
        if column not in frame.columns:
            continue
        null_count = int(frame[column].isna().sum())
        provenance_null_values += null_count
        if null_count:
            _issue(
                issues,
                severity="ERROR",
                issue_class="NULL_REQUIRED_PROVENANCE",
                dataset=dataset,
                column=column,
                count=null_count,
            )

    provenance_key_duplicate_rows = 0
    key = ["_source_path", "_source_sheet", "_source_row"]
    if all(column in frame.columns for column in key):
        provenance_key_duplicate_rows = int(frame.duplicated(key, keep=False).sum())
        if provenance_key_duplicate_rows:
            _issue(
                issues,
                severity="ERROR",
                issue_class="DUPLICATE_PROVENANCE_KEY",
                dataset=dataset,
                count=provenance_key_duplicate_rows,
            )

    source_file_mismatches = 0
    if {"_source_path", "_source_file"}.issubset(frame.columns):
        expected_files = frame["_source_path"].fillna("").map(
            lambda value: PurePosixPath(str(value)).name
        )
        source_file_mismatches = int(
            expected_files.ne(frame["_source_file"].fillna("").astype(str)).sum()
        )
        if source_file_mismatches:
            _issue(
                issues,
                severity="ERROR",
                issue_class="SOURCE_FILE_PATH_MISMATCH",
                dataset=dataset,
                count=source_file_mismatches,
            )

    source_level_mismatches = 0
    if "_source_level" in frame.columns:
        expected_level = SOURCE_LEVEL_BY_DATASET[dataset]
        source_level_mismatches = int(
            frame["_source_level"].fillna("").astype(str).ne(expected_level).sum()
        )
        if source_level_mismatches:
            _issue(
                issues,
                severity="ERROR",
                issue_class="SOURCE_LEVEL_MISMATCH",
                dataset=dataset,
                count=source_level_mismatches,
                details=f"expected={expected_level}",
            )

    snapshot_id_mismatches = 0
    if "_snapshot_id" in frame.columns:
        snapshot_id_mismatches = int(
            frame["_snapshot_id"].fillna("").astype(str).ne(snapshot_id).sum()
        )
        if snapshot_id_mismatches:
            _issue(
                issues,
                severity="ERROR",
                issue_class="SNAPSHOT_ID_MISMATCH",
                dataset=dataset,
                count=snapshot_id_mismatches,
            )

    row_hash_invalid = 0
    if "_row_sha256" in frame.columns:
        valid_hash = (
            frame["_row_sha256"]
            .fillna("")
            .astype(str)
            .map(lambda value: bool(SHA256_PATTERN.fullmatch(value)))
        )
        row_hash_invalid = int((~valid_hash).sum())
        if row_hash_invalid:
            _issue(
                issues,
                severity="ERROR",
                issue_class="INVALID_ROW_SHA256",
                dataset=dataset,
                count=row_hash_invalid,
            )

    source_row_invalid = 0
    if "_source_row" in frame.columns:
        source_rows = pd.to_numeric(frame["_source_row"], errors="coerce")
        non_integer = source_rows.mod(1).ne(0) & source_rows.notna()
        source_row_invalid = int(
            (source_rows.isna() | source_rows.le(0) | non_integer).sum()
        )
        if source_row_invalid:
            _issue(
                issues,
                severity="ERROR",
                issue_class="INVALID_SOURCE_ROW",
                dataset=dataset,
                count=source_row_invalid,
            )

    date_null_values = 0
    date_parse_failures = 0
    future_date_values = 0
    date_min = ""
    date_max = ""
    for column in DATE_COLUMNS_BY_DATASET[dataset]:
        if column not in frame.columns:
            continue
        metrics = _date_metrics(frame[column], snapshot_date)
        date_null_values += int(metrics["date_null_values"])
        date_parse_failures += int(metrics["date_parse_failures"])
        future_date_values += int(metrics["future_date_values"])
        date_min = str(metrics["date_min"])
        date_max = str(metrics["date_max"])
        for issue_class, metric_name in (
            ("NULL_DATE_VALUE", "date_null_values"),
            ("DATE_PARSE_FAILURE", "date_parse_failures"),
            ("FUTURE_DATE_VALUE", "future_date_values"),
        ):
            count = int(metrics[metric_name])
            if count:
                details = (
                    f"snapshot_date={snapshot_date.isoformat()}"
                    if issue_class == "FUTURE_DATE_VALUE"
                    else ""
                )
                _issue(
                    issues,
                    severity="ERROR",
                    issue_class=issue_class,
                    dataset=dataset,
                    column=column,
                    count=count,
                    details=details,
                )

    numeric_type_failures = 0
    numeric_columns = sorted(
        set(BASE_COLUMNS_BY_DATASET[dataset]).intersection(NUMERIC_HEADERS)
    )
    for column in numeric_columns:
        if column not in frame.columns:
            continue
        failures = _numeric_type_failures(frame[column])
        numeric_type_failures += failures
        if failures:
            _issue(
                issues,
                severity="ERROR",
                issue_class="NUMERIC_TYPE_FAILURE",
                dataset=dataset,
                column=column,
                count=failures,
            )

    duplicate_metrics = _duplicate_metrics(frame)
    if duplicate_metrics["duplicate_flag_inconsistencies"]:
        _issue(
            issues,
            severity="ERROR",
            issue_class="DUPLICATE_FLAG_INCONSISTENCY",
            dataset=dataset,
            count=duplicate_metrics["duplicate_flag_inconsistencies"],
        )

    summary = {
        "dataset": dataset,
        "rows": len(frame),
        "columns": len(frame.columns),
        "source_files": int(frame["_source_path"].nunique())
        if "_source_path" in frame.columns
        else 0,
        "missing_required_columns": len(missing),
        "unexpected_columns": len(unexpected),
        "column_order_mismatch": column_order_mismatch,
        "provenance_null_values": provenance_null_values,
        "provenance_key_duplicate_rows": provenance_key_duplicate_rows,
        "source_file_mismatches": source_file_mismatches,
        "source_level_mismatches": source_level_mismatches,
        "snapshot_id_mismatches": snapshot_id_mismatches,
        "row_hash_invalid": row_hash_invalid,
        "source_row_invalid": source_row_invalid,
        "date_null_values": date_null_values,
        "date_parse_failures": date_parse_failures,
        "future_date_values": future_date_values,
        "numeric_type_failures": numeric_type_failures,
        "date_min": date_min,
        "date_max": date_max,
        **duplicate_metrics,
        "status": "ERROR"
        if any(row["severity"] == "ERROR" for row in issues)
        else "OK",
    }
    return summary, issues


def _load_expected_datasets(
    staging_path: Path,
) -> tuple[dict[str, pd.DataFrame], list[str], list[str]]:
    expected_files = {f"{name}.parquet": name for name in EXPECTED_DATASETS}
    available_files = {path.name for path in staging_path.glob("*.parquet")}
    missing = sorted(set(expected_files).difference(available_files))
    unexpected = sorted(available_files.difference(expected_files))
    datasets = {
        dataset: pd.read_parquet(staging_path / filename)
        for filename, dataset in expected_files.items()
        if filename in available_files
    }
    return datasets, missing, unexpected


def reconcile_manifest(
    manifest: pd.DataFrame,
    datasets: Mapping[str, pd.DataFrame],
) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    """Compara linhas e disposições do manifesto com os Parquets publicados."""
    issues: list[dict[str, object]] = []
    required = {
        "relative_path",
        "dataset",
        "input_rows",
        "output_rows",
        "disposition",
    }
    missing = sorted(required.difference(manifest.columns))
    if missing:
        _issue(
            issues,
            severity="ERROR",
            issue_class="MANIFEST_MISSING_COLUMNS",
            count=len(missing),
            details="|".join(missing),
        )
        return pd.DataFrame(), issues

    manifest_duplicates = int(
        manifest.duplicated(["dataset", "relative_path"], keep=False).sum()
    )
    if manifest_duplicates:
        _issue(
            issues,
            severity="ERROR",
            issue_class="DUPLICATE_MANIFEST_KEY",
            count=manifest_duplicates,
        )

    observed_counts: dict[tuple[str, str], int] = {}
    for dataset, frame in datasets.items():
        if "_source_path" not in frame.columns:
            continue
        counts = frame.groupby("_source_path", dropna=False).size()
        observed_counts.update(
            {(dataset, str(path)): int(count) for path, count in counts.items()}
        )

    manifest_keys = {
        (str(row.dataset), str(row.relative_path))
        for row in manifest.itertuples(index=False)
    }
    unmanifested = sorted(set(observed_counts).difference(manifest_keys))
    for dataset, relative_path in unmanifested:
        _issue(
            issues,
            severity="ERROR",
            issue_class="UNMANIFESTED_SOURCE_PRESENT",
            dataset=dataset,
            count=observed_counts[(dataset, relative_path)],
            details=f"path={relative_path}",
        )

    records: list[dict[str, object]] = []
    for row in manifest.itertuples(index=False):
        dataset = str(row.dataset)
        relative_path = str(row.relative_path)
        manifest_rows = int(row.output_rows)
        staging_rows = observed_counts.get((dataset, relative_path), 0)
        delta = staging_rows - manifest_rows
        disposition = str(row.disposition)
        status = "OK"
        if delta != 0:
            status = "ERROR"
            _issue(
                issues,
                severity="ERROR",
                issue_class="SOURCE_ROW_RECONCILIATION_FAILURE",
                dataset=dataset,
                count=abs(delta),
                details=f"path={relative_path};delta={delta}",
            )
        if disposition != "INCLUDED_IN_STAGING" and staging_rows != 0:
            status = "ERROR"
            _issue(
                issues,
                severity="ERROR",
                issue_class="EXCLUDED_SOURCE_PRESENT_IN_STAGING",
                dataset=dataset,
                count=staging_rows,
                details=f"path={relative_path}",
            )
        records.append(
            {
                "relative_path": relative_path,
                "dataset": dataset,
                "input_rows": int(row.input_rows),
                "manifest_output_rows": manifest_rows,
                "staging_rows": staging_rows,
                "row_delta": delta,
                "disposition": disposition,
                "status": status,
            }
        )

    reconciliation = pd.DataFrame(records)
    if not reconciliation.empty:
        reconciliation = reconciliation.sort_values(
            ["dataset", "relative_path"]
        ).reset_index(drop=True)
    return reconciliation, issues


def _calculated_quality_indicators(
    manifest: pd.DataFrame,
    datasets: Mapping[str, pd.DataFrame],
) -> dict[str, int]:
    federal = datasets.get("federal_transferencias", pd.DataFrame())
    icms = datasets.get("estadual_icms", pd.DataFrame())
    flagged = (
        int(icms["_duplicate_group_id"].notna().sum())
        if "_duplicate_group_id" in icms.columns
        else 0
    )
    return {
        "source_tables_observed": len(manifest),
        "source_rows_observed": int(manifest["input_rows"].sum()),
        "source_files_excluded_from_staging": int(
            manifest["disposition"].ne("INCLUDED_IN_STAGING").sum()
        ),
        "source_rows_excluded_from_staging": int(
            (manifest["input_rows"] - manifest["output_rows"]).sum()
        ),
        "staging_datasets": len(datasets),
        "staging_rows": sum(len(frame) for frame in datasets.values()),
        "federal_source_files_included": int(
            manifest.loc[
                manifest["dataset"].eq("federal_transferencias")
                & manifest["disposition"].eq("INCLUDED_IN_STAGING")
            ].shape[0]
        ),
        "federal_rows": len(federal),
        "icms_rows_retained": len(icms),
        "icms_duplicate_rows_flagged": flagged,
    }


def reconcile_quality_summary(
    quality_summary: pd.DataFrame,
    manifest: pd.DataFrame,
    datasets: Mapping[str, pd.DataFrame],
) -> tuple[pd.DataFrame, list[dict[str, object]]]:
    """Compara os indicadores publicados pelo staging com valores recalculados."""
    issues: list[dict[str, object]] = []
    required = {"indicator", "value", "nature"}
    missing = sorted(required.difference(quality_summary.columns))
    if missing:
        _issue(
            issues,
            severity="ERROR",
            issue_class="QUALITY_SUMMARY_MISSING_COLUMNS",
            count=len(missing),
            details="|".join(missing),
        )
        return pd.DataFrame(), issues

    duplicate_indicators = int(quality_summary["indicator"].duplicated(keep=False).sum())
    if duplicate_indicators:
        _issue(
            issues,
            severity="ERROR",
            issue_class="DUPLICATE_QUALITY_INDICATOR",
            count=duplicate_indicators,
        )

    observed = {
        str(row.indicator): int(row.value)
        for row in quality_summary.itertuples(index=False)
    }
    calculated = _calculated_quality_indicators(manifest, datasets)
    records = []
    for indicator, calculated_value in calculated.items():
        observed_value = observed.get(indicator)
        status = "OK"
        if observed_value is None:
            status = "ERROR"
            _issue(
                issues,
                severity="ERROR",
                issue_class="MISSING_QUALITY_INDICATOR",
                details=indicator,
            )
        elif observed_value != calculated_value:
            status = "ERROR"
            _issue(
                issues,
                severity="ERROR",
                issue_class="QUALITY_INDICATOR_MISMATCH",
                count=abs(observed_value - calculated_value),
                details=(
                    f"indicator={indicator};observed={observed_value};"
                    f"calculated={calculated_value}"
                ),
            )
        records.append(
            {
                "indicator": indicator,
                "published_value": observed_value,
                "calculated_value": calculated_value,
                "delta": None
                if observed_value is None
                else observed_value - calculated_value,
                "status": status,
            }
        )
    return pd.DataFrame(records), issues


def _sum_column(frame: pd.DataFrame, column: str) -> int:
    return int(frame[column].sum()) if column in frame.columns else 0


def build_validation_summary(
    dataset_summary: pd.DataFrame,
    manifest: pd.DataFrame,
    reconciliation: pd.DataFrame,
    quality_reconciliation: pd.DataFrame,
    issues: pd.DataFrame,
    *,
    missing_dataset_files: int,
    unexpected_dataset_files: int,
) -> pd.DataFrame:
    """Produz indicadores agregados e explicita sua natureza."""
    error_count = int(issues["severity"].eq("ERROR").sum()) if not issues.empty else 0
    warning_count = int(issues["severity"].eq("WARNING").sum()) if not issues.empty else 0
    rows_validated = _sum_column(dataset_summary, "rows")
    indicators = [
        ("datasets_expected", len(EXPECTED_DATASETS), "observed"),
        ("datasets_loaded", len(dataset_summary), "observed"),
        ("missing_dataset_files", missing_dataset_files, "calculated"),
        ("unexpected_dataset_files", unexpected_dataset_files, "calculated"),
        ("rows_validated", rows_validated, "calculated"),
        ("source_manifest_rows", len(manifest), "observed"),
        (
            "included_source_tables",
            int(manifest["disposition"].eq("INCLUDED_IN_STAGING").sum()),
            "calculated",
        ),
        (
            "excluded_source_tables",
            int(manifest["disposition"].ne("INCLUDED_IN_STAGING").sum()),
            "calculated",
        ),
        (
            "row_reconciliation_failures",
            int(reconciliation["status"].eq("ERROR").sum())
            if not reconciliation.empty
            else len(manifest),
            "calculated",
        ),
        (
            "quality_indicator_failures",
            int(quality_reconciliation["status"].eq("ERROR").sum())
            if not quality_reconciliation.empty
            else 1,
            "calculated",
        ),
    ]
    for column in (
        "missing_required_columns",
        "unexpected_columns",
        "column_order_mismatch",
        "provenance_null_values",
        "provenance_key_duplicate_rows",
        "source_file_mismatches",
        "source_level_mismatches",
        "snapshot_id_mismatches",
        "row_hash_invalid",
        "source_row_invalid",
        "date_null_values",
        "date_parse_failures",
        "future_date_values",
        "numeric_type_failures",
        "duplicate_flagged_rows",
        "duplicate_groups",
        "duplicate_excess",
        "duplicate_flag_inconsistencies",
    ):
        indicators.append((column, _sum_column(dataset_summary, column), "calculated"))
    indicators.extend(
        [
            ("validation_errors", error_count, "calculated"),
            ("validation_warnings", warning_count, "calculated"),
        ]
    )
    return pd.DataFrame(indicators, columns=["indicator", "value", "nature"])


def validate_staging_directory(staging_path: Path) -> StagingValidationResult:
    """Valida um staging publicado sem modificar seus arquivos."""
    root = staging_path.expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Diretório de staging não encontrado: {root}")

    snapshot_id = root.name
    snapshot_date = snapshot_date_from_id(snapshot_id)
    manifest_path = root / "source_manifest.csv"
    quality_path = root / "staging_quality_summary.csv"
    for required_path in (manifest_path, quality_path):
        if not required_path.is_file():
            raise FileNotFoundError(f"Entrada de staging não encontrada: {required_path}")
    manifest = pd.read_csv(manifest_path)
    quality_summary = pd.read_csv(quality_path)

    datasets, missing_files, unexpected_files = _load_expected_datasets(root)
    issue_records: list[dict[str, object]] = []
    for filename in missing_files:
        _issue(
            issue_records,
            severity="ERROR",
            issue_class="MISSING_DATASET_FILE",
            details=filename,
        )
    for filename in unexpected_files:
        _issue(
            issue_records,
            severity="WARNING",
            issue_class="UNEXPECTED_DATASET_FILE",
            details=filename,
        )

    dataset_records: list[dict[str, object]] = []
    for dataset in EXPECTED_DATASETS:
        if dataset not in datasets:
            continue
        summary, dataset_issues = validate_dataset_frame(
            dataset,
            datasets[dataset],
            snapshot_id=snapshot_id,
            snapshot_date=snapshot_date,
        )
        dataset_records.append(summary)
        issue_records.extend(dataset_issues)

    dataset_summary = pd.DataFrame(dataset_records)
    if not dataset_summary.empty:
        dataset_summary = dataset_summary.sort_values("dataset").reset_index(drop=True)
    reconciliation, reconciliation_issues = reconcile_manifest(manifest, datasets)
    issue_records.extend(reconciliation_issues)
    quality_reconciliation, quality_issues = reconcile_quality_summary(
        quality_summary,
        manifest,
        datasets,
    )
    issue_records.extend(quality_issues)
    issues = pd.DataFrame(
        issue_records,
        columns=["severity", "issue_class", "dataset", "column", "count", "details"],
    )
    validation_summary = build_validation_summary(
        dataset_summary,
        manifest,
        reconciliation,
        quality_reconciliation,
        issues,
        missing_dataset_files=len(missing_files),
        unexpected_dataset_files=len(unexpected_files),
    )
    return StagingValidationResult(
        dataset_summary=dataset_summary,
        manifest_reconciliation=reconciliation,
        quality_reconciliation=quality_reconciliation,
        validation_issues=issues,
        validation_summary=validation_summary,
    )


def write_validation_output(
    result: StagingValidationResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica relatórios de validação de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino de validação já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        result.dataset_summary.to_csv(
            partial / "dataset_validation_summary.csv",
            index=False,
        )
        result.manifest_reconciliation.to_csv(
            partial / "manifest_reconciliation.csv",
            index=False,
        )
        result.quality_reconciliation.to_csv(
            partial / "quality_reconciliation.csv",
            index=False,
        )
        result.validation_issues.to_csv(
            partial / "validation_issues.csv",
            index=False,
        )
        result.validation_summary.to_csv(
            partial / "staging_validation_summary.csv",
            index=False,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.rename(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
