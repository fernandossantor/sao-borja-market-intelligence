"""Curadoria local das séries educacionais de São Borja."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class EducationResult:
    values: pd.DataFrame
    validation: pd.DataFrame
    manifest: pd.DataFrame
    paths: dict[str, Path]


def _target(root: Path, identifier: str) -> tuple[Path, Path]:
    if not identifier or Path(identifier).name != identifier:
        raise ValueError("Identificador inválido")
    target = root.resolve() / identifier
    partial = target.with_name(f".{identifier}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(target)
    return target, partial


def curate_education_series(
    *, sources: dict[str, Path], roots: dict[str, Path], execution_id: str
) -> EducationResult:
    """Normaliza cinco capturas INEP preservadas e publica sem sobrescrever."""
    expected = {"ideb", "rates", "basic_enrollment", "early_enrollment", "higher_education"}
    if set(sources) != expected or set(roots) != {"staging", "curated", "exports", "audit"}:
        raise ValueError("Entradas ou camadas obrigatórias ausentes")
    payloads, manifest_rows = {}, []
    for name, path in sources.items():
        content = path.read_bytes()
        payload = json.loads(content)
        if payload.get("annotations", {}).get("source_name") != "INEP" or not isinstance(
            payload.get("data"), list
        ):
            raise ValueError("Fonte educacional inválida")
        payloads[name] = payload["data"]
        manifest_rows.append(
            {
                "source_id": name,
                "source_file": path.name,
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
                "declared_source": "INEP via Sebrae/Datawheel",
                "nature": "observed",
            }
        )
    rows = []

    def add(year, indicator, label, unit, value, source, category=""):
        rows.append(
            {
                "municipality_code": 4318002,
                "municipality_name": "São Borja",
                "reference_year": int(year),
                "indicator_id": indicator,
                "indicator_name": label,
                "category": category,
                "unit": unit,
                "numeric_value": float(value),
                "nature": "observed",
                "source_id": source,
            }
        )

    for item in payloads["ideb"]:
        level = int(item["Education Level ID"])
        add(
            item["Year"],
            f"ideb_{'early' if level == 1 else 'final'}_years",
            f"IDEB — {item['Education Level']}",
            "índice",
            item["IDEB Index"],
            "ideb",
            item["Education Level"],
        )
    for item in payloads["rates"]:
        slug = "fundamental" if int(item["Education Level ID"]) == 0 else "secondary"
        level = item["Education Level"]
        add(
            item["Year"],
            f"age_grade_distortion_{slug}",
            f"Distorção idade-série — {level}",
            "%",
            item["Age-Grade Distortion Rate"],
            "rates",
            level,
        )
        add(
            item["Year"],
            f"dropout_{slug}",
            f"Abandono escolar — {level}",
            "%",
            item["Dropout Rate"],
            "rates",
            level,
        )
    for item in payloads["basic_enrollment"]:
        add(
            item["Year"],
            "basic_education_enrollments",
            "Matrículas na educação básica",
            "matrículas",
            item["Enrollments"],
            "basic_enrollment",
        )
    for item in payloads["early_enrollment"]:
        add(
            item["Year"],
            "early_childhood_enrollments",
            "Matrículas na educação infantil",
            "matrículas",
            item["Enrollments"],
            "early_enrollment",
        )
    item = payloads["higher_education"][0]
    if int(item.get("Municipality ID", 0)) != 4318002 or int(item.get("Year", 0)) != 2024:
        raise ValueError("Retrato superior divergente")
    for field, indicator, label in (
        ("Enrollments", "higher_education_enrollments", "Matrículas no ensino superior"),
        ("Admissions", "higher_education_admissions", "Ingressantes no ensino superior"),
        ("Graduates", "higher_education_graduates", "Concluintes do ensino superior"),
    ):
        add(2024, indicator, label, "pessoas", item[field], "higher_education")
    values = pd.DataFrame(rows).sort_values(["indicator_id", "reference_year"])
    duplicates = int(values.duplicated(["reference_year", "indicator_id"]).sum())
    validation = pd.DataFrame(
        [
            ("rows", len(values), "calculated", "PASS" if len(values) == 67 else "FAIL"),
            (
                "indicators",
                values.indicator_id.nunique(),
                "calculated",
                "PASS" if values.indicator_id.nunique() == 11 else "FAIL",
            ),
            ("duplicate_keys", duplicates, "calculated", "PASS" if not duplicates else "FAIL"),
            ("minimum_year", values.reference_year.min(), "calculated", "PASS"),
            ("maximum_year", values.reference_year.max(), "calculated", "PASS"),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if "FAIL" in set(validation.status):
        raise ValueError("Validação educacional falhou")
    manifest = pd.DataFrame(manifest_rows)
    targets = {layer: _target(root, execution_id) for layer, root in roots.items()}
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        values.to_csv(targets["staging"][1] / "education_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "education_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "education_series.csv", index=False)
        manifest.to_csv(targets["audit"][1] / "source_manifest.csv", index=False)
        validation.to_csv(targets["audit"][1] / "validation.csv", index=False)
        promoted: list[Path] = []
        for target, partial in targets.values():
            target.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(target)
            promoted.append(target)
    except Exception:
        for _, partial in targets.values():
            shutil.rmtree(partial, ignore_errors=True)
        for target in reversed(locals().get("promoted", [])):
            shutil.rmtree(target, ignore_errors=True)
        raise
    return EducationResult(values, validation, manifest, {k: v[0] for k, v in targets.items()})
