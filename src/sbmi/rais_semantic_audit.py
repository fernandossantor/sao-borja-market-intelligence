"""Auditoria semântica local da família histórica denominada RAIS."""

from __future__ import annotations

import hashlib
import shutil
from collections import defaultdict
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path

import pandas as pd

RAIS_EXPORTS = tuple(
    f"rais_{name}.csv"
    for name in (
        "1735_employment_series",
        "1735_profile",
        "1735_reconstructed_employment",
        "6449_panel",
        "6450_panel",
        "canonical",
        "consolidated",
        "dataset_profile",
        "historical_coverage",
        "semantic_audit",
        "semantic_mapping",
        "sidra_census",
        "timeseries_scan",
    )
)


@dataclass(frozen=True)
class RaisSemanticAuditResult:
    processed_inventory: pd.DataFrame
    export_contracts: pd.DataFrame
    duplicate_groups: pd.DataFrame
    mapping_summary: pd.DataFrame
    issues: pd.DataFrame
    summary: pd.DataFrame
    inputs: tuple[Path, ...]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _role_from_name(name: str) -> str:
    lowered = name.casefold()
    if name == "RAIS SB 2024.parquet":
        return "MICRODATA_CANDIDATE"
    if "layout" in lowered:
        return "LAYOUT_REFERENCE"
    if "_notas" in lowered or "sumário" in lowered:
        return "NOTES_OR_SUMMARY"
    return "TABULAR_PRODUCT_CANDIDATE"


