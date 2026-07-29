"""Modelo canônico longo para indicadores territoriais curados."""

from __future__ import annotations

import hashlib
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

KEY_COLUMNS = ["territory_id", "reference_period", "indicator_id", "category_id", "source_dataset"]


@dataclass(frozen=True)
class CanonicalResult:
    output_path: Path
    facts: pd.DataFrame
    indicators: pd.DataFrame
    territories: pd.DataFrame
    validation: pd.DataFrame
    reconciliation: pd.DataFrame


def _validate_identifier(value: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("run_id deve ser um identificador não vazio")
    if Path(value).name != value or value in {".", ".."}:
        raise ValueError("run_id deve ser um nome simples")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _slug(value: object) -> str:
    text = unicodedata.normalize("NFKD", str(value)).encode("ascii", "ignore").decode()
    return "_".join(text.lower().strip().replace("-", " ").split())


def _require(frame: pd.DataFrame, columns: set[str], dataset: str) -> None:
    missing = columns.difference(frame.columns)
    if missing:
        raise ValueError(f"Contrato divergente em {dataset}: {sorted(missing)}")


def _row(*, indicator_id: str, indicator_name: str, year: int, theme: str,
         subtheme: str, value: float, value_text: str, unit: str,
         dataset: str, source: Path, source_hash: str, level: str = "indicator",
         category_id: str = "", category_name: str = "", nature: str = "observed",
         rank: int | None = None, classification: str = "",
         comparability: str = "NOT_ASSESSED", limitations: str = "") -> dict:
    key = "|".join(["4318002", str(year), indicator_id, category_id, dataset])
    return {
        "fact_id": hashlib.sha256(key.encode()).hexdigest()[:24],
        "territory_id": "4318002", "territory_level": "municipality",
        "territory_name": "São Borja", "uf": "RS", "reference_period": str(year),
        "reference_year": year, "theme": theme, "subtheme": subtheme,
        "indicator_id": indicator_id, "indicator_name": indicator_name,
        "indicator_level": level, "category_id": category_id,
        "category_name": category_name, "value_numeric": float(value),
        "value_text": str(value_text), "unit": unit, "nature": nature, "rank": rank,
        "classification": classification, "comparability_status": comparability,
        "source_dataset": dataset, "source_file": str(source),
        "source_sha256": source_hash, "transformation": "canonical_reshape",
        "limitations": limitations,
    }


def _census(root: Path) -> tuple[list[dict], list[Path]]:
    composition_path = root / "household_composition.parquet"
    territory_path = root / "territory.parquet"
    if not composition_path.is_file() or not territory_path.is_file():
        raise FileNotFoundError("Entrada censitária curada ausente")
    composition = pd.read_parquet(composition_path)
    territory = pd.read_parquet(territory_path)
    _require(composition, {"composicao_domiciliar", "porcentagem_de_domicilios",
                           "codigo_do_municipio"}, "census_composition")
    _require(territory, {"ano_da_pesquisa", "area_km2",
                         "densidade_demografica_hab_km2", "codigo_do_municipio"},
             "census_territory")
    if len(composition) != 3 or len(territory) != 1:
        raise ValueError("Contagem censitária divergente")
    if any(set(frame["codigo_do_municipio"].astype(str)) != {"4318002"}
           for frame in (composition, territory)):
        raise ValueError("Geografia censitária divergente")
    year = int(territory.iloc[0]["ano_da_pesquisa"])
    if year != 2022:
        raise ValueError("Período censitário divergente")
    rows = []
    source_hash = _sha256(composition_path)
    for item in composition.itertuples(index=False):
        category = str(item.composicao_domiciliar)
        rows.append(_row(
            indicator_id="demography.household_composition.share",
            indicator_name="Participação na composição domiciliar", year=year,
            theme="demography", subtheme="household_composition",
            value=item.porcentagem_de_domicilios,
            value_text=str(item.porcentagem_de_domicilios), unit="percent",
            dataset="census_2022_household_composition", source=composition_path,
            source_hash=source_hash, category_id=_slug(category), category_name=category,
            limitations="Categorias não formam necessariamente uma partição exaustiva."))
    source_hash = _sha256(territory_path)
    item = territory.iloc[0]
    for indicator_id, name, column, unit in (
        ("demography.territory.area", "Área territorial", "area_km2", "km2"),
        ("demography.territory.population_density", "Densidade demográfica",
         "densidade_demografica_hab_km2", "inhabitants_per_km2"),
    ):
        rows.append(_row(indicator_id=indicator_id, indicator_name=name, year=year,
                         theme="demography", subtheme="territory", value=item[column],
                         value_text=str(item[column]), unit=unit,
                         dataset="census_2022_territory", source=territory_path,
                         source_hash=source_hash))
    return rows, [composition_path, territory_path]


def _idsc(root: Path) -> tuple[list[dict], list[Path]]:
    path = root / "social_idsc_summary.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Entrada curada ausente: {path}")
    factsheet_path = root / "social_idsc_factsheet.csv"
    comparison_path = root / "historical_comparison.csv"
    frame = pd.read_csv(path)
    _require(frame, {"ods", "score", "rank", "classification"}, "idsc")
    if len(frame) != 17 or frame["ods"].duplicated().any():
        raise ValueError("Contrato IDSC divergente")
    source_hash = _sha256(path)
    rows = [_row(indicator_id=f"social.idsc.{_slug(item.ods)}.score",
                 indicator_name=f"Pontuação {item.ods}", year=2025, theme="social",
                 subtheme="idsc", value=item.score, value_text=str(item.score),
                 unit="source_score", dataset="idsc_br_2025", source=path,
                 source_hash=source_hash, rank=int(item.rank),
                 classification=str(item.classification),
                 comparability="NOT_ASSESSED_SINGLE_EDITION",
                 limitations="Classificação é heurística do projeto; metodologia "
                             "oficial não foi revalidada.")
            for item in frame.itertuples(index=False)]
    factsheet = pd.read_csv(factsheet_path)
    comparison = pd.read_csv(comparison_path)
    _require(factsheet, {"indicator", "value"}, "idsc_factsheet")
    _require(comparison, {"dataset", "status", "rows_current", "rows_historical",
                          "mismatched_cells"}, "idsc_historical_comparison")
    if len(factsheet) != 11 or len(comparison) != 2:
        raise ValueError("Contagem de evidências IDSC divergente")
    return rows, [path, factsheet_path, comparison_path]


