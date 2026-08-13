"""Curadoria conservadora das séries oficiais DCA de São Borja."""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

REVENUE_ACCOUNTS = {
    "RO1.0.0.0.00.0.0": "Receitas correntes",
    "RO1.1.0.0.00.0.0": "Impostos, taxas e contribuições de melhoria",
    "RO1.2.0.0.00.0.0": "Contribuições",
    "RO1.3.0.0.00.0.0": "Receita patrimonial",
    "RO1.6.0.0.00.0.0": "Receita de serviços",
    "RO1.7.0.0.00.0.0": "Transferências correntes",
    "RO1.9.0.0.00.0.0": "Outras receitas correntes",
    "RO2.0.0.0.00.0.0": "Receitas de capital",
    "RO2.1.0.0.00.0.0": "Operações de crédito",
    "RO2.4.0.0.00.0.0": "Transferências de capital",
    "RO2.9.0.0.00.0.0": "Outras receitas de capital",
}
EXPENSE_ACCOUNTS = {
    "DO3.0.00.00.00.00": "Despesas correntes",
    "DO3.1.00.00.00.00": "Pessoal e encargos sociais",
    "DO3.2.00.00.00.00": "Juros e encargos da dívida",
    "DO3.3.00.00.00.00": "Outras despesas correntes",
    "DO4.0.00.00.00.00": "Despesas de capital",
    "DO4.4.00.00.00.00": "Investimentos",
    "DO4.6.00.00.00.00": "Amortização da dívida",
}
REVENUE_MEASURES = (
    "Receitas Brutas Realizadas",
    "Deduções - FUNDEB",
    "Outras Deduções da Receita",
)
EXPENSE_MEASURES = (
    "Despesas Empenhadas",
    "Despesas Liquidadas",
    "Despesas Pagas",
)


@dataclass(frozen=True)
class DcaSeriesResult:
    values: pd.DataFrame
    coverage: pd.DataFrame
    validation: pd.DataFrame
    paths: dict[str, Path]


def _targets(roots: dict[str, Path], execution_id: str):
    if set(roots) != {"staging", "curated", "exports", "audit"}:
        raise ValueError("Camadas obrigatórias ausentes")
    targets = {}
    for layer, root in roots.items():
        final = root.resolve() / execution_id
        partial = final.with_name(f".{execution_id}.partial")
        if final.exists() or partial.exists():
            raise FileExistsError(final)
        targets[layer] = (final, partial)
    return targets


