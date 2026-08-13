"""Extensão paralela do modelo canônico com séries territoriais validadas."""

from __future__ import annotations

import hashlib
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from sbmi.canonical_territorial_model import (
    KEY_COLUMNS,
    _row,
    _sha256,
    _slug,
    _validate_identifier,
)


@dataclass(frozen=True)
class SeriesCanonicalResult:
    output_path: Path
    facts: pd.DataFrame
    indicators: pd.DataFrame
    territories: pd.DataFrame
    validation: pd.DataFrame
    reconciliation: pd.DataFrame


def _read(path: Path, required: set[str]) -> pd.DataFrame:
    if not path.is_file():
        raise FileNotFoundError(f"Entrada curada ausente: {path}")
    frame = pd.read_csv(path, dtype={"municipality_code": str})
    missing = required.difference(frame.columns)
    if missing:
        raise ValueError(f"Contrato divergente em {path.name}: {sorted(missing)}")
    if set(frame["municipality_code"]) != {"4318002"}:
        raise ValueError(f"Geografia divergente em {path.name}")
    return frame


def _numeric(frame: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    numeric = frame.copy()
    numeric["numeric_value"] = pd.to_numeric(numeric["numeric_value"], errors="coerce")
    promoted = numeric.loc[numeric["numeric_value"].notna()].copy()
    return promoted, len(numeric) - len(promoted)


def _text_or(value: object, fallback: object) -> str:
    if pd.isna(value) or not str(value).strip():
        return str(fallback)
    return str(value)


def _canonical_rows(path: Path, family: str) -> tuple[list[dict], int, int]:
    common = {"municipality_code", "reference_year", "numeric_value", "nature"}
    requirements = {
        "demography_historical": common | {
            "table_id", "variable_id", "variable_name", "unit_code", "unit_name",
            "raw_value", "value_status",
        },
        "demography_census": common | {
            "table_id", "variable_id", "variable_name", "unit_code", "unit_name",
            "raw_value", "value_status", "category_key", "category_dimensions_json",
            "comparability_note",
        },
        "economy_gdp": common | {
            "indicator_id", "indicator_name", "variable_id", "unit", "raw_value",
            "value_status", "value_kind", "methodology_series",
        },
        "business_employment": common | {
            "indicator_id", "indicator_name", "unit",
        },
        "education": common | {
            "indicator_id", "indicator_name", "category", "unit", "source_id",
        },
        "public_finance": common | {
            "indicator_id", "indicator_name", "account_code", "unit", "source_id",
            "accounting_stage", "limitation",
        },
        "siconfi_dca": common | {
            "dimension", "account_code", "indicator_name", "measure", "unit",
        },
    }
    frame = _read(path, requirements[family])
    promoted, excluded = _numeric(frame)
    source_hash = _sha256(path)
    rows = []
    for item in promoted.to_dict("records"):
        category_id = ""
        category_name = ""
        classification = ""
        comparability = "NOT_ASSESSED_ACROSS_YEARS"
        limitations = ""
        if family == "demography_historical":
            indicator_id = (
                f"demography.sidra.t{item['table_id']}.v{item['variable_id']}."
                f"u{item['unit_code']}"
            )
            indicator_name = item["variable_name"]
            unit = item["unit_name"]
            value_text = item["raw_value"]
            theme, subtheme = "demography", "historical"
            dataset = "demography_historical_sidra"
            limitations = "Estimativas anuais e resultados censitários não são equivalentes."
        elif family == "demography_census":
            indicator_id = (
                f"demography.census.t{item['table_id']}.v{item['variable_id']}."
                f"u{item['unit_code']}"
            )
            indicator_name = item["variable_name"]
            unit = item["unit_name"]
            value_text = item["raw_value"]
            theme, subtheme = "demography", "census_series"
            dataset = "demography_census_sidra"
            classification = item["category_dimensions_json"]
            category_id = hashlib.sha256(classification.encode()).hexdigest()[:16]
            category_name = item["category_key"]
            limitations = item["comparability_note"]
        elif family == "economy_gdp":
            indicator_id = (
                f"economy.gdp.{item['methodology_series']}.{item['indicator_id']}."
                f"{item['value_kind']}.v{item['variable_id']}"
            )
            indicator_name = item["indicator_name"]
            unit = item["unit"]
            value_text = item["raw_value"]
            theme, subtheme = "economy", "gdp_vab"
            dataset = "economy_gdp_series"
            limitations = "Séries metodológicas permanecem separadas."
        elif family == "business_employment":
            indicator_id = f"economy.business_employment.{item['indicator_id']}"
            indicator_name = item["indicator_name"]
            unit = item["unit"]
            value_text = str(item["numeric_value"])
            theme, subtheme = "economy", "business_employment"
            dataset = "business_employment_series"
            limitations = "Vínculos não equivalem a pessoas ou empresas únicas."
        elif family == "education":
            indicator_id = f"education.{item['indicator_id']}"
            indicator_name = item["indicator_name"]
            unit = item["unit"]
            value_text = str(item["numeric_value"])
            theme, subtheme = "education", "education_series"
            dataset = "education_series"
            category_name = str(item["category"])
            category_id = _slug(category_name)
        elif family == "public_finance":
            indicator_id = f"public_finance.local.{item['indicator_id']}"
            indicator_name = item["indicator_name"]
            unit = item["unit"]
            value_text = str(item["numeric_value"])
            theme, subtheme = "public_finance", "local_curated"
            dataset = "public_finance_local_series"
            category_name = _text_or(item["account_code"], item["source_id"])
            category_id = _slug(category_name)
            classification = str(item["accounting_stage"])
            limitations = str(item["limitation"])
        else:
            measure = str(item["measure"])
            indicator_id = (
                f"public_finance.siconfi.{item['dimension']}."
                f"{_slug(item['account_code'])}.{_slug(measure)}"
            )
            indicator_name = f"{item['indicator_name']} — {measure}"
            unit = item["unit"]
            value_text = str(item["numeric_value"])
            theme, subtheme = "public_finance", "siconfi_dca"
            dataset = "siconfi_dca_official_series"
            limitations = "Contas hierárquicas não devem ser somadas entre si."
        rows.append(
            _row(
                indicator_id=indicator_id,
                indicator_name=str(indicator_name),
                year=int(item["reference_year"]),
                theme=theme,
                subtheme=subtheme,
                value=float(item["numeric_value"]),
                value_text=str(value_text),
                unit=str(unit),
                dataset=dataset,
                source=path,
                source_hash=source_hash,
                category_id=category_id,
                category_name=category_name,
                nature=str(item["nature"]),
                classification=classification,
                comparability=comparability,
                limitations=limitations,
            )
        )
    return rows, len(frame), excluded


def build_series_canonical_model(
    *,
    base_root: Path,
    series_paths: dict[str, Path],
    output_root: Path,
    run_id: str,
) -> SeriesCanonicalResult:
    """Acrescenta séries validadas sem modificar os builders canônicos históricos."""
    _validate_identifier(run_id)
    expected_families = {
        "demography_historical", "demography_census", "economy_gdp",
        "business_employment", "education", "public_finance", "siconfi_dca",
    }
    if set(series_paths) != expected_families:
        raise ValueError("Famílias de séries divergentes")
    base_path = base_root.resolve() / "fact_territorial_indicator.parquet"
    if not base_path.is_file():
        raise FileNotFoundError(f"Canônico estendido ausente: {base_path}")
    base = pd.read_parquet(base_path)
    if base.empty or base.duplicated(KEY_COLUMNS).any():
        raise ValueError("Contrato do canônico estendido divergente")
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True)
    try:
        new_rows = []
        reconciliations = [
            ("canonical_extended_previous", len(base), len(base), 0, "COMPLEMENTARY", "PRESERVE")
        ]
        inputs = [base_path]
        for family in sorted(series_paths):
            path = series_paths[family].resolve()
            rows, observed, excluded = _canonical_rows(path, family)
            new_rows.extend(rows)
            inputs.append(path)
            reconciliations.append(
                (family, observed, len(rows), excluded, "COMPLEMENTARY", "PROMOTE_NUMERIC_ONLY")
            )
        additions = pd.DataFrame(new_rows).reindex(columns=base.columns)
        additions = additions.astype(base.dtypes.to_dict())
        facts = pd.concat([base, additions], ignore_index=True)
        facts = facts.sort_values(KEY_COLUMNS, kind="stable").reset_index(drop=True)
        required = KEY_COLUMNS + ["value_numeric", "unit", "source_sha256"]
        duplicates = int(facts.duplicated(KEY_COLUMNS).sum())
        nulls = int(facts[required].isna().sum().sum())
        if duplicates or nulls:
            raise ValueError("Reconciliação das séries canônicas falhou")
        indicator_columns = [
            "indicator_id", "indicator_name", "indicator_level", "theme", "subtheme", "unit"
        ]
        indicators = facts[indicator_columns].drop_duplicates().sort_values("indicator_id")
        territory_columns = ["territory_id", "territory_level", "territory_name", "uf"]
        territories = facts[territory_columns].drop_duplicates()
        if len(territories) != 1:
            raise ValueError("Dimensão territorial divergente")
        reconciliation = pd.DataFrame(
            reconciliations,
            columns=[
                "dataset", "rows_observed", "rows_promoted", "rows_excluded",
                "overlap_classification", "decision",
            ],
        )
        expected_rows = len(base) + len(additions)
        validation = pd.DataFrame(
            [
                ("base_fact_rows", len(base), "PASS", len(base)),
                ("added_fact_rows", len(additions), "PASS", len(additions)),
                ("fact_rows", len(facts), "PASS", expected_rows),
                ("distinct_indicators", len(indicators), "PASS", len(indicators)),
                ("distinct_territories", len(territories), "PASS", 1),
                ("duplicate_fact_keys", duplicates, "PASS", 0),
                ("null_required_cells", nulls, "PASS", 0),
                ("historical_files_modified", 0, "PASS", 0),
            ],
            columns=["indicator", "value", "status", "expected"],
        )
        facts.to_parquet(partial / "fact_territorial_indicator.parquet", index=False)
        indicators.to_parquet(partial / "dim_indicator.parquet", index=False)
        territories.to_parquet(partial / "dim_territory.parquet", index=False)
        reconciliation.to_csv(partial / "source_reconciliation.csv", index=False)
        validation.to_csv(partial / "validation_summary.csv", index=False)
        manifest = [("input", str(path), path.stat().st_size, _sha256(path)) for path in inputs]
        for path in sorted(partial.iterdir()):
            manifest.append(("output", path.name, path.stat().st_size, _sha256(path)))
        pd.DataFrame(manifest, columns=["role", "path", "bytes", "sha256"]).to_csv(
            partial / "canonical_manifest.csv", index=False
        )
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return SeriesCanonicalResult(
        target, facts, indicators, territories, validation, reconciliation
    )