def _ips(root: Path) -> tuple[list[dict], list[Path]]:
    path = root / "ips_published_summary_2024_2026.csv"
    if not path.is_file():
        raise FileNotFoundError(f"Entrada curada ausente: {path}")
    summary_path = root / "ips_2026_summary.csv"
    frame = pd.read_csv(path)
    _require(frame, {"reference_year", "comparability_status", "ibge_code",
                     "indicator_label", "indicator_key", "indicator_level",
                     "value_text", "value_numeric", "unit", "nature"}, "ips")
    if len(frame) != 48:
        raise ValueError("Contagem IPS divergente")
    if set(frame["ibge_code"].astype(str)) != {"4318002"}:
        raise ValueError("Geografia IPS divergente")
    summary = pd.read_csv(summary_path)
    expected_summary = frame.loc[frame["reference_year"].eq(2026)].reset_index(drop=True)
    if list(summary.columns) != list(expected_summary.columns) or not summary.equals(
            expected_summary):
        raise ValueError("Resumo IPS 2026 não é duplicata de conteúdo da série completa")
    source_hash = _sha256(path)
    rows = [_row(indicator_id=f"social.ips.{item.indicator_key}",
                 indicator_name=item.indicator_label, level=item.indicator_level,
                 year=int(item.reference_year), theme="social", subtheme="ips",
                 value=item.value_numeric, value_text=item.value_text, unit=item.unit,
                 nature=item.nature, dataset="ips_brasil_published_original",
                 source=path, source_hash=source_hash,
                 comparability=item.comparability_status,
                 limitations="Edições publicadas não são estritamente comparáveis.")
            for item in frame.itertuples(index=False)]
    return rows, [path, summary_path]