def audit_rais_semantics(
    snapshot_root: Path,
    *,
    current_year: int | None = None,
) -> RaisSemanticAuditResult:
    """Perfila a família sem afirmar autoridade nem promover seus produtos."""
    root = snapshot_root.expanduser().resolve()
    processed_root, exports_root = root / "processed" / "rais", root / "exports"
    parquet_files = sorted(processed_root.glob("*.parquet"))
    export_files = [exports_root / name for name in RAIS_EXPORTS]
    if not parquet_files:
        raise FileNotFoundError(f"Parquets RAIS ausentes: {processed_root}")
    missing = [path.name for path in export_files if not path.is_file()]
    if missing:
        raise FileNotFoundError(f"Exports RAIS ausentes: {missing}")
    reference_year = current_year or datetime.now(UTC).year

    inventory_rows, hash_owners = [], defaultdict(list)
    microdata = None
    for path in parquet_files:
        frame = pd.read_parquet(path)
        digest = _sha256(path)
        hash_owners[digest].append(path)
        if path.name == "RAIS SB 2024.parquet":
            microdata = frame
        schema = hashlib.sha256(
            "\x1f".join(f"{column}:{frame[column].dtype}" for column in frame).encode()
        ).hexdigest()
        inventory_rows.append(
            {
                "file_name": path.name,
                "bytes": path.stat().st_size,
                "rows_observed": len(frame),
                "columns_observed": len(frame.columns),
                "role_hint": _role_from_name(path.name),
                "role_evidence": "FILE_NAME_ONLY",
                "schema_sha256": schema,
                "content_sha256": digest,
                "nature": "observed_and_calculated",
            }
        )
    if microdata is None:
        raise FileNotFoundError("RAIS SB 2024.parquet ausente")

    duplicate_rows = []
    duplicate_items = sorted(
        ((digest, paths) for digest, paths in hash_owners.items() if len(paths) > 1),
        key=lambda item: [path.name for path in item[1]],
    )
    for number, (digest, paths) in enumerate(duplicate_items, start=1):
        duplicate_rows.append(
            {
                "duplicate_group_id": f"rais-exact-{number:03d}",
                "files": "|".join(path.name for path in paths),
                "file_count": len(paths),
                "excess_files": len(paths) - 1,
                "sha256": digest,
                "classification": "EXACT_DUPLICATE",
                "decision": "PRESERVE_AND_REVIEW_SEMANTIC_REDUNDANCY",
                "nature": "calculated",
            }
        )
    duplicates = pd.DataFrame(duplicate_rows)

    contracts = []
    for path in export_files:
        frame = pd.read_csv(path, dtype=str, keep_default_na=False)
        contracts.append(
            {
                "file_name": path.name,
                "bytes": path.stat().st_size,
                "rows_observed": len(frame),
                "columns_observed": len(frame.columns),
                "content_sha256": _sha256(path),
                "authority_status": "NOT_PROVEN",
                "methodology_status": "PENDING_REVIEW",
                "promotion_status": "BLOCKED",
                "nature": "observed_and_recommended",
            }
        )

    mapping = pd.read_csv(exports_root / "rais_semantic_mapping.csv")
    if not {"column_name", "economic_domain"}.issubset(mapping.columns):
        raise ValueError("Contrato divergente em rais_semantic_mapping.csv")
    mapping_summary = (
        mapping["economic_domain"]
        .fillna("<NA>")
        .value_counts(dropna=False)
        .rename_axis("economic_domain")
        .reset_index(name="rows_observed")
    )
    mapping_summary["nature"] = "calculated"
    unmapped = int(mapping["economic_domain"].fillna("").eq("unmapped").sum())
    coverage = pd.read_csv(exports_root / "rais_historical_coverage.csv")
    if "end_year" not in coverage:
        raise ValueError("Contrato divergente em rais_historical_coverage.csv")
    future_rows = int(pd.to_numeric(coverage["end_year"], errors="coerce").gt(reference_year).sum())
    monetary_text = [
        column
        for column in microdata
        if column.startswith("vl_rem_") and not pd.api.types.is_numeric_dtype(microdata[column])
    ]
    duplicate_names = [column for column in microdata if column.endswith("_1")]
    issues = pd.DataFrame(
        [
            (
                "MIXED_FAMILY_CONTENT",
                len(parquet_files),
                "multiple_role_hints_from_file_names",
                "DO_NOT_TREAT_DIRECTORY_NAME_AS_SOURCE_AUTHORITY",
                "observed_and_interpreted",
            ),
            (
                "EXACT_BINARY_DUPLICATES",
                sum(len(paths) for _, paths in duplicate_items),
                f"{len(duplicates)} sha256 groups",
                "PRESERVE_AND_REVIEW_SEMANTIC_REDUNDANCY",
                "calculated_and_recommended",
            ),
            (
                "FUTURE_PERIOD_REQUIRES_REVIEW",
                future_rows,
                f"end_year>{reference_year} in rais_historical_coverage.csv",
                "DO_NOT_TREAT_AS_OBSERVED_PERIOD",
                "observed_and_recommended",
            ),
            (
                "UNMAPPED_SEMANTICS",
                unmapped,
                "economic_domain=unmapped",
                "REVIEW_BEFORE_AGGREGATION",
                "observed_and_calculated",
            ),
            (
                "MONETARY_COLUMNS_AS_TEXT",
                len(monetary_text),
                "|".join(monetary_text),
                "DEFINE_LOCALE_AWARE_DECIMAL_CONVERSION",
                "observed_and_recommended",
            ),
            (
                "DUPLICATED_COLUMN_NAMES_NORMALIZED",
                len(duplicate_names),
                "|".join(duplicate_names),
                "RECOVER_SOURCE_HEADER_MEANING",
                "observed_and_recommended",
            ),
        ],
        columns=["issue_class", "affected_items", "evidence", "decision", "nature"],
    )
    summary = pd.DataFrame(
        [
            ("processed_files", len(parquet_files), "observed"),
            ("processed_rows", sum(row["rows_observed"] for row in inventory_rows), "calculated"),
            ("unique_schemas", len({row["schema_sha256"] for row in inventory_rows}), "calculated"),
            ("exact_duplicate_groups", len(duplicates), "calculated"),
            (
                "exact_duplicate_files",
                sum(len(paths) for _, paths in duplicate_items),
                "calculated",
            ),
            ("rais_export_files", len(export_files), "observed"),
            ("unmapped_semantic_rows", unmapped, "calculated"),
            ("future_period_rows", future_rows, "calculated_diagnostic"),
            ("microdata_rows", len(microdata), "observed"),
            ("microdata_columns", len(microdata.columns), "observed"),
            ("promotion_allowed", 0, "recommended_decision"),
        ],
        columns=["indicator", "value", "nature"],
    )
    return RaisSemanticAuditResult(
        pd.DataFrame(inventory_rows),
        pd.DataFrame(contracts),
        duplicates,
        mapping_summary,
        issues,
        summary,
        tuple(parquet_files + export_files),
    )


def write_rais_semantic_audit(result: RaisSemanticAuditResult, output_dir: Path) -> Path:
    """Publica CSVs atomicamente e recusa sobrescrita."""
    target = output_dir.expanduser().resolve()
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    try:
        outputs = {
            "rais_processed_inventory.csv": result.processed_inventory,
            "rais_export_contracts.csv": result.export_contracts,
            "rais_exact_duplicate_groups.csv": result.duplicate_groups,
            "rais_semantic_mapping_summary.csv": result.mapping_summary,
            "rais_semantic_issues.csv": result.issues,
            "rais_semantic_summary.csv": result.summary,
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
            partial / "rais_semantic_manifest.csv", index=False
        )
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
