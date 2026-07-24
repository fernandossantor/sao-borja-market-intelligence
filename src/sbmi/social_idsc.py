"""Builder portátil do IDSC-BR 2025 para a Base Territorial Comum."""

from __future__ import annotations

import hashlib
import json
import math
import re
import shutil
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

DEFAULT_SHEET_NAME = "Todos os Dados"
DEFAULT_MUNICIPALITY = "São Borja"
OVERALL_SCORE_COLUMN = "Pontuação Indice ODS 2025"
NATIONAL_RANK_COLUMN = "Classificação 2025"
MISSING_VALUES_COLUMN = "Valores faltantes"
MUNICIPALITY_COLUMN = "Município"
GOAL_SCORE_PATTERN = re.compile(r"^Goal\s+(\d+)\s+Score$", re.IGNORECASE)


@dataclass(frozen=True)
class IDSCBuildResult:
    """Produtos e metadados gerados pelo builder."""

    summary: pd.DataFrame
    factsheet: pd.DataFrame
    metadata: dict[str, Any]
    comparison: pd.DataFrame


def normalize_text(value: object) -> str:
    """Normaliza texto para comparação municipal sem perder o valor original."""
    text = unicodedata.normalize("NFKD", str(value or ""))
    text = "".join(character for character in text if not unicodedata.combining(character))
    return " ".join(text.lower().strip().split())


def classify_score(score: float) -> str:
    """Replica a classificação heurística usada no builder histórico."""
    if score >= 80:
        return "excelente"
    if score >= 70:
        return "forte"
    if score >= 50:
        return "intermediario"
    if score >= 30:
        return "fragil"
    return "critico"


def goal_score_columns(columns: pd.Index) -> list[tuple[int, str]]:
    """Identifica e ordena colunas de pontuação dos ODS."""
    identified: list[tuple[int, str]] = []
    for column in columns:
        match = GOAL_SCORE_PATTERN.fullmatch(str(column).strip())
        if match:
            identified.append((int(match.group(1)), str(column)))
    identified.sort(key=lambda item: item[0])
    if not identified:
        raise ValueError("Nenhuma coluna de pontuação ODS foi encontrada.")
    goals = [goal for goal, _column in identified]
    if len(goals) != len(set(goals)):
        raise ValueError(f"Há números de ODS repetidos nas colunas: {goals}")
    return identified


def municipality_row(frame: pd.DataFrame, municipality: str) -> pd.Series:
    """Seleciona exatamente uma linha do município solicitado."""
    if MUNICIPALITY_COLUMN not in frame.columns:
        raise ValueError(f"Coluna obrigatória ausente: {MUNICIPALITY_COLUMN}")
    normalized = frame[MUNICIPALITY_COLUMN].map(normalize_text)
    matched = frame.loc[normalized.eq(normalize_text(municipality))]
    if matched.empty:
        raise ValueError(f"Município não encontrado: {municipality}")
    if len(matched) > 1:
        raise ValueError(
            f"Foram encontradas {len(matched)} linhas para o município {municipality}."
        )
    return matched.iloc[0]


def _required_columns(frame: pd.DataFrame) -> None:
    required = {
        MUNICIPALITY_COLUMN,
        OVERALL_SCORE_COLUMN,
        NATIONAL_RANK_COLUMN,
        MISSING_VALUES_COLUMN,
    }
    missing = sorted(required.difference(frame.columns))
    if missing:
        raise ValueError(f"Colunas obrigatórias ausentes: {missing}")


def _numeric(value: object, label: str) -> float:
    number = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    if pd.isna(number):
        raise ValueError(f"Valor não numérico em {label}: {value!r}")
    return float(number)


def build_summary(frame: pd.DataFrame, row: pd.Series) -> pd.DataFrame:
    """Constrói o ranking municipal dos ODS."""
    records: list[dict[str, object]] = []
    for goal_number, column in goal_score_columns(frame.columns):
        records.append(
            {
                "ods": f"ODS {goal_number}",
                "score": _numeric(row[column], column),
            }
        )
    summary = pd.DataFrame(records).sort_values(
        ["score", "ods"],
        ascending=[False, True],
        kind="stable",
    )
    summary = summary.reset_index(drop=True)
    summary["rank"] = range(1, len(summary) + 1)
    summary["classification"] = summary["score"].map(classify_score)
    return summary[["ods", "score", "rank", "classification"]]


