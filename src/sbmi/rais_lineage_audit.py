"""Auditoria de linhagem entre fontes raw/rais e produtos processados."""

from __future__ import annotations

import hashlib
import shutil
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from sbmi.demography_census_comparison import canonical_value, normalize_header


@dataclass(frozen=True)
class RaisLineageAuditResult:
    raw_inventory: pd.DataFrame
    pair_results: pd.DataFrame
    difference_summary: pd.DataFrame
    issues: pd.DataFrame
    summary: pd.DataFrame
    inputs: tuple[Path, ...]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _drop_empty_margins(frame: pd.DataFrame) -> pd.DataFrame:
    return frame.dropna(axis=0, how="all").dropna(axis=1, how="all").reset_index(drop=True)


def _without_decimal_separator(text: str) -> str:
    sign = "-" if text.startswith("-") else ""
    digits = text.lstrip("+-").replace(".", "").lstrip("0") or "0"
    return sign + digits


def _difference_class(raw_value: tuple[str, str], processed_value: tuple[str, str]) -> str:
    if raw_value[0] != "missing" and processed_value[0] == "missing":
        return "RAW_VALUE_LOST"
    if (
        raw_value[0] == "number"
        and processed_value[0] == "number"
        and "." in raw_value[1]
        and _without_decimal_separator(raw_value[1])
        == _without_decimal_separator(processed_value[1])
    ):
        return "DECIMAL_SEPARATOR_LOSS"
    if raw_value[0] == "missing" and processed_value[0] != "missing":
        return "PROCESSED_VALUE_ADDED"
    return "OTHER_VALUE_DIFFERENCE"


def _compare_frames(raw: pd.DataFrame, processed: pd.DataFrame) -> tuple[str, Counter[str]]:
    raw = _drop_empty_margins(raw)
    processed = processed.reset_index(drop=True)
    if raw.shape != processed.shape:
        return "STRUCTURAL_DIFFERENCE", Counter()
    differences: Counter[str] = Counter()
    for column_index, processed_column in enumerate(processed.columns):
        raw_values = raw.iloc[:, column_index].map(canonical_value)
        processed_values = processed[processed_column].map(canonical_value)
        for raw_value, processed_value in zip(raw_values, processed_values, strict=True):
            if raw_value != processed_value:
                differences[_difference_class(raw_value, processed_value)] += 1
    return ("CONTENT_EQUIVALENT" if not differences else "VALUE_DIFFERENCE"), differences