def curate_siconfi_dca_series(
    snapshot_dir: Path, *, roots: dict[str, Path], execution_id: str
) -> DcaSeriesResult:
    """Publica valores observados e materializa ausências somente na auditoria."""
    manifest = pd.read_csv(snapshot_dir / "manifest.csv")
    required_manifest = {"reference_year", "file", "bytes", "sha256"}
    if not required_manifest.issubset(manifest.columns):
        raise ValueError("Manifesto DCA incompleto")
    if set(manifest["reference_year"]) != set(range(2019, 2026)):
        raise ValueError("Cobertura anual inesperada")
    rows = []
    observed_labels: dict[str, set[str]] = {}
    for item in manifest.itertuples(index=False):
        source_path = (snapshot_dir / str(item.file)).resolve()
        if source_path.parent != snapshot_dir.resolve() or not source_path.is_file():
            raise ValueError(f"Arquivo DCA inválido: {item.file}")
        content = source_path.read_bytes()
        digest = hashlib.sha256(content).hexdigest()
        if len(content) != int(item.bytes) or digest != str(item.sha256).lower():
            raise ValueError(f"Integridade DCA divergente: {item.file}")
        payload = json.loads(content)
        for source in payload["items"]:
            code = source.get("cod_conta")
            column = source.get("coluna")
            if code in REVENUE_ACCOUNTS and column in REVENUE_MEASURES:
                dimension = "revenue"
                label = REVENUE_ACCOUNTS[code]
            elif code in EXPENSE_ACCOUNTS and column in EXPENSE_MEASURES:
                dimension = "expense"
                label = EXPENSE_ACCOUNTS[code]
            else:
                continue
            observed_labels.setdefault(code, set()).add(source["conta"])
            rows.append(
                {
                    "municipality_code": 4318002,
                    "municipality_name": "São Borja",
                    "reference_year": int(source["exercicio"]),
                    "dimension": dimension,
                    "account_code": code,
                    "indicator_name": label,
                    "measure": column,
                    "unit": "R$ correntes",
                    "numeric_value": source["valor"],
                    "nature": "observed",
                    "source_file": item.file,
                }
            )
    if any(len(labels) != 1 for labels in observed_labels.values()):
        raise ValueError("Mudança de rótulo observada")
    values = pd.DataFrame(rows).sort_values(
        ["dimension", "account_code", "measure", "reference_year"]
    )
    keys = ["reference_year", "account_code", "measure"]
    duplicates = int(values.duplicated(keys).sum())
    coverage_rows = []
    observed_keys = set(values[keys].itertuples(index=False, name=None))
    for year in range(2019, 2026):
        for code, label in REVENUE_ACCOUNTS.items():
            for measure in REVENUE_MEASURES:
                coverage_rows.append(
                    (
                        year,
                        "revenue",
                        code,
                        label,
                        measure,
                        "OBSERVED" if (year, code, measure) in observed_keys else "MISSING",
                    )
                )
        for code, label in EXPENSE_ACCOUNTS.items():
            for measure in EXPENSE_MEASURES:
                coverage_rows.append(
                    (
                        year,
                        "expense",
                        code,
                        label,
                        measure,
                        "OBSERVED" if (year, code, measure) in observed_keys else "MISSING",
                    )
                )
    coverage = pd.DataFrame(
        coverage_rows,
        columns=[
            "reference_year",
            "dimension",
            "account_code",
            "indicator_name",
            "measure",
            "status",
        ],
    )
    validation = pd.DataFrame(
        [
            ("rows", len(values), "PASS" if len(values) else "FAIL"),
            (
                "accounts",
                values.account_code.nunique(),
                "PASS" if values.account_code.nunique() == 18 else "FAIL",
            ),
            ("duplicate_keys", duplicates, "PASS" if not duplicates else "FAIL"),
            (
                "years",
                values.reference_year.nunique(),
                "PASS" if values.reference_year.nunique() == 7 else "FAIL",
            ),
            ("missing_combinations", int((coverage.status == "MISSING").sum()), "PASS"),
        ],
        columns=["indicator", "value", "status"],
    )
    if "FAIL" in set(validation.status):
        raise ValueError("Validação DCA falhou")
    targets = _targets(roots, execution_id)
    for _, partial in targets.values():
        partial.mkdir(parents=True)
    try:
        values.to_csv(targets["staging"][1] / "siconfi_dca_series_staging.csv", index=False)
        values.to_csv(targets["curated"][1] / "siconfi_dca_series.csv", index=False)
        values.to_csv(targets["exports"][1] / "siconfi_dca_series.csv", index=False)
        coverage.to_csv(targets["audit"][1] / "coverage.csv", index=False)
        validation.to_csv(targets["audit"][1] / "validation.csv", index=False)
        manifest.to_csv(targets["audit"][1] / "source_manifest.csv", index=False)
        promoted: list[Path] = []
        for final, partial in targets.values():
            final.parent.mkdir(parents=True, exist_ok=True)
            partial.replace(final)
            promoted.append(final)
    except Exception:
        for _, partial in targets.values():
            shutil.rmtree(partial, ignore_errors=True)
        for final in reversed(locals().get("promoted", [])):
            shutil.rmtree(final, ignore_errors=True)
        raise
    return DcaSeriesResult(values, coverage, validation, {k: v[0] for k, v in targets.items()})