def build_factsheet(row: pd.Series, summary: pd.DataFrame) -> pd.DataFrame:
    """Replica os indicadores sintéticos do factsheet histórico."""
    overall_score = _numeric(row[OVERALL_SCORE_COLUMN], OVERALL_SCORE_COLUMN)
    national_rank = int(_numeric(row[NATIONAL_RANK_COLUMN], NATIONAL_RANK_COLUMN))
    missing_values = int(_numeric(row[MISSING_VALUES_COLUMN], MISSING_VALUES_COLUMN))
    best = summary.iloc[0]
    worst = summary.iloc[-1]
    classification_counts = summary["classification"].value_counts()

    records = [
        ("Pontuação ODS Geral", overall_score),
        ("Ranking Nacional", national_rank),
        ("Valores Faltantes", missing_values),
        ("ODS Mais Forte", best["ods"]),
        ("Score ODS Mais Forte", float(best["score"])),
        ("ODS Mais Fraco", worst["ods"]),
        ("Score ODS Mais Fraco", float(worst["score"])),
        ("ODS Excelentes", int(classification_counts.get("excelente", 0))),
        ("ODS Fortes", int(classification_counts.get("forte", 0))),
        ("ODS Frágeis", int(classification_counts.get("fragil", 0))),
        ("ODS Críticos", int(classification_counts.get("critico", 0))),
    ]
    return pd.DataFrame(records, columns=["indicator", "value"])


def _number_or_none(value: object) -> float | None:
    if value is None or pd.isna(value):
        return None
    text = str(value).strip().replace(",", ".")
    if not re.fullmatch(r"[-+]?\d+(?:\.\d+)?", text):
        return None
    return float(text)


def _equivalent_value(left: object, right: object, tolerance: float = 1e-9) -> bool:
    left_number = _number_or_none(left)
    right_number = _number_or_none(right)
    if left_number is not None and right_number is not None:
        return math.isclose(left_number, right_number, rel_tol=tolerance, abs_tol=tolerance)
    return str(left).strip() == str(right).strip()


def compare_summary(current: pd.DataFrame, historical_path: Path) -> dict[str, object]:
    """Compara o resumo atual com o CSV histórico, sem substituir o baseline."""
    if not historical_path.is_file():
        return {
            "dataset": "summary",
            "historical_path": str(historical_path),
            "status": "MISSING_BASELINE",
            "rows_current": len(current),
            "rows_historical": 0,
            "mismatched_cells": None,
        }
    historical = pd.read_csv(historical_path)
    required = ["ods", "score", "rank", "classification"]
    if any(column not in historical.columns for column in required):
        return {
            "dataset": "summary",
            "historical_path": str(historical_path),
            "status": "BASELINE_SCHEMA_MISMATCH",
            "rows_current": len(current),
            "rows_historical": len(historical),
            "mismatched_cells": None,
        }
    left = current[required].sort_values("rank").reset_index(drop=True)
    right = historical[required].sort_values("rank").reset_index(drop=True)
    mismatches = 0
    if len(left) != len(right):
        mismatches += abs(len(left) - len(right)) * len(required)
    for index in range(min(len(left), len(right))):
        for column in required:
            if not _equivalent_value(left.at[index, column], right.at[index, column]):
                mismatches += 1
    return {
        "dataset": "summary",
        "historical_path": str(historical_path),
        "status": "IDENTICAL" if mismatches == 0 else "DIFFERENT",
        "rows_current": len(left),
        "rows_historical": len(right),
        "mismatched_cells": mismatches,
    }