def _csv_pair(raw_path: Path, processed_path: Path) -> tuple[str, Counter[str], int, int]:
    raw = pd.read_csv(raw_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    processed = pd.read_parquet(processed_path)
    raw_headers = [normalize_header(column) for column in raw.columns]
    processed_headers = [normalize_header(column) for column in processed.columns]
    if raw_headers != processed_headers:
        return "STRUCTURAL_DIFFERENCE", Counter(), len(raw), len(processed)
    classification, differences = _compare_frames(raw, processed)
    return classification, differences, len(raw), len(processed)


def audit_rais_lineage(raw_snapshot_root: Path, processed_root: Path) -> RaisLineageAuditResult:
    """Compara fontes capturadas com candidatos processados sem alterar nenhum deles."""
    raw_root = raw_snapshot_root.expanduser().resolve() / "raw" / "rais"
    processed = processed_root.expanduser().resolve()
    raw_files = sorted(path for path in raw_root.iterdir() if path.is_file())
    processed_files = sorted(processed.glob("*.parquet"))
    if not raw_files:
        raise FileNotFoundError(f"Fontes raw/rais ausentes: {raw_root}")
    if not processed_files:
        raise FileNotFoundError(f"Parquets processados ausentes: {processed}")

    inventory_rows = []
    for path in raw_files:
        status = "UNSUPPORTED_DEPENDENCY" if path.suffix.casefold() == ".xls" else "READABLE"
        inventory_rows.append(
            {
                "raw_file": path.name,
                "extension": path.suffix.casefold().lstrip("."),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
                "read_status": status,
                "nature": "observed_and_calculated",
            }
        )

    pair_rows = []
    total_differences: Counter[str] = Counter()
    used_processed: set[Path] = set()
    raw_csv = raw_root / "RAIS SB 2024.csv"
    processed_csv = processed / "RAIS SB 2024.parquet"
    if raw_csv.is_file() and processed_csv.is_file():
        classification, differences, raw_rows, processed_rows = _csv_pair(raw_csv, processed_csv)
        total_differences.update(differences)
        used_processed.add(processed_csv)
        pair_rows.append(
            {
                "raw_file": raw_csv.name,
                "raw_unit": "CSV",
                "processed_file": processed_csv.name,
                "pair_method": "EXACT_DECLARED_PAIR",
                "raw_rows": raw_rows,
                "processed_rows": processed_rows,
                "classification": classification,
                "cell_differences": sum(differences.values()),
                "decision": "LINEAGE_CONTENT_CONFIRMED"
                if classification == "CONTENT_EQUIVALENT"
                else "BLOCK_PROCESSED_PRODUCT",
                "nature": "observed_and_calculated",
            }
        )

    for workbook in sorted(raw_root.glob("*.xlsx")):
        book = pd.ExcelFile(workbook)
        for sheet in book.sheet_names:
            candidate = processed / f"{workbook.stem}_{sheet}.parquet"
            if not candidate.is_file():
                pair_rows.append(
                    {
                        "raw_file": workbook.name,
                        "raw_unit": sheet,
                        "processed_file": "",
                        "pair_method": "FILE_AND_SHEET_NAME_CANDIDATE",
                        "raw_rows": "",
                        "processed_rows": "",
                        "classification": "NO_NOMINAL_CANDIDATE",
                        "cell_differences": "",
                        "decision": "PRESERVE_FOR_FUTURE_REVIEW",
                        "nature": "observed_and_calculated",
                    }
                )
                continue
            raw_frame = _drop_empty_margins(pd.read_excel(workbook, sheet_name=sheet, header=None))
            processed_frame = pd.read_parquet(candidate)
            classification, differences = _compare_frames(raw_frame, processed_frame)
            total_differences.update(differences)
            used_processed.add(candidate)
            pair_rows.append(
                {
                    "raw_file": workbook.name,
                    "raw_unit": sheet,
                    "processed_file": candidate.name,
                    "pair_method": "FILE_AND_SHEET_NAME_CANDIDATE",
                    "raw_rows": len(raw_frame),
                    "processed_rows": len(processed_frame),
                    "classification": classification,
                    "cell_differences": sum(differences.values()),
                    "decision": "LINEAGE_CONTENT_CONFIRMED"
                    if classification == "CONTENT_EQUIVALENT"
                    else "BLOCK_PROCESSED_PRODUCT",
                    "nature": "observed_and_calculated",
                }
            )

    pairs = pd.DataFrame(pair_rows)
    difference_summary = pd.DataFrame(
        [
            {
                "difference_class": name,
                "affected_cells": total_differences.get(name, 0),
                "decision": "BLOCK_PROCESSED_PRODUCT",
                "nature": "calculated",
            }
            for name in (
                "DECIMAL_SEPARATOR_LOSS",
                "RAW_VALUE_LOST",
                "PROCESSED_VALUE_ADDED",
                "OTHER_VALUE_DIFFERENCE",
            )
        ]
    )
    unsupported = sum(row["read_status"] == "UNSUPPORTED_DEPENDENCY" for row in inventory_rows)
    unmatched_processed = len(set(processed_files).difference(used_processed))
    issues = pd.DataFrame(
        [
            (
                "DECIMAL_SEPARATOR_LOSS",
                total_differences["DECIMAL_SEPARATOR_LOSS"],
                "ERROR",
                "DO_NOT_USE_OR_PROMOTE_AFFECTED_PRODUCTS",
            ),
            (
                "RAW_VALUES_LOST",
                total_differences["RAW_VALUE_LOST"],
                "ERROR",
                "DO_NOT_USE_OR_PROMOTE_AFFECTED_PRODUCTS",
            ),
            (
                "UNSUPPORTED_XLS_SOURCES",
                unsupported,
                "NOT_ASSESSED",
                "INSTALL_PINNED_READER_AND_AUDIT_SEPARATELY",
            ),
            (
                "UNMATCHED_PROCESSED_FILES",
                unmatched_processed,
                "NOT_ASSESSED",
                "REQUIRE_EXPLICIT_LINEAGE_MAPPING",
            ),
        ],
        columns=["issue_class", "affected_items", "classification", "decision"],
    )
    issues["nature"] = "observed_calculated_and_recommended"
    classes = pairs["classification"].value_counts()
    summary = pd.DataFrame(
        [
            ("raw_files", len(raw_files), "observed"),
            ("processed_files", len(processed_files), "observed"),
            ("candidate_pairs", int(pairs["processed_file"].ne("").sum()), "calculated"),
            ("content_equivalent_pairs", int(classes.get("CONTENT_EQUIVALENT", 0)), "calculated"),
            ("value_difference_pairs", int(classes.get("VALUE_DIFFERENCE", 0)), "calculated"),
            (
                "structural_difference_pairs",
                int(classes.get("STRUCTURAL_DIFFERENCE", 0)),
                "calculated",
            ),
            (
                "no_nominal_candidate_units",
                int(classes.get("NO_NOMINAL_CANDIDATE", 0)),
                "calculated",
            ),
            (
                "decimal_separator_loss_cells",
                total_differences["DECIMAL_SEPARATOR_LOSS"],
                "calculated",
            ),
            ("raw_value_lost_cells", total_differences["RAW_VALUE_LOST"], "calculated"),
            ("unsupported_xls_files", unsupported, "observed"),
            ("unmatched_processed_files", unmatched_processed, "calculated"),
            ("promotion_allowed", 0, "recommended_decision"),
        ],
        columns=["indicator", "value", "nature"],
    )
    inputs = tuple(raw_files + sorted(used_processed))
    return RaisLineageAuditResult(
        pd.DataFrame(inventory_rows), pairs, difference_summary, issues, summary, inputs
    )


def write_rais_lineage_audit(result: RaisLineageAuditResult, output_dir: Path) -> Path:
    """Publica a auditoria atomicamente, preservando entradas."""
    target = output_dir.expanduser().resolve()
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    try:
        outputs = {
            "rais_raw_inventory.csv": result.raw_inventory,
            "rais_lineage_pairs.csv": result.pair_results,
            "rais_lineage_difference_summary.csv": result.difference_summary,
            "rais_lineage_issues.csv": result.issues,
            "rais_lineage_summary.csv": result.summary,
        }
        for name, frame in outputs.items():
            frame.to_csv(partial / name, index=False)
        manifest = [
            ("input", str(path), path.stat().st_size, _sha256(path)) for path in result.inputs
        ]
        manifest.extend(
            ("output", path.name, path.stat().st_size, _sha256(path))
            for path in sorted(partial.iterdir())
        )
        pd.DataFrame(manifest, columns=["role", "path", "bytes", "sha256"]).to_csv(
            partial / "rais_lineage_manifest.csv", index=False
        )
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
