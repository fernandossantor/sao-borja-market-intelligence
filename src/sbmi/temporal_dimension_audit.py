"""Diagnóstico temporal das dimensões existentes no modelo territorial."""

from __future__ import annotations

import shutil
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

DIMENSIONS = {
    "demografia": "Demografia",
    "economia_estrutura_produtiva": "Economia e estrutura produtiva",
    "renda_emprego_trabalho": "Renda, emprego e trabalho",
    "educacao": "Educação",
    "infraestrutura_conectividade": "Infraestrutura e conectividade",
    "financas_publicas_transferencias": "Finanças públicas e transferências",
    "saude_condicoes_sociais": "Saúde e condições sociais",
    "ambiente_politico_regulatorio": "Ambiente político e regulatório",
    "ambiente_sociocultural_territorial": "Ambiente sociocultural e territorial",
    "transversal_multitematico": "Transversal e multitemático",
}
THEME_MAP = {
    "demography": "demografia",
    "economy": "economia_estrutura_produtiva",
    "social": "transversal_multitematico",
}


@dataclass(frozen=True)
class TemporalAuditResult:
    output_path: Path
    coverage: pd.DataFrame
    gaps: pd.DataFrame
    summary: pd.DataFrame


def audit_temporal_dimensions(
    canonical_path: Path,
    output_root: Path,
    run_id: str,
    *,
    start_year: int = 1996,
    end_year: int = 2026,
) -> TemporalAuditResult:
    if Path(run_id).name != run_id or not run_id:
        raise ValueError("run_id deve ser um nome simples")
    if end_year < start_year:
        raise ValueError("Intervalo temporal inválido")
    facts_path = canonical_path.resolve() / "fact_territorial_indicator.parquet"
    if not facts_path.is_file():
        raise FileNotFoundError(f"Fatos canônicos ausentes: {facts_path}")
    facts = pd.read_parquet(facts_path)
    required = {"theme", "reference_year", "indicator_id", "source_dataset"}
    if not required.issubset(facts.columns):
        raise ValueError("Contrato canônico temporal divergente")
    facts = facts.loc[facts["reference_year"].between(start_year, end_year)].copy()
    facts["dimension"] = facts["theme"].map(THEME_MAP)
    unmapped = sorted(set(facts.loc[facts["dimension"].isna(), "theme"]))
    if unmapped:
        raise ValueError(f"Temas canônicos sem dimensão existente: {unmapped}")
    expected = set(range(start_year, end_year + 1))
    coverage_rows = []
    gap_rows = []
    for dimension, label in DIMENSIONS.items():
        subset = facts.loc[facts["dimension"].eq(dimension)]
        years = sorted(set(subset["reference_year"].astype(int)))
        missing = sorted(expected.difference(years))
        coverage_rows.append({
            "dimension": dimension,
            "dimension_label": label,
            "first_year": min(years) if years else None,
            "last_year": max(years) if years else None,
            "years_covered": len(years),
            "target_years": len(expected),
            "fact_rows": len(subset),
            "distinct_indicators": subset["indicator_id"].nunique(),
            "coverage_status": (
                "NO_CANONICAL_EVIDENCE"
                if not years
                else "COMPLETE"
                if not missing
                else "PARTIAL"
            ),
            "nature": "calculated",
        })
        gap_rows.append({
            "dimension": dimension,
            "missing_year_count": len(missing),
            "missing_years": ",".join(map(str, missing)),
            "gap_status": "NONE" if not missing else "TEMPORAL_GAPS_PRESENT",
            "what_cannot_be_concluded": (
                "Ausência no modelo canônico não comprova ausência em fontes "
                "brutas ou externas."
            ),
            "nature": "calculated_diagnostic",
        })
    coverage = pd.DataFrame(coverage_rows)
    gaps = pd.DataFrame(gap_rows)
    summary = pd.DataFrame([
        ("dimensions", len(DIMENSIONS), "calculated"),
        ("dimensions_with_evidence",
         int(coverage["years_covered"].gt(0).sum()), "calculated"),
        ("dimensions_complete", int(coverage["coverage_status"].eq("COMPLETE").sum()),
         "calculated"),
        ("target_start_year", start_year, "observed_parameter"),
        ("target_end_year", end_year, "observed_parameter"),
    ], columns=["indicator", "value", "nature"])
    target = output_root.resolve() / run_id
    partial = target.with_name(f".{target.name}.partial")
    if target.exists() or partial.exists():
        raise FileExistsError(f"Saída existente ou incompleta: {target}")
    partial.mkdir(parents=True)
    try:
        coverage.to_csv(partial / "temporal_dimension_coverage.csv", index=False)
        gaps.to_csv(partial / "temporal_dimension_gaps.csv", index=False)
        summary.to_csv(partial / "temporal_dimension_summary.csv", index=False)
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return TemporalAuditResult(target, coverage, gaps, summary)
