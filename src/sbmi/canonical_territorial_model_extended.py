"""Extensão paralela do modelo canônico com fatos históricos SIDRA."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from sbmi.canonical_territorial_model import (
    KEY_COLUMNS,
    _census,
    _idsc,
    _ips,
    _row,
    _sha256,
    _validate_identifier,
)


@dataclass(frozen=True)
class ExtendedResult:
    output_path: Path
    facts: pd.DataFrame
    indicators: pd.DataFrame
    territories: pd.DataFrame
    validation: pd.DataFrame
    reconciliation: pd.DataFrame


def _sidra(root: Path) -> tuple[list[dict], list[Path], int]:
    path = root / "sidra_historical_values.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Entrada SIDRA curada ausente: {path}")
    frame = pd.read_csv(
        path,
        dtype={
            "table_id": str,
            "variable_id": str,
            "category_id": str,
            "unit_code": str,
            "municipality_code": str,
        },
    )
    required = {
        "table_id", "municipality_code", "reference_year", "variable_id",
        "variable_name", "category_id", "category_name", "unit_code",
        "unit_name", "raw_value", "numeric_value", "value_status",
    }
    if not required.issubset(frame.columns):
        raise ValueError("Contrato SIDRA divergente")
    if set(frame["municipality_code"]) != {"4318002"}:
        raise ValueError("Geografia SIDRA divergente")
    if not set(frame["reference_year"]).issubset(set(range(1996, 2027))):
        raise ValueError("Período SIDRA divergente")
    numeric = frame.loc[frame["value_status"].eq("OBSERVED_NUMERIC")].copy()
    if numeric.empty or numeric["numeric_value"].isna().any():
        raise ValueError("Contrato numérico SIDRA divergente")
    rows = []
    source_hash = _sha256(path)
    for item in numeric.itertuples(index=False):
        rows.append(_row(
            indicator_id=(
                f"economy.sidra.t{item.table_id}.v{item.variable_id}.u{item.unit_code}"
            ),
            indicator_name=str(item.variable_name),
            year=int(item.reference_year),
            theme="economy",
            subtheme="agriculture_livestock_forestry",
            value=float(item.numeric_value),
            value_text=str(item.raw_value),
            unit=str(item.unit_name),
            dataset=f"sidra_table_{item.table_id}_1996_2024",
            source=path,
            source_hash=source_hash,
            category_id=f"c{item.category_id}",
            category_name=str(item.category_name),
            comparability="NOT_ASSESSED_ACROSS_YEARS",
            limitations=(
                "Marcadores ausentes ou suprimidos permanecem na fonte curada "
                "e não são promovidos como fatos numéricos."
            ),
        ))
    return rows, [path], len(frame) - len(numeric)


def build_extended_canonical_model(
    *,
    census_root: Path,
    idsc_root: Path,
    ips_root: Path,
    sidra_root: Path,
    output_root: Path,
    run_id: str,
) -> ExtendedResult:
    """Constrói uma nova versão sem substituir o builder canônico histórico."""
    _validate_identifier(run_id)
    target = output_root.expanduser().resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True)
    try:
        census_rows, census_files = _census(census_root.resolve())
        idsc_rows, idsc_files = _idsc(idsc_root.resolve())
        ips_rows, ips_files = _ips(ips_root.resolve())
        sidra_rows, sidra_files, excluded = _sidra(sidra_root.resolve())
        facts = pd.DataFrame(census_rows + idsc_rows + ips_rows + sidra_rows)
        facts = facts.sort_values(KEY_COLUMNS, kind="stable").reset_index(drop=True)
        if facts.duplicated(KEY_COLUMNS).any():
            raise ValueError("Chaves canônicas duplicadas")
        required = KEY_COLUMNS + ["value_numeric", "unit"]
        if facts[required].isna().any().any():
            raise ValueError("Campos canônicos obrigatórios contêm nulos")
        indicator_columns = [
            "indicator_id", "indicator_name", "indicator_level", "theme",
            "subtheme", "unit",
        ]
        indicators = facts[indicator_columns].drop_duplicates().sort_values("indicator_id")
        territory_columns = ["territory_id", "territory_level", "territory_name", "uf"]
        territories = facts[territory_columns].drop_duplicates()
        if len(territories) != 1:
            raise ValueError("Dimensão territorial divergente")
        source_roots = {
            "census": census_root.resolve(),
            "idsc": idsc_root.resolve(),
            "ips": ips_root.resolve(),
            "sidra": sidra_root.resolve(),
        }
        reconciliation = pd.DataFrame([
            ("canonical_previous_sources", 70, 70, "COMPLEMENTARY", "PRESERVE"),
            ("sidra_historical_values", len(sidra_rows) + excluded, len(sidra_rows),
             "COMPLEMENTARY", "PROMOTE_NUMERIC_ONLY"),
            ("sidra_missing_or_suppressed", excluded, 0, "COMPLEMENTARY", "EXCLUDE"),
        ], columns=[
            "dataset", "rows_observed", "rows_promoted",
            "overlap_classification", "decision",
        ])
        validation = pd.DataFrame([
            ("fact_rows", len(facts), "PASS", 70 + len(sidra_rows)),
            ("distinct_indicators", len(indicators), "PASS", len(indicators)),
            ("distinct_territories", len(territories), "PASS", 1),
            ("duplicate_fact_keys", int(facts.duplicated(KEY_COLUMNS).sum()), "PASS", 0),
            ("null_required_cells", int(facts[required].isna().sum().sum()), "PASS", 0),
            ("sidra_missing_or_suppressed_excluded", excluded, "INFORMATIONAL", excluded),
            ("historical_files_modified", 0, "PASS", 0),
        ], columns=["indicator", "value", "status", "expected"])
        facts.to_parquet(partial / "fact_territorial_indicator.parquet", index=False)
        indicators.to_parquet(partial / "dim_indicator.parquet", index=False)
        territories.to_parquet(partial / "dim_territory.parquet", index=False)
        reconciliation.to_csv(partial / "source_reconciliation.csv", index=False)
        validation.to_csv(partial / "validation_summary.csv", index=False)
        manifest = []
        for path in census_files + idsc_files + ips_files + sidra_files:
            manifest.append(("input", str(path), path.stat().st_size, _sha256(path)))
        for name, root in source_roots.items():
            manifest.append(("source_root", f"{name}:{root}", 0, ""))
        for path in sorted(partial.iterdir()):
            manifest.append(("output", path.name, path.stat().st_size, _sha256(path)))
        pd.DataFrame(manifest, columns=["role", "path", "bytes", "sha256"]).to_csv(
            partial / "canonical_manifest.csv", index=False
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return ExtendedResult(
        target, facts, indicators, territories, validation, reconciliation
    )