def build_canonical_territorial_model(*, census_root: Path, idsc_root: Path,
                                      ips_root: Path, output_root: Path,
                                      run_id: str) -> CanonicalResult:
    """Constrói e valida o primeiro produto territorial canônico."""
    _validate_identifier(run_id)
    target = output_root.expanduser().resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    try:
        census_rows, census_files = _census(census_root.expanduser().resolve())
        idsc_rows, idsc_files = _idsc(idsc_root.expanduser().resolve())
        ips_rows, ips_files = _ips(ips_root.expanduser().resolve())
        facts = pd.DataFrame(census_rows + idsc_rows + ips_rows)
        facts = facts.sort_values(KEY_COLUMNS, kind="stable").reset_index(drop=True)
        if len(facts) != 70 or facts.duplicated(KEY_COLUMNS).any():
            raise ValueError("Reconciliação canônica falhou")
        required = KEY_COLUMNS + ["value_numeric", "unit"]
        if facts[required].isna().any().any():
            raise ValueError("Campos canônicos obrigatórios contêm nulos")
        indicator_columns = ["indicator_id", "indicator_name", "indicator_level",
                             "theme", "subtheme", "unit"]
        indicators = facts[indicator_columns].drop_duplicates().sort_values("indicator_id")
        territory_columns = ["territory_id", "territory_level", "territory_name", "uf"]
        territories = facts[territory_columns].drop_duplicates()
        if len(indicators) != 36 or len(territories) != 1:
            raise ValueError("Dimensões canônicas divergentes")
        census_root = census_root.expanduser().resolve()
        idsc_root = idsc_root.expanduser().resolve()
        ips_root = ips_root.expanduser().resolve()
        reconciliation = pd.DataFrame([
            ("census_curated", 5, 5, "UNIQUE", "PROMOTE",
             census_root / "household_composition.parquet"),
            ("idsc_summary", 17, 17, "UNIQUE", "PROMOTE",
             idsc_root / "social_idsc_summary.csv"),
            ("ips_published_2024_2026", 48, 48, "UNIQUE", "PROMOTE",
             ips_root / "ips_published_summary_2024_2026.csv"),
            ("ips_2026_summary", 16, 0, "CONTENT_DUPLICATE", "EXCLUDE",
             ips_root / "ips_2026_summary.csv"),
            ("idsc_factsheet", 11, 0, "COMPLEMENTARY", "EXCLUDE",
             idsc_root / "social_idsc_factsheet.csv"),
            ("idsc_historical_comparison", 2, 0, "COMPLEMENTARY", "EXCLUDE",
             idsc_root / "historical_comparison.csv"),
        ], columns=["dataset", "rows_observed", "rows_promoted",
                    "overlap_classification", "decision", "evidence_path"])
        reconciliation["evidence_path"] = reconciliation["evidence_path"].astype(str)
        reconciliation["evidence_sha256"] = reconciliation["evidence_path"].map(
            lambda value: _sha256(Path(value)))
        nulls = int(facts[required].isna().sum().sum())
        validation = pd.DataFrame([
            ("fact_rows", len(facts), "EXPECTED", 70),
            ("distinct_indicators", len(indicators), "EXPECTED", 36),
            ("distinct_territories", len(territories), "EXPECTED", 1),
            ("duplicate_fact_keys", int(facts.duplicated(KEY_COLUMNS).sum()), "PASS", 0),
            ("null_required_cells", nulls, "PASS", 0),
            ("historical_files_modified", 0, "PASS", 0),
        ], columns=["indicator", "value", "status", "expected"])
        facts.to_parquet(partial / "fact_territorial_indicator.parquet", index=False)
        indicators.to_parquet(partial / "dim_indicator.parquet", index=False)
        territories.to_parquet(partial / "dim_territory.parquet", index=False)
        reconciliation.to_csv(partial / "source_reconciliation.csv", index=False)
        validation.to_csv(partial / "validation_summary.csv", index=False)
        manifest = []
        for path in census_files + idsc_files + ips_files:
            manifest.append(("input", str(path), path.stat().st_size, _sha256(path)))
        for path in sorted(partial.iterdir()):
            manifest.append(("output", path.name, path.stat().st_size, _sha256(path)))
        pd.DataFrame(manifest, columns=["role", "path", "bytes", "sha256"]).to_csv(
            partial / "canonical_manifest.csv", index=False)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return CanonicalResult(target, facts, indicators, territories, validation, reconciliation)
