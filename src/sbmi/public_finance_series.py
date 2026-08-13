"""Curadoria conservadora das capturas locais SICONFI de São Borja."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class PublicFinanceResult:
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


def curate_public_finance_series(
    *, sources: dict[str, Path], roots: dict[str, Path], execution_id: str
) -> PublicFinanceResult:
    """Publica apenas níveis explicitamente selecionados, sem somar hierarquias."""
    expected = {
        "revenue_total",
        "capital_expense",
        "current_expense",
        "revenue_categories",
        "transfer_categories",
    }
    if set(sources) != expected or set(roots) != {"staging", "curated", "exports", "audit"}:
        raise ValueError("Entradas ou camadas obrigatórias ausentes")
    payloads, manifest_rows = {}, []
    for name, path in sources.items():
        content = path.read_bytes()
        payload = json.loads(content)
        ann = payload.get("annotations", {})
        if ann.get("source_name") != "SICONFI" or not isinstance(payload.get("data"), list):
            raise ValueError("Captura SICONFI inválida")
        payloads[name] = payload["data"]
        manifest_rows.append(
            {
                "source_id": name,
                "source_file": path.name,
                "bytes": len(content),
                "sha256": hashlib.sha256(content).hexdigest(),
                "declared_source": "Tesouro Nacional/SICONFI via Sebrae/Datawheel",
                "nature": "observed",
            }
        )

    rows = []

    def add(year, indicator, label, value, source, code="", limitation=""):
        rows.append(
            {
                "municipality_code": 4318002,
                "municipality_name": "São Borja",
                "reference_year": int(year),
                "indicator_id": indicator,
                "indicator_name": label,
                "account_code": code,
                "unit": "R$ correntes",
                "numeric_value": float(value),
                "accounting_stage": "não comprovado",
                "nature": "observed",
                "source_id": source,
                "limitation": limitation,
            }
        )

    for x in payloads["revenue_total"]:
        if int(x.get("Municipality ID", 0)) != 4318002:
            raise ValueError("Município divergente")
        add(
            x["Year"],
            "municipal_revenue_excluding_intra_budget",
            "Receita municipal exceto intraorçamentária",
            x["Revenue Value"],
            "revenue_total",
            limitation="Ausência de 2022 na captura; estágio da receita não traduzido.",
        )

    selected = {
        "capital_expense": {
            "DO4.4.00.00.00.00": "Investimentos",
            "DO4.6.00.00.00.00": "Amortização da dívida",
        },
        "current_expense": {
            "DO3.0.00.00.00.00": "Despesas correntes",
            "DO3.1.00.00.00.00": "Pessoal e encargos sociais",
            "DO3.2.00.00.00.00": "Juros e encargos da dívida",
            "DO3.3.00.00.00.00": "Outras despesas correntes",
        },
        "revenue_categories": {
            "RO1.0.0.0.00.0.0": "Receitas correntes",
            "RO1.7.0.0.00.0.0": "Transferências correntes",
            "RO1.9.0.0.00.0.0": "Outras receitas correntes",
        },
        "transfer_categories": {
            "RO1.7.1.0.00.0.0": "Transferências correntes da União",
            "RO1.7.2.4.00.0.0": "Transferências correntes de convênios estaduais",
            "RO1.7.5.0.00.0.0": "Transferências correntes de outras instituições públicas",
            "RO2.4.1.0.00.0.0": "Transferências de capital da União",
            "RO2.4.2.2.00.0.0": "Transferências de capital de convênios estaduais",
        },
    }
    for source, codes in selected.items():
        for x in payloads[source]:
            code = x.get("Expense ID") or x.get("Revenue ID")
            if code in codes:
                value = x.get("Expense Value", x.get("Revenue Value"))
                add(
                    x["Year"],
                    f"siconfi_{code.lower().replace('.', '_')}",
                    codes[code],
                    value,
                    source,
                    code,
                    "Categoria hierárquica observada; não somar com seus pais ou "
                    "filhos. Estágio contábil não traduzido.",
                )
    values = pd.DataFrame(rows).sort_values(["indicator_id", "reference_year"])
    dup = int(values.duplicated(["reference_year", "indicator_id"]).sum())
    validation = pd.DataFrame(
        [
            ("rows", len(values), "calculated", "PASS" if len(values) == 20 else "FAIL"),
            (
                "indicators",
                values.indicator_id.nunique(),
                "calculated",
                "PASS" if values.indicator_id.nunique() == 15 else "FAIL",
            ),
            ("duplicate_keys", dup, "calculated", "PASS" if not dup else "FAIL"),
            ("minimum_year", values.reference_year.min(), "calculated", "PASS"),
            ("maximum_year", values.reference_year.max(), "calculated", "PASS"),
        ],
        columns=["indicator", "value", "nature", "status"],
    )
    if "FAIL" in set(validation.status):
        raise ValueError("Validação fiscal falhou")
    manifest = pd.DataFrame(manifest_rows)
    targets = {layer: _target(root, execution_id) for layer, root in roots.items()}
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        values.to_csv(targets["staging"][1] / "public_finance_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "public_finance_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "public_finance_series.csv", index=False)
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
    return PublicFinanceResult(values, validation, manifest, {k: v[0] for k, v in targets.items()})