def compare_factsheet(current: pd.DataFrame, historical_path: Path) -> dict[str, object]:
    """Compara o factsheet por indicador, tratando valores numéricos semanticamente."""
    if not historical_path.is_file():
        return {
            "dataset": "factsheet",
            "historical_path": str(historical_path),
            "status": "MISSING_BASELINE",
            "rows_current": len(current),
            "rows_historical": 0,
            "mismatched_cells": None,
        }
    historical = pd.read_csv(historical_path)
    required = {"indicator", "value"}
    if not required.issubset(historical.columns):
        return {
            "dataset": "factsheet",
            "historical_path": str(historical_path),
            "status": "BASELINE_SCHEMA_MISMATCH",
            "rows_current": len(current),
            "rows_historical": len(historical),
            "mismatched_cells": None,
        }
    left = current.set_index("indicator")["value"]
    right = historical.set_index("indicator")["value"]
    indicators = sorted(set(left.index).union(right.index))
    mismatches = 0
    for indicator in indicators:
        if indicator not in left.index or indicator not in right.index:
            mismatches += 1
        elif not _equivalent_value(left.loc[indicator], right.loc[indicator]):
            mismatches += 1
    return {
        "dataset": "factsheet",
        "historical_path": str(historical_path),
        "status": "IDENTICAL" if mismatches == 0 else "DIFFERENT",
        "rows_current": len(left),
        "rows_historical": len(right),
        "mismatched_cells": mismatches,
    }


def build_idsc(
    source_path: Path,
    *,
    municipality: str = DEFAULT_MUNICIPALITY,
    sheet_name: str = DEFAULT_SHEET_NAME,
    historical_exports_dir: Path | None = None,
) -> IDSCBuildResult:
    """Lê a fonte, produz resumo/factsheet e compara com exportações históricas."""
    source = source_path.expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Fonte IDSC não encontrada: {source}")

    frame = pd.read_excel(source, sheet_name=sheet_name)
    _required_columns(frame)
    row = municipality_row(frame, municipality)
    summary = build_summary(frame, row)
    factsheet = build_factsheet(row, summary)
    source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()

    comparisons: list[dict[str, object]] = []
    if historical_exports_dir is not None:
        baseline = historical_exports_dir.expanduser().resolve()
        comparisons.append(
            compare_summary(summary, baseline / "social_idsc_summary.csv")
        )
        comparisons.append(
            compare_factsheet(factsheet, baseline / "social_idsc_factsheet.csv")
        )
    comparison = pd.DataFrame(
        comparisons,
        columns=[
            "dataset",
            "historical_path",
            "status",
            "rows_current",
            "rows_historical",
            "mismatched_cells",
        ],
    )

    metadata: dict[str, Any] = {
        "dataset": "IDSC-BR 2025",
        "municipality": municipality,
        "geographic_scope": "município",
        "reference_year": 2025,
        "source_file": str(source),
        "source_sheet": sheet_name,
        "source_sha256": source_sha256,
        "source_rows_observed": int(len(frame)),
        "source_columns_observed": int(len(frame.columns)),
        "ods_scores_observed": int(len(summary)),
        "score_unit": "pontuação conforme arquivo de origem",
        "classification_nature": "calculated_project_heuristic",
        "classification_thresholds": {
            "excelente": ">= 80",
            "forte": ">= 70 e < 80",
            "intermediario": ">= 50 e < 70",
            "fragil": ">= 30 e < 50",
            "critico": "< 30",
        },
        "limitations": [
            "A escala e a metodologia oficial do índice não foram revalidadas nesta etapa.",
            "As classes excelente/forte/intermediario/fragil/critico são heurísticas do projeto.",
            "A reprodução do builder histórico não implica validação causal ou substantiva.",
        ],
    }
    return IDSCBuildResult(
        summary=summary,
        factsheet=factsheet,
        metadata=metadata,
        comparison=comparison,
    )


def write_idsc_result(
    result: IDSCBuildResult,
    output_dir: Path,
    *,
    replace: bool = False,
) -> Path:
    """Publica os produtos localmente de modo atômico."""
    target = output_dir.expanduser().resolve()
    if target.exists():
        if not replace:
            raise FileExistsError(f"Destino IDSC já existe: {target}")
        shutil.rmtree(target)
    partial = target.with_name(f".{target.name}.partial")
    if partial.exists():
        shutil.rmtree(partial)
    partial.mkdir(parents=True, exist_ok=False)
    try:
        result.summary.to_csv(partial / "social_idsc_summary.csv", index=False)
        result.factsheet.to_csv(partial / "social_idsc_factsheet.csv", index=False)
        result.comparison.to_csv(partial / "historical_comparison.csv", index=False)
        (partial / "social_idsc_metadata.json").write_text(
            json.dumps(result.metadata, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        partial.replace(target)
    except Exception:
        shutil.rmtree(partial, ignore_errors=True)
        raise
    return target
