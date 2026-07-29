"""Reconstrução incremental de dois produtos censitários com decimais preservados."""

from __future__ import annotations

import hashlib
import math
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DATASETS = {
    "household_composition": {
        "source": "Censo 2022 - Composição domiciliar - São Borja (RS).xlsx",
        "historical": "Censo 2022 - Composição domiciliar - São Borja (RS)_Sheet1.parquet",
        "columns": {
            "Composição domiciliar": "composicao_domiciliar",
            "Porcentagem de domicílios": "porcentagem_de_domicilios",
            "Município": "municipio",
            "Sigla UF": "sigla_uf",
            "Código do Município": "codigo_do_municipio",
        },
        "numeric": ("porcentagem_de_domicilios",),
        "rows": 3,
    },
    "territory": {
        "source": "Censo 2022 - Território - São Borja (RS).xlsx",
        "historical": "Censo 2022 - Território - São Borja (RS)_Sheet1.parquet",
        "columns": {
            "Ano da pesquisa": "ano_da_pesquisa",
            "Área(km²)": "area_km2",
            "Densidade demográfica(hab/km²)": "densidade_demografica_hab_km2",
            "Município": "municipio",
            "Sigla UF": "sigla_uf",
            "Código do Município": "codigo_do_municipio",
        },
        "numeric": ("area_km2", "densidade_demografica_hab_km2"),
        "rows": 1,
    },
}


@dataclass(frozen=True)
class RebuildResult:
    staging_path: Path
    curated_path: Path
    audit_path: Path
    summary: pd.DataFrame
    comparison: pd.DataFrame


def _validate_identifier(identifier: str) -> None:
    if not isinstance(identifier, str) or not identifier.strip():
        raise ValueError("run_id deve ser um identificador não vazio")
    if Path(identifier).name != identifier or identifier in {".", ".."}:
        raise ValueError("run_id deve ser um nome simples")


def _reserve(root: Path, run_id: str) -> tuple[Path, Path]:
    target = root.expanduser().resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True, exist_ok=False)
    return target, partial


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _load_source(path: Path, spec: dict[str, object]) -> pd.DataFrame:
    frame = pd.read_excel(path, sheet_name="Sheet1")
    expected = list(spec["columns"])
    if list(frame.columns) != expected or len(frame) != spec["rows"]:
        raise ValueError(f"Contrato bruto divergente: {path.name}")
    frame = frame.rename(columns=spec["columns"]).copy()
    for column in spec["numeric"]:
        frame[column] = pd.to_numeric(frame[column], errors="raise").astype("float64")
    for column in ("municipio", "sigla_uf"):
        frame[column] = frame[column].astype(str).str.strip()
    if set(frame["codigo_do_municipio"].astype(str)) != {"4318002"}:
        raise ValueError(f"Município divergente: {path.name}")
    if set(frame["municipio"].astype(str)) != {"São Borja"} or set(
        frame["sigla_uf"].astype(str)
    ) != {"RS"}:
        raise ValueError(f"Geografia divergente: {path.name}")
    if "ano_da_pesquisa" in frame and set(frame["ano_da_pesquisa"].astype(int)) != {2022}:
        raise ValueError(f"Período divergente: {path.name}")
    return frame


def _comparison(dataset: str, rebuilt: pd.DataFrame, historical: pd.DataFrame, numeric):
    if list(rebuilt.columns) != list(historical.columns) or len(rebuilt) != len(historical):
        raise ValueError(f"Contrato histórico divergente: {dataset}")
    rows = []
    for row_index in range(len(rebuilt)):
        for column in numeric:
            rebuilt_value = float(rebuilt.iloc[row_index][column])
            historical_value = float(historical.iloc[row_index][column])
            ratio = historical_value / rebuilt_value if rebuilt_value else None
            status = (
                "IDENTICAL"
                if math.isclose(historical_value, rebuilt_value, rel_tol=0, abs_tol=1e-12)
                else "EXPECTED_CHANGE"
            )
            rows.append(
                {
                    "dataset": dataset,
                    "row_index": row_index,
                    "column": column,
                    "historical_value": historical_value,
                    "rebuilt_value": rebuilt_value,
                    "historical_to_rebuilt_ratio": ratio,
                    "classification": status,
                    "justification": (
                        "UNCHANGED"
                        if status == "IDENTICAL"
                        else "TRANSFORMATION_ERROR_CORRECTION_DECIMAL_SCALE"
                    ),
                    "nature": "observed_and_calculated",
                }
            )
    return rows


def rebuild_census_products(
    *,
    source_root: Path,
    historical_root: Path,
    staging_root: Path,
    curated_root: Path,
    audit_root: Path,
    run_id: str,
) -> RebuildResult:
    _validate_identifier(run_id)
    roots = (staging_root, curated_root, audit_root)
    reserved: list[tuple[Path, Path]] = []
    try:
        for root in roots:
            reserved.append(_reserve(root, run_id))
    except Exception:
        for _, partial in reserved:
            shutil.rmtree(partial, ignore_errors=True)
        raise
    (
        (staging_target, staging_partial),
        (curated_target, curated_partial),
        (
            audit_target,
            audit_partial,
        ),
    ) = reserved
    source_root = source_root.expanduser().resolve()
    historical_root = historical_root.expanduser().resolve()
    frames = {}
    comparison_rows = []
    manifest_rows = []
    try:
        for dataset, spec in DATASETS.items():
            source_path = source_root / str(spec["source"])
            historical_path = historical_root / str(spec["historical"])
            if not source_path.is_file() or not historical_path.is_file():
                raise FileNotFoundError(f"Entrada ausente: {dataset}")
            frame = _load_source(source_path, spec)
            historical = pd.read_parquet(historical_path)
            comparison_rows.extend(_comparison(dataset, frame, historical, spec["numeric"]))
            frames[dataset] = frame
            manifest_rows.append(
                {
                    "dataset": dataset,
                    "source_path": str(source_path),
                    "source_sha256": _sha256(source_path),
                    "historical_path": str(historical_path),
                    "historical_sha256": _sha256(historical_path),
                    "rows": len(frame),
                    "nature": "observed_and_calculated",
                }
            )
        comparison = pd.DataFrame(comparison_rows)
        if len(comparison) != 5 or set(comparison["classification"]) != {"EXPECTED_CHANGE"}:
            raise ValueError("Comparação não confirmou as cinco correções esperadas")
        for dataset, frame in frames.items():
            frame.to_parquet(staging_partial / f"{dataset}.parquet", index=False)
            frame.to_parquet(curated_partial / f"{dataset}.parquet", index=False)
        manifest = pd.DataFrame(manifest_rows)
        manifest.to_csv(audit_partial / "census_rebuild_manifest.csv", index=False)
        comparison.to_csv(audit_partial / "census_rebuild_comparison.csv", index=False)
        summary = pd.DataFrame(
            [
                ("datasets_rebuilt", 2, "calculated"),
                ("rows_rebuilt", sum(len(frame) for frame in frames.values()), "calculated"),
                ("corrected_cells", len(comparison), "calculated"),
                ("historical_files_modified", 0, "observed"),
            ],
            columns=["indicator", "value", "nature"],
        )
        summary.to_csv(audit_partial / "census_rebuild_summary.csv", index=False)
        staging_partial.replace(staging_target)
        curated_partial.replace(curated_target)
        audit_partial.replace(audit_target)
    except Exception:
        for _, partial in reserved:
            shutil.rmtree(partial, ignore_errors=True)
        raise
    return RebuildResult(staging_target, curated_target, audit_target, summary, comparison)
