"""Curadoria rastreável das séries locais de estabelecimentos e emprego."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

MUNICIPALITY_CODE = 4318002


@dataclass(frozen=True)
class SeriesResult:
    values: pd.DataFrame
    manifest: pd.DataFrame
    validation: pd.DataFrame
    paths: dict[str, Path]


def _target(root: Path, identifier: str) -> tuple[Path, Path]:
    if not identifier or Path(identifier).name != identifier:
        raise ValueError("Identificador inválido")
    target = root.resolve() / identifier
    partial = target.with_name(f".{identifier}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(target)
    return target, partial


def _read(path: Path, expected_table: str) -> tuple[bytes, dict]:
    content = path.read_bytes()
    payload = json.loads(content)
    if payload.get("annotations", {}).get("table") != expected_table:
        raise ValueError("Tabela declarada divergente")
    if not isinstance(payload.get("data"), list):
        raise ValueError("Dados ausentes")
    return content, payload


def curate_business_employment_series(
    *,
    establishments_path: Path,
    workers_path: Path,
    roots: dict[str, Path],
    execution_id: str,
) -> SeriesResult:
    """Normaliza capturas locais e publica novas saídas sem sobrescrever."""
    if set(roots) != {"staging", "curated", "exports", "audit"}:
        raise ValueError("Camadas obrigatórias ausentes")
    targets = {layer: _target(root, execution_id) for layer, root in roots.items()}
    est_bytes, est = _read(establishments_path, "Estabelecimentos")
    worker_bytes, workers = _read(workers_path, "Vinculos")
    rows = []
    for item in est["data"]:
        rows.append(
            {
                "municipality_code": int(item["Municipality ID"]),
                "municipality_name": item["Municipality"],
                "reference_year": int(item["Year"]),
                "indicator_id": "rais_establishments",
                "indicator_name": "Estabelecimentos declarantes na RAIS",
                "unit": "estabelecimentos",
                "numeric_value": float(item["Establishments"]),
                "nature": "observed",
                "source_file": establishments_path.name,
            }
        )
    for item in workers["data"]:
        common = {
            "municipality_code": int(item["Municipality ID"]),
            "municipality_name": item["Municipality"],
            "reference_year": int(item["Year"]),
            "nature": "observed",
            "source_file": workers_path.name,
        }
        rows.extend(
            [
                common
                | {
                    "indicator_id": "rais_formal_jobs",
                    "indicator_name": "Vínculos formais ativos",
                    "unit": "vínculos",
                    "numeric_value": float(item["Workers"]),
                },
                common
                | {
                    "indicator_id": "rais_average_nominal_remuneration",
                    "indicator_name": "Remuneração média nominal",
                    "unit": "reais correntes",
                    "numeric_value": float(item["Remuneration Avg Nominal"]),
                },
            ]
        )
    values = pd.DataFrame(rows).sort_values(["indicator_id", "reference_year"])
    key = ["municipality_code", "reference_year", "indicator_id"]
    duplicates = int(values.duplicated(key).sum())
    years = values.groupby("indicator_id").reference_year.agg(["min", "max", "count"])
    validation = pd.DataFrame(
        [
            ("rows", len(values), "calculated", "PASS"),
            ("duplicate_keys", duplicates, "calculated", "PASS" if not duplicates else "FAIL"),
            (
                "municipality_codes",
                values.municipality_code.nunique(),
                "calculated",
                "PASS" if set(values.municipality_code) == {MUNICIPALITY_CODE} else "FAIL",
            ),
            (
                "indicators",
                values.indicator_id.nunique(),
                "calculated",
                "PASS" if values.indicator_id.nunique() == 3 else "FAIL",
            ),
            (
                "complete_2016_2025",
                int(
                    ((years["min"] == 2016) & (years["max"] == 2025) & (years["count"] == 10)).sum()
                ),
                "calculated",
                "PASS",
            ),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if "FAIL" in set(validation.status) or validation.iloc[-1].value != 3:
        raise ValueError("Validação das séries falhou")
    manifest = pd.DataFrame(
        [
            {
                "source_file": establishments_path.name,
                "bytes": len(est_bytes),
                "sha256": hashlib.sha256(est_bytes).hexdigest(),
                "declared_source": "Ministério do Trabalho/RAIS via Sebrae/Datawheel",
                "nature": "observed",
            },
            {
                "source_file": workers_path.name,
                "bytes": len(worker_bytes),
                "sha256": hashlib.sha256(worker_bytes).hexdigest(),
                "declared_source": "Ministério do Trabalho/RAIS via Sebrae/Datawheel",
                "nature": "observed",
            },
        ]
    )
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        values.to_csv(targets["staging"][1] / "business_employment_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "business_employment_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "business_employment_series.csv", index=False)
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
    return SeriesResult(values, manifest, validation, {k: v[0] for k, v in targets.items()})
